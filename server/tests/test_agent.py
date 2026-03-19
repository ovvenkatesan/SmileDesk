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

    @patch('agent.supabase')
    @patch('sentiment.analyze_sentiment_and_summarize', new_callable=AsyncMock)
    @patch('agent.storage.get_public_audio_url')
    async def test_log_call_to_supabase(self, mock_get_url, mock_analyze, mock_supabase):
        import agent
        
        # Setup mocks
        mock_get_url.return_value = "https://example.com/audio.mp3"
        mock_analyze.return_value = {"sentiment": "Happy", "summary": "Good call."}
        
        mock_table = MagicMock()
        mock_supabase.table.return_value = mock_table
        mock_insert = MagicMock()
        mock_table.insert.return_value = mock_insert
        
        mock_agent = MagicMock()
        mock_agent.chat_ctx = MagicMock()
        mock_msg = MagicMock()
        mock_msg.role = "user"
        mock_msg.content = "Hello!"
        mock_agent.chat_ctx.messages = [mock_msg]
        
        # Set some session state
        agent.session_states["test_room"] = {"booked_appointment": True}
        
        # Call the function
        await agent.log_call_to_supabase("user123", 1000, "test_room", mock_agent)
        
        # Verify db insert was called with expected data
        mock_supabase.table.assert_called_with("calls")
        mock_table.insert.assert_called_once()
        
        insert_args = mock_table.insert.call_args[0][0]
        self.assertEqual(insert_args["caller_number"], "user123")
        self.assertEqual(insert_args["outcome"], "booked_appointment")
        self.assertEqual(insert_args["sentiment"], "Happy")
        self.assertEqual(insert_args["transcript"], "User: Hello!")
        self.assertEqual(insert_args["audio_url"], "https://example.com/audio.mp3")
        mock_insert.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()


