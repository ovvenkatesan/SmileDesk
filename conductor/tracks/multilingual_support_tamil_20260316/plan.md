# Implementation Plan: Multilingual Support (Tamil)

## Phase 1: Deepgram STT Configuration
- [x] Task: Update `pipeline.py` to configure Deepgram for multilingual support. e8c9386
    - [x] Modify `deepgram.STT()` initialization to include `language="multi"` or explicitly list `["en", "ta"]` based on LiveKit Deepgram plugin documentation.

## Phase 2: Sarvam TTS Configuration
- [x] Task: Ensure `sarvam_tts.py` handles language switching. 1a997ce
    - [x] Review `SarvamTTS` implementation to ensure it correctly passes the target language to the Sarvam API based on the LLM's output, or verify if Sarvam auto-detects.

## Phase 3: Prompt Engineering
- [x] Task: Update the `get_system_prompt()` in `pipeline.py`. debb087
    - [x] Add explicit instructions: "You are fully bilingual in English and Tamil. Detect the language the user is speaking and reply in the exact same language. Do not mix languages within a single sentence unless necessary for medical terms."

## Phase 4: Testing & Verification
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Testing & Verification' (Protocol in workflow.md)
    - [ ] Manually test the agent by speaking to it in Tamil and verifying it responds accurately in Tamil using the Sarvam voice.