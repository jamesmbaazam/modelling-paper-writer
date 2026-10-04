# 59 — Berenguer et al. (2021), *Thorax*
**"Development and validation of a prediction model for 30-day mortality in hospitalised patients with COVID-19: the COVID-19 SEIMC score"**
Berenguer J, Borobia AM, Ryan P, Rodríguez-Baño J, Bellón JM, Jarrín I, et al. *Thorax* 76(9):920–929. doi:10.1136/thoraxjnl-2020-216001.

**Archetype:** *clinical prediction model*, in the clinical-journal register — a regression model developed on one multicentre cohort, **externally validated on an independent cohort**, converted into an integer score, and banded into risk categories a clinician can act on. The corpus's TRIPOD-compliant exemplar.

## Structure
BMJ-family labelled abstract — **Objective / Design / Setting / Participants / Interventions / Main outcome measures / Results / Conclusions** — then a **`Key messages`** box, then `Introduction` → `Methods` (*Source of data* · *Participants* · predictors · statistical analysis) → `Results` → `Discussion`.

**The `Design` field is a single phrase naming the study type**: "Multivariable prognostic prediction model". A reader filtering a search result knows immediately what kind of evidence this is.

**The `Key messages` box is three questions, answered**, and the middle one is unusually candid about the literature the paper is joining:
> "**What is the bottom line?** In a recent systematic review and critical appraisal of prediction models for COVID-19, 50 prognostic models were identified. All models were considered to have a high risk of bias, and none were recommended for clinical use."

**State the appraisal that condemns your own field in the box at the top of the paper**, then spend the paper earning an exception. This is the most disarming possible way to enter a crowded and criticised literature.

## Opening move
> "The clinical spectrum of the novel SARS-CoV-2 associated COVID-19 varies broadly, from asymptomatic disease to pneumonia and life-threatening complications, including acute respiratory distress syndrome, multisystem organ failure and death."

The range of outcomes is the reason a risk score is needed at all, and it is stated first. The known predictors are then surveyed in one sentence, with the dominant one separated from the rest:
> "The main poor prognostic factor identified in different series of COVID-19 is advanced age. Other factors that have been associated with poor outcomes include male gender, several comorbidities, lymphocyte counts, high concentrations of different inflammatory or coagulation markers, serum levels of different cytokines and features derived from imaging studies."

**Name the one predictor everybody already knows, then list the candidates.** It tells a reader what a new score has to beat.

The aim is then stated as a two-part task — develop *and* validate — which is the distinction this literature most often collapses: "Our study's objective was to develop and validate a prediction score to estimate the probability of 30-day mortality in patients with severe COVID-19."

## Methods
◆ **Name the reporting guideline in the first line of Methods and supply the completed checklist**:
> "The predictive model's development followed the recommendations stated in the Transparent Reporting of a multivariable prediction model for Individual Prognosis or Diagnosis (TRIPOD) Initiative (see online supplemental appendix table 1)."

- **Describe both cohorts with their registration identifiers**, which is what separates a prospective registered study from a retrospective data pull: the derivation cohort was "registered in ClinicalTrials.gov (NCT04355871)" and the validation cohort "registered in the European Union Electronic Register of Post-Authorisation Studies (EUPAS34331)."
- **Make the validation genuinely external, and prove the cohorts are disjoint:**
  > "The external validation cohort (VC) included 2126 of the 2226 patients from COVID-19@HULP **after the exclusion of the 100 patients contributing to COVID-19@Spain**."

  Overlap between derivation and validation sets is the commonest way an "external" validation is not external. The paper removes the overlap and reports the count removed.
- **Report where the eligibility criteria differ between cohorts**, rather than implying they match: "No age limit was required in the DC, whereas an age of 18 years or older was an eligibility criterion in the external VC."
- **State the variable-selection rule as a stopping criterion with a number**: "choosing the combination with the highest AUROC. The process stopped when the inclusion of a new variable in the model meant an increase lower than 0.005 unit in the AUROC." A reproducible rule, not a narrative of what was tried.
- **Assess calibration and discrimination separately, each by named method** — the requirement `ml-prediction.md` §7.4 makes:
  > "We assessed the predictive performance of the model by examining measures of calibration and discrimination. We developed a calibration plot with estimates of the calibration slope and intercept. Calibration was also assessed using the Hosmer-Lemeshow test. Discrimination was examined by calculating its AUROC with the 95% CI. We carried out internal validation through a bootstrap with 1000 random samples with replacement to estimate the model optimism and shrinkage factor."

  Calibration plot **plus** slope and intercept **plus** a formal test, and bootstrap optimism correction — this is the full standard, and it is four sentences.
- **Give the arithmetic that turns coefficients into a usable score**: "The logistic regression model's coefficients were converted to a simplified score to facilitate its application in clinical practice. The score was developed, dividing each coefficient by the coefficient with the lowest value and rounding to an integer."
- **Report the full operating-characteristic set, not one threshold**: "The sensitivity, specificity, positive and negative predictive values, and likelihood ratios were calculated for different scores."
- **Name the software with its version and vendor**: "Stata software (V.15.0; Stata Corporation, College Station, Texas, USA)."

## Results
**Describe both cohorts side by side on the characteristics that drive the outcome, and let the differences stand:**
> "Patients' characteristics in the DC and VC were median age 70 and 61 years, male sex 61.0% and 47.9%, median time from onset of symptoms to admission 5 and 8 days, and 30-day mortality 26.6% and 15.5%, respectively."

