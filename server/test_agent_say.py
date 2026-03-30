import inspect
from livekit.agents.voice import AgentSession

print("AgentSession methods:")
print([d for d in dir(AgentSession) if not d.startswith('_')])
