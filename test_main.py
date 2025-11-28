from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sales Coach API. Use /coach to get feedback."}

def test_coach_pitch_valid():
    pitch_data = {"pitch_text": "I have a great product that solves all your problems."}
    response = client.post("/coach", json=pitch_data)
    assert response.status_code == 200
    data = response.json()
    assert "feedback" in data
    assert "score" in data
    assert data["pitch_received"] == pitch_data["pitch_text"]

def test_coach_pitch_empty():
    pitch_data = {"pitch_text": ""}
    response = client.post("/coach", json=pitch_data)
    assert response.status_code == 400
