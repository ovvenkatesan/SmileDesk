// client/widget.js

document.addEventListener('DOMContentLoaded', () => {
    const callButton = document.getElementById('call-button');
    const statusText = callButton.querySelector('.status-text');
    
    // Check if LiveKit is loaded
    if (typeof window.LivekitClient === 'undefined') {
        console.error('LiveKit JS SDK not loaded.');
        statusText.innerText = 'Error: SDK Missing';
        return;
    }

    const { Room, RoomEvent } = window.LivekitClient;
    const room = new Room({
        adaptiveStream: true,
        dynacast: true,
    });

    console.log("LiveKit Room initialized:", room);

    // Initial state setup
    // We will wire up connection logic in the next phase.
});