from livekit.agents import llm
ctx = llm.ChatContext()
print(ctx.messages)
print(type(ctx.messages))
