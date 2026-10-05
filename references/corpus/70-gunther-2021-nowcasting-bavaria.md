# 70 — Günther et al. (2021), *Biometrical Journal*
**"Nowcasting the COVID-19 pandemic in Bavaria"**
Günther F, Bender A, Katz K, Küchenhoff H, Höhle M. *Biom J* 63(3):490–502. doi:10.1002/bimj.202000112.

**Archetype:** the *operational nowcast* — an existing delay-adjustment model extended for one surveillance system, run daily for a health authority, and evaluated against both synthetic data with a known truth and the data that arrived later. Where McGough 2020 argues that a method generalises, this paper argues that one system's peculiarities (half its onset dates missing, a delay distribution that drifts, weekday effects) have been handled, and checks each handling choice.

## Structure
*Biometrical Journal*: `Abstract` → `1. Introduction` → **`2. Data`** → `3. Methods` (*3.1 Nowcasting*, in two numbered steps · *3.2* the reproduction number · *3.3 Evaluation of the methods* · *3.4 Implementation*) → `4. Results` (data, imputation, nowcast, reproduction number, evaluation) → discussion → appendix sensitivity analysis.

**Data gets its own section ahead of Methods**, because the method's two steps exist to repair two features of the data: missing onset dates and a reporting date that is closer to the event than the one the nowcast uses. A reader who has not met the data cannot judge the model.

**The method is presented as numbered steps** — "The nowcast itself consists of two steps: imputation of missing disease onset dates (Step 1) and Bayesian nowcasting based on the imputed data (Step 2)" — and the subsections carry those names, so a reader can find where each assumption enters.

## Opening move
> "Daily reported case numbers of an infectious disease outbreak do not correspond to the actual number of disease onsets on that day. Due to delays from reporting and testing, the number of newly reported cases and the actual number of newly diseased cases can substantially differ. It is the latter, however, that is of central interest when assessing the state and dynamics of an epidemic outbreak."

**The first sentence names the gap between what is counted and what matters**, and the third says which of the two the reader should care about. The problem is stated before any method is named.

**The term is pinned down against rival uses before it is used**:
> "In the following, we will refer to this delay adjustment approach as the nowcast and define the reporting delay as the time between disease onset and official case reporting by a health authority. Other authors use the term nowcasting for models that focus on adjusting the administrative delay between the first case report to a local health authority and registration (in aggregated data) at higher (e.g., state and/or federal) authorities…, or to perform nowcasting of fatal cases between case registration and fatality date"

**When a term covers several delays in the literature, say which delay yours is, and name the others.** A nowcast of onsets and a nowcast of registrations answer different questions, and the paragraph prevents the comparison a careless reader would make.

**Credit is given up front**: "The approaches are based on previously published work, that we considerably extended and adapted to the current task of nowcasting COVID-19 cases." The random-walk prior is attributed to the paper that showed it worked — "The utilization of the first-order random walk for modeling … was motivated by results of McGough, Johansson, Lipsitch, and Menzies".

## Methods
- **Choose the timestamp that never revises as the anchor.** Two reporting dates exist; the paper nowcasts on the one fixed at publication: "Since we get our data from the LGL, the number of cases reported to the LGL on a specific date is complete and will not change on subsequent days." The earlier local-authority date, closer to onset but still filling in, is used only where its incompleteness does not matter: "we use the date of reporting to the local health authority only for the imputation of missing disease onsets, while the nowcast is based on the date a case was reported to the LGL".
- **Quantify the missingness and rank its causes**:
  > "the daily COVID-19 surveillance data of Bavaria contain about 50%–60% cases with missing information on the day of symptom onset in the weeks close to now… The missing onset information exists partly due to the heavy workload imposed on health authorities during the pandemic, but also because a certain proportion of cases have no or only very mild symptoms. However, we expect the latter explanation to be less prominent than the former."

  The ranking matters: if missingness were mostly asymptomatic infection, imputing an onset date would be inventing one. **Say which mechanism you think dominates, because the imputation's validity depends on it.**
