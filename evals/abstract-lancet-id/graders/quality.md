---
type: llm
weight: 1
---

The response is a structured abstract for The Lancet Infectious Diseases.

PASS only if ALL of the following hold:
- It has the five Lancet fields Background, Methods, Findings, Interpretation, Funding.
- The headline result (about 8,100 cases averted, 95% CrI 5,300–11,600) appears in
  Findings with its interval, and the interval is labelled (CrI, not bare parentheses).
- The counterfactual comparator ("relative to no expansion" or equivalent) is stated
  next to the headline number.
- The stated word count is 300 or fewer, and the abstract is plausibly that length.
- Every number in the abstract appears in the user's brief; no new numbers are invented.
- Interpretation says what should change or what the result implies for decisions,
  not merely that "further research is needed".
- It does not claim to be "the first study" or say "little is known".

FAIL if any of these are missing, if numbers not in the brief appear as findings, or if
the abstract is unstructured prose.
