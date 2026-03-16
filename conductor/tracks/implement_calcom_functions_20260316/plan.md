# Implementation Plan: Cal.com Function Calling

## Phase 1: Create Cal.com API Client
- [x] Task: Create `cal_client.py` to handle raw HTTP requests to Cal.com. a6954aa
    - [ ] Implement `get_available_slots(date_from, date_to, event_type_id)`.
    - [ ] Implement `create_booking(name, email, start_time, event_type_id)`.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Create Cal.com API Client' (Protocol in workflow.md)

## Phase 2: Define LiveKit AI Tools
- [ ] Task: Create `tools.py` with `@llm.ai_callable` decorators.
    - [ ] Define `AssistantTools` class inheriting from `llm.FunctionContext`.
    - [ ] Implement `check_availability` method wrapping the API client.
    - [ ] Implement `book_appointment` method wrapping the API client.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Define LiveKit AI Tools' (Protocol in workflow.md)

## Phase 3: Agent Integration
- [ ] Task: Inject tools into the Gemini Agent.
    - [ ] Update `pipeline.py` to import and pass `AssistantTools()` to the `Agent` constructor via `fnc_ctx`.
    - [ ] Update the `SYSTEM_PROMPT` to explicitly instruct the agent on when and how to use the booking tools.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Agent Integration' (Protocol in workflow.md)