# 32 — Olival et al. (2017), *Nature*
**"Host and viral traits predict zoonotic spillover from mammals"**
Olival KJ, Hosseini PR, Zambrana-Torrelio C, Ross N, Bogich TL, Daszak P. *Nature* 546:646–650. doi:10.1038/nature22975. PMC5570460.
**Citations:** ~1,200 (OpenAlex, Sept 2026).

**Archetype:** the *trait-based prediction* paper — a hand-curated relational database plus statistical learning to predict which hosts and which viruses matter, with the output framed as a surveillance priority map rather than as a model.

## Structure
Abstract → Main → `Methods` with subheadings that are each an auditable decision:
*Database · Phylogenetic signal · Host phylogenetic analysis and phylogenetic host breadth · GAM fitting and selection · Model cross-validation · Spatial variables · Calculating and visualizing missing viruses and missing zoonoses · Data availability · Code availability*
Extended Data Fig. 1 is a **conceptual diagram of the three nested models**, referenced as the organising structure of the whole paper.

## Opening move
> "The majority of human emerging infectious diseases are zoonotic, with viruses that originate in wild mammals of particular concern (for example, HIV, Ebola and SARS). Understanding patterns of viral diversity in wildlife and determinants of successful cross-species transmission, or spillover, are therefore key goals for pandemic surveillance programs. However, few analytical tools exist to identify which host species are likely to harbour the next human virus, or which viruses can cross species boundaries."

Pattern: **importance → the two questions that follow → "However, few analytical tools exist to…".** The gap is a *tool* gap, which is exactly what a predictive-modelling paper can fill.

## Methods — modelling conventions worth copying
- **Three models, each answering one component of one process**, declared up front: "We fit three inter-related models to elucidate specific components of the process of zoonotic spillover" — total viral richness per host, zoonotic proportion per host, zoonotic potential per virus. A conceptual figure shows how they nest.
- **The database is described as a research product with inclusion rules**: 2,805 host–virus associations, 754 mammal species, 586 viruses, 1940–2015, cross-checked against ICTV and the Global Mammal Parasite Database. Exclusions are named: experimental infections, captive/zoological records, cell-culture discoveries — only field-detected associations are retained.
- **Evidence quality is scored and then used**: detection methods scored 0–2, with "Viral isolation and PCR detection with sequence confirmation… scored as a 2 (=stringent data)" and serology 0–1. Parallel analyses on the full and stringent datasets test whether the conclusions survive.
- **Model class justified by what it buys you**: "our use of GAMs, an incorporation of smooth spline predictor functions into the generalized linear model (GLM) framework, allowed us to examine the functional form of our predictor variables." Interpretability of shape, not raw accuracy, is the stated reason.
- **Correlated candidate predictors handled by parallel models, not by picking one**: where mechanistic redundancy existed, "we fit alternate GAMs using only one of each of these variables", then compared by AIC within 2 ΔAIC. Term selection by double-penalty smoothing.
- **Two cross-validation schemes, for two different failure modes.** Random 10-fold CV tests general predictive validity. Then **geographic cross-validation**: "systematically removed all observations (species) from each given zoogeographical region", refit, and tested predictions for the held-out region. Regions where predictions were significantly biased are *hatched on the published map*. This is the single best idea in the paper — **hold out along the dimension you intend to extrapolate over, and show on the figure where you failed.**
- **Sampling bias entered as a predictor, not corrected post hoc**: disease-related publication counts per species and per virus are included as model terms, so effort is adjusted for inside the model. Its dominance is then reported honestly: "research effort had the strongest effect on the total number of viruses per host, explaining 31.9% of the total deviance."
- **Phylogenetic non-independence quantified before and after correction** (Blomberg's K > 1 for body mass, reduced below 0.5 by phylogenetic eigenvector regression), with the residual problem admitted: "there is currently no modelling approach to control for phylogeny using GAMs."
- **Performance reported as deviance explained, defined in the text** — (D_null − D_model)/D_null — and then *contextualised against comparable studies* rather than left to look small: 27.2%–49.2% is "greater than or comparable to studies examining much narrower groups of mammal hosts".
- Effects communicated by **partial effect plots with 95% confidence bands**, plus relative percent deviance per term.

## Results
> "Of 586 mammalian viruses in our dataset, 263 (44.9%) have been detected in humans, 75 of which are exclusively human and 188 (71.5% of human viruses) zoonotic—defined operationally here as viruses detected at least once in humans and at least once in another mammal species."
> "The best-fit model for total viral richness per wild mammal species explained 49.2% of the total deviance, and included a per-species measure of disease-related research effort, phylogenetically corrected body mass, geographic range, mammal sympatry, and taxonomy (order)."
> "our model results show that bats are host to a significantly higher proportion of zoonoses than all other mammalian orders after controlling for reporting effort and other predictor variables."
> "We found that the proportion of zoonotic viruses per species increases with host phylogenetic proximity to humans, and that this relationship is significant even when we removed 'reverse zoonoses' primarily associated with transmission from humans to primates."

Two habits: **define contested terms operationally at first use** ("defined operationally here as…"), and **state the confound you controlled for inside the claim sentence** ("after controlling for reporting effort and other predictor variables"). The bat result would be worthless without that clause, and the authors put it in the sentence rather than in the Methods.

Predictions are framed as an actionable gap: "missing viruses" and "missing zoonoses" mapped geographically as surveillance priorities.

## Discussion and limitations
> "We acknowledge several important caveats in this study. First, our estimates of missing viruses and missing zoonoses per species are based on the current maximum observed research effort from the literature, and these estimates should be viewed as relative, not absolute."
> "our ecological and biological predictor variables only explain a portion of the total variation in viral richness per host and zoonotic potential based on viral traits, although this is greater than that reported in comparable order-specific studies."

Enumerated (*First… Second… Third…*), and the crucial one is a **scale caveat**: relative, not absolute. Say which of your numbers are ordinal.

## Data, code and funding
> "All datasets (host traits, viral traits, full list of host–virus associations and associated references, phylogenetic trees, and phylogenetic distance matrices) needed to fully replicate and evaluate these analyses are provided at 10.5281/zenodo.596810."
> "All R code and R package dependencies needed to fully replicate and evaluate these analyses are provided at 10.5281/zenodo.596810."
Note "and R package dependencies" — the environment, not just the scripts.

## Distinctive moves to borrow
1. **Cross-validate along the axis you will extrapolate over**, and mark the failures on the map.
2. **Score the quality of each data point and re-run on the high-quality subset.**
3. **Put sampling effort in the model as a covariate** and report how much of the signal it takes.
4. Run parallel models over redundant predictors instead of silently choosing one.
5. Contextualise a modest deviance-explained against comparable studies.
6. State the confound-adjustment inside the claim sentence.
