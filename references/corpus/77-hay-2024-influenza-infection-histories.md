# 77 — Hay et al. (2024), *PLoS Biology*
**"Reconstructed influenza A/H3N2 infection histories reveal variation in incidence and antibody dynamics over the life course"**
Hay JA, Zhu H, Jiang CQ, Kwok KO, Shen R, Kucharski A, et al. *PLoS Biol* 22(11):e3002864. doi:10.1371/journal.pbio.3002864.

**Archetype:** *serological inference* at its most ambitious — each of 1,130 people's lifetime influenza infection history reconstructed from antibody titres against 20 strains, and the reconstructions pooled into five decades of incidence by quarter, place and age. The force of infection is not assumed to be constant or age-structured; it is recovered period by period. What makes the paper an exemplar is how carefully it says what has been estimated and what has not.

## Structure
PLoS Biology: `Abstract` → a one-sentence summary → `Introduction` → `Results` (participant data · antibody patterns by age · inference of kinetics and histories · kinetics parameters · incidence · spatial · age patterns · titre and risk) → `Discussion` → `Materials and methods` last.

**Results open with the raw data before any model output.** The first figure shows seropositivity and seroconversion by age and strain, and five patterns are described in it before the inference is introduced, so the reader can judge later whether the model's conclusions follow from what is visible in the data.

## Opening move
> "Patterns of influenza infections in humans are highly varied across time, space, and demography."

**The inference problem is named as a decoding problem**:
> "Estimating influenza infection histories from serological data therefore presents a decoding problem, as the space of possible exposure histories which could lead to an observed antibody landscape is large, and observed antibody titres are highly variable due to within-host and laboratory-level effects."

**The case for serology is made from the weakness of surveillance**: routine illness surveillance varies in quality across places and years, whereas "unobserved past infections and vaccinations leave a signature in an individual's measurable antibody profile."

## Methods
- **Name the sources of variation the model must separate**, and keep the list in the Discussion: variation in titres arises from "(i) exposure to different combinations of viruses at different times; (ii) time-dependent antibody kinetics observed at different times relative to an exposure; (iii) random and strain-specific, systematic variation in the HI assay."
- **Model the assay, not only the biology**: "A crucial component of the model is the observation level, which accounts for the fact that some strains elicit systematically higher or lower titres than others in the HI assay".
- **Test the inference on simulated data that resemble the real data**: scenario analyses "using simulated data closely resembling the Fluscape data, demonstrating that our inference system was able to accurately recover infection histories, attack rates, and antibody kinetics parameters under a range of assumptions and model misspecifications".
- **Fit the same model to a second cohort** (Ha Nam, Viet Nam) and compare the parameter estimates, so differences between datasets are visible rather than hidden in one fit.
- **Say why simplifications were needed**: the fixed-effect term on boosting and waning "masks a substantial amount of individual-level and strain-level variation… This is a necessary simplification to ensure identifiability of the post-exposure kinetics parameters while simultaneously inferring hundreds of thousands of latent infection states."

## Results
**Validate against the only external signal available, with a null comparison**:
> "We estimated antibody boosting events (infections) with >25% posterior probability for 68.9% of time windows in which individuals self-reported influenza vaccination (62 of 90 windows from 77 individuals…), compared to 43.1% (mean of null simulations; 95% quantiles: 32.8% to 51.7%) of randomly selected time windows of the same duration from randomly selected individuals"

**When there is no gold standard, compare against a null of randomly chosen windows**, so a hit rate of 69% has something to be better than.

**Flag a suspicious estimate as a likely artefact, in the Results**: the attack rate for one quarter of 1985 "was unusually high (51.8% posterior median; 95% CrI: 0.207% to 63.8%), suggesting that there might be residual bias from systematically higher titres for the A/Mississippi/1985 virus not captured by the antibody kinetics and measurement models."

**Decline a finding the data cannot distinguish from chance**:
> "To understand if this variation reflects epidemiological differences between locations or simply sampling variation, we generated a comparable null simulation where no significant spatial variation in incidence would be expected… Given the overlapping uncertainty intervals of the model estimates with the simulations, we cannot exclude the possibility that the estimated attack rates from the Fluscape data exhibited no more variation overall than would be expected by chance"

**Qualify a striking result immediately**: most individuals appeared to be infected soon after birth, but "our model requires a number of assumptions regarding cross-reactivity to pre-birth strains and antigenic distance between strains which limits our ability to draw this conclusion, particularly given contrasting previous findings from longitudinal serological studies in children."

