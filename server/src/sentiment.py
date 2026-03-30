import os
import json
import logging
from google import genai
from google.genai import types

logger = logging.getLogger("voice-agent-sentiment")

async def analyze_sentiment_and_summarize(transcript: str) -> dict:
    if not transcript or not transcript.strip():
        return {"sentiment": "Neutral", "summary": "No transcript available.", "name": "Unknown", "phone": "Unknown", "language": "English"}

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return {"sentiment": "Neutral", "summary": "API Key missing.", "name": "Unknown", "phone": "Unknown", "language": "English"}

    # Refined prompt to prioritize actual spoken language detection
    prompt = f"""
    Analyze the following dental clinic call transcript.
    
    Extract the following five details:
    1. A single word representing the caller's sentiment (e.g., Anxious, Neutral, Angry, Satisfied, Urgent).
    2. A brief 1-2 sentence summary of the call's outcome.
    3. The caller's Name (if mentioned).
    4. The caller's Phone Number (if mentioned).
    5. The primary language SPOKEN by the User (the Caller). 
       - If they speak mostly Tamil script, return "Tamil".
       - If they speak a mix of English and Tamil, return "Tanglish".
       - If they speak mostly English, return "English".

    Transcript:
    {transcript}

    Respond ONLY in valid JSON format like this:
    {{"sentiment": "Anxious", "summary": "Patient booked an emergency appointment.", "name": "Venkatesh", "phone": "9697012480", "language": "Tamil"}}
    """

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-3.1-flash-lite-preview',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )

        if not response.text:
            return {"sentiment": "Neutral", "summary": "Analysis empty.", "name": "Unknown", "phone": "Unknown", "language": "English"}

        result = json.loads(response.text)
        
        name = result.get("name", "Unknown")
        phone = result.get("phone", "Unknown")
        language = result.get("language", "English")
        base_summary = result.get("summary", "Summary unavailable.")

        prefix = ""
        if name != "Unknown": prefix = f"[{name}] "
        elif phone != "Unknown": prefix = f"[{phone}] "

        return {
            "sentiment": result.get("sentiment", "Neutral"),
            "summary": prefix + base_summary,
            "name": name,
            "phone": phone,
            "language": language
        }
    except Exception as e:
        logger.error(f"Error during sentiment analysis: {e}")
        return {"sentiment": "Neutral", "summary": "Failed to generate summary.", "name": "Unknown", "phone": "Unknown", "language": "English"}