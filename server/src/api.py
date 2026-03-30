import os
import uuid
import logging
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from typing import List, Dict, Any
from pydantic import BaseModel
from livekit.api import AccessToken, VideoGrants
from supabase import create_client, Client
from livekit import api as livekit_api_module

# Relative import fix
try:
    from cal_client import CalClient
except ImportError:
    from .cal_client import CalClient

load_dotenv()

app = FastAPI(title="Smile Garden Voice AI API")

# Initialize Supabase Client
supabase_url: str = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
supabase_key: str = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY", "")
supabase: Client | None = None
if supabase_url and supabase_key:
    supabase = create_client(supabase_url, supabase_key)

# Setup CORS for the dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Smile Garden Voice AI API is running"}

@app.post("/api/vobiz-webhook")
async def vobiz_webhook():
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial>
        <User>sip:smilegarden-j23vmzmq.livekit.cloud</User>
    </Dial>
</Response>"""
    return Response(content=xml_content, media_type="application/xml")

@app.get("/api/token")
async def get_token():
    livekit_url = os.getenv("LIVEKIT_URL")
    livekit_api_key = os.getenv("LIVEKIT_API_KEY")
    livekit_api_secret = os.getenv("LIVEKIT_API_SECRET")

    if not all([livekit_url, livekit_api_key, livekit_api_secret]):
        raise HTTPException(status_code=500, detail="LiveKit credentials not configured on server")

    room_name = f"web-room-{uuid.uuid4().hex[:8]}"
    participant_identity = f"user-{uuid.uuid4().hex[:8]}"

    grant = VideoGrants(room_join=True, room=room_name)
    access_token = AccessToken(
        livekit_api_key, livekit_api_secret
    ).with_identity(participant_identity).with_name("Web User").with_grants(grant).to_jwt()

    try:
        lk_api = livekit_api_module.LiveKitAPI(livekit_url, livekit_api_key, livekit_api_secret)
        await lk_api.agent_dispatch.create_dispatch(
            livekit_api_module.CreateAgentDispatchRequest(
                agent_name="pallavi-voice-agent",
                room=room_name
            )
        )
    except Exception as e:
        print(f"Error dispatching agent: {e}")
    finally:
        await lk_api.aclose()

    return {
        "token": access_token,
        "url": livekit_url,
        "room": room_name
    }

@app.get("/api/dashboard/roi")
def get_roi_snapshot():
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        response = supabase.table("calls").select("*").execute()
        calls = response.data
        total_calls = len(calls)
        leads_saved = supabase.table("bookings").select("id", count="exact").execute().count or 0
        conversion_rate = round((leads_saved / total_calls * 100) if total_calls > 0 else 0, 1)

        return {
            "leads_saved": leads_saved,
            "estimated_value": leads_saved * 200,
            "period": "All Time",
            "total_calls": total_calls,
            "conversion_rate": conversion_rate
        }
    except Exception as e:
        print(f"Error fetching ROI data: {e}")
        return {
            "leads_saved": 0, "estimated_value": 0, "period": "All Time", "total_calls": 0, "conversion_rate": 0
        }

@app.get("/api/dashboard/agent-status")
def get_agent_status():
    return {
        "status": "online",
        "last_active": datetime.now().isoformat()
    }

@app.get("/api/dashboard/calls")
def get_call_logs():
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        response = supabase.table("calls").select("*").order("start_time", desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching calls: {e}")
        raise HTTPException(status_code=500, detail="Error fetching calls from database")

@app.get("/api/dashboard/calls/{call_id}")
def get_call_details(call_id: str):
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        response = supabase.table("calls").select("*").eq("id", call_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Call not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching call details: {e}")
        raise HTTPException(status_code=500, detail="Error fetching call details")

async def sync_bookings():
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        cal = CalClient()
        res = await cal.get_all_bookings()
        bookings_data = res.get("data", [])
        for b in bookings_data:
            b_id = b.get("uid", b.get("id"))
            b_email = b.get("attendee", {}).get("email", "unknown")
            b_phone = b_email.split("@")[0] if "@smilegarden.dummy" in b_email else b_email
            b_start = b.get("start", b.get("startTime"))
            b_status = b.get("status", "Accepted")
            b_type = b.get("eventType", {}).get("title", "Consultation")

            supabase.table("bookings").upsert({
                "id": b_id,
                "patient_number": b_phone,
                "date": b_start,
                "type": b_type,
                "status": b_status
            }, on_conflict="id").execute()
        return {"status": "success", "synced": len(bookings_data)}
    except Exception as e:
        print(f"Error syncing bookings: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/dashboard/sync")
async def post_sync():
    return await sync_bookings()

@app.get("/api/dashboard/bookings")
def get_booking_history():
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        response = supabase.table("bookings").select("*").order("date", desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching bookings: {e}")
        raise HTTPException(status_code=500, detail="Error fetching bookings from database")

@app.get("/api/dashboard/advanced-stats")
def get_advanced_stats():
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        # 1. Fetch Calls for After-Hours and Language
        calls_res = supabase.table("calls").select("start_time, language").execute()
        calls = calls_res.data
        
        # 2. Fetch Bookings for New Patients and No-Shows
        bookings_res = supabase.table("bookings").select("patient_number, date, is_no_show, status").execute()
        bookings = bookings_res.data
        
        # Logic for After-Hours (9 AM - 6 PM IST)
        def is_after_hours(dt_str):
            if not dt_str: return False
            try:
                # Handle standard ISO formats
                clean_time = dt_str.replace("Z", "+00:00")
                dt = datetime.fromisoformat(clean_time)
                ist_dt = dt.astimezone(timezone(timedelta(hours=5, minutes=30)))
                return ist_dt.hour < 9 or ist_dt.hour >= 18
            except Exception:
                return False

        after_hours_count = sum(1 for c in calls if is_after_hours(c.get("start_time")))
        
        # Logic for Language Breakdown
        lang_map = {}
        for c in calls:
            lang = c.get("language", "English")
            lang_map[lang] = lang_map.get(lang, 0) + 1
        
        # Logic for New Patients (Unique numbers)
        unique_patients = len(set(b.get("patient_number") for b in bookings if b.get("patient_number")))
        
        # Logic for No-Shows/Cancellations
        no_shows = sum(1 for b in bookings if b.get("is_no_show") or b.get("status") in ["Cancelled", "Rejected"])
        
        # Logic for Scheduling Efficiency (Mocked for now)
        efficiency = 78.2 

        return {
            "after_hours_calls": after_hours_count,
            "language_breakdown": lang_map,
            "new_patients": unique_patients,
            "no_shows": no_shows,
            "scheduling_efficiency": efficiency,
            "total_bookings": len(bookings),
            "total_calls": len(calls)
        }
    except Exception as e:
        print(f"Error fetching advanced stats: {e}")
        raise HTTPException(status_code=500, detail="Error calculating advanced metrics")

@app.post("/api/dashboard/bookings/{booking_id}/no-show")
def mark_no_show(booking_id: str, is_no_show: bool = True):
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    try:
        response = supabase.table("bookings").update({"is_no_show": is_no_show}).eq("id", booking_id).execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        print(f"Error marking no-show: {e}")
        raise HTTPException(status_code=500, detail="Error updating booking")
