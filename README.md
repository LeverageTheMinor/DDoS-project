SECTION 1 - Title and Description:

\# Feedback API



A FastAPI-based REST API for collecting model feedback

SECTION 2 - Setup Instructions:



\## Setup Instructions



\### 1. Install Required Packages

Open terminal/command prompt in this folder and run:

pip install -r requirements.txt

SECTION 3 - Running the API:



\### 2. Run the API
uvicorn main:app --reload



You should see:

INFO:     Uvicorn running on http://127.0.0.1:8000



SECTION 4 - Testing Instructions:



\### 3. Test the API

Open your browser and go to:

http://127.0.0.1:8000/docs



SECTION 5 - API Documentation:



\## API Endpoints



\### POST /feedback

Submit feedback about a model prediction.



\*\*Example Request:\*\*

{

"model\_name": "sentiment-classifier",

"input\_id": "review-001",

"original\_prediction": "positive",

"correct\_label": "negative",

"comments": "Model missed sarcasm",

"user\_id": "user123"

}

SECTION 6 - GET Endpoint:



\### GET /feedback

Get all submitted feedback.


SECTION 7 - Notes:



\## Notes

\- Currently stores data in memory (resets when server restarts)

\- For production use, connect to a database

