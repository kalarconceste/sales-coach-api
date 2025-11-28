from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Sales Coach API", version="1.0.0")

class SalesPitch(BaseModel):
    pitch_text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sales Coach API. Use /coach to get feedback."}

@app.post("/coach")
def coach_pitch(pitch: SalesPitch):
    if not pitch.pitch_text:
        raise HTTPException(status_code=400, detail="Pitch text cannot be empty")
    
    # Simulated AI feedback logic
    feedbacks = [
        "Great energy, but try to focus more on the customer's pain points.",
        "Excellent opening! Consider shortening the value proposition.",
        "Good attempt. Remember to ask open-ended questions.",
        "Strong closing, but the introduction needs more hook."
    ]
    
    return {
        "pitch_received": pitch.pitch_text,
        "feedback": random.choice(feedbacks),
        "score": random.randint(70, 100)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
