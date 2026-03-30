import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the try/except CancelledError with LiveKit's official add_shutdown_callback
old_block = '''    try:
        # Keep the entrypoint running indefinitely while the room is connected.
        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.
        await asyncio.sleep(86400)
    except asyncio.CancelledError:
        logger.info("Job was cancelled because user hung up. Logging call to Supabase...")
        loop = asyncio.get_event_loop()
        loop.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent))
        raise'''

new_block = '''    # Use LiveKit's official shutdown callback to guarantee execution
    async def shutdown_hook():
        logger.info("Job shutdown initiated. Logging call to Supabase...")
        await log_call_to_supabase(caller_id, start_time, ctx.room.name, agent)
        
    ctx.add_shutdown_callback(shutdown_hook)'''

# Wait, if there are multiple variations, let's just use Python's replace safely
if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("WARNING: Exact block not found. Trying regex.")
    import re
    content = re.sub(r'\s*try:\s*# Keep the entrypoint running.*?raise', '\n' + new_block, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully injected ctx.add_shutdown_callback into entrypoint!")
