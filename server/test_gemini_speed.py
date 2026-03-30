import asyncio
import time
from livekit.plugins import google
from livekit.agents import llm

async def test():
    t=time.time()
    l=google.LLM(model='gemini-3.1-flash-lite-preview')
    ctx = llm.ChatContext()
    ctx.messages = [{"role": "user", "content": "hi"}]
    print(f'init: {time.time()-t:.2f}s')
    t=time.time()
    try:
        s=l.chat(chat_ctx=ctx)
        async for chunk in s: pass
        print(f'chat: {time.time()-t:.2f}s')
    except Exception as e:
        print(f'error: {e}')

if __name__ == "__main__":
    asyncio.run(test())
