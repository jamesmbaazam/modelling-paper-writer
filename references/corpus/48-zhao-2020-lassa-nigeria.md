# 48 — Zhao et al. (2020), *Epidemiology & Infection*
**"Large-scale Lassa fever outbreaks in Nigeria: quantifying the association between disease reproduction number and local rainfall"**
Zhao S, Musa SS, Fu H, He D, Qin J. *Epidemiol Infect* 148:e4. doi:10.1017/S0950268819002267.

**Archetype:** *surveillance-data transmissibility analysis with an environmental covariate* — estimate R from routine case counts using phenomenological growth curves, then regress those estimates on an ecological driver. A compact analysis built entirely from public data, and the corpus's exemplar of what a mid-tier epidemiology journal publishes.

## Structure
Cambridge format: unstructured `Abstract` → `Key words` → `Introduction` → **`Data and methods`** (*Data*, growth models, model selection, heterogeneity test, regression) → **`Results and discussion`** (merged) → limitations → conclusion.

**The merged `Results and discussion` suits a short paper** where each result needs its interpretation immediately and there is no room to say anything twice. **`Data and methods` rather than `Methods`** signals, correctly, that the data sources are half the contribution when everything is secondary.

## Opening move
> "Lassa fever (LF) is increasingly recognised as an important rodent-borne viral haemorrhagic fever presenting a severe public health threat to sub-Saharan West Africa. In 2017–18, LF caused an unprecedented epidemic in Nigeria and the situation was worsening in 2018–19."

The Introduction then builds the causal chain the paper will test, link by link, each cited:
> "The common reservoir of LASV is *Mastomys natalensis*, one of the most widespread rodent species in sub-Saharan Africa, which exhibits sensitive population dynamics to the water level, e.g. rainfall, flooded agricultural activities. Previous studies have recognised the ecological association between the population levels of rodents and rainfall."

Rainfall → rodent populations → human infection. **Lay out the mechanistic chain in the Introduction so a statistical association later reads as a test of a mechanism rather than data dredging.**

**The gap is stated as a missing quantification of a known idea**, which is both honest and checkable:
> "While there have been discussions about the association of rainfall level and LF incidence rate, this association has not yet been demonstrated and quantified."

Not "little is known" — the discussion exists; what is missing is the demonstration and the number. **"Has not yet been demonstrated and quantified" is a reusable formula** for a paper whose contribution is evidential rather than conceptual.

The disease is characterised with the numbers that establish why it matters, including the range that makes the case fatality meaningful: "LF has a high case fatality rate ranging from 1% in the community to over 60% in hospital settings."

## Methods
- **Name the data source, its publisher and its public availability in one sentence**: "Weekly LF surveillance data are obtained from the Nigeria Centre for Disease Control (NCDC), where the data are publicly available from the weekly situation reports released by NCDC. Laboratory-confirmed case time series are used for analysis."
- **State the case definition used and say it is the restrictive one** — laboratory-confirmed only — so the reader knows which denominator is in play.
- **Justify the unit selection by an explicit, pre-stated criterion** rather than by convenience: the five states analysed are those "that were among the top 10 hardest-hit states in both the 2018 and 2019 epidemics, i.e. Edo, Ondo, Ebonyi, Bauchi and Plateau". The selection rule is given before the names.
- **Disclose the provenance of the covariate honestly, including that it is not official**: "The state rainfall records of each state were collected on monthly average basis from the historical records of the World Weather Online website."
- **Fit several models of the same class and average rather than choosing one**: "We quantify the infectivity of LF by the reproduction numbers estimated from four different growth models: the Richards, three-parameter logistic, Gompertz and Weibull growth models", summarised "with model-average estimates". Where no model is mechanistically privileged, model averaging is more defensible than selecting a winner — compare the vote-counting across models in `evidence.md` §6.2.
- **Benchmark against a naive time-series model**: "Most of the models have positive partial R-squared against the baseline AR(2) model." A growth-curve fit means little without a baseline that could also fit a rising curve.
- **Test heterogeneity formally before asserting it**: "Cochran's Q test is further applied to test the spatial heterogeneity of the LF epidemics." The claim of spatial heterogeneity is backed by a named test rather than by inspection of a map.
- **Use a random-effect regression to pool across states and lags**: "A linear random-effect regression model is adopted to quantify the association between R and state rainfall with various lag terms."

## Results
**Report the estimate for each season with intervals, and state the comparison explicitly**:
> "Our estimated R s for 2017–18 (1.33 with 95% CI 1.29–1.37) was significantly higher than those for 2016–17 (1.23 with 95% CI: (1.22, 1.24)) and 2018–19 (ranged from 1.08 to 1.36)."

**Give the association in interpretable units with its lag and its interval** — the sentence the paper exists to produce:
> "We find that a one-unit (mm) increase in average monthly rainfall over the past 7 months could cause a 0.62% (95% CI 0.20%–1.05%)) rise in R."

Unit of exposure, lag window, percentage effect on the outcome, confidence interval. **An environmental-driver result needs all four or it cannot be used.**

**Show the lag graphically before testing it**, which is how the 7-month window is made credible rather than fished: "The cumulative lagged effects were observed via matching the peak timing of the rainfall and epidemic curves. In Figure 1(c), we shift the rainfall time series of the five states by +6 months to match the trends of the national LF epidemic curve."

