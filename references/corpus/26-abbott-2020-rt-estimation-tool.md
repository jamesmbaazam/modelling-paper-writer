# 26 — Abbott et al. (2020), *Wellcome Open Research*
**"Estimating the time-varying reproduction number of SARS-CoV-2 using national and subnational case counts"** [version 2]
Abbott S, Hellewell J, Thompson RN, Sherratt K, Gibbs HP, Bosse NI, Munday JD, Meakin S, … Kucharski AJ, Eggo RM, Funk S. *Wellcome Open Res* 5:112. doi:10.12688/wellcomeopenres.16006.2

**Archetype:** the *living methods-and-tool* paper — the deliverable is a continuously updated pipeline, website and set of R packages; the article documents the method and versions itself alongside the software. This is the template for writing up a reproducible analysis pipeline rather than a finding.

## Structure
Structured abstract (**Background / Methods / Results / Conclusions**) → `Amendments from Version 1` (an explicit, versioned changelog) → `Introduction` → `Methods` (*Data*; *Delays between case onset and report*; *Estimating the time-varying reproduction number and nowcasting reported infections*; *Estimating the daily growth rate and doubling time*; *Estimated change in daily cases*; *The effect of changes in testing procedure*; *Forecasting the reproduction number and case counts by date of infection*; *Reporting*; *Website, summarised estimates, and interactivity*) → `Discussion` → `Data availability` → `Software availability` → Acknowledgements.

Two structural features are distinctive and worth copying:
1. **The changelog is part of the article.** "In this update we include details of our new open-source time-varying reproduction method that is based on inferring latent infections rather than attempting to reconstruct them via backsampling as discussed in the previous version of this article. This approach reduces bias in estimates and increases the potential for rapid changes over time." The paper states outright that "new versions of this live article will be released alongside changes to the methods to create a record of the methodology used throughout the pandemic."
2. **A Methods subsection dedicated to a known bias** — *The effect of changes in testing procedure* — sits in Methods, not Discussion, because it governs how the output should be read.

## Opening move
> "The coronavirus disease 2019 (COVID-19) pandemic that emerged in December 2019 has since spread to over 100 countries in every continent except Antarctica. While some information on the progress of an outbreak in a given country can be gained from the reported numbers of confirmed cases and deaths, these numbers can obscure changes in the underlying dynamics of the outbreak due to delays between infection and the eventual reporting of a case or death."

Pattern: **scale → why the obvious data are misleading → the estimand that fixes it.** The second paragraph then defines R_t and argues for it: "reproduction number estimates reflect variations in transmission intensity … Monitoring changes in the time-varying reproduction can account for this delay and reveals variations in transmissibility that are not clear when using only reported cases."

## Methods
- **A compact displayed model block** replaces pages of prose — four lines that give the whole generative model:
  `R_t ~ R_{t−1} × GP` ; `I_t = R_t Σ_τ w_τ I_{t−τ}` ; `D_t = Σ_τ ξ_τ I_{t−τ}` ; `C_t ~ NB(D_t ω_(t mod 7), φ)`
  followed by a paragraph glossing each line in words. Notation is then reused consistently.
- **Priors are stated with their justification, and the previous choice is reported and explained**: "We used a log normal prior for the reproduction number (R0) with mean 1 and standard deviation 1 reflecting our current belief that Rt is likely to be centered around 1 in most of the world… This contrasts with our earlier approach which was to use a gamma prior with a of mean 2.6 and standard deviation 2."
- Gaussian process hyperpriors specified operationally: "The length scale was given an inverse gamma prior with shape and scale values optimised to give a distribution with 98% of the density between 2 days and 21 days. The prior on the magnitude was standard normal."
- **Full computational detail**: "A minimum of 4 chains were used with a warmup of 500 each and 4000 samples post warmup. Convergence was assessed using the R hat diagnostic."
- Delay distributions are estimated, not assumed, with censoring handled explicitly, and the resulting numbers are reported in the text: "an onset to case report delay distribution with a mean of 6.5 days and a standard deviation of 17 days and an onset to death report delay distribution with a mean of 13.1 days and a standard deviation of 11.7 days."
- **Every arbitrary choice is stated with its reason**: right truncation of "the last 3 days of data, based on qualitative inspection of the stability of case counts"; inclusion criteria of "fewer than 14 days with non-zero case counts" because "This restriction reduces the likelihood of spurious estimates for countries with limited transmission or case ascertainment"; "For computational reasons the maximum allowed delay is set to be 30 days."
- Derived parameters are traced to their source and to the change made: the generation time is "sourced from [18] but refit using a log-normal incubation period with a mean of 5.2 days (SD 1.1)… rather than the incubation period used in the original study (code available here: …)".

