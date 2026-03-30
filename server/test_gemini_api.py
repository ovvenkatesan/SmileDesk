import asyncio
import os
import aiohttp
from dotenv import load_dotenv

load_dotenv(r'D:\Projects\BMad\SmileGardenVoiceAgent\server\.env')
api_key = os.getenv('GEMINI_API_KEY')
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'

async def test():
    payload = {"contents": [{"parts": [{"text": "say hi"}]}]}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            print("Status:", resp.status)
            print("Response:", await resp.text())

asyncio.run(test())
