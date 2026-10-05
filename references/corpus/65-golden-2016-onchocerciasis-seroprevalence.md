# 65 — Golden et al. (2016), *Parasites & Vectors*
**"Analysis of age-dependent trends in Ov16 IgG4 seroprevalence to onchocerciasis"**
Golden A, Steel C, Yokobe L, Jackson E, Barney R, Kubofcik J, et al. *Parasit Vectors* 9:338. doi:10.1186/s13071-016-1623-1.

**Archetype:** *serological inference* in an **elimination-monitoring** setting, where the question is not how much transmission there is but whether it has stopped — and where the serological marker's own performance must be established before the model built on it means anything.

## Structure
BMC structured abstract (**Background / Methods / Results / Conclusions**) → `Keywords` → `Background` → `Methods` → `Results` → `Discussion` → `Conclusions` → electronic supplementary material.

**The paper does two things in sequence, and the order matters**: first it validates the antibody marker against a reference standard, then it fits a transmission model to the marker. A serological model inherits every weakness of its assay, so the assay is characterised first.

## Opening move
> "Diagnostics provide a means to measure progress toward disease elimination. Many countries in Africa are approaching elimination of onchocerciasis after successful implementation of mass drug administration programs as well as vector control."

**Then the question, which is about the tool rather than the disease:**
> "An understanding of how markers for infection such as skin snip microfilaria and Onchocerca volvulus-specific seroconversion perform in near-elimination settings informs how to best use these markers."

**As prevalence falls, a diagnostic's performance changes** — positive predictive value collapses, and markers of past exposure stop tracking current infection. The paper's framing is that near-elimination is a distinct measurement regime requiring its own validation, which is a transferable insight for any elimination programme.

The `Background` establishes burden and the programmes that changed it, with the donation that enabled them named: "The disease affects approximately 37 million people in Africa and the Americas; more than 500,000 people are visually impaired and 250,000 people are blinded by the disease… The donation of the anti-parasitic medicine ivermectin, by Merck… has enabled the development of large mass drug administration (MDA) programs."

## Methods
- **Describe the survey frame and the two marker types measured on the same people**: "All-age participants from 35 villages in Togo were surveyed in 2013 and 2014 for skin snip Onchocerca volvulus microfilaria and IgG4 antibody response by enzyme-linked immunosorbent assay (ELISA) to the Onchocerca volvulus-specific antigen Ov16."
- **Survey all ages, not only the sentinel group.** Onchocerciasis monitoring conventionally samples children; this paper samples everyone and shows what the extra ages buy (below).
- **Determine the positivity threshold by a model rather than a fixed cut-off**: "A Gaussian mixture model applying the expectation-maximization (EM) algorithm was used to determine seropositivity from Ov16 ELISA data." **Where a continuous assay has no agreed cut-off, fit the two underlying distributions and let the data place the boundary.**
- **Define the reference standard explicitly, as a composite**: "Performance of Ov-16 IgG4 response as a marker for infection was determined using combined PCR-positive and/or MF-positive result as a true positive within the PCR tested samples set."
- **Distinguish the two things the marker could measure**, which is the crux of the paper: antibody "as a marker for active infection, **as opposed to (current and previous) exposure to infection**". An antibody that marks lifetime exposure cannot by itself demonstrate interrupted transmission; one that marks active infection can.
- **Stratify villages by an observable before fitting**: "These villages were stratified by all-age seroprevalence into three clusters: < 15 %; 15–20 %; and > 20 %." The stratification variable is the thing a programme can measure, so the resulting model is usable operationally.

## Results
**Report both markers, in the whole population and in the sentinel age group**:
> "O. volvulus microfilaremia prevalence and Ov16 seroprevalence were, 2.5 and 19.7 %, respectively, in the total population, and 1.6 and 3.6 % in children under 11."

The gap between 19.7% seroprevalence and 2.5% microfilaraemia across all ages, against 3.6% and 1.6% in children, is the whole argument: in adults the antibody largely records historical exposure; in children it tracks current infection.

**Report diagnostic performance with the age restriction attached, and the event count that limits it:**
> "in children under 11 years of age, the anti-Ov16 IgG4 antibody response demonstrate a sensitivity and specificity of 80 and 97 %, respectively, against active infections as determined by combined PCR and microscopy on skin snips."

and, candidly, "**although in this age range there were only five true positives**."

**Report the event count behind a sensitivity estimate.** Eighty per cent of five is four; the point estimate is almost uninformative on its own, and the paper says so rather than letting the percentage stand unqualified.

**Show how the performance degrades outside the validated range**, which is what establishes the age restriction as necessary rather than arbitrary: "Both sensitivity and specificity of the Ov-16 antibody test drop as a broader age range is included in the analysis - down to 60 and 75 %."

