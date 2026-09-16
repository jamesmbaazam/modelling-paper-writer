# 35 — Wynants et al. (2020), *BMJ*
**"Prediction models for diagnosis and prognosis of covid-19: systematic review and critical appraisal"**
*BMJ* 369:m1328. doi:10.1136/bmj.m1328. PMC7222643.
**Citations:** ~3,300 (OpenAlex, Sept 2026) — the most cited COVID-19 machine-learning paper in this corpus, and it is a paper saying the models don't work.

**Archetype:** the *living systematic review and critical appraisal* — applies a formal risk-of-bias instrument to an entire rapidly produced literature and returns a verdict. The most consequential thing a modeller can read before writing a prediction paper, because it lists exactly what appraisers will mark you down for.

## Structure
Structured abstract: **Objective / Design / Data sources / Study selection / Data extraction / Results / Conclusion / Systematic review registration / Readers' note.**
Body: `Introduction` → `Methods` (incl. *Patient and public involvement*) → `Results` (*Primary datasets · Models to predict risk of developing covid-19 or hospital admission · Diagnostic models to detect covid-19 · Prognostic models for patients with diagnosis of covid-19 · Risk of bias*) → `Discussion` (*Challenges and opportunities · Study limitations · Implications for practice · Conclusion*).
Plus **Box 1** (availability of models in a usable format), **Box 2** (common causes of risk of bias), and the BMJ "What is already known on this topic / What this study adds" panel.

## Opening move
> "To review and critically appraise published and preprint reports of prediction models for diagnosing coronavirus disease 2019 (covid-19) in patients with suspected infection, for prognosis of patients with covid-19, and for detecting people in the general population at increased risk of becoming infected with covid-19 or being admitted to hospital with the disease."

No background sentence at all — the structured abstract begins with the objective and the three use cases. The motivation appears in the Introduction instead, and locates the problem in the incentives:
> "Models ranging from rule based scoring systems to advanced machine learning models (deep learning) have been proposed and published in response to a call to share relevant covid-19 research findings rapidly and openly… Many of these prediction models are published in open access repositories, ahead of peer review."

## Appraisal conventions
Two formal instruments, named and cited, and applied to every study:
> "Reviewers used a standardised data extraction form based on the CHARMS (critical appraisal and data extraction for systematic reviews of prediction modelling studies) checklist and PROBAST (prediction model risk of bias assessment tool) for assessing the reported prediction models."

Risk of bias is reported **by PROBAST domain** — participants, predictors, outcome, analysis — rather than as a single score, so authors can see which part of their own pipeline is weakest.

## The list of failings — read this as a checklist of what not to do
> "Many studies had small sample sizes…, which led to an increased risk of overfitting, particularly if complex modelling strategies were used."
> "The test used to determine the outcome varied between participants…, or one of the predictors (e.g., fever) was part of the outcome definition."
> "Study participants were often excluded because they did not develop the outcome at the end of the study period but were still in follow-up (that is, they were in hospital but had not recovered or died), yielding a highly selected study sample."
> "Only five studies assessed calibration…, but the method to check calibration was probably suboptimal in two studies."
> "However, in six of these models, the datasets used for the external validation were not representative of the target population… Consequently, predictive performance could differ if the models are applied in the targeted population."
> "Careful description of model specification and subsequent estimation were lacking, challenging the transparency and reproducibility of the models. Every study used a different deep learning architecture, some were established and others specifically designed, without benchmarking the used architecture against others."
> "Only three studies accounted for censoring by using Cox regression…, or competing risk models."

Six recurring, nameable sins: **outcome leakage into predictors; excluding still-in-follow-up patients; case-control sampling misrepresented as a cohort; calibration ignored; unrepresentative external validation; unbenchmarked bespoke architectures.**

## Results storytelling
> "4909 titles were screened, and 51 studies describing 66 prediction models were included."
> "C index estimates ranged from 0.73 to 0.81 in prediction models for the general population, from 0.65 to more than 0.99 in diagnostic models, and from 0.85 to 0.99 in prognostic models."
> "Among the diagnostic model studies, only five reported on prevalence of covid-19 and used a cross sectional or cohort design; the prevalence varied between 17% and 79%… Because 31 diagnostic studies used either case-control sampling or an unclear method of data collection, the prevalence in these diagnostic studies might not have been representative of their target population."
> "All models were rated at high or unclear risk of bias, mostly because of non-representative selection of control patients, exclusion of patients who had not experienced the event of interest by the end of the study, high risk of model overfitting, and vague reporting."

Note the treatment of headline performance: **C-index ranges are reported and then immediately undercut** by the design facts that make them uninterpretable. A near-perfect AUC is presented as a symptom, not an achievement.

Code availability is itself converted into an appraisal metric: "Seven studies made their source code available on GitHub… Thirty one studies did not include any usable equation, format, or reference for use or validation of their prediction model."

## Voice
Predominantly passive for verdicts ("All models were rated at high or unclear risk of bias"), first-person plural for reviewer actions ("We searched…", "We identified…"). Criticism is blunt but never intemperate, and its force comes from repetition rather than escalation:
> "Hence, we do not recommend any of these reported prediction models to be used in current practice."
> "Therefore, we have cause for concern that the predictions of these models are unreliable when used in other people."
> "A high risk of bias implies that the performance of these models in new samples will probably be worse than that reported by the researchers."

Urgency is acknowledged and then explicitly declined as an excuse: "Although we recognise that all studies were done under severe time constraints caused by urgency, we recommend…".

## Limitations and recommendations
> "With new publications on covid-19 related prediction models rapidly entering the medical literature, this systematic review cannot be viewed as an up-to-date list of all currently available covid-19 related prediction models. Also, 45 of the studies we reviewed were only available as preprints."

Recommendations, verbatim and directly actionable for anyone writing an ML prediction paper:
> "When creating a new prediction model, we recommend building on previous literature and expert opinion to select predictors, rather than selecting predictors in a purely data driven way; this is especially important for datasets with limited sample size."
> "Based on the predictors included in multiple models identified by our review, we encourage researchers to consider incorporating several candidate predictors: for diagnostic models, these include age, body temperature or fever, signs and symptoms…, sex, blood pressure, creatinine…"
> "Sharing data and expertise for development, validation, and updating of covid-19 related prediction models is urgently needed."
Plus adherence to TRIPOD, with translations linked.

## Living-review mechanism
> "This article is a living systematic review that will be updated to reflect emerging evidence. Updates may occur for up to two years from the date of original publication."
Protocol and registration on OSF; superseded versions retained as data supplements. Compare the versioning approach of [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md).

## Distinctive moves to borrow
1. **Use a named, published appraisal instrument** and report by domain, so criticism is auditable rather than personal.
2. **Report headline performance and then explain why it cannot be believed**, in the same paragraph.
3. **Convert criticism into a positive resource** — the list of candidate predictors future modellers should consider.
4. Deliver a non-recommendation once, plainly, and repeat it without amplifying the language.
5. Acknowledge the pressure people were under, then decline to lower the standard.
6. Treat code and equation availability as a measurable quality attribute.

## Related files
The imaging-specific counterpart is [36-roberts-2021-ml-covid-imaging-pitfalls](36-roberts-2021-ml-covid-imaging-pitfalls.md); the single-model critique is [31-lazer-2014-parable-of-google-flu](31-lazer-2014-parable-of-google-flu.md); for a paper that satisfies most of these criteria, see [37-zoabi-2021-covid-symptom-prediction](37-zoabi-2021-covid-symptom-prediction.md).
