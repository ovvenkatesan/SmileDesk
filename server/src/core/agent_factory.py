# -*- coding: utf-8 -*-
from livekit.agents.voice import Agent
from livekit.plugins import google, elevenlabs, silero
from livekit.agents import llm
import logging

logger = logging.getLogger("cogentxai.core")

class CogentXAIAgent(Agent):
    def __init__(self, 
                 persona_config: dict, 
                 tools: list = None, 
                 chat_ctx: llm.ChatContext | None = None):
        
        # AGGRESSIVE: sub-500ms STT (ElevenLabs Scribe v2)
        stt = elevenlabs.STT(model_id="scribe_v2")

        # MODEL LOCK: gemini-3.1-flash-lite-preview (Ultra Fast)
        llm_model = google.LLM(model=persona_config.get("model", "gemini-3.1-flash-lite-preview"))

        # AGGRESSIVE: TTS Latency tuning
        tts = elevenlabs.TTS(
            model="eleven_turbo_v2_5",
            voice_id=persona_config.get("voice_id", "Nda4CxqYPMJ65wadFnhJ"),
            streaming_latency=1 # AGGRESSIVE: Start streaming almost instantly
        )

        # SUB-500ms VAD TUNING
        vad = silero.VAD.load(
            min_speech_duration=0.1,
            min_silence_duration=0.15 # AGGRESSIVE: Wait only 150ms for user response
        )

        super().__init__(
            instructions=persona_config.get("system_prompt", ""),
            stt=stt,
            llm=llm_model,
            tts=tts,
            vad=vad,
            min_endpointing_delay=0.05, # AGGRESSIVE: LLM starts after 50ms of silence
            max_endpointing_delay=0.5,
            tools=tools or [],
            chat_ctx=chat_ctx
        )
