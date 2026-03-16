# Initial Concept

It is SAAS platform

---

# Smile Garden Voice AI Agent

## Vision
Create a specialized, 24/7 Voice AI support agent that elevates customer satisfaction by ensuring absolute accountability—where no inquiry falls through the cracks. This system will streamline operations by freeing up front-desk staff while acting as a sophisticated, always-available concierge that caters to both local patients and international medical tourists.

## Target Audience
1. **SME Clinic Owners (B2B Buyers):** Seeking operational ROI transparency and a zero missed-call rate.
2. **Urgent Local Patients (B2C Primary):** High-intent users in pain, seeking immediate reassurance and friction-free booking.
3. **Foreign Medical Tourists (B2C Secondary):** Planning-focused users looking for transparent pricing, seamless logistics, and multilingual communication.

## Core Features & Concepts
- **Dynamic State Engine:** Utilizes non-linear intent resolution to separate 'social logic' (empathy/listening) from 'business logic' (updating booking payloads).
- **Patient Web Widget:** A lightweight (<100KB) Vanilla JS web component featuring context-aware hero buttons (e.g., "I'm in pain right now").
- **Owner Dashboard PWA:** A Next.js/Tailwind application prioritizing the "After-Hours ROI Snapshot" to prove value to clinic owners.
- **Zero-Wait Telephony:** SIP trunking integration (Vobiz) to pick up on ring one, every time.
- **Multilingual Support:** English (Primary) and Tamil (Secondary via Sarvam TTS) for regional demographics.
- **Comprehensive Appointment Management:** Patients can seamlessly book, reschedule, or cancel their dental appointments directly through the Voice AI, which securely interfaces with the Cal.com API.

## Success Criteria (North Star)
- **Zero Missed Opportunities:** Achieve a 0% missed call rate via infinite concurrency.
- **Increased Conversions:** 25-35% boost in after-hours conversions within 6 months.
- **Operational Efficiency:** Reduce caller "on-hold" time by 60%.

## Constraints & Future Scope
- **Current Constraints:** Initial scheduling must integrate with Cal.com. Widget must load instantly even on 3G roaming connections. Minimal API spend without degrading voice quality.
- **Future Expansions:** Google Calendar integration, deeper EHR/CRM connections (e.g., Dentrix).