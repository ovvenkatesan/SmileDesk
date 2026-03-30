import asyncio
import time
from livekit.plugins import elevenlabs
from livekit.agents import stt

async def test():
    t=time.time()
    s = elevenlabs.STT(model_id="scribe_v2_realtime")
    print(f'init: {time.time()-t:.2f}s')
    t=time.time()
    try:
        stream = s.stream()
        print(f'stream open: {time.time()-t:.2f}s')
    except Exception as e:
        print(f'error: {e}')

if __name__ == "__main__":
    asyncio.run(test())
