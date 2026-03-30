import asyncio
import os
from dotenv import load_dotenv
import sys
sys.path.append('src')
from cal_client import CalClient

load_dotenv()

async def test():
    client = CalClient()
    try:
        # Testing for tomorrow and day after
        res = await client.get_available_slots('2026-03-30', '2026-03-31', 5042550)
        print("API Response:", res)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(test())
