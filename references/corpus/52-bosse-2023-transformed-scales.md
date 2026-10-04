# 52 — Bosse et al. (2023), *PLoS Computational Biology*
**"Scoring epidemiological forecasts on transformed scales"**
Bosse NI, Abbott S, Cori A, van Leeuwen E, Bracher J, Funk S. *PLoS Comput Biol* 19(8):e1011393. doi:10.1371/journal.pcbi.1011393.

**Archetype:** *forecast evaluation* in its methodological form — not *which model won* but *on what scale the question should be asked*. A short argumentative paper that derives three interpretations of one choice, demonstrates the consequences on real hub data, and is candid that the choice is a value judgement.

## Structure
PLoS Comput Biol: `Abstract` → `Author summary` → `Introduction` (with the propriety of scoring rules taught from first principles) → theory → application to the European Forecast Hub → `Discussion` → `Data Availability`.

**The argument runs theory → properties → demonstration → caveats**, and the three properties claimed for the transformation are enumerated in the abstract and then delivered in that order. When a paper's contribution is an argument rather than a result, **number the claims up front and discharge them in sequence**.

## Opening move
> "Forecast evaluation is essential for the development of predictive epidemic models and can inform their use for public health decision-making. Common scores to evaluate epidemiological forecasts are the Continuous Ranked Probability Score (CRPS) and the Weighted Interval Score (WIS), which can be seen as measures of the absolute distance between the forecast distribution and the observation."

The gap is then a mismatch between the tool and the subject matter — the strongest kind of methodological gap:
> "However, applying these scores directly to predicted and observed incidence counts may not be the most appropriate due to the exponential nature of epidemic processes and the varying magnitudes of observed values across space and time."

**Two concrete reasons the default is wrong for this domain** — exponential growth, and incidence varying by orders of magnitude across place and time — not a general complaint about scoring rules.

**The three benefits are then enumerated in the abstract and each is a different kind of justification**:
> "Using the CRPS on log-transformed values as an example, we list three attractive properties: Firstly, it can be interpreted as a probabilistic version of a relative error. Secondly, it reflects how well models predicted the time-varying epidemic growth rate. And lastly, using arguments on variance-stabilizing transformations, it can be shown that under the assumption of a quadratic mean-variance relationship, the logarithmic transformation…"

An interpretation, an epidemiological meaning, and a statistical property. **Justify a methodological choice on more than one axis**, so a reader who rejects one argument may still accept another.

## Methods
- **Teach the concept the whole paper rests on, from first principles, in the Introduction.** Propriety is defined rather than cited:
  > "Proper scoring rules are constructed such that they encourage honest forecasting and cannot be 'gamed' or 'cheated'. Assuming that the forecaster's actual best judgement corresponds to a predictive distribution F, a proper score is constructed such that if F was the data-generating process, no other distribution G would yield a better expected score. A scoring rule is called strictly proper if there is no other distribution that under F achieves the same expected score as F, meaning that any deviation from F leads to a worsening of expected scores. Forecasters (anyone or anything that issues a forecast) are thus incentivised to report their true belief F about the future."

  Note the parenthetical definition of a term the reader may think they know: "Forecasters (anyone or anything that issues a forecast)". **Define the agent as well as the method** when a model and a person are both covered by the same word.
- **State the distributional condition under which the statistical justification holds, and name the distributions that satisfy it**: the log transformation is a variance-stabilising transformation "appropriate for variables that are approximately normally distributed and have a quadratic mean-variance relationship with σ = c × μ (this is e.g. approximately true for the negative binomoial distribution and large μ). Alternatively, the square-root transformation can be appropriate in the case of a Poisson distributed variable."
- **Demonstrate on data a reader already knows** — the European COVID-19 Forecast Hub — so the effect of the choice can be compared against a published evaluation on the natural scale.

## Results
**Report what the transformation does to the comparison, across every dimension the hub varies**:
> "When applying this approach to forecasts from the European COVID-19 Forecast Hub, we found overall scores on the log scale to be more equal across, time, location and target type (cases, deaths) than scores on the natural scale. Scores on the log scale were much less influenced by the overall incidence level in a country and showed a slight tendency to be higher in locations with very low incidences. **We found that model rankings changed noticeably.**"

**"Model rankings changed noticeably" is the sentence that makes the paper matter.** A methodological choice that leaves conclusions unchanged is a footnote; one that reorders the leaderboard is a finding, and it is reported plainly rather than softened.

**Characterise which failure modes each scale punishes**, which turns an abstract scale choice into something a forecaster can reason about:
> "On the natural scale, missing the peak and overshooting was more severely penalised than missing the nadir and the following upswing in numbers. Both failure modes tended to be more equally penalised on the log scale (with undershooting receiving slightly higher penalties in our example)."

**Decompose the score into its components on both scales.** The WIS components — overprediction, underprediction and dispersion — are reported as relative contributions on the natural and logarithmic scale, so the reader can see *where* the change in ranking comes from rather than only that it happened.

