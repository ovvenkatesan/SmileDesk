# Track Specification: Implement Multi-Agent Language Routing

## Overview
This track refactors the existing single-agent architecture into a Multi-Agent system using LiveKit's `AgentHandoff` capabilities. Instead of relying on a single prompt and dynamic TTS switching, the system will use a lightweight "Triage Agent" to detect language and route to either a dedicated "English Agent" or a dedicated "Tamil Agent".

## Objectives
- Create a `TriageAgent` that greets the user and determines their preferred language.
- Create an `EnglishAgent` with an English-only prompt and Deepgram TTS.
- Create a `TamilAgent` with a Tamil-only prompt and Sarvam TTS.
- Implement `@llm.function_tool` methods on the TriageAgent to perform seamless handoffs to the specialized agents.

## Scope
- **In Scope:** Refactoring `pipeline.py` and `tools.py` to support multi-agent classes. Implementing context preservation (`chat_ctx.copy()`) during handoff so the user doesn't have to repeat themselves.
- **Out of Scope:** Adding new Cal.com functionality.

## Technical Details
- **TriageAgent:** Fast STT (nova-3 multi), Fast LLM, Fast TTS.
- **Handoff:** Returns an instance of the target Agent class from a tool call.