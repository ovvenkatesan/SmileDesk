import asyncio
from livekit.agents import llm
from livekit.agents.voice import Agent

print("Checking chat_ctx attributes...")
ctx = llm.ChatContext()
print("Has messages?", hasattr(ctx, 'messages'))
print("Is callable?", callable(ctx.messages))

# Simulate the actual loop
try:
    if callable(ctx.messages):
        for msg in ctx.messages():
            pass
        print("Success using messages()")
    else:
        for msg in ctx.messages:
            pass
        print("Success using messages as property")
except Exception as e:
    print(f"Error: {e}")
