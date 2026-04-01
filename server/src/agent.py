# -*- coding: utf-8 -*-
import logging
import os
import time
import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.rtc import RemoteParticipant
from livekit.api import LiveKitAPI
from livekit.protocol.egress import RoomCompositeEgressRequest, EncodedFileOutput, S3Upload
from core.pipeline import create_agent
from supabase import create_client, Client
import storage

load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"
logger = logging.getLogger("voice-agent")

# Initialize Supabase Client for call logging
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL", "")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_DEFAULT_KEY", "")
supabase: Client | None = None
if supabase_url and supabase_key:
    supabase = create_client(supabase_url, supabase_key)

# Global dictionary to track session state for logging purposes
session_states = {}

async def start_recording(room_name: str) -> str | None:
    """Starts a LiveKit Egress recording, with graceful failure if quota is exceeded."""
    livekit_url = os.getenv("LIVEKIT_URL")
    livekit_api_key = os.getenv("LIVEKIT_API_KEY")
    livekit_api_secret = os.getenv("LIVEKIT_API_SECRET")

    if not all([livekit_url, livekit_api_key, livekit_api_secret]):
        return None

    s3_endpoint = f"{supabase_url}/storage/v1/s3" if supabase_url else ""
    s3_access_key = os.getenv("SUPABASE_S3_ACCESS_KEY", "")
    s3_secret_key = os.getenv("SUPABASE_S3_SECRET_KEY", "")

    s3_upload = None
    if all([s3_endpoint, s3_access_key, s3_secret_key]):
        s3_upload = S3Upload(
            access_key=s3_access_key,
            secret=s3_secret_key,
            region="auto",
            endpoint=s3_endpoint,
            bucket="call_recordings"
        )

    lk_api = LiveKitAPI(livekit_url, livekit_api_key, livekit_api_secret)
    file_out = EncodedFileOutput(filepath=f"{room_name.replace('+', '')}.ogg", disable_manifest=True)
    if s3_upload:
        file_out.s3.CopyFrom(s3_upload)

    req = RoomCompositeEgressRequest(room_name=room_name, audio_only=True, file=file_out)

    try:
        info = await lk_api.egress.start_room_composite_egress(req)
        logger.info(f"Started egress for room {room_name}: {info.egress_id}")
        return info.egress_id
    except Exception as e:
        if "egress minutes exceeded" in str(e):
            logger.warning("Recording skipped: LiveKit Egress free minutes exceeded.")
        else:
            logger.error(f"Failed to start egress: {e}")
        return None
    finally:
        await lk_api.aclose()

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    start_time = time.time()
    asyncio.create_task(start_recording(ctx.room.name))

    session_states[ctx.room.name] = {
        "booked_appointment": False,
        "phone_number_collected": None,
        "end_call_requested": False
    }

    caller_id = "unknown"
    for p in ctx.room.remote_participants.values():
        if isinstance(p, RemoteParticipant):
            identity = p.identity
            caller_id = identity.split("@")[0].replace("sip:", "") if identity.startswith("sip:") else identity
            break

    agent = create_agent(caller_id=caller_id, room_name=ctx.room.name, session_states=session_states)
    await agent.start(ctx.room)

    # UPDATED: Using full Tamil script for the initial greeting as requested
    greeting = "Hello! வணக்கம்! Smile Garden-ல இருந்து பேசுறேன். How can I help you today?"
    agent.say(greeting, allow_interruptions=True)

    @agent.on("agent_state_changed")
    def on_agent_state_changed(state):
        if state == "listening":
            asyncio.create_task(check_for_hangup(ctx))

    async def shutdown_hook():
        await log_call_to_supabase(caller_id, start_time, ctx.room.name, agent)

    ctx.add_shutdown_callback(shutdown_hook)

async def check_for_hangup(ctx: JobContext):
    state = session_states.get(ctx.room.name, {})
    if state.get("end_call_requested"):
        await asyncio.sleep(1)
        await ctx.room.disconnect()

async def log_call_to_supabase(caller_id, start_time, room_name, agent):
    try:
        from sentiment import analyze_sentiment_and_summarize
        import storage
        duration = int(time.time() - start_time)
        state = session_states.get(room_name, {})
        outcome = "booked_appointment" if state.get("booked_appointment") else "assistance_provided"
        audio_url = storage.get_public_audio_url(f"{room_name.replace('+', '')}.ogg")

        transcript_lines = []
        if agent and hasattr(agent, 'chat_ctx') and agent.chat_ctx:
            messages = agent.chat_ctx.messages() if callable(agent.chat_ctx.messages) else agent.chat_ctx.messages
            for msg in messages:
                role = msg.role.capitalize() if hasattr(msg, 'role') else 'Unknown'
                content = getattr(msg, 'content', '')
                text = " ".join([c if isinstance(c, str) else getattr(c, "text", "") for c in content]) if isinstance(content, list) else content
                transcript_lines.append(f"{role}: {text}")

        transcript_text = "\n".join(transcript_lines) or "No transcript could be extracted."
        analysis = await analyze_sentiment_and_summarize(transcript_text)

        final_id = caller_id
        if final_id.startswith("user-") or final_id == "unknown":
            name, phone = analysis.get("name", "Unknown"), analysis.get("phone", "Unknown")
            if name != "Unknown" and phone != "Unknown": final_id = f"{name} ({phone})"
            elif phone != "Unknown": final_id = phone
            elif name != "Unknown": final_id = name

        if supabase:
            supabase.table("calls").insert({
                "caller_number": final_id,
                "duration_seconds": duration,
                "status": "completed",
                "outcome": outcome,
                "transcript": transcript_text,
                "sentiment": analysis.get("sentiment", "Neutral"),
                "summary": analysis.get("summary", "Call ended."),
                "audio_url": audio_url,
                "language": analysis.get("language", "English")
            }).execute()
        
        if room_name in session_states: del session_states[room_name]
    except Exception as e:
        logger.error(f"Error in log_call_to_supabase: {e}")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, agent_name="pallavi-cogentxai-core"))
