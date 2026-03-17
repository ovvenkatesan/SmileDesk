from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI(title="Smile Garden Voice AI API")

# Setup CORS for the dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to dashboard domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Smile Garden Voice AI API is running"}

@app.get("/api/dashboard/roi")
def get_roi_snapshot():
    # Mock data
    return {
        "leads_saved": 42,
        "estimated_value": 8400, # e.g. 42 leads * $200 average value
        "period": "Last 30 Days"
    }

@app.get("/api/dashboard/agent-status")
def get_agent_status():
    # Mock data
    return {
        "status": "online",
        "last_active": datetime.now().isoformat()
    }

@app.get("/api/dashboard/calls")
def get_call_logs():
    # Mock data
    now = datetime.now()
    return [
        {
            "id": "1",
            "caller_number": "+1234567890",
            "start_time": (now - timedelta(hours=2)).isoformat(),
            "duration_seconds": 145,
            "status": "completed",
            "outcome": "booked_appointment"
        },
        {
            "id": "2",
            "caller_number": "+1987654321",
            "start_time": (now - timedelta(hours=5)).isoformat(),
            "duration_seconds": 65,
            "status": "completed",
            "outcome": "questions_answered"
        }
    ]

@app.get("/api/dashboard/calls/{call_id}")
def get_call_details(call_id: str):
    # Mock data
    if call_id == "1":
        return {
            "id": "1",
            "transcript": "Agent: Hello, Smile Garden Dental. How can I help you today?\nCaller: Hi, I'm in a lot of pain and need to see a dentist as soon as possible.\nAgent: I'm so sorry to hear that. I can help you schedule an emergency appointment. Let me check our availability.",
            "sentiment": "Anxious",
            "summary": "Patient called with dental pain and scheduled an emergency appointment."
        }
    elif call_id == "2":
        return {
            "id": "2",
            "transcript": "Agent: Welcome to Smile Garden Dental. How may I assist you?\nCaller: Hi, I just wanted to ask what time you open tomorrow?\nAgent: We open at 8:00 AM tomorrow. Would you like to schedule an appointment?",
            "sentiment": "Neutral",
            "summary": "Patient inquired about opening hours."
        }
    else:
        raise HTTPException(status_code=404, detail="Call not found")

@app.get("/api/dashboard/bookings")
def get_booking_history():
    # Mock data
    return [
        {"id": 101, "date": "2026-03-18T09:00:00", "type": "Emergency", "status": "Confirmed"},
        {"id": 102, "date": "2026-03-19T14:00:00", "type": "Checkup", "status": "Rescheduled"},
        {"id": 103, "date": "2026-03-20T10:30:00", "type": "Consultation", "status": "Confirmed"}
    ]
