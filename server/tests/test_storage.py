import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import storage

class TestStorage(unittest.TestCase):
    @patch('storage.get_supabase_client')
    def test_upload_audio_to_supabase_success(self, mock_get_client):
        # Setup mock client
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        
        # Mock the upload response
        mock_bucket = MagicMock()
        mock_client.storage.from_.return_value = mock_bucket
        mock_bucket.upload.return_value = True
        mock_bucket.get_public_url.return_value = "https://example.com/audio.mp3"
        
        # Test file upload
        with patch('builtins.open', mock_open(read_data=b"fake-audio-data")):
            url = storage.upload_audio_to_supabase("dummy.mp3", "test_room.mp3")
            
        self.assertEqual(url, "https://example.com/audio.mp3")
        mock_client.storage.from_.assert_called_with("call_recordings")
        mock_bucket.upload.assert_called_once()
        
    @patch('storage.get_supabase_client')
    def test_get_public_audio_url(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        
        mock_bucket = MagicMock()
        mock_client.storage.from_.return_value = mock_bucket
        mock_bucket.get_public_url.return_value = "https://example.com/test_room.mp3"
        
        url = storage.get_public_audio_url("test_room.mp3")
        self.assertEqual(url, "https://example.com/test_room.mp3")

if __name__ == '__main__':
    unittest.main()
