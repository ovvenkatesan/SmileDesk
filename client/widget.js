// client/widget.js

// CONFIGURATION: Set this to your backend API URL.
// In production, this might be a relative path like '/api/token' 
// or an environment variable injected during build.
const API_BASE_URL = "http://34.82.17.6:8000";

document.addEventListener('DOMContentLoaded', () => {
  const callButton = document.getElementById('call-button');
  const statusText = callButton.querySelector('.status-text');
  
  if (typeof window.LivekitClient === 'undefined') {
    console.error('LiveKit JS SDK not loaded.');
    statusText.innerText = 'Error: SDK Missing';
    return;
  }

  const { Room, RoomEvent, setLogLevel } = window.LivekitClient;
  setLogLevel('error');

  const room = new Room({
    adaptiveStream: true,
    dynacast: true,
  });

  // Handle Room Events
  room.on(RoomEvent.Connected, () => {
    updateButtonState('active', 'Connected (Click to hang up)');
    console.log('Room connected');
  });

  room.on(RoomEvent.Disconnected, () => {
    updateButtonState('default', 'Talk to us');
    console.log('Room disconnected');
  });

  // Handle remote audio playback
  room.on(RoomEvent.TrackSubscribed, (track, publication, participant) => {
    if (track.kind === 'audio') {
      const audioElement = track.attach();
      // Optional: append to DOM if needed for some browser policies, 
      // though LiveKit usually handles playing automatically.
      document.body.appendChild(audioElement);
      console.log('Attached remote audio track');
    }
  });
  
  room.on(RoomEvent.TrackUnsubscribed, (track, publication, participant) => {
    track.detach();
  });

  let isConnecting = false;

  // Handle button click
  callButton.addEventListener('click', async () => {
    // Disconnect if already connected
    if (room.state === 'connected') {
      room.disconnect();
      return;
    }

    if (isConnecting) return;

    try {
      isConnecting = true;
      updateButtonState('connecting', 'Connecting...');

      // Request microphone access
      await navigator.mediaDevices.getUserMedia({ audio: true, video: false });

      // Fetch token from our local Python API
      const response = await fetch(`${API_BASE_URL}/api/token`);
      if (!response.ok) {
        throw new Error("Failed to fetch LiveKit token from server. Is the API running?");
      }
      
      const data = await response.json();
      
      if (!data.url || !data.token) {
        throw new Error("Invalid token data received from server.");
      }

      // Connect to LiveKit
      await room.connect(data.url, data.token);
      
      // Publish local microphone to the room so the agent can hear us
      await room.localParticipant.setMicrophoneEnabled(true);

      // Note: State updates are handled by RoomEvent.Connected

    } catch (error) {
      console.error("Connection failed details:", error);
      let errorMsg = error.message;
      if (error.name === "NotAllowedError" || error.name === "NotFoundError") {
        errorMsg = "Microphone access was denied or no microphone was found. Please allow microphone permissions.";
      }
      alert("Failed to connect:\n" + errorMsg);
      updateButtonState('default', 'Talk to us');
    } finally {
      isConnecting = false;
    }
  });

  function updateButtonState(stateClass, text) {
    callButton.className = `fab ${stateClass}`;
    statusText.innerText = text;
  }
});
