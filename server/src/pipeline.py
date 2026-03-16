from livekit.agents.voice import Agent, AgentSession
from agent_triage import TriageAgent
import logging

logger = logging.getLogger("voice-agent")

def create_agent() -> tuple[Agent, AgentSession]:
    """Creates and configures the Voice Pipeline Agent and Session."""

    # We start with the Triage Agent to detect the language and perform handoff
    agent = TriageAgent()

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
