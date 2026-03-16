import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPipeline(unittest.TestCase):
    @patch.dict(os.environ, {"DEEPGRAM_API_KEY": "fake_key", "GEMINI_API_KEY": "fake_key", "GOOGLE_API_KEY": "fake_key"})
    @patch('pipeline.VoiceAgent')
    def test_voice_pipeline_config(self, mock_agent_class):
        try:
            import pipeline
            agent_config = pipeline.create_agent()
            mock_agent_class.assert_called_once()
            
            # check what arguments were passed
            kwargs = mock_agent_class.call_args.kwargs
            
            self.assertIn('stt', kwargs)
            self.assertIn('llm', kwargs)
            self.assertIn('tts', kwargs)
            self.assertIn('instructions', kwargs)
            
            # verify Neighborhood Nurse persona
            self.assertIn("Neighborhood Nurse", kwargs['instructions'])
        except ImportError as e:
            self.fail(f"Failed to import pipeline module: {e}")

if __name__ == '__main__':
    unittest.main()
