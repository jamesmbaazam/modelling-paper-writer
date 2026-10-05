---
type: llm
weight: 1
---

The response rewrites three results sentences.

PASS only if ALL hold:
- Each rewritten sentence contains a number from the brief and a comparator (vs. the
  best individual model, vs. the baseline, across horizons, or out of 7 seasons).
- "Performed well", "substantially", "about", "most" are replaced with the actual
  values, not retained.
- Every number either appears in the brief or is computed from numbers in the brief (for example a difference, a percentage, a rate per 1,000, a predictive value, a count back-calculated from a rate, or a date). A computed number is not invented. A number that cannot be traced to the brief is invented.
- The verbs match the evidence: descriptive past tense for what was observed
  ("scored", "was"), no "proves" or "demonstrates that X will".

FAIL if any rewritten sentence still relies on a vague qualifier without a number, if a
number is invented, or if the response adds sentences the user did not ask for beyond
a brief note.
