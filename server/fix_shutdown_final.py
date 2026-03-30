import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''    def _on_disconnect(*args, **kwargs):
        logger.info("Room disconnected event caught! Spawning shielded log task...")
        # Get the main event loop so the task doesn't die when the Job task gets cancelled
        loop = asyncio.get_event_loop()
        loop.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent))

    ctx.room.on("disconnected", _on_disconnect)'''

new_block = '''    try:
        # Keep the entrypoint running indefinitely while the room is connected.
        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.
        await asyncio.sleep(86400)
    except asyncio.CancelledError:
        logger.info("Job was cancelled because user hung up. Logging call to Supabase...")
        loop = asyncio.get_event_loop()
        loop.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent))
        raise # Re-raise to allow LiveKit to finish graceful teardown
'''

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully injected the bulletproof shutdown loop into entrypoint!")
else:
    print("Could not find old block. Here is what the end of entrypoint looks like:")
    print(content[content.find('def _on_disconnect'):])
