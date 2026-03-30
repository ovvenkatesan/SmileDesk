import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken newline in the string literal
content = content.replace('transcript_text = "\n".join(transcript_lines)', 'transcript_text = "\\n".join(transcript_lines)')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
