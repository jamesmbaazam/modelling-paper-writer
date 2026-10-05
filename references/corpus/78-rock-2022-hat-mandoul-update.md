# 78 — Rock et al. (2022), *Infectious Diseases of Poverty*
**"Update of transmission modelling and projections of gambiense human African trypanosomiasis in the Mandoul focus, Chad"**
Rock KS, Huang CI, Crump RE, Bessell PR, Brown PE, Tirados I, et al. *Infect Dis Poverty* 11:11. doi:10.1186/s40249-022-00934-8.

**Archetype:** the *model update that audits its own predictions* — a group returns to a published projection four years on, checks it against the data that arrived, separates what changed because the methods improved from what changed because there were more data, and re-projects. It sits under scenario projection (five strategies to 2030) and policy counterfactual (the share of a transmission reduction attributed to each intervention), but the move worth copying is the audit.

## Structure
*Infectious Diseases of Poverty* (BMC): structured abstract (**Background / Method / Results / Conclusions**) → graphical abstract → `Keywords` → `Background` → `Methods` (*Data* · *The gHAT model* · *Assessment and update of model fits*, in three numbered steps · *Projections and cessation*) → `Results` → `Discussion` (with a `Limitations` subsection) → `Conclusions` → declarations.

**The update is designed as three numbered steps**, each isolating one source of change: the old model re-run with the screening numbers that actually happened; the new model fitted to the old data; the new model fitted to all the data. "By comparing step 1 and 2 we can see the impact of model improvements, but not improvements due to more data availability."

## Opening move
> "A new World Health Organization (WHO) roadmap has set out control, elimination or eradication goals to be achieved by 2030 for 20 different neglected tropical diseases (NTDs)—a collection of mainly infectious diseases affecting some of the poorest and most marginalised populations globally."

The Introduction then gives the disease's clinical course, diagnostic algorithm and control tools at length — necessary, because the paper's argument turns on diagnostic specificity, passive versus active screening, and vector control, and a modelling reader may know none of them.

**The paper questions its own earlier conclusion in the Introduction**: earlier work "suggested that it was likely that transmission was already interrupted by 2015… However, in the present study we question whether this is consistent with the low-level but persistent case reporting still occurring in the focus." **Open an update by stating which earlier finding the new data put in doubt.**

**Then the questions a programme manager would ask, numbered**: "(i) given there were six reported cases in 2018 and 11 in 2019, what does this tell us about underlying transmission? (ii) when can we expect to observe zero cases reported? (iii) can active screening and vector control be stopped without risking recrudescence?"

## Methods
- **Correct the old projection for what actually happened before judging it**: the earlier paper assumed 27,265 people screened each year from 2016; the real numbers were lower, so step 1 re-runs the old model with them. "Large differences between assumed screening levels and actual screening levels can have a substantial impact on model projections".
- **Tabulate every change between old and new models** (Table 1): specificity fixed at 100% versus estimated; false positives absent, stage 1 only, or either stage; detection improvements assumed versus estimated; vector reduction assumed versus estimated.
- **Explain why specificity matters as prevalence falls**: "As infection continues to decline in Mandoul—and globally—the positive predictive value of tests is reduced and eventually false positives may outnumber true positives without parasitological confirmation".
- **Estimate a quantity that was also measured in the field, as a check**: "Estimating the tsetse reduction using the model fitting, rather than substituting the value measured in the field allows us to test whether there is agreement between model outputs based on human case data and entomological dynamics observed in the study region. Any differences in these two could indicate that infection is occurring outside of the area under control".
- **Relax an assumption when the fit shows it is wrong, and say so**: "Based on preliminary results which assumed false positives must be stage 1, we relaxed this assumption and allowed false positives to be reported as either stage 1 or stage 2 with a fitted probability."
- **Use the field's reporting checklist** (PRIME-NTD), completed in the supplement.

## Results
**Begin with the audit, including what the earlier model got wrong**:
> "The previous model predicted that there would be a median of zero cases by 2017 in AS and by 2018 in PS. Newly available data from 2017 to 2019 are very low, but cases were still reported, indicating that our previous model overestimated the impact of the strategy on case reporting from 2014."

**Give the new model's predictions next to the observed counts**: "Median active detection predictions increased to 26, 26 and 18 for 2017–2019 compared to zero for the previous model with new screening data… (actively reported cases were 15, 3 and 10, and passively reported cases were 7, 3 and 1 for 2017–2019)", and say where the intervals still miss: they "now cover all the reported data for the prediction period except passive cases in 2015 and active cases in 2018."

**The field check is reported as agreement with a measured value**: "the focus-wide reduction of tsetse (after 4 months) was estimated to be 99.1% (95% CI 96.1–99.6%), around our 99% assumed estimate based on the catch of tsetse from monitoring traps in the intervention area."

