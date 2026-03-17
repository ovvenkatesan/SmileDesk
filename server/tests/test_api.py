import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Smile Garden Voice AI API is running"}

def test_get_roi_snapshot():
    response = client.get("/api/dashboard/roi")
    assert response.status_code == 200
    data = response.json()
    assert "leads_saved" in data
    assert "estimated_value" in data

def test_get_agent_status():
    response = client.get("/api/dashboard/agent-status")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] in ["online", "offline", "on_call"]

def test_get_call_logs():
    response = client.get("/api/dashboard/calls")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "id" in data[0]
        assert "caller_number" in data[0]
        assert "duration_seconds" in data[0]

def test_get_call_details():
    # Assuming call id '1' exists in mock data
    response = client.get("/api/dashboard/calls/1")
    assert response.status_code == 200
    data = response.json()
    assert "transcript" in data
    assert "sentiment" in data
