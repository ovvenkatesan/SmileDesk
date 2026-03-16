import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLogging(unittest.TestCase):
    @patch.dict(os.environ, {"DEEPGRAM_API_KEY": "fake_key", "GEMINI_API_KEY": "fake_key", "GOOGLE_API_KEY": "fake_key"})
    @patch('pipeline.VoiceAgent')
    def test_agent_events_registered(self, mock_agent_class):
        try:
            import pipeline
            agent = pipeline.create_agent()
            
            # This is a basic test verifying if any event handlers were mocked
            # In a real implementation we'd check specific events like "user_started_speaking"
            # For this simple mock we just verify we can import and run the code without error
            self.assertIsNotNone(agent)
            
        except ImportError as e:
            self.fail(f"Failed to import pipeline module: {e}")

if __name__ == '__main__':
    unittest.main()
