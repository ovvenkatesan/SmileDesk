---
design_intent: D
design_status: not-started
---

# 02: SME Clinic Owner's ROI Verification

**Project:** Smile Garden Voice AI Agent
**Created:** 2026-03-15
**Method:** Whiteport Design Studio (WDS)

---

## Transaction (Q1)

**What this scenario covers:**
Verify the overnight performance of the Voice AI by checking the "After-Hours ROI Snapshot."

---

## Business Goal (Q2)

**Goal:** Operational Peace & Efficiency
**Objective:** Prove the SaaS value proposition through operational transparency, ensuring subscription retention.

---

## User & Situation (Q3)

**Persona:** SME Clinic Owner (B2B Buyer)
**Situation:** It's 8:00 AM on a Monday, and the clinic owner is arriving at the office. They want to know what happened over the weekend before the morning rush begins.

---

## Driving Forces (Q4)

**Hope:** See clear, dollar-denominated proof that the system captured leads and recovered revenue while the clinic was closed.

**Worry:** Facing a "black box" where they don't know if the AI missed important patient calls or failed to book emergency slots over the weekend.

---

## Device & Starting Point (Q5 + Q6)

**Device:** Desktop
**Entry:** The owner opens their web browser and goes to the Smile Garden SaaS Dashboard login page, clicking a saved bookmark.

---

## Best Outcome (Q7)

**User Success:**
Owner immediately sees the exact number of missed calls converted into bookings and the estimated dollar value of those appointments.

**Business Success:**
Owner feels the monthly SaaS subscription is completely justified as a profit center, preventing churn.

---

## Shortest Path (Q8)

1. **Owner Dashboard - Login** — Owner enters phone number and completes passwordless OTP verification.
2. **Owner Dashboard - Home** — Owner sees the large "After-Hours ROI Snapshot" card displaying bookings and recovered revenue. ✓

---

## Trigger Map Connections

**Persona:** SME Clinic Owner (B2B Buyer)

**Driving Forces Addressed:**
- ✅ **Want:** Desires absolute transparency into clinic operations; wants to see concrete ROI and recovered revenue.
- ❌ **Fear:** Fears "black box" solutions.

**Business Goal:** Operational Peace & Efficiency

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 02.1 | `02.1-owner-dashboard-login/` | Authenticate the owner | Enters OTP and submits |
| 02.2 | `02.2-owner-dashboard-home/` | Review overnight ROI | Scenario Success ✓ |
