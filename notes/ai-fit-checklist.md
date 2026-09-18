# Is AI the Right Tool? — A Fit Checklist

A reusable checklist for deciding whether a problem actually calls for an
LLM (or ML more broadly), or whether it's better solved with simpler code,
a classic algorithm, or no automation at all. Run through this *before*
reaching for a prompt.

The core trap this guards against: LLMs are so general-purpose that they
can be made to sort-of-work on almost anything, which makes it easy to
reach for one even when a 10-line function or a lookup table would be
more accurate, cheaper, faster, and easier to debug.

---

## The 4 Questions

Ask these in order. Any "no" is a reason to look hard at a non-LLM (or
partially non-LLM) approach.

### 1. Language?
Does the task actually involve understanding, generating, or transforming
**natural language** (or another fuzzy, unstructured input like an image
or freeform audio)? If the input and output are structured data —
numbers, fixed categories, well-defined fields — an LLM is rarely the
best first choice.

### 2. Fuzzy-tolerant?
Can the task tolerate **approximate, non-deterministic answers**, or does
it need to be exactly right and reproducible every time? LLMs are
probabilistic; the same input can yield different outputs across calls.
If correctness is binary and must be guaranteed (billing math, compliance
rules, security checks), that's a strong signal to use deterministic code
instead.

### 3. Does a simpler tool already exist?
Before reaching for an LLM, check whether the problem is already solved
by something boring: a regex, a SQL query, a rules engine, a lookup
table, a classic ML classifier, a spellchecker library, a search index.
Simpler tools are cheaper, faster, more testable, and don't hallucinate.
If one exists and covers the real-world input distribution well enough,
use it — or use it as the first pass and reserve the LLM for the
leftover fuzzy cases.

### 4. What's the cost of being wrong?
If the AI gets this wrong, what happens? Rank the failure mode:
- **Low cost** (a slightly awkward summary, a draft that gets edited) →
  LLM is fine, even encouraged.
- **Medium cost** (wrong categorization that a human reviews downstream)
  → LLM is fine with a human-in-the-loop or a confidence threshold.
- **High cost** (wrong medical/legal/financial output, irreversible
  action, silent data corruption) → need strong guardrails: validation,
  human review, deterministic checks — or avoid LLM involvement in the
  decision-critical path entirely.

---

## LLM Sweet Spot vs. Wrong Tool — Quick Reference

| Signal | LLM sweet spot | Wrong tool for LLM |
|---|---|---|
| Input type | Unstructured text/image/freeform speech | Structured data already in clean fields |
| Task shape | Summarize, draft, translate, classify open-ended intent, extract meaning from messy text | Arithmetic, exact lookups, deterministic transforms, sorting/filtering |
| Tolerance for variance | Some variation in phrasing/style is fine or even desirable | Output must be bit-for-bit identical / auditable every run |
| Existing alternative | No good rules-based or ML solution exists | A regex, SQL query, or simple classifier already nails it |
| Failure cost | Low-medium, reviewable, correctable | High, irreversible, or silently wrong |
| Reasoning needed | Judgment calls, ambiguity resolution, synthesis across sources | Pure computation or fixed business logic |
| Example | "Summarize this customer complaint and tag the sentiment" | "Calculate this month's invoice total" |

---

## The Core Principle: Best Systems Are Hybrids

The best real-world systems rarely pick *only* LLM or *only* classic
code. They split the problem:

- **LLM handles the fuzzy edges** — understanding free text, resolving
  ambiguity, generating natural-language output, handling the long tail
  of inputs a rules engine can't anticipate.
- **Code/tools handle the exact parts** — math, validation, database
  lookups, business rules, anything that must be correct and
  reproducible every time.

Concretely, this often looks like: LLM parses/extracts intent → code
validates and executes → LLM (optionally) explains the result back in
natural language. The LLM is the fuzzy front-and-back end; deterministic
code is the trusted middle.

Treat "should this be an LLM call" and "should this be a function call"
as two separate design decisions inside the same system, not a single
either/or choice for the whole product.

---

## Quick Use

1. Walk through the 4 questions for the specific use case.
2. Check it against the reference table.
3. Default to the smallest, most deterministic tool that solves the
   problem; add an LLM only where fuzziness genuinely requires it.
4. If you're still unsure, use the **AI Fit Assessment** prompt template
   in `prompts/prompt-library.md` to get a structured recommendation.
