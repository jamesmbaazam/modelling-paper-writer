# 29 — Bhatt et al. (2013), *Nature*
**"The global distribution and burden of dengue"**
Bhatt S, Gething PW, Brady OJ, Messina JP, Farlow AW, Moyes CL, Drake JM, Brownstein JS, Hoen AG, Sankoh O, Myers MF, George DB, Jaenisch T, Wint GRW, Simmons CP, Scott TW, Farrar JJ, Hay SI. *Nature* 496:504–507. doi:10.1038/nature12060. PMC3651993.
**Citations:** ~10,400 (OpenAlex, Sept 2026) — the most cited ML-based paper in infectious disease modelling.

**Archetype:** the *risk-mapping and burden-estimation* paper — supervised ML (boosted regression trees) over environmental covariates produces a global risk surface, which a second, Bayesian stage converts into a burden estimate. The dominant template for ML in spatial epidemiology.

## Structure
Abstract → continuous unheaded main text → `Methods` with four task-shaped subheadings:
*Assembly of the occurrence database and its quality control · Explanatory covariates · Predicting the probability of occurrence (risk) of dengue transmission · Estimation of dengue burden and populations at risk*
→ Acknowledgements → References → Supplementary Information A–E.

The Methods subheadings are **the pipeline stages in execution order**. For any ML paper, this beats a generic `Data`/`Model`/`Analysis` split: the reader can audit each stage independently.

## Opening move
> "Dengue is a systemic viral infection transmitted between humans by Aedes mosquitoes. For some patients dengue is a life-threatening illness. There are currently no licensed vaccines or specific therapeutics, and substantial vector control efforts have not stopped its rapid emergence and global spread."

Pattern: **what the disease is → why it matters clinically → why existing control has failed → therefore the evidence base must improve.** Four short sentences, no ML vocabulary at all. The algorithm is never the selling point.

## Supervised learning conventions
- **Algorithm named, then explained in one sentence of plain mechanism**: "a boosted regression tree (BRT) statistical model of dengue risk"; "The BRT approach combines regression trees with gradient boosting, whereby an initial regression tree is fitted and iteratively improved upon in a forward stagewise manner (boosting)."
- **Training data defined as a unit of observation, precisely**: an occurrence is "one or more laboratory or clinically confirmed infection(s) of dengue occurring at a unique location (a 5 km × 5 km pixel) within one calendar year". 8,309 records from 2,838 sources, 1960–2012, with "manual review and automatic quality control to ensure information fidelity and precise geo-positioning".
- **Covariates justified by mechanism, not by availability**: eight gridded covariates chosen for "factors known or hypothesised to contribute to suitability for dengue transmission" — precipitation, a biologically derived temperature-suitability index built from the extrinsic incubation period, NDVI, urbanisation, accessibility, relative poverty. Preprocessing stated: standardised to identical resolution, extent and boundaries; "No covariate grids were shown to be adversely affected by multicollinearity."
- **The absence problem is solved explicitly**, which is the hardest part of presence-only ML and the part most papers fudge: "pseudo-absence points were randomly generated based on dengue presence or absence certainty measures at a national or subnational level. Pseudo-absence locations were restricted to a maximum distance μ from any recorded presence site. Additionally, to compensate for 'contamination' of true but unobserved presences within the generated pseudo-absences, n_p pseudo-presence points were generated."
- **Uncertainty in a modelling choice is turned into an ensemble** rather than resolved arbitrarily: "rather than using an individual parameter combination from π, we created an ensemble of 336 BRT models spanning reasonable ranges in π and evaluated the central tendency as the mean across all 336 BRT models." This is the paper's key methodological move — *propagate the arbitrary choice instead of defending it*.
- **Performance reported with the spread across the ensemble**: "Validation statistics indicated high predictive performance of the BRT ensemble mean map with area under the receiver operating characteristic (AUC) of 0.81 (±0.02 SD, n = 336)."
- **Overfitting addressed by appeal to the method's own property**, briefly: BRT "has been shown to fit complicated response functions efficiently, while guarding against overfitting."
- Covariate effects reported in prose rather than as a variable-importance table: "We found high levels of precipitation and temperature suitability for dengue transmission to be most strongly associated among the variables considered with elevated dengue risk, although low precipitation was not found to strongly limit transmission." Note the concessive clause — the *absence* of an expected effect is reported too.

## Results storytelling
The ML output is never the headline. **The headline is the burden**, with Bayesian credible intervals:
> "We estimate that there were 96 million apparent dengue infections globally in 2010. Asia bore 70% (67 [47–94] million infections) of this burden…"
> "We estimate that an additional 294 (217–392) million inapparent infections occurred worldwide in 2010."
> "This infection total is more than three times the dengue burden estimate of the World Health Organization."
> "Predicted risk in Africa, though more unevenly distributed than in other tropical endemic regions, is much more widespread than suggested previously."

The comparison to the standing WHO figure is what made the paper matter. **Anchor a new estimate to the number it replaces**, and state the multiple.

## Voice
Active, first-person plural: "We compiled a database", "we chose a set of gridded environmental covariates", "Here we present the outcome of a new project to derive an evidence-based map of dengue risk". Passive reserved for data handling ("All occurrence data underwent manual review"). Confidence expressed through the validation statistic rather than through adjectives.

## Limitations
> "It remains the case, however, that the empirical evidence base for global dengue risk is more limited than that available, for example, for Plasmodium falciparum and P. vivax malaria."
> "Africa has the poorest record of occurrence data and, as such, increased information from this continent would help to better define the spatial distribution of dengue within it and to improve derivative burden estimates."
> "The absolute uncertainties in the national burden estimates are inevitably a function of population size, with the greatest uncertainties in India, Indonesia, Brazil and China."

**Uncertainty is localised, not global**: the paper says *where* it is least trustworthy and *why*, naming countries. For a map, that is the only honest form of a limitation.

## Data and code
Weak by modern standards and worth noting as the thing not to copy: "the full bibliography and occurrence data are available from authors on request" — no repository, no code. Compare `32` Olival (Zenodo DOI for data *and* code) and `33` Han (Dryad).

## Distinctive moves to borrow
1. **Name the pipeline stages as Methods subheadings**, in execution order.
2. **Turn an arbitrary modelling choice into an ensemble** and report the spread as part of the performance statistic.
3. Derive at least one covariate from mechanism (the temperature-suitability index) rather than using raw climate layers.
4. Report the covariate that *didn't* matter.
5. Localise your uncertainty geographically and name the countries.
6. Lead with the burden, not the AUC.
