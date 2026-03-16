# Track Specification: Implement actual Sarvam TTS API integration

## Overview
The initial pipeline scaffolding used a "stub" implementation for Sarvam TTS. This track will replace that stub with a fully functional integration that connects to the Sarvam.ai API to synthesize speech from text and stream the resulting audio back to the LiveKit room.

## Objectives
- Integrate the official `sarvam` Python SDK or make direct HTTP calls to the Sarvam API.
- Update `SarvamTTS` in `sarvam_tts.py` to correctly yield audio chunks.
- Implement proper async handling for streaming TTS if supported, or buffer text and send complete sentences if only batch synthesis is supported by Sarvam.
- Ensure the audio format (sample rate, channels) returned by Sarvam matches what LiveKit expects (usually 24kHz, mono).

## Scope
- **In Scope:** Modifying `sarvam_tts.py` to use real API credentials, handling API requests/responses to Sarvam, decoding audio bytes, creating a true `ChunkedStream`.
- **Out of Scope:** LLM prompt tuning, UI updates.

## Technical Details
- **API Endpoint:** Sarvam Text-to-Speech API.
- **Environment:** Requires `SARVAM_API_KEY`.
- **Implementation:** Subclass `livekit.agents.tts.TTS` and `livekit.agents.tts.ChunkedStream`. Audio data needs to be yielded as `livekit.rtc.AudioFrame` objects.