# 51 — Sherratt et al. (2023), *eLife*
**"Predictive performance of multi-model ensemble forecasts of COVID-19 across European nations"**
Sherratt K, Gruson H, Grah R, Johnson H, Niehus R, Prasse B, et al. (European COVID-19 Forecast Hub). *eLife* 12:e81916. doi:10.7554/eLife.81916.

**Archetype:** *forecast evaluation* at hub scale — run a collaborative forecasting platform, standardise what everyone submits, build an ensemble, and evaluate every contributing model against it across countries, horizons and targets. The European counterpart to the US hub papers, and the corpus's exemplar of **comparing an ensemble against its own components**.

## Structure
*eLife* structured abstract (**Background / Methods / Results / Conclusions / Funding**) → `Introduction` → `Results` → `Discussion` → `Methods` → `Data availability` → supplementary files including an **MDAR checklist**.

**The abstract is unusually operational**: it states the hub's recruitment rule, the submission format, the ensemble construction method *including the date the method changed*, and the comparison metric — enough that a reader could rebuild the platform from the abstract alone.

## Opening move
> "Short-term forecasts of infectious disease burden can contribute to situational awareness and aid capacity planning. Based on best practice in other fields and recent insights in infectious disease epidemiology, one can maximise the predictive performance of such forecasts if multiple models are combined into an ensemble."

The Introduction then argues why *this* geography justifies a hub, rather than assuming it — the most transferable passage for anyone proposing a collaborative platform:
> "European public health professionals operate across national, regional, and continental scales, with strong existing policy networks in addition to rich patterns of cross-border migration influencing epidemic dynamics… a consistent approach to forecasting across the continent as a whole can support accurately informing cross-European monitoring, analysis, and guidance."

and names the equity argument for multi-country work: "where there is limited capacity for infectious disease forecasting at a national level, forecasters generating multi-country results can provide an othe[rwise unavailable capability]".

**Justify the scope of a collaborative effort by the decisions it serves at each scale** — national, regional, continental — not by the size of the dataset.

## Methods
- **State the standardisation that makes comparison possible**, which is the hub's actual contribution: forecasts for "COVID-19 cases and deaths reported by a standardised source for 32 countries over the next 1–4 weeks", submitted "using standardised quantiles of the predictive distribution".
- **Give the ensemble rule and disclose that it changed, with the date**:
  > "Each week we created an ensemble forecast, where each predictive quantile was calculated as the equally-weighted average (initially the mean and then from 26th July the median) of all individual models' predictive quantiles."

  **A protocol change mid-study is disclosed in the abstract with its date.** Concealing it would have made the evaluation uninterpretable; stating it costs a clause.
- **Name the comparison metric and what it is relative to**: "We measured the performance of each model using the relative Weighted Interval Score (WIS), comparing models' forecast accuracy relative to all other models."
- **Separate what was done prospectively from what was explored afterwards**: "We retrospectively explored alternative methods for ensemble forecasts, including weighted averages based on models' past predictive performance." The word *retrospectively* marks the boundary between the hub's real-time operation and the post-hoc analysis.
- **Define the unit of evaluation explicitly**: "we created 2139 forecasting scores, where each score summarises a unique combination of forecasting model, variable, country, and week ahead horizon."

## Results
**Describe the participation structure, including its unevenness, before any performance claim:**
> "Modellers created forecasts choosing from a set of 32 possible locations, four time horizons, and two variables, and modellers variously joined and left the Hub over time. This meant the number of models contributing to the Hub varied over time and by forecasting target."

then the concrete extremes: "we received the most forecasts for Germany, with 29 unique models submitting 1-week case forecasts, while only 12 models ever submitted 4-week case or death forecasts for Liechtenstein."

**An unbalanced panel is the central methodological hazard of hub evaluations**, and naming the sparsest and densest cells is how a reader calibrates their trust in the averages.

**Report how teams expressed uncertainty, as a count**: "Only three models provided point forecasts with no estimate of uncertainty around their predictions, while 41 models provided the full set of 23 probabilistic quantiles across the predictive distribution for each target."

**Give the headline as a proportion of models beaten, with N and the number of distinct models behind it**:
> "Across all horizons and locations, the ensemble performed better on relative WIS than 83% of participating models' forecasts of incident cases (with a total N=886 predictions from 23 unique models), and 91% of participating models' forecasts of deaths (N=763 predictions from 20 models)."

**"Beat 83% of models" is more informative than a mean score**, because it survives the panel being unbalanced — and both the prediction count and the model count are given so the reader knows whether the percentage rests on many models or many repeats of a few.

**Report the horizon-dependence separately per target, because they differ**: "Across a 1–4 week time horizon, ensemble performance declined with longer forecast periods when forecasting cases, but remained stable over 4 weeks for incident death forecasts."

**State the ensemble-method finding as a ranked choice among the options tried**: "Among several choices of ensemble methods we found that the most influential and best choice was to use a median average of models instead of using the mean, regardless of methods of weighting component forecast models." The phrase *most influential* separates which knob mattered from which setting won — weighting turned out not to matter, the mean-versus-median choice did.

## Literature
Author–year citations, *eLife* style, very dense in the Discussion where the horizon finding is placed against prior hub evaluations on both sides: "Previous work has found rapidly declining performance for case forecasts with increasing horizon (Cramer et al., 2021b; Castro et al., 2020), while death forecasts can perform well with up to 6 weeks lead time (Friedman et al., 2021)."

## Voice
First-person plural, past tense, with claims bounded to the study period and targets. Conclusions are addressed to forecast *users* as well as producers, which is rare and useful: "Our findings also highlight that forecast consumers should place more weight on incident death forecasts than incident case forecasts at forecast horizons greater than 2 weeks."

**Write at least one conclusion for the person consuming the forecast**, not only for the person making it.

## Discussion and limitations
Opens by restating what was collected and what was found, then takes the hardest finding — that forecasting turning points is hard — and **explains it with the specific history of the study period** rather than as a generic caveat:
> "Our study period included multiple fundamental changes in viral-, individual-, and population-level factors driving the transmission of COVID-19 across Europe. In early 2021, the introduction of vaccination started to change population-level associations between infections, cases, and deaths … while the Delta variant emerged and became dominant … Similarly from late 2021 we saw the interaction of individually waning immunity during the emergence and global spread of the Omicron variant … Neither the extent nor timing of these factors were uniform across European countries covered by the Forecast Hub … This meant that the performance of any single forecasting model depended partly on the ability, speed, and precision with which it could adapt to new conditions for each forecast target."

**The cases-versus-deaths contrast is then explained by two mechanisms, each argued from epidemiology and from data quality**:
> "First, COVID-19 has a typical serial interval of less than a week. This implies that case forecasts of more than 2 weeks only remain valid if rates of both transmission and detection remain stable over the entire forecast horizon…
>
> Second, we can interpret the higher reliability of death forecasts as due to the different lengths and distributions of time lags from infection to case and death reporting. For example, a spike in infections may be matched by a consistently sharp increase in case reporting, but a longer tailed distribution of the subsequent increase in death reports. This creates a lower magnitude of fluctuation in the time-series of deaths compared to that of cases. Similarly, surveillance data for death reporting is substantially more consistent, with fewer errors and retrospective corrections, than case reporting."

**Explain a performance difference between two targets with the generation interval and the reporting process**, not with model quality. This is the move that turns an evaluation result into epidemiological understanding.

## Data, code and funding
Among the strongest availability statements in the corpus: the source data were **already public before the study**, the forecast repository is archived with a Software Heritage revision identifier, and the analysis lives in its own public repository — "All source data were openly available before the study, originally available at: https://github.com/covid19-forecast-hub-europe/covid19-forecast-hub-europe (copy archived at swh:1:rev:…). All data and code for this study are openly available on Github." Participating-team metadata is supplied as a supplementary CSV, and an **MDAR checklist** is filed.

**Separate the platform repository from the analysis repository, and archive the platform at a specific revision** — the evaluation then refers to a fixed snapshot of a moving object.

## Distinctive moves to borrow
1. **Justify a collaborative platform by the decisions it serves at each scale**, including the capacity-equity argument for places that cannot forecast alone.
2. **Standardise the submission format** — a fixed quantile set from a named data source — and say so in the abstract; that standardisation is the contribution.
3. **Disclose a protocol change with its date**, in the abstract.
4. **Mark explicitly which analyses were prospective and which retrospective.**
5. **Define the unit of evaluation** (model × variable × country × horizon) and report how many there were.
6. **Describe the participation panel and its sparsest and densest cells** before reporting averages over it.
7. **Count how teams expressed uncertainty**, including how many gave none.
8. **Report the ensemble as a percentage of models beaten, with N predictions and N models.**
9. **Report horizon-dependence per target** when targets behave differently.
10. **Separate which choice mattered from which option won** — median versus mean mattered; weighting did not.
11. **Explain performance differences with the generation interval and the reporting process**, not with model quality.
12. **Write a conclusion for forecast consumers**, telling them which outputs to trust and at what horizon.
13. **Archive the moving platform at a fixed revision**, and keep the analysis code in a separate repository.

## Related files
For the US hub counterparts see [09-cramer-2022-covid-forecast-hub-evaluation](09-cramer-2022-covid-forecast-hub-evaluation.md) and [10-reich-2019-flusight-multiyear](10-reich-2019-flusight-multiyear.md); for the WIS itself see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md); for assessing forecasts issued in real time by a single team see [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md); for collaborative nowcasting organised the same way see [43-mcgough-2020-nobbs-nowcasting](43-mcgough-2020-nobbs-nowcasting.md).
