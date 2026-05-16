# SHL Assessment Recommender Engine

An intelligent, production-oriented SHL assessment recommendation API built using FastAPI, deterministic retrieval, constraint-aware ranking, and robust conversational logic.

This system is designed to simulate a real-world recruiter assistant capable of understanding hiring requirements, refining recommendations across multiple conversational turns, and producing grounded SHL assessment recommendations with strong reliability guarantees.

The engine is intentionally architected to remain evaluator-safe, deterministic, and resilient under adversarial or stress-test scenarios.

---

# Core Capabilities

The recommender engine supports:

- Multi-turn hiring conversations
- Constraint-aware recommendation refinement
- Role and skill inference
- Seniority understanding
- Time-limit filtering
- Remote assessment compatibility
- Technical vs behavioral balancing
- Comparison workflows
- Prompt injection resistance
- Off-topic refusal handling
- Conversational memory across turns
- Evaluator-safe deterministic outputs

The system guarantees:
- Schema-safe API responses
- Catalog-grounded recommendations only
- No hallucinated assessment links
- Robust fallback handling
- Exception-safe behavior

---

# Key Engineering Design Decisions

Unlike naive LLM wrappers, this project intentionally separates:

## 1. Deterministic Recommendation Logic
Assessment recommendations are generated using:
- TF-IDF retrieval
- Explicit constraint extraction
- Rule-grounded ranking
- Catalog validation

This avoids:
- hallucinated assessments
- invalid URLs
- inconsistent ranking behavior
- unstable evaluator outputs

---

## 2. LLM Usage Is Restricted

Large Language Models are optionally used only for:
- lightweight conversational phrasing
- natural clarification wording
- concise response polishing

LLMs are NOT trusted for:
- recommendation ranking
- catalog generation
- structured JSON outputs
- schema-critical logic

This dramatically improves production robustness.

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
- Recommendation refinement
- Catalog-grounded validation

---

## Robust Conversational Logic

Supports:

- Clarification flows
- Follow-up refinement requests
- Recommendation regeneration
- Multi-turn conversational memory
- Constraint merging
- Compare requests
- Turn-limit handling
- Graceful fallback responses

---

## Safety & Reliability

- Prompt injection defense
- Off-topic refusal handling
- Exception-safe responses
- URL validation
- Strict schema compliance
- Catalog-grounded recommendations only
- No hallucinated assessments
- Robust evaluator-safe behavior

---

# Supported SHL Test Types

| Code | Type |
|------|------|
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
- Uvicorn
- TF-IDF Retrieval
- Gemini API (optional)
- Deterministic ranking pipeline

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
```

---

# Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/sandipanb01/shl-main.git
cd shl-main
```

---

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the API

## Start FastAPI Server

```bash
uvicorn main:app --reload
```

Expected console output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

# Swagger API Documentation

Once the server starts:

```text
http://127.0.0.1:8000/docs
```

This provides:
- interactive endpoint testing
- request schema validation
- response inspection
- API exploration

---

# Health Check

## Browser

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

---

## Curl Command

```bash
curl -X GET "http://127.0.0.1:8000/health"
```

---

# Chat Endpoint

## Curl Example

### Windows PowerShell

```powershell
curl -X POST "http://127.0.0.1:8000/chat" ^
-H "Content-Type: application/json" ^
-d "{\"messages\":[{\"role\":\"user\",\"content\":\"Hiring a Java backend engineer with communication skills\"}]}"
```

---

## Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java backend engineer with communication skills"
    }
  ]
}
```

---

## Example Response

```json
{
  "reply": "Here’s a shortlist of suitable SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
```

---

# Example Multi-Turn Conversation

```json
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
```

---

# Stress-Test Behaviors Handled

The system is intentionally hardened against:

- vague prompts
- malformed payloads
- contradictory constraints
- excessive conversation length
- prompt injection attempts
- off-topic requests
- invalid roles
- empty requests
- comparison ambiguity
- recommendation refinement conflicts
- hallucination risks

---

# Example Queries

- "Hiring a backend engineer with stakeholder communication skills."
- "Need assessments under 30 minutes."
- "Remove coding-heavy tests."
- "Add personality assessments."
- "Need remote-friendly assessments."
- "Compare two SHL assessments."
- "Focus on teamwork and collaboration."

---

# Deployment

Successfully deployable on:

- Render
- Railway
- Replit
- VPS environments
- Dockerized environments

---

## Recommended Production Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# Deployment Notes

For Render deployment:

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Optional environment variables:

| Variable | Purpose |
|----------|----------|
| GEMINI_API_KEY | Enables optional Gemini conversational polishing |
| PYTHON_VERSION | Recommended: 3.11.9 |

---

# Why This Project Stands Out

This project focuses heavily on production-grade backend engineering principles rather than relying entirely on LLM behavior.

The architecture emphasizes:

- deterministic recommendation pipelines
- evaluator-safe outputs
- explicit constraint extraction
- conversational robustness
- graceful degradation
- schema consistency
- reliability under stress testing

The result is a significantly more stable and production-oriented recommendation engine compared to naive prompt-only implementations.

---

# Future Improvements

Potential future upgrades include:

- Hybrid BM25 + vector retrieval
- Semantic embedding search
- Redis caching
- Multi-language support
- Analytics dashboard
- Recommendation explainability scoring
- Recruiter preference profiles
- Feedback-based ranking optimization
- Async retrieval pipelines

---

# Author

Sandipan Bhattacharjee

GitHub:
https://github.com/sandipanb01

---

# License

MIT License