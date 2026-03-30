import os
import re

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = '''        final_caller_id = caller_id
        if caller_id.startswith("user-") and state.get("phone_number_collected"):
            final_caller_id = state.get("phone_number_collected")'''

# We move the final_caller_id logic to AFTER the sentiment analysis so we can use Gemini's extracted data
new_code = '''        final_caller_id = caller_id'''

content = content.replace(old_code, new_code)

old_code_2 = '''        logger.info(f"Analyzing sentiment... Transcript length: {len(transcript_text)}")
        analysis = await analyze_sentiment_and_summarize(transcript_text)'''

new_code_2 = '''        logger.info(f"Analyzing sentiment... Transcript length: {len(transcript_text)}")
        analysis = await analyze_sentiment_and_summarize(transcript_text)
        
        # Override caller ID if Gemini found their name/phone in the transcript
        extracted_name = analysis.get("name", "Unknown")
        extracted_phone = analysis.get("phone", "Unknown")
        
        if final_caller_id.startswith("user-") or final_caller_id == "unknown":
            if extracted_name != "Unknown" and extracted_phone != "Unknown":
                final_caller_id = f"{extracted_name} ({extracted_phone})"
            elif extracted_phone != "Unknown":
                final_caller_id = extracted_phone
            elif extracted_name != "Unknown":
                final_caller_id = extracted_name
            elif state.get("phone_number_collected"):
                final_caller_id = state.get("phone_number_collected")'''

content = content.replace(old_code_2, new_code_2)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully patched agent.py to use Gemini-extracted Identity for the Caller column")
