import os
import aiohttp
import json
import logging

logger = logging.getLogger("voice-agent-sentiment")

async def analyze_sentiment_and_summarize(transcript: str) -> dict:
    """
    Analyzes the call transcript using Gemini to extract sentiment and a short summary.
    Returns a dictionary with 'sentiment' and 'summary'.
    """
    if not transcript or not transcript.strip():
        return {"sentiment": "Neutral", "summary": "No transcript available."}

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.warning("GEMINI_API_KEY not set. Cannot perform sentiment analysis.")
        return {"sentiment": "Neutral", "summary": "API Key missing."}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
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

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "response_mime_type": "application/json"
        }
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                if resp.status != 200:
                    logger.error(f"Gemini API returned status {resp.status}")
                    return {"sentiment": "Neutral", "summary": "Sentiment analysis failed."}
                
                data = await resp.json()
                text_response = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")
                
                result = json.loads(text_response)
                return {
                    "sentiment": result.get("sentiment", "Neutral"),
                    "summary": result.get("summary", "Summary unavailable.")
                }
    except Exception as e:
        logger.error(f"Error during sentiment analysis: {e}")
        return {"sentiment": "Neutral", "summary": "Error during analysis."}