**Show that a pattern comes from the data, not the model**: age trends in infection frequency "were similar under different assumptions for the infection history model, suggesting that these findings were driven by features of the data and not an artifact of the model structure".

## Literature
Numbered PLoS citations. The incidence estimate is placed against cohort studies elsewhere (South Africa, New Zealand) that also found high rates, and against a lower Hong Kong estimate for the same period, with a candidate explanation for the difference. The titre–protection relationship is set against the historic challenge-study benchmark of 50% protection at 1:40.

## Voice
First-person plural, past tense. The estimand is renamed to match what was measured: "We reconstructed population-wide and location-specific historical infection, or, more precisely, seroincidence rates from these infection histories". The hedges are specific — "we cannot exclude", "limits our ability to draw this conclusion" — rather than general.

## Discussion and limitations
**Say what the estimand is, and what it is not**:
> "However, it is important to note that we have estimated the incidence of detectable antibody responses and not necessarily clinically relevant infections—not all infections lead to seroconversions and not all antibody boosts reflect detectable virus shedding."

**Give the direction of the main bias**: if people were infected by strains missing from the panel, "it is likely the model would underestimate infection incidence; antigenic mismatch between the infection strain and the measured strain would lead to lower observed titres, which will lead to a lower posterior probability of infection in the model."

**Refuse a causal reading the design cannot support**:
> "As stated by Hobson and colleagues in 1972, care must be taken in assigning causality to the titre-mediated infection risk estimated here. In the present model, titres necessarily decreased over time following infection due to antigenic drift and short-term waning. If protection is governed by non-HI immunity that wanes at a similar rate, then the same association between titre and relative risk could be observed."

and bound what the estimate can be used for: "our estimates are only of relative rather than absolute risk of infection; predicting the future probability of infection for an individual would additionally require knowing the force of infection (probability of exposure) as well as knowing which strain will circulate."

**Report a sensitivity analysis that failed**: an alternative model of punctuated antigenic change "(not shown)" could not be fitted — "we were unable to produce converged model fits due to the discretization of the parameter space and thus we do not present these results" — and the gap is covered by a simulation–recovery experiment instead.

**Distinguish laboratory artefact from epidemiology as a stated risk**: the rise in titres between rounds "might reflect systematic measurement bias rather than increased recent infections as inferred by our model", for example from the delay between collection and testing of the first samples.

## Data, code and funding
Every figure and table caption ends with the same sentence: "The data underlying this figure can be found at https://doi.org/10.5281/zenodo.12795911". **Point each figure to its data, in the caption**, so a reader of any single figure can find what produced it. The inference package is open source and was extended for this analysis.

## Distinctive moves to borrow
1. **Show the raw data and its visible patterns before the inference.**
2. **Name the inference problem** (here, decoding) and why it is hard.
3. **List the sources of variation the model must separate**, and return to the list in the Discussion.
4. **Model the assay** as well as the biology.
5. **Recover known histories from simulated data** that resemble the real data, including under misspecification.
6. **Validate against a weak external signal with a null comparison.**
7. **Flag a suspicious estimate as a probable artefact** in the Results.
8. **Decline a finding that cannot be distinguished from chance**, using a null simulation.
9. **Show a pattern survives alternative model structures** before attributing it to the data.
10. **Rename the estimand to what was measured** — seroincidence, not infection.
11. **Refuse a causal reading of an association** the design cannot separate, and say what else would produce it.
12. **Report a sensitivity analysis that failed**, and what was done instead.
13. **End every caption with the DOI of its data.**

## Related files
For age-stratified immunity acquisition inferred by fitting a mechanistic model see [46-griffin-2015-malaria-immunity](46-griffin-2015-malaria-immunity.md); for antibody dynamics within a host see [41-pawelek-2012-within-host-influenza](41-pawelek-2012-within-host-influenza.md). Other *serological inference* exemplars: see [64-ximenes-2014-hepatitis-a-foi](64-ximenes-2014-hepatitis-a-foi.md) for three mixing structures fitted to one serosurvey and compared; [65-golden-2016-onchocerciasis-seroprevalence](65-golden-2016-onchocerciasis-seroprevalence.md) for a serological marker validated before the model built on it, in an elimination setting; [40-prayitno-2017-dengue-seroprevalence](40-prayitno-2017-dengue-seroprevalence.md) for a force of infection from one age-stratified serosurvey, used to show that surveillance understates burden.
