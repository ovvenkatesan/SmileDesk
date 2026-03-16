import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestTools(unittest.IsolatedAsyncioTestCase):

    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('cal_client.CalClient.get_available_slots')
    async def test_check_availability_tool(self, mock_get_slots):
        from tools import AssistantTools
        
        mock_get_slots.return_value = {
            "slots": {
                "2026-03-20": [
                    {"time": "2026-03-20T09:00:00Z"}
                ]
            }
        }
        
        tools = AssistantTools()
        result = await tools.check_availability(date_from="2026-03-20", date_to="2026-03-20", event_type_id=123)
        
        self.assertIn("2026-03-20T09:00:00Z", result)
        mock_get_slots.assert_called_once_with("2026-03-20", "2026-03-20", 123)

    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('cal_client.CalClient.create_booking')
    async def test_book_appointment_tool(self, mock_create_booking):
        from tools import AssistantTools
        
        mock_create_booking.return_value = {
            "booking": {
                "id": 12345,
                "status": "ACCEPTED"
            }
        }
        
        tools = AssistantTools()
        result = await tools.book_appointment(
            name="Jane Doe",
            email="jane@example.com",
            start_time="2026-03-20T09:00:00Z",
            event_type_id=123
        )
        
        self.assertIn("12345", result)
        self.assertIn("ACCEPTED", result)
        mock_create_booking.assert_called_once_with(
            "Jane Doe", "jane@example.com", "2026-03-20T09:00:00Z", 123
        )

    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('cal_client.CalClient.get_booking_by_email')
    async def test_get_bookings_tool(self, mock_get_bookings):
        from tools import AssistantTools
        
        mock_get_bookings.return_value = {
            "bookings": [
                {
                    "id": 12345,
                    "start": "2026-03-20T09:00:00Z",
                    "status": "ACCEPTED"
                }
            ]
        }
        
        tools = AssistantTools()
        result = await tools.get_bookings(email="jane@example.com")
        
        self.assertIn("12345", result)
        self.assertIn("2026-03-20T09:00:00Z", result)
        mock_get_bookings.assert_called_once_with("jane@example.com")

    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('cal_client.CalClient.cancel_booking')
    async def test_cancel_appointment_tool(self, mock_cancel_booking):
        from tools import AssistantTools
        
        mock_cancel_booking.return_value = {
            "booking": {
                "id": 12345,
                "status": "CANCELLED"
            }
        }
        
        tools = AssistantTools()
        result = await tools.cancel_appointment(booking_id=12345, cancel_reason="Patient request")
        
        self.assertIn("Successfully canceled", result)
        self.assertIn("12345", result)
        mock_cancel_booking.assert_called_once_with(12345, "Patient request")

    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('cal_client.CalClient.reschedule_booking')
    async def test_reschedule_appointment_tool(self, mock_reschedule_booking):
        from tools import AssistantTools
        
        mock_reschedule_booking.return_value = {
            "booking": {
                "id": 12346,
                "status": "ACCEPTED"
            }
        }
        
        tools = AssistantTools()
        result = await tools.reschedule_appointment(booking_id=12345, new_start_time="2026-03-25T10:00:00Z")
        
        self.assertIn("Successfully rescheduled", result)
        self.assertIn("12346", result)
        mock_reschedule_booking.assert_called_once_with(12345, "2026-03-25T10:00:00Z")

if __name__ == '__main__':
    unittest.main()
