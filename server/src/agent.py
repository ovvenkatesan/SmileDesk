import logging
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.rtc import RemoteParticipant
from pipeline import create_agent

load_dotenv()
logger = logging.getLogger("voice-agent")

def prewarm(proc):
    """Prewarm the agent process."""
    logger.info("Prewarming voice agent process")

async def entrypoint(ctx: JobContext):
    """Entrypoint for the LiveKit agent worker."""
    logger.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Extract Caller ID from SIP participant identity or metadata if available
    caller_id = None
    for p in ctx.room.participants.values():
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
    agent, session = create_agent(caller_id=caller_id)
    
    await session.start(agent, room=ctx.room)
    logger.info("Agent connected and ready")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
