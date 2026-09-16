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
- It contains no invented numbers beyond those in the brief.

FAIL if the paragraph is a generic list of model simplifications with no consequence
stated, if it invents sensitivity results, or if it is written as a bulleted checklist
rather than manuscript prose.
