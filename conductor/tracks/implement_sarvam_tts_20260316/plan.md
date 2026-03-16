# Implementation Plan: Sarvam TTS Integration

## Phase 1: Research and SDK Setup
- [x] Task: Research Sarvam TTS Python integration and update requirements. 92e5d1f
    - [ ] Add `requests` or `aiohttp` to `server/requirements.txt` if needed for REST API, or add Sarvam SDK if one exists.
    - [ ] Update `server/tests/test_deps.py`.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Research and SDK Setup' (Protocol in workflow.md) [checkpoint: 5f9f3e5]

## Phase 2: TTS Implementation
- [~] Task: Implement Sarvam API call in `sarvam_tts.py`.
    - [ ] Retrieve `SARVAM_API_KEY` from environment.
    - [ ] Implement the `_main_task` in `DummyChunkedStream` (rename it to `SarvamChunkedStream`) to make the async HTTP request to Sarvam's API.
    - [ ] Decode the returned audio (typically base64 encoded wav/pcm).
    - [ ] Yield the audio as `livekit.rtc.AudioFrame`.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: TTS Implementation' (Protocol in workflow.md)

## Phase 3: Testing and Integration
- [ ] Task: Write unit tests for `SarvamTTS`.
    - [ ] Mock the API response to avoid actual billing during tests.
    - [ ] Verify that audio frames are yielded correctly.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Testing and Integration' (Protocol in workflow.md)