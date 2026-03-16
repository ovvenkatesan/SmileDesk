# Conversation Flow: Constraints

## 1. Opening
**Saga:** Before we finalize this Brief, let's establish our design parameters—what some might call constraints. Knowing our boundaries early actually gives us the freedom to design the best possible solution within them.

Are there any hard boundaries we need to respect for the MVP (Phase 1) launch of Smile Garden? 

For example:
- **Technical:** Must it strictly integrate *only* with Cal.com initially, or are there other legacy systems?
- **Timeline:** Do you have a strict launch date or milestone we must hit?
- **Budget:** Are there constraints on API costs (e.g., ElevenLabs/Sarvam TTS or Deepgram STT per-minute costs) that will dictate how chatty the bot is allowed to be?
**User:** initally we will go with cal.com and leter on we may change to google calendar and time line ASAP and Budget is As minimum as possible without affecting the quality of the serice

## 2. Reflection
**Saga:** Got it. These are very clear design parameters:

**Technical:** We will use Cal.com for the MVP, but the architecture must remain modular so we can easily swap to or add Google Calendar in a future iteration.
**Timeline:** ASAP (we need to prioritize the core "concierge" flow over "nice-to-have" edge features to get to market quickly).
**Budget/Quality:** Minimal API spend, but *not* at the expense of the core empathetic quality. This means we might need to be smart about system prompts (keeping them lean to save on Gemini token costs) and perhaps optimizing the TTS/STT vendor choices (e.g., using Deepgram's fastest/cheapest models that still maintain high accuracy).

What parts of the project are *flexible*? For example, are you open to the initial web widget just being a simple "click to call" button rather than a fully branded custom UI, just to speed up the ASAP launch?
**User:** very simple, standard "click to call" component is enough

## Final Output
**Constraints as Design Parameters:**
- **Technical/Integrations:** Built initially for Cal.com, but calendar integration logic must be modular/abstracted to allow swapping to Google Calendar in the future without rebuilding the core state engine.
- **Timeline vs. Scope:** Time-to-market is "ASAP." This necessitates a lean UI approach; the web widget will be a standard, unbranded "click to call" component rather than a custom-designed interface, focusing all development effort on the backend voice orchestration.
- **Budget vs. Quality:** API costs (Gemini, Deepgram, Sarvam) must be minimized, but strictly *never* at the expense of the "empathetic concierge" quality. Cost savings must be found in structural efficiency (lean prompting, efficient state updates) rather than degrading the voice model quality.