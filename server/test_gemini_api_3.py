import asyncio
import os
import aiohttp
from dotenv import load_dotenv

load_dotenv(r'D:\Projects\BMad\SmileGardenVoiceAgent\server\.env')
api_key = os.getenv('GEMINI_API_KEY')

async def test():
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'
    payload = {"contents": [{"parts": [{"text": "say hi"}]}]}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, timeout=10) as resp:
            print("Status:", resp.status)

asyncio.run(test())
