import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('WorkerOptions(\n            entrypoint_fnc=entrypoint,\n            prewarm_fnc=prewarm\n        )', 'WorkerOptions(\n            entrypoint_fnc=entrypoint,\n            prewarm_fnc=prewarm,\n            agent_name="pallavi-voice-agent"\n        )')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
