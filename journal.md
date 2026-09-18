# Learning Journal

## Day 1 — 2026-08-19

- "**What I learned**":
    The AI landscape as nested layers — AI ⊃ ML ⊃ GenAI ⊃ LLMs. AI = any machine doing smart things; ML = learns patterns         from data; GenAI = creates new content; LLMs = language models that predict the next word (Claude is one). Product-leader      lesson: match the tool to the job — don't use an LLM where plain ML fits. Also learned: a Git commit is a local save on my     computer, and a push uploads it to GitHub.
- **"What I built**":
-     
  Set up my ai-residency workspace (README, journal, folders), made my first Git commit, and pushed my first repo to GitHub.
  
-**"Questions I still have**":

## Day2 - 2026-08-20

- "**What I learned**":
-     An LLM generates text by predicting the next token in a loop. Text is read as tokens (~4 characters each, roughly ¾ of a word) and I pay per token, so tokens = cost and speed. The context window is the model's limited working memory — when it fills, early content drops off, which is why RAG is needed for large documents. Also: a peaked probability means a strong pattern (confident), a flat spread means the model is guessing (hallucination risk).
- **"What I built**":
-     Ran experiments in Claude on prediction confidence, tokenization, and the context window.
- -**"Questions I still have**":
-

## Day 5 — 2026-09-18

- "**What I learned**":
-     Reaching for an LLM by default is a trap — the better habit is to check fit first: is the input actually language/fuzzy, can the task tolerate a non-deterministic answer, does a simpler tool (regex, SQL, rules engine, classic ML) already solve it, and what's the cost if it's wrong. The best real systems are usually hybrids — LLM for the fuzzy edges (understanding messy input, generating natural language), deterministic code for the exact parts (math, validation, business rules) — not an all-or-nothing choice.
- **"What I built**":
-     Wrote `notes/ai-fit-checklist.md`, a reusable "Is AI the right tool?" checklist (the 4 fit questions, a sweet-spot-vs-wrong-tool reference table, and the hybrid-systems principle). Added an "AI Fit Assessment" prompt template to `prompts/prompt-library.md` that takes a described use case, runs it through the 4 questions, and recommends LLM / classic ML / simple code / hybrid / no AI plus risks — without defaulting to "use an LLM."
- **"Questions I still have**":
- 
