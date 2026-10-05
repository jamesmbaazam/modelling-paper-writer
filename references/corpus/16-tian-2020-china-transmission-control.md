# 16 — Tian et al. (2020), *Science*
**"An investigation of transmission control measures during the first 50 days of the COVID-19 epidemic in China"**
Tian H, Liu Y, Li Y, Wu C-H, Chen B, Kraemer MUG, et al. *Science* 368(6491):638–642. PMC7164389.

**Archetype:** the *natural-experiment evaluation* — statistical association across many jurisdictions, plus a mechanistic counterfactual, written under emergency time pressure for a general-science readership.

## Structure
A one-line **editor's summary box** ("The most effective interventions") precedes the abstract. Then abstract, then continuous unlabelled main text; no Methods section at all in the body — model specification, priors and sensitivity analyses live entirely in the Supplementary Materials. Acknowledgements → References and Notes → Supplementary Materials.

## Opening move
> "Responding to an outbreak of a novel coronavirus [agent of coronavirus disease 2019 (COVID-19)] in December 2019, China banned travel to and from Wuhan city on 23 January 2020 and implemented a national emergency response. We investigated the spread and control of COVID-19 using a data set that included case reports, human movement, and public health interventions."

Pattern: **dated intervention → "We investigated … using a data set that included …".** The data are named in the first paragraph, because in an evaluation paper the data *are* the contribution.

## Methods
- The SEIR model is named but never written out; parameters appear only in a table with means and **95% Bayesian credible intervals** (the table row for R₀ reads: basic reproduction number, mean 3.15, 95% BCI 3.04 to 3.26; reporting proportion 0.002 (0.001–0.003)).
- **Two inferential engines, deliberately paired**: (i) regression of case counts on intervention timing across 342 cities, reported with coefficients, 95% CIs and p-values (the table row for suspension of intra-city public transport, implementation: coefficient –3.50, 95% CI –4.28 to –2.73, P < 0.01); (ii) a mechanistic SEIR counterfactual. The association survives only because both point the same way.
- Non-parametric tests reported in full: "Mann-Whitney U = 8197, z = −3.4, P < 0.01".
- Assumptions are argued, not asserted: "it is unlikely that this decline happened because the supply of susceptible people was exhausted."
- Figure captions carry methodological detail that would otherwise need a Methods section.

## Results
> "the Wuhan travel ban was associated with a delayed arrival time of COVID-19 in other cities by an estimated 2.91 days [95% confidence interval (CI), 2.54 to 3.29 days] on average"
> "Cities that implemented a Level 1 response (any combination of control measures) preemptively … reported 33.3% (95% CI, 11.1 to 44.4%) fewer laboratory-confirmed cases during the first week"
> "Our model suggests that without the Wuhan travel ban or the national emergency response, there would have been 744,000 (±156,000) confirmed COVID-19 cases outside Wuhan by 19 February"
> "A total of 262 cities reported cases within 28 days."

Three uncertainty conventions coexist and are used for different objects: **95% CI** for regression estimates, **95% BCI** for fitted model parameters, **± SD** for simulated counterfactual counts. Keep them distinct and label each.

Verbs are chosen carefully to match the design: interventions are "associated with" outcomes; the model "suggests"; the response "appears to have delayed the growth and limited the size of the COVID-19 epidemic".

## Literature
Numbered, moderate density, grouped by topic. The gap is stated as an evidential gap, not an absence of papers:
> "Although the spatial spread of infectious diseases has been intensively studied, including explicit studies of the role of human movement, the effectiveness of travel restrictions and social distancing measures in preventing the spread of infection is uncertain."

A historical benchmark is used to make a rate meaningful: 2009 H1N1 "took 132 days to reach the same number of cities in China."

## Voice
Past tense for what was done and observed; present for standing implications. First person plural throughout ("we investigated", "we estimate", "we therefore carried out"). Hedges are load-bearing: "potentially hold lessons", "is uncertain", "would not have curbed", "may need to be reinstated, in some form".

> "This implies that a large fraction of the Chinese population remains at risk of COVID-19; control measures may need to be reinstated, in some form, if there is a resurgence of transmission."

## Discussion and limitations
The design limitation is stated *before* the conclusion is restated, in the same breath:
> "This study has drawn inferences not from controlled experiments but from statistical and mathematical analyses of the temporal and spatial variation in case reports, human mobility, and transmission control measures. With that caveat, control measures were strongly associated with the containment of COVID-19…"
> "We could not investigate the impact of all elements of the national emergency response because many were introduced simultaneously across China."

The second is the standard confounding-by-co-intervention admission every NPI evaluation owes its reader.

## Data, code and funding
> "Data and materials availability: Code and data are available on the following GitHub repository: https://github.com/huaiyutian/COVID-19_TCM-50d_China"

## Distinctive moves to borrow
1. **"With that caveat, …"** — concede the design, then state the conclusion in the same sentence rather than burying the caveat at the end.
2. Pair a regression across units with a mechanistic counterfactual; report both.
3. Anchor every date. The paper is legible years later because nothing is "recently".
4. Give the counterfactual as an absolute number of cases — that is the sentence that gets quoted.

## Related files
Other *real-time transmission analysis* exemplars: see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md) for an individual-based model fitted to a live national epidemic while control decisions were still being made; [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md) for district-level transmission estimates turned into beds needed during an outbreak response; [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) for a widely used R_t estimator with two failing assumptions fixed, shipped in the package the field already uses; [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) for the real-time Bayesian estimate of a time-varying reproduction number, in a clinical journal's structure; [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md) for a living pipeline whose article versions its method alongside its software; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver; [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast whose corrected onsets feed a reproduction-number estimate, evaluated against later data.
