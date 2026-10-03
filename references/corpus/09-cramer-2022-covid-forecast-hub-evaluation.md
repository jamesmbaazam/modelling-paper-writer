# 09 — Cramer et al. (2022), *PNAS*
**"Evaluation of individual and ensemble probabilistic forecasts of COVID-19 mortality in the United States"**
Cramer EY, Ray EL, Lopez VK, Bracher J, Brennen A, et al. (US COVID-19 Forecast Hub). *PNAS* 119(15):e2113561119. PMC9169655.

**Archetype:** the *large-scale forecast evaluation* paper — hundreds of authors, tens of thousands of scored predictions, one pre-specified metric. The writing problem it solves is making a vast, heterogeneous comparison legible.

## Structure
`Significance` → `Abstract` → Introduction (unheaded, ~7 ¶) → `Results` with **claim-shaped subheadings** → `Discussion` → `Methods` (PNAS places these last) → SI Appendix + Datasets.

Results subheadings:
*Summary of Models · Overall Model Accuracy · Model Accuracy Rankings Are Highly Variable · Observations on Accuracy in Specific Weeks · Model Performance in Specific Pandemic Waves · Individual Model Forecast Performance Varies Substantially by Location · Forecast Performance Degrades with Increasing Horizons*

Methods subheadings — each one an operational decision that a critic could challenge:
*Surveillance Data · Forecast Format · Forecast Model Eligibility and Evaluation Period · Aggregated Forecast Evaluation of Pandemic Phases · Disaggregated Forecast Evaluation by Pandemic Wave · Forecast Locations · Forecast Models · Forecast Submission Timing · Evaluation Methodology · Forecast Comparisons*

The Results are organised by **the dimension of stratification** — overall, by week, by wave, by location, by horizon — which is exactly how a reader wants to interrogate a forecast evaluation.

## Opening move
Significance:
> "This paper compares the probabilistic accuracy of short-term forecasts of reported deaths due to COVID-19 during the first year and a half of the pandemic in the United States. Results show high variation in accuracy between and within stand-alone models and more consistent accuracy from an ensemble model that combined forecasts from all eligible models."

Abstract:
> "Short-term probabilistic forecasts of the trajectory of the COVID-19 pandemic in the United States have served as a visible and important communication channel between the scientific modeling community and both the general public and decision-makers. Forecasting models provide specific, quantitative, and evaluable predictions that inform short-term decisions such as healthcare staffing needs, school closures, and allocation of medical supplies."

Pattern: **what forecasts are for, in terms of specific decisions → the scale of the enterprise → the finding.** The abstract names the actual decisions ("healthcare staffing needs, school closures, and allocation of medical supplies") rather than saying "inform policy".

The Introduction's justification chain is worth memorising: surveillance data "only present a partial, time-lagged picture of transmission and do not show if and when changes may occur in the future" → forecasts fill that gap → "Providing prediction uncertainty is critical for such decisions, as it allows stakeholders to assess the most likely outcomes and plausible worst-case scenarios."

## Methods
- **One primary metric, named, cited and interpreted for the reader**: "To evaluate probabilistic accuracy, the primary metric used was the weighted interval score (WIS), a nonnegative metric, which measures how consistent a collection of prediction intervals is with an observed value. For WIS, a lower value represents smaller error."
- Scores are made interpretable by **relativising to a naïve baseline**: "The COVIDhub-ensemble achieved a relative WIS of 0.61, which can be interpreted as achieving, on average, 39% less probabilistic error than the baseline forecast in the evaluation period, adjusting for the difficulty of the specific predictions made." The gloss after "which can be interpreted as" converts a metric into a sentence a decision-maker can use.
- Calibration is reported **separately from accuracy**, using empirical coverage of prediction intervals — accuracy and calibration are different virtues and are never conflated.
- Inclusion criteria are stated as criteria, and their influence is tested: "Values of relative WIS and rankings of models were robust to changing thresholds for submission inclusion criteria and to the inclusion or exclusion of individual outlying or revised observations (SI Appendix, Tables S3 and S4)."
- Scale is quantified precisely: "A total of 28 models met inclusion criteria, yielding 1,791 submission files with 556,050 specific predictions for unique combinations of forecast dates, targets (horizons forecasted), and locations."
- Reporting follows a published guideline: "We followed the EPIFORGE 2020 guidelines for reporting results from epidemiological forecasting studies."

