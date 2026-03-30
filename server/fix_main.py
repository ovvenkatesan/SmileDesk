import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'a', encoding='utf-8') as f:
    f.write('\n\nif __name__ == "__main__":\n    cli.run_app(\n        WorkerOptions(\n            entrypoint_fnc=entrypoint,\n            prewarm_fnc=prewarm\n        )\n    )\n')
