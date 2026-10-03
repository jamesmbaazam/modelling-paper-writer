# 34 — Yang, Santillana & Kou (2015), *PNAS*
**"Accurate estimation of influenza epidemics using Google search data via ARGO"**
*PNAS* 112(47):14473–14478. doi:10.1073/pnas.1515373112. PMC4664296.
**Citations:** ~420 (OpenAlex, Sept 2026).

**Archetype:** the *corrective successor* — a paper that exists because a famous method failed, enumerates the reasons it failed, and fixes each one in turn. The template for building on a public failure without gloating.

## Structure
`Significance` → Abstract → introduction → **`Our Contribution`** → `Results` → `Discussion` (*Strength of ARGO*; *Limitations and Next Steps*) → `Materials and Methods` (*Google Data · CDC's Data · Formulation of Our Model · The ARGO Model · Parameter Estimation of ARGO Model · Accuracy Metrics*) → extensive SI.

**`Our Contribution` as a named section** is the structural signature: the failures of the predecessor are enumerated in the introduction, then this section answers them (i)–(iv) in the same order. If your paper is a response to identified flaws, give the response its own heading and preserve the ordering.

## Opening move
> "Big data generated from the Internet have great potential in tracking and predicting massive social activities. In this article, we focus on tracking influenza epidemics. We propose a model that utilizes publicly available Google search data to estimate current influenza-like illness activity level."

And the positioning, which is a model of how to describe a predecessor's failure fairly:
> "In 2009, Google Flu Trends (GFT), a digital disease detection system that uses the volume of selected Google search terms to estimate current influenza-like illnesses (ILI) activity, was identified by many as a good example of how big data would transform traditional statistical predictive analysis. However, significant discrepancies between GFT's flu estimates and those measured by the Centers for Disease Control (CDC) in subsequent years led to considerable doubt about the value of digital disease detection systems."

Note: the failure is attributed to *the discrepancies*, and the reputational damage is described as happening to the whole field — which is what motivates a fix rather than a dismissal.

## Methods
- **Three-stage model presentation**: conceptual (a hidden Markov structure establishing that flu activity causes searches, not the reverse) → **numbered formal assumptions** (autoregressive structure on logit ILI; conditional Gaussian log search volumes; conditional independence) → the operational equation with N = 52 autoregressive terms and K = 100 search terms. Stating assumptions as numbered propositions before the equation is unusual outside statistics journals and is worth importing.
- **Regularisation choice justified empirically, with the alternatives shown**: L1 on both autoregressive and search terms, with a supplementary table comparing five specifications (same L1, separate L1, same L2, separate L2, elastic net). "L1 penalty generally outperforms the L2 penalty… [it] tends to shrink the coefficients of unnecessary independent variables to be exactly zero."
- **Rare honesty about hyperparameter selection**: "the cross-validation result is highly noisy… we need to prespecify some of the hyperparameters." Most papers hide this; saying it makes the rest more believable.
- **Rolling-window retraining with strict temporal integrity**: a two-year (104-week) moving window, out-of-sample from March 2009 to July 2015, "assuming we had access only to the historical CDC's ILI reports up to the previous week of estimation."
- **Five benchmarks, trained under identical conditions**: GFT, Santillana et al., GFT+AR(3), AR(3) alone, and a naive previous-week baseline — with an explicit fairness statement: "For fair comparison, all benchmark models (ii–iv) are dynamically trained with a 2-y moving window." **If you benchmark, say what you did to make the comparison fair.**
- **Five error metrics**, all expressed relative to the naive method: "the number reported is the ratio of error of a given method to that of the naive method."
- **A summary comparison statistic with bootstrap CIs**: relative efficiency, "the ratio of the true mean-squared error of method 2 to that of method 1", enabling one-line claims instead of metric-by-metric recitation.
- **Robustness against the specific ways this class of model fails**: tested against unrevised CDC reports (to avoid forward-looking bias), and against 25 different Google Trends snapshots — "ARGO is threefold more stable than the method of ref. 16."

## The three fixes, stated as design responses
Each GFT failure identified by [31-lazer-2014-parable-of-google-flu](31-lazer-2014-parable-of-google-flu.md) gets a mechanism:
1. *Model drift* → dynamic retraining on a rolling window.
2. *Changing search behaviour* → L1 regularisation reselects terms over time.
3. *Ignoring time-series structure* → 52 autoregressive lags capture seasonality.

## Results
> "Close inspection shows that, in the post-2009 regular flu seasons, ARGO uniformly outperformed all other alternative estimation methods in terms of RMSE, MAE, MAPE, and correlation."
> "ARGO avoids the notorious overshooting problem of GFT, as seen in Fig. 1."
> "Our method is twice as accurate as the method that combines GFT with autoregressive terms."
> "ARGO self-corrected its performance the following week by shifting a portion of model weights… achieved the fastest self-correction."

The last is the distinctive framing: **the paper's headline virtue is recovery, not accuracy.** Given that the predecessor's fatal flaw was staying wrong for two years, "self-correcting" is precisely the right property to foreground.

## Discussion and limitations
> "Although ARGO displays a clear superiority over previous methods, it is not fail-proof. Because it relies on the public's search behavior, any abrupt changes to the inner works of the search engine or any changes in the way health-related search information is displayed to users will affect the accuracy of our methodology."
> "We expect that ARGO will be fast at correcting itself if any such change takes place in the future."

The limitation is the *same vulnerability* the predecessor had; the claim is only that the new method recovers faster. That is a modest, defensible, and therefore credible position.

A dated development note is included rather than quietly folded in: "After the initial submission of this article in May 2015, Google announced that GFT would be discontinued… This new development makes our contribution timely and useful."

## Data, code and funding
"All data used in this article are publicly available. Therefore, IRB approval is not needed." Sources given with URLs and an access date; an R package implementing ARGO is released.

## Distinctive moves to borrow
1. **Enumerate the predecessor's flaws, then give your response its own section in the same order.**
2. State assumptions as numbered propositions before the model equation.
3. **Report every error metric relative to a naive baseline**, and add one summary statistic with CIs.
4. Say explicitly what you did to make the benchmark comparison fair.
5. Admit when hyperparameter selection was noisy and had to be prespecified.
6. If your predecessor failed by staying wrong, make **recovery speed** the advertised property.
