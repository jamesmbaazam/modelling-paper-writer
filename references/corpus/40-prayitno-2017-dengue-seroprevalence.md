# 40 — Prayitno et al. (2017), *PLoS Neglected Tropical Diseases*
**"Dengue seroprevalence and force of primary infection in a representative population of urban dwelling Indonesian children"**
Prayitno A, Taurel A-F, Nealon J, Satari HI, Karyanti MR, Sekartini R, et al. *PLoS Negl Trop Dis* 11(6):e0005621. doi:10.1371/journal.pntd.0005621.

**Archetype:** the *serological inference* paper — convert an age-stratified cross-sectional serosurvey into a transmission quantity (the force of infection) using a catalytic model, and use it to argue that routine surveillance understates burden. The design is a survey; the contribution is the inference drawn from it.

## Structure
PLoS structured abstract (**Background / Methodology–Principal Findings / Conclusions–Significance**) → **`Author summary`** written for the practitioner → `Introduction` → `Methods` (*Ethic statement* · *Study area* · *Sampling design* · *Sample size* · *Enrolment* · laboratory · statistical analysis) → `Results` → `Discussion` → `Supporting information` → `Acknowledgments`.

**The Methods subheadings are the survey's design decisions in the order a critic would audit them** — where, how sampled, how many, how recruited, how assayed, how analysed. For any study whose validity rests on representativeness, this ordering *is* the argument.

◆ **The reporting guideline is named in the first line of Methods and the completed checklist is supplied**: "The present study is reported according to STrengthening the Reporting of OBservational studies in Epidemiology (STROBE) recommendations (supporting information file)", with `S1 Checklist. STROBE Checklist.` in the supporting information. This is the convention `SKILL.md` §6 asks for, done exactly.

## Opening move
> "Indonesia reports the second highest dengue disease burden in the world; these data are from passive surveillance reports and are likely to be significant underestimates. Age-stratified seroprevalence data are relatively unbiased indicators of past exposure and allow understanding of transmission dynamics."

Two sentences carrying the whole rationale: **the existing data source, its specific defect, and the alternative data source that does not share the defect.** The second sentence is the methodological justification for the entire study, and it is stated as a property of the data type, not of this study.

The `Author summary` makes the policy stake explicit in a way the abstract does not: "Understanding the intensity of dengue virus transmission and associated risk factors nationwide is necessary to guide and prioritize appropriate prevention and control measures against dengue disease, especially considering the availability of the first dengue vaccine and recent recommendations for its use in areas of high endemicity, as measured by seroprevalence and other indicators."

**Write the Author Summary for the decision, not as a simplified abstract.** Seroprevalence was at that moment the criterion for dengue vaccine eligibility, so the summary says so; the abstract does not need to.

## Methods
- **Describe the setting with the administrative units the sampling will use**, including the operational definition of the category being sampled: "Villages are considered either as rural (*desa*) or urban (*kelurahan*) based on population density, percentage of agricultural household and number of urban facilities such as schools and hospitals." A reader can now judge what "urban" means in the headline.
- **Name the sampling design by its published provenance**: "A population-based cross-sectional study design was adapted from the World Health Organization (WHO) Expanded Program on Immunization (EPI) cluster survey method."
- **Give the sample size calculation with every input**, including the ones that are judgement: the calculation used "95% confidence, a margin error of 5% and accounting for clustering with a design effect of 2", with expected seroprevalence per age band "based on Indonesian expert opinion and published regional data", and "To account for incomplete data, a 10% contingency was applied." The resulting allocation is then given per cluster and per age group, so the design is reproducible.
- **State the eligibility rule and the residency requirement**, which is what makes a prevalence attributable to a place: participants were enrolled "if they were healthy, 1–18 years of age on inclusion day, and had lived in the location for at least 1 year."
- **Record the refusals as part of the sampling procedure**: "If the parents refused the participation of the selected child, the household was not included. This process was continued until the desired sample size was achieved in each of the 30 clusters."
- **Name the inferential model and the assumption that makes it identifiable, in the same clause**: "Using a catalytic model and considering a constant force of infection we estimated 13.1% of children experience a primary infection per year." Constant force of infection is the assumption the whole estimate rests on, and it is stated in the abstract rather than hidden in a supplement.
- **Report two estimators of the same underlying quantity.** The median age of seroconversion is estimated "through a linear model" and the annual infection rate through the catalytic model; the two are reported side by side and compared with the literature separately.

## Results
**Report the headline prevalence with its interval and then immediately disaggregate by the variable the model uses** — age — so the reader sees the gradient the catalytic model is fitted to:
> "an adjusted national seroprevalence in this urban population of 69.4% [95% CI: 64.4–74.3] (33.8% [95% CI: 26.4–41.2] in the 1–4-year-olds, 65.4% [95% CI: 69.1–71.7] in the 5–9-year-olds, 83.1% [95% CI: 77.1–89.0] in the 10–14-year-olds, and 89.0% [95% CI: 83.9–94.1] in the 15–18-year–olds)"

Note "adjusted": the weighting implied by the cluster design is signalled in the word attached to the estimate.

**Convert the modelled parameter into the sentence a policymaker will quote**: "more than 80% of children aged 10 years or over have experienced dengue infection at least once." The force of infection is the inference; the cumulative exposure by age 10 is the communication.

