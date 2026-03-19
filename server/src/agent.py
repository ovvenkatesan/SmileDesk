import logging
import os
import time
import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.rtc import RemoteParticipant
from livekit.api import LiveKitAPI
from livekit.protocol.egress import RoomCompositeEgressRequest, EncodedFileOutput, S3Upload
from pipeline import create_agent
from supabase import create_client, Client
import storage

load_dotenv()
logger = logging.getLogger("voice-agent")

# Initialize Supabase Client for call logging
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY", "")
supabase: Client | None = None
if supabase_url and supabase_key:
    supabase = create_client(supabase_url, supabase_key)

# Global dictionary to track session state for logging purposes
# Key: room_name, Value: dict of session metadata
session_states = {}

async def start_recording(room_name: str) -> str | None:
    """Starts a LiveKit Egress recording for the given room, uploading to Supabase S3."""
    livekit_url = os.getenv("LIVEKIT_URL")
    livekit_api_key = os.getenv("LIVEKIT_API_KEY")
    livekit_api_secret = os.getenv("LIVEKIT_API_SECRET")
    
    if not all([livekit_url, livekit_api_key, livekit_api_secret]):
        logger.error("LiveKit credentials missing. Cannot start recording.")
        return None

    # Supabase S3 settings (uses AWS S3 protocol under the hood)
    # The endpoint is usually https://<project-ref>.supabase.co/storage/v1/s3
    s3_endpoint = f"{supabase_url}/storage/v1/s3" if supabase_url else ""
    s3_access_key = os.getenv("SUPABASE_S3_ACCESS_KEY", "")
    s3_secret_key = os.getenv("SUPABASE_S3_SECRET_KEY", "")
    
    if not all([s3_endpoint, s3_access_key, s3_secret_key]):
        logger.warning("Supabase S3 credentials not fully configured. Using mock local file for Egress.")
        s3_upload = None
    else:
        s3_upload = S3Upload(
            access_key=s3_access_key,
            secret=s3_secret_key,
            region="auto",
            endpoint=s3_endpoint,
            bucket="call_recordings"
        )
        
    lk_api = LiveKitAPI(livekit_url, livekit_api_key, livekit_api_secret)
    
    # We output to mp3
    file_out = EncodedFileOutput(
        filepath=f"{room_name}.mp3",
        disable_manifest=True
    )
    if s3_upload:
        file_out.s3 = s3_upload

    req = RoomCompositeEgressRequest(
        room_name=room_name,
        audio_only=True,
        file=file_out
    )
    
    try:
        info = await lk_api.egress.start_room_composite_egress(req)
        logger.info(f"Started egress for room {room_name}: {info.egress_id}")
        return info.egress_id
    except Exception as e:
        logger.error(f"Failed to start egress: {e}")
        return None
    finally:
        await lk_api.aclose()

def prewarm(proc):
    """Prewarm the agent process."""
    logger.info("Prewarming voice agent process")

async def entrypoint(ctx: JobContext):
    """Entrypoint for the LiveKit agent worker."""
    logger.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Track call start time
    start_time = time.time()
    
    # Start recording
    asyncio.create_task(start_recording(ctx.room.name))
    
    # Initialize session state for this room
    session_states[ctx.room.name] = {
        "booked_appointment": False,
        "phone_number_collected": None,
        "end_call_requested": False
    }

    # Extract Caller ID from SIP participant identity or metadata if available
    caller_id = None
    for p in ctx.room.remote_participants.values():
        if isinstance(p, RemoteParticipant):
            # SIP participants typically have identities like sip:+1234567890@domain
            identity = p.identity
            if identity.startswith("sip:"):
                caller_id = identity.split("@")[0].replace("sip:", "")
            else:
                caller_id = identity # Fallback to identity string
            logger.info(f"Identified remote caller: {caller_id}")
            break
            
    if not caller_id:
        logger.info("No explicit caller ID found, treating as unknown web user.")
        caller_id = "unknown"

    # Initialize Voice Assistant with configured STT and LLM, passing caller context
    # Pass the room name down so tools can update the session state
    agent, session = create_agent(caller_id=caller_id, room_name=ctx.room.name)
    
    await session.start(agent, room=ctx.room)
    logger.info("Agent connected and ready")
    
    # Hook into agent speech completion to check if we should hang up
    @agent.on("agent_speech_committed")
    def on_agent_speech_committed(msg):
        # We check state here because we want to let the agent finish saying "Goodbye" 
        # before we aggressively cut the connection.
        asyncio.create_task(check_for_hangup(ctx))

    # Proactively greet the user
    await session.say("Welcome to Smile Garden Dental clinic, how can I help you today?", allow_interruptions=False)

    # Hook into the disconnection event to log the call to Supabase
    ctx.room.on("disconnected", lambda: log_call_to_supabase(caller_id, start_time, ctx.room.name))

async def check_for_hangup(ctx: JobContext):
    """Checks if the tool requested a call end, and disconnects after a short delay."""
    state = session_states.get(ctx.room.name, {})
    if state.get("end_call_requested"):
        logger.info("End call requested. Waiting 3 seconds for TTS to finish before disconnecting...")
        await asyncio.sleep(3) # Give the TTS a moment to actually play the goodbye audio
        logger.info("Disconnecting room.")
        await ctx.room.disconnect()

def log_call_to_supabase(caller_id, start_time, room_name):
    duration = int(time.time() - start_time)
    
    # Retrieve session state
    state = session_states.get(room_name, {})
    
    # Determine outcome based on what happened during the call
    outcome = "booked_appointment" if state.get("booked_appointment") else "assistance_provided"
    
    # Get the audio URL generated by LiveKit Egress (configured in start_recording)
    audio_url = storage.get_public_audio_url(f"{room_name}.mp3")
    
    # If the user called from the web widget but provided a phone number during booking,
    # use that phone number for the call log instead of the random "user-xxx" ID.
    final_caller_id = caller_id
    if caller_id.startswith("user-") and state.get("phone_number_collected"):
        final_caller_id = state.get("phone_number_collected")
        
    logger.info(f"Call disconnected. Logging to Supabase. Duration: {duration}s. Outcome: {outcome}")
    
    if supabase:
        try:
            supabase.table("calls").insert({
                "caller_number": final_caller_id,
                "duration_seconds": duration,
                "status": "completed",
                "outcome": outcome,
                "sentiment": "Neutral",
                "summary": "Call ended.",
                "audio_url": audio_url
            }).execute()
            logger.info("Successfully logged call to Supabase.")
        except Exception as e:
            logger.error(f"Failed to log call to Supabase: {e}")
            
    # Cleanup session state
    if room_name in session_states:
        del session_states[room_name]

if __name__ == "__main__":
    cli.run_app(WorkerOptions(
        entrypoint_fnc=entrypoint, 
        prewarm_fnc=prewarm,
        agent_name="pallavi-voice-agent"
    ))
