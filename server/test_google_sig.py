import inspect
from livekit.plugins import google
print(inspect.signature(google.STT.__init__))
