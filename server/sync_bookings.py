import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

CAL_API_KEY = os.getenv("CAL_API_KEY")
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY")

if not all([CAL_API_KEY, SUPABASE_URL, SUPABASE_KEY]):
    print("Error: Missing environment variables. Please check your .env file.")
    exit(1)

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def fetch_all_cal_bookings():
    """Fetches all recent bookings from Cal.com API v2"""
    base_url = "https://api.cal.com/v2/bookings"
    headers = {
        "Authorization": f"Bearer {CAL_API_KEY}",
        "cal-api-version": "2024-08-13",
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(base_url) as response:
            if response.status != 200:
                text = await response.text()
                # Try v1 fallback if v2 fails
                print(f"v2 API returned: {response.status}. Attempting v1 fallback...")
                return await fetch_all_cal_bookings_v1()
            
            data = await response.json()
            if data and isinstance(data, dict) and "data" in data:
                return data["data"]
            return data if isinstance(data, list) else []

async def fetch_all_cal_bookings_v1():
    """Fallback to fetch all bookings using Cal.com v1 API"""
    url = f"https://api.cal.com/v1/bookings?apiKey={CAL_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Failed to fetch from v1 API as well: {await response.text()}")
                return []
            data = await response.json()
            return data.get("bookings", [])

async def sync():
    print("Fetching bookings from Cal.com...")
    bookings = await fetch_all_cal_bookings()
    
    if not bookings:
        print("No bookings found in Cal.com.")
        return

    print(f"Found {len(bookings)} bookings. Syncing to Supabase...")
    
    synced_count = 0
    skipped_count = 0
    
    for b in bookings:
        try:
            # Handle both v1 and v2 payload structures
            start_time = b.get("startTime", b.get("start"))
            if not start_time:
                continue
                
            status = b.get("status", "ACCEPTED")
            
            # Extract attendee info
            attendees = b.get("attendees", [])
            patient_identifier = "Unknown"
            
            if attendees and len(attendees) > 0:
                attendee = attendees[0]
                email = attendee.get("email", "")
                
                # Check if it's our dummy email system (e.g., 9898433433@smilegarden.dummy)
                if email.endswith("@smilegarden.dummy"):
                    patient_identifier = email.replace("@smilegarden.dummy", "")
                else:
                    patient_identifier = email
                    
            # Determine event type
            event_type_str = "Consultation"
            if b.get("title") and "Emergency" in b.get("title", ""):
                event_type_str = "Emergency"
                
            # Check if this booking already exists in Supabase to avoid duplicates
            existing = supabase.table("bookings").select("*").eq("date", start_time).eq("patient_number", patient_identifier).execute()
            
            if not existing.data:
                # Insert into Supabase
                supabase.table("bookings").insert({
                    "patient_number": patient_identifier,
                    "date": start_time,
                    "type": event_type_str,
                    "status": status.capitalize()
                }).execute()
                print(f"✅ Synced: {patient_identifier} at {start_time}")
                synced_count += 1
            else:
                skipped_count += 1
                
        except Exception as e:
            print(f"❌ Error processing booking: {e}")
            
    print(f"\nSync complete! Added {synced_count} new bookings. Skipped {skipped_count} existing bookings.")

if __name__ == "__main__":
    asyncio.run(sync())