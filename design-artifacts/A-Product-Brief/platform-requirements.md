# Platform Requirements: {{project_name}}

> Technical Boundaries & Platform Decisions

**Created:** {{date}}
**Author:** {{user_name}}
**Related:** [Product Brief](./product-brief.md)

---

## Technology Stack

### Core Platform

**Approach:** Custom Full-Stack Application (Python Backend + Next.js/VanillaJS Frontend)

The system is a decoupled, real-time Voice AI application. It relies on a heavy Python orchestration layer to manage the WebRTC connections and LLM state, paired with a dual-frontend strategy to serve both patients (lightweight widget) and clinic owners (PWA dashboard).

### Key Technologies

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Frontend (Widget)** | Vanilla JS / Web Components | Ensures instant loading on poor networks (3G/4G) and prevents CSS/framework conflicts when embedded on various clinic websites. |
| **Frontend (Dashboard)** | Next.js (React) | Industry standard for fast SaaS dashboard development, enables easy PWA configuration. |
| **Styling** | Tailwind CSS + shadcn/ui | Allows rapid execution of the "Minimal Soft" UI style on the dashboard. |
| **Backend/Orchestration** | Python 3.10+ | Robust ecosystem for AI/ML and necessary for the LiveKit agent framework. |
| **Real-Time Routing** | LiveKit SDK / Cloud | Low-latency WebRTC hub managing the audio streams. |
| **Telephony** | Vobiz SIP | SIP trunking to bridge traditional phone lines to the LiveKit server. |
| **Voice Models** | Deepgram (STT) + Sarvam.ai (TTS) | Fast transcription and culturally resonant/native language synthesis. |
| **AI Brain** | Gemini 2.0 | Contextual reasoning and function calling. |

---

## Plugin/Package Stack

{{#if plugins}}
| Plugin | Purpose | Status |
|--------|---------|--------|
{{#each plugins}}
| {{this.name}} | {{this.purpose}} | {{this.status}} |
{{/each}}
{{else}}
*To be determined during development*
{{/if}}

---

## Integrations

### Required Integrations

- **Cal.com:** Primary scheduling API for reading clinic availability and booking/rescheduling patient slots.
- **Vobiz SIP:** Telephony bridge to route inbound phone calls directly to the LiveKit server.
- **Deepgram:** Ultra-fast, real-time Speech-to-Text (STT) for parsing patient audio.
- **Sarvam.ai:** Text-to-Speech (TTS) engine utilized for generating natural, culturally resonant audio (including Tamil support).
- **Google Analytics:** To track user interaction on the web widget and clinic owner usage within the dashboard.
- **Stripe:** For handling potential patient deposits during the booking flow, as well as billing the B2B clinic owners for their SaaS subscription.
- **Firebase Auth (Phone):** Handling passwordless, SMS OTP-based authentication for clinic owners logging into the dashboard.

### Future Integrations

- **Google Calendar:** Planned secondary scheduling option. The backend booking logic must be abstracted enough in Phase 1 so it isn't strictly coupled to Cal.com's specific data structures. *(Timeline: Phase 2/Expansion)*
- **Clinic CRM / EHR:** Future integration to pull patient history (e.g., Dentrix, Solutionreach). *(Timeline: Future Expansion)*

---

## Contact Strategy

### Primary Contact Method

For B2B SaaS Support (Clinic Owners contacting the platform developers): **Direct Email Support.**

### Contact Channels

| Channel | Priority | Implementation |
|---------|----------|----------------|
| Email Support | Primary | A simple `mailto:` link or a very basic contact form located in the dashboard footer/settings page. |

*Rationale:* Given the aggressive "ASAP" timeline for the MVP, building a complex internal ticketing system or live-chat support widget for the B2B dashboard is out of scope. Direct email is sufficient for early adopters to report bugs or request assistance.

---

## UX Constraints

*These constraints inform what's possible in Phase 4 (UX Design)*

### Platform Limitations

{{#each ux_constraints}}
- {{this}}
{{/each}}

### Performance Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| **Mobile First** | {{mobile_first}} | {{mobile_rationale}} |
| **Page Load** | {{page_load_target}} | {{load_rationale}} |
| **Offline Support** | {{offline_support}} | {{offline_rationale}} |

---

## Multilingual Requirements

**Languages:** English (Primary), Tamil (Secondary via Voice)

**Implementation:** 
- The B2B SaaS Owner Dashboard and underlying backend logic will be English-only. 
- The Patient-facing Voice AI will handle real-time multilingual inputs and synthesis (English/Tamil) via the Deepgram and Sarvam.ai integrations.

---

## SEO & Performance Requirements

### Performance Targets (Critical)

| Metric | Target | Rationale |
|--------|--------|-----------|
| **Widget Bundle Size** | < 100KB | The Vanilla JS web widget must load instantly on 3G roaming connections for medical tourists. |
| **Dashboard LCP** | < 2.5s | Next.js owner dashboard must pass Core Web Vitals to feel premium and fast. |
| **Voice Latency** | < 800ms | The round-trip time (STT -> LLM -> TTS) must remain under a second to maintain conversational fluidity. |

### Structured Data

| Page Type | Schema Type | Key Properties |
|-----------|-------------|----------------|
| SaaS Landing Page | SoftwareApplication | name, applicationCategory, operatingSystem, offers |
| Clinic Site | LocalBusiness | name, address, telephone, openingHours, medicalSpecialty |

### Security Headers

| Header | Purpose |
|--------|---------|
| **Strict-Transport-Security (HSTS)** | Force HTTPS |
| **Content-Security-Policy (CSP)** | Prevent XSS and unauthorized frame embedding (vital for the widget) |

---

## Maintenance & Ownership

| Aspect | Owner | Notes |
|--------|-------|-------|
| **Content Updates (Prompts)** | Product Owner (V-Duo) | Updated centrally via the backend as the AI behavior is tuned. |
| **Technical Maintenance** | Product Owner (V-Duo) | Management of the LiveKit server, Python backend, and Next.js frontend. |
| **Clinic Administration** | Clinic Owners | Clinic owners only manage their specific dashboard settings (e.g., Auth, viewing ROI metrics). |

---

## Development Handoff Notes

*For Phase 6 (Deliveries)*

### Key Considerations

- The web widget MUST be strictly bundled as a lightweight Vanilla JS Custom Element (<100KB) to ensure it does not negatively impact the loading speed of any client clinic's existing website.
- The Python backend must handle Deepgram and Sarvam APIs asynchronously to ensure the lowest possible latency for voice responses.
- Booking logic should abstract the calendar interface so that Cal.com can be easily swapped for Google Calendar in the future without affecting the Gemini prompt structure.

---

## Next Steps

- [ ] **Phase 2: Trigger Mapping** — Map user psychology
- [ ] **Phase 4: UX Design** — Begin design within these constraints

---

_Generated by Whiteport Design Studio_




