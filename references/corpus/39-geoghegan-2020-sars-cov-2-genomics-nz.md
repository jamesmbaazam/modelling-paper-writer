# 39 — Geoghegan et al. (2020), *Nature Communications*
**"Genomic epidemiology reveals transmission patterns and dynamics of SARS-CoV-2 in Aotearoa New Zealand"**
Geoghegan JL, Ren X, Storey M, Hadfield J, Jelley L, Jefferies S, et al. *Nat Commun* 11:6351. doi:10.1038/s41467-020-20235-8.

**Archetype:** the *phylodynamics / genomic epidemiology* paper — sequence a large share of an outbreak's cases, reconstruct introductions and transmission lineages from the phylogeny, and use the genomic reconstruction to answer an epidemiological question the case data alone cannot.

## Structure
*Nature Communications*: one-paragraph `Abstract` → a separate **editor's one-sentence summary** → `Introduction` → **`Results and discussion`** (merged) → `Methods` (at the end, pipeline-ordered) → `Data availability` → `Acknowledgements` → author contributions → peer-review file.

**Merging Results and Discussion is the right choice here** and worth copying when each finding needs interpreting as it lands: a lineage count means nothing until you say what it implies about border control. The paper interprets inline and never repeats itself in a separate section.

**Methods are ordered as the laboratory-and-analysis pipeline**: *Ethics statement* → *Genomic sequencing of SARS-CoV-2* → phylogenetic analysis → lineage assignment → R_e estimation. Each stage is independently auditable, which is the same convention the ML papers use (`ml-prediction.md` §7.2).

## Opening move
> "New Zealand is one of a handful of countries that aimed to eliminate coronavirus disease 19 (COVID-19)."

One sentence establishing why this outbreak is scientifically interesting rather than merely another national dataset. The abstract does the same with geography doing the work: "New Zealand, a geographically remote Pacific island with easily sealable borders, implemented a nationwide 'lockdown' of all non-essential services to curb the spread of COVID-19."

**The aims are stated as a list of four, in one sentence, with the data that will answer them:**
> "To investigate the origins, time-scale and duration of virus introductions into New Zealand, the extent and pattern of viral spread across the country, and to quantify the effectiveness of intervention measures, we generated whole-genome sequences from 56% of all documented SARS-CoV-2 cases from New Zealand and combined these with detailed epidemiological data."

**Lead with sampling fraction, not sample size.** "56% of all confirmed cases" tells a reader what inferences are supportable; "649 genomes" does not. Genomic epidemiology papers live or die on this number and it appears in the abstract, the Introduction and the Results.

## Methods
- **State the sampling denominator and its unevenness, then show the unevenness did not matter**: "DHBs submitted between 0.1 and 81% of their positive samples to the Institute of Environmental Science and Research (ESR), Wellington, for sequencing. Despite this disparity, a strong nationwide spatial representation was achieved." The disparity is reported first, with its range, and the reassurance is backed by a figure correlating cases and genomes per district.
- **Define an operational category that readers will otherwise misread**: "A 'probable case' means a person who has been classified as such by the medical officer of health based on exposure history and clinical symptoms, and who has either returned a negative laboratory result or could not be tested."
- **Name every tool with its version, in pipeline order** — ARTIC medaka pipeline (v1.1.0), trimmomatic (v0.36), Burrows–Wheeler Aligner, iVar (v1.2), Picard (v2.10.10), bcftools mpileup (v1.9), vcflib (v1.0.0) — and give the **numeric quality thresholds that decide what becomes data**: "SNPs were quality trimmed using vcflib (v 1.0.0) requiring 20× depth and overall quality of 30. Positions that were <20× were masked to N in the final consensus genome. Positions with an alternative allele frequency between 20 to 79% were also masked to N."
- **Report attrition from samples received to sequences analysed**: "A total of 733 laboratory-confirmed samples of SARS-CoV-2 were received by ESR for whole-genome sequencing… In total, 649 sequences passed our quality control."
- **Point at the pipeline rather than paraphrasing it**: "Steps included in the pipeline are described in detail online (https://github.com/ESR-NZ/NZ_SARS-CoV-2_genomics)."
- **Report the key model parameter as an estimate with an interval, and interpret it**: "The sampling proportion of this cluster, a key parameter of the model, had a mean of 0.75 (95% CI: 0.4–1), suggesting sequencing captured the majority of cases in this outbreak." In phylodynamics the sampling proportion is where the inference is most fragile, so it is stated rather than buried.

## Results
**Convert the phylogeny into epidemiological counts that a public health reader can act on.** The central result is a partition of introductions by what they led to:
> "Despite the small size of the New Zealand outbreak, there were 277 separate introductions of the virus out of the 649 cases considered. Of these, we estimated that 24% (95% CI: 23–30) led to only one other secondary case (i.e. singleton) while just 19% (95% CI: 15–20) of these introduced cases led to ongoing transmission, forming a transmission lineage (i.e. onward transmission to more than one individual…). The remainder (57%) did not lead to a transmission event."

Three categories that sum to 100%, each defined inline, each with an interval. **A phylogeny is not a result; a partition of introductions by outcome is.**

**State the counter-intuitive finding and give its mundane explanation immediately**: "New Zealand transmission lineages most often originated in North America, rather than in Asia where the virus first emerged, likely reflecting the high prevalence of the virus in North America during the sampling period."

**Rule out the alternative explanation for a frequency shift** — the move that separates genomic epidemiology from genomic description:
> "it is noteworthy that the increase in glycine in New Zealand samples is due to multiple importation events of this variant rather than selection for this mutation within New Zealand."

A variant rising in frequency can be selection or repeated importation; the paper says which, and that is a claim only genomic data can make.