- **One sentence on what the target is not**: "Note also that the date of symptom onset does not correspond to the infection date due to a preceding incubation time."
- **Justify a design choice by the comparison it enables**: imputing onsets for every case "implies that we also consider presymptomatic and asymptomatic COVID-19 cases in our analyses… The rationale is that this allows to compare the nowcasting results to the daily reported case numbers."
- **Name the assumption the imputation makes, then design a test of it**:
  > "Since this imputation induces, conditional on the predictors of the GAMLSS imputation model, a missing at random assumption with respect to the time between disease onset and case reporting, we perform a sensitivity analysis, where we omit (i) all individuals where the reports say explicitly that they were symptom-free and (ii) all individuals with missing information about symptoms."

  **Missing at random is stated by name, and the sensitivity analysis is built to break it.** The appendix reports that the epidemic curve and reproduction number keep their shape under both exclusions.
- **Specify the evaluation grid as a table of model variants** (Table 1) — observation distribution crossed with delay-model structure — so the evaluation reads as a designed comparison rather than a model search.
- **Include an oracle**: on synthetic data the model is also fitted "with the known true changepoints in the delay distribution (that are unknown in real-world applications)". **An oracle variant measures what not knowing costs**, and bounds how much better any changepoint strategy could do.
- **Trim the estimate where it is known to be biased**, rather than reporting it and warning: the reproduction number is estimated only up to a point that leaves time for 95% of secondary cases to appear — "This avoids a downward bias in the … estimation near" the present.

## Results
**Report what the delay model found about the data before what the nowcast found about the epidemic**: "All covariates turned out to be relevant: we find an increase in expected delay time over the reporting weeks, lower reporting delay for older cases, and differences over the course of a week."

**The headline is the divergence between the corrected and the raw curve, in dates**:
> "The induced bias due to the reporting delay is obvious: the estimated daily new cases stabilize from around March 20 on and start to decrease afterward, while the reported cases still show a rapid increase."

**State the reporting rule for the most uncertain days, and why**: "we set a reporting lag between the current date and reported nowcast results of 2 days due to considerable uncertainty in the nowcasts for dates with very few observations with reported or imputed disease onset." The two most recent days are withheld rather than shown with intervals too wide to use.

**Overlay the later truth on the real-time nowcast** — Figure 2 adds the "retrospective true number of disease onsets known up until July 31" — and say how well it matched: "the prediction intervals contain the actual number of onsets for most days."

**Warn against the most tempting misreading of the reproduction number**:
> "care is required, if interpreting this result with the timing of interventions, because the … estimator is defined forward in time and describes the transmission process within the following 10 days."

A reader will line the estimate up against intervention dates; the sentence says why that alignment is off by up to ten days.

**Report the evaluation as ranked lessons, with what failed**:
> "first and foremost, it is important to account for existing changes in delay between disease onset and case reporting over time. Ignoring such changes can severely bias the predicted number of disease onsets."

Then second (negative binomial over Poisson) and third (the random-walk prior), and the alternatives that lost: "We also tried i.i.d. log-Gamma priors and a smooth modeling of the epidemic curve based on truncated power splines as proposed in Höhle and an der Heiden, but found the first-order random walk to perform best." The more flexible delay model is reported with its practical cost, not only its scores: it "had convergence problems on some days and might be overly complex for many scenarios."

**The table carries the size of the lesson**: on the retrospective Bavarian data, the constant-delay model's 95% intervals covered the truth 19% of the time, against 84% for the negative binomial model with two-weekly changepoints.

## Literature
Author–year citations. The paper is generous to the work it extends (Höhle and an der Heiden; McGough 2020) and specific about the national comparator, the Robert Koch Institute's nowcast, naming the features that differ — weekday effects, a calendar-time trend in the delay, and a generation-time distribution rather than a constant: "an der Heiden and Hamouda used a constant generation time of 4 days, while our approach includes a more realistic assumption of an individually varying time".

**A compartmental alternative is criticised on what it requires, not on its results**:
> "while compartmental models can be useful for forecasting, its value for real-time estimation of R ( t ) hinges on it being a realistic model with a well-calibrated parameter estimated. Instead, we prefer the more statistically driven transmission-tree–based estimates, which rely less on model assumptions and more on a statistically sound analysis of the available data."

## Voice
First-person plural, past tense for the evaluation, present for the method. The prose is plain and occasionally rough (non-native constructions such as "allows to compare"), which costs nothing: every decision is given a reason. One closing sentence outruns the evidence — "we believe that our results give a much more reliable picture of the course of the pandemic than the mostly used time series of reported cases" — where the evaluation supports a narrower claim about onset counts near the present.

