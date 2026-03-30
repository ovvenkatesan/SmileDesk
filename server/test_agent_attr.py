import inspect
from livekit.agents.voice import Agent
print('chat_ctx in Agent:', hasattr(Agent, 'chat_ctx') or hasattr(Agent, '_chat_ctx') or property in [type(getattr(Agent, 'chat_ctx', None))])
