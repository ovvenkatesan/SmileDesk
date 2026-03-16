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

if __name__ == '__main__':
    unittest.main()
