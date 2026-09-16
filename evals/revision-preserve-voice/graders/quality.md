---
type: llm
weight: 1
---

The response revises a discussion paragraph written in UK English, past tense,
first-person plural.

PASS only if ALL hold:
- UK spellings are preserved (modelled, behaviour, recognise, analyse, colour); no
  US spellings are introduced.
- Past tense and "we" voice are preserved.
- The revised paragraph is shorter than the original but keeps all three points
  (deterministic choice; no stochastic extinction analysis so take-off probabilities
  are approximate; uniform application of risk tiers assumed).
- The edits are visible — either a before/after, a marked-up version, or a short list
  of what changed — rather than a silent rewrite with no indication of what moved.
- Nothing is added beyond this paragraph (no new limitations, no new sections).

FAIL if spelling or tense is changed, if a point is dropped, if the response expands
scope, or if it rewrites without showing what changed.
