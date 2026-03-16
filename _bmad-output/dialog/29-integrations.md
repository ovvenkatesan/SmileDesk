# Conversation Flow: Integrations

## 1. Opening
**Saga:** Now that the core stack is locked, let's talk about third-party Integrations.

We already know the massive ones:
- **Cal.com** (For MVP Scheduling)
- **Vobiz** (For SIP Telephony)
- **Deepgram / Sarvam.ai / Gemini** (The AI Brain)

Aside from those core operational APIs, will you need any other integrations for the MVP? 
For example:
- **Analytics:** Do you need PostHog or Google Analytics on the Owner Dashboard to track usage?
- **Payments:** Will the AI or widget ever need to collect a deposit via Stripe before booking?
- **Auth:** Since it's a B2B SaaS, how are owners logging into the dashboard? (e.g., Supabase Auth, Clerk, Auth0, NextAuth?)

And lastly, are there any *future* integrations (like Google Calendar, which we mentioned earlier) that we should document now so the architecture supports them later?
**User:** Analytics --> google analytics, payment: Stripes, auth: firebase phno auth

## Final Output
**Integrations Documented:**
- **Analytics:** Google Analytics (for tracking dashboard usage and widget interactions).
- **Payments:** Stripe (potentially for collecting deposits/fees via the widget or billing the clinic owners for the SaaS).
- **Authentication:** Firebase Phone Auth (passwordless login via SMS OTP for clinic owners).
- **Future:** Google Calendar (abstracting the booking logic away from strict Cal.com dependence).