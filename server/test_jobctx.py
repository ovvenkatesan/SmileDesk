import inspect
from livekit.agents import JobContext

print([m for m in dir(JobContext) if not m.startswith('_')])
