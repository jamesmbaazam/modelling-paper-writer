---
type: llm
weight: 1
---

The response rewrites a weak introduction gap statement.

PASS only if ALL hold:
- "Little is known" is replaced by a checkable statement of what previous estimates
  exist or do not (e.g. estimates exist for clade IIb; none from household pairs for
  clade Ib), using [ref] or [Author YEAR] placeholders rather than invented citations.
- The "first study" claim is dropped or replaced with a claim about scope or rigour
  (what the household data and truncation adjustment make possible).
- "Novel" is removed; the method is named by what it does (accounts for right
  truncation).
- The paragraph ends with a "Here, we…" sentence naming the model and the data.
- No invented numbers or citations.

FAIL if any of the three anti-patterns survives, if a citation is fabricated with a
specific author, year or DOI presented as real, or if the response only critiques
without rewriting.