**Attribute the transmission reduction by counterfactual, over two horizons** (Table 3): vector control accounts for 74.0% of the reduction over 2013–2015 but 34.7% over 2013–2019, as the other interventions accumulate effect. **An attribution depends on the window; give two.**

**Report support for structural alternatives, and what they imply**: "Less than 0.1% of the ensemble model was made up of simulations from Models 7 and 8" (those with animal reservoirs), and even within them, animals were unlikely to be a maintenance reservoir.

**Stress-test the projection against the worst plausible event**: even with 90% tsetse reintroduction in 2021, "only 2% of our model simulations… saw resurgence of infection in humans where transmission occurred beyond 2030".

## Literature
Numbered citations, with the group's own earlier paper treated as the main comparator throughout. Field and diagnostic literature supplies the specificity priors; the programme's own data (WHO HAT Atlas, the national control programme) are cited as primary sources.

## Voice
First-person plural. The register is self-critical without being defensive — "In hindsight the level used… was higher than achieved" — and every concession is followed by what it did or did not change.

## Discussion and limitations
**Say how much the earlier error mattered, with the evidence**: "Despite this, we don't think that in this instance the screening level substantially impacted our results, as is demonstrated with our re-simulation of the original gHAT model with correct screening coverage for those years".

**Generalise the lesson about projections**: "predictive modelling always faces the challenge of defining realistic future intervention strategies as there are scenarios where changing to a different strategy than the one modelled can have a major impact on results… Here we try to mitigate against this situation by providing projections for five alternative strategies".

**The recommendation follows from the specificity result**: projections suggest zero passive cases before 2023, "although active case detection would continue due to imperfect specificity of the current diagnostic algorithm, and therefore additional confirmatory testing (such as mAECT, LAMP or trypanolysis) ought to be considered." The model predicts that the programme will keep finding cases that are not cases, and recommends the test that would show it.

**Limitations name the biology left out and the operational assumptions that could fail**: no asymptomatic self-cure, no importation, deterministic dynamics, and passive screening assumed to stay intact — "Reduction in the capacity or coverage to find and treat gHAT-infected people could have deleterious impact".

## Data, code and funding
The case data belong to WHO and are available on request "for researchers who meet the criteria for access"; model code and outputs are on the Open Science Framework, and an interactive interface shows both the counterfactuals and the projections. **When the data cannot be shared, share the code and the outputs, and say exactly who controls the data.**

## Distinctive moves to borrow
1. **Open an update by naming the earlier finding the new data question.**
2. **Number the programme manager's questions** in the Introduction.
3. **Correct the old projection for what actually happened** before judging it.
4. **Separate method improvements from new data** with a stepwise design.
5. **Tabulate every change between old and new models.**
6. **Explain why test specificity matters more as prevalence falls.**
7. **Estimate a quantity that was also measured in the field**, as a check on the model.
8. **Report what the earlier model got wrong**, first, with observed counts beside predictions.
9. **Attribute effects over more than one window.**
10. **Report the posterior weight of structural alternatives.**
11. **Stress-test projections against the worst plausible event.**
12. **Derive the recommendation from the model's mechanism** — here, false positives and the test that would expose them.
13. **Say who controls the data** when it cannot be shared.

## Related files
For an independent model update that audits its own inputs see [61-abbas-2020-hpv-input-revisions](61-abbas-2020-hpv-input-revisions.md); for serological markers validated before modelling elimination see [65-golden-2016-onchocerciasis-seroprevalence](65-golden-2016-onchocerciasis-seroprevalence.md); for a programme's forecasts scored against what happened see [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md). Other *policy counterfactual* exemplars: see [01-grais-2008-measles-orv-niamey](01-grais-2008-measles-orv-niamey.md) for a stochastic model fitted to one outbreak and re-run under alternative response scenarios; [20-nouvellet-2015-rapid-diagnostics-ebola](20-nouvellet-2015-rapid-diagnostics-ebola.md) for three strategies compared on several metrics at two scales, with an answer that depends on context; [49-verguet-2015-measles-sia](49-verguet-2015-measles-sia.md) for a model used to compute a campaign schedule rather than project a scenario, delivered as a per-country table. Other *scenario projection for policy* exemplars: see [12-ferguson-2006-mitigating-pandemic](12-ferguson-2006-mitigating-pandemic.md) for a large individual-based simulation organised around intervention options, with almost no equations; [25-davies-2020-npi-uk](25-davies-2020-npi-uk.md) for an age-structured model run under a ladder of intervention scenarios while the decisions were being made; [47-ngonghala-2020-npi-math-assessment](47-ngonghala-2020-npi-math-assessment.md) for a stability analysis that precedes the scenarios, in the applied-mathematics register; [69-kerr-2021-test-trace-quarantine](69-kerr-2021-test-trace-quarantine.md) for scenarios run on a documented agent-based model and then checked against the months that followed.
