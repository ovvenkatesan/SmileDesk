import asyncio
import time
import os
import sys

# Add src to path so we can import agent and sentiment properly
sys.path.append(r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src')

from dotenv import load_dotenv
load_dotenv("D:\Projects\BMad\SmileGardenVoiceAgent\server\.env")

from agent import log_call_to_supabase, session_states

class MockMsg:
    def __init__(self, role, content):
        self.role = role
        self.content = content

class MockChatCtx:
    def messages(self):
        return [MockMsg("user", "Hello this is a test.")]

class MockAgent:
    def __init__(self):
        self.chat_ctx = MockChatCtx()

async def test():
    print("Running log_call_to_supabase directly...")
    await log_call_to_supabase("user-123", time.time() - 60, "test-room", MockAgent())
    print("Finished.")

asyncio.run(test())
