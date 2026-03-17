# Specification: Owner Dashboard PWA

## Overview
Create a Next.js progressive web application (PWA) dashboard for Smile Garden Dental clinic owners. This dashboard provides a "Proof of Value" by visualizing the performance of the Voice AI agent, including a core After-Hours ROI snapshot, detailed call logs with transcripts and sentiment analysis, and agent status. 

## Functional Requirements
- **Authentication:** Implement Firebase Phone Authentication (Passwordless SMS OTP) to secure the dashboard.
- **Backend API:** Create a new Python-based API (using FastAPI or similar) alongside the existing LiveKit worker to serve dashboard data.
- **Dashboard Layout:** Implement a responsive "Bento Box" grid layout.
- **Key Widgets (Bento Box Components):**
  - **ROI Snapshot:** The primary North Star metric showing leads saved and estimated financial value generated (especially after-hours).
  - **Agent Status:** Live indicator of the agent's current state (e.g., online, offline, currently on a call).
  - **Call Logs:** A sortable/filterable list of recent calls handled by the AI.
  - **Call Details (Drill-down):** Clicking a call reveals the full text transcript of the conversation and an AI-generated sentiment analysis (e.g., Anxious, Neutral, Satisfied).
  - **Booking History:** A dedicated view showing appointments successfully booked, rescheduled, or cancelled by the AI.

## Non-Functional Requirements
- **Frontend Stack:** Next.js (App Router), Tailwind CSS, and shadcn/ui for accessible, rapid UI development.
- **PWA Capabilities:** Configured with a web manifest and service worker so it can be installed as an app on the clinic owner's phone.
- **Design System:** Strict adherence to the "Minimal Soft" style defined in `product-guidelines.md` (Sage Green/Mint, Muted Cerulean, warm off-white backgrounds).
- **Responsive:** Mobile-first approach, as owners will frequently check this on their phones.

## Acceptance Criteria
- [ ] User can log in using Firebase SMS OTP.
- [ ] User is redirected to the dashboard upon successful authentication.
- [ ] Dashboard displays the ROI Snapshot, Agent Status, Call Logs, and Booking History in a Bento Box layout.
- [ ] Selecting a specific call log displays the call transcript and sentiment analysis.
- [ ] The dashboard consumes data from a newly established Python backend API route.
- [ ] The application passes Lighthouse PWA installability checks.

## Out of Scope
- Implementing the actual LiveKit call transcription processing and saving it to a database (this spec assumes the backend will mock or query an existing datastore for the transcripts/sentiment, while a future track will wire the live agent's memory to that database).