import asyncio
import base64
import logging
import os
import langid

import aiohttp
from livekit.agents import tts, utils, APIConnectOptions, DEFAULT_API_CONNECT_OPTIONS, APIStatusError, APITimeoutError, APIConnectionError
from livekit.agents.tts import TTSCapabilities

logger = logging.getLogger("voice-agent.sarvam")

class SarvamTTS(tts.TTS):
    def __init__(self, *, sample_rate: int = 24000, num_channels: int = 1, api_key: str | None = None, speaker: str = "kavitha"):
        super().__init__(
            capabilities=TTSCapabilities(streaming=False),
            sample_rate=sample_rate,
            num_channels=num_channels,
        )
        self.api_key = api_key or os.getenv("SARVAM_API_KEY")
        if not self.api_key:
            raise ValueError("SARVAM_API_KEY is required")
        self._speaker = speaker
        self._session = None

    @property
    def provider(self) -> str:
        return "sarvam"
        
    @property
    def model(self) -> str:
        return "bulbul:v3"
        
    def synthesize(self, text: str, *, conn_options: APIConnectOptions = DEFAULT_API_CONNECT_OPTIONS) -> tts.ChunkedStream:
        return SarvamChunkedStream(tts=self, input_text=text, conn_options=conn_options)

    async def aclose(self) -> None:
        if self._session:
            await self._session.close()

    def _ensure_session(self) -> aiohttp.ClientSession:
        if not self._session:
            self._session = aiohttp.ClientSession()
        return self._session


class SarvamChunkedStream(tts.ChunkedStream):
    async def _run(self, output_emitter: tts.AudioEmitter) -> None:
        try:
            # Detect language using langid. If it detects Tamil ('ta'), set target to 'ta-IN', else default to 'en-IN'
            detected_lang, _ = langid.classify(self._input_text)
            target_lang_code = "ta-IN" if detected_lang == "ta" else "en-IN"
            
            logger.info(f"Detected language: {detected_lang}, using TTS target: {target_lang_code}")

            payload = {
                "inputs": [self._input_text],
                "target_language_code": target_lang_code, 
                "speaker": self._tts._speaker,
                "model": self._tts.model,
                "speech_sample_rate": self._tts.sample_rate,
                "enable_preprocessing": True
            }
            
            headers = {
                "api-subscription-key": self._tts.api_key,
                "Content-Type": "application/json"
            }
            
            async with self._tts._ensure_session().post(
                "https://api.sarvam.ai/text-to-speech",
                json=payload,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=30, sock_connect=self._conn_options.timeout),
            ) as resp:
                if resp.status != 200:
                    error_message = await resp.text()
                    raise aiohttp.ClientResponseError(
                        request_info=resp.request_info,
                        history=resp.history,
                        status=resp.status,
                        message=error_message,
                        headers=resp.headers
                    )
                
                data = await resp.json()
                
            if not data or "audios" not in data or not data["audios"]:
                raise Exception("No audio data in response")
                
            audio_base64 = data["audios"][0]
            audio_bytes = base64.b64decode(audio_base64)
            
            # Using audio/wav since Sarvam generally returns a WAV file when base64 decoded
            output_emitter.initialize(
                request_id=utils.shortuuid(),
                sample_rate=self._tts.sample_rate,
                num_channels=self._tts.num_channels,
                mime_type="audio/wav", 
            )
            
            output_emitter.push(audio_bytes)
            output_emitter.flush()

        except asyncio.TimeoutError:
            raise APITimeoutError() from None
        except aiohttp.ClientResponseError as e:
            raise APIStatusError(
                message=e.message, status_code=e.status, request_id=None, body=None
            ) from None
        except Exception as e:
            raise APIConnectionError() from e
