import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the broken block by targeting the try statement and its contents precisely
bad_block = "    try:\n        # Keep the entrypoint running indefinitely while the room is connected.\n        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.\n        await asyncio.sleep(86400)\n    except asyncio.CancelledError:"

good_block = "    try:\n        # Keep the entrypoint running indefinitely while the room is connected.\n        # LiveKit will raise an asyncio.CancelledError here when the user hangs up or the session ends.\n        await asyncio.sleep(86400)\n    except asyncio.CancelledError:"

# Wait, let me just find exactly what is on line 151 and fix it by splitting lines
lines = content.split('\n')
for i, line in enumerate(lines):
    if line.strip() == "try:":
        lines[i] = "    try:"
    if "await asyncio.sleep(86400)" in line:
        lines[i] = "        await asyncio.sleep(86400)"
    if "except asyncio.CancelledError:" in line:
        lines[i] = "    except asyncio.CancelledError:"
    if "logger.info(\"Job was cancelled because user hung up. Logging call to Supabase...\")" in line:
        lines[i] = "        logger.info(\"Job was cancelled because user hung up. Logging call to Supabase...\")"
    if "loop = asyncio.get_event_loop()" in line:
        lines[i] = "        loop = asyncio.get_event_loop()"
    if "loop.create_task(log_call_to_supabase" in line:
        lines[i] = "        loop.create_task(log_call_to_supabase(caller_id, start_time, ctx.room.name, agent))"
    if line.strip() == "raise # Re-raise to allow LiveKit to finish graceful teardown":
        lines[i] = "        raise"

with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

import py_compile
try:
    py_compile.compile(path, doraise=True)
    print("Compilation successful!")
except Exception as e:
    print("Compilation failed:", e)
