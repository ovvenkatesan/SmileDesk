# Implementation Plan: Multi-Agent Language Routing

## Phase 1: Define Specialized Agents
- [x] Task: Create `EnglishAgent` and `TamilAgent` classes.
    - [x] Create specialized `get_english_prompt()` and `get_tamil_prompt()` functions.
    - [x] Configure `EnglishAgent` to use Deepgram TTS (e.g., aura-asteria-en).
    - [x] Configure `TamilAgent` to use Sarvam TTS.
    - [x] Both agents should have access to `AssistantTools` for booking.

## Phase 2: Create Triage Agent & Handoff Tools
- [x] Task: Implement the `TriageAgent`.
    - [x] Write a prompt for the TriageAgent to greet in both languages and determine preference.
    - [x] Implement `@llm.function_tool` methods `transfer_to_english` and `transfer_to_tamil`.
    - [x] Ensure handoff copies the `chat_ctx` so history is preserved.

## Phase 3: Update Pipeline Entrypoint
- [x] Task: Update `create_agent` in `pipeline.py`.
    - [x] Set the initial agent to `TriageAgent`.

## Phase 4: Testing & Verification
- [x] Task: Conductor - User Manual Verification 'Phase 4: Testing & Verification' (Protocol in workflow.md) [checkpoint: 3d382b9]
    - [x] Verify the agent greets the user, detects the language, and successfully transitions to the correct TTS and Persona without dropping the call.