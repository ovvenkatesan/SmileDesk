import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import sys
import os
import asyncio
import base64
import wave
import io

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestSarvamTTS(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Create a tiny dummy WAV file for the mock to return
        self.dummy_wav_io = io.BytesIO()
        with wave.open(self.dummy_wav_io, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(24000)
            # Write 10 samples of silence (20 bytes)
            wav_file.writeframes(b'\x00\x00' * 10)
            
        self.dummy_wav_bytes = self.dummy_wav_io.getvalue()
        self.dummy_base64 = base64.b64encode(self.dummy_wav_bytes).decode('utf-8')

    @patch.dict(os.environ, {"SARVAM_API_KEY": "fake_key"})
    async def test_sarvam_chunked_stream_run(self):
        from sarvam_tts import SarvamTTS, SarvamChunkedStream
        from livekit.agents.tts import AudioEmitter
        
        tts = SarvamTTS(api_key="fake_key")
        
        # Mock the connection options
        mock_conn_options = MagicMock()
        mock_conn_options.timeout = 10
        
        stream = SarvamChunkedStream(tts=tts, input_text="Hello", conn_options=mock_conn_options)
        
        mock_emitter = MagicMock(spec=AudioEmitter)
        
        # Mock the aiohttp post response
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = {"audios": [self.dummy_base64]}
        
        mock_post_ctx = MagicMock()
        mock_post_ctx.__aenter__ = AsyncMock(return_value=mock_response)
        mock_post_ctx.__aexit__ = AsyncMock(return_value=None)
        
        mock_session = MagicMock()
        mock_session.post.return_value = mock_post_ctx
        
        # Patch the session creation
        with patch('aiohttp.ClientSession', return_value=mock_session):
            await stream._run(mock_emitter)
            
        # Verify the emitter was initialized and pushed to
        mock_emitter.initialize.assert_called_once()
        self.assertEqual(mock_emitter.push.call_count, 1)
        mock_emitter.flush.assert_called_once()
        
        # Check what was pushed (should be 64 bytes of raw PCM incl header)
        pushed_args = mock_emitter.push.call_args[0]
        self.assertEqual(len(pushed_args[0]), 64)

if __name__ == '__main__':
    unittest.main()
