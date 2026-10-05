# 73 — Shi et al. (2016), *Environmental Health Perspectives*
**"Three-month real-time dengue forecast models: an early warning system for outbreak alerts and policy decision support in Singapore"**
Shi Y, Liu X, Kok SY, Rajarethinam J, Liang S, Yap G, et al. *Environ Health Perspect* 124(9):1369–1375. doi:10.1289/ehp.1509981.

**Archetype:** the *operational early-warning forecast* — a statistical forecasting system built inside a national agency, validated out of sample, and used to move resources ahead of an outbreak. It belongs with the rapid-response papers because its deliverable is a dated warning acted on: in March 2013 it forecast a June peak near the one that came, and the national campaign launched two months early. Its evaluation is thinner than its operational record, and the file says where.

## Structure
EHP structured abstract (**Background / Objectives / Methods / Results / Conclusions**) → `Introduction` → `Materials and Methods` (*Statistical Analyses* · *Other Approaches* · *Model Comparison* · *Data*) → `Results` → `Discussion` → `Conclusion`.

**Data come last in Methods**, after the model and its comparators — the reverse of the usual order, and workable here because each data stream is a candidate covariate rather than the object of the analysis.

## Opening move
> "Dengue is an acute infectious disease common to tropical and subtropical regions."

The Introduction moves from global burden to Singapore's particular exposure — equatorial, aseasonal, all four serotypes, "approximately 200 USD per capita per year" in economic cost — to the absence of a vaccine, which makes vector control the only lever and lead time the thing a forecast can buy.

**The strongest move is a list of criteria any operational forecast must meet, stated before the method**:
> "Any statistical approach to forecast dengue would need to meet certain criteria to be practical: a ) use only data that are available at the time the forecast is made; b ) be capable of forecasting weeks or months into the future to give lead time for preparing a public health response (for instance, hiring new control staff); c ) possess validated and demonstrated predictive performance using data that were not used in its construction, to prevent over-fitting and to ascertain confidence levels; and lastly, d ) be able to process new data rapidly."

**Prior work is then judged against the same criteria**:
> "Although the aforementioned models meet many of the criteria noted above, it is noteworthy that none has been validated against data not used in its construction, and none was developed explicitly for operational use, suggesting that their predictive performance and usefulness to operations were not tested."

**Set out the criteria a useful answer must meet, then show the literature fails them** — a gap the reader can check, rather than an absence of work. Criterion (b)'s parenthesis, "hiring new control staff", ties lead time to a decision with its own lag.

**The trade-off between mechanistic and statistical models is stated fairly, with the condition under which the statistical choice fails**:
> "In contrast, correlative statistical approaches—which describe the phenomenon but not the underlying process—are well suited to integration with multiple live data streams and may have good predictive accuracy if future conditions do not stray too far from the conditions used to parameterize them."

## Methods
- **Explain the method in plain terms for a public-health readership**: LASSO "extends standard regression and related models such as logistic regression by simultaneously selecting which parameters to include in the model and what their values should be", with cross-validation described step by step.
- **Fit a separate model for each horizon, and say what that buys**: one submodel per forecast week from 1 to 12, so that each horizon can use its own predictors — and, from the Discussion, "Having distinct submodels also obviates the need to forecast future values of the predictors, which would be the case if a single model for 1 week ahead were used and then iterated to obtain longer-term forecasts."
- **Compare against the methods the local literature used**, re-implemented: seasonal ARIMA and step-down linear regression, both from earlier Singapore studies, on "The same training and validation data sets".
- **Split time three ways**: train on 2001–2010, validate on 2011–2012, then apply the validated models to the 2013 epidemic, the largest on record.
- **Construct a covariate to cancel a known sampling bias, and argue for the assumption it rests on.** The vector data come from control operations, which "tend to favor outbreak periods and areas with transmission, thus biasing estimates upwards". The index is therefore the share of breeding sites that hold the main vector, with the other, ubiquitous species standing in for search effort:
  > "There are two justifications for this assumption: a ) another Aedes species, Ae. albopictus, is so widespread that the amount of Ae. albopictus breeding found is a good proxy for total effort in identifying breeding sites, and b ) Ae. aegypti is the primary vector for dengue in Singapore"

  **When surveillance effort follows the outcome, build the covariate as a ratio that divides the effort out**, and state why the denominator measures effort.

## Results
**Accuracy by horizon, against both comparators, with intervals**:
> "Notably, the MAPE degrades slowly over time under the LASSO approach, with a rise from 17% error [95% confidence interval (CI): 16, 19%] forecasting 1 week to 24% error (95% CI: 22, 26%) forecasting 3 months into the future. In contrast, both the step-down and SARIMA approaches had a MAPE of 29% at 3 months ahead"

**Coverage is reported separately from accuracy**: "although the LASSO and SARIMA predictions were conservative in the sense that the actual coverage of prediction intervals exceeded the target of 95%, the step-down approach led to forecasts that understated the uncertainty".

