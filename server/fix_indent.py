import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('    try:\n        # Keep', '    try:\n        # Keep')
content = content.replace('        await asyncio.sleep(86400)', '        await asyncio.sleep(86400)')

# Let's just do a clean replace of that exact block
old_block = '''    try:
        # Keep the entrypoint running indefinitely while the room is connected.
        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.
        await asyncio.sleep(86400)
    except asyncio.CancelledError:'''

new_block = '''    try:
        # Keep the entrypoint running indefinitely while the room is connected.
        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.
        await asyncio.sleep(86400)
    except asyncio.CancelledError:'''

content = content.replace('''    try:\n        # Keep the entrypoint running indefinitely while the room is connected.\n        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.\n        await asyncio.sleep(86400)\n    except asyncio.CancelledError:''', '''    try:\n        # Keep the entrypoint running indefinitely while the room is connected.\n        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.\n        await asyncio.sleep(86400)\n    except asyncio.CancelledError:''')

# Wait, let's just write the exact block with hardcoded spaces
content = content.replace('    try:\n        # Keep the entrypoint running indefinitely while the room is connected.\n        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.\n        await asyncio.sleep(86400)\n    except asyncio.CancelledError:', '    try:\n        # Keep the entrypoint running indefinitely while the room is connected.\n        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.\n        await asyncio.sleep(86400)\n    except asyncio.CancelledError:')
