from livekit.agents.voice import Agent
from livekit.plugins import deepgram, google
from livekit.agents import llm
from sarvam_tts import SarvamTTS
from tools import AssistantTools
from datetime import datetime, timezone
import logging

logger = logging.getLogger("voice-agent.english")

def get_english_prompt() -> str:
    current_date = datetime.now(timezone.utc).astimezone().strftime("%A, %B %d, %Y")
    
    return f"""You are Pallavi, the Smile Garden Voice AI Agent. You adopt the persona of a 'Warm and Familiar Neighborhood Nurse'. 
You are empathetic, reassuring, highly competent, and grounded. 
Never sound robotic or overly technical. 
Acknowledge patient anxieties and provide a frictionless path to booking an emergency slot or finding information.

You are currently speaking to the patient in English. Reply EXCLUSIVELY in English. Do NOT use Tamil.

Today's date is {current_date}. 
When checking for availability or booking an appointment, you MUST ALWAYS use the event_type_id: 5042550 (which represents a standard 30-minute dental consultation). Do not invent or guess another ID.

When a patient asks to book an appointment, check the available slots using `check_availability` first, then offer a time. Once they confirm, ask for their full name and phone number (not email). Then use `book_appointment` to finalize it.

When a patient wants to cancel or reschedule, ask for their email address to locate their booking using `get_bookings`. Once you locate the correct booking ID, confirm the details with them.
For cancellations, use `cancel_appointment` with an appropriate reason.
For rescheduling, find a new available slot using `check_availability`, confirm the new time, and then use `reschedule_appointment` to move the appointment.
"""

class EnglishAgent(Agent):
    def __init__(self, chat_ctx: llm.ChatContext | None = None):
        stt = deepgram.STT(language="en-US") # English STT for English Agent
        llm_model = google.LLM(model="gemini-3.1-flash-lite-preview")
        tts = deepgram.TTS(model="aura-2-asteria-en") # English female voice
        tools_instance = AssistantTools()
        
        super().__init__(
            instructions=get_english_prompt(),
            stt=stt,
            llm=llm_model,
            tts=tts,
            tools=[
                tools_instance.check_availability,
                tools_instance.book_appointment,
                tools_instance.get_bookings,
                tools_instance.cancel_appointment,
                tools_instance.reschedule_appointment
            ],
            chat_ctx=chat_ctx
        )