The validation cohort is nine years younger, less male, presents three days later and has 11 percentage points lower mortality. **A validation cohort that differs from the derivation cohort is a feature, not a flaw** — it is what makes the validation informative — and reporting the differences in one sentence lets the reader judge the transfer.

**Report the event counts, not only the cohort sizes**: "The developing cohort included 4035 patients, of which 1074 (26.6%) died"; "The external VC included 2202 patients, 341 (15.5%) died."

**State that the sample exceeded the required size**, with the calculation deposited: "The cohort size was more than twice the required for developing a clinical prognostic model (online supplemental appendix figure 1)." Events-per-variable is the standard risk-of-bias criterion in this literature (`ml-prediction.md` §7.8); this paper pre-empts it.

**Report discrimination with intervals in both cohorts, and for both the model and the simplified score:**
> "Calibration and discrimination were satisfactory with an area under the receiver operating characteristic curve with a 95% CI for prediction of 30-day mortality of 0.822 (0.806–0.837) in the DC and 0.845 (0.819–0.870) in the VC."

and separately "when we applied the same approach to the simplified point score, the AUROC (95% CI) was 0.806 (0.791 to 0.820) in the DC and 0.849 (0.831 to 0.866) in the external VC." **Report the performance of the thing clinicians will actually use** — the rounded integer score — not only of the underlying regression.

**Deliver the output as risk bands with their observed probability ranges:**
> "A simplified score system ranging from 0 to 30 to predict 30-day mortality was also developed. The risk was considered to be low with 0–2 points (0%–2.1%), moderate with 3–5 (4.7%–6.3%), high with 6–8 (10.6%–19.5%) and very high with 9–30 (27.7%–100%)."

Four bands, each with the mortality range it corresponds to. **A prediction model becomes clinically usable when it is a small number of bands with probabilities attached**, not a continuous risk score.

## Literature
Numbered BMJ-style citations. Prior prognostic factors are surveyed compactly in the Introduction, and the critical appraisal of the field is cited in the `Key messages` box rather than buried. Related models are characterised by their shared weakness — "The model performance was good across all studies, although the same methodological limitations found in the meta-analysis also applied."

## Voice
Impersonal and clinical in the abstract, first-person plural in the Discussion. Claims are bounded to the population studied and the outcome measured; the conclusion is a capability statement rather than a recommendation: "provides a useful tool to predict 30-day mortality probability with a high degree of accuracy among hospitalised patients with COVID-19."

## Discussion and limitations
Opens by restating the design, the predictors, and the two properties that matter clinically — performance in both cohorts and the risk stratification.

**The most instructive passage explains a deliberate omission, with the evidence that argued for inclusion:**
> "Of note, our model does not take into account comorbidities, which have been associated with worse COVID-19 prognosis in descriptive studies and included in most prognostic prediction models reported to date. In our study, underlying diseases such as hypertension, obesity, liver cirrhosis, chronic neurological disorder, active neoplasia and dementia were independently associated with an increased risk of 30-day mortality. **However, none of these conditions improved the model's discrimination capacity and, following the principle of parsimony, were discarded.**"

**Explain why you left out the variables your readers expect**: they were significant, they did not improve discrimination, and parsimony decided it. A reader who would otherwise object now has the answer, with the evidence.

**Make a headline finding concrete with a worked patient**: "our score would classify a 65-year-old male pat[ient]…" — turning a coefficient into the kind of case a clinician sees.

The claim that age dominates is stated strongly but bounded by the authors' knowledge: "our study highlights the extraordinary impact of age on COVID-19 mortality, which is, to the best of our knowledge, unparalleled in infectious diseases."

## Data, code and funding
Both cohorts carry trial-registry identifiers; the TRIPOD checklist, the sample-size calculation, the calibration results and the alternative-model comparison are all in the supplementary appendix. The score is fully specified in the paper — coefficients, integer weights, bands — so it can be implemented without the authors' code, which for a clinical score is the relevant form of reproducibility.

## Distinctive moves to borrow
1. **Quote the critical appraisal that condemns your field in a box at the top**, then earn the exception.
2. ◆ **Name TRIPOD in the first line of Methods and supply the completed checklist.**
3. **Register both cohorts and give the identifiers.**
4. **Prove the validation cohort is disjoint** from the derivation cohort, and report how many patients you removed to make it so.
5. **Report where eligibility criteria differ between cohorts.**
6. **State the variable-selection stopping rule as a number** (ΔAUROC < 0.005).
7. **Assess calibration by plot, slope, intercept and a formal test** — not by assertion — alongside discrimination with intervals.
8. **Bootstrap for optimism and shrinkage**, and say so.
9. **Report cohort differences in one sentence** and treat them as what makes the validation informative.
10. **Give event counts, and state that the sample exceeded the required size.**
11. **Report performance of the simplified score, not only the underlying model.**
12. **Deliver risk bands with observed probability ranges**, few enough to remember.
13. **Explain the variables you deliberately omitted**, including the evidence that favoured them.
14. **Specify the score completely in the paper**, so it can be implemented without your code.

## Related files
For the machine-learning counterpart with a different split design and thinner performance reporting see [58-yadaw-2020-covid-mortality-prediction](58-yadaw-2020-covid-mortality-prediction.md); for a clinical prediction model reporting auPRC and two operating points see [37-zoabi-2021-covid-symptom-prediction](37-zoabi-2021-covid-symptom-prediction.md); for the appraisal that this paper's `Key messages` box quotes see [35-wynants-2020-covid-prediction-models-review](35-wynants-2020-covid-prediction-models-review.md); for the rules this paper satisfies see `references/ml-prediction.md`.
