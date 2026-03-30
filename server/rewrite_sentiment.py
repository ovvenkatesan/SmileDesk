import os

path = r'D:\Projects\BMad\SmileGardenVoiceAgent\server\src\sentiment.py'

new_code = '''import os
import json
import logging
from google import genai
from google.genai import types

logger = logging.getLogger("voice-agent-sentiment")

async def analyze_sentiment_and_summarize(transcript: str) -> dict:
    if not transcript or not transcript.strip():
        return {"sentiment": "Neutral", "summary": "No transcript available."}

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return {"sentiment": "Neutral", "summary": "API Key missing."}

    prompt = f"""
    Analyze the following dental clinic call transcript.
    Provide two things:
    1. A single word representing the caller's sentiment (e.g., Anxious, Neutral, Angry, Satisfied, Urgent).
    2. A brief 1-2 sentence summary of the call's outcome.

    Transcript:
    {transcript}

    Respond ONLY in valid JSON format like this:
    {{"sentiment": "Anxious", "summary": "Patient has a severe toothache and booked an emergency appointment."}}
    """

    try:
        client = genai.Client(api_key=api_key)
        # using the newest lightweight model that is guaranteed to work
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        # If it fails, fallback
        if not response.text:
            return {"sentiment": "Neutral", "summary": "Sentiment analysis empty."}

        result = json.loads(response.text)
        return {
            "sentiment": result.get("sentiment", "Neutral"),
            "summary": result.get("summary", "Summary unavailable.")
        }
    except Exception as e:
        logger.error(f"Error during sentiment analysis using google SDK: {e}")
        # Always return fallback so we don't crash the database insert
        return {"sentiment": "Neutral", "summary": "Failed to generate summary."}
'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_code)
print("Successfully rewrote sentiment.py to use official google.genai SDK")
