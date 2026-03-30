import asyncio
import time
import os
from livekit.plugins import google
from livekit.agents import llm
from dotenv import load_dotenv
load_dotenv()

async def test():
    l=google.LLM(model='gemini-3.1-flash-lite-preview')
    ctx = llm.ChatContext()
    ctx.messages = [{'role': 'user', 'content': 'hi'}]
    t=time.time()
    try:
        s=l.chat(chat_ctx=ctx)
        first_token = False
        async for chunk in s:
            if not first_token:
                print(f'TTFT (Time to First Token): {time.time()-t:.2f}s')
                first_token = True
        print(f'Total Chat Time: {time.time()-t:.2f}s')
    except Exception as e:
        print(f'error: {e}')

if __name__ == '__main__':
    asyncio.run(test())