## Discussion and limitations
**Three numbered limitations, each saying which output survives the violation.** The first is the strongest move in the paper:
> "we correct for a bias due to delays between disease onset and case reporting, but provide no correction for possible cases in the population that were not tested… Assuming a constant factor of underreporting, we can analyze the dynamics of the outbreak in a more reliable way by our nowcasting method compared to focusing on daily counts of newly reported cases. Furthermore, R ( t ) estimates would be invariant to such constant underreporting. However, if the proportion of undetected cases varies over time, then the dynamics of the pandemic is not described adequately by our approach as well."

**Say which estimates are invariant to a violated assumption and which are not.** Constant under-ascertainment leaves the reproduction number untouched and the case counts biased; varying ascertainment biases both. That turns a generic caveat into a statement of which numbers to trust.

The second limitation is an identifiability problem at the edge of the data: "short-term changes, especially in the time close to the current day can lead to a bias, because it is particularly hard to distinguish between developments in the epidemic curve and changes in the reporting delay with no or very less data."

**The reproduction number is then argued to be the more robust output, for a stated reason**: it "only requires stable conditions within a short time window, since it compares the estimated and reported number of disease onsets to the situation at time points close by, instead of looking at the absolute numbers over a longer period of time."

**The close restates the estimand and points to the data that would complete it**: "For the interpretation, it has to be emphasized, that we estimate the number of persons with disease onset on a certain day", and "our estimated epidemic curve should be related to other data sources, like hospital admission, ICU admission, or death numbers."

## Data, code and funding
The line-list data are confidential, so the paper ships code with a **synthetic dataset built on the real reporting dates**:
> "Code to reproduce our analysis and for adaption to other application scenarios is available at https://github.com/FelixGuenther/nc_covid19_bavaria . There, we also provide an artificial data set based on the observed reporting dates of cases but for data protection reasons featuring only artificial information on the age and disease onset dates of the cases."

**When the data cannot be released, release data with the same structure**, so the pipeline runs end to end. The journal's reproducibility badge is qualified honestly: the results "were reproduced partially for data confidentiality reasons." The nowcast itself is published daily on a public webpage named in the abstract.

## Distinctive moves to borrow
1. **Give the data its own section before Methods** when the method exists to repair the data.
2. **Name the method's steps and title the subsections with them.**
3. **Define your delay against the other delays the same term covers.**
4. **Anchor on the timestamp that never revises**; use the earlier, still-filling one only where its incompleteness does not matter.
5. **Rank the causes of missingness**, because the imputation's validity depends on which dominates.
6. **Name the missing-at-random assumption and build the sensitivity analysis to break it.**
7. **Lay out the evaluation as a grid of model variants**, and include an **oracle** that knows what reality hides.
8. **Trim estimates where they are known to be biased** instead of reporting them with a warning.
9. **Withhold the most recent days** when their intervals are too wide to act on, and say so.
10. **Overlay the later truth on the real-time output.**
11. **Warn against the misreading readers will make** — here, aligning a forward-defined reproduction number with intervention dates.
12. **Report evaluation results as ranked lessons, including what lost** and what failed to converge.
13. **Say which outputs are invariant to a violated assumption**, not only that the assumption may fail.
14. **Ship a synthetic dataset with the real structure** when the real data are confidential.

## Related files
For the nowcasting method whose random-walk prior this paper adopts see [43-mcgough-2020-nobbs-nowcasting](43-mcgough-2020-nobbs-nowcasting.md); for the real-time comparison of eight nowcasting systems, one of them (SU) with this model's structure, see [71-wolffram-2023-nowcast-hub](71-wolffram-2023-nowcast-hub.md); for the delay biases treated as guidance see [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md) and [27-gostic-2020-practical-considerations-rt](27-gostic-2020-practical-considerations-rt.md); for a real-time reproduction-number pipeline see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md); for a reproduction number tracked district by district during an outbreak response, with a single time-varying transmission rate in place of a nowcast, see [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md). Other *real-time transmission analysis* exemplars: see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md) for an individual-based model fitted to a live national epidemic while control decisions were still being made; [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) for a widely used R_t estimator with two failing assumptions fixed, shipped in the package the field already uses; [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md) for a natural-experiment evaluation across Chinese cities, with a mechanistic counterfactual, written under emergency time pressure; [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) for the real-time Bayesian estimate of a time-varying reproduction number, in a clinical journal's structure; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver.
