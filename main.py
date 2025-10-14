from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime, timezone
import uuid

# Create the FastAPI app
app = FastAPI(title="Feedback API")

# Define the schema for feedback
class Feedback(BaseModel):
    model_name: str
    input_id: str
    original_prediction: str
    correct_label: str
    comments: str | None = None
    user_id: str | None = None

# In-memory storage (for demo)
feedback_storage = []

@app.post("/feedback", status_code=status.HTTP_201_CREATED)
def submit_feedback(feedback: Feedback):
    feedback_id = str(uuid.uuid4())
    data = {
        "feedback_id": feedback_id,
        "model_name": feedback.model_name,
        "input_id": feedback.input_id,
        "original_prediction": feedback.original_prediction,
        "correct_label": feedback.correct_label,
        "comments": feedback.comments,
        "user_id": feedback.user_id,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    feedback_storage.append(data)
    return {"message": "Feedback received successfully", "feedback_id": feedback_id}

@app.get("/feedback")
def get_feedback():
    return {"feedbacks": feedback_storage}