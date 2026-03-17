# Implementation Plan: Web Widget & Single Page Site

## Phase 1: Setup and Basic HTML Structure
- [x] Task: Create basic `index.html` structure. 94337b4
    - [x] Add basic Smile Garden Dental branding layout.
    - [x] Link a CSS file for styling and responsiveness.
- [x] Task: Add Voice Agent floating action button (FAB) UI. faa3bcb
    - [x] Implement bottom-right anchored button.
    - [x] Add basic hover and state styles (default, connecting, active).
- [x] Task: Conductor - User Manual Verification 'Phase 1: Setup and Basic HTML Structure' (Protocol in workflow.md) [checkpoint: 08c30c4]

## Phase 2: LiveKit SDK Integration
- [x] Task: Setup LiveKit JS Client SDK. 3478b00
    - [x] Import the LiveKit JS SDK via CDN.
    - [x] Create `widget.js` to manage the LiveKit `Room` object.
- [x] Task: Conductor - User Manual Verification 'Phase 2: LiveKit SDK Integration' (Protocol in workflow.md) [checkpoint: 771f72b]

## Phase 3: Connection Logic and State Management
- [x] Task: Handle button click and microphone permissions. a48d9e2
    - [x] Request microphone access when the FAB is clicked.
    - [x] Initiate connection to the LiveKit room and handle token generation (or static token setup for testing).
- [~] Task: Wire up UI state to connection events.
    - [ ] Update visual state based on connection events (connecting, connected, disconnected).
    - [ ] Implement click-to-disconnect logic.
    - [ ] Handle audio playback of the remote agent's track.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Connection Logic and State Management' (Protocol in workflow.md)