# 58 — Yadaw et al. (2020), *The Lancet Digital Health*
**"Clinical features of COVID-19 mortality: development and validation of a clinical prediction model"**
Yadaw AS, Li Y-C, Bose S, Iyengar R, Bunyavanich S, Pandey G. *Lancet Digit Health* 2(10):e516–e525. doi:10.1016/S2589-7500(20)30217-X.

**Archetype:** *clinical prediction model* — develop a patient-level classifier on routine data, validate it on held-out patients, and argue it is deployable. The contribution is a **parsimonious** model: three features, chosen because they are the ones a clinician already has.

## Structure
Lancet-family structured abstract (**Background / Methods / Findings / Interpretation / Funding**) → **`Research in context`** panel → `Introduction` → `Methods` → `Results` → `Discussion`. The *Lancet Digital Health* format is the clinical Lancet format with the same mandatory panels, and the paper uses them exactly as `evidence.md` §1.2 describes.

**Two held-out sets, named by what makes them different**, is the structural decision that defines the paper: `test dataset 1 (retrospective)` is a random split of the same period, `test dataset 2 (prospective)` is the next day's patients. The naming carries the design.

## Opening move
> "The COVID-19 pandemic has affected millions of individuals and caused hundreds of thousands of deaths worldwide. Predicting mortality among patients with COVID-19 who present with a spectrum of complications is very difficult, hindering the prognostication and management of the disease."

The Introduction then explains *why* prediction is hard here specifically, rather than asserting it: "Clinical experience thus far has shown substantial heterogeneity in the trajectory of SARS-CoV-2 infection, spanning from patients who are asymptomatic to those with mild, moderate, and severe disease forms with low survival rates."

**The `Research in context` panel states the gap as two concrete deficiencies in prior work**, with the search terms given:
> "We searched PubMed and its associated LitCovid repository for publications in English from database inception until May 10, 2020, using the terms 'coronavirus', 'COVID-19', 'death', 'mortality', and 'prediction'. The studies we identified generally focused on a small set of clinical features, risk factors, or small cohorts… These studies also used relatively simple analytical methods, which might not adequately model the inherent difficulties of the data (eg, collinear or irrelevant features, non-linear relationships between features and mortality, noise, and missing data)."

**Name the properties of the data that defeat simple methods** — collinearity, non-linearity, noise, missingness — rather than claiming machine learning is better in general. That list is the justification for the method choice, and it is checkable.

## Methods
- **State the data source, the population and the window precisely**: "patient-level data captured in the Mount Sinai Data Warehouse database for individuals with a confirmed diagnosis of COVID-19 who had a health system encounter between March 9 and April 6, 2020."
- **Split along two different axes and say which is which:**
  > "For initial analyses, we used patient data from March 9 to April 5, and randomly assigned (80:20) the patients to the development dataset or test dataset 1 (retrospective). Patient data for those with encounters on April 6, 2020, were used in test dataset 2 (prospective)."

  The random split tests generalisation to new patients from the same period; the date split tests generalisation forward in time, which is the axis the model will actually be used over. **`ml-prediction.md` §7.3 asks for the split to run along the axis of intended extrapolation — this paper does both and labels them.**
- **Report the metric chosen and where it is computed**: "We assessed the resultant models in terms of the area under the receiver operating characteristic curve (AUC) score in the test datasets."
- **Describe feature selection as a systematic procedure**, not a hand-picked list: "Using the development dataset (n=3841) and a systematic machine learning framework, we developed a COVID-19 mortality prediction model."

## Results
**Report the headline with the sample sizes of both test sets, not just the metric**:
> "we developed a COVID-19 mortality prediction model that showed high accuracy (AUC=0·91) when applied to test datasets of retrospective (n=961) and prospective (n=249) patients."

**Name the features, and characterise them by their availability rather than their coefficients:**
> "This model was based on three clinical features: patient's age, minimum oxygen saturation over the course of their medical encounter, and type of patient encounter (inpatient vs outpatient and telehealth visits)."

The third feature is worth noticing: *where the patient was seen* is a proxy for triage decisions already made by clinicians. The paper reports it plainly rather than disguising it, and this is the kind of feature `ml-prediction.md` §7.5 would ask you to interrogate — a reader should ask whether it leaks the outcome.

**Argue for parsimony as a deployment property**, which is the paper's real claim:
> "Our work shows that input of three highly accessible clinical parameters for a patient—age, minimum oxygen saturation, and type of patient encounter—into an automatable XGBoost algorithm has the potential to accurately classify patients as likely to live or die."

"Highly accessible" and "automatable" are doing the work. **A three-feature model that uses data already in the chart can be deployed; a fifty-feature model usually cannot.**

**State the deployment vision concretely, as a thing a clinician would recognise:**
> "we envision that incorporation of our automatable mortality prediction model into the clinical care workflow of a patient with COVID-19 could yield an additional vital sign that is assessed regularly during a patient's encounter."

