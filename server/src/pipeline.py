from livekit.agents.voice import Agent, AgentSession
from agent_unified import UnifiedAgent
import logging

logger = logging.getLogger("voice-agent")

def create_agent(caller_id: str = "unknown") -> tuple[Agent, AgentSession]:
    """Creates and configures the single, unified Voice Pipeline Agent and Session."""

    # Initialize the single multilingual agent
    agent = UnifiedAgent(caller_id=caller_id)

    session = AgentSession(
        stt=agent.stt,
        llm=agent.llm,
        tts=agent.tts
    )

    @session.on("user_state_changed")
    def _on_user_state_changed(state):
        if state == "speaking":
            logger.info("User started speaking...")
        elif state == "listening":
            logger.info("User stopped speaking. Processing intent...")

    @session.on("agent_state_changed")
    def _on_agent_state_changed(state):
        if state == "speaking":
            logger.info("Agent started speaking...")
        elif state == "listening":
            logger.info("Agent stopped speaking.")

    return agent, session
