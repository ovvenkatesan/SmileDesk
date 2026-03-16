# Track Specification: Implement Multilingual Support (Tamil)

## Overview
This track focuses on giving Pallavi, the Smile Garden Voice AI Agent, the ability to seamlessly converse in Tamil. This satisfies the core demographic requirement to serve regional patients effectively.

## Objectives
- Integrate Tamil speech-to-text (STT) capabilities via Deepgram (or by enabling multilingual detection).
- Integrate Tamil text-to-speech (TTS) capabilities via Sarvam TTS.
- Update the system prompt to explicitly inform the LLM (Gemini 2.5 Flash) that it should dynamically detect the user's language (English or Tamil) and respond in the same language.

## Scope
- **In Scope:** Updating `pipeline.py` to configure Deepgram for code-switching or explicitly adding Tamil. Updating the LLM instructions. Ensuring Sarvam TTS can handle Tamil output correctly.
- **Out of Scope:** Translating existing UI elements (this is strictly for the Voice AI component).

## Technical Details
- **STT:** Deepgram must be configured to detect or support `ta-IN` alongside `en-US`.
- **LLM:** Gemini 2.5 natively supports Tamil; prompt engineering will guide its behavior.
- **TTS:** Sarvam TTS needs to be verified/configured to process Tamil characters and output natural-sounding audio.