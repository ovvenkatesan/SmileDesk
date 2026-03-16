import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestCalClient(unittest.IsolatedAsyncioTestCase):
    
    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('aiohttp.ClientSession.get')
    async def test_get_available_slots(self, mock_get):
        from cal_client import CalClient
        
        # Mock successful response
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = {
            "slots": {
                "2026-03-20": [
                    {"time": "2026-03-20T09:00:00Z"},
                    {"time": "2026-03-20T10:00:00Z"}
                ]
            }
        }
        mock_get.return_value.__aenter__.return_value = mock_response

        client = CalClient()
        slots = await client.get_available_slots("2026-03-20", "2026-03-21", event_type_id=123)
        
        self.assertIn("2026-03-20", slots["slots"])
        self.assertEqual(len(slots["slots"]["2026-03-20"]), 2)
        mock_get.assert_called_once()

    @patch.dict(os.environ, {"CAL_API_KEY": "test_key"})
    @patch('aiohttp.ClientSession.post')
    async def test_create_booking(self, mock_post):
        from cal_client import CalClient
        
        # Mock successful response
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = {
            "booking": {
                "id": 12345,
                "status": "ACCEPTED"
            }
        }
        mock_post.return_value.__aenter__.return_value = mock_response

        client = CalClient()
        booking_result = await client.create_booking(
            name="John Doe", 
            email="john@example.com", 
            start_time="2026-03-20T09:00:00Z", 
            event_type_id=123
        )
        
        self.assertEqual(booking_result["booking"]["id"], 12345)
        self.assertEqual(booking_result["booking"]["status"], "ACCEPTED")
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()
