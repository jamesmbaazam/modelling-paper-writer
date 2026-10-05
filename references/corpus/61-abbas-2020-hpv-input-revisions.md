# 61 — Abbas et al. (2020), *The Lancet Global Health*
**"Effects of updated demography, disability weights, and cervical cancer burden on estimates of human papillomavirus vaccination impact at the global, regional, and national levels: a PRIME modelling study"**
Abbas KM, van Zandvoort K, Brisson M, Jit M. *Lancet Glob Health* 8(4):e536–e544. doi:10.1016/S2214-109X(20)30022-X.

**Archetype:** *vaccine impact*, and an unusual sub-type — the paper's subject is **how much the answer moves when the inputs are updated**. Nothing about the model structure changes; three external data sources are refreshed and the consequences are attributed to each. The corpus's exemplar of **auditing an existing model rather than building a new one**.

## Structure
Lancet structured abstract → **`Research in context`** panel → `Introduction` → `Methods` (including *Role of the funding source*) → `Results` → `Discussion`. Extensive appendices carry the global, regional and national estimates — the national results run to a second appendix file.

**The title states the inputs, the outputs and the model by name**, which is exactly right for a paper whose contribution is a revision: a reader of the earlier PRIME work knows immediately whether this supersedes their numbers.

## Opening move
> "Cervical cancer has the fourth greatest global burden of cancer among women for both incidence and mortality, and is the leading cause of cancer death among women in 42 countries. WHO estimated that 570 000 new cases occurred and 311 000 women died from cervical cancer globally in 2018, with nearly 90% of these deaths occurring in low-income and middle-income countries."

Burden with rank, counts, year and the distributional fact that drives the equity argument. The biology is then given with the attributable fractions that make vaccine choice meaningful: the vaccines protect against "HPV 16/18 genotypes, which cause 70% of all cervical cancers. In addition to HPV 16/18, the nonavalent vaccine also protects against high-risk HPV types 31/33/45/52/58 which cause 18·5% of HPV-positive cervical cancers."

**Anchor the analysis to the policy target it informs**, named with its owner and date: "In May, 2018, the WHO Director-General called for global action to eliminate cervical cancer as a public health problem… The proposed 90–70–90 targets for 2030 comprise 90% coverage o[f vaccination]…"

**The `Research in context` panel states what the model already established and what has changed since** — the cleanest possible justification for a revision:
> "PRIME was developed in 2014 in collaboration with WHO… It was used to show that vaccinating 12-year-old girls against HPV was cost-effective in almost every country for the bivalent and quadrivalent vaccines. Since its development and the introduction of a nonavalent vaccine in 2014, new data and methods for demography from the UN World Population Prospects 2019 revision, disability weights from the Global Burden of Disease 2017 study, and cervical cancer burden from the Global Cancer Incidence, Mortality and Prevalence 2018 database have become available, and were used to update the model."

**The gap is the age of the inputs, not a flaw in the method.** A paper can be justified by the obsolescence of its predecessor's data, and saying so plainly is more honest than manufacturing a methodological novelty.

## Methods
- **Name each updated input with its source, version and year** — three sources, each pinned: "population demography of the UN World Population Prospects (UNWPP) 2019 revision, disability weights of the Global Burden of Disease (GBD) 2017 study, and cervical cancer burden from the Global Cancer Incidence, Mortality and Prevalence (GLOBOCAN) 2018 database."
- **State the scenario grid exhaustively in one sentence**: "We estimated the lifetime health benefits for bivalent or quadrivalent and nonavalent vaccination of 9-year-old and 12-year-old girls at 90% coverage during 2020–29 in 177 countries." Two vaccine types × two ages × one coverage × a defined decade × a country count.
- **Define the counterfactual and the output units together, including the inverted metric**:
  > "Health impact was presented in terms of cervical cancer cases, deaths, or disability-adjusted life-years (DALYs) averted per 1000 vaccinated girls in comparison with the counterfactual scenario of no vaccination, and **the number of girls needed to be vaccinated to prevent a single case, death, or DALY**."

  **Report the number-needed-to-vaccinate alongside the rate averted.** It is the same information inverted, but it is the form a programme manager and a health economist each recognise, and it maps directly onto cost per outcome.
- **Attribute the change to each input separately, not only in combination.** The headline result is a decomposition, which is only possible because the updates were applied one at a time as well as together.
- ◆ **Include the Lancet-mandated funding-role statement**: "The funders of this study had no role in study design, data collection, data analysis, data interpretation, or writing of the manuscript. All authors had full access to data in the study, and final responsibility for the decision to submit for publication."

## Results
**Report the change from the previous estimates as the headline, per outcome:**
> "In estimating the health impact of HPV vaccination of 9-year-old girls, the combined updates to demography, disability weights, cervical cancer burden estimates resulted in a 26% increase in the estimated number of cases averted, a 51% increase in deaths averted, and a 72% increase in DALYs averted per 1000 vaccinated girls for both the bivalent or quadrivalent and nonavalent vaccines, compared with previous estimates."

