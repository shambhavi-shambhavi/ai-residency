# Prompt Library

Reusable prompt templates. Fill in the bracketed placeholders before use.

---

## AI Fit Assessment

**Purpose:** Given a described use case, evaluate whether AI (specifically
an LLM) is actually the right tool, using the 4-question framework from
`notes/ai-fit-checklist.md`. Prevents defaulting to "just use an LLM" by
forcing an explicit comparison against classic ML, simple code, hybrid
approaches, and doing nothing.

**Template:**

```
You are a pragmatic AI product engineer. Your job is to evaluate whether
AI is the right tool for the use case below — not to justify using AI by
default. You are equally willing to recommend classic ML, plain code, a
hybrid approach, or "no AI needed."

USE CASE:
[describe the use case: what problem is being solved, what the input
looks like, what the output should be, who uses it, and any constraints
like latency, volume, budget, or accuracy requirements]

Evaluate the use case against these 4 questions, answering each
explicitly:

1. Language? — Does this genuinely involve natural language or other
   fuzzy/unstructured input (text, image, freeform audio)? Or is the
   input/output actually structured data?

2. Fuzzy-tolerant? — Can the task tolerate approximate, non-deterministic
   answers, or does it require exact, reproducible correctness every
   time?

3. Does a simpler tool already exist? — Could a regex, SQL query, rules
   engine, lookup table, spellchecker, or classic ML classifier already
   solve this well? Name the specific alternative if one exists.

4. Cost of being wrong? — If the AI/system gets this wrong, what's the
   actual impact? Classify as low / medium / high and explain who is
   harmed and how recoverable the error is.

Then produce:

- **Recommendation:** one of [LLM / classic ML / simple code / hybrid /
  no AI needed], with a one-sentence justification.
- **If hybrid:** specify exactly which part should be LLM (the fuzzy
  part) and which part should be deterministic code/tools (the exact
  part), and how they connect.
- **Risks & guardrails:** list the specific risks of the recommended
  approach (e.g., hallucination, latency, cost, drift, edge cases) and
  the minimum guardrail for each (e.g., validation layer, human review,
  confidence threshold, fallback to rules).
- **What would change the answer:** name one condition under which your
  recommendation would flip (e.g., "if volume exceeds X/day," "if the
  input distribution becomes messier than described").

Do not default to recommending an LLM. If a simpler tool solves this as
well or better, say so plainly, even if the use case was framed as an
"AI project."
```

**Notes:**
- Pair with `notes/ai-fit-checklist.md` — the template operationalizes
  that checklist as a prompt you can run against any pitched use case.
- Useful in product reviews or intake for new AI feature requests, to
  catch "AI-washing" (calling something an AI feature when a simple
  script would do) before engineering time is spent.
