# -*- coding: utf-8 -*-
from livekit.agents.voice import Agent
from livekit.plugins import google, elevenlabs, silero
from livekit.agents import llm
from tools import AssistantTools
from datetime import datetime, timezone, timedelta
import logging

logger = logging.getLogger("voice-agent.unified")

def get_system_prompt(caller_id: str) -> str:
    ist_tz = timezone(timedelta(hours=5, minutes=30))
    current_time_ist = datetime.now(ist_tz)
    current_date_str = current_time_ist.strftime("%A, %B %d, %Y")
    current_time_str = current_time_ist.strftime("%I:%M %p")

    greeting_instruction = f"The caller's phone number is detected as {caller_id}." if caller_id and caller_id != "unknown" else "The caller's phone number is unknown."

    return f"""You are Pallavi, the AI Front Desk for Smile Garden Dental Care. 
Professional and Extremely Respectful. Persona: 'Akka'.

**PRONUNCIATION (NO DIGITS):**
NEVER use digits (0-9). Spell out all numbers/times in Tamil script.
- 11:00 AM -> ???? ????????? ???????.

**RESPECT:**
Treat all as elders. Use '?????????', '???????????'. Address as "Sir" or "Ma'am".

**LANGUAGE LOCK:**
Only Tamil and English. If you hear Telugu/Malayalam, assume it is Tamil and respond in Tamil.

**BOOKING:**
Event ID: 5042550. Clinic in IST.

**OPERATIONAL:**
Be very brief (1-2 sentences). Respond instantly.
Today is {current_date_str}, {current_time_str} IST. {greeting_instruction}
"""

class UnifiedAgent(Agent):
    def __init__(self, caller_id: str = "unknown", room_name: str = "unknown", chat_ctx: llm.ChatContext | None = None, session_states: dict = None):
        stt = elevenlabs.STT(model_id="scribe_v2")
        
        # MODEL LOCK: gemini-3.1-flash-lite-preview (Ultra Fast)
        llm_model = google.LLM(model="gemini-3.1-flash-lite-preview")

        tts = elevenlabs.TTS(
            model="eleven_turbo_v2_5",
            voice_id="Nda4CxqYPMJ65wadFnhJ", # Harini
            streaming_latency=1 # AGGRESSIVE: Minimum buffer
        )

        tools_instance = AssistantTools(room_name=room_name, session_states=session_states)
        
        # SUB-500ms TUNING
        vad = silero.VAD.load(
            min_speech_duration=0.1,
            min_silence_duration=0.15 # AGGRESSIVE: Wait only 150ms of silence
        )

        super().__init__(
            instructions=get_system_prompt(caller_id),
            stt=stt,
            llm=llm_model,
            tts=tts,
            vad=vad,
            min_endpointing_delay=0.05, # SUB-500ms TARGET: Start LLM after 50ms
            max_endpointing_delay=0.5,
             # Thinking while the user is talking
            tools=[
                tools_instance.check_availability,
                tools_instance.book_appointment,
                tools_instance.get_bookings,
                tools_instance.cancel_appointment,
                tools_instance.reschedule_appointment,
                tools_instance.transfer_call,
                tools_instance.end_call
            ],
            chat_ctx=chat_ctx
        )
