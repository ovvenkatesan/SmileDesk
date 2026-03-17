# Implementation Plan: Owner Dashboard PWA

## Phase 1: Backend API Setup
- [x] Task: Initialize Python API server. 617d436
    - [x] Add `fastapi` and `uvicorn` to `requirements.txt`.
    - [x] Create `server/src/api.py` with basic routing.
- [x] Task: Create mock data endpoints. 4c14c86
    - [x] Endpoint for ROI Snapshot data.
    - [x] Endpoint for Agent Status.
    - [x] Endpoint for Call Logs list.
    - [x] Endpoint for specific Call Details (Transcript & Sentiment).
- [x] Task: Conductor - User Manual Verification 'Phase 1: Backend API Setup' (Protocol in workflow.md) [checkpoint: ed368e6]

## Phase 2: Next.js Initialization & PWA Setup
- [x] Task: Bootstrap Next.js project. e565066
    - [x] Initialize Next.js app in a new `dashboard/` directory.
    - [x] Configure Tailwind CSS.
    - [x] Initialize `shadcn/ui` and apply "Minimal Soft" color palette to `tailwind.config.ts`.
- [x] Task: Configure PWA capabilities. e565066
    - [x] Add `next-pwa` (or similar) plugin.
    - [x] Create `manifest.json` and basic icons for installation.
- [x] Task: Conductor - User Manual Verification 'Phase 2: Next.js Initialization & PWA Setup' (Protocol in workflow.md) [checkpoint: 00210d4]

## Phase 3: Firebase Auth Integration
- [x] Task: Setup Firebase client. e716200
    - [x] Install `firebase` SDK in the dashboard project.
    - [x] Create Firebase configuration module using environment variables.
- [x] Task: Build Login Flow. 305ee5a
    - [x] Create an SMS OTP login page UI.
    - [x] Implement Firebase RecaptchaVerifier and signInWithPhoneNumber logic.
    - [x] Create a protected route wrapper for the dashboard.
- [~] Task: Conductor - User Manual Verification 'Phase 3: Firebase Auth Integration' (Protocol in workflow.md)

## Phase 4: Bento Box Dashboard UI
- [ ] Task: Build main dashboard layout.
    - [ ] Create a responsive CSS Grid layout for the Bento Box design.
- [ ] Task: Implement core widgets (UI only).
    - [ ] Create the ROI Snapshot component.
    - [ ] Create the Agent Status indicator component.
    - [ ] Create the Call Logs list component.
    - [ ] Create the Booking History component.
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Bento Box Dashboard UI' (Protocol in workflow.md)

## Phase 5: Data Integration & Call Details
- [ ] Task: Connect frontend to API.
    - [ ] Implement fetch logic to retrieve data from the Python API endpoints.
    - [ ] Populate the Bento Box widgets with the fetched data.
- [ ] Task: Implement Call Details drill-down.
    - [ ] Create a modal or slide-over panel for viewing a specific call.
    - [ ] Display the fetched call transcript and AI sentiment analysis.
- [ ] Task: Conductor - User Manual Verification 'Phase 5: Data Integration & Call Details' (Protocol in workflow.md)