# Design Log: Smile Garden Voice AI Agent

## Key Decisions

| Date | Decision | Phase | Who |
|---|---|---|---|
| 2026-03-15 | Adopted a generic B2B SaaS architecture (multi-tenant) instead of a single-clinic bespoke build. | Phase 1: Product Brief | Saga + V-Duo |
| 2026-03-15 | Selected "Minimal Soft / Consumer Wellness" visual aesthetic over dense enterprise patterns. | Phase 1: Product Brief | Saga + V-Duo |
| 2026-03-15 | Chose Next.js for the Owner Dashboard and Vanilla JS Web Components for the Patient Widget (<100KB). | Phase 1: Product Brief | Saga + V-Duo |

## Progress

### 2026-03-15 - Phase 1: Product Brief Complete

**Agent:** Saga (Product Brief)
**Brief Level:** Standard

**Artifacts Created:**
- `design-artifacts/A-Product-Brief/project-brief.md`
- `design-artifacts/A-Product-Brief/content-language.md`
- `design-artifacts/A-Product-Brief/visual-direction.md`
- `design-artifacts/A-Product-Brief/inspiration-analysis.md`
- `design-artifacts/A-Product-Brief/platform-requirements.md`

**Summary:** Established the business foundation for the Smile Garden Voice AI Agent as a B2B SaaS product targeting dental clinic owners. We mapped out the "Dynamic State Engine" structural concept to handle non-linear voice interactions, set the visual direction to "Consumer Health," and locked down strict technical constraints including a sub-100KB payload for the patient widget and a Next.js stack for the owner dashboard.

**Next:** Phase 2 - Trigger Mapping

### 2026-03-15 - Phase 2: Trigger Mapping Complete

**Agent:** Saga (Trigger Mapping - Dream Mode)
**Methodology:** WDS Effect Mapping (Business Goals -> Target Groups -> Driving Forces -> Features)

**Artifacts Created:**
- `design-artifacts/B-Trigger-Map/trigger-map.md`
- `design-artifacts/B-Trigger-Map/personas/urgent-local-patient.md`
- `design-artifacts/B-Trigger-Map/personas/foreign-medical-tourist.md`
- `design-artifacts/B-Trigger-Map/personas/sme-clinic-owner.md`
- `_bmad-output/_progress/agent-experiences/2026-03-15-trigger-map-Dream.md`

**Summary:** Mapped the core business goals (Zero Missed Opportunities, Operational Peace) to the psychological driving forces of the B2B buyers (Clinic Owners) and B2C users (Urgent Patients, Foreign Tourists). Validated that the proposed technical features (Dynamic State Engine, Zero-Wait Telephony, After-Hours ROI Dashboard) directly trigger the positive forces and mitigate the negative fears of each target group. Prioritized these features into a Phase 1 MVP roadmap.

**Next:** Phase 3 - UX Scenarios

### 2026-03-15 — Phase 3: UX Scenarios Complete

**Agent:** Saga (Scenario Outline)
**Scenarios:** 3 scenarios covering 5 pages
**Quality:** Excellent

**Artifacts Created:**
- `design-artifacts/C-UX-Scenarios/00-ux-scenarios.md` — Scenario index
- `design-artifacts/C-UX-Scenarios/01-urgent-patient-booking/01-urgent-patient-booking.md` — Urgent Local Patient's Emergency Search
- `design-artifacts/C-UX-Scenarios/01-urgent-patient-booking/01.1-patient-web-widget/01.1-patient-web-widget.md` — Validate pain and secure emergency booking
- `design-artifacts/C-UX-Scenarios/02-owner-roi-check/02-owner-roi-check.md` — SME Clinic Owner's ROI Verification
- `design-artifacts/C-UX-Scenarios/02-owner-roi-check/02.1-owner-dashboard-login/02.1-owner-dashboard-login.md` — Authenticate the owner
- `design-artifacts/C-UX-Scenarios/02-owner-roi-check/02.2-owner-dashboard-home/02.2-owner-dashboard-home.md` — Review overnight ROI
- `design-artifacts/C-UX-Scenarios/03-owner-quality-tuning/03-owner-quality-tuning.md` — SME Clinic Owner's Quality Assurance
- `design-artifacts/C-UX-Scenarios/03-owner-quality-tuning/03.1-owner-dashboard-logs/03.1-owner-dashboard-logs.md` — Review and playback completed AI interactions
- `design-artifacts/C-UX-Scenarios/03-owner-quality-tuning/03.2-owner-dashboard-settings/03.2-owner-dashboard-settings.md` — Tweak AI behavior

**Summary:** Translated the Trigger Map into 3 concrete UX scenarios covering all 5 core UI views for the MVP. Outlined the patient-facing widget interaction and the owner-facing dashboard workflows (ROI checking and Quality Assurance tuning). All scenarios achieved maximum quality scores for completeness and strategic alignment.

**Next:** Phase 4 - UX Design

### 2026-03-15 — Phase 4: UX Design Complete

**Agent:** Freya (UX Design - Dream Mode)
**Methodology:** WDS Scenario-Driven Design

**Artifacts Created:**
- Page specifications for all 5 pages across 3 scenarios.
- `_bmad-output/_progress/agent-experiences/2026-03-15-ux-design-Dream.md`

**Summary:** Translated the 3 UX Scenarios into concrete page specifications. The Patient Web Widget was designed as a minimalist, fast-loading floating action button with context-aware triggers. The Owner Dashboard was designed using a Bento-box layout, leveraging Tailwind CSS and shadcn/ui to meet the Next.js technical constraints and the "Consumer Health" aesthetic.

**Next:** Implementation Phase
