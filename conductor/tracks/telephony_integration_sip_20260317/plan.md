# Implementation Plan: Telephony Integration (SIP)

## Phase 1: SIP Ingress Configuration Documentation
- [ ] Task: Document LiveKit Cloud SIP Configuration.
    - [ ] Create a markdown guide in `docs/sip-setup.md` detailing the CLI/Dashboard steps required to configure SIP Ingress on LiveKit Cloud for Vobiz.
    - [ ] Include details on how LiveKit SIP Dispatch rules map incoming phone numbers to LiveKit Rooms.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: SIP Ingress Configuration Documentation' (Protocol in workflow.md)

## Phase 2: Python Worker Updates for SIP
- [ ] Task: Extract Caller ID from metadata.
    - [ ] Update `server/src/agent.py` to inspect the `ctx.room.participants` or connection metadata for the SIP caller's phone number upon connection.
    - [ ] Pass the extracted phone number as context to `create_agent()` in `pipeline.py`.
- [ ] Task: Update Agent Prompt.
    - [ ] Update `server/src/pipeline.py` to accept the `caller_id` variable.
    - [ ] Modify the initial prompt instructions to greet the user based on whether their number is known or unknown.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Python Worker Updates for SIP' (Protocol in workflow.md)

## Phase 3: Call Transfer Capability
- [ ] Task: Implement `transfer_call` tool.
    - [ ] Add a new `@llm.function_tool` in `server/src/tools.py` named `transfer_call`.
    - [ ] Implement the LiveKit Server API logic to issue a SIP Refer/Transfer command to the participant. *(Requires `livekit-api` package)*
- [ ] Task: Register tool with the Agent.
    - [ ] Ensure the new tool is passed to the Gemini LLM configuration.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Call Transfer Capability' (Protocol in workflow.md)