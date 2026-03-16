import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPipeline(unittest.TestCase):
    @patch.dict(os.environ, {"DEEPGRAM_API_KEY": "fake_key", "GEMINI_API_KEY": "fake_key", "GOOGLE_API_KEY": "fake_key", "SARVAM_API_KEY": "fake_key", "CAL_API_KEY": "fake_key"})
    @patch('pipeline.Agent')
    @patch('pipeline.AgentSession')
    def test_voice_pipeline_config(self, mock_session_class, mock_agent_class):
        try:
            import pipeline
            agent_config, session_config = pipeline.create_agent()
            
            # check what arguments were passed
            kwargs = mock_agent_class.call_args.kwargs
            
            # verify Neighborhood Nurse persona
            self.assertIn("Neighborhood Nurse", kwargs['instructions'])
            
            # verify session configuration
            session_kwargs = mock_session_class.call_args.kwargs
            self.assertIn('stt', session_kwargs)
            self.assertIn('llm', session_kwargs)
            self.assertIn('tts', session_kwargs)
            
            # verify cancellation/rescheduling instructions are present
            self.assertIn("cancel or reschedule", kwargs['instructions'])
            self.assertIn("cancel_appointment", kwargs['instructions'])
            self.assertIn("reschedule_appointment", kwargs['instructions'])
            
        except ImportError as e:
            self.fail(f"Failed to import pipeline module: {e}")

if __name__ == '__main__':
    unittest.main()
