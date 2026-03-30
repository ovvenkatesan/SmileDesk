import asyncio
import os
import aiohttp
from dotenv import load_dotenv

load_dotenv(r'D:\Projects\BMad\SmileGardenVoiceAgent\server\.env')
api_key = os.getenv('GEMINI_API_KEY')
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}'

async def test():
    print("Sending request to Gemini...")
    payload = {"contents": [{"parts": [{"text": "say hi"}]}]}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=10) as resp:
                print("Status:", resp.status)
                print("Response:", await resp.text())
    except Exception as e:
        print("Error:", e)

asyncio.run(test())
