---
type: llm
weight: 1
---

The response is a limitations paragraph for a branching-process contact-tracing model.

PASS only if ALL hold:
- Each limitation names the specific question the model cannot answer because of it
  (e.g. no household structure → cannot evaluate household quarantine), not just that
  the model "is a simplification" or "does not capture all complexity".
- At least one limitation states the likely direction of bias on the main result
  (e.g. assuming full quarantine compliance makes control look more feasible than it is).
- It distinguishes limitations that were discharged by the sensitivity analyses
  (coverage, delay) from those that remain live (compliance, homogeneous mixing).
- Every number either appears in the brief or is computed from numbers in the brief (for example a difference, a percentage, a rate per 1,000, a predictive value, a count back-calculated from a rate, or a date). A computed number is not invented. A number that cannot be traced to the brief is invented.

FAIL if the paragraph is a generic list of model simplifications with no consequence
stated, if it invents sensitivity results, or if it is written as a bulleted checklist
rather than manuscript prose.
