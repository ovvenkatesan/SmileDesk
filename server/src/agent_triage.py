from livekit.agents.voice import Agent
from livekit.plugins import deepgram, google
from livekit.agents import llm
import logging

logger = logging.getLogger("voice-agent.triage")

def get_triage_prompt() -> str:
    return """You are Pallavi, the Smile Garden Voice AI Agent. You are the initial greeter for the clinic.
Your ONLY job is to figure out if the patient wants to speak English or Tamil.

When the user speaks:
1. Greet them warmly and ask how you can help them. Example: "Hello! Welcome to Smile Garden Dental. Vanakkam! How can I help you today?"
2. Based on their response, immediately use either the `transfer_to_english` or `transfer_to_tamil` tool to transfer the call to the appropriate specialist agent.
3. Do NOT try to book appointments or answer dental questions yourself. Just transfer the call.
"""

class TriageAgent(Agent):
    def __init__(self):
        stt = deepgram.STT(language="multi", model="nova-3") # Listen to both initially
        llm_model = google.LLM(model="gemini-3.1-flash-lite-preview")
        tts = deepgram.TTS(model="aura-2-asteria-en") # Use english voice for initial quick greeting
        
        super().__init__(
            instructions=get_triage_prompt(),
            stt=stt,
            llm=llm_model,
            tts=tts,
        )

    @llm.function_tool(description="Transfer the call to the English speaking agent.")
    async def transfer_to_english(self):
        logger.info("Transferring to English Agent")
        # Defer import to avoid circular dependencies
        from agent_english import EnglishAgent
        
        # Copy the chat context, but exclude the TriageAgent's instructions
        new_ctx = self.chat_ctx.copy(exclude_instructions=True)
        return EnglishAgent(chat_ctx=new_ctx), "Transferring to English specialist"

    @llm.function_tool(description="Transfer the call to the Tamil speaking agent.")
    async def transfer_to_tamil(self):
        logger.info("Transferring to Tamil Agent")
        # Defer import to avoid circular dependencies
        from agent_tamil import TamilAgent
        
        # Copy the chat context, but exclude the TriageAgent's instructions
        new_ctx = self.chat_ctx.copy(exclude_instructions=True)
        return TamilAgent(chat_ctx=new_ctx), "Transferring to Tamil specialist"
