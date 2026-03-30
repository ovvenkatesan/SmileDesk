import os
import re

# 1. Update agent.py (Remove deepgram from prewarm)
path_agent = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path_agent, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(', deepgram', '')
content = re.sub(r'\s*deepgram\.STT\(model="nova-2-general", language="en-IN"\)', '', content)

with open(path_agent, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update agent_unified.py (Remove deepgram import and comments)
path_unified = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent_unified.py'
with open(path_unified, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('from livekit.plugins import deepgram, google, elevenlabs, silero', 'from livekit.plugins import google, elevenlabs, silero')
content = re.sub(r'\s*# Deepgram Nova-2 handles Indian accents and rapid Tanglish code-switching seamlessly and much faster\.', '', content)

with open(path_unified, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Update .env (Remove DEEPGRAM_API_KEY)
path_env = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\.env'
with open(path_env, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(path_env, 'w', encoding='utf-8') as f:
    for line in lines:
        if not line.startswith('DEEPGRAM_API_KEY'):
            f.write(line)

print('Successfully removed Deepgram from agent.py, agent_unified.py, and .env')
