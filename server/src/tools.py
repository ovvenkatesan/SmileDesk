import logging
from livekit.agents import llm
from typing import Annotated
from cal_client import CalClient
from datetime import datetime, timezone, timedelta

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

    @llm.function_tool(description="Lookup a user's existing appointment bookings by their email address.")
    async def get_bookings(
        self,
        email: Annotated[str, "Patient's email address"]
    ) -> str:
        logger.info(f"Tool called: get_bookings({email})")
        try:
            result = await self.cal_client.get_booking_by_email(email)
            
            bookings_list = result.get("data", result.get("bookings", []))
            
            if bookings_list:
                bookings = []
                for b in bookings_list:
                    b_id = b.get("uid", b.get("id"))
                    b_time = b.get("start")
                    b_status = b.get("status")
                    bookings.append(f"ID: {b_id}, Time: {b_time}, Status: {b_status}")
                return f"Found bookings for {email}:\n" + "\n".join(bookings)
            else:
                return f"No bookings found for email {email}."
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
