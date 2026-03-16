import logging
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice import Agent as VoiceAgent
from livekit.plugins import deepgram, google

load_dotenv()
logger = logging.getLogger("voice-agent")

def prewarm(proc):
    """Prewarm the agent process."""
    logger.info("Prewarming voice agent process")

async def entrypoint(ctx: JobContext):
    """Entrypoint for the LiveKit agent worker."""
    logger.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Initialize Voice Assistant with basic configurations
    # We will expand this in the next task with actual models
    logger.info("Agent connected and ready")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
