import os
import re

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\sentiment.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_code = '''import os
import json
import logging
from google import genai
from google.genai import types

logger = logging.getLogger("voice-agent-sentiment")

async def analyze_sentiment_and_summarize(transcript: str) -> dict:
    if not transcript or not transcript.strip():
        return {"sentiment": "Neutral", "summary": "No transcript available.", "name": "Unknown", "phone": "Unknown"}

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return {"sentiment": "Neutral", "summary": "API Key missing.", "name": "Unknown", "phone": "Unknown"}

    prompt = f"""
    Analyze the following dental clinic call transcript.
    Extract the following four details:
    1. A single word representing the caller's sentiment (e.g., Anxious, Neutral, Angry, Satisfied, Urgent).
    2. A brief 1-2 sentence summary of the call's outcome. Do not include the name/phone here.
    3. The caller's Name (if mentioned in the transcript). If not mentioned, return "Unknown".
    4. The caller's Phone Number (if mentioned in the transcript). If not mentioned, return "Unknown".

    Transcript:
    {transcript}

    Respond ONLY in valid JSON format like this:
    {{"sentiment": "Anxious", "summary": "Patient has a severe toothache and booked an emergency appointment.", "name": "Venkatesh", "phone": "9697012480"}}
    """

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        if not response.text:
            return {"sentiment": "Neutral", "summary": "Sentiment analysis empty.", "name": "Unknown", "phone": "Unknown"}

        result = json.loads(response.text)
        
        # Prepend Name/Phone to the summary automatically
        name = result.get("name", "Unknown")
        phone = result.get("phone", "Unknown")
        base_summary = result.get("summary", "Summary unavailable.")
        
        prefix = ""
        if name != "Unknown" and phone != "Unknown":
            prefix = f"[{name} / {phone}] "
        elif name != "Unknown":
            prefix = f"[{name}] "
        elif phone != "Unknown":
            prefix = f"[{phone}] "
            
        final_summary = prefix + base_summary

        return {
            "sentiment": result.get("sentiment", "Neutral"),
            "summary": final_summary,
            "name": name,
            "phone": phone
        }
    except Exception as e:
        logger.error(f"Error during sentiment analysis using google SDK: {e}")
        return {"sentiment": "Neutral", "summary": "Failed to generate summary.", "name": "Unknown", "phone": "Unknown"}
'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_code)
print("Successfully patched sentiment.py to extract Name and Phone")
