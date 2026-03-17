# Specification: Telephony Integration (SIP)

## Overview
Integrate the Smile Garden Voice AI Agent with traditional telephony using SIP trunking (Vobiz). This track configures LiveKit Cloud to accept incoming SIP calls, routes them to the Python agent worker, and equips the agent with context and call management tools.

## Functional Requirements
- **SIP Ingress via LiveKit Cloud:** Configure LiveKit Cloud to act as the SIP endpoint, receiving calls forwarded from the Vobiz SIP trunk.
- **Caller ID Extraction:** The LiveKit Python worker must extract the caller's phone number (Caller ID) from the incoming SIP participant metadata/headers.
- **Contextual Greeting:** The agent should use the extracted phone number to look up the patient (or politely greet an unknown number) right at the start of the call.
- **Call Transfer Capability:** Implement a new tool for the Gemini agent that allows it to transfer the active SIP call to a human receptionist's phone number when requested by the caller or when the agent cannot resolve the issue.

## Non-Functional Requirements
- **Low Latency:** Ensure the "Zero-Wait Telephony" promise by keeping the routing from Vobiz -> LiveKit Cloud -> Python Worker as direct as possible.
- **Graceful Failure:** If the SIP transfer fails, the agent must be notified and inform the user.

## Acceptance Criteria
- [ ] LiveKit Cloud SIP Ingress is configured and verified to receive calls.
- [ ] When a call is received, the Python worker logs the correct Caller ID.
- [ ] The agent's initial prompt incorporates the caller's phone number.
- [ ] A `@llm.function_tool` named `transfer_call` is implemented.
- [ ] The agent successfully executes a call transfer to a designated test number during a live test.

## Out of Scope
- Provisioning the actual Vobiz phone numbers (assumed to be handled out-of-band by the clinic owner).
- Deep CRM integration for the caller ID lookup (for this track, we just extract the number and pass it to the prompt; database lookup logic will be separate).