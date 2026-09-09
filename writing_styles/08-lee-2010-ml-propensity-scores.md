# 08 — Lee, Lessler & Stuart (2010), *Statistics in Medicine*
**"Improving propensity score weighting using machine learning"**
*Stat Med* 29(3):337–346. doi:10.1002/sim.3782. PMC2807890.

**Archetype:** the *simulation-benchmark methods* paper — no real outbreak at all; a factorial simulation study comparing estimators under known truth. This is the template for any "does method X beat method Y" contribution.

## Structure
`Abstract` → `Introduction` (~6 ¶) → `Methods` (simulation setup; propensity score estimation methods; estimation of treatment effect; performance metrics) → `Results` (`Covariate balance`, `Estimate of effect and standard error`, `Weights`, then smaller/larger sample sizes) → `Discussion` (~5 ¶) → Acknowledgements → References.

The Results subheadings are **the performance metrics themselves**, in a fixed order that matches the order the metrics were defined in Methods.

## Opening move
> "Machine learning techniques such as classification and regression trees (CART) have been suggested as promising alternatives to logistic regression for the estimation of propensity scores. The authors examined the performance of various CART-based propensity score models using simulated data. Hypothetical studies of varying sample sizes (n=500, 1000, 2000) with a binary exposure, continuous outcome, and ten covariates were simulated under seven scenarios differing by degree of non-linear and non-additive associations between covariates and the exposure."

Pattern: **claim in the literature → "we examined … using simulated data" → the exact simulation design in one long specifying sentence.** The design is given before any motivation is elaborated.

## Methodology conventions
- **Scenario lettering.** Seven data-generating scenarios labelled A–G, ordered by increasing non-linearity/non-additivity ("A: additivity and linearity (main effects only)" … "G: moderate non-additivity and non-linearity"). These letters then index every table, figure and results sentence in the paper. This is the single most portable device in the paper.
- Notation kept inline and minimal: `Pr(A=1|W_i) = 1/(1+exp(−β·f(W_i)))`, `Y = α_i W_i + γA`, with the true effect fixed and stated (γ = −0.4).
- Tuning parameters are given exactly, with the source: 100 bootstrap replicates for bagged CART; "20 000 iterations and a shrinkage parameter of 0.0005" for boosted CART, citing McCaffrey et al.
- Software named to the package and version: `rpart`, `ipred`, `randomForest`, `twang`, R 2.6.1.
- **Performance metrics defined as a closed list before any results appear**: absolute standardized mean difference (ASAM), absolute bias, standard error, 95% CI coverage — then reported in that same order in every table.
- Sensitivity analysis is a single targeted paragraph (adding outcome noise at σ = 0.1, 0.2) that defends the one clearly unrealistic design choice.

## Results storytelling
Means across 1000 replicates, ranges in parentheses; coverage as a percentage; bias as a percentage.
> "All methods displayed generally acceptable performance under conditions of either non-linearity or non-additivity alone. However, under conditions of both moderate non-additivity and moderate non-linearity, logistic regression had subpar performance, while ensemble methods provided substantially better bias reduction and more consistent 95% CI coverage."
> "Across all scenarios, bagged CART, random forests, and boosted CART averaged mean absolute biases of 10.3%, 7.7%, and 6.8%, respectively. Boosted CART displayed the best 95% CI coverage with ≥98.6% coverage in all scenarios."
> "For example, in Scenario E, the proportion of comparison group weights greater than ten by method was: logistic regression: 3.5%, CART: 0.9%, pruned CART: 0.7%, bagged CART: 0.0%, random forests: 3.1%, boosted CART 0.7%."

Structure of a results paragraph: **overall verdict sentence → the "however" that identifies where methods separate → the numbers that prove it.** Comparative adjectives are used openly ("subpar", "substantially better", "best"), which is licensed here because the truth is known by construction.

Boxplots over 1000 replicates are used to argue about *dispersion*, not just central tendency — captions call out "high outliers".

## Literature integration
Numbered brackets, dense in the Introduction, thin in Results. The gap is framed as adoption rather than discovery:
> "The suggestion to use such algorithms for propensity score model construction is not new. However, these methods have not been widely applied in the propensity score literature, perhaps because of the 'black box' nature of some of the algorithms and difficulty in etiologic interpretations of results."
The Discussion then rebuts the objection head-on: "However, etiologic inference is not a necessary component of propensity score estimation. Therefore, machine learning techniques may be well-suited to the task…"

## Voice
Past tense for what was done and observed; present for implications. "We" used sparingly ("we examined", "we performed"); some sentences use "the authors". Hedged conclusions despite decisive simulations: "The results suggest that ensemble methods, especially boosted CART, may be useful for propensity score weighting."

## Limitations
Framed as *deliberate design choices with a rationale*, which is the strongest form:
> "In this study we used only the basic, off-the-shelf versions of each of the methods, since that is likely what most applied researchers would do. It is likely that any method may perform better when implemented by a highly skilled user."
Also: outcome fully determined by covariates (justified by citing standard practice, then defended with the noise sensitivity analysis); no post-weighting covariate adjustment (deliberate, to isolate the propensity score).

## Distinctive moves to borrow
1. Letter-code your data-generating scenarios and never renumber them.
2. Fix a metric order and repeat it in every table so readers pattern-match instead of re-reading.
3. Benchmark against the incumbent default method (here, logistic regression), and report where the incumbent is *fine* as well as where it fails.
4. Justify the "off-the-shelf" configuration as the realistic user's configuration.
