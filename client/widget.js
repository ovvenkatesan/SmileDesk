// client/widget.js

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
    updateButtonState('default', 'Talk to AI Concierge');
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

      // For static testing: prompt for URL and Token
      const url = window.prompt("Enter LiveKit WebSocket URL (e.g., wss://your-project.livekit.cloud):");
      if (!url) throw new Error("Connection URL required.");

      const token = window.prompt("Enter LiveKit Access Token:");
      if (!token) throw new Error("Access Token required.");

      // Connect to LiveKit
      await room.connect(url, token);

      // Note: State updates are handled by RoomEvent.Connected

    } catch (error) {
      console.error("Connection failed:", error);
      alert("Failed to connect: " + error.message);
      updateButtonState('default', 'Talk to AI Concierge');
    } finally {
      isConnecting = false;
    }
  });

  function updateButtonState(stateClass, text) {
    callButton.className = `fab ${stateClass}`;
    statusText.innerText = text;
  }
});