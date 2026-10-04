# 62 — Grubaugh et al. (2017), *Nature*
**"Genomic epidemiology reveals multiple introductions of Zika virus into the United States"**
Grubaugh ND, Ladner JT, Kraemer MUG, Dudas G, Tan AL, Gangavarapu K, et al. *Nature* 546(7658):401–405. doi:10.1038/nature22400.

**Archetype:** *phylodynamics / genomic epidemiology*, with the question framed around **introductions rather than spread** — when did transmission start, how many times did the virus arrive, and from where. The corpus's exemplar of **combining genomes with mosquito surveillance and travel data** so that three independent data streams corroborate one conclusion.

## Structure
*Nature* Letter: one-paragraph `Abstract` → unheaded continuous argument with figure callouts → `Methods` at the end, organised as the field-to-analysis pipeline (*Ethical statement* · *Florida Zika virus case data* · *Clinical sample collection and RNA extraction* · sequencing · phylogenetics · travel and mosquito analyses) → `Data availability` → Extended Data.

**The Methods are a chain of custody.** They begin with ethics and the surveillance system, move through specimen collection, and only then reach sequencing — appropriate when samples came from an outbreak response rather than a study.

## Opening move
> "Zika virus (ZIKV) is causing an unprecedented epidemic linked to severe congenital syndromes. In July 2016, mosquito-borne ZIKV transmission was reported in the continental United States and since then, hundreds of locally-acquired infections have been reported in Florida."

Then the aims, stated as three questions with the two data types that will answer them:
> "To gain insights into the timing, source, and likely route(s) of ZIKV introduction, we tracked the virus from its first detection in Florida by sequencing ZIKV genomes from infected patients **and Aedes aegypti mosquitoes**."

**Sequencing the vector as well as the patients** is the design decision that distinguishes this paper, and it is in the first sentence of the aims.

## Methods
- **Describe the surveillance system that generated the cases**, by name and by process: weekly reports "obtained from the Florida DOH mosquito-borne disease surveillance system", with symptom-onset dates for the transmission zones "determined by the Florida DOH investigation process".
- **Explain every judgement call about ambiguous cases**, so the counts are auditable: "The one local ZIKV infection diagnosed in Duval County was believed to have originated elsewhere in Florida. Therefore, this case is listed as 'unknown origin' in Fig. 1b." And for the travel figure: "only the countries visited by 5 or more times by ZIKV-infected travelers diagnosed in Florida are shown. Countries with 5 or fewer visits were aggregated into an 'other' category by region."
- **State the ethics route for outbreak-response specimens** in full, including why consent was waived and the regulatory category:
  > "This work was conducted as part of the public health response in Florida and samples were collected under a waiver of consent granted by the Florida DOH Human Research Protection Program. The work received a non-human subjects research designation (category 4 exemption) by the Florida DOH since this research was performed with leftover clinical diagnostic samples involving no more than minimal risk. All samples were deidentified prior to receipt by the study investigators."
- **Report the mosquito surveillance effort as numbers, including the negative result**: "A total of 24,306 Ae. aegypti and 45 Ae. albopictus were collected… Up to 50 mosquitoes of the same species and trap night were pooled together for ZIKV RNA testing. The infection rates were calculated using a maximum likelihood estimate (MLE). **None of the Ae. albopictus pools contained ZIKV RNA.**"
- **Say what the maps were made with, and that the basemaps are open**: "The maps presented in our figures were generated using Matplotlib and ESRI basemaps… The software and basemaps are open source and 'freely available to anyone'."

## Results
**Report the introduction count as a range bounded by what the data can support:**
> "We show that at least four introductions, but potentially as many as 40, contributed to the outbreak in Florida and that local transmission likely started in the spring of 2016 - several months before initial detection."

The construction *at least four, potentially as many as 40* is an honest statement of an identifiability limit: the phylogeny places a floor on the number of introductions, and sampling fraction places a ceiling. **Give the bound the data supports, not a point estimate the data cannot support.**

**State the cryptic-transmission finding with its magnitude in time** — local transmission began "several months before initial detection" — which is the operationally important result for a surveillance system.

**Corroborate the genomic inference with two independent data streams:**
> "Our analyses show that most introductions are linked to the Caribbean, a finding corroborated by the high incidence rates and traffic volumes from the region into the Miami area."

Genomes say where the lineages came from; incidence data says where the virus was circulating; traffic data says where the people came from. **Three independent streams agreeing is a much stronger claim than any one of them.**

**Quantify the travel exposure that makes the location special**: "We estimated that Miami and nearby Fort Lauderdale received ~72% of traffic and Miami received more air and sea traffic from ZIKV endemic areas than any other city in the United States."

**Rule out the obvious alternative explanation using a comparison region**:
> "By June, most of Florida and several cities across the South likely supported high Ae. aegypti populations … however, most of this region has not reported local Ae. aegypti-borne virus transmission in at least 60 years. In fact, the only region outside of Florida with local ZIKV transmission is southern Texas, which is also the only other region with recent DENV outbreaks."

