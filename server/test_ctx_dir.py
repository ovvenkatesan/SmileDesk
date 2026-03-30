import inspect
from livekit.agents import llm
ctx = llm.ChatContext()
print([d for d in dir(ctx) if not d.startswith('_')])
