import aiohttp
import os
import logging
from typing import Dict, Any, Optional
import urllib.parse

logger = logging.getLogger("voice-agent.calcom")

class CalClient:
    """Client for interacting with the Cal.com API."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("CAL_API_KEY")
        if not self.api_key:
            raise ValueError("CAL_API_KEY is required to initialize CalClient")
        self.base_url = "https://api.cal.com/v1"

    async def get_available_slots(self, date_from: str, date_to: str, event_type_id: int) -> Dict[str, Any]:
        """
        Fetch available slots for a given date range and event type.
        
        Args:
            date_from: Start date in YYYY-MM-DD format.
            date_to: End date in YYYY-MM-DD format.
            event_type_id: The ID of the Cal.com event type.
            
        Returns:
            A dictionary containing available slots.
        """
        params = {
            "startTime": f"{date_from}T00:00:00Z",
            "endTime": f"{date_to}T23:59:59Z",
            "eventTypeId": event_type_id,
            "apiKey": self.api_key
        }
        query_string = urllib.parse.urlencode(params)
        url = f"{self.base_url}/slots?{query_string}"
        
        logger.info(f"Fetching slots from {date_from} to {date_to} for event {event_type_id}")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    error_msg = await response.text()
                    logger.error(f"Failed to fetch slots: {error_msg}")
                    response.raise_for_status()
                return await response.json()

    async def create_booking(self, name: str, email: str, start_time: str, event_type_id: int) -> Dict[str, Any]:
        """
        Create a new booking.
        
        Args:
            name: Patient's full name.
            email: Patient's email.
            start_time: ISO 8601 formatted start time (e.g., "2026-03-20T09:00:00Z").
            event_type_id: The ID of the Cal.com event type.
            
        Returns:
            The booking response object.
        """
        url = f"{self.base_url}/bookings?apiKey={self.api_key}"
        
        payload = {
            "eventTypeId": event_type_id,
            "start": start_time,
            "responses": {
                "name": name,
                "email": email,
                "location": "Smile Garden Dental Clinic"
            },
            "timeZone": "Asia/Kolkata", # Setting local timezone for Chennai
            "language": "en"
        }
        
        logger.info(f"Creating booking for {name} at {start_time}")
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200 and response.status != 201:
                    error_msg = await response.text()
                    logger.error(f"Failed to create booking: {error_msg}")
                    response.raise_for_status()
                return await response.json()
