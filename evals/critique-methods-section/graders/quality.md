---
type: llm
weight: 1
---

The response critiques a thin modelling methods section without rewriting it.

PASS only if it identifies at least FIVE of the following gaps, each as a concrete
request a reviewer would make:
- No parameter table with sources and a fixed/sampled/fitted column.
- Priors, chains, iterations, warm-up and convergence diagnostics for the MCMC are
  absent.
- The observation model linking model infections to hospital admissions (reporting /
  hospitalisation probability by age) is not stated.
- The intervention scenarios are not enumerated (coverage values, timing, duration,
  assumed efficacy and waning for the vaccine and the monoclonal antibody), and no
  baseline scenario is named.
- "Sensitivity analyses were conducted" says neither what was varied nor with what
  result.
- Software version, packages, and code/data availability are missing.
- No reporting guideline is named.
- Immunity assumptions (waning, maternal antibodies, seasonality forcing) are absent.

It must also NOT rewrite the section as new prose. A brief example of what a
sentence could look like is fine; a full replacement section is a FAIL.

FAIL if fewer than five gaps are identified, if the critique is generic ("add more
detail"), or if the response rewrites the section.
