from livekit.agents.voice import Agent, AgentSession
from livekit.plugins import deepgram, google
from sarvam_tts import SarvamTTS
import logging

logger = logging.getLogger("voice-agent")

SYSTEM_PROMPT = """You are the Smile Garden Voice AI Agent, adopting the persona of a 'Warm and Familiar Neighborhood Nurse'. 
You are empathetic, reassuring, highly competent, and grounded. 
Never sound robotic or overly technical. 
Acknowledge patient anxieties and provide a frictionless path to booking an emergency slot or finding information.
"""

def create_agent() -> tuple[Agent, AgentSession]:
    """Creates and configures the Voice Pipeline Agent and Session."""
    
    stt = deepgram.STT()
    llm = google.LLM(model="gemini-2.5-flash") # Configure with appropriate gemini model
    tts = SarvamTTS()

    agent = Agent(
        instructions=SYSTEM_PROMPT
    )
    
    session = AgentSession(
        stt=stt,
        llm=llm,
        tts=tts
    )
    
    @session.on("user_state_changed")
    def _on_user_state_changed(state):
        if state == "speaking":
            logger.info("User started speaking...")
        elif state == "listening":
            logger.info("User stopped speaking. Processing intent...")

    @session.on("agent_state_changed")
    def _on_agent_state_changed(state):
        if state == "speaking":
            logger.info("Agent started speaking...")
        elif state == "listening":
            logger.info("Agent stopped speaking.")
        
    return agent, session
