# 10 — Reich et al. (2019), *PNAS*
**"A collaborative multiyear, multimodel assessment of seasonal influenza forecasting in the United States"**
*PNAS* 116(8):3146–3154. doi:10.1073/pnas.1812594116. PMC6386665.

**Archetype:** the *multi-team forecast evaluation* paper — many models, one scoring rule, several seasons; the contribution is the comparison infrastructure as much as the result.

## Structure
`Significance` (~150 words) → `Abstract` (~250 words) → `Introduction` (~1000 words, unbroken) → `Results` with declarative subheadings → `Discussion` → `Materials and Methods` (last, per PNAS) → Acknowledgements → 44 references.

Results subheadings are **findings phrased as sentences**, not topics:
- *Performance in Forecasting Week-Ahead Incidence*
- *Performance in Forecasting Seasonal Targets*
- *Comparing Models' Forecasting Performance by Season*
- *Comparison Between Statistical and Compartmental Models*
- *Delayed Case Reporting Impacts Forecast Score*

Materials and Methods subheadings: *FluSight Challenge Overview*, *Summary of Models*, *Metric Used for Evaluation and Comparison*, *Specific Model Comparisons*, *Reproducibility and Data Availability*.

## Opening move
Significance statement: "Accurate prediction of the size and timing of infectious disease outbreaks could help public health officials in planning an appropriate response."

Abstract:
> "Influenza infects an estimated 9–35 million individuals each year in the United States and is a contributing cause for between 12,000 and 56,000 deaths annually. Seasonal outbreaks of influenza are common in temperate regions of the world, with highest incidence typically occurring in colder and drier months of the year. Real-time forecasts of influenza transmission can inform public health response to outbreaks."

Pattern: **burden in numbers → the regularity that makes forecasting possible → what a forecast would buy.** Burden is always quantified with a range, never with "many".

## Methods
- **No model equations in the main text.** The 22 models live in Table 1 with columns for abbreviation, description, reference, and binary flags (uses external data / mechanistic / ensemble). Mechanistic models are described narratively as "variations on the susceptible–infectious–recovered (SIR) model".
- The *scoring rule* is the one thing given full formal treatment, because it is the paper's instrument: `log f_m(z*|x)`, with the modified log score (predictions within ±0.5 percentage points counted as accurate) spelled out, and Equations 1–2 used to justify reporting the **geometric mean of scores** rather than raw log scores, because it is interpretable as an average probability assigned to the truth.
- Prospectivity is a methodological claim, defended explicitly: forecasts were out-of-sample and teams could not refit; the four post-hoc bug fixes are documented rather than hidden.
- A regression (Eq. 3) with fixed effects for model, target and week-of-season is used to *isolate* the effect of data revision — i.e. a secondary analysis designed to answer one alternative explanation.
- Data pulled through a versioned API (DELPHI epidata) so the analysis is re-runnable; ground truth pinned to an explicit date ("as of September 27, 2017").

## Results
CIs inline and parenthetical; scores reported on the interpretable (exponentiated) scale.
> "The model with the highest average score for the week-ahead targets across all regions and seasons was CU-EKF_SIRS. This model achieved a region-specific average forecast score for week-ahead targets between 0.32 and 0.55."
> "Larger revisions to the initially reported data were strongly associated with a decrease in the forecast score for the forecasts made using the initial, unrevised data."
> "average change in forecast score of −0.29 (95% CI: −0.39, −0.19)"
> "In HHS region 9, over 51% of initially reported wILI values ended up being revised by over 0.5 percentage points while in HHS region 5 less than 1% of values were revised that much."

Recurring paragraph shape: **absolute performance → comparison to the historical baseline model → the size of the improvement.** The baseline is the rhetorical anchor for every claim; nothing is "good" in the abstract, only "better than baseline by 0.17".

## Literature
~1 citation per 160 words; concentrated in Introduction and Methods. Positioning is explicitly about scope:
> "While multimodel comparisons exist in the literature for single-outbreak performance, here we compare a consistent set of models over seven influenza seasons."
Field growth is quantified rather than asserted: "Over the past 15 y, the number of published research articles on forecasting infectious diseases has tripled (Web of Science)…"

## Voice
Present tense for the state of the field, past for what the collaboration did. Strongly active with "we" ("we assembled", "we compare", "we expect"); passive reserved for the evaluation protocol ("forecasts are evaluated for accuracy at the end of the season"), which reads as impartiality. Superlatives are always tied to the metric ("the models with the highest average score"), never to quality in general.

Scare quotes used deliberately to flag terms the authors will not take at face value: "big data", "historical baseline".

## Discussion and limitations
> "There are several important limitations to this work as presented. While we have assembled and analyzed a range of models from experienced influenza-forecasting teams, there are large gaps in the types of data and models represented in our library of models."
> "While seven seasons of forecasts from 22 models is the largest study we know of that compares models from multiple teams, this remains a less-than-ideal sample size."
> "these results should not be used to extrapolate hypothetical accuracy in pandemic settings, as these models were optimized specifically to forecast seasonal influenza."

The third is a **scope fence**: an explicit prohibition on a misreading the authors expect. Every limitation is followed by the research it motivates.

## Data, code and funding — reproducibility
> "To maximize the reproducibility and data availability for this project, the data and code for the entire project (excluding specific model code) are publicly available."
GitHub + Zenodo DOI, interactive site (flusightnetwork.io) and Shiny app, and the manuscript itself generated with R 3.5.1 + Sweave/knitr so text and numbers cannot diverge. Conflicts of interest disclosed concretely.

## Distinctive moves to borrow
1. **Complicate your own dichotomy.** The paper sets up statistical vs. mechanistic, then immediately notes real methods blend the two.
2. **Make the baseline the unit of comparison** for every performance claim.
3. Treat the scoring rule as the object requiring rigour when the models themselves are heterogeneous.
4. Dynamic manuscript generation as a reproducibility device.

## Related files
Other *forecast evaluation* exemplars: see [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md) for forecasts issued in real time and scored afterwards, with calibration, sharpness and bias separated; [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md) for the weighted interval score, taught through worked examples; [53-bracher-2021-preregistered-forecasts](53-bracher-2021-preregistered-forecasts.md) for an evaluation protocol registered before the forecasts were scored; [09-cramer-2022-covid-forecast-hub-evaluation](09-cramer-2022-covid-forecast-hub-evaluation.md) for tens of thousands of scored predictions made legible under one pre-specified metric; [51-sherratt-2023-european-forecast-hub](51-sherratt-2023-european-forecast-hub.md) for an ensemble evaluated against its own components across European countries; [52-bosse-2023-transformed-scales](52-bosse-2023-transformed-scales.md) for the argument that the scale forecasts are scored on is itself a choice with consequences; [71-wolffram-2023-nowcast-hub](71-wolffram-2023-nowcast-hub.md) for the hub design applied to nowcasts, pre-registered, with the evaluation target itself put to a sensitivity test.
