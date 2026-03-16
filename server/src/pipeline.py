from livekit.agents.voice import Agent as VoiceAgent
from livekit.plugins import deepgram, google
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

    agent = VoiceAgent(
        stt=stt,
        llm=llm,
        instructions=SYSTEM_PROMPT
    )
    
    return agent