## Literature
Numbered PLoS citations. The paper situates scoring rules in the broader forecasting literature — economics and meteorology are named in the first sentence of the Introduction — and points at an adjacent field for further options: "Potentially, the variance stabilising time-series forecasting literature may be a useful source of other transformations for various forecast settings."

## Voice
First-person plural and argumentative rather than declarative: "we argue that", "we suggested using", "One could argue that", "Users nevertheless need to be aware". The paper is explicit that it is making a case rather than reporting a result, and it **states the opposing position fairly before answering it** (below).

## Discussion and limitations
Opens by restating the proposal and the three properties, in the order promised. Then the strength, stated as a fit between method and subject:
> "The most important strength of this approach is that the evaluation better accommodates the exponential nature of the epidemiological process and the types of errors forecasters who accurately model those processes are expected to make."

**The downside is then stated, immediately countered, and then the counter is itself qualified** — three moves in four sentences, and the best passage in the paper:
> "A potential downside is that forecast evaluation is unreliable in situations where observed values are zero or very small. One could argue that this correctly reflect inherent uncertainty about the future course of an epidemic when numbers are small. Users nevertheless need to be aware that this can pose issues in practice. Including very small values in prediction intervals… can lead to excessive dispersion values on the log scale."

**Then the genuine value disagreement is laid out with both sides given their best argument:**
> "Similarly, locations with lower incidences may get disproportionate weight (i.e. high scores) when evaluating forecasts on the log scale. [Others] argue that it is desirable to give large weight to forecasts for locations with high incidences, as this reflects performance on the targets we should care about most. On the other hand, scoring forecasts on the log scale may be less influenced by outliers and better reflect consistent performance across time, space, and forecast targets. Furthermore, decision makers may specifically care about situations in which numbers start to rise from a previously low level."

**Where a methodological choice encodes a value judgement, say so and give the opposing view its strongest form.** The paper does not claim the log scale is correct; it claims it is appropriate for a stated set of concerns, and names the concerns that favour the alternative.

**Refuse to over-claim the generality of the specific transformation**: "The log-transformation is only one of many transformations that may be useful and appropriate in an epidemiological context", followed by a catalogue of alternatives with the conditions for each — population standardisation, square root for Poisson, Box-Cox, dividing by the last observed value for multiplicative growth rates, first differences on the log scale.

**Report an alternative that is blocked by the data format, and say what would unblock it:**
> "Dividing values by the previous value, unfortunately, is not feasible under the current quantile-based format of the Forecast Hubs, as the growth rate of the α-quantile may be different from the α-quantile of the growth-rate. However, it may be an interesting approach if predictive samples are available or if quantiles for weekwise growth rates have been collected."

A format constraint is identified precisely, with the mathematical reason and the conditions under which it disappears — useful to anyone designing a hub.

Closes by generalising the proposal into a framework: "It is possible to go beyond choosing a single transformation by constructing composite scores as a weighted sum of scores based on different transformations. This would make it possible to create custom scores and allow forecast consumers to choose and assign explicit weights to different qualities of the forecasts."

## Data, code and funding
One line, one repository: "All code and data is available at https://github.com/epiforecasts/transformation-forecast-evaluation." Every author's funding is itemised with grant numbers and funders.

## Distinctive moves to borrow
1. **State the mismatch between the standard tool and your subject matter** — exponential processes, magnitudes varying by orders — rather than criticising the tool in general.
2. **Enumerate your claims in the abstract and discharge them in order**, when the contribution is an argument.
3. **Justify a methodological choice on several independent axes** — interpretability, epidemiological meaning, statistical property.
4. **Teach the foundational concept from first principles** rather than citing it, when the whole argument depends on it.
5. **Name the distributional condition** under which your justification holds, and the distributions that satisfy it.
6. **Demonstrate on a dataset readers already know**, so the effect of the change is visible against a published analysis.
7. **Say plainly if your choice changes the rankings.** That is the finding.
8. **Characterise which failure modes each option punishes**, so forecasters can reason about the choice.
9. **Decompose the score into components under both options**, to show where the difference arises.
10. **Give the opposing position its strongest argument** where the choice encodes a value judgement, and decline to declare a winner.
11. **Catalogue the alternatives you did not use**, with the condition that would make each appropriate.
12. **Identify a constraint imposed by the data format**, with the reason and what would lift it.

## Related files
For the score this paper transforms see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md); for the hub data it is demonstrated on see [51-sherratt-2023-european-forecast-hub](51-sherratt-2023-european-forecast-hub.md) and [09-cramer-2022-covid-forecast-hub-evaluation](09-cramer-2022-covid-forecast-hub-evaluation.md); for the calibration/sharpness/bias decomposition that motivates separating forecast qualities see [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md); for a methods paper that similarly builds complexity in visible steps see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md).
