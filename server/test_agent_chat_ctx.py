from livekit.agents.voice import Agent
from livekit.plugins import google, elevenlabs, deepgram, silero
from livekit.agents import llm

a = Agent(
    instructions="hi",
    stt=deepgram.STT(vad_events=False),
    llm=google.LLM(),
    tts=elevenlabs.TTS(),
    vad=silero.VAD.load()
)
print("chat_ctx value:", a.chat_ctx)
