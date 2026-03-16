from livekit.agents.voice import Agent, AgentSession
from livekit.plugins import deepgram, google
from sarvam_tts import SarvamTTS
from tools import AssistantTools
import logging

logger = logging.getLogger("voice-agent")

SYSTEM_PROMPT = """You are Pallavi, the Smile Garden Voice AI Agent. You adopt the persona of a 'Warm and Familiar Neighborhood Nurse'. 
You are empathetic, reassuring, highly competent, and grounded. 
Never sound robotic or overly technical. 
Acknowledge patient anxieties and provide a frictionless path to booking an emergency slot or finding information.

When a patient asks to book an appointment, check the available slots using `check_availability` first, then offer a time. Once they confirm, use `book_appointment` to finalize it.

When a patient wants to cancel or reschedule, ask for their email address to locate their booking using `get_bookings`. Once you locate the correct booking ID, confirm the details with them.
For cancellations, use `cancel_appointment` with an appropriate reason. 
For rescheduling, find a new available slot using `check_availability`, confirm the new time, and then use `reschedule_appointment` to move the appointment.
"""

def create_agent() -> tuple[Agent, AgentSession]:
    """Creates and configures the Voice Pipeline Agent and Session."""
    
    stt = deepgram.STT()
    llm = google.LLM(model="gemini-2.5-flash") # Configure with appropriate gemini model
    tts = SarvamTTS()
    tools = AssistantTools()

    agent = Agent(
        instructions=SYSTEM_PROMPT,
        tools=[
            tools.check_availability,
            tools.book_appointment,
            tools.get_bookings,
            tools.cancel_appointment,
            tools.reschedule_appointment
        ]
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
