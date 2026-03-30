import os
import re

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the fragile disconnect hook with an asyncio.shield/background loop approach
old_hook = 'ctx.room.on("disconnected", lambda *args, **kwargs: asyncio.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent)))'
new_hook = '''
    def _on_disconnect(*args, **kwargs):
        logger.info("Room disconnected event caught! Spawning shielded log task...")
        # Get the main event loop so the task doesn't die when the Job task gets cancelled
        loop = asyncio.get_event_loop()
        loop.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent))
        
    ctx.room.on("disconnected", _on_disconnect)
'''

content = content.replace(old_hook, new_hook)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