Three outcomes, three different magnitudes of revision — 26%, 51%, 72% — which tells a reader that the update does not shift everything uniformly, and that the metric they care about determines how much their previous number was wrong.

**Then give the new absolute estimates**, so the paper is usable and not only a correction: "the bivalent or quadrivalent HPV vaccine was estimated to avert 15 cases, 12 deaths, and 243 DALYs per 1000 vaccinated girls, and the nonavalent HPV vaccine was estimated to avert 19 cases, 14 deaths, and 306 DALYs per 1000 vaccinated girls."

**Name which input dominated, and explain the mechanism:**
> "We found that the demography update from the WHO 2009 life tables to the UNWPP 2019 revision was the major driver for change in the health impact estimates of PRIME, in comparison with the updates to disability weights or cervical cancer burden estimates. Because UNWPP mortality estimates are declining over time and incorporate population aging (unlike static WHO life tables), using UNWPP 2019 estimates led to an increasing life expectancy among women and a subsequent increase in lifetime risk of cervical [cancer]."

**A demographic assumption, not an epidemiological one, turned out to drive the vaccine impact estimate.** Women living longer are at risk for longer, so more cancers are preventable. Static life tables understate that, and the paper traces the whole chain from data source to conclusion.

**Draw out the double consequence for decision-makers**: "HPV vaccination both provides greater health benefits and is more cost-effective than was previously estimated" — with the reasoning given in both directions, "because the number of girls needed to be vaccinated to prevent a single case, death, or DALY are lower than previous forecasts" and "because the number of cases, deaths, and DALYs averted per vaccinated girl is higher than our earlier estimates."

**Convert the regional finding into a prioritisation, ranked:**
> "because of a higher burden of cervical cancer before vaccination in the WHO African region compared with other regions, HPV vaccination will provide the greatest relative health benefits in this region and the countries within this region should be prioritised for HPV vaccine introduction and scale-up. Based on WHO-initiated guidance on priority setting in health care, the African region has the greatest potential to benefit from HPV vaccination, followed by the South-East Asia region, the region of the Americas, Western Pacific region, European region, and Eastern Mediterranean region."

A complete ordering of all six WHO regions, tied to published priority-setting guidance rather than to the authors' judgement.

## Literature
Numbered Lancet citations, sparse. The paper's own predecessor is the main reference point, and WHO guidance documents are cited as the policy frame. The data sources are treated as citable objects in their own right, with version and year — appropriate when they are the subject of the paper.

## Voice
First-person plural, past tense for the work and future for the policy implication ("will provide the greatest relative health benefits", "should be prioritised"). The comparative framing — *greater than previously estimated*, *lower than previous forecasts* — runs through every results sentence, which keeps the reader oriented to the fact that this is a revision.

## Discussion and limitations
Opens by restating exactly what was updated and over what scenario grid, then the direction of the change and its two consequences, then the regional prioritisation.

**The principal limitation is a structural property of the model, stated plainly** and inherited rather than introduced: PRIME "includes only direct effects of HPV vaccination and excludes indirect herd effects."

For a vaccine against a sexually transmitted infection, excluding herd effects is a substantial and conservative simplification — vaccinating girls protects unvaccinated people too — so the impact estimates are lower bounds. **When a limitation makes your estimate conservative, say which way it runs**; this paper names the omission clearly, though it would be stronger still for stating the direction explicitly.

## Distinctive moves to borrow
1. **Justify a paper by the obsolescence of its predecessor's inputs**, stated plainly in the evidence-before-this-study panel.
2. **Put the model name, the inputs and the outputs in the title** when the contribution is a revision.
3. **Pin every data source with its version and year**, and treat the sources as the subject.
4. **Decompose the change by input**, not only in combination, and name which one dominated.
5. **Trace the mechanism from data source to conclusion** — static life tables understate ageing, ageing raises lifetime risk, raised risk raises preventable burden.
6. **Report both the revision and the new absolute estimates**, so the paper is usable as well as corrective.
7. **Give the change per outcome** when the revision moves them by different amounts.
8. **Report number-needed-to-vaccinate alongside the rate averted** — the same fact in the two forms different readers use.
9. **State the scenario grid exhaustively in one sentence** before any result.
10. **Convert a regional finding into a complete ranked prioritisation**, tied to published guidance rather than to your own judgement.
11. **Anchor the analysis to a named policy target with its owner and date.**
12. **Name an inherited structural limitation** of the model you are updating, even though it is not yours.

## Related files
For the global vaccine impact exemplar with explicit counterfactual reasoning see [60-watson-2022-covid-vaccination-impact](60-watson-2022-covid-vaccination-impact.md); for impact carried through to an ICER against a threshold see [38-chen-2019-pneumococcal-cost-effectiveness](38-chen-2019-pneumococcal-cost-effectiveness.md); for campaign-schedule optimisation from a transmission model see [49-verguet-2015-measles-sia](49-verguet-2015-measles-sia.md); for the value-of-information framing of which input to improve see [23-li-2017-essential-information-ebola](23-li-2017-essential-information-ebola.md).