**Report associations with the effect sizes and the reference category made explicit**: "the subject's age group (1–4 vs 5–9 OR = 4.25; 1–4 vs. 10–14 OR = 12.60; and 1–4 vs 15–18 OR = 21.87; p<0.0001) and the number of cases diagnosed in the household since the subject was born (p = 0.0004) remained associated with dengue serological status." "Remained associated" signals these survived the multivariate model.

**Compare with prior estimates, matched on place, year and age band, and offer competing explanations for the difference without choosing**:
> "A seroprevalence study conducted in 1995 in healthy children in Yogyakarta, Indonesia… reported the presence of neutralizing antibodies in 56.2% of 4–9-year-old children… These are slightly lower than the rates observed in our study and may be reflective of increasing dengue endemicity in the intervening decades, or geographic variability."

The comparison carries assay, place, year and age range — the four things that make two seroprevalence numbers comparable or not. Further comparisons are given the same treatment: "Sri Lanka (Colombo, 2008, 52.0% in those <12 years of age, and median age of seroconversion of 4.7 years)", "Vietnam (Binh Thuan, 2003, 65.7% in 7–13 year olds)".

## Literature
Numbered PLoS citations, moderate density, concentrated in the Introduction and in the Discussion's comparison paragraph. Prior studies are used as calibration points for the new estimate rather than reviewed, and each is cited with the details needed to judge comparability.

## Voice
First-person plural, past tense, with hedges attached to specific inferences: "may be reflective of increasing dengue endemicity", "it is likely that nearby peri-urban populations may have experienced similar high levels of exposure", "these data are strongly suggestive that". The strongest claim in the paper is deliberately framed as suggestion rather than estimate, because the design does not support an estimate — see the scope fence below.

## Discussion and limitations
Opens by naming the design strengths that the claim depends on, rather than restating the result:
> "This is the first dengue antibody seroprevalence study conducted in a representative population of urban dwelling Indonesian children. The findings benefit from a cluster sampling design with probability proportional to size method, and sensitive and specific dengue diagnostic assays performed in the same laboratory."

"Performed in the same laboratory" is the kind of detail that matters enormously in serology and is usually omitted.

Limitations are specific and each is given a direction or a magnitude:
- **An excluded population, with the likely direction of the error**: "while we excluded rural areas from this study for operational reasons, it is likely that nearby peri-urban populations may have experienced similar high levels of exposure."
- **An assay limitation, with the reason it is judged small**: "cross-reaction between flaviviruses has been documented and the risk of false positives cannot be excluded. We consider this risk as low, because reports of other viruses such as Japanese encephalitis and Zika, in Indonesia, are rare." The judgement is argued from local epidemiology, not asserted.
- **A scope fence followed by the inference the design *does* support** — the best passage in the paper:
  > "This study was not designed to make national-level infection or disease burden estimates but the observation that 13.1% of children suffer a primary infection per year translates into many millions of infections per year… While a modelling approach would be required to quantify this burden, these data are strongly suggestive that dengue infections result in a significant burden of symptomatic and severe disease in urban Indonesia."

  The paper refuses the burden estimate, states the order of magnitude anyway, names the method that would be needed to do it properly, and grades its own claim to "strongly suggestive". **Declining to make the estimate while still saying what the number means is more persuasive than either overclaiming or staying silent.**

Closes on the research that should follow, in the form of a prediction: "Prospective incidence studies would likely reveal dengue burdens far in excess of reported incidence rates."

## Data, code and funding
Ethical approval is named by committee; consent is described including assent from older minors ("An informed consent form was signed by a parent or legal guardian, and by the subject if aged 13–18 years"); the cluster list is published as an appendix; and the STROBE checklist is supplied. Industry involvement is visible in the author list and acknowledgements, including technical statistical advice named by person and affiliation.

## Distinctive moves to borrow
1. **Justify the data type, not just the study.** "Age-stratified seroprevalence data are relatively unbiased indicators of past exposure" is the sentence that licenses the whole design.
2. **State the identifying assumption in the abstract**, in the same clause as the estimate it produces ("considering a constant force of infection").
3. **Give the sample size calculation with all its inputs**, including where the expected prevalences came from, and the per-cluster allocation.
4. **Report prevalence disaggregated by the variable the model is fitted to**, so the reader sees the gradient behind the parameter.
5. **Translate the fitted parameter into a cumulative statement by age** — what a policymaker will actually quote.
6. **Compare with prior seroprevalence estimates on assay, place, year and age band**, and offer competing explanations for the difference without adjudicating.
7. **Argue that a known assay bias is small from local epidemiology**, rather than asserting it.
8. **Fence the scope, then state the order of magnitude anyway**, name the method that would do it properly, and grade the claim accordingly.
9. ◆ **Name the reporting guideline in the first line of Methods and supply the completed checklist.**
10. **Write the Author Summary around the decision in play**, not as a simplified abstract.

## Related files
For the mapping-and-burden approach to the same disease see [29-bhatt-2013-global-dengue-distribution](29-bhatt-2013-global-dengue-distribution.md); for parameter estimation from observational data with a clean estimand see [07-lauer-2020-incubation-period](07-lauer-2020-incubation-period.md); for the reporting-rate problem this paper's serology circumvents see [18-bjornstad-2002-tsir-measles](18-bjornstad-2002-tsir-measles.md).
