# SHL Conversational Assessment Recommender (FastAPI)

This repo contains the **final `main.py`** for an SHL-style **stateless** conversational assessment recommender, exposed via FastAPI.

## What it does (assignment-aligned)
- **Endpoints**
  - `GET /health` → `{"status":"ok"}`
  - `POST /chat` → returns:
    - `reply` (string)
    - `recommendations` (array; empty while clarifying/refusing/comparing; 1–10 when shortlisting)
    - `end_of_conversation` (boolean)
- **Stateless API**: every `/chat` request includes full conversation history.
- **Grounded recommendations**: recommendations are restricted to the provided catalog/URL allowlist in the project.
- **Required behaviors**
  1. Clarifies vague requests before recommending
  2. Recommends 1–10 assessments once enough context exists
  3. Refines when constraints change mid-conversation
  4. Compares assessments using catalog fields only
  5. Refuses out-of-scope requests (legal/general HR/prompt injection)

## Local run (Windows PowerShell)
From the project directory that contains the full assignment package (catalog, requirements, etc.):

```powershell
uvicorn main:app --reload