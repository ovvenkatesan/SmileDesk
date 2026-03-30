# 🚀 Smile Garden Voice AI: Startup Guide

Follow these steps to launch the complete ecosystem. You will need **4 separate terminal windows**.

---

## 1. Backend Agent (The "Brain")
This handles the LiveKit connection and the AI conversation logic.
- **Directory:** `D:\Projects\BMad\SmileGardenVoiceAgent\server`
- **Command:**
  ```powershell
  venv\Scripts\activate
  python src/agent.py dev
  ```
- **Expected Output:** `registered worker {"agent_name": "pallavi-voice-agent", ...}`

---

## 2. API Server (The "Bridge")
Provides tokens for the web widget and data for the Admin Dashboard.
- **Directory:** `D:\Projects\BMad\SmileGardenVoiceAgent\server`
- **Command:**
  ```powershell
  venv\Scripts\activate
  uvicorn src.api:app --host 0.0.0.0 --port 8000
  ```
- **Expected Output:** `INFO: Uvicorn running on http://0.0.0.0:8000`

---

## 3. Web Client (The "Patient Landing Page")
The public-facing website with the "Talk to Us" widget.
- **Directory:** `D:\Projects\BMad\SmileGardenVoiceAgent\client`
- **Command:**
  ```powershell
  python -m http.server 3000
  ```
- **Access URL:** [http://localhost:3000](http://localhost:3000)

---

## 4. Admin Dashboard (The "Clinic Management View")
Real-time KPIs, Call Logs, and Recording playback.
- **Directory:** `D:\Projects\BMad\SmileGardenVoiceAgent\dashboard`
- **Command:**
  ```powershell
  npm run dev
  ```
- **Access URL:** [http://localhost:3001](http://localhost:3001) (or check terminal for port)

---

## 🛡️ Quick Health Check
1. **Bilingual Test:** Start a call and speak a mix of Tamil and English.
2. **Transfer Test:** Call from a phone and say "Transfer me to the receptionist."
3. **Dashboard Test:** Refresh the dashboard after a call to see the new log and "Appointments Booked" counter increase.
4. **Recording Test:** Click the "Play" button in the dashboard (Note: Requires LiveKit Egress quota availability).

**Happy Shipping! 🥂**
