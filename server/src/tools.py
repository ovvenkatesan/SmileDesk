import logging
from livekit.agents import llm
from typing import Annotated
from cal_client import CalClient

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
            slots = await self.cal_client.get_available_slots(date_from, date_to, event_type_id)
            # Simplistic parsing to return a readable string to the LLM
            if not slots or "slots" not in slots or not slots["slots"]:
                return "No available slots found for the requested dates."
                
            available_times = []
            for date, daily_slots in slots["slots"].items():
                for slot in daily_slots:
                    available_times.append(slot.get("time"))
            
            if not available_times:
                return "No available slots found for the requested dates."
                
            return f"Available slots: {', '.join(available_times)}"
        except Exception as e:
            logger.error(f"Error checking availability: {e}")
            return "There was an error checking the calendar. Please advise the user that the system is temporarily down."

    @llm.function_tool(description="Create a new dental appointment booking.")
    async def book_appointment(
        self,
        name: Annotated[str, "Patient's full name"],
        email: Annotated[str, "Patient's email address"],
        start_time: Annotated[str, "ISO 8601 formatted start time (e.g. '2026-03-20T09:00:00Z')"],
        event_type_id: Annotated[int, "The ID of the event type to book"]
    ) -> str:
        logger.info(f"Tool called: book_appointment({name}, {start_time})")
        try:
            result = await self.cal_client.create_booking(name, email, start_time, event_type_id)
            if "booking" in result and result["booking"].get("status") == "ACCEPTED":
                booking_id = result["booking"].get("id")
                return f"Successfully booked appointment! Booking ID is {booking_id} with status ACCEPTED."
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
            if "bookings" in result and result["bookings"]:
                bookings = []
                for b in result["bookings"]:
                    bookings.append(f"ID: {b.get('id')}, Time: {b.get('start')}, Status: {b.get('status')}")
                return f"Found bookings for {email}:\n" + "\n".join(bookings)
            else:
                return f"No bookings found for email {email}."
        except Exception as e:
            logger.error(f"Error fetching bookings: {e}")
            return "There was an error fetching the bookings."

    @llm.function_tool(description="Cancel an existing dental appointment.")
    async def cancel_appointment(
        self,
        booking_id: Annotated[int, "The ID of the booking to cancel"],
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
        booking_id: Annotated[int, "The ID of the booking to reschedule"],
        new_start_time: Annotated[str, "ISO 8601 formatted new start time (e.g. '2026-03-25T10:00:00Z')"]
    ) -> str:
        logger.info(f"Tool called: reschedule_appointment({booking_id}, {new_start_time})")
        try:
            result = await self.cal_client.reschedule_booking(booking_id, new_start_time)
            new_id = result.get("booking", {}).get("id", "Unknown")
            return f"Successfully rescheduled appointment. New Booking ID is {new_id}."
        except Exception as e:
            logger.error(f"Error rescheduling booking: {e}")
            return f"There was an error rescheduling the booking {booking_id}."
