---
type: llm
weight: 1
---

The response is the Recommendations section of a best-practice guidance paper.

PASS only if ALL hold:
1. Each recommendation states the cost of ignoring it, using the simulation results in the
   brief (for example the 21% underestimate of the mean, or the 9% upward bias in R_t).
2. At least one recommendation is explicitly negative ("we do not recommend…" or
   equivalent), with a reason.
3. The section ends with, or contains, a bulleted summary of the recommendations that is
   usable on its own.
4. Every number either appears in the brief or is computed from numbers in the brief (for example a difference, a percentage, a rate per 1,000, a predictive value, a count back-calculated from a rate, or a date). A computed number is not invented. A number that cannot be traced to the brief is invented.

FAIL if any condition is violated.