Mosquito abundance alone does not explain the outbreak, because many places have the mosquitoes and no transmission. **Then the conclusion is stated as a conjunction of conditions**, not a single cause: "the combination of travelers, mosquito ecology, and human population density likely make Miami one of the few places in the continental United States at risk."

**Reconcile two findings that appear to conflict** — many introductions, yet an outbreak — with the parameter that connects them:
> "Despite this, we estimated that the average R₀ was less than 1 and therefore multiple introductions were necessary to give rise to the observed outbreak."

**R₀ < 1 and a sustained outbreak are only compatible under repeated importation**, and saying so turns the introduction count from a descriptive statistic into the explanation.

**Compare against the related endemic pathogen to make the scale legible**, and explain the difference: "more reported ZIKV cases in 2016 (256) than DENV cases since 2009 (136). This case difference may be reflected by lower incidence of endemic DENV than epidemic ZIKV in source countries, resulting in fewer DENV importations (reported travel cases since 2009: 654 DENV and 1,016 ZIKV)."

**Acknowledge the ascertainment problem explicitly where it bites**: "Given that the majority of ZIKV infections are asymptomatic, the true number of ZIKV cases was likely much higher."

**Derive a forecast from the mechanism**, which is what makes the paper useful beyond the episode:
> "Because Florida is unlikely to sustain long-term ZIKV transmission, the potential for future ZIKV outbreaks in this region is dependent upon activity elsewhere. Therefore, we expect that outbreaks in Florida will cycle with the ZIKV transmission dynamics in the Americas."

If R₀ < 1 locally, local outbreaks are a function of foreign incidence — a prediction that follows directly from the estimated parameter and tells surveillance where to look.

**Give an operational recommendation that falls out of a correlation**: "The number of weekly ZIKV cases (based on symptoms onset) was correlated with mean Ae. aegypti abundance per trap night determined from the same week and zone (Spearman r = 0.61). This suggests that when the virus is present, mosquito abundance numbers alone could be used to target control efforts."

## Literature
Numbered *Nature* citations, dense and compressed. Prior work establishes the vector ecology, the regional spread timeline, and the precedent of DENV and CHIKV outbreaks in the same counties — which is what licenses the comparison used to rule out mosquito abundance as a sufficient explanation.

## Voice
First-person plural, past tense. Inference verbs are graded tightly to the evidence: "at least four… but potentially as many as 40", "likely started", "most introductions are linked to", "likely provided", "we expect that". Every claim about an unobserved event carries a hedge; the counts and traffic volumes do not.

## Data, code and funding
Sequence data under two named NCBI BioProjects with per-sample GenBank accessions in a supplementary table; remaining data in Extended Data or on request. Ethics covers both the human samples and the public health context. The map provenance and licence are stated.

## Distinctive moves to borrow
1. **Frame the question as introductions, timing and source** when a pathogen is newly arrived, rather than as transmission dynamics.
2. **Sequence the vector as well as the patients**, and say so in the aims.
3. **Report the introduction count as a bounded range** — a floor from the phylogeny, a ceiling from sampling — rather than a point estimate.
4. **State how long transmission preceded detection.** That is the finding a surveillance system can act on.
5. **Corroborate a genomic inference with independent streams** — incidence in source regions and passenger traffic.
6. **Rule out a necessary-but-not-sufficient explanation with a comparison region** that has the condition and not the outcome.
7. **State the conclusion as a conjunction of conditions**, not a single cause.
8. **Reconcile apparently conflicting findings with the parameter that connects them** — R₀ < 1 plus repeated importation.
9. **Compare with the related endemic pathogen** and explain the difference through importation pressure.
10. **Derive a forecast from the mechanism**: if local R₀ < 1, local risk tracks foreign incidence.
11. **Explain every judgement call about ambiguous cases** so the counts are auditable.
12. **Give the full ethics route for outbreak-response specimens**, including the waiver and exemption category.
13. **Report the negative surveillance result** — no virus in the secondary vector — with the sampling effort behind it.

## Related files
For genomic epidemiology used to assess an elimination campaign see [39-geoghegan-2020-sars-cov-2-genomics-nz](39-geoghegan-2020-sars-cov-2-genomics-nz.md), which partitions introductions by outcome; for superspreading inferred from the same kind of data see [63-lemieux-2021-boston-superspreading](63-lemieux-2021-boston-superspreading.md); for *Aedes*-borne risk mapping from covariates see [29-bhatt-2013-global-dengue-distribution](29-bhatt-2013-global-dengue-distribution.md); for importation-driven dynamics in a non-genomic setting see [17-grenfell-2001-travelling-waves](17-grenfell-2001-travelling-waves.md) and [18-bjornstad-2002-tsir-measles](18-bjornstad-2002-tsir-measles.md).
