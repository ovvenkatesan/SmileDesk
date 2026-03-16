# Project Context: Smile Garden Dental Voice AI Agent

## Working Relationship
- **Project Owner:** V-Duo
- **Facilitator:** Saga (Strategic Business Analyst)

## Initial Context
- **Project:** Smile Garden Dental Voice AI Agent
- **Description:** A specialized Voice AI support agent designed to automate patient appointment scheduling, rescheduling, and reminder calls through both a web-based voice interface and traditional phone lines for 24/7 conversational experience.

### Core Functionalities
- **Web Voice Widget:** Click-to-talk interface on smilegarden.in.
- **Inbound Telephony:** Voice agent over dedicated support phone number.
- **Outbound Reminders:** Automated system for patient calls.

### Architecture & Technology Stack
- **Orchestration:** Python 3.10+ & LiveKit Python SDK
- **Media Routing:** LiveKit Cloud
- **Telephony Bridge:** Vobiz SIP
- **Speech-to-Text:** Deepgram
- **Conversational Brain:** Gemini
- **Text-to-Speech:** Sarvam.ai (including regional languages like Tamil)
- **Scheduling Engine:** Cal.com

### System Flow
1. Connection (LiveKit room)
2. Listening (Deepgram STT)
3. Processing (Python backend + Gemini)
4. Action/Response (Gemini output + Cal.com API)
5. Speaking (Sarvam.ai TTS)

### Implementation Phases
1. Environment & Tooling
2. Pipeline Integration
3. Telephony & Web
4. Outbound Automation

### Future Expansion
- Clinic management system / CRM integration
- Human handoff mechanism