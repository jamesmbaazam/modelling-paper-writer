# 75 — Jackson et al. (2014), *PLoS ONE*
**"The effects of school closures on influenza outbreaks and pandemics: systematic review of simulation studies"**
Jackson C, Mangtani P, Hawker J, Olowokure B, Vynnycky E. *PLoS One* 9(5):e97297. doi:10.1371/journal.pone.0097297.

**Archetype:** the *systematic review of models* — not of data. Forty-five simulation studies of one intervention are collected, their predictions extracted, and the spread of predictions explained by the assumptions behind them. The contribution is to separate what the models agree on from what depends on an assumption nobody has measured. A companion review of the epidemiological studies was published separately, and the two are designed to be read together.

## Structure
PLoS ONE structured abstract (**Background / Objectives / Methods / Results / Conclusions**) → `Introduction` → `Methods` → `Results` (peak and cumulative attack rates · epidemic duration · duration of and threshold for closure · closure strategies) → `Discussion` → a PRISMA checklist in the supporting information.

**Results are organised by outcome and by policy lever, not by study.** Each subsection collects what every model predicted about one quantity, so the reader sees the range before the explanation.

## Opening move
> "The World Health Organization currently recommends that school closures are considered as part of a mitigation strategy during an influenza pandemic. However, it has been difficult for epidemiologists and public health services to make clear recommendations to policy makers, as the impact of such closures remains unclear"

**The case for reviewing models rather than data is made from the weakness of the data**:
> "It is difficult to draw conclusions on the effectiveness of school closures from epidemiological data. Observational studies frequently vary in factors studied, such as the timing and duration of closure, case definitions, and population covered. In addition, other interventions have often been used concurrently with school closures. Consequently, mathematical modelling has increasingly been used to predict the effects of school closure on influenza outbreaks."

## Methods
- **Define what a model must allow to be included**: studies "were included if they modelled school closures during an influenza outbreak and allowed comparison of baseline simulations with no intervention (or a specified intervention) to simulations in which schools were closed." A review of models needs a comparator inside each model, and this sets it.
- **Draw the boundary with the neighbouring evidence explicitly**: models that estimated the effect of closures during a particular outbreak were excluded — "Such studies (which are included in another review) are useful in informing assumptions made in transmission models, but are beyond the scope of this review of predictive modelling studies."
- **Define each extracted outcome as a formula**, so studies reporting in different forms can be put on one scale: the percentage reduction in peak incidence "defined as 100×((peak in the absence of school closure – peak with school closure)/peak in the absence of school closure)", and likewise for the cumulative attack rate.
- **Extract the range, not only the headline**: where a study reported several scenarios, "the most extreme values derived for each value of viral transmissibility were extracted and presented along with the estimate derived from the main analysis." **In a review of models, the range each model produced is data; extract it.**
- **Extract the assumption most likely to drive the answer** — the assumed effect of closure on contact patterns — and record whether it was based on data. The answer frames the review: it "varied between studies and was rarely based on empirical data."

## Results
**Report the typical range and the outliers in one sentence**: "Predictions of the reduction in the peak incidence were typically 20–60%… but some studies predicted much larger reductions of ≥90%" The abstract keeps the same discipline: reductions "were frequently 20–60% but some studies predicted >90% reductions or even increases under certain assumptions".

**Plot every prediction grouped by its key assumption.** Figures 1 and 2 show each study's estimate with symbols for R₀ and panels for whether household and community contacts were assumed to rise, stay unchanged, follow empirical data or go unstated. The grouping turns a scatter of numbers into an argument about why they differ.

**Explain each outlier by the assumption that produced it**:
> "Only two studies predicted that the peak incidence might increase markedly under some circumstances following school closures, e.g. by 27% if school closures caused a doubling in the number of contacts in the household and community, or by 13% if school systems were closed for two weeks at a prevalence of 1% in the general population (and if R 0 was 2.4). As the authors discuss, these increases appeared to result from the assumptions that school closure occurred early and briefly or that they resulted in children doubling their numbers of contacts"

**Summarise the qualitative findings in a table of directions** (Table 1): for each factor, the direction in which it moves the effect of closure — higher R₀, smaller effect; higher attack rates in children, larger effect — "assuming that factors other than those specified remain unchanged". Where models disagreed, the table says so: "Results differed between models".