## Results
Counts of models, relative scores, coverage rates and ratios — never a raw score without a comparator.
> "In total, 18 models had a relative WIS of less than 1, indicating lower probabilistic forecast error than the baseline model, and 10 models (including the baseline) had a relative WIS of 1 or greater."
> "Across 1- through 4-wk-ahead horizons, 79 wk, and 50 states, only the ensemble model achieved near-nominal coverage rates for both the 50% and 95% PIs."
> "The COVIDhub-ensemble was the only model that ranked in the top half of all models (standardized rank > 0.5) for more than 75% of the observations it forecasted, although it made the single best forecast less frequently than any other model."
> "Models in general systematically underpredicted the mortality curve as trends were rising and overpredicted as trends were falling."
> "For the two teams who made 20-wk-ahead forecasts for all 50 states, the average WIS was 2.9 to 4 times higher at a 20-wk horizon than it was at a 1-wk horizon."

Two habits: **the concessive clause inside the headline claim** ("although it made the single best forecast less frequently than any other model") and **mechanistic explanation of a pattern in the score decomposition** ("The biggest increases in WIS were from increased penalties for underprediction, suggesting that the model forecasts did not accurately capture the possibility of increases in incidence at long horizons").

Negative findings about the authors' own ensemble are reported in the Results, not softened: "In some of the selected waves (e.g., North Dakota and Florida), the ensemble forecast showed inappropriate levels of uncertainty, with the 95% PIs covering the eventual observations less than 80% of the time."

## Literature
Numbered; concentrated in the Introduction, where ensembles' prior track record is established across pathogens: "Ensemble approaches have previously demonstrated superior performance compared with single models in forecasting influenza, Ebola, and dengue fever outbreaks. Preliminary research suggested that COVID-19 ensemble forecasts were also more accurate and precise than individual models in the early phases of the pandemic." The paper's contribution is then scale and duration rather than novelty — "This supports prior results and confirms that…".

## Voice
Past tense for the evaluation, present for standing conclusions. First-person plural for analytic choices: "we sought to evaluate", "We ranked models", "we implemented specific inclusion criteria", "we note that…". Hedging is used to mark inference beyond the data: "suggesting that their approaches … were robust to anomalies", "These four examples appeared to be representative of trends observed when looking across a larger number of waves."

## Discussion and limitations
Opens by naming the tension the paper exposes rather than by restating results:
> "This work illustrates the tension between the desire for long-term forecasts, which would be helpful for public-health practitioners, and the decline in forecast accuracy at longer horizons shown by all forecasting methods."

Then a **bulleted "We summarize the key findings of the work as follows"** list — five bullets, each a finding plus its practical implication. A bulleted findings list is unusual in PNAS and works because the results are so multidimensional.

A distinctive methodological caution is raised against the paper's own post hoc wave analysis:
> "A post hoc evaluation that focuses exclusively on these 'change-points' may reward models that may regularly predict extreme changes even when they do not occur at other times. Adapting proper scoring rules to weigh good performance in both kinds of situations is difficult."

## Discussion and limitations
> "Rigorous evaluation of forecast accuracy faces many limitations in practice. The large variation and correlation in forecast errors across targets, submission weeks, and locations makes it difficult to create rigorous comparisons of models."
> "Ground-truth data are not static. They can be later revised as more data become available."
> "because this evaluation focuses on incident death forecasts, it cannot speak to model performance for incident cases or hospitalizations."
> "the Hub did not collect data on experimental modeling studies for which certain features can be included or left out to explicitly test what features of a model increase predictive accuracy. An observational study could be conducted with forecasts collected by the Hub, but any such analysis would be confounded by other factors…"

The last one is the strongest form of limitation writing: **explain why the obvious follow-up analysis would not be valid**, so the reader does not mistake correlation in the data for an experiment.

## Data, code and funding
> "The forecasts from models used in this paper are available from the COVID-19 Forecast Hub GitHub repository … and the Zoltar forecast archive … These are both publicly accessible. The code used to generate all figures and tables in the manuscript is available in a public repository … All analyses were conducted using the R language for statistical computing (version 4.0.2)."

## Distinctive moves to borrow
1. **Relativise every score to a naïve baseline and gloss it in plain English.**
2. Report accuracy and calibration as separate results.
3. Stratify the Results by each dimension a reader would ask about, one subheading each.
4. Report where your own preferred model failed, in the Results.
5. Pre-empt misuse: explain why the tempting follow-up analysis would be confounded.
