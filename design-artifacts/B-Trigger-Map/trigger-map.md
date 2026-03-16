# Trigger Map: Smile Garden Voice AI Agent

> Connecting Business Goals to User Psychology

**Created:** 2026-03-15
**Author:** Saga (via Dream Mode)
**Related:** [Product Brief](../A-Product-Brief/project-brief.md)

---

## 1. Business Goals (WHY are we doing this?)

### Primary Goal: Zero Missed Opportunities (Total Lead Capture)
- **Metric:** Achieve a 0% missed call rate via infinite concurrency.
- **Metric:** 25-35% increase in after-hours conversions within the first 6 months.

### Secondary Goal: Operational Peace & Efficiency
- **Metric:** Reduce caller 'on-hold' time by 60%.
- **Metric:** AI successfully resolves 80% of routine inbound queries without human intervention.

---

## 2. Target Groups (WHO can help us achieve this?)

| Group | Role | How they help achieve the goal |
|-------|------|--------------------------------|
| **SME Clinic Owners** | B2B Buyer | They purchase the SaaS, defining the adoption of the system. |
| **Urgent Local Patients** | B2C Primary User | They generate the inbound booking volume that drives ROI. |
| **Foreign Medical Tourists** | B2C Secondary User | They provide high-value bookings that require complex logistics. |
| **Front Desk Staff** | Internal User | They validate the operational peace and provide the "warm handoff". |

---

## 3. Driving Forces (WHAT motivates them?)

### SME Clinic Owners (The Buyer)
- **Positive (+):** Desires absolute transparency into clinic operations; wants to see concrete ROI and recovered revenue.
- **Negative (-):** Fears "black box" solutions; terrified that an AI might sound robotic, lack empathy, and alienate their patient base.

### Urgent Local Patients (The Primary User)
- **Positive (+):** Seeking immediate reassurance, empathy, and a fast path to pain relief.
- **Negative (-):** Deeply frustrated by busy signals, long hold times, and unreturned voicemails.

### Foreign Medical Tourists (The Secondary User)
- **Positive (+):** Wants clear pricing, seamless logistics scheduling across timezones, and communication in a familiar language.
- **Negative (-):** Anxious about hidden costs, miscommunication, and traveling internationally without a confirmed, rock-solid itinerary.

### Front Desk Staff (The Internal User)
- **Positive (+):** Wants to focus on in-person hospitality; appreciates receiving a "Context Brief" before the patient arrives.
- **Negative (-):** Resents having to clean up after poorly functioning software; fears being replaced rather than augmented.

---

## 4. Trigger Mapping (HOW do we trigger the driving forces?)

### Map 1: The B2B Buyer Journey
*Connecting the Clinic Owner's needs to the Business Goals.*

- **Goal:** Zero Missed Opportunities & Operational Peace
  - **Target:** SME Clinic Owner
    - **Driver (+):** Needs to see concrete ROI
      - **Trigger (Feature):** **After-Hours ROI Snapshot Dashboard** (A prominent widget showing exact dollar amounts recovered while closed).
    - **Driver (-):** Fears a robotic, alienating AI
      - **Trigger (Feature):** **Call Quality Playback & Tuning** (Ability to listen to anonymized successful AI interactions to build trust in the "Neighborhood Nurse" persona).

### Map 2: The B2C Patient Journey
*Connecting the Patient's needs to the Business Goals.*

- **Goal:** Zero Missed Opportunities
  - **Target:** Urgent Local Patient
    - **Driver (+):** Seeking immediate reassurance
      - **Trigger (Feature):** **Dynamic State Engine Voice Flow** (AI immediately validates anxiety before asking for booking details).
    - **Driver (-):** Frustrated by busy signals
      - **Trigger (Feature):** **Zero-Wait Concurrent Telephony** (LiveKit SIP routing ensures the AI picks up on ring one, every time).

  - **Target:** Foreign Medical Tourist
    - **Driver (+):** Wants seamless logistics across timezones
      - **Trigger (Feature):** **24/7 Context-Aware Web Widget** (Contextual buttons like "Check my insurance" or "See Tuesday Morning slots" that adapt to their browsing timezone).
    - **Driver (-):** Anxious about miscommunication
      - **Trigger (Feature):** **Multilingual Voice Synthesis** (Deepgram/Sarvam integration providing culturally resonant spoken responses).

### Map 3: The Internal Operational Journey
*Connecting the Staff's needs to the Business Goals.*

- **Goal:** Operational Peace & Efficiency
  - **Target:** Front Desk Staff
    - **Driver (+):** Wants to focus on hospitality
      - **Trigger (Feature):** **Automated Context Briefs** (The system pushes a summary of the patient's anxieties and AI conversation history directly to the clinic's CRM/Hygienist view before arrival).

---

## 5. Feature Prioritization (Phase 1 MVP)

Based on the mapping above, here are the strictly prioritized features for the MVP:

**High Priority (Must Have for Goal Achievement):**
1. **Zero-Wait Concurrent Telephony:** Core LiveKit/Vobiz setup to eliminate busy signals.
2. **Dynamic State Engine Voice Flow:** The Gemini logic that prioritizes empathy (social logic) alongside scheduling (business logic).
3. **After-Hours ROI Snapshot:** The core Next.js dashboard view for the clinic owner.
4. **Context-Aware Web Widget:** The lightweight (<100KB) Vanilla JS web interface with contextual hero buttons.

**Medium Priority (Fast Follows):**
5. **Automated Context Briefs:** Pushing notes to the hygienist/staff.
6. **Multilingual Synthesis (Tamil):** Sarvam integration for regional demographics.

**Low Priority (Future Expansion):**
7. Google Calendar Integration.
8. Deep EHR/CRM integration (Dentrix).

---
*Generated by Saga (WDS Analyst)*