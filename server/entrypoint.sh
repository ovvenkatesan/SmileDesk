#!/bin/bash

# Start the API Server in the background
echo "Starting API Server on port 8000..."
uvicorn src.api:app --host 0.0.0.0 --port 8000 &

# Start the LiveKit Agent in the foreground
echo "Starting LiveKit Agent..."
python src/agent.py dev