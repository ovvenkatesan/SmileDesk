# -*- coding: utf-8 -*-
import logging
from core.agent_factory import CogentXAIAgent
from clients.smile_garden.config import get_smile_garden_persona
from tools import AssistantTools

logger = logging.getLogger("cogentxai.pipeline")

def create_agent(caller_id: str = "unknown", 
                 room_name: str = "unknown", 
                 session_states: dict = None):
    
    # LOGIC: Load the correct client config based on room name or other metadata
    # For now, default to Smile Garden (Pallavi)
    persona_config = get_smile_garden_persona(caller_id)
    
    # Initialize the tools for this specific agent
    tools_instance = AssistantTools(room_name=room_name, session_states=session_states)
    
    # Create the agent using the factory
    agent = CogentXAIAgent(
        persona_config=persona_config,
        tools=[
            tools_instance.check_availability,
            tools_instance.book_appointment,
            tools_instance.get_bookings,
            tools_instance.cancel_appointment,
            tools_instance.reschedule_appointment,
            tools_instance.transfer_call,
            tools_instance.end_call
        ]
    )
    
    return agent
