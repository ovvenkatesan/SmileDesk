from livekit.agents.voice import Agent as VoiceAgent
from livekit.plugins import deepgram, google
from sarvam_tts import SarvamTTS
import logging

logger = logging.getLogger("voice-agent")

SYSTEM_PROMPT = """You are the Smile Garden Voice AI Agent, adopting the persona of a 'Warm and Familiar Neighborhood Nurse'. 
You are empathetic, reassuring, highly competent, and grounded. 
Never sound robotic or overly technical. 
Acknowledge patient anxieties and provide a frictionless path to booking an emergency slot or finding information.
"""

def create_agent() -> VoiceAgent:
    """Creates and configures the Voice Pipeline Agent."""
    
    stt = deepgram.STT()
    llm = google.LLM(model="gemini-2.0-flash-001") # Configure with appropriate gemini model
    tts = SarvamTTS()

    agent = VoiceAgent(
        stt=stt,
        llm=llm,
        tts=tts,
        instructions=SYSTEM_PROMPT
    )
    
    @agent.on("user_started_speaking")
    def _on_user_started_speaking():
        logger.info("User started speaking...")

    @agent.on("user_stopped_speaking")
    def _on_user_stopped_speaking():
        logger.info("User stopped speaking. Processing intent...")

    @agent.on("agent_started_speaking")
    def _on_agent_started_speaking():
        logger.info("Agent started speaking...")

    @agent.on("agent_stopped_speaking")
    def _on_agent_stopped_speaking():
        logger.info("Agent stopped speaking.")
        
    return agent