**Compare the two reference methods against each other, and explain the discordance mechanically:**
> "More infections were detected by real-time PCR targeting the O. volvulus O-150 repeat sequence than by MF by skin snip microscopy, suggesting that PCR is more sensitive to detect active infections… Respective sensitivities for the PCR and skin snip microscopy compared to the composite PCR/MF microscopy positive results, are 80 and 66 %. Some microscopy-positive specimens were not detected by PCR, possibly as a result of using the same residual skin biopsies, which may have lost target DNA or MF through handling. All MF-positives which were missed by PCR had low (< 10) overall combined counts of MF."

The discordant cases are characterised rather than dismissed — they were the low-burden ones, which is consistent with a handling-loss explanation.

**Declare a sampling bias and withhold the affected statistic:**
> "Our sampling for the PCR analysis was biased, so relative prevalence data are not discussed."

**Say which results you are declining to report because the design does not support them.** One sentence prevents a reader from drawing the inference the data cannot carry.

**Fit a biphasic model and justify it by fit**: "Age-dependence of seroprevalence for each cluster was best reflected by a **two-phase** force-of-infection (FOI) catalytic model. In all clusters, the lower of the two phases of FOI was associated with a younger age group."

**A two-phase force of infection encodes an intervention's history**: older people were exposed under high transmission, younger people under the post-MDA regime, so one rate cannot fit both. The model's shape is a record of the programme.

**Report the parameter that orders the villages, and its direction:**
> "The age at which transition from lower to higher seroconversion, between the two phases of FOI, was found to be highest (older) for the cluster of villages with < 15 % seroprevalence and lowest (younger) for the cluster with the highest all-age seroprevalence."

The breakpoint age is itself the progress indicator: where transmission has been suppressed longest, the transition sits in older cohorts. **Derive a monotone indicator from the model that a programme can track over time.**

## Literature
Numbered BMC citations, concentrated in the `Background` on the elimination programmes and in the `Discussion` on prior assay comparisons. The literature is used to establish what the markers are known to do, which is the baseline the paper tests in a new prevalence regime.

## Voice
First-person plural and impersonal in roughly equal measure. Inference is hedged where the counts are small ("possibly as a result of", "suggesting that PCR is more sensitive"), and the central conclusion is bounded to the population studied: the marker "is an accurate marker for active infection in children under 11 years of age **in this population**."

## Discussion and limitations
Opens by characterising the infection intensities in the near-elimination setting, which is what makes the diagnostic problem hard: "the average total microfilaria counts per MF-positive participant was 12 (range 0–131) and the median was 4, with over 70 % of total microfilaria counts at less than ten counts across both biopsies per participant."

The `Conclusions` do three things in three sentences — state what the marker is good for and in whom, state what the broader age range adds operationally, and state what the clustering enabled methodologically:
> "The anti-Ov16 IgG4 antibody response is an accurate marker for active infection in children under 11 years of age in this population. Applying Ov16 surveillance to a broader age range provides additional valuable information for understanding progression toward elimination and can inform where targeted augmented interventions may be needed. Clustering of villages by all-age sero-surveillance allowed application of a biphasic FOI model to differentiate seroconversion rates for different age groups within the village cluster categories."

**The middle sentence is the policy contribution**: the extra age groups do not improve the infection estimate, but they locate where additional intervention is needed — a different and more actionable use of the same survey.

## Distinctive moves to borrow
1. **Treat near-elimination as a distinct measurement regime** in which a diagnostic's performance must be re-established.
2. **Validate the marker before modelling it**, against a defined composite reference standard.
3. **Distinguish a marker of active infection from a marker of lifetime exposure**, and say which yours is.
4. **Place a continuous assay's cut-off with a mixture model** rather than a fixed threshold.
5. **Report sensitivity and specificity with the age restriction attached**, and show how they degrade outside it.
6. **Give the event count behind a sensitivity estimate** — "only five true positives" — so the reader can discount the percentage.
7. **Compare your two reference methods against each other** and characterise the discordant cases mechanically.
8. **Declare a sampling bias and withhold the statistic it would corrupt.**
9. **Stratify by an observable the programme can measure**, so the model is operationally usable.
10. **Fit a multi-phase force of infection** where an intervention has changed transmission, and read the phases as a record of the programme.
11. **Derive a monotone indicator from the model** — here the breakpoint age — that can be tracked over time.
12. **Say what a wider sampling frame buys**, even when it does not improve the primary estimate.

## Related files
For the comparison of force-of-infection model forms see [64-ximenes-2014-hepatitis-a-foi](64-ximenes-2014-hepatitis-a-foi.md); for a single-model serosurvey with a constant force of infection see [40-prayitno-2017-dengue-seroprevalence](40-prayitno-2017-dengue-seroprevalence.md); for diagnostic performance as the subject of a modelling paper see [20-nouvellet-2015-rapid-diagnostics-ebola](20-nouvellet-2015-rapid-diagnostics-ebola.md); for age-structured immunity inferred from clinical rather than serological data see [46-griffin-2015-malaria-immunity](46-griffin-2015-malaria-immunity.md). Other *serological inference* exemplars: see [77-hay-2024-influenza-infection-histories](77-hay-2024-influenza-infection-histories.md) for lifetime infection histories reconstructed from multi-strain serology, with the estimand renamed seroincidence.
