import os
import logging
from supabase import create_client, Client

logger = logging.getLogger("voice-agent-storage")

def get_supabase_client() -> Client | None:
    supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
    supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY", "")
    if supabase_url and supabase_key:
        return create_client(supabase_url, supabase_key)
    return None

def upload_audio_to_supabase(file_path: str, destination_name: str, bucket_name: str = "call_recordings") -> str | None:
    """
    Manually upload a local MP3 file to Supabase Storage.
    Returns the public URL if successful.
    """
    client = get_supabase_client()
    if not client:
        logger.error("Supabase client not initialized. Cannot upload audio.")
        return None

    try:
        with open(file_path, "rb") as f:
            res = client.storage.from_(bucket_name).upload(destination_name, f, {"content-type": "audio/mpeg"})
            logger.info(f"Successfully uploaded {destination_name} to {bucket_name}")
            return get_public_audio_url(destination_name, bucket_name)
    except Exception as e:
        logger.error(f"Failed to upload audio to Supabase: {e}")
        return None

def get_public_audio_url(file_name: str, bucket_name: str = "call_recordings") -> str | None:
    """
    Get the public URL for a file in Supabase Storage.
    """
    client = get_supabase_client()
    if not client:
        return None
    try:
        return client.storage.from_(bucket_name).get_public_url(file_name)
    except Exception as e:
        logger.error(f"Failed to generate public URL: {e}")
        return None
