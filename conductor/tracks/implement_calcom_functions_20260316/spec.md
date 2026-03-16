# Track Specification: Implement Cal.com Function Calling

## Overview
This track implements the "business logic" layer of the Dynamic State Engine. By giving the Gemini LLM access to external functions, the agent will transform from a simple conversational bot into a functional concierge capable of looking up clinic availability and executing real bookings.

## Objectives
- Integrate the Cal.com REST API into the Python backend.
- Define LiveKit `@llm.ai_callable()` functions for checking availability and booking appointments.
- Update the Agent initialization to inject these tools into the Gemini context.
- Ensure proper error handling (e.g., if a requested time slot is unavailable, the agent should gracefully ask for an alternative).

## Scope
- **In Scope:** `check_availability` function, `book_appointment` function, Cal.com API communication.
- **Out of Scope:** Rescheduling/Canceling appointments (will handle in a future enhancement track if needed), payment processing.

## Technical Details
- **API Endpoint:** Cal.com Public API (v1 or v2).
- **Environment:** Requires `CAL_API_KEY` (already present in `.env`).
- **Implementation:** Create a new `tools.py` module containing a class extending `livekit.agents.llm.FunctionContext`.