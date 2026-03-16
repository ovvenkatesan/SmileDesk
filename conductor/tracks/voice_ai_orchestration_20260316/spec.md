# Track Specification: Implement core Voice AI orchestration and LiveKit pipeline

## Overview
This track focuses on scaffolding the core Python backend to support the Smile Garden Voice AI Agent. It will set up the LiveKit agent framework, integrate the essential voice AI models (Deepgram for STT, Sarvam for TTS, Gemini for LLM reasoning), and establish the base "Dynamic State Engine" capable of maintaining conversational context.

## Objectives
- Set up a Python 3.10+ project structure for the agent.
- Integrate the LiveKit Python SDK to handle WebRTC audio streams.
- Configure Deepgram STT, Sarvam TTS, and Gemini 2.0 plugins within the LiveKit pipeline.
- Implement a basic context-aware system prompt (the "Neighborhood Nurse" persona).
- Expose the agent via a LiveKit room to test basic conversational functionality.

## Scope
- **In Scope:** Python backend setup, LiveKit integration, basic STT/LLM/TTS pipeline, simple prompt engineering.
- **Out of Scope:** Vobiz SIP telephony bridge, Cal.com scheduling API functions, frontend web widget, frontend dashboard.

## Technical Details
- **Language:** Python 3.10+
- **Framework:** LiveKit Python SDK
- **Dependencies:** `livekit-agents`, `livekit-plugins-deepgram`, `livekit-plugins-google` (for Gemini), custom Sarvam TTS integration if no direct plugin exists.
- **Architecture:** The agent will listen to audio tracks, stream text to Gemini, and stream audio responses back via Sarvam/LiveKit.