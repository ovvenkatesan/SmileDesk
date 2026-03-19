# Smile Garden Voice AI Agent - Technology Stack

## Core Platform Approach
Custom Full-Stack Application decoupled into a real-time Voice AI orchestration layer and a dual-frontend architecture serving both patients (lightweight widget) and clinic owners (PWA dashboard).

## Key Technologies

### Backend & Orchestration
- **Language/Framework:** Python 3.10+
- **Real-Time Logic:** LiveKit Python SDK (manages WebRTC connections and LLM state)
- **Server API:** `livekit-api` package used for server-side interventions (e.g. SIP call transfers).
- **Data Persistence:** Supabase PostgreSQL for metadata/transcripts and Supabase Storage (S3-compatible) for MP3 call recordings.
- **Audio Capture:** LiveKit Room Composite Egress.

### Frontend (Owner Dashboard)
- **Framework:** Next.js (React) - Industry standard for fast SaaS dashboard development, easily configured as a PWA.
- **Styling:** Tailwind CSS + shadcn/ui - Rapid execution of the "Minimal Soft" UI style.

### Frontend (Patient Web Widget)
- **Framework:** Vanilla JS / Web Components (Custom Element) - Ensures instant loading (<100KB) on poor networks and prevents CSS/framework conflicts on clinic websites.
- **Styling:** Shadow DOM scoped CSS.

### AI & Voice Models
- **Speech-to-Text (STT):** Deepgram - Ultra-fast, real-time audio parsing.
- **Text-to-Speech (TTS):** Sarvam.ai - Generates natural, culturally resonant audio (English & Tamil).
- **Conversational Brain:** Gemini 2.0 - Contextual reasoning, intent resolution, and function calling.

### Telephony & Integrations
- **Telephony:** Vobiz SIP - SIP trunking to bridge traditional phone lines to the LiveKit server.
- **Call Routing:** LiveKit Cloud SIP Ingress and Dispatch Rules route Vobiz calls to worker rooms.
- **Scheduling API:** Cal.com - Primary API for reading availability and booking/rescheduling slots.
- **Payments:** Stripe - For handling potential deposits or B2B SaaS billing.
- **Authentication:** Firebase Auth (Phone) - Passwordless SMS OTP authentication for clinic owners.