# Conversation Flow: Business Model

## 1. Opening
**Saga:** Now that we have our positioning, let's talk about the business model—specifically, how this Voice AI Agent fits into the clinic's operations and revenue. Obviously, Smile Garden Dental itself is a B2C business (serving patients directly). But I want to understand how the *AI Agent project* is being treated. 

Is this an internal operational tool purely funded by the clinic to improve its own B2C service, or is there any aspect of this where you might white-label or sell this Voice AI solution to *other* dental clinics in the future (which would make it a B2B product as well)?
**User:** It is SAAS Model and I wll provide this service to multiple customer and multiple verticle

## 2. Follow up 1
**Saga:** Oh, that is a huge pivot in a great way! So while Smile Garden Dental is your initial proof-of-concept or "Customer Zero," the actual product you are building is a B2B SaaS Voice AI platform for the broader healthcare and service industries.

In a B2B SaaS model, we have to think about two distinct groups: the people who *buy* the software (the clinic owners/managers) and the people who *interact* with it (the patients/customers). 

Since you plan to expand to multiple verticals later, are you currently focusing your core feature set *exclusively* on dental clinic needs (like integrating specifically with Cal.com for dental appointments) for the initial launch, or are you trying to build it generically from day one?
**User:** wanted to build generically from day one

## 3. Reflection
**Saga:** Okay, this is a critical structural decision. Here is what I am hearing about the business model:

**The Model:** B2B SaaS (Software as a Service)
**The Buyers:** Business owners across multiple verticals (starting with clinics like Smile Garden, but scaling to other service-based businesses).
**The Revenue Strategy:** A subscription-based platform where businesses pay to use your Voice AI for their inbound/outbound calls and scheduling.
**The Implications:** Because you are building generically from day one, the architecture must support dynamic prompt injection (so the AI knows if it's acting as a dental receptionist vs. a car mechanic), multi-tenant data isolation, and flexible calendar integrations (beyond just one clinic's Cal.com link).

Does this accurately reflect how you view the business model and its technical implications?
**User:** yes

## Final Output
**Decision:** B2B SaaS (with Smile Garden as "Customer Zero")

**Rationale:** The user intends to build a generic Voice AI scheduling and customer service platform that can be sold to multiple customers across multiple verticals, rather than a bespoke internal tool for a single clinic.

**Implications:** 
- The architecture must be multi-tenant from day one.
- The AI context (prompts, business rules, allowed functions) must be dynamically injected per tenant rather than hardcoded.
- Integrations (like Cal.com) must support OAuth/user-level connections rather than a single global API key.
- The UI must account for a "Business Dashboard" (where owners configure the agent) completely separate from the end-user (patient/customer) experience.