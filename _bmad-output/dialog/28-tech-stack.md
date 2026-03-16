# Conversation Flow: Tech Stack

## 1. Opening
**Saga:** Since you already outlined the core backend stack for the AI orchestration (Python, LiveKit, Deepgram, Gemini, Sarvam), we just need to quickly define the frontend framework for the interfaces.

You mentioned earlier that the MVP will consist of:
1. A very simple, unbranded "click to call" web widget (embedded on clinic sites).
2. A Progressive Web App (PWA) for the Owner Dashboard.

For the frontend development, what is your preferred stack? 
For example, we commonly see:
- **Next.js (React) + Tailwind CSS:** Great for fast dashboard development and easy PWA configuration.
- **Vue/Nuxt:** If your team prefers a slightly lighter footprint.
- **Vanilla JS / Web Components:** Best for the embeddable web widget to ensure it doesn't conflict with whatever CMS the clinic uses (WordPress, Wix, etc.).

Do you have a specific frontend framework and styling approach in mind for these two pieces?
**User:** your choice

## 2. Recommendation
**Saga:** Excellent. Given the goals and constraints we've established, here is the exact frontend stack I recommend to pair with your Python backend:

**1. The Owner Dashboard (PWA):**
- **Framework:** Next.js (React)
- **Styling:** Tailwind CSS + shadcn/ui
- **Rationale:** Next.js makes building a PWA trivial and handles data fetching beautifully. Pairing it with Tailwind and shadcn/ui allows us to rapidly build that "Consumer Health" aesthetic (rounded corners, soft colors) without writing everything from scratch. It's the industry standard for fast SaaS dashboard development.

**2. The Patient Web Widget (Embedded):**
- **Framework:** Vanilla JavaScript / Web Components (custom element)
- **Styling:** Shadow DOM scoped CSS
- **Rationale:** If we use React for the widget, we risk bundle size bloat or version conflicts if the clinic's website *also* uses React. A Vanilla JS Web Component encapsulated in a Shadow DOM ensures it loads instantly (vital for 3G medical tourists) and its styling will never clash with the clinic's existing WordPress/Wix CSS.

Does this Next.js + Vanilla JS split sound good to you?
**User:** yes

## Final Output
**Technology Stack Documented:**
- **Backend Orchestration:** Python 3.10+, LiveKit SDK.
- **Dashboard Frontend:** Next.js (React), styled with Tailwind CSS & shadcn/ui.
- **Widget Frontend:** Vanilla JS Web Component with Shadow DOM CSS.