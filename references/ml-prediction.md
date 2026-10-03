# Machine learning and predictive modelling

Companion to `SKILL.md` §7. Read this for the risk-mapping / trait-prediction, digital
surveillance / nowcasting, clinical-prediction and ML critique / appraisal archetypes.
Everything in `SKILL.md` §1–§6 and §8 still applies; the corpus quotations behind these rules
are in `evidence.md` §7.

## Rules

Worked passages: `examples.md` §12.9–§12.10.

- **Lead with the problem and the burden, never the algorithm or the AUC.** Name the method
  once and justify it by a property of the data.
- **Structure Methods as the pipeline in execution order** (database → covariates →
  fitting → validation → burden), each stage independently auditable.
- **State the train/test split in one unambiguous sentence** ("…excluded from all previous
  steps") and split along the axis you will extrapolate over — temporal or geographic, not
  random. Feature selection, tuning and thresholds live inside the training fold.
- **Report performance with an interval, against a naive baseline, with calibration, and
  (under imbalance) auPRC; give two named operating points; state what made the benchmark
  fair.** Metric set in a fixed order in every table.
- **Confront training-data bias explicitly**: put sampling effort in the model as a
  covariate; fit a model of your own sampling process and show it does not reproduce the
  result; retrain without distrusted features and publish the cost; name the confound that
  could mimic your signal.
- **Interpretation is a result**: importance *and* partial dependence; unify top variables
  into one concept; report the covariate that did not matter; state the adjustment inside
  the claim sentence; ship predictions as a named, falsifiable list.
- **Say which numbers are ordinal**, and localise uncertainty to the places it is largest.
- **Pre-submission appraisal (Wynants 2020, Roberts 2021)**: no outcome leakage, no
  case-control reported as cohort, ≥20 events per variable, calibration assessed, external
  validation on a representative set, architecture benchmarked, no "Frankenstein datasets",
  a usable model artefact, predictors chosen from prior knowledge not data alone.
- **Google Flu Trends lessons**: beat a boring benchmark or drop the claim; nonsense
  predictors surfacing is evidence about the procedure; build in recovery (rolling
  retraining) because platform data-generating processes change.

## Anti-patterns

- Leading with the algorithm, or with the AUC, instead of with the problem and the burden.
- A performance metric with no uncertainty, no baseline, and no named operating point.
- A random train/test split for a model that will be used forward in time or in new places.
- Feature selection, tuning or threshold choice performed before the split.
- Discrimination reported without calibration.
- Sampling bias acknowledged in the Discussion but not modelled, tested, or adjusted for.
- Predictions that cannot be checked because the candidate list was never published.
- "External validation" on a dataset that is not representative of the target population.

## Checklist

Run with `checklist.md` before returning.

- [ ] Problem and burden lead; algorithm named once and justified by a property of the data.
- [ ] Methods subheadings are the pipeline stages in execution order.
- [ ] Split stated in one sentence, along the axis of intended extrapolation, with everything
      held out *before* any tuning.
- [ ] Performance with an interval, against a naive baseline, plus calibration and (under
      imbalance) auPRC; benchmark fairness stated.
- [ ] Sampling bias modelled or tested, not merely acknowledged; the mimicking confound named.
- [ ] Variable importance and partial effects; the null result reported; adjustment stated
      inside the claim sentence.
- [ ] Predictions released as a named, falsifiable list; ordinal quantities labelled as relative.
- [ ] Checked against the pre-submission appraisal list above; TRIPOD+AI or equivalent named.
