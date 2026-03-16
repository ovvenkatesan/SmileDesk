from livekit.agents import tts
from livekit.agents.tts import TTSCapabilities
import asyncio
import logging

logger = logging.getLogger("voice-agent.sarvam")

class SarvamTTS(tts.TTS):
    def __init__(self, *, sample_rate: int = 24000, num_channels: int = 1):
        super().__init__(
            capabilities=TTSCapabilities(streaming=False),
            sample_rate=sample_rate,
            num_channels=num_channels,
        )
    
    @property
    def provider(self) -> str:
        return "sarvam"
        
    def synthesize(self, text: str, **kwargs) -> tts.ChunkedStream:
        logger.warning("SarvamTTS.synthesize is a stub and does not produce real audio.")
        # In a real implementation, this would call Sarvam's API and return a ChunkedStream
        # For now we just return a dummy chunked stream to satisfy the type checker.
        return DummyChunkedStream(text, self)

class DummyChunkedStream(tts.ChunkedStream):
    def __init__(self, text: str, tts_instance: tts.TTS):
        super().__init__(tts=tts_instance, input_text=text)
        self._text = text

    async def _main_task(self):
        # Stub implementation doing nothing
        pass
