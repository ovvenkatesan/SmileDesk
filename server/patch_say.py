import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('asyncio.create_task(agent.say(greeting, allow_interruptions=True))', 'asyncio.create_task(session.say(greeting, allow_interruptions=True))')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully patched agent.say to session.say")