"An additional vital sign" tells a clinical reader exactly what the model would be, in their own vocabulary.

**Gate the deployment claim on validation that has not happened yet** — stated three times, including in the abstract's Interpretation: "External validation of this prediction model in other populations is needed"; "We recognise that external validation of our prediction model in other populations is the next step in model development"; and conditionally, "**Should such validation show that our model performs well in multiple populations**, we envision…".

## Literature
Numbered Lancet-style citations, sparse, concentrated in the Introduction and the `Research in context` panel. The field is characterised by its methodological limitations rather than reviewed paper by paper — appropriate when the contribution is a methodological improvement on a crowded literature.

## Voice
First-person plural, past for the work and conditional for the deployment claims: "might have utility", "has the potential to", "could yield". The gap between what was shown (AUC on two internal test sets) and what is claimed (clinical utility) is marked by a modal in every sentence that crosses it.

## Discussion and limitations
Opens by restating the design and the result, then the clinical motivation — "factors that contribute most to mortality are not always readily apparent, rendering care and management of these patients difficult in settings of finite health-care resources" — then the deployment vision, then limitations.

The limitations are specific and several name the direction or the fix:
- **The feature set is bounded by what routine care collects**: "the clinical features available to us were limited to those routinely collected during hospital encounters… development of even better prediction models should be possible using a richer set of features." The named richer features — "demographics, comorbidities, laboratory test measurements, vital signs, chest imaging, clinical notes, and omic data" — make the limitation actionable.
- **A small test set, with the event count given**, which is the number that actually matters:
  > "Specifically, test dataset 2 included only 249 patients, with only 25 patients who died."

  **Report events, not just sample size.** Twenty-five deaths is the real precision constraint on the prospective AUC, and `ml-prediction.md` §7.8 flags small event counts as a risk-of-bias criterion.
- **A temporal scope fence, with the mechanism spelled out**: "our datasets only represent a snapshot in time, and mortality outcomes might change in different timeframes… Changing these date ranges could have changed their respective mortality rates. Similar changes could also occur for the values of time-varying features like mini[mum oxygen saturation]."

  A model fitted during one phase of a pandemic encodes that phase's case mix and treatment practice; the paper says so.

**What a reader should notice is missing**, measured against `ml-prediction.md` §7.4 and §7.8: there is no **calibration** assessment, no **auPRC** despite substantial class imbalance, no confidence interval on the AUC, and no named operating point with its sensitivity and specificity. The parsimony and the dual-split design are exemplary; the performance reporting is thinner than the corpus's clinical-prediction standard, and a writer should take the former and supply the latter.

## Distinctive moves to borrow
1. **Split along two axes and name the splits by what they test** — a random split for new patients, a date split for the next day's patients.
2. **State the gap as named properties of the data that defeat simpler methods**, not as a general claim for machine learning.
3. **Give the search terms and date in the evidence-before-this-study panel.**
4. **Characterise the selected features by their availability**, not their coefficients, when the claim is deployability.
5. **Argue parsimony as a deployment property**: three features already in the chart.
6. **Describe the deployed model in the user's vocabulary** — "an additional vital sign".
7. **Gate the deployment claim on external validation**, and repeat the gate in the abstract.
8. **Report the event count in the smallest test set**, not only the sample size.
9. **Fence the temporal scope** and name the time-varying features that would shift.
10. **Name the richer data that would improve the model**, so the limitation points somewhere.

## What to avoid from this paper
- **Discrimination reported without calibration.** `ml-prediction.md` §7.4 treats these as separate virtues; `35-wynants-2020-covid-prediction-models-review` names missing calibration as the most common failing in exactly this literature.
- **No interval on the AUC** and **no auPRC** under class imbalance — compare [37-zoabi-2021-covid-symptom-prediction](37-zoabi-2021-covid-symptom-prediction.md), which gives both.
- **No named operating point.** A model proposed as a vital sign needs a threshold with its sensitivity and specificity.
- **An unexamined feature that may encode clinical judgement.** Encounter type reflects triage decisions; whether that is legitimate signal or outcome leakage is worth a paragraph it does not get.

## Related files
For the clinical-prediction exemplar that reports calibration, auPRC and two operating points see [37-zoabi-2021-covid-symptom-prediction](37-zoabi-2021-covid-symptom-prediction.md); for the appraisal criteria this paper would be judged against see [35-wynants-2020-covid-prediction-models-review](35-wynants-2020-covid-prediction-models-review.md) and [36-roberts-2021-ml-covid-imaging-pitfalls](36-roberts-2021-ml-covid-imaging-pitfalls.md); for the rules themselves see `references/ml-prediction.md`; for a clinical-journal prediction model with external validation see [59-berenguer-2021-covid-mortality-score](59-berenguer-2021-covid-mortality-score.md).
