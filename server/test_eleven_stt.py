import asyncio
import time
import os
from livekit.plugins import elevenlabs
from dotenv import load_dotenv
load_dotenv()

async def test():
    print("Testing ElevenLabs STT...")
    try:
        s = elevenlabs.STT(model_id="scribe_v2")
        print("ElevenLabs STT initialized successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
