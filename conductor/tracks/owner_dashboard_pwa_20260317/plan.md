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
- [~] Task: Conductor - User Manual Verification 'Phase 1: Backend API Setup' (Protocol in workflow.md)

## Phase 2: Next.js Initialization & PWA Setup
- [ ] Task: Bootstrap Next.js project.
    - [ ] Initialize Next.js app in a new `dashboard/` directory.
    - [ ] Configure Tailwind CSS.
    - [ ] Initialize `shadcn/ui` and apply "Minimal Soft" color palette to `tailwind.config.ts`.
- [ ] Task: Configure PWA capabilities.
    - [ ] Add `next-pwa` (or similar) plugin.
    - [ ] Create `manifest.json` and basic icons for installation.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Next.js Initialization & PWA Setup' (Protocol in workflow.md)

## Phase 3: Firebase Auth Integration
- [ ] Task: Setup Firebase client.
    - [ ] Install `firebase` SDK in the dashboard project.
    - [ ] Create Firebase configuration module using environment variables.
- [ ] Task: Build Login Flow.
    - [ ] Create an SMS OTP login page UI.
    - [ ] Implement Firebase RecaptchaVerifier and signInWithPhoneNumber logic.
    - [ ] Create a protected route wrapper for the dashboard.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Firebase Auth Integration' (Protocol in workflow.md)

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