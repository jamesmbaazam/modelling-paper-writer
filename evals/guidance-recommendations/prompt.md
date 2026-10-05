---
tags: [guidance, discussion]
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

We're writing a best-practice paper on estimating the serial interval from contact-tracing
data. Write the Recommendations section. Our simulation results (1,000 simulated outbreaks,
true mean serial interval 5.0 days, SD 2.5):

- Ignoring right truncation during the growth phase underestimated the mean by 21% (3.95
  days) when estimated at day 30 of the outbreak; the bias fell to 4% by day 90.
- Ignoring interval censoring of daily onset dates inflated the estimated SD by 12%.
- A model accounting for both recovered a mean of 5.0 days (95% interval 4.7–5.3).
- Fitting a normal distribution instead of a gamma gave negative serial intervals a 2.3%
  probability, which then propagated into R_t estimates as a 9% upward bias during growth.
- Reporting only the mean, without the SD, made downstream R_t estimates impossible to
  reproduce in 31 of 40 published studies we reviewed.
