import os
import re

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the fragile event hook and add an explicit await loop at the end of entrypoint
old_code = r'''    def _on_disconnect\(\*args, \*\*kwargs\):
        logger\.info\("Room disconnected event caught! Spawning shielded log task..."\)
        # Get the main event loop so the task doesn't die when the Job task gets cancelled
        loop = asyncio\.get_event_loop\(\)
        loop\.create_task\(log_call_to_supabase\(caller_id, start_time, ctx\.room\.name, agent\)\)

    ctx\.room\.on\("disconnected", _on_disconnect\)'''

new_code = '''    # Wait for the room to close
    try:
        logger.info("Agent is listening. Waiting for job completion...")
        # wait_for_disconnect might be cancelled when LiveKit tears down the job.
        await asyncio.sleep(86400) # Sleep indefinitely. LiveKit will raise CancelledError here when user hangs up.
    except asyncio.CancelledError:
        logger.info("Job was cancelled because user hung up. Logging call...")
        # Get the main event loop to spawn the task outside of this dying context
        loop = asyncio.get_event_loop()
        loop.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent))
        raise'''

content = re.sub(old_code, new_code, content, flags=re.MULTILINE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully patched agent.py to catch CancelledError for guaranteed shutdown logging")
