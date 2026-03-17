# LiveKit SIP Ingress Setup Guide (Vobiz)

This document outlines the steps required to configure LiveKit Cloud to receive incoming SIP calls from the Vobiz SIP trunk for the Smile Garden Voice AI Agent.

## Prerequisites
- A LiveKit Cloud project.
- The `livekit-cli` installed locally.
- Access to your Vobiz SIP provider portal.

## Step 1: Create a SIP Ingress Trunk in LiveKit
First, you need to tell LiveKit Cloud to expect and accept SIP connections from your provider.

Using the LiveKit CLI:
```bash
lk sip inbound create \
  --name "vobiz-inbound" \
  --numbers "+1234567890" \ # Replace with your actual Vobiz phone number(s)
  --auth-username "vobiz_user" \ # If Vobiz requires authentication to send to you
  --auth-password "vobiz_pass"
```

*Note: LiveKit will provide you with a SIP URI (e.g., `sip:+1234567890@sip.livekit.cloud`). Keep this handy.*

## Step 2: Configure Vobiz to Point to LiveKit
Log into your Vobiz dashboard and configure your phone number's routing:
1. Locate the routing or SIP forwarding section for your number.
2. Set the destination to the LiveKit SIP URI provided in Step 1.
3. Ensure the audio codec is set to G.711 (PCMU/PCMA) or Opus, which LiveKit supports.

## Step 3: Create a SIP Dispatch Rule
LiveKit needs to know what to do when a call arrives on that trunk. A Dispatch Rule tells LiveKit which Room to place the caller into.

For the Voice Agent, we typically want a unique room per call.

Create a `dispatch.json` file:
```json
{
  "name": "route-all-to-agent",
  "trunkIds": ["<TRUNK_ID_FROM_STEP_1>"],
  "rule": {
    "dispatchRuleIndividual": {
      "roomPrefix": "call-"
    }
  }
}
```

Apply the rule using the CLI:
```bash
lk sip dispatch create --request dispatch.json
```
*This rule will automatically create a room named `call-<random-uuid>` for every incoming SIP call.*

## Step 4: Worker Connection
When the call connects, the LiveKit SIP participant will join the room. Your Python Voice Agent worker will detect the `RoomEvent.ParticipantConnected` event (or trigger via `AutoSubscribe`) and join the same room to begin speaking.

## Step 5: Caller ID Extraction
The SIP caller's phone number is passed into the LiveKit Room as the participant's `identity` or attached to their `metadata`.
- **Identity:** Usually follows the format `sip:<caller-number>@<domain>`.
- **Metadata:** Can contain additional SIP headers.

The Python worker should parse this identity to extract the raw phone number for CRM lookup.