## Results — reporting conventions
A dedicated *Reporting* subsection fixes the presentation rules once:
> "We report the median and 90% credible intervals for all measures with 20%, 50% and 90% credible intervals shown in figures."
And a distinction between estimates and estimates-from-partial-data is made visible in every figure: "we show a cut-off in figures based on the mean of all delays. Values prior to this point are defined as estimates with values past this point being defined as estimates based on partial data. In reality, this is a continuum…"

**Probabilistic statements are turned into a defined vocabulary** rather than left to the reader:
> "It was assumed that if less than 5% of samples were subcritical then an increase in cases was definite, if less than 20% … likely, if more than 80% … a decrease in cases was likely and if more than 95% … definite. For countries/regions with between 20% and 80% of samples being subcritical we could not make a statement about the likely change in cases (defined as unsure)."
The categories "definite / likely / unsure" are defined numerically before use — an excellent solution to the problem of communicating posterior probabilities to non-technical readers.

Forecasts are explicitly demoted relative to estimates:
> "These forecasts are indicative only and should not be considered with a weight equal to the real-time estimates. Changes in contact rates, mobility, and public health interventions are not accounted for which may lead to significant inaccuracy."

## Discussion and limitations
Organised as **advantages → limitations → future work → use case**, each signposted:
> "There are several advantages associated with our approach. Firstly, reported counts are the only data required, which allows our approach to be used in a wide variety of contexts."
> "Our approach is also subject to several limitations. Firstly, the model requires that the proportion of infections that are notified is constant over the 12 weeks considered."

Every limitation is followed by its *direction* and its *duration*:
> "If the true delay from onset to notification for a given country is shorter than our global delay, then we will overestimate onset case numbers, and vice versa for true delays longer than the distribution we used."
> "any changes in surveillance testing procedures will only bias the estimates temporarily if they begin to remain consistent again after they have changed."
And where nothing can be done, that is said: "Unfortunately, in the absence of data, this issue can only be explored via scenario analysis."

## Voice
Present tense for what the tool does ("We use daily counts…", "We report the median…"), past for what was fitted. First-person plural throughout. Claims about utility are hedged and framed as hope rather than assertion: "This resource may be useful for policymakers…"; "We hope that our tool will be used to support decisions in countries worldwide."

## Data, code and funding — and software availability
The most complete in the corpus, and the section is structured rather than a sentence: latest data (Harvard Dataverse), **archived data at time of publication**, licence (MIT), then `Software availability` split into *Development* (five named repositories with their roles: website front-end, scheduling framework, `EpiNow2`, `covidregionaldata`, `RtD3`) and *Archived at the time of publication* (a Zenodo DOI for each). Funder role stated: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript." Author roles are given per person using CRediT categories.

## Distinctive moves to borrow
1. **Separate "development" from "archived at time of publication"** in software availability — a live repository is not a citable artefact.
2. Define a plain-language vocabulary for posterior probabilities, numerically, before using it.
3. Put known biases in Methods when they determine how output must be read.
4. Report the previous version's choice when you change a prior, and say why.
5. State the direction of every bias, not just its existence.

## Related files
Other *real-time transmission analysis* exemplars: see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md) for an individual-based model fitted to a live national epidemic while control decisions were still being made; [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md) for district-level transmission estimates turned into beds needed during an outbreak response; [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) for a widely used R_t estimator with two failing assumptions fixed, shipped in the package the field already uses; [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md) for a natural-experiment evaluation across Chinese cities, with a mechanistic counterfactual, written under emergency time pressure; [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) for the real-time Bayesian estimate of a time-varying reproduction number, in a clinical journal's structure; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver; [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast whose corrected onsets feed a reproduction-number estimate, evaluated against later data.
