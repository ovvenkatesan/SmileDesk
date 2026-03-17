# Specification: Smile Garden Dental Web Page & Voice Agent Widget

## Overview
Create a single-page website for Smile Garden Dental Clinic that features a call button anchored to the bottom right. This button allows users to immediately connect and speak directly to our Voice AI agent directly from their browser.

## Functional Requirements
- **Single Page Layout:** A minimal, lightweight landing page for Smile Garden Dental Clinic.
- **Call Button:** A floating action button (FAB) positioned at the bottom right corner of the page.
- **Direct Connect:** Clicking the button immediately requests microphone access from the browser and initiates the connection to the LiveKit server.
- **Agent Integration:** Establish real-time WebRTC audio communication with the backend LiveKit Python agent using the LiveKit JS client.
- **Connection States:** The button should visually indicate connection status (e.g., Connecting, Connected, Disconnect) to provide user feedback.

## Non-Functional Requirements
- **Performance:** Built with static HTML, CSS, and Vanilla JS to guarantee instant loading (<100KB), matching the project's lightweight constraint.
- **Responsiveness:** The layout and the floating button must be fully responsive and work seamlessly on mobile devices.
- **Browser Compatibility:** Support modern browsers capable of handling WebRTC and microphone permissions.

## Acceptance Criteria
- [ ] The webpage displays basic Smile Garden Dental Clinic branding.
- [ ] A call button is visibly anchored to the bottom right of the screen on all device sizes.
- [ ] Clicking the button prompts for microphone permissions (if not already granted).
- [ ] Upon granting permission, the browser successfully connects to the backend LiveKit room.
- [ ] Two-way audio communication with the Voice AI agent is established.
- [ ] The user can click the button again (or a stop button) to disconnect the call.

## Out of Scope
- Building the full Next.js Owner Dashboard.
- SIP Trunking / Vobiz integration (this track handles web-based WebRTC only).
- Complex UI modals for the widget (going with "Direct Connect" approach).