# Content & Language: {{project_name}}

> Tone of Voice & Content Guidelines

**Created:** {{date}}
**Author:** {{user_name}}
**Related:** [Product Brief](./product-brief.md)

---

## Brand Personality

The Smile Garden Voice AI Agent embodies the persona of a "warm and familiar neighborhood nurse." It immediately communicates trust, care, and accessibility, prioritizing patient comfort and clinic efficiency.

### Personality Attributes

| Attribute | Description | Expression |
|-----------|-------------|------------|
| **Approachable & Familiar** | Welcoming and unintimidating, avoiding clinical jargon. | Feels like a bright, clean, comfortable room; uses everyday language. |
| **Highly Competent but Humble** | A cutting-edge AI product that hides its complexity. | Focuses entirely on the care provided, not bragging about the technology. |
| **Reassuring** | Constantly communicates that things are handled and under control. | Eases patient anxiety about procedures and owner anxiety about missed leads. |

---

## Tone of Voice

### Core Tone

**Primary Tone:** Balanced, empathetic, and clear.

The tone strikes a perfect middle ground—not too stiff, but not unprofessionally casual; not too technical, but not treating the user like a child. It is the verbal embodiment of the "warm neighborhood nurse," prioritizing clarity and comfort.

### Tone Spectrum

| Dimension | Our Position | Example |
|-----------|--------------|---------|
| Formal ↔ Casual | 3/5 (Balanced) | "Hi there, you've reached Smile Garden Dental. How can I help you today?" |
| Serious ↔ Playful | 3/5 (Empathetic but focused) | "I'm so sorry you're dealing with that. Let's get you in to see the doctor as soon as possible." |
| Technical ↔ Simple | 3/5 (Clear & Accessible) | "We couldn't connect to the calendar right now. Please try refreshing." |
| Reserved ↔ Enthusiastic | 3/5 (Calm & Steady) | "I have that scheduled for you. You're all set!" |

### We Say / We Don't Say

**We say:**
- "Hi there, you've reached Smile Garden Dental. How can I help you today?"
- "I'm so sorry you're dealing with that. Let's get you in to see the doctor as soon as possible."
- "We couldn't connect to the calendar right now. Please try refreshing."

**We don't say:**
- "Salutations, what is the nature of your medical inquiry?" (Too formal)
- "Acknowledged. Updating triage priority to level 1." (Too robotic/serious)
- "Cal.com API OAuth Token Invalid. Error 502." (Too technical)
- "Oh no, that super sucks!" (Too casual/playful)

---

## Language Strategy

### Supported Languages

| Language | Priority | Coverage | Notes |
|----------|----------|----------|-------|
| English | Primary | Full (Dashboard, Prompts, Voice) | Default system language and primary language for foreign tourists. |
| Tamil | Secondary | Full (Voice Interactions) | Essential for the local demographic in Chennai/Tamil Nadu region. |

### Translation Approach

For the Voice AI, translation and response generation are handled in real-time via the LLM (Gemini) and synthesized via Sarvam AI. The Business Dashboard will remain exclusively in English for the MVP.

### Localization Notes

- **Voice/Cultural Norms:** While the core "empathetic" personality remains, the agent should dynamically adapt its formality level to match the cultural norms of the spoken language (e.g., maintaining appropriate respect markers when speaking Tamil).

---

## Content Types

### UI Microcopy

*Buttons, labels, error messages, system feedback*

**Guidelines:**
{{#each microcopy_guidelines}}
- {{this}}
{{/each}}

**Examples:**
| Context | ✅ Do | ❌ Don't |
|---------|-------|---------|
{{#each microcopy_examples}}
| {{this.context}} | {{this.do}} | {{this.dont}} |
{{/each}}

### Marketing Content

*Headlines, feature descriptions, value propositions*

**Guidelines:**
{{#each marketing_guidelines}}
- {{this}}
{{/each}}

### Informational Content

*Service descriptions, about pages, FAQs*

**Guidelines:**
{{#each informational_guidelines}}
- {{this}}
{{/each}}

---

## SEO Strategy

### Page-Keyword Map (B2B SaaS Landing Page)

| Page | URL Slug | Primary Keyword (EN) | Secondary Keyword (EN) |
|------|----------|---------------------|----------------------|
| Homepage | / | AI dental receptionist | Voice AI for dental clinics |
| Features | /features | Automated dental scheduling software | Multilingual dental booking AI |
| Alternatives | /vs-answering-services | Dental answering service alternatives | How to reduce missed calls in dental practice |

### URL Structure

**Pattern:**
```
example.com/{slug}          → English
example.com/ta/{slug}        → Tamil
```

### Primary Keywords (by language)

**English:**
- AI dental receptionist
- Automated dental scheduling software
- Dental answering service alternatives
- Voice AI for Indian clinics

### Structured Data Plan

| Page Type | Schema Type | Key Properties |
|-----------|-------------|----------------|
| SaaS Landing Pages | SoftwareApplication | name, applicationCategory, operatingSystem, offers |
| Clinic Site | LocalBusiness | name, address, telephone, openingHours, medicalSpecialty |

### Keyword Usage Guidelines

- **Page titles:** Primary keyword + brand name (60 chars or less)
- **Meta descriptions:** Primary keyword + benefit + CTA (150-160 chars)
- **H1 headings:** Primary keyword (can differ from title tag)
- **Body content:** Natural mentions, not stuffed
- **URL slugs:** Short, keyword-rich

---

## Content Structure Principles

### Structure Type
Action-Oriented Interfaces (B2C & B2B)

### User's Vision
The user envisions a system built on anticipation rather than reaction. The interfaces must immediately prove their value without requiring the user to "dig" for answers. 

### Content Priorities

**Must be prominent (visible immediately):**
- **Patient Web Widget:** Context-Aware Hero Buttons (e.g., "I'm in pain right now", "Check my insurance"). The content must adapt based on the specific webpage the patient is currently viewing. It eliminates the "Blank Page" problem.
- **Owner Dashboard:** The "After-Hours ROI Snapshot." Specifically, dollar-denominated metrics showing "Recovered Leakage" (appointments booked while closed and the estimated production value of those appointments).

### Navigation Principles
- **Patient Web Widget:** Anticipation over Conversation. Offer solutions before the question is asked.
- **Owner Dashboard:** Proof of Value (ROI) over Raw Data. Frame the AI as a profit center, not an expense.

### Not Included
- Generic "How can I help you?" chat bubbles on the web widget.
- Purely technical metrics (e.g., "API uptime" or raw "Total Conversations") taking precedence on the owner dashboard home screen.

### Clarity Level

{{clarity_level}}

---

## Content Ownership

| Content Type | Owner | Update Frequency |
|--------------|-------|------------------|
| AI System Prompts | Product Owner | As needed for tuning |
| Web Widget Copy | Product Owner | Rarely |
| Dashboard UI Text | Product Owner | With new features |

---

## Writing Checklist

Before publishing any content, verify:

- [ ] Tone matches the "Neighborhood Nurse" guidelines (Empathetic, clear, calm).
- [ ] Language is appropriate for the target audience (avoiding clinical jargon).
- [ ] SEO Keywords included naturally (for B2B SaaS pages).
- [ ] Spelling and grammar checked.
- [ ] Accessible language used throughout.

---

## Next Steps

- [ ] **Visual Direction** — Establish visual style and brand
- [ ] **Phase 2: Trigger Mapping** — Connect content to user psychology
- [ ] **Phase 4: UX Design** — Apply tone to interface copy

---

_Generated by Whiteport Design Studio_

