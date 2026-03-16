import logging
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
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

    # Initialize Voice Assistant with configured STT and LLM
    agent = create_agent()
    
    agent.start(ctx.room)
    logger.info("Agent connected and ready")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
