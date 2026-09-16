---
type: llm
weight: 1
---

The response rewrites a weak introduction gap statement. Judge ONLY the revised paragraph
(the block-quoted text presented as the fix). Ignore the original paragraph if it is quoted
back, and ignore the explanatory notes.

PASS if ALL four hold in the revised paragraph:
1. It does not assert ignorance vaguely. Banned as standalone claims: "little is known",
   "remains scarce", "poorly understood", "evidence is limited". A specific, checkable claim
   is what is wanted, and phrases like "estimates are limited to [named source]" or "we
   identified no estimates from household pairs" are checkable and therefore acceptable.
2. It does not contain a priority claim of the form "the first study to" / "first to".
   Hedged checkable claims such as "to our knowledge, no published estimate has…" are
   acceptable.
3. It does not contain the word "novel".
4. Its final sentence begins "Here, we" or "Here we" and mentions both household
   transmission pairs and a Bayesian model.

Placeholders such as [ref], [Author YEAR] or [describe source] are expected and acceptable.
The year 2024 and the place name South Kivu are from the brief and acceptable.

FAIL only if one of the four conditions is violated.
