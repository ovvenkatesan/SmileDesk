import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sentiment import analyze_sentiment_and_summarize

class TestSentiment(unittest.IsolatedAsyncioTestCase):
    @patch('sentiment.os.getenv')
    @patch('sentiment.aiohttp.ClientSession.post')
    async def test_analyze_sentiment_success(self, mock_post, mock_getenv):
        mock_getenv.return_value = "fake_api_key"
        
        # Setup mock response
        mock_response = AsyncMock()
        mock_response.status = 200
        
        fake_response_data = {
            "candidates": [{
                "content": {
                    "parts": [{"text": json.dumps({"sentiment": "Urgent", "summary": "Patient in pain."})}]
                }
            }]
        }
        mock_response.json = AsyncMock(return_value=fake_response_data)
        
        # We need to mock the async context manager for post()
        mock_post_context = AsyncMock()
        mock_post_context.__aenter__.return_value = mock_response
        mock_post.return_value = mock_post_context
        
        result = await analyze_sentiment_and_summarize("Caller: My tooth hurts!")
        
        self.assertEqual(result["sentiment"], "Urgent")
        self.assertEqual(result["summary"], "Patient in pain.")
        
    async def test_empty_transcript(self):
        result = await analyze_sentiment_and_summarize("")
        self.assertEqual(result["sentiment"], "Neutral")
        self.assertIn("No transcript", result["summary"])

if __name__ == '__main__':
    unittest.main()