**Report a negative finding that closes off a live public question**: "By examining the time of the most recent common ancestor, or TMRCA, of the samples, we found no evidence that the virus was circulating in New Zealand before the first reported case on 26 February."

**Report a surveillance performance metric derived from the genomes**, with its definition inline: "we found that detection was more efficient (i.e. fewer cases were missed) later in the epidemic in that the detection lag (the duration of time from the first inferred transmission event to the first detected case) declined with the age of transmission lineages."

**Quantify the intervention on the one cluster where the data support it**, with both endpoints and intervals:
> "Its effective reproductive number, R_e, decreased over time from 7 at the beginning of the outbreak (95% credible interval, CI: 3.7–10.7) to 0.2 (95% CI: 0.1–0.4) by the end of March."

Note the restraint: R_e is estimated for the largest cluster, not for the country, because that is the unit the phylodynamic model can support.

**Show what the genomics added over the existing investigation, as a count**: "analysis of genomic data has linked five additional cases to this cluster that were not identified in the initial epidemiological investigation, highlighting the added value of genomic analysis." A methods-advocacy claim backed by a number from this study rather than asserted in the Discussion.

**Tie the micro-scale to the national scale explicitly**: "This cluster, seeded by a single-super spreading event that resulted in New Zealand's largest chain of transmission, illustrates the link between micro-scale transmission to nationwide spread."

## Literature
Numbered superscript citations, *Nature* style, sparse in the Results and clustered in the Introduction. Prior work is used to license interpretation rather than to review the field: "Preliminary studies suggest that the D614G mutation can enhance viral infectivity in cell culture and phylodynamic approaches have shown an increase in growth and size of lineages with this mutation" — the hedge "preliminary" is doing real work before the paper's own contrary finding about importation.

A comparator country is named to make the design legible: "from strong population lockdowns such as that used in New Zealand, to countries like Sweden that limited the sizes of social gatherings… but which did not impose a strict lockdown."

## Voice
First-person plural and past tense for the work ("we generated", "we sequenced", "we estimated", "we found no evidence"), present for standing implications. Inference verbs are graded to the evidence: epidemiological attribution is "most likely originated in the USA"; a mechanism is "probably initiated by a super spreading event"; a pattern is "likely reflecting"; and the aggregate claim is "suggests that implementing a strict and early lockdown in New Zealand rapidly reduced multiple chains of virus transmission". Nothing is said to be proven.

## Discussion and limitations
The interpretation is distributed through `Results and discussion` and gathered in a closing paragraph that combines the verdict with a forward-looking operational recommendation:
> "The marked decrease in R_e of this large cluster coupled with the relatively low number of virus introductions that resulted in a transmission lineage suggests that implementing a strict and early lockdown in New Zealand rapidly reduced multiple chains of virus transmission. As New Zealand continues its goal to eliminate COVID-19 community transmission, but with positive cases still detected amongst individuals quarantined at the border reflecting high virus incidence in other localities, it is imperative that ongoing genomic surveillance is an integral part of the national response to monitor any re-emergence of the virus, particularly when border restrictions might eventually be eased."

The limitations are carried inline where each result appears — uneven sequencing by district, the sampling proportion as "a key parameter of the model", the weak temporal signal ("we also inferred a weak yet significant temporal signal in the data, reflecting the low mutation rate of SARS-CoV-2") — rather than collected into a paragraph. For a short, merged-section paper this is defensible; for a longer one, collect them.

## Data, code and funding
A model availability statement for genomic work: raw data under a named BioProject accession and on GISAID, with the accession list as supplementary data; case data pointed at their public source; and analysis code in a separate public repository — "Phylogenetic tree files and code used to analyse them are available online (https://github.com/sebastianduchene/summarise_importations)." Ethics and consent are covered by a statement naming the approval route and de-identification: "All samples were de-identified before receipt by the researchers. Under contract for the Ministry of Health, ESR has the approval to conduct genomic sequencing for surveillance of notifiable diseases."

Per-author contributions are itemised, funders are listed with grant numbers, and the diagnostic laboratories and public health units that supplied samples and epidemiological data are thanked by role.

## Distinctive moves to borrow
1. **Lead with the sampling fraction, not the sample size.** It is the number that bounds every inference in a genomic epidemiology paper.
2. **Partition introductions by outcome** — singleton, transmission lineage, dead end — into categories that sum to 100%, each defined inline with an interval.
3. **Distinguish importation from selection** when a variant's frequency changes. That distinction is the paper's reason to exist.
4. **Report the sampling proportion the phylodynamic model assumed**, with its interval, and say what it implies about coverage.
5. **Give the quality thresholds that decide what becomes data** — depth, quality score, allele-frequency masking — and the attrition from samples received to sequences analysed.
6. **Count what the genomics added** over the conventional investigation (five extra linked cases), rather than asserting added value.
7. **Estimate R_e only for the unit the data support** — here one cluster — and say so by naming the cluster.
8. **Report the negative finding** that closes a live public question (no cryptic circulation before the first case).
9. **Define operational categories** like "probable case" where a reader would otherwise assume.
10. **Merge Results and Discussion** when each finding needs interpreting as it lands, and then do not repeat them.

## Related files
For the real-time transmission analyses this complements see [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) and [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md); for R_t estimation from case data alone see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md) , [27-gostic-2020-practical-considerations-rt](27-gostic-2020-practical-considerations-rt.md) and [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md); for the spatial-introduction framing without genomes see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md). Other *phylodynamics / genomic epidemiology* exemplars: see [62-grubaugh-2017-zika-introductions](62-grubaugh-2017-zika-introductions.md) for introductions, timing and source corroborated by genomes, mosquito surveillance and travel data; [63-lemieux-2021-boston-superspreading](63-lemieux-2021-boston-superspreading.md) for two superspreading events compared by what they went on to seed.
