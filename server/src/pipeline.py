from livekit.agents.voice import Agent, AgentSession
from agent_unified import UnifiedAgent
import logging

logger = logging.getLogger("voice-agent")

def create_agent(caller_id: str = "unknown", room_name: str = "unknown", session_states: dict = None) -> tuple[Agent, AgentSession]:
    """Creates and configures the single, unified Voice Pipeline Agent and Session."""
    
    agent = UnifiedAgent(caller_id=caller_id, room_name=room_name, session_states=session_states)
    
    # Initialize empty session - agent will be passed during session.start()
    session = AgentSession()

    # Adding explicit debug logs to catch communication drops
    @session.on("user_started_speaking")
    def _on_user_started_speaking():
        logger.info(">>> USER STARTED SPEAKING")

    @session.on("user_stopped_speaking")
    def _on_user_stopped_speaking():
        logger.info("<<< USER STOPPED SPEAKING. Processing intent...")

    @session.on("agent_started_speaking")
    def _on_agent_started_speaking():
        logger.info("AGENT STARTED SPEAKING")

    @session.on("agent_stopped_speaking")
    def _on_agent_stopped_speaking():
        logger.info("AGENT STOPPED SPEAKING")

    return agent, session