## Literature
Numbered citations, with the 45 included studies tabulated in the supporting information. The Discussion sets the model predictions against the epidemiological estimates — studies "have estimated that school closures have reduced the total number of cases of pandemic influenza by 28%, 35% and 52% in Calgary, Edmonton, and the province of Alberta" — and notes that these sit "towards the lower end of those predicted by the simulation studies".

## Voice
First-person plural, past tense, cautious throughout: "predicted", "usually", "typically", "appeared to result from". The review never states a model result as a fact about the world.

## Discussion and limitations
**Separate the robust qualitative result from the fragile quantitative one**:
> "Despite the marked quantitative differences in the model estimates, some qualitative results were consistent across many studies. For example, the reduction in peak incidence was consistently predicted to be larger than that in the cumulative attack rate, since the reduction in contact resulting from school closure slows, rather than eliminates, transmission."

**Then draw the policy goal from the robust result**: "Such a reduction in the peak burden on health services could be highly beneficial if demand for intensive care and other services is high… This may be a more attainable goal of school closure than a reduction in the cumulative attack rate."

**Name the assumption that limits the whole literature, and what would fix it**:
> "Although many of the models' assumptions relating to the natural history of influenza and human population structure were based on empirical data, a range of assumptions have been made regarding population contact patterns. This is an important limitation of much of the published literature, as predictions of the effects of school closure depend upon the amount of contact (and therefore transmission) between individuals whilst schools are closed and while they are open."

**Use external data to judge which models to believe**: the only study predicting large increases in both peak and cumulative attack rates did so only under an assumption "which is inconsistent with findings to date from published contact studies; it therefore appears unlikely that school closures would dramatically increase attack rates."

**Propose a structural remedy for the field**: "Development of a consensus "baseline" scenario, in which the natural history and behavioural parameters were set at agreed values and which models could use in simulating outbreaks in the absence of interventions, could help to facilitate comparison of results from different models".

**Position the two evidence streams as complements, not rivals**: epidemiological studies "report on events during particular outbreaks without making assumptions about individuals' behaviour or the properties of the causative virus", while predictive models "are able to investigate which factors… influence the effectiveness of a school closure policy. The two sources of evidence – epidemiological studies and simulation studies – are therefore complementary."

**Check that the review is not out of date**: "Several simulation studies published since then meet the inclusion criteria but do not affect the conclusions of the review".

## What to avoid from this paper
- **Single-reviewer screening**: abstracts "were screened initially by one reviewer; a second reviewer assessed any paper whose usefulness or findings were unclear to the first reviewer." Dual independent screening is the PRISMA expectation.
- **No appraisal of model quality.** Studies are weighted equally whatever their calibration or validation; a review of models can grade them, for instance by whether the contact assumption was data-based, and here that grouping is used descriptively but not as a weight.

## Distinctive moves to borrow
1. **Argue for reviewing models from the weakness of the observational evidence.**
2. **Require a within-model comparator** as an inclusion criterion.
3. **Define every extracted outcome as a formula** so studies share a scale.
4. **Extract each model's range**, not only its headline.
5. **Extract the driving assumption and whether it was data-based.**
6. **Plot all predictions grouped by that assumption.**
7. **Explain each outlier by the assumption that produced it.**
8. **Tabulate directions of effect**, and say where models disagree.
9. **Separate the qualitative consensus from the quantitative spread**, and draw the policy goal from the consensus.
10. **Judge models against external data** on their key assumption.
11. **Propose a consensus baseline scenario** so future models can be compared.
12. **Present models and observational studies as complements**, with a companion review of the other.

## Related files
For school closures and other interventions in individual-based pandemic models see [12-ferguson-2006-mitigating-pandemic](12-ferguson-2006-mitigating-pandemic.md); for the influence of contact assumptions on model conclusions see [68-ajelli-2010-abm-vs-metapopulation](68-ajelli-2010-abm-vs-metapopulation.md); for 37 models re-implemented and compared on one decision see [23-li-2017-essential-information-ebola](23-li-2017-essential-information-ebola.md). Other *review* exemplars: see [05-altizer-2006-seasonality-review](05-altizer-2006-seasonality-review.md) for a review that inventories the distinct mechanisms through which one driver, seasonality, acts; [15-heesterbeek-2015-models-global-health](15-heesterbeek-2015-models-global-health.md) for the field-defining review of what modelling can and cannot do for global health; [14-baker-2021-infectious-disease-global-change](14-baker-2021-infectious-disease-global-change.md) for a synthesis review whose contribution is a framework for a scattered literature.
