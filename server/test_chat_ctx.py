import asyncio
from livekit.agents import llm

ctx = llm.ChatContext()
ctx.messages.append(llm.ChatMessage(role="user", content="hello"))
print(ctx.messages)
print(type(ctx.messages))
