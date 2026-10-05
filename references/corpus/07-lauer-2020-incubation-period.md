# 07 — Lauer et al. (2020), *Annals of Internal Medicine*
**"The Incubation Period of Coronavirus Disease 2019 (COVID-19) From Publicly Reported Confirmed Cases: Estimation and Application"**
Lauer SA, Grantz KH, Bi Q, Jones FK, Zheng Q, Meredith HR, Azman AS, Reich NG, Lessler J. doi:10.7326/M20-0504. PMC7081172.

**Archetype:** the *rapid parameter-estimation* paper — one well-defined epidemiological quantity, estimated cleanly from scraped public data, translated directly into a policy number.

## Structure
Structured abstract with mandated labels: **Background / Objective / Design / Setting / Participants / Measurements / Results / Limitation / Conclusion / Primary Funding Source** (one sentence each except Results).
`Introduction` (~5 ¶) → `Methods` (`Data Collection`, `Statistical Analysis`, `Role of the Funding Source`) → `Results` (case characteristics; primary log-normal estimates; sensitivity analyses) → `Discussion` (findings → policy → limitations) → Reproducible Research Statement.

Note the journal-imposed **single-sentence "Limitation:" field in the abstract** — the limitation is promoted to the top of the paper, not hidden at the end.

## Opening move
> "A novel human coronavirus, severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), was identified in China in December 2019. There is limited support for many of its key epidemiologic features, including the incubation period for clinical disease (coronavirus disease 2019 [COVID-19]), which has important implications for surveillance and control activities."

Pattern: **new pathogen → the specific quantity that is missing → why that quantity governs a decision.** Three sentences, no throat-clearing.

## Methods
- **Almost no mathematical notation.** The model is named, not written: "parametric accelerated failure time model", "we assumed that the incubation time follows a log-normal distribution, as seen in other acute respiratory viral infections". Distributional choice is justified by biology, then tested against alternatives (gamma, Weibull, Erlang) in an appendix table.
- Assumptions stated as short "We assumed…" sentences: "We assumed that exposure always preceded symptom onset"; "This model conservatively assumes that persons are exposed … immediately before the active monitoring program and assumes perfect ascertainment of symptomatic cases."
- **Interval-censoring described in prose**: "we defined conservative upper and lower bounds for the possible interval of each event."
- Sensitivity analyses are pre-enumerated and each is a named subset: fever-only onset (n=99), mainland China (n=73) vs. outside (n=108), alternative distributions, and an alternative exposure lower bound.
- Software named with version and package: "coarseDataTools and activemonitr packages in the R statistical programming language, version 3.6.2".

## Results
Format is rigid and never varies: **point estimate + unit + (95% CI, lower to upper unit)**, one decimal place, "to" rather than an en dash inside the CI.
> "The median incubation period was estimated to be 5.1 days (95% CI, 4.5 to 5.8 days), and 97.5% of those who develop symptoms will do so within 11.5 days (CI, 8.2 to 15.6 days) of infection."
> "We estimated that fewer than 2.5% of infected persons will show symptoms within 2.2 days (CI, 1.8 to 2.9 days) of exposure…"
> "These estimates imply that, under conservative assumptions, 101 out of every 10 000 cases (99th percentile, 482) will develop symptoms after 14 days of active monitoring or quarantine."

Two moves worth stealing:
1. **Report the policy-relevant quantile, not the mean.** The 97.5th percentile is what sets a quarantine window, so it leads.
2. **Translate to natural frequencies.** "101 out of every 10 000 cases" rather than 1.01%.

## Literature
~19 numbered references, clustered in Introduction and Discussion. Prior estimates are surveyed, then the contribution is framed as *more conservative*, not *more novel*:
> "Our results are broadly consistent with other estimates of the incubation period. Our analysis, which was based on 181 confirmed COVID-19 cases, made more conservative assumptions about the possible window of symptom onset and the potential for continued exposure through transmission clusters outside Wuhan."
Plausibility is anchored to relatives of the pathogen: "in line with those of other known human coronaviruses, including SARS (mean, 5 days; range, 2 to 14 days)".

## Voice
Active, first-person plural, short sentences: "We searched…", "We recorded…", "We classified…". Hedging is placed on *decisions*, not on estimates:
> "Although it is essential to weigh the costs of extending active monitoring or quarantine against the potential or perceived costs of failing to identify a symptomatic case, there may be high-risk scenarios … where it could be prudent to extend the period of active monitoring."

## Discussion and limitations
> "This analysis has several important limitations. Our data include early case reports, with associated uncertainty in the intervals of exposure and symptom onset."
Four limitations, each stated *and then partially discharged* by a sensitivity analysis or by an explanation of direction of bias (confirmed cases "may overrepresent hospitalized persons"). Ends by naming what the study cannot speak to at all: asymptomatic infection.

## Data, code and funding — reproducibility
> "Study protocol: Not applicable. Statistical code and data set: Available at https://github.com/HopkinsIDD/ncov_incubation."
GitHub link **plus** a Zenodo release DOI pinned to the submission, plus an interactive Shiny application, plus explicit preprint disclosure ("posted as a preprint on medRxiv on 4 February 2020").

## Distinctive moves to borrow
- The word **"conservative"** is used as a load-bearing methodological claim and repeated deliberately.
- Every headline number arrives with the decision it informs attached to it.
- Ship a tool, not just an estimate.

## Related files
Other *parameter estimation* exemplars: see [80-simmons-2013-norovirus-immunity](80-simmons-2013-norovirus-immunity.md) for a textbook immunity duration overturned by arithmetic and then re-estimated across six model structures; [54-ganyani-2020-generation-interval](54-ganyani-2020-generation-interval.md) for an interval between two unobserved events recovered from symptom-onset data; [55-stopard-2021-malaria-eip](55-stopard-2021-malaria-eip.md) for a parameter estimated mechanistically, by modelling every scale that generates the data.
