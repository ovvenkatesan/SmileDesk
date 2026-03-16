# Implementation Plan: Appointment Rescheduling and Cancellations

## Phase 1: Update API Client (`cal_client.py`)
- [x] Task: Add methods to manage existing bookings. 6c557da
    - [x] Implement `get_booking_by_email(email)`.
    - [x] Implement `cancel_booking(booking_id, cancel_reason)`.
    - [x] Implement `reschedule_booking(booking_id, new_start_time)`.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Update API Client' (Protocol in workflow.md) [checkpoint: b66d965]

## Phase 2: Update AI Tools (`tools.py`)
- [ ] Task: Expose new capabilities to Gemini.
    - [ ] Add `@llm.function_tool` for `cancel_appointment`.
    - [ ] Add `@llm.function_tool` for `reschedule_appointment`.
    - [ ] Include logic to first lookup the booking ID using email if the patient doesn't know their ID.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Update AI Tools' (Protocol in workflow.md)

## Phase 3: Agent Prompt Integration
- [ ] Task: Update `pipeline.py` system prompt.
    - [ ] Instruct the agent on the exact flow for canceling and rescheduling (e.g. asking for email to find the booking, confirming details, then executing the action).
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Agent Prompt Integration' (Protocol in workflow.md)