# 43 — McGough et al. (2020), *PLoS Computational Biology*
**"Nowcasting by Bayesian Smoothing: A flexible, generalizable model for real-time epidemic tracking"**
McGough SF, Johansson MA, Lipsitch M, Menzies NA. *PLoS Comput Biol* 16(4):e1007735. doi:10.1371/journal.pcbi.1007735.

**Archetype:** the *nowcasting / reporting-delay method* paper — correct an incomplete, right-truncated case series for reporting delay, demonstrate the method on two unrelated diseases, benchmark it against an existing implementation, and ship it as software. A methods paper whose claim is **generalisability**, which dictates everything about how it is evidenced.

## Structure
PLoS Comput Biol: `Abstract` → `Author summary` → `Introduction` → `Results` (model description, then the two applications, then the benchmark, then robustness) → `Discussion` → `Materials and methods` (*Surveillance data* · *Reporting triangle* · model · *…performance metrics* · software) → availability.

**The structural decision that defines the archetype: two diseases, chosen to differ in the one property the method is sensitive to.** Dengue in Puerto Rico and influenza-like illness in the United States are not two illustrations; they are a designed contrast — "settings exhibiting a range of common reporting delay characteristics (from stable to time-varying)". A generalisability claim needs at least two settings that differ in the dimension at issue, and the paper says which dimension that is.

## Opening move
> "Achieving accurate, real-time estimates of disease activity is challenged by delays in case reporting. 'Nowcast' approaches attempt to estimate the complete case counts for a given reporting date, using a time series of case reports that is known to be incomplete due to reporting delays."

The problem, then the class of solution, then the two specific deficiencies in that class that this paper fixes:
> "However, many nowcast approaches ignore a crucial feature of infectious disease transmission—that future cases are intrinsically linked to past reported cases—and are optimized to one or two applications, which may limit generalizability."

**Two named defects, each addressed by a named feature of the new method** — a temporal dependency between case counts, and demonstration across settings. The gap is a property of existing methods, which is checkable, rather than an absence of work.

**The Introduction enumerates the causes of the delay before modelling it** — a list worth borrowing for any delay-distribution paper:
> "Multiple features of the disease and surveillance system contribute to reporting delays, including: delays in symptoms onset after infection; delays in medical care-seeking after onset; delays in providers obtaining and reporting diagnostic information; level of awareness of disease activity influencing care-seeking and reporting; and system-level processing delays, a result of complex and multi-tiered disease reporting and communication systems interacting at multiple administrative levels."

Then the consequence in operational terms — "surveillance data are typically not complete until weeks or months after infections have actually occurred" — and the method's provenance in another field: "With origins in the insurance claims and actuarial literature, nowcast models aim to estimate the number of occurred-but-not-yet-reported events."

## Methods
- **Describe the data by what the two timestamps mean**, which is the whole substance of a delay analysis: for dengue, "The times used for the analysis were the time of onset as reported by the reporting clinician and the time of laboratory report completion"; for ILI, "the week of ILI-related care seeking and the week when those cases were posted online in FluView".
- **Give the data volume and span for each source**: "approximately 53,000 cases of dengue in Puerto Rico and 2.77 million cases of ILI in the United States over a 21-year (1092 weeks) and 3.75-year (196 weeks) period, respectively."
- **Disclose a data irregularity and the restriction it forced**: "ILI data with delays of more than 6 months occasionally had irregularities, so we restricted the analyses to delays of up to 6 months."
- **Define the structure the problem lives in, and state the truncation explicitly**:
  > "Delays in reporting are often structurally decomposed into a (T x D) dimensional 'reporting triangle,' where T is the most recent week ('now') and D is the maximum reporting delay, in weeks, observed in the data. The data are right-truncated, since at any given week t, delays longer than T–t cannot be observed."
- **Write out every performance metric as a formula** — MAE, RMSE, rRMSE, and then two metrics for the *change* between weeks (MAEΔ, RMSEΔ), plus lag-1 autocorrelation of predictions and of cases, plus a logarithmic score with its binning stated ("bin widths of 25 cases for dengue and 1000 cases for influenza"). **Metrics chosen to test the claim**: because the method's selling point is smoothness and temporal coherence, metrics on the week-to-week change and on autocorrelation are reported alongside the usual error metrics.
- **Score the distribution, not only the point estimate.** The logarithmic scoring rule is applied to the posterior predictive distribution, which is what makes the uncertainty claim testable.

## Results
**State what the model learns, in words, before any equation**:
> "the approach learns from historical information on cases reported at multiple delays (e.g. no delay, 1-week delay, 2-week delay, etc.) from the week of case onset to estimate the reporting delay probability at each delay and the relationship between case counts from week-to-week, and uses this relationship to predict the number of not-yet-reported cases in the present using a log-linear model."

**Report the benchmark honestly in both directions.** The comparison does not favour the new method everywhere, and the paper says so in the same sentence:
> "point estimates for NobBS were substantially more accurate than the HH model for dengue cases (rRMSE improved by 300%) and slightly less accurate for ILI cases (rRMSE decreased by 19%)."

**Then separate the two virtues and show where the real gain is** — accuracy versus calibration, exactly as `SKILL.md` §6 requires (`evidence.md` §6.2):
> "However, analysis of the probability distributions of the nowcasts revealed a much more substantial difference; the average score for NobBS was approximately twice as high for dengue and more than 10 times as high for ILI cases. This indicates that the NobBS approach assigned much higher probability to the actual outcome, even though point accuracy was somewhat lower for the ILI cases."

