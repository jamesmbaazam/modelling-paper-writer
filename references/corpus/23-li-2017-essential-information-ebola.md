# 23 — Li et al. (2017), *PNAS*
**"Essential information: Uncertainty and optimal control of Ebola outbreaks"**
Li S-L, Bjørnstad ON, Ferrari MJ, Mummah R, Runge MC, Fonnesbeck CJ, Tildesley MJ, Probert WJM, Shea K. *PNAS* 114(22):5659–5664. PMC5465899.

**Archetype:** the *decision-analytic multi-model* paper — instead of building one more model, it re-implements 37 published models and asks which uncertainty actually matters for choosing an action. The template for value-of-information and structured decision-making work.

## Structure
`Significance` → `Abstract` → `Introduction` → `Results` (figures and an elasticity table) → `Discussion` → `Materials and Methods` (*Literature Survey of Published Ebola Models*, *Compartment Models*, *Management Actions*, *Intervention Implementation*, *VoI Analysis*) → `SI Text` → Dataset S1.

## Opening move
> "Early resolution of uncertainty during an epidemic outbreak can lead to rapid and efficient decision making, provided that the uncertainty affects prioritization of actions. The wide range in caseload projections for the 2014 Ebola outbreak caused great concern and debate about the utility of models. By coding and running 37 published Ebola models with five candidate interventions, we found that, despite this large variation in caseload projection, the ranking of management options was relatively consistent."

Pattern: **a general principle stated as a conditional → the controversy that makes the principle urgent → the concrete thing done, with numbers, and the finding.** The "provided that…" clause in sentence one is the paper's entire thesis.

## Methods
- Published models are treated as **data**: surveyed, classified into four structural families (SEIHFR, SEIHR, SEIFR, SEIR), re-coded, and run under identical conditions. "Models were equally weighed."
- Standardised harness stated plainly: "starting with 10 infectious cases in a population of 10,000 individuals"; time-dependent parameters "we fixed baseline parameters at values used at the start of the epidemic". Simulation method named: Gillespie algorithm with tau-leaping.
- Compartment notation glossed on first use: "susceptible (S) to exposed (E), infectious (I), and then removed (R) compartments".
- Numbered display equations reserved for the two quantities that carry the argument: elasticity, and the expected value of perfect information (EVPI/EVPXI), with every variable defined.
- Sensitivity is a **gradient, not a point**: intervention effect sizes swept from 10% to 100% in 10% increments, so the conclusion can be stated as a threshold: an intervention "is optimal in 22 of 37 models if the effect is over 30%".

## Results
Mean ± SD across models, and counts of models supporting each recommendation — the natural units when models are the sample.
> "mean projected caseload was 5,615 ± 2,705 (SD), ranging from 184 to 9,887 cases"
> "Reducing funeral transmission is optimal in 22 of 37 models if the effect is over 30% and optimal in 31 of 37 models if interventions associated with burials lead to an 80% reduction."
> "The EVPI analysis showed that the expected improvement in management outcomes caused by resolving all model-specific uncertainties is an 11% reduction in caseload."
> "Targeting the uncertainties in model structure could improve management (i.e., reduction in caseload) by 9% (82% of total EVPI), but targeting uncertainties in caseload projection could only achieve 1% improvement of management (12% of total EVPI)."

The last sentence is the paper: uncertainty is **decomposed and each component priced in the currency of the decision** (cases averted), not in the currency of model fit.

## Literature
Numbered references; broad in the Introduction, sparse in Methods. Prior work is credited for mechanism and then displaced by a different question:
> "Hospital settings and funerals have been identified as critical transmission sources and targets for intervention"
> "Despite model-specific variations in caseload projections, a critical question for decision making is whether different models lead to different management recommendations or different rankings of alternative management actions."

## Voice
Past tense for what was done and found; present for standing facts. Strongly active and first-person plural: "we explored", "we conducted a literature survey", "we classified 37 models". Hedging is conditional and quantitative: "could improve management by 11%", "may allow for better integration".

The thesis sentence:
> "Our study shows that the uncertainty that is of most interest epidemiologically may not be the same as the uncertainty that is most relevant for management."

## Discussion and limitations
Framed as declared design choices:
> "Our study chose a 30% change to illustrate the management ranking based on caseload; we did not specifically consider the operational cost or constraints inherent in achieving that level of effect with each intervention."

Cost and feasibility are named as the missing dimension rather than quietly ignored — and that omission is exactly what a decision-maker would ask about first, so naming it protects the paper.

## Data, code and funding
R code released in three named files (`Functions.R`, `Parameters.R`, `Running models.R`); all 37 models' parameters supplied as Dataset S1 (xlsx). Re-implementing others' models and publishing the implementations is itself a contribution.

## Distinctive moves to borrow
1. **Ask whether the disagreement matters.** Divergent projections are not automatically a problem; test whether they change the recommended action.
2. Price each source of uncertainty in decision units (EVPI), so "we need better data on X" becomes a quantified claim.
3. Report robustness as a vote count across models ("optimal in 22 of 37 models").
4. Sweep the intervention effect size and state conclusions as thresholds.

## Related files
Other *methods / simulation benchmark* exemplars: see [06-keeling-rohani-2002-spatial-coupling](06-keeling-rohani-2002-spatial-coupling.md) for a phenomenological term derived from an explicit mechanism, with the conditions under which the shortcut holds; [08-lee-2010-ml-propensity-scores](08-lee-2010-ml-propensity-scores.md) for a factorial simulation study comparing estimators against a known truth; [68-ajelli-2010-abm-vs-metapopulation](68-ajelli-2010-abm-vs-metapopulation.md) for two model classes run head to head with synchronised parameters and seeding; [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md) for a fitted quantity shown to be unidentifiable from the data everyone fits it to; [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md) for a scoring rule taught through worked examples so readers can use it; [52-bosse-2023-transformed-scales](52-bosse-2023-transformed-scales.md) for the argument that the scale forecasts are scored on is itself a choice with consequences.