**The misses are reported alongside the successes**: "The start and end of several epidemics were accurately forecasted by both the LASSO and step-down approaches, although the peak of the large 2005 outbreak was not well described by the LASSO model." The 2013 forecasts are walked through at four dates, including the first, which was wrong: "Early in the epidemic, the model forecast was of a mild rise, which was exceeded by the actual epidemic… Overall, the model predicted a slightly more rapid end to, and smaller size of, the epidemic than that which occurred."

**The covariate effects are reported with a warning about reading them**: "Interpretation of climatic and other factors was difficult because the strength of their association varied between forecast windows and because they operated over different time lags."

## Literature
Author–year citations in the EHP style. Earlier Singapore forecasting studies are described one by one — method, horizon, data — before the shared weakness is named, so the criticism follows from the description.

## Voice
First-person plural. The operational account uses dates and counts rather than adjectives. The Conclusions of the abstract are broader than the evidence — LASSO models "have the potential to markedly improve forecasting techniques for recurrent infectious disease outbreaks such as dengue" — on the strength of one city and one comparison.

## Discussion and limitations
**The main limitation is stated from the user's side**:
> "The largest of these limitations is that although very good predictive accuracy can be achieved, the 12 models built using the LASSO method are not amenable to interpretation because they were constructed for their predictive accuracy, not to explain the etiology of outbreaks. In particular, attempts to explain to stakeholders why the model forecast a large epidemic in 2013 were hindered by the numerous covariates acting at different lags."

**Describe a limitation by the moment it caused a problem.** The forecast was right and still hard to act on, because nobody could say why it was right. The size of the problem is given: roughly 60 of more than 200 candidate predictors in the 12-week model, "the same covariate was often selected at different lags and frequently was selected with differently signed coefficients at those different lags." A remedy is proposed — feed a mechanistic mosquito model's output in place of raw weather.

**The operational record is the paper's real evidence, and it is specific**:
> "In late March 2013, our models forecasted an earlier-than-usual increase in dengue cases in June 2013, which could potentially peak at 800 cases/week. Specifically, the forecast predicted a peak in case count of 863 during the 26th week of 2013, which is very close to the observed number of cases, which peaked at 842 cases/week during the 25th week."

and what was done with it: the forecasts "helped guide hospital bed management and public health interventions, including preemptive source reduction measures, recruitment of ground staff, and education campaigns", and the forecast "facilitated early risk communication to the public and the advanced launch of Dengue Campaign in April, 2 months ahead of its traditional June launch."

**Give the forecast's date, the predicted value, the observed value and the decision it changed.** That sentence does more for the paper's claim than the MAPE table.

**The horizon is bounded by use and by its inputs**: "We restricted the forecast window to 12 weeks to avoid the increased level of inaccuracy that accompanies long-term projection and because short- (several weeks) and medium-term (several months) projections are the most useful for local planning purposes", and going further would need weather forecasts that are not available that far ahead.

## Distinctive moves to borrow
1. **State the criteria an operational forecast must meet** before introducing the method.
2. **Judge prior work against those criteria**, so the gap is checkable.
3. **Tie lead time to a decision with its own lag** — hiring staff.
4. **State when a statistical model will fail**: when future conditions stray from those it was fitted to.
5. **Fit one model per horizon** and say what that avoids — forecasting the predictors.
6. **Re-implement the local literature's methods as comparators** on identical data splits.
7. **Build a covariate as a ratio that cancels surveillance effort**, and justify the denominator.
8. **Report coverage separately from accuracy.**
9. **Walk through the forecasts at several dates of one epidemic**, including the early one that was wrong.
10. **Describe a limitation by the moment it caused trouble** — explaining a forecast to stakeholders.
11. **Give the forecast date, predicted value, observed value and the decision changed.**

## What to avoid from this paper
- **One error metric, and not a proper score.** MAPE scores only the point forecast and penalises over- and under-prediction asymmetrically; `evidence.md` §6.2 asks for a proper scoring rule on the predictive distribution. Compare [71-wolffram-2023-nowcast-hub](71-wolffram-2023-nowcast-hub.md), which reports the weighted interval score and its decomposition.
- **Prediction intervals from the residual standard deviation.** Intervals built by overlaying the fitted residual error ignore parameter uncertainty and the horizon's own error structure; the coverage above 95% is reported as "conservative" when it is a calibration failure in the other direction.
- **A circular claim offered as an advantage**: "Tautologically, by selecting the model complexity using cross-validation to optimize predictive performance, predictive performance of the routine is optimized". Cross-validation optimises the validation criterion, not performance on the next epidemic.
- **No naive baseline.** Both comparators are fitted models; a seasonal-average or persistence forecast would show how much of the skill any model adds.
- **No code or data-availability statement.** The data sources are named and linked, but the forecasting routine itself is not shared.

## Related files
For rapid-response forecasts of beds during an epidemic see [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md) and [44-finger-2019-diphtheria-rapid-response](44-finger-2019-diphtheria-rapid-response.md); for the global distribution and burden of dengue see [29-bhatt-2013-global-dengue-distribution](29-bhatt-2013-global-dengue-distribution.md); for proper scoring rules and baselines see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md) and [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md); for the rules on predictive models see `references/ml-prediction.md`.
