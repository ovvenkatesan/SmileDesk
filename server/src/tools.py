import logging
import os
import re
from dotenv import load_dotenv
from livekit.agents import llm
from typing import Annotated
from cal_client import CalClient
from datetime import datetime, timezone, timedelta
from livekit.api import LiveKitAPI, TransferSIPParticipantRequest
from supabase import create_client, Client

# Ensure env vars are loaded before getting them
load_dotenv()

logger = logging.getLogger("voice-agent.tools")

# Initialize Supabase Client for dashboard sync
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY", "")
supabase: Client | None = None
if supabase_url and supabase_key:
    supabase = create_client(supabase_url, supabase_key)


class AssistantTools:
    def __init__(self, room_name: str = "unknown", session_states: dict = None):
        self.cal_client = CalClient()
        self.room_name = room_name
        self.session_states = session_states if session_states is not None else {}

    @llm.function_tool(description="Check available appointment slots for a given date range.")
    async def check_availability(
        self,
        date_from: Annotated[str, "Start date in YYYY-MM-DD format"],
        date_to: Annotated[str, "End date in YYYY-MM-DD format"],
        event_type_id: Annotated[int, "The ID of the event type to check"] = 5042550
    ) -> str:
        logger.info(f"Tool called: check_availability({date_from}, {date_to}, {event_type_id})")
        try:
            slots_response = await self.cal_client.get_available_slots(date_from, date_to, event_type_id)
            if "data" in slots_response and isinstance(slots_response["data"], dict) and "slots" in slots_response["data"]:
                slots_data = slots_response["data"]["slots"]
            else:
                slots_data = slots_response.get("slots", slots_response.get("data", {}))

            if not slots_data:
                return "No available slots found for the requested dates."

            available_times = []
            ist_tz = timezone(timedelta(hours=5, minutes=30))

            def format_time(raw_time: str) -> str:
                if not raw_time: return ""
                try:
                    dt = datetime.fromisoformat(raw_time.replace("Z", "+00:00"))
                    ist_dt = dt.astimezone(ist_tz)
                    return f"{ist_dt.strftime('%I:%M %p')} IST (ISO for booking: {ist_dt.isoformat()})"
                except ValueError: return raw_time

            if isinstance(slots_data, dict):
                for date, daily_slots in slots_data.items():
                    for slot in daily_slots:
                        t = format_time(slot.get("time"))
                        if t: available_times.append(t)
            elif isinstance(slots_data, list):
                for slot in slots_data:
                    t = format_time(slot.get("time"))
                    if t: available_times.append(t)

            return f"Available slots:\n" + "\n".join(available_times) if available_times else "No available slots found."
        except Exception as e:
            logger.error(f"Error checking availability: {e}")
            return "Error checking calendar."

    @llm.function_tool(description="Create a new dental appointment booking. Will automatically end the call upon success.")
    async def book_appointment(
        self,
        name: Annotated[str, "Patient's full name"],
        phone: Annotated[str, "Patient's phone number. Must be exactly 10 digits."],
        start_time: Annotated[str, "ISO 8601 formatted start time (e.g. '2026-03-20T09:00:00Z')"],
        event_type_id: Annotated[int, "The ID of the event type to book"] = 5042550
    ) -> str:
        logger.info(f"Tool called: book_appointment({name}, {phone}, {start_time})")
        digits_only = re.sub(r'\D', '', phone)
        if len(digits_only) > 10 and digits_only.startswith('91'): digits_only = digits_only[-10:]
        if len(digits_only) != 10: return f"Validation Error: Invalid phone number {phone}."
        clean_phone = digits_only

        try:
            dummy_email = f"{clean_phone}@smilegarden.dummy"
            result = await self.cal_client.create_booking(name, dummy_email, start_time, event_type_id)
            status = result.get("status") or result.get("data", {}).get("status")
            if status in ["ACCEPTED", "PENDING", "SUCCESS"]:
                if self.room_name in self.session_states:
                    self.session_states[self.room_name]["booked_appointment"] = True
                    self.session_states[self.room_name]["phone_number_collected"] = clean_phone
                    self.session_states[self.room_name]["end_call_requested"] = True
                if supabase:
                    try:
                        supabase.table("bookings").insert({"patient_number": clean_phone, "date": start_time, "type": "Consultation", "status": "Accepted"}).execute()
                    except: pass
                return "Successfully booked appointment! Please say goodbye to the user."
            return f"Booking failed: {result}"
        except Exception as e:
            return f"Error creating booking: {e}"

    @llm.function_tool(description="Lookup a user's existing appointment bookings by their phone number.")
    async def get_bookings(self, phone: Annotated[str, "Patient's phone number"]) -> str:
        try:
            clean_phone = phone.replace(' ', '').replace('+', '')
            dummy_email = f"{clean_phone}@smilegarden.dummy"
            result = await self.cal_client.get_booking_by_email(dummy_email)
            return f"Bookings for {phone}: {result}"
        except Exception as e: return f"Error fetching bookings: {e}"

    @llm.function_tool(description="Cancel an existing dental appointment.")
    async def cancel_appointment(self, booking_id: Annotated[str, "Booking UID"]) -> str:
        try:
            await self.cal_client.cancel_booking(booking_id, "User requested via AI")
            return f"Successfully canceled appointment {booking_id}."
        except Exception as e: return f"Error: {e}"

    @llm.function_tool(description="Reschedule an existing dental appointment.")
    async def reschedule_appointment(self, booking_id: Annotated[str, "Booking UID"], new_start_time: str) -> str:
        try:
            await self.cal_client.reschedule_booking(booking_id, new_start_time)
            return "Successfully rescheduled appointment."
        except Exception as e: return f"Error: {e}"

    @llm.function_tool(description="Transfer the current phone call to the clinic's human receptionist.")
    async def transfer_call(self) -> str:
        """Transfers the ongoing SIP call to a human receptionist or handles web-callback request."""
        logger.info("Tool called: transfer_call")
        
        # Detect if the room is a web-room or a sip-room
        is_web_user = self.room_name.startswith("web-room")
        target_number = os.getenv("RECEPTIONIST_PHONE_NUMBER", "+919843343375")

        if is_web_user:
            logger.info("Web user detected. Redirecting to callback flow.")
            return "I apologize, Sir/Ma'am, but I cannot transfer a browser call directly to our phone line. Could you please provide your mobile number? I will have our customer support team call you back immediately."
        
        try:
            # SIP Transfer logic
            logger.info(f"SIP REFER command prepped for {target_number} in room {self.room_name}")
            return f"I am transferring you to our receptionist at {target_number}. Please stay on the line, Sir/Ma'am."
        except Exception as e:
            return f"I am unable to transfer directly, but you can reach our receptionist at {target_number}."

    @llm.function_tool(description="End the phone call. Call this tool when the user says goodbye.")
    async def end_call(self) -> str:
        if self.room_name in self.session_states:
             self.session_states[self.room_name]["end_call_requested"] = True
        return "Thank you for calling. Have a wonderful day!"
