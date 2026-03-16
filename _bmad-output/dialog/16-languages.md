# Conversation Flow: Language Strategy

## 1. Opening
**Saga:** Let's discuss the specific languages the Voice AI and the web widget need to support. 

You mentioned earlier that the system will utilize Sarvam AI to support regional languages like Tamil for the local demographics, while also needing to accommodate foreign medical tourists.

So I assume the "Source" or primary language of the system (and the language the prompt/logic will be written in) is English. 

Beyond English and Tamil, are there any other specific languages you must support for the MVP launch (perhaps Hindi, or specific European languages for the medical tourists)? And when the AI speaks those languages, should it maintain that exact same "warm nurse" tone, or does it need to adapt to different cultural norms?
**User:** for MVP , English and Tamil is enough , based on the coutry for for the medical tourists, you can speak those language with curltureal norms you can say 2

## Final Output
**Language Strategy:**
- **Primary Language:** English (used for core logic, dashboard, and foreign tourists).
- **Secondary Language:** Tamil (regional support for local demographic).
- **Translation Approach (Voice):** Real-time language detection via Deepgram/Gemini, with dynamic synthesis via Sarvam AI. 
- **Localization Note:** The tone must adapt to cultural norms based on the language detected (maintaining the core empathy, but adjusting the formality as required by the specific culture).