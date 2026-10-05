# 71 — Wolffram et al. (2023), *PLoS Computational Biology*
**"Collaborative nowcasting of COVID-19 hospitalization incidences in Germany"**
Wolffram D, Abbott S, an der Heiden M, Funk S, Günther F, Hailer D, et al. *PLoS Comput Biol* 19(8):e1011394. doi:10.1371/journal.pcbi.1011394.

**Archetype:** the *pre-registered real-time nowcast comparison* — eight independently run nowcasting systems and two ensembles, applied every day for five months to an indicator that set legal thresholds, scored against a pre-specified final data version. It is the nowcasting counterpart of the forecast hubs (Cramer 2022, Bracher 2021b), and what it adds is an account of how a well-defined evaluation can still have the wrong target.

## Structure
PLoS Comput Biol: `Abstract` → `Author summary` → `1 Introduction` → `2 Methods` (*2.1* the indicator's definition · *2.2 Nowcast targets and study period* · *2.3 Overview of models* · ensembles · *2.5 Evaluation metrics*) → `3 Results` (*3.1 Completeness of submissions* · *3.2 Visual inspection* · *3.3 Formal evaluation* · **3.4 Interpretation of evaluation results** · *3.5* unusual reporting · *3.6 Retrospective variations of models* · *3.7 Sensitivity of results to definition of final data*) → `4 Discussion`.

**The Introduction ends with a roadmap paragraph** ("The remainder of the manuscript is structured as follows…"), which a paper with seven Results subsections needs.

**Results run from what was submitted, to what it looked like, to how it scored, to why** — and then three subsections that each test an explanation: unusual events, retrospective model changes, and the choice of target. **A subsection titled *Interpretation of evaluation results* is a deliberate place to reconcile findings that appear to conflict**, instead of scattering the reconciliation through the Discussion.

## Opening move
> "During infectious disease outbreaks, real-time surveillance data contributes to situational awareness and risk management, informing resource planning and control measures. However, the timely interpretation of epidemiological indicators is often hampered by the preliminary nature of real-time data. Due to reporting delays, the most recent data points are usually incomplete and subject to retrospective upward corrections."

**The gap is two named omissions in the literature, each with its consequence**:
> "However, two important aspects are rarely addressed in the current literature. Firstly, few studies assess the performance of methods in real-time settings. The papers we are aware of… contain only retrospective case studies which risk smoothing over some of the difficulties occurring in real time (e.g., major data revisions, time pressure on analysts). Also, few studies include comparisons with existing methods."

The parenthesis says what retrospective evaluation hides. **Name what the easier study design misses, concretely**, and the case for the harder design makes itself.

**The indicator's definition is introduced as the reason the problem is hard, with both sides of the public argument**: hospitalisations are counted by the date of the positive test, not of admission, and "This definition led to some criticism in the public discourse but was defended as a necessary compromise between timeliness and data quality by RKI."

## Methods
- **Pre-register, and tabulate every deviation**: "To facilitate a transparent assessment, we preregistered our evaluation study, specifying the criteria to assess the submitted nowcasts… In some instances, we had to deviate from the protocol. These are detailed in the respective subsections and summarized in Table A1". Deviations reappear in place — the retrospective comparison period was dropped "due to time constraints, only two teams provided complete sets of retrospective nowcasts prior to the beginning of the prospective study."
- **Explain an awkward indicator with individual timelines.** Figure 2 follows eight people, A to H, through positive test, admission and report, and the caption says why each is or is not counted on day *t*: "even though individuals F and G are hospitalized or reported within the period t − 6 to t, they are not counted in the 7-day hospitalization incidence for day t because the positive test is reported before t − 6." **When the estimand's definition is counter-intuitive, draw a handful of individuals through it.**
- **Measure how incomplete the data are before modelling the incompleteness**:
  > "Same-day values covered 50–60% of the ultimately reported hospitalizations, with a slight upward trend over the study period (left panel). Around 85% were reached after 14 days and even after 70 days, there were upward corrections of more than 3%."

  The last clause — corrections still arriving after 70 days — is the fact the Discussion turns on.
- **Show why the official shortcut misleads**: the legal thresholds used the unrevised "frozen" value, and "due to the temporal and geographic differences shown in Fig 3, the same frozen value can translate to rather different final values of the hospitalization incidence."
- **Tabulate the models by the design choices that will later explain their scores.** Table 1 gives each model's uncertainty method, data input, weekday handling, maximum delay and training window — columns chosen so that the Results can point back to them. **Put the comparison table's columns where the explanations will be.**
- **Pre-specify the primary ensemble and say why**: "As the expected number of contributed models was moderate, the MeanEnsemble was expected to be better-behaved than the MedianEnsemble… The MeanEnsemble was therefore prespecified as the primary ensemble approach".
- **Admit an implementation error and bound its effect**: "Regrettably, this consideration was overlooked in our real-time ensemble, leading to some instances of quantile crossing… As this occurred only in a small fraction of instances, we consider the impact on overall results negligible."
- **Explain the scoring rule's components so they can be used diagnostically**: the interval score's "first term characterizes the spread of the predictive distribution, the second penalizes overprediction… and the third term penalizes underprediction."
- **Use a no-correction baseline and be candid about how it was chosen**: FrozenBaseline "applies no correction and just issues the current data version", and "while the study protocol specified that a baseline model was to be included, its definition was only agreed upon later."

## Results
**The headline is a relative score against doing nothing**: "most models were able to reduce the error of the uncorrected time series (FrozenBaseline) by roughly 80% (relative WIS of 0.2), while the ILM model achieved a reduction of about 90% (relative WIS 0.1)."

**Label the analysis that was not pre-registered, and give the reason for it**:
> "As we consider the nowcasts for the most recent days the most relevant from a public health perspective, we conclude with an additional non-preregistered summary of scores across horizons -7 to 0 days."

**Use the score decomposition to name the shared failure**: "Penalties for underprediction make up a very large part of the overall scores for all models except for ILM. This confirms the observation of a downward bias". Calibration is reported separately and is the paper's main negative finding: "All other models were overconfident and did not reach the respective nominal coverage levels."

**Open the interpretation section by conceding the results look contradictory**: "As some of the presented results may seem contradictory at first sight, we provide some additional interpretations." Absolute scores improve with horizon while relative scores worsen; the paper explains why, and traces it to a design choice in Table 1 — "the values of around 40 days as chosen by most teams may have been too low and led models to ignore a non-negligible fraction of hospitalizations still to be added."

**Separate a good score from a good point estimate**: the KIT model scored well on WIS but "did not issue particularly accurate point predictions… Its lower WIS values were primarily a result of better uncertainty quantification."

**State each model's load-bearing assumption, then show the days it broke**:
> "The nowcasting models in our study assumed either that the probability of hospitalization given a positive test remains roughly constant (the ILM model) or that the delay distribution in hospitalizations does so (all other models). In Fig 10, we therefore show four examples where these assumptions were violated."

Overwhelmed hospitals in Saxony, deleted records in Bremen, the Easter weekend, and — for the one model with the other assumption — the shift to Omicron, whose lower severity pushed its nowcasts up. **Group the models by the assumption they share, and illustrate each failure with a dated case.**

**Re-run models retrospectively to isolate a cause, and say when a change is a probe rather than an improvement**: the best model was re-run with a shorter maximum delay — "This was not meant as an improvement but as an adjustment to assess the impact of longer/shorter maximum delays."

**Test the result's sensitivity to the target itself.** Scores are recomputed against later and later data versions, and against a "rolling" target that gives every reference date the same 40 days to fill in. Under the rolling target, "the ensemble nowcasts clearly lead the field."

## Literature
Numbered PLoS citations. The paper places itself in the forecast-hub tradition explicitly — "We aimed for compatibility with the Forecast Hub ecosystem in many technical and methodological aspects, in particular by following the same submission format and evaluation criteria" — so that its results add to an existing evidence base rather than starting a new one. Nowcasting's origins in econometrics and actuarial science are given in one sentence.

## Voice
First-person plural, past tense. The register is unusually self-critical for a study run by the organisers of the platform it evaluates: "Regrettably", "turned out not to be ideal in retrospect", "easier to get right in hindsight than in real time". The criticism is always attached to a fix the reader can adopt.

## Discussion and limitations
**The best model's win is decomposed into two errors that cancelled**:
> "On the one hand, it used a maximum delay that is longer than those of the other models, but, judging by Fig 3, still somewhat too short. On the other hand, the model appears to have a tendency to slightly overpredict the number of hospitalizations added up to a given maximum delay. As these two aspects work in different directions, the resulting nowcasts are overall well-aligned with the defined target"

**When the winner may have won by offsetting errors, say so.** It stops readers adopting the winning model for the wrong reason.

**The ensemble's limitation is structural, not statistical**: "a majority of its members followed similar strategies and had similar weaknesses (specifically a downward bias due to neglecting very long delays)." An unweighted ensemble of models that share a bias inherits it.

**The pre-registered target is defended and then criticised**:
> "As the choice of 8 August 2022 was preregistered and known to all participating teams, the prediction task was well-defined, and we stuck to this choice for our main analysis. Nonetheless, this definition, which was based on the assumption that data would be stable after 100 days, turned out not to be ideal in retrospect. In particular, it implies that for the first day of our study period (22 November 2021), retrospective additions could accumulate over 259 days, while for the last (29 April 2022) this was restricted to 100 days."

**Keep the pre-registered analysis as primary, then show with numbers why it was the wrong target.** The 259-versus-100-day asymmetry makes the problem concrete, and the rolling alternative is offered as the design for the next study.

**What the estimand should include is argued from public-health relevance**: very late additions are probably hospitalisations not primarily due to COVID-19, and "it can be questioned whether hospitalizations a long time after a positive test are relevant for the real-time assessment of healthcare burden."

**The legal shortcut is given its due before it is criticised**: frozen values have "the advantage of simplicity and unambiguity, which are required for actionable guidelines in a legal context… An important downside, however, is that the same frozen value can mean rather different things at different time points and in different locations".

**The comparison is scoped to systems, not models**:
> "we note, however, that the present paper is a comparison of nowcasting systems, which are given by a statistical model, but also various additional analytical choices, in particular the assumed maximum delay and the length of training data used at each time point. These decisions can have a substantial impact on predictive performance… and are easier to get right in hindsight than in real time."

**A real-time comparison ranks analysts' choices as much as methods; say so**, so the ranking is not read as a verdict on the underlying statistical models.

**The uptake by the media is reported with an uncomfortable detail**: "data journalists were overall hesitant to use the ensemble nowcasts and prioritized individual nowcasts based on methods described in peer-reviewed publications. Interestingly, the best-performing models in our study were the MeanEnsemble and the yet unpublished ILM approach."

## Data, code and funding
The nowcasts, the truth data and the evaluation code are in public repositories with a Zenodo release, and each team's code repository is listed in the appendix. **The data versions themselves are recoverable**: "Time-stamped versions of hospitalization data as available at different points in time can be retrieved from the commit history of the repository as well as directly from Robert Koch Institute." For a nowcasting benchmark the vintages are the dataset; keeping them in version control makes the study re-runnable. CRediT roles are itemised for all sixteen authors, who span universities, the national public-health institute, a foreign public-health institute and a newspaper's data team.

## Distinctive moves to borrow
1. **Name what retrospective evaluation hides** — revisions, time pressure — to justify a real-time design.
2. **Pre-register, keep the pre-registered analysis primary, and tabulate every deviation.**
3. **Label non-pre-registered analyses as such, with the reason.**
4. **Draw individual timelines through a counter-intuitive indicator definition.**
5. **Measure the data's incompleteness by delay before modelling it.**
6. **Give the comparison table the columns that will explain the results.**
7. **Admit an implementation error and bound its effect.**
8. **Score relative to a no-correction baseline** and use the score's spread, over- and under-prediction components diagnostically.
9. **Give apparent contradictions their own interpretation subsection.**
10. **Group models by their load-bearing assumption and show a dated case where each broke.**
11. **Re-run models retrospectively as probes**, and say when a change is a probe, not an improvement.
12. **Test sensitivity to the evaluation target**, not only to the models.
13. **Say when the winner won through offsetting errors.**
14. **Scope a real-time comparison to systems** — model plus analysts' choices.
15. **Keep the data vintages in version control.**

## Related files
For the forecast hubs this study adapts to nowcasting see [09-cramer-2022-covid-forecast-hub-evaluation](09-cramer-2022-covid-forecast-hub-evaluation.md), [51-sherratt-2023-european-forecast-hub](51-sherratt-2023-european-forecast-hub.md) and, for the pre-registered German and Polish forecast study by the same lead group, [53-bracher-2021-preregistered-forecasts](53-bracher-2021-preregistered-forecasts.md); for the weighted interval score see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md); for a single nowcasting method evaluated against later data see [43-mcgough-2020-nobbs-nowcasting](43-mcgough-2020-nobbs-nowcasting.md) and [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md); for delay distributions as guidance see [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md). Other *forecast evaluation* exemplars: see [10-reich-2019-flusight-multiyear](10-reich-2019-flusight-multiyear.md) for the multi-team, multi-season influenza comparison and its shared infrastructure; [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md) for forecasts issued in real time and scored afterwards, with calibration, sharpness and bias separated; [52-bosse-2023-transformed-scales](52-bosse-2023-transformed-scales.md) for the argument that the scale forecasts are scored on is itself a choice with consequences.
