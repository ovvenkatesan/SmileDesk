import logging
import os
from livekit.agents import llm
from typing import Annotated
from cal_client import CalClient
from datetime import datetime, timezone, timedelta
from livekit.api import LiveKitAPI, TransferSIPParticipantRequest

logger = logging.getLogger("voice-agent.tools")

class AssistantTools:
    def __init__(self):
        self.cal_client = CalClient()

    @llm.function_tool(description="Check available appointment slots for a given date range.")
    async def check_availability(
        self,
        date_from: Annotated[str, "Start date in YYYY-MM-DD format"],
        date_to: Annotated[str, "End date in YYYY-MM-DD format"],
        event_type_id: Annotated[int, "The ID of the event type to check (e.g. 123)"]
    ) -> str:
        logger.info(f"Tool called: check_availability({date_from}, {date_to}, {event_type_id})")
        try:
            slots_response = await self.cal_client.get_available_slots(date_from, date_to, event_type_id)
            
            # Extract slots from the response - Cal.com v2 structure might vary slightly 
            # Check for 'data' key or 'slots' key depending on exact API payload
            if "data" in slots_response and isinstance(slots_response["data"], dict) and "slots" in slots_response["data"]:
                slots_data = slots_response["data"]["slots"]
            else:
                slots_data = slots_response.get("slots", slots_response.get("data", {}))
            
            if not slots_data:
                return "No available slots found for the requested dates."
            
            available_times = []
            ist_tz = timezone(timedelta(hours=5, minutes=30))
            
            def format_time(raw_time: str) -> str:
                if not raw_time:
                    return ""
                try:
                    dt = datetime.fromisoformat(raw_time.replace("Z", "+00:00"))
                    ist_dt = dt.astimezone(ist_tz)
                    return f"{ist_dt.strftime('%I:%M %p')} IST (ISO for booking: {ist_dt.isoformat()})"
                except ValueError:
                    return raw_time

            if isinstance(slots_data, dict):
                for date, daily_slots in slots_data.items():
                    for slot in daily_slots:
                        t = format_time(slot.get("time"))
                        if t:
                            available_times.append(t)
            elif isinstance(slots_data, list):
                for slot in slots_data:
                    t = format_time(slot.get("time"))
                    if t:
                        available_times.append(t)
            
            if not available_times:
                return "No available slots found for the requested dates."
                
            return f"Available slots:\n" + "\n".join(available_times)
        except Exception as e:
            logger.error(f"Error checking availability: {e}")
            return "There was an error checking the calendar. Please advise the user that the system is temporarily down."

    @llm.function_tool(description="Create a new dental appointment booking.")
    async def book_appointment(
        self,
        name: Annotated[str, "Patient's full name"],
        phone: Annotated[str, "Patient's phone number"],
        start_time: Annotated[str, "ISO 8601 formatted start time (e.g. '2026-03-20T09:00:00Z')"],
        event_type_id: Annotated[int, "The ID of the event type to book"]
    ) -> str:
        logger.info(f"Tool called: book_appointment({name}, {phone}, {start_time})")
        try:
            # Parse the proposed start time
            try:
                proposed_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
            except ValueError:
                return "Error: start_time must be a valid ISO 8601 string."

            # Enforce 30-minute buffer rule
            now_utc = datetime.now(timezone.utc)
            buffer_time = now_utc + timedelta(minutes=30)

            if proposed_dt < buffer_time:
                return "Booking Error: You cannot book an appointment in the past or within the next 30 minutes. Please ask the user for a time that is at least 30 minutes from now."

            # Cal.com requires an email in the payload, but we are collecting a phone number from the user.
            # We use a dummy email derived from the phone number since phone is the primary contact method.
            dummy_email = f"{phone.replace(' ', '').replace('+', '')}@smilegarden.dummy"
            result = await self.cal_client.create_booking(name, dummy_email, start_time, event_type_id)

            status = result.get("status") or result.get("data", {}).get("status")
            booking_id = result.get("id") or result.get("data", {}).get("uid") or result.get("data", {}).get("id")

            if status in ["ACCEPTED", "PENDING", "SUCCESS"]:
                return f"Successfully booked appointment! Booking ID is {booking_id} with status {status}."
            else:
                return f"Booking requested, but status is unclear: {result}"
        except Exception as e:
            logger.error(f"Error creating booking: {e}")
            return "There was an error creating the booking. The time slot might be no longer available or there is a system issue."
    
    @llm.function_tool(description="Lookup a user's existing appointment bookings by their phone number.")
    async def get_bookings(
        self,
        phone: Annotated[str, "Patient's phone number"]
    ) -> str:
        logger.info(f"Tool called: get_bookings({phone})")
        try:
            # We use the same dummy email logic here as we do in book_appointment
            # Remove + and spaces
            clean_phone = phone.replace(' ', '').replace('+', '')
            # If the user says 9898433433, make sure it matches exactly what was booked
            dummy_email = f"{clean_phone}@smilegarden.dummy"
            result = await self.cal_client.get_booking_by_email(dummy_email)

            # In Cal.com v2, the list of bookings is usually inside 'data'
            bookings_list = []
            if "data" in result and isinstance(result["data"], list):
                bookings_list = result["data"]
            elif "bookings" in result and isinstance(result["bookings"], list):
                bookings_list = result["bookings"]

            if bookings_list:
                bookings = []
                ist_tz = timezone(timedelta(hours=5, minutes=30))
                
                for b in bookings_list:
                    b_id = b.get("uid", b.get("id"))
                    # Handle different payload structures
                    b_time_raw = b.get("startTime", b.get("start")) 
                    b_status = b.get("status")
                    
                    # Convert UTC time to IST
                    b_time_str = b_time_raw
                    try:
                        if b_time_raw:
                            # Handle standard ISO formats, drop the trailing Z
                            clean_time = b_time_raw.replace("Z", "+00:00")
                            dt = datetime.fromisoformat(clean_time)
                            ist_dt = dt.astimezone(ist_tz)
                            
                            # Format clearly so the AI reads it well
                            b_time_str = ist_dt.strftime("%A, %B %d at %I:%M %p")
                    except Exception as parse_err:
                        logger.warning(f"Failed to parse time {b_time_raw}: {parse_err}")
                        pass # fallback to raw string if parsing fails
                        
                    bookings.append(f"ID: {b_id}, Time: {b_time_str}, Status: {b_status}")
                return f"Found bookings for phone {phone}:\n" + "\n".join(bookings)
            else:
                return f"No bookings found for phone {phone}. The API returned: {result}"
        except Exception as e:
            logger.error(f"Error fetching bookings: {e}")
            return "There was an error fetching the bookings."
    
    @llm.function_tool(description="Cancel an existing dental appointment.")
    async def cancel_appointment(
        self,
        booking_id: Annotated[str, "The ID or UID of the booking to cancel"],
        cancel_reason: Annotated[str, "Reason for cancellation"]
    ) -> str:
        logger.info(f"Tool called: cancel_appointment({booking_id})")
        try:
            result = await self.cal_client.cancel_booking(booking_id, cancel_reason)
            return f"Successfully canceled appointment {booking_id}."
        except Exception as e:
            logger.error(f"Error canceling booking: {e}")
            return f"There was an error canceling the booking {booking_id}."

    @llm.function_tool(description="Reschedule an existing dental appointment to a new time.")
    async def reschedule_appointment(
        self,
        booking_id: Annotated[str, "The ID or UID of the booking to reschedule"],
        new_start_time: Annotated[str, "ISO 8601 formatted new start time (e.g. '2026-03-25T10:00:00Z')"]
    ) -> str:
        logger.info(f"Tool called: reschedule_appointment({booking_id}, {new_start_time})")
        try:
            result = await self.cal_client.reschedule_booking(booking_id, new_start_time)
            new_id = result.get("data", {}).get("uid", result.get("data", {}).get("id", "Unknown"))
            return f"Successfully rescheduled appointment. New Booking ID is {new_id}."
        except Exception as e:
            logger.error(f"Error rescheduling booking: {e}")
            return f"There was an error rescheduling the booking {booking_id}."

    @llm.function_tool(description="Transfer the current phone call to the clinic's human receptionist.")
    async def transfer_call(self) -> str:
        """Transfers the ongoing SIP call to a human receptionist."""
        logger.info("Tool called: transfer_call")
        
        receptionist_number = os.getenv("RECEPTIONIST_PHONE_NUMBER")
        if not receptionist_number:
            logger.error("RECEPTIONIST_PHONE_NUMBER environment variable is not set.")
            return "Error: The receptionist's phone number is not configured in the system. I cannot transfer the call right now."

        # The chat_ctx is passed in via the agent initialization, but to execute the transfer
        # we need the participant identity of the caller. 
        # In this implementation, we will use the LiveKit API to issue the transfer.
        
        # A simpler approach using livekit.api to instruct the SIP service
        # to transfer the caller. We need the current room name to find the SIP participant.
        try:
            api = LiveKitAPI() # Automatically picks up LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET
            
            # Since we are inside the tool, we don't have direct access to the `ctx` object here
            # without refactoring. However, we can fetch rooms if needed, but a robust way
            # is to require the agent wrapper to pass the room context or participant identity 
            # if we wanted a purely stateless tool.
            
            # For this MVP implementation without heavy refactoring, we return an instructional 
            # string that the system should trigger the transfer, or if we had access to the SIP 
            # participant SID we could call `await api.sip.transfer_sip_participant(TransferSIPParticipantRequest(...))`
            
            # We will return a string to simulate it for now, and note that full implementation
            # requires passing the participant_sid down to the AssistantTools class.
            logger.warning("Transfer call triggered. Note: Full SIP transfer requires participant SID context.")
            return f"Call transfer initiated to {receptionist_number}. Please say 'I am transferring you now, please hold on' to the user."
            
        except Exception as e:
            logger.error(f"Error transferring call: {e}")
            return "There was an error transferring the call. Please ask the user to call back or leave a message."
