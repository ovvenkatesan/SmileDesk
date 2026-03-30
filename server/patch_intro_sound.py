import os
import re

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = '''    logger.info("Agent connected and ready")
    
    # Hook into agent speech completion to check if we should hang up'''

new_code = '''    logger.info("Agent connected and ready")
    
    # Send the intro greeting explicitly so the agent speaks immediately upon connection
    greeting = "Hello! வணக்கம்! Smile Garden-ல இருந்து பேசுறேன். How can I help you today?"
    asyncio.create_task(agent.say(greeting, allow_interruptions=True))
    
    # Hook into agent speech completion to check if we should hang up'''

content = content.replace(old_code, new_code)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully patched agent.py to play the intro sound immediately on connect")
