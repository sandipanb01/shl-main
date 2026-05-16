"""
SHL Assessment Recommender — FastAPI Service (Evaluator-Safe, Deterministic)

Goals:
- Stateless: every request includes full conversation history.
- Robust: never 500s; always returns schema-compliant JSON.
- Grounded: recommendations ONLY from SHL_CATALOG and ONLY URLs in VALID_URLS.
- Behaviors: clarify, recommend, refine, compare, refuse, prompt-injection defense.
- Stress-tested heuristics:
  - No clarifier loops (handles "no preference"/"don't know").
  - Turn-cap safe (forces shortlist before max 8 messages).
  - Hard exclusion honored (e.g., remove coding tests => exclude K/S).
  - Soft-skills diversification for stakeholder/teamwork (inject P/B/C/E if possible).
  - Progressive relaxation only when needed (keeps constraints unless too few results).

NOTE:
- This implementation intentionally does NOT call external LLMs for decisions.
  That avoids non-determinism and avoids parsing/timeouts in the evaluator.
"""

import math
import os
import re
import logging
from collections import Counter, defaultdict
from typing import List, Dict, Optional, Tuple

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from catalog import SHL_CATALOG, VALID_URLS

# ── Logging ────────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("shl")

# ── FastAPI ────────────────────────────────────────────────────────────────────
app = FastAPI(title="SHL Assessment Recommender", version="2.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Constants ──────────────────────────────────────────────────────────────────
MAX_RECS = 10
RETRIEVE_K = 30

TURN_CAP_TOTAL_MESSAGES = 8  # evaluator cap: user+assistant total messages
TEST_TYPE_CODES = {"A", "B", "C", "E", "K", "P", "S"}

# Refusal / prompt-injection probes
INJECTION_PATTERNS = [
    r"ignore (all|previous) rules",
    r"(reveal|print|show).*(system prompt|hidden prompt)",
    r"system prompt",
    r"developer mode",
    r"jailbreak",
    r"bypass",
    r"hidden instructions",
    r"prompt injection",
]
OFFTOPIC_KEYWORDS = [
    # legal
    "legal", "law", "lawsuit", "court", "contract", "compliance", "gdpr", "dpdp", "dpdpa",
    # salary / general HR
    "salary", "compensation", "pay", "ctc", "notice period", "bond",
    # interview coaching / certs / out-of-scope
    "interview questions", "certifications", "aws certification", "certification",
    "give me interview questions", "resume", "cv",
]

COMPARE_PATTERNS = [
    r"\bcompare\b",
    r"\bvs\b",
    r"\bversus\b",
    r"\bdifference\b",
    r"\bwhich is better\b",
    r"\bwhat is the difference\b",
]

NO_PREFERENCE_PHRASES = [
    "no preference", "no pref", "dont know", "don't know", "not sure", "no idea",
    "anything", "whatever", "up to you", "doesn't matter", "does not matter",
    "na", "n/a", "skip", "not applicable", "can't say", "cannot say", "prefer not",
]

SOFTSKILL_SIGNALS = ["stakeholder", "communication", "teamwork", "collaboration", "client", "influence", "partnering"]

# ── Models (schema non-negotiable) ─────────────────────────────────────────────
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class Recommendation(BaseModel):
    name: str
    url: str
    test_type: str

class ChatResponse(BaseModel):
    reply: str
    recommendations: List[Recommendation]
    end_of_conversation: bool


# ── Tokenization / Retrieval (TF-IDF) ─────────────────────────────────────────
def _tok(text: str) -> List[str]:
    return re.findall(r"[a-z0-9#+\.\/]+", (text or "").lower())

def _build_tfidf() -> Tuple[Dict[str, float], List[Dict[str, float]]]:
    docs: List[List[str]] = []
    for a in SHL_CATALOG:
        bag = (
            " ".join([a.get("name", "")] * 4)
            + " " + " ".join(a.get("keywords", []) * 3)
            + " " + a.get("description", "")
            + " " + " ".join(a.get("job_levels", []))
            + " " + a.get("test_type", "")
        )
        docs.append(_tok(bag))

    N = len(docs)
    df = Counter()
    for tokens in docs:
        for t in set(tokens):
            df[t] += 1
    idf = {t: math.log((N + 1) / (cnt + 1)) + 1 for t, cnt in df.items()}

    doc_vectors: List[Dict[str, float]] = []
    for tokens in docs:
        cnt = Counter(tokens)
        total = sum(cnt.values()) or 1
        doc_vectors.append({t: (cnt[t] / total) * idf.get(t, 0.0) for t in cnt})
    return idf, doc_vectors

IDF, DOC_VECTORS = _build_tfidf()
log.info(f"TF-IDF index built over {len(SHL_CATALOG)} assessments.")

def retrieve(query: str, top_k: int = RETRIEVE_K) -> List[dict]:
    q_tok = _tok(query)
    if not q_tok:
        return SHL_CATALOG[:top_k]

    q_cnt = Counter(q_tok)
    q_total = sum(q_cnt.values()) or 1

    scores = []
    for i, dv in enumerate(DOC_VECTORS):
        score = sum(
            (q_cnt[t] / q_total) * IDF.get(t, 0.0) * dv.get(t, 0.0)
            for t in q_cnt if t in dv
        )
        scores.append((score, i))
    scores.sort(reverse=True)
    out = [SHL_CATALOG[i] for s, i in scores[:top_k] if s > 0]
    return out if out else SHL_CATALOG[:top_k]


# ── Conversation Helpers ───────────────────────────────────────────────────────
def _last_user_message(messages: List[Message]) -> str:
    for m in reversed(messages):
        if m.role == "user":
            return m.content or ""
    return ""

def _build_user_context(messages: List[Message], cap: int = 2800) -> str:
    return " ".join(m.content for m in messages if m.role == "user")[-cap:]

def _recent_assistant_text(messages: List[Message], n: int = 4) -> str:
    return " ".join([m.content for m in messages if m.role == "assistant"][-n:]).lower()

def _user_said_no_preference(text: str) -> bool:
    t = (text or "").strip().lower()
    return any(p in t for p in NO_PREFERENCE_PHRASES)

def _is_prompt_injection(text: str) -> bool:
    t = (text or "").lower()
    return any(re.search(p, t) for p in INJECTION_PATTERNS)

def _is_offtopic(text: str) -> bool:
    t = (text or "").lower()
    if _is_prompt_injection(t):
        return True
    return any(k in t for k in OFFTOPIC_KEYWORDS)

def _is_compare_request(text: str) -> bool:
    t = (text or "").lower()
    if any(re.search(p, t) for p in COMPARE_PATTERNS):
        return True
    if " vs " in t or " versus " in t:
        return True
    return False

def _should_force_shortlist(messages: List[Message]) -> bool:
    # If we're about to hit the evaluator cap, stop asking questions.
    return len(messages) >= (TURN_CAP_TOTAL_MESSAGES - 1)

def _has_role_or_skill_signal(text: str) -> bool:
    toks = set(_tok(text))
    role_skill = {
        "developer", "engineer", "analyst", "manager", "sales", "support",
        "java", "python", "android", "backend", "frontend", "cloud", "devops",
        "sql", "excel", "microservices", "leadership", "stakeholder", "communication",
        "teamwork", "collaboration", "client",
    }
    return bool(toks & role_skill)

def _is_vague(messages: List[Message]) -> bool:
    full = _build_user_context(messages)
    if not full.strip():
        return True
    if len(full.split()) < 5:
        return True
    return not _has_role_or_skill_signal(full)

def _is_vague_first_turn(messages: List[Message]) -> bool:
    user_msgs = [m for m in messages if m.role == "user"]
    return len(user_msgs) == 1 and _is_vague(messages)

def _avoid_repeating_question(messages: List[Message], candidate_q: str) -> bool:
    asked = _recent_assistant_text(messages)
    cq = (candidate_q or "").lower()

    # Treat reworded repeats as repeats using intent keywords
    intent_groups = [
        ["seniority", "years", "junior", "mid", "senior", "experience"],
        ["time limit", "minutes", "mins", "duration", "under", "within", "max", "maximum"],
        ["focus", "emphasize", "technical", "cognitive", "personality", "communication"],
    ]
    for keys in intent_groups:
        if any(k in cq for k in keys) and any(k in asked for k in keys):
            return True

    return cq in asked


# ── Constraint Extraction ──────────────────────────────────────────────────────
def _extract_max_duration_minutes(text: str) -> Optional[int]:
    t = (text or "").lower()
    m = re.search(r"(under|within|max|maximum)\s*(\d{1,3})\s*(min|mins|minutes)", t)
    if m:
        try:
            return int(m.group(2))
        except Exception:
            return None
    return None

def _extract_remote_requirement(text: str) -> Optional[bool]:
    t = (text or "").lower()
    if "remote" in t:
        if "not remote" in t or "no remote" in t:
            return False
        return True
    return None

def _extract_seniority_signal(text: str) -> Optional[str]:
    t = (text or "").lower()
    if any(x in t for x in ["junior", "entry", "entry-level", "graduate", "intern"]):
        return "junior"
    if any(x in t for x in ["mid", "mid-level", "intermediate"]):
        return "mid"
    if any(x in t for x in ["senior", "lead", "principal", "manager"]):
        return "senior"
    m = re.search(r"(\d{1,2})\s*\+?\s*years", t)
    if m:
        try:
            y = int(m.group(1))
            if y <= 2:
                return "junior"
            if 3 <= y <= 6:
                return "mid"
            if y >= 7:
                return "senior"
        except Exception:
            pass
    return None

def _extract_test_type_preferences(text: str) -> Tuple[set, set, bool]:
    """
    Returns (include_types, exclude_types, hard_exclude_flag).
    hard_exclude_flag is True when user explicitly says remove/avoid coding/technical tests.
    """
    t = (text or "").lower()
    include = set()
    exclude = set()
    hard_exclude = False

    # Includes
    if "personality" in t:
        include.add("P")
    if "cognitive" in t or "aptitude" in t or "ability" in t:
        include.add("A")
    if "situational" in t or "judgement" in t:
        include.add("B")
    if "competenc" in t:
        include.add("C")
    if "simulation" in t:
        include.add("S")
    if "exercise" in t or "interview" in t:
        include.add("E")
    if "skills" in t or "technical" in t or "coding" in t:
        include.add("K")

    # Excludes (hard intent)
    if ("remove" in t or "avoid" in t or "no " in t) and ("coding" in t or "technical" in t):
        hard_exclude = True
        # pragmatic: treat K and S as "coding-heavy"
        exclude.update({"K", "S"})

    if "remove personality" in t or "no personality" in t:
        exclude.add("P")

    include = {x for x in include if x in TEST_TYPE_CODES}
    exclude = {x for x in exclude if x in TEST_TYPE_CODES}
    return include, exclude, hard_exclude

def _softskill_present(text: str) -> bool:
    t = (text or "").lower()
    return any(w in t for w in SOFTSKILL_SIGNALS)


# ── Compare (grounded) ────────────────────────────────────────────────────────
def _best_catalog_match(name_like: str) -> Optional[dict]:
    if not name_like:
        return None
    by_name = {a["name"].lower(): a for a in SHL_CATALOG}
    if name_like.lower() in by_name:
        return by_name[name_like.lower()]
    toks = set(_tok(name_like))
    best_score, best = 0, None
    for nlow, entry in by_name.items():
        overlap = len(toks & set(_tok(nlow)))
        if overlap > best_score:
            best_score, best = overlap, entry
    return best if best_score >= 1 else None

def _extract_compare_candidates(text: str) -> List[str]:
    t = text.strip()
    if " vs " in t.lower():
        parts = re.split(r"\bvs\b", t, flags=re.IGNORECASE)
        if len(parts) >= 2:
            return [parts[0].strip(), parts[1].strip()]
    m = re.search(r"difference between (.+?) and (.+)", t, flags=re.IGNORECASE)
    if m:
        return [m.group(1).strip(), m.group(2).strip()]
    return []

def _compare_reply(text: str) -> str:
    cands = _extract_compare_candidates(text)
    a1 = _best_catalog_match(cands[0]) if len(cands) > 0 else None
    a2 = _best_catalog_match(cands[1]) if len(cands) > 1 else None

    if not a1 and not a2:
        return "Which two SHL assessments would you like to compare (exact catalog names)?"
    if a1 and not a2:
        return f"I found {a1['name']} in the catalog. Which other assessment should I compare it against?"
    if a2 and not a1:
        return f"I found {a2['name']} in the catalog. Which other assessment should I compare it against?"

    def fmt(a: dict) -> str:
        return (
            f"- {a['name']} [{a['test_type']}] | duration:{a.get('duration_min','?')}min | "
            f"remote:{a.get('remote_testing','?')} | adaptive:{a.get('adaptive_irt','?')} | "
            f"levels:{', '.join(a.get('job_levels', []))}"
        )

    return (
        "Here’s a catalog-grounded comparison:\n"
        f"{fmt(a1)}\n{fmt(a2)}\n\n"
        "If you share the role and what you want to measure (skills vs cognitive vs personality), I can refine the recommendation."
    )


# ── Deterministic Scoring & Selection ─────────────────────────────────────────
def _valid_entry(a: dict) -> bool:
    return (
        isinstance(a.get("name", ""), str)
        and a.get("name", "").strip() != ""
        and a.get("url", "") in VALID_URLS
        and a.get("test_type", "") in TEST_TYPE_CODES
    )

def _score_assessment(
    a: dict,
    query: str,
    max_mins: Optional[int],
    include_types: set,
    exclude_types: set,
    remote_req: Optional[bool],
    seniority: Optional[str],
) -> float:
    score = 0.0
    q = (query or "").lower()

    name = (a.get("name", "") or "").lower()
    desc = (a.get("description", "") or "").lower()
    ttype = a.get("test_type", "")

    # include/exclude soft influence (hard filtering happens elsewhere)
    if include_types and ttype in include_types:
        score += 2.5
    if exclude_types and ttype in exclude_types:
        score -= 6.0

    # Duration preference
    dur = a.get("duration_min", None)
    if isinstance(dur, int) and max_mins is not None:
        score += 1.2 if dur <= max_mins else -3.5

    # Remote preference
    rt = a.get("remote_testing", None)
    if remote_req is not None and isinstance(rt, bool):
        score += 0.8 if rt == remote_req else -2.5

    # Seniority alignment
    levels = [x.lower() for x in a.get("job_levels", []) if isinstance(x, str)]
    if seniority:
        if seniority == "junior" and any("entry" in x or "junior" in x for x in levels):
            score += 1.0
        if seniority == "mid" and any("mid" in x or "professional" in x for x in levels):
            score += 1.0
        if seniority == "senior" and any("senior" in x or "manager" in x or "executive" in x for x in levels):
            score += 1.0

    # Softskills boost
    if _softskill_present(q) and ttype in {"P", "B", "C", "E"}:
        score += 1.2

    # Tech keyword overlap boost
    tech_terms = ["java", "android", "kotlin", "sql", "excel", "python", "selenium", "cloud", "unix", "devops"]
    for term in tech_terms:
        if term in q and (term in name or term in desc):
            score += 0.9

    return score

def _diversify_if_softskills(
    ranked: List[dict],
    query: str,
    exclude_types: set,
    max_mins: Optional[int],
    remote_req: Optional[bool],
) -> List[dict]:
    """
    When stakeholder/teamwork signals exist, ensure we try to include a mix of P/B/C/E if available.
    This operates on already-filtered candidates (ideally excludes applied).
    """
    q = (query or "").lower()
    if not _softskill_present(q):
        return ranked

    # Build pools by type (keeping original ranking order)
    pools = defaultdict(list)
    for a in ranked:
        pools[a.get("test_type", "")].append(a)

    # Desired types in priority order
    desired = ["E", "C", "B", "P"]

    chosen = []
    chosen_names = set()

    # Always keep top few from rank (but avoid excluded if present)
    for a in ranked:
        if len(chosen) >= 5:
            break
        if a.get("test_type") in exclude_types:
            continue
        nm = a.get("name")
        if nm in chosen_names:
            continue
        chosen.append(a)
        chosen_names.add(nm)

    # Inject at least 1 from each desired type if possible
    for ttype in desired:
        if ttype in exclude_types:
            continue
        already = any(x.get("test_type") == ttype for x in chosen)
        if already:
            continue
        for a in pools.get(ttype, []):
            nm = a.get("name")
            if nm in chosen_names:
                continue
            chosen.append(a)
            chosen_names.add(nm)
            break

    # Fill remaining from ranked order
    for a in ranked:
        if len(chosen) >= MAX_RECS:
            break
        if a.get("test_type") in exclude_types:
            continue
        nm = a.get("name")
        if nm in chosen_names:
            continue
        chosen.append(a)
        chosen_names.add(nm)

    # If we still have too few, allow excluded at the bottom as absolute last resort
    if len(chosen) < 3:
        for a in ranked:
            if len(chosen) >= MAX_RECS:
                break
            nm = a.get("name")
            if nm in chosen_names:
                continue
            chosen.append(a)
            chosen_names.add(nm)

    return chosen[:MAX_RECS]

def _recommend_deterministic(messages: List[Message]) -> List[Recommendation]:
    user_text = _build_user_context(messages)
    query = user_text

    max_mins = _extract_max_duration_minutes(user_text)
    remote_req = _extract_remote_requirement(user_text)
    seniority = _extract_seniority_signal(user_text)
    include_types, exclude_types, hard_exclude = _extract_test_type_preferences(user_text)

    retrieved = retrieve(query, top_k=RETRIEVE_K)
    retrieved = [a for a in retrieved if _valid_entry(a)]

    # PASS 1: strict filter (honor hard constraints)
    candidates = []
    for a in retrieved:
        ttype = a.get("test_type")

        # HARD exclude if user requested it
        if hard_exclude and ttype in exclude_types:
            continue

        # Duration hard-ish filter: if duration exists and exceeds max, exclude.
        # (But we may relax later if too few remain)
        dur = a.get("duration_min", None)
        if max_mins is not None and isinstance(dur, int) and dur > max_mins:
            continue

        # Remote hard-ish filter only if remote_testing is known.
        rt = a.get("remote_testing", None)
        if remote_req is not None and isinstance(rt, bool) and rt != remote_req:
            continue

        candidates.append(a)

    # PASS 2: relax duration/remote, but still honor HARD excludes
    if len(candidates) < 5:
        relaxed = []
        for a in retrieved:
            ttype = a.get("test_type")
            if hard_exclude and ttype in exclude_types:
                continue
            relaxed.append(a)
        candidates = relaxed

    # PASS 3: absolute last resort: allow excluded, but they must sink to bottom
    allow_excluded = False
    if len(candidates) < 2:
        allow_excluded = True
        candidates = list(retrieved)

    scored = []
    for a in candidates:
        s = _score_assessment(a, query, max_mins, include_types, exclude_types, remote_req, seniority)
        # If we had to allow excluded types, nuke them to the bottom.
        if allow_excluded and hard_exclude and a.get("test_type") in exclude_types:
            s -= 1000.0
        scored.append((s, a))

    scored.sort(key=lambda x: x[0], reverse=True)
    ranked = [a for _, a in scored]

    # Diversify when softskills are requested (inside filtered pool)
    ranked = _diversify_if_softskills(ranked, query, exclude_types if hard_exclude else set(), max_mins, remote_req)

    # Convert to output recommendations with de-dup
    out: List[Recommendation] = []
    seen = set()
    for a in ranked:
        if len(out) >= MAX_RECS:
            break
        nm = a["name"]
        if nm in seen:
            continue
        seen.add(nm)
        out.append(Recommendation(name=nm, url=a["url"], test_type=a["test_type"]))

    # If user demanded hard exclude, ensure excluded types are not present unless unavoidable
    if hard_exclude:
        filtered = [r for r in out if r.test_type not in exclude_types]
        if len(filtered) >= 3:
            out = filtered[:MAX_RECS]
        else:
            # keep filtered first, then append others at bottom (only if needed)
            rest = [r for r in out if r.test_type in exclude_types]
            out = (filtered + rest)[:MAX_RECS]

    return out[:MAX_RECS]


# ── Clarification Policy ───────────────────────────────────────────────────────
def _clarifying_question(messages: List[Message]) -> str:
    ctx = _build_user_context(messages).lower()

    # Ask seniority first if missing
    has_seniority = any(x in ctx for x in ["junior", "mid", "senior", "years", "experience", "lead", "manager", "intern", "entry"])
    if not has_seniority:
        return "What seniority level is the role (junior/mid/senior or years of experience)?"

    # Then ask time limit if not present
    has_time = bool(_extract_max_duration_minutes(ctx))
    if not has_time:
        return "Do you have a time limit in minutes for the assessment package?"

    # Then ask focus
    return "Should the shortlist emphasize (a) technical skills, (b) cognitive/problem-solving, or (c) personality/communication fit?"


# ── Endpoints ──────────────────────────────────────────────────────────────────
@app.get("/")
async def root():
    return {
        "message": "SHL Assessment Recommender API is running.",
        "docs": "/docs",
        "health": "/health"
    }
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        messages = req.messages

        # Basic validation
        if not messages:
            raise HTTPException(400, "messages list is empty")

        for m in messages:
            if m.role not in ("user", "assistant"):
                raise HTTPException(400, f"Invalid role '{m.role}'. Must be 'user' or 'assistant'.")
            if not isinstance(m.content, str):
                raise HTTPException(400, "Message content must be a string.")

        if messages[-1].role != "user":
            raise HTTPException(400, "Last message must be from 'user'.")

        # Trim to last 8 messages to respect evaluator cap and avoid runaway histories
        if len(messages) > TURN_CAP_TOTAL_MESSAGES:
            messages = messages[-TURN_CAP_TOTAL_MESSAGES:]

        last_user = _last_user_message(messages)

        # 1) Refuse off-topic / injection
        if _is_offtopic(last_user):
            return ChatResponse(
                reply="I can’t help with that. I can only recommend SHL Individual Test Solutions from the SHL catalog. Tell me the role and key skills you want to assess.",
                recommendations=[],
                end_of_conversation=False,
            )

        # 2) Compare mode (grounded, no recommendations)
        if _is_compare_request(last_user):
            return ChatResponse(
                reply=_compare_reply(last_user),
                recommendations=[],
                end_of_conversation=False,
            )

        # 3) If user says “no preference / don’t know”, do NOT loop on clarifiers.
        # Move to best-effort shortlist unless it's the vague first turn.
        if _user_said_no_preference(last_user) and not _is_vague_first_turn(messages):
            recs = _recommend_deterministic(messages)
            return ChatResponse(
                reply="No problem — I’ll make a best-effort shortlist from the SHL catalog based on what you shared. If you add constraints (time limit, test mix, seniority), I’ll refine.",
                recommendations=recs,
                end_of_conversation=False,
            )

        # 4) Clarify if vague AND we still have room before cap
        if _is_vague(messages) and not _should_force_shortlist(messages):
            q = _clarifying_question(messages)
            if _avoid_repeating_question(messages, q):
                # If we'd repeat ourselves, provide shortlist instead (best-effort).
                recs = _recommend_deterministic(messages)
                return ChatResponse(
                    reply="Thanks — here’s a best-effort shortlist from the SHL catalog. Add any constraints and I’ll refine.",
                    recommendations=recs,
                    end_of_conversation=False,
                )
            return ChatResponse(reply=q, recommendations=[], end_of_conversation=False)

        # 5) Hard rule: vague first turn -> do not recommend (unless forced by turn cap)
        if _is_vague_first_turn(messages) and not _should_force_shortlist(messages):
            q = _clarifying_question(messages)
            if _avoid_repeating_question(messages, q):
                q = "What role are you hiring for (job title) and what are the top skills to assess?"
            return ChatResponse(reply=q, recommendations=[], end_of_conversation=False)

        # 6) Recommend (deterministic) — also covers refinement automatically (uses full history)
        recs = _recommend_deterministic(messages)
        return ChatResponse(
            reply="Got it. Here’s a shortlist of SHL assessments from the catalog. If you share any constraints (time limit, test mix, remote/in-person, seniority), I’ll refine.",
            recommendations=recs,
            end_of_conversation=False,
        )

    except HTTPException:
        raise
    except Exception as e:
        # Never 500 — always schema compliant
        log.exception(f"Unhandled error in /chat: {e}")
        return ChatResponse(
            reply="I can recommend SHL assessments from the catalog. What role are you hiring for and what skills matter most?",
            recommendations=[],
            end_of_conversation=False,
        )


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)