# Conversation Flow: Multilingual & SEO

## 1. Opening
**Saga:** We're almost at the finish line! Let's translate our Language and SEO strategy into actual technical platform requirements.

**Multilingual:**
We previously agreed on English (Primary) and Tamil (Secondary). For the SaaS dashboard, you are building in Next.js. Do you plan to implement Next.js standard i18n routing (e.g., `example.com/` for English, `example.com/ta/` for Tamil), or will the MVP dashboard be English-only while only the *Voice AI* speaks Tamil?

**Performance & SEO:**
Because the widget needs to load instantly for medical tourists on 3G, we should mandate a strict performance target for the widget bundle (e.g., under 100KB total).
For the Next.js SaaS landing page, we will mandate Core Web Vitals compliance (LCP < 2.5s) and `SoftwareApplication` Schema markup.

Does restricting the MVP dashboard to English (while keeping the Voice AI multilingual) and setting a strict <100KB payload limit on the web widget sound like the right technical constraints?
**User:** yes

## Final Output
**Multilingual & SEO Constraints Documented:**
- **Multilingual Scope:** The B2B Owner Dashboard and underlying system prompts are English-only. The Patient-facing Voice AI handles real-time multilingual inputs (English/Tamil) via Deepgram/Sarvam.
- **Performance:** Strict sub-100KB bundle size for the Vanilla JS web widget.
- **SEO/Vitals:** Next.js B2B landing pages must hit green Core Web Vitals and implement `SoftwareApplication` schema.