**Report a derived quantity — the turning point — with its calendar meaning and what it means when it moves**: "Most of the regions exhibit an epidemic turning point (τ) ranging from the epidemiological week (EW) 4–10, i.e. from the end of January to mid-March, in each year… Larger τ means the more extension in the duration of the epidemics." Epidemiological weeks are translated into dates, and the parameter is interpreted in one clause.

**Name the competing explanations for the derived quantity rather than attributing it**: "The turning point (τ) could be affected by several factors including seasonality, intervention program and dep[loyment]…".

## Literature
Numbered Cambridge citations, moderate density, concentrated in the Introduction where the mechanistic chain is assembled. The literature is used for three distinct jobs: establishing the ecology (rodent–rainfall), supplying an external parameter for a derived calculation (seroprevalence), and citing the theory that licenses that derivation.

## Voice
First-person plural, present tense for the analysis. Causal language is hedged where the design is observational — "could cause a 0.62% rise in R", "could be affected by several factors" — though the abstract's closing claim, "We report clear evidence of rainfall impacts on LF epidemics in Nigeria and quantify the impact", is stronger than the regression design supports. A writer borrowing this paper's structure should keep the hedged in-text formulations and **not** escalate in the abstract.

## Discussion and limitations
The limitations are short, specific and — unusually — each is followed by what was done about it or what could be:

- **A data limitation with the design change it forced**: "the weather data are available only from a limited number of observatory stations and thus it is not sufficient to capture more accurate spatial variability. In this work, instead of exploring the spatial differences in the associations between rainfall and LF epidemic, we relaxed the setting and studied a general relationship."

  **The limitation is converted into a stated scope decision**, so the reader knows the paper is answering the general question deliberately rather than failing at the specific one.
- **A limitation of the estimand, with the route to the quantity readers will want** — the best passage in the paper:
  > "For the transmissibility estimation, our growth modelling framework can provide the estimates of R, but not the basic reproduction number commonly denoted as R₀. However, according to the theoretical epidemiology, the R₀ can be determined by R₀ = R/S, where S denotes the population susceptibility. Although S is not involved in our modelling framework, the information of S could be acquired from local serological surveillances. The existing literature reported 21.3% seroprevalence among Nigerian humans by the enzyme-linked immunosorbent assay (ELISA). Hence, the R₀ can be calculated as 1.63 by using S = 1–21.3% = 0.787 and the R = 1.28 as the average of the 2016–18 LF epidemics."

  **Say which quantity your method does *not* estimate, give the relation that connects it to the one you want, source the missing input from the literature, and do the arithmetic in the open.** The reader gets the number they came for and can see exactly which external input it rests on.
- **A statement of what kind of study this is**, which bounds every causal reading: "This was a data-driven modelling study, and we quantified the effect of rainfall as a weather-driven force of R based on previous ecological and epidemiological evidences."
- **Named confounders in the same ecological chain**: "the factors including seasonality, agricultural land-using, subtropical or tropical forest coverage that…" — the other things that covary with rainfall and could drive the association.

## Distinctive moves to borrow
1. **Lay out the mechanistic chain in the Introduction** so a later statistical association reads as a mechanism test.
2. **"Has not yet been demonstrated and quantified"** — a gap statement that credits existing discussion and names what is missing.
3. **Give the unit-selection rule before naming the units selected.**
4. **Disclose non-official data provenance plainly** rather than obscuring it.
5. **Model-average across a family when none is mechanistically privileged**, and benchmark against a naive time-series model.
6. **Test heterogeneity with a named test** before claiming it.
7. **Report an environmental association with exposure unit, lag, effect size and interval** — all four.
8. **Show the lag graphically before fitting it**, so the window is not fished.
9. **Translate epidemiological weeks into dates** and interpret derived parameters in one clause.
10. **Convert a data limitation into an explicit scope decision.**
11. **Name the quantity your method cannot estimate, give the relation to it, source the missing input, and show the arithmetic.**
12. **Name the confounders that covary with your exposure** in the same ecological chain.

## What to avoid from this paper
- **An abstract claim stronger than the design.** "Clear evidence of rainfall impacts" overstates a lagged ecological regression on five states; the in-text "could cause" is right.
- **A reproduction number without a stated generation-interval assumption.** Growth-curve R estimates depend on it (see [27-gostic-2020-practical-considerations-rt](27-gostic-2020-practical-considerations-rt.md) §on generation-interval misspecification).

## Related files
For R_t estimation done mechanistically from incidence see [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) and [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md); for the seasonality mechanisms this paper's rainfall association instantiates see [05-altizer-2006-seasonality-review](05-altizer-2006-seasonality-review.md); for rodent reservoirs and zoonotic spillover traits see [33-han-2015-rodent-reservoirs](33-han-2015-rodent-reservoirs.md) and [32-olival-2017-zoonotic-spillover-traits](32-olival-2017-zoonotic-spillover-traits.md); for serological inputs of the kind used here to recover R₀ see [40-prayitno-2017-dengue-seroprevalence](40-prayitno-2017-dengue-seroprevalence.md).
