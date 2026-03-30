import inspect
from livekit.agents import llm
ctx = llm.ChatContext()
print(type(ctx.messages))
