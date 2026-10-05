# 24 — Davies et al. (2021), *Science*
**"Estimated transmissibility and impact of SARS-CoV-2 lineage B.1.1.7 in England"**
*Science* 372(6538):eabg3055. PMC8128288.

**Archetype:** the *competing-hypotheses* paper — several mechanisms could explain one observation; each is formalised, fitted, and compared, and the winner is chosen on an explicit criterion. The strongest available template for causal argument in a modelling paper.

## Structure
Science's structured editor's abstract (`INTRODUCTION` / `RATIONALE` / `RESULTS` / `CONCLUSION`) plus a summary box, then the main text with topic subheadings:
*Characteristics of the new variant · Measuring the new variant's growth rate · Mechanistic hypotheses for the rapid spread · Implications for COVID-19 dynamics in England · Discussion*
then `Materials and methods` (*Summary of control measures in England in late 2020*, *Data sources*, *Statistical methods in brief*, *Transmission dynamic model*, **"Apparent growth of VOC 202012/01 not a result of testing artifacts"**).

That last Methods subheading is a **pre-emptive rebuttal given its own heading** — the most obvious alternative explanation is refuted where a sceptical reader will look for it.

## Opening move
> "A severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) variant, VOC 202012/01 (lineage B.1.1.7), emerged in southeast England in September 2020 and is rapidly spreading toward fixation. Using a variety of statistical and dynamic modeling approaches, we estimate that this variant has a 43 to 90% (range of 95% credible intervals, 38 to 130%) higher reproduction number than preexisting variants."

Pattern: **the observation → "using a variety of … approaches" → the headline number with its uncertainty, in sentence two.** The abstract does not withhold the answer.

## Methods
- **Triangulation is the design.** Multinomial and binomial GLMMs on sequence data and on S-gene target failure, a negative-binomial state-space model, an R_t analysis, and a full age-structured transmission model — deliberately different in their assumptions so agreement is informative: "Combining multiple lines of evidence allowed us to draw robust inferences."
- Method sentences name the model class, the estimand, and the data in one breath: "We fitted a set of multinomial and binomial generalized linear mixed models (GLMMs), in which we estimated the rate by which the VOC displaces other resident SARS-CoV-2 variants across different regions in the UK, based on both the COG-UK sequence data and the S gene target failure data."
- **Five competing mechanistic hypotheses** (increased transmissibility, longer infectious period, immune escape, increased child susceptibility, shorter generation interval) are each implemented as a model variant and ranked by DIC; the conclusion is stated as parsimony rather than proof.
- Sensitivity analyses are reported with their conclusion in the same sentence: "As a sensitivity analysis, we also ran model projections with a seasonal component such that transmission is 20% higher in winter than in summer, but this did not qualitatively affect our results (fig. S24 and table S5)."
- Notation is light and consistent: *R*, *R₀*, *R_t*, growth rate *r*(i,t), generation time *T*; CrI and CI distinguished and used correctly.

## Results
Every estimate carries an interval; where several models give several intervals, the **range across models** is reported rather than a spurious single interval:
> "we estimate that this variant has a 43 to 90% (range of 95% credible intervals, 38 to 130%) higher reproduction number than preexisting variants."
> "The increased transmissibility model does not identify a clear increase or decrease in the severity of disease associated with VOC 202012/01, finding similar odds of hospitalization given infection [odds ratio, 0.92; 95% credible interval (CrI), 0.77 to 1.10]."
> "The rapid spread of VOC 202012/01 is not an artifact of geographical differences in contact behavior and does not substantially differ by age, sex, or socioeconomic stratum."
> "Regardless of control measures, all regions of England were projected to experience a new wave of COVID-19 cases and deaths in early 2021, peaking in February 2021 if no substantial control measures were introduced."

Null results are reported as informative, with the interval doing the work: "Our estimates of severity are uncertain and are consistent with anything from a moderate decrease to a moderate increase."

## Literature
Numbered, dense; 3–4 citations per conceptual claim in the Rationale. The gap is framed as a mismatch between existing knowledge and a new object:
> "Our current understanding of effective pharmaceutical and nonpharmaceutical control of SARS-CoV-2 does not reflect the epidemiological and clinical characteristics of VOC 202012/01. Estimates of the growth rate, disease severity, and impact of this novel variant are crucial for informing rapid policy responses to this potential threat."

## Voice
Present tense for estimates and mechanisms, past for events. First-person plural throughout: "we estimate", "we fitted", "we performed", "our analysis". Hedging is precise about what is and is not supported:
> "The most parsimonious explanation for this increase in the reproduction number is that people infected with VOC 202012/01 are more infectious than people infected with a preexisting variant, although there is also reasonable support for a longer infectious period and multiple mechanisms may be operating."

## Discussion and limitations
> "There are limitations to our analysis. We have considered a small number of intervention and vaccination scenarios, which should not be regarded as the only available options for policy-makers. Our transmission model does not explicitly capture nursing home or hospital transmission of SARS-CoV-2, and we fit the model to each region of England separately rather than pooling information across regions and explicitly modeling transmission between regions."
> "Our conclusions about school closures were based on the assumption that children had reduced susceptibility and infectiousness relative to adults, but the precise values of these parameters and the impact of school closures remain the subject of scientific debate."

Two categories again: **scope of scenarios** and **contested parameters**, with the scientific debate acknowledged rather than resolved by assertion. The scenario limitation explicitly warns policymakers against reading the scenario set as the option set.

## Data, code and funding
> "All analysis code and data have been archived with Zenodo. Code and data for the negative binomial state-space model, multinomial and binomial mixed models, and transmission dynamic model are maintained at www.github.com/nicholasdavies/newcovid, and code and data for the Rt analysis are maintained at https://github.com/epiforecasts/covid19.sgene.utla.rt."

## Distinctive moves to borrow
1. **Enumerate the competing mechanisms, fit all of them, rank them on a stated criterion, and report the runners-up.**
2. Give the "it's an artifact" rebuttal its own heading and its own analysis.
3. Report a range of credible intervals across methods when several methods target the same quantity.
4. State null findings as intervals that span both directions, and say so in words.

## Related files
Other *competing hypotheses* exemplars: see [57-yakob-2015-cdifficile-displacement](57-yakob-2015-cdifficile-displacement.md) for three mechanisms, one parameter each, ranked by whether they can reproduce the data; [56-lavine-2021-endemicity](56-lavine-2021-endemicity.md) for rival explanations framed as immunity components that wane at different rates.
