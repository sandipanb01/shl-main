# SHL Assessment Recommender — Approach Document

**Role:** Research Intern, AI Application — SHL Labs

---

## 1. Design Overview

### Stack & Rationale

| Component | Choice | Why |
|---|---|---|
| Framework | FastAPI + Pydantic | Auto schema validation, async, OpenAPI docs |
| LLM | Gemini 1.5 Flash (Free) | 15 RPM free, fast (<5s), JSON mode, large context |
| Retrieval | TF-IDF cosine similarity | Zero cold-start, no external DB, sub-ms latency |
| Deployment | Render.com (free tier) | Persistent process (no cold-start penalty vs serverless) |

### Architecture: RAG-Lite

Rather than a full vector DB pipeline (FAISS + embedding API), I built an in-process TF-IDF index at startup in <50ms. The catalog is indexed with weighted fields:

- Assessment name: ×4 weight
- Keywords: ×3 weight
- Description: ×1 weight

On every `/chat` call, the top-14 retrieved candidates are injected into the system prompt as "primary candidates", grounding the LLM without restricting it if a better match exists. This eliminates embedding API latency and keeps each call well under the 30-second timeout.

### Agent Behavior (State Machine via Prompt)

Four modes encoded in system prompt:
1. **CLARIFY** — ask one focused question if query is vague
2. **RECOMMEND** — 1–10 grounded assessments once context is sufficient
3. **REFINE** — update shortlist on constraint changes (not restart)
4. **COMPARE** — grounded comparison using only catalog metadata

Turn count is tracked; at turn ≥7 the model is instructed to give its best shortlist without further questions, respecting the 8-turn cap.

### Hallucination Prevention

Post-LLM validation (`_ground_recommendations`) fuzzy-matches every LLM-returned name against the catalog using word-overlap scoring. Anything with zero overlap is silently dropped. URLs are always sourced from the catalog dictionary — the LLM never writes URLs to the final output directly.

---

## 2. Prompt Engineering

The system prompt contains:
- Complete one-line-per-assessment catalog summary (keeps tokens low)
- Retrieval-augmented top-14 candidates injected per call
- Explicit mode instructions (CLARIFY / RECOMMEND / REFINE / COMPARE)
- Hard refusal triggers: legal, salary, off-topic, prompt injection
- JSON-only output enforcement using Gemini's native `response_mime_type="application/json"`
- Turn-cap awareness instructions

Using `temperature=0.2` keeps responses deterministic and reduces hallucination risk.

---

## 3. Evaluation

### Hard Evals
- Schema compliance: every response validated against Pydantic model
- URL validation: post-LLM grounding drops any non-catalog URL
- Turn cap: server-side check at turn ≥7

### Recall@10 Spot-Check
Tested against 3 representative personas:
- *Java developer, mid-level, stakeholder work* → Java 8, OPQ32r, Business Analysis, Verify Numerical in top 10 ✓
- *Senior Data Scientist, Python/ML/SQL* → Python, Data Science, SQL, OPQ32r, Automata DS in top 10 ✓
- *Entry-level customer service, call centre* → Call Center Solution, Customer Contact, Reading Comprehension ✓

### Behavior Probes
- Vague turn-1 query → no recs (server-side guard + prompt) ✓
- Prompt injection → graceful refusal, no recs ✓
- Legal/salary question → polite out-of-scope refusal ✓
- Refinement (add personality) → shortlist updated, not reset ✓
- Job description paste → shortlist in 1 turn ✓

### What Didn't Work Initially
1. Without retrieval injection, Gemini occasionally invented assessment names like "SHL Leadership Pro". Fixed by TF-IDF retrieval + post-LLM grounding.
2. Gemini without `response_mime_type="application/json"` added markdown fences around JSON inconsistently. Fixed by using native JSON mode.
3. First version didn't strip recs on vague first turn at the server level — relying only on the prompt was insufficient. Added server-side `_is_vague_first_turn()` guard.

---

## 4. AI Tools Used

Used Claude (claude.ai) for code review, edge-case brainstorming, and prompt iteration. All code reflects genuine understanding of design choices — no agentic/no-code builders used.
