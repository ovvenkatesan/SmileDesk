# Track Specification: Implement Appointment Rescheduling and Cancellations

## Overview
This track extends the Cal.com integration to allow the Smile Garden Voice AI Agent to handle modifications to existing appointments. Patients frequently need to reschedule or cancel their visits, and the AI should handle this gracefully.

## Objectives
- Extend `CalClient` to support fetching an existing booking by email or ID, canceling a booking, and rescheduling a booking.
- Add corresponding `@llm.function_tool` decorated functions in `tools.py` for Gemini to use.
- Update the system prompt to instruct the agent on how to handle rescheduling and cancellation requests securely and empathetically.

## Scope
- **In Scope:** `cancel_appointment` function, `reschedule_appointment` function, updating `tools.py`, updating `cal_client.py`.
- **Out of Scope:** Sending manual confirmation emails (handled by Cal.com automatically).

## Technical Details
- **API Endpoints:** Cal.com API endpoints for GET /bookings, DELETE /bookings/{id}, and POST /bookings/{id}/reschedule.
- **Environment:** Relies on existing `CAL_API_KEY`.