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
- In the abstract, every number either appears in the brief or is computed from numbers in the brief (for example a difference, a percentage, a rate per 1,000, a predictive value, a count back-calculated from a rate, or a date). A computed number is not invented. A number that cannot be traced to the brief is invented.
- Interpretation says what should change or what the result implies for decisions,
  not merely that "further research is needed".
- It does not claim to be "the first study" or say "little is known".

FAIL if any of these are missing, if a number that cannot be traced to the brief appears as a finding, or if
the abstract is unstructured prose.
