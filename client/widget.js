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

    let isConnecting = false;

    // Handle button click
    callButton.addEventListener('click', async () => {
        // If already connected, do nothing (disconnect logic handled in next task)
        if (room.state === 'connected' || isConnecting) {
            return;
        }

        try {
            isConnecting = true;
            updateButtonState('connecting', 'Connecting...');

            // Request microphone access early to ensure permissions
            await navigator.mediaDevices.getUserMedia({ audio: true, video: false });

            // For static testing: prompt for URL and Token
            // In production, these should be fetched from your backend API
            const url = window.prompt("Enter LiveKit WebSocket URL (e.g., wss://your-project.livekit.cloud):");
            if (!url) throw new Error("Connection URL required.");
            
            const token = window.prompt("Enter LiveKit Access Token:");
            if (!token) throw new Error("Access Token required.");

            // Connect to LiveKit
            await room.connect(url, token);
            console.log("LiveKit Room initialized and connected:", room);
            
            // State updates for successful connection
            updateButtonState('active', 'Connected (Click to hang up)');
            
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