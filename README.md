# SHL Assessment Recommender Engine

An intelligent, production-oriented SHL assessment recommendation API built using FastAPI, deterministic retrieval, constraint-aware ranking, and robust conversational logic.

Designed to handle:
- multi-turn hiring conversations
- vague queries
- refinements and follow-ups
- recommendation constraints
- comparison requests
- prompt injection attempts
- evaluator stress tests
- malformed conversational flows

The system is fully grounded to the SHL catalog and guarantees schema-safe responses.

---

# Features

## Intelligent Recommendation Engine
- Deterministic TF-IDF retrieval
- Constraint-aware ranking
- Role + skill inference
- Seniority detection
- Remote assessment handling
- Duration-aware filtering
- Test-type prioritization

---

## Robust Conversational Logic
Supports:
- Clarification flows
- Refinement requests
- Follow-up constraints
- Recommendation regeneration
- Comparison queries
- Context-aware conversation memory
- Turn-limit handling

---

## Safety & Reliability
- Prompt injection defense
- Off-topic refusal handling
- Catalog-grounded recommendations only
- URL validation
- Schema-safe responses
- Exception-safe API behavior
- No hallucinated assessments

---

# Supported SHL Test Types

| Code | Type |
|---|---|
| A | Ability / Cognitive |
| B | Behavioral / Situational |
| C | Competency |
| E | Interview / Simulation |
| K | Knowledge / Technical |
| P | Personality |
| S | Simulation |

---

# Tech Stack

- FastAPI
- Python
- Pydantic
- TF-IDF Retrieval
- Gemini API (optional natural language enhancement)
- Uvicorn

---

# Project Structure

```text
.
├── main.py
├── catalog.py
├── requirements.txt
├── render.yaml
├── README.md
└── test_agent.py
Local Setup
Clone Repository
git clone https://github.com/sandipanb01/shl-main.git
cd shl-main
Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Running the API
Start FastAPI Server
uvicorn main:app --reload

You should see something like:

INFO:     Uvicorn running on http://127.0.0.1:8000
Swagger API Docs

Once the server starts:

http://127.0.0.1:8000/docs
Health Check
Browser

Open:

http://127.0.0.1:8000/health

Expected Response:

{
  "status": "ok"
}
Curl Command
curl -X GET "http://127.0.0.1:8000/health"
Chat Endpoint
Curl Example
curl -X POST "http://127.0.0.1:8000/chat" ^
-H "Content-Type: application/json" ^
-d "{\"messages\":[{\"role\":\"user\",\"content\":\"Hiring a Java backend engineer with communication skills\"}]}"
Example Request
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java backend engineer with communication skills"
    }
  ]
}
Example Response
{
  "reply": "Here’s a shortlist of SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
Example Multi-Turn Conversation
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a mid-level Java developer."
    },
    {
      "role": "assistant",
      "content": "Any constraints?"
    },
    {
      "role": "user",
      "content": "Under 30 minutes and focus on teamwork."
    }
  ]
}
Deployment

Successfully deployable on:

Render
Railway
Replit
VPS environments

Recommended start command:

uvicorn main:app --host 0.0.0.0 --port $PORT