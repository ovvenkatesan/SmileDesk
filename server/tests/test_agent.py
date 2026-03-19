import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestAgent(unittest.IsolatedAsyncioTestCase):
    def test_agent_module_has_main(self):
        try:
            import agent
            self.assertTrue(hasattr(agent, 'entrypoint'))
            self.assertTrue(hasattr(agent, 'prewarm'))
        except ImportError as e:
            self.fail(f"Failed to import agent module: {e}")

    @patch('agent.LiveKitAPI')
    async def test_start_recording(self, mock_livekit_api):
        import agent
        
        # Setup mock Egress API
        mock_api_instance = MagicMock()
        mock_livekit_api.return_value = mock_api_instance
        
        mock_egress_info = MagicMock()
        mock_egress_info.egress_id = "eg_test_123"
        mock_api_instance.egress.start_room_composite_egress = AsyncMock(return_value=mock_egress_info)
        mock_api_instance.aclose = AsyncMock()

        # Call the function
        egress_id = await agent.start_recording("test_room")
        
        # Assertions
        self.assertEqual(egress_id, "eg_test_123")
        mock_api_instance.egress.start_room_composite_egress.assert_called_once()
        mock_api_instance.aclose.assert_called_once()

if __name__ == '__main__':
    unittest.main()

