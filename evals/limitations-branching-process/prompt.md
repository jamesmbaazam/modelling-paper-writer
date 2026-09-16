---
tags: [discussion, limitations]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Write the limitations paragraph for the Discussion of our paper. The model is a stochastic
branching process of SARS-CoV-2 transmission with contact tracing, seeded with 20 initial
cases, no age structure, no household structure, homogeneous mixing, fixed 80% contact
tracing coverage, and a delay from symptom onset to isolation sampled from a lognormal with
median 3.4 days. We assumed all traced contacts comply with quarantine. The paper's main
result is that outbreaks are controlled in >80% of simulations when R0 = 1.5 but <40% when
R0 = 3.5. We ran sensitivity analyses on tracing coverage (40–100%) and delay (median 2–8
days) but not on compliance.
