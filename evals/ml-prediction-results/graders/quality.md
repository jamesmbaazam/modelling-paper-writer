---
type: llm
weight: 1
---

The response is a results paragraph for a clinical prediction model.

PASS only if ALL hold:
- It reports external validation performance as the headline, with the interval, and
  does not lead with internal performance alone.
- It gives the comparator (logistic model AUROC 0.79) next to the headline so the
  reader can see the gain.
- It reports calibration (slope 0.92) and the operating point (threshold, sensitivity,
  specificity), not discrimination alone.
- It states the cohort sizes and event rates, and notes the shift in mortality between
  cohorts.
- Every number either appears in the brief or is computed from numbers in the brief (for example a difference, a percentage, a rate per 1,000, a predictive value, a count back-calculated from a rate, or a date). A computed number is not invented. A number that cannot be traced to the brief is invented.
- It does not say the model "can be used in clinical practice" or similar; any
  implication for use is hedged to what was shown.

FAIL if any number cannot be traced to the brief, if calibration or the operating point is omitted, if
the comparator is omitted, or if clinical readiness is overclaimed.