**Reporting a loss on one metric and a large gain on another, with the interpretation attached, is more convincing than a clean sweep.**

**Name the mechanism behind the performance rather than only the performance**: "NobBS introduces a simple dependency between case counts over time; that is, changes in case counts between weeks are assumed to be related via a first-order random walk process on the logarithmic scale. This feature is critical in the context of infectious disease transmission, where the number of true infections in a given week mechanistically depends in part on the number of true infections in previous weeks due to the infectious process, whether the pathogen is transmitted directly or by vectors."

**Report a trade-off as a trade-off, with both directions**: "we further demonstrate an important trade-off related to moving window sizes for delay distribution estimates; short windows improve the real-time characterization of the delay distribution but are susceptible to over-estimating that variability, potentially decreasing nowcast accuracy." A tuning parameter with a genuine tension is more useful to a reader than a recommended default.

**Report degraded performance in the harder regime, and still claim the comparison**: "when reporting delays are time-varying, as is often the case in epidemics, we show that the NobBS approach is less accurate compared to its performance in a stable delay distribution, but still shows improvement over the HH approach likely because the NobBS approach is informed by the number of cases experienced in previous weeks, not just the delay distribution."

## Literature
Numbered PLoS citations. The standout move is how a near-simultaneous competing paper is handled — cited, credited, and then differentiated on specifics rather than ignored or disparaged:
> "Indeed, a recently published study describes a similar approach to NobBS, proposing the same model structure (an adaptation of the historic chain-ladder approach) and similar priors (namely, a first-order random walk on the underlying distribution of cases), finding that this approach performed well for two diseases. Two key differences in model structure are that NobBS parameterizes the delay distribution as a Dirichlet as opposed to a random walk, to model the underlying delay distribution as a probability vector, and omits a model intercept."

**When someone else has published the same idea, say so, state the two concrete differences, and let the reader judge.** The paper then claims the contribution that remains genuinely its own: "We also aimed to identify and deconstruct the features that contribute to good performance."

**Criticise the comparator on an operational ground, not a statistical one**: "the HH approach software includes the option to model a time-varying delay explicitly in the nowcast approach, but requires specifying the time at which the delay distribution is expected to change (the change-point), which is generally not known in real-time." A requirement that cannot be met in real time is a decisive objection to a real-time method.

## Voice
First-person plural, present tense for the method and past for the evaluation. Claims are bounded by the evidence: "can be immediately adapted in a variety of disease settings" is licensed by "Lacking any disease-specific parameterization, and relying only on historical trends of case reporting as input" — the generality claim is derived from a property of the model, not from the two successes.

## Discussion and limitations
Opens with what was done and what was shown, then immediately qualifies the scope of the win ("outperforms an existing method in terms of point estimate (reduced RMSE, lower bias) and probabilistic (higher logarithmic score) predictive performance. In particular, NobBS performs well even when the delays in case reporting change over time"), then the trade-off, then the basis for generalisation.

The limitations are carried in the same register as the results — each is a condition on use rather than an apology: the moving-window trade-off, the degradation under time-varying delays, the restriction to delays under six months, and the requirement that at least one case be initially reported for a nowcast to exist at all ("the subset of weeks in which both models could produce forecasts (weeks with at least one case initially reported)"), which is quietly the most important operational limit for a rare disease.

## Data, code and funding
Ships as an R package named in the abstract — "We present an R package, 'NobBS,' as a tool to complement both routine public health surveillance as well as forecasting efforts" — with both data sources identified by their public APIs and dashboards (FluView; the DELPHI epidemiological data API, with its repository URL). CRediT contributor roles are itemised per author, including `Software`, and competing interests are declared.

## Distinctive moves to borrow
1. **Evidence a generalisability claim with settings chosen to differ in the property at issue**, and name that property.
2. **State the two defects of existing methods**, then fix exactly those, so the contribution is checkable.
3. **Enumerate the mechanisms that generate the delay** before modelling the delay.
4. **Say what the two timestamps are.** A delay analysis is only as meaningful as the events it is measured between.
5. **Define the reporting triangle and state the right-truncation explicitly.**
6. **Choose metrics that test your actual claim** — here, errors on the week-to-week *change* and autocorrelation, because the claim is smoothness.
7. **Score the predictive distribution, not just the point estimate**, and report accuracy and calibration separately.
8. **Report the benchmark loss alongside the gain**, in the same sentence, with the interpretation.
9. **Name the single structural feature responsible for the gain**, and say why it is mechanistically right for the problem.
10. **Present a tuning parameter as a trade-off with both directions**, not a recommended default.
11. **Handle a simultaneous competing publication by crediting it and naming two concrete differences.**
12. **Object to a comparator on operational grounds** — a change-point "generally not known in real-time" — where that is the decisive issue.

## Related files
For the biases this method corrects, treated as guidance, see [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md) and [27-gostic-2020-practical-considerations-rt](27-gostic-2020-practical-considerations-rt.md); for the real-time pipeline that consumes nowcast output see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md); for proper scoring rules and the accuracy-versus-calibration distinction see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md) and [09-cramer-2022-covid-forecast-hub-evaluation](09-cramer-2022-covid-forecast-hub-evaluation.md). Other *nowcasting / reporting delays* exemplars: see [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast that adopts this paper's random-walk prior and handles missing onset dates; [71-wolffram-2023-nowcast-hub](71-wolffram-2023-nowcast-hub.md) for eight nowcasting systems compared in real time and scored against later data.
