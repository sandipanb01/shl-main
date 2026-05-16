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

# API Endpoints

## Health Check

```bash
GET /health

Response:

{
  "status": "ok"
}
Chat Endpoint
POST /chat

Example Request:

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a backend engineer with strong communication skills."
    }
  ]
}

Example Response:

{
  "reply": "Here’s a shortlist of suitable SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}