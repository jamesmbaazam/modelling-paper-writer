---
tags: [ml, results]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

Write the main results paragraph for our paper on a gradient-boosted model predicting
30-day mortality in hospitalised dengue patients, for npj Digital Medicine. Results:
derivation cohort n = 4,812 (Vietnam, 2018–2022), external validation cohort n = 1,207
(Thailand, 2023). AUROC 0.86 (95% CI 0.83–0.89) internal, 0.81 (0.76–0.86) external.
Calibration slope 0.92 external. At the pre-specified threshold (predicted risk ≥ 5%),
sensitivity 84%, specificity 71%. A logistic model on the same 8 predictors: AUROC 0.79
(0.74–0.84) external. Mortality was 3.1% in derivation and 4.4% in validation.
