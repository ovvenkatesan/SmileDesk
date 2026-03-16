# Conversation Flow: Contact Strategy

## 1. Opening
**Saga:** Let's discuss the Contact Strategy. This step is a bit "meta" for our project because your entire product *is* a contact strategy (an AI answering the phone/chat). 

But let's look at it from the perspective of the **B2B SaaS Owner Dashboard**. 

If a clinic owner using your dashboard runs into a technical issue with the AI, or has a billing question, how do you want them to contact you (the support team)? 
- Do you want a simple support form inside the dashboard?
- A direct email link?
- Or perhaps a chat bubble in the corner where they can talk to *your* support team?
**User:** Google Calendar, which we mentioned earlier, that we should document now so the architecture supports them later

## 2. Clarification
**Saga:** Ah, I see! You're referring back to the Integrations section. I did actually add Google Calendar to the "Future Integrations" section of our Platform Requirements document, specifically noting that the architecture needs to be built modularly now to support it later without rewriting the core scheduling logic.

For this specific step (Contact Strategy), we are just deciding how the clinic owners using your SaaS dashboard will contact *you* for support. 

For the MVP, what is the easiest way for them to get help if the dashboard crashes or the AI goes offline? A simple "Email Support" button, or a built-in "Support Ticket" form?
**User:** continue

## Final Output
**Contact Strategy (B2B Support):**
- **Primary Method:** Direct Email Support link.
- **Rationale:** For an MVP where time-to-market is 'ASAP', building a complex internal ticketing system is out of scope. A simple, prominent `mailto:` link or basic contact form in the dashboard footer will suffice for early clinic owners to report bugs or ask questions.