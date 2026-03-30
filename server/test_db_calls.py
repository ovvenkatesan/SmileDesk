import requests
import json
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv("D:\Projects\BMad\SmileGardenVoiceAgent\server\.env")
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY", "")
supabase = create_client(supabase_url, supabase_key)

response = supabase.table("calls").select("start_time").order("start_time", desc=True).execute()
print(json.dumps(response.data[:5], indent=2))
