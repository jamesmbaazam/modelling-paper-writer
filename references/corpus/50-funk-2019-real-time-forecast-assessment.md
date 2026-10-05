# 50 — Funk et al. (2019), *PLoS Computational Biology*
**"Assessing the performance of real-time epidemic forecasts: A case study of Ebola in the Western Area region of Sierra Leone, 2014-15"**
Funk S, Camacho A, Kucharski AJ, Lowe R, Eggo RM, Edmunds WJ. *PLoS Comput Biol* 15(2):e1006785. doi:10.1371/journal.pcbi.1006785.

**Archetype:** *forecast evaluation*, in its hardest form — assess forecasts **you issued in real time**, after the fact, against what happened, using metrics that separate different kinds of being wrong. The corpus's foundational paper for the calibration/sharpness/bias decomposition.

## Structure
PLoS Comput Biol: `Abstract` → `Author summary` → `Introduction` → `Materials and methods` (*Ethics statement* · *Data sources* · model · **one subsection per metric**) → `Results` → `Discussion` → `Data Availability` → `Funding Statement`.

**Each evaluation metric gets its own methods subsection with its formula, its interpretation and its degenerate cases.** For an evaluation paper the metrics *are* the methods, and a reader must be able to adopt one without adopting the rest.

## Opening move
> "Real-time forecasts based on mathematical models can inform critical decision-making during infectious disease outbreaks. Yet, epidemic forecasts are rarely evaluated during or after the event, and there is little guidance on the best metrics for assessment."

Two gaps in one sentence — forecasts are not evaluated, and there is no agreed way to evaluate them — and the paper addresses both. The Introduction sharpens the first into a checkable observation about the field's practice: "forecasts made during an outbreak are rarely investigated during or after the event for their accuracy, and only recently have forecasters begun to make results, code, models and data available for retrospective analysis."

**Describe the existing evaluation infrastructure and its limitation honestly**, including the authors' own community:
> "The growing importance of infectious disease forecasts is epitomised by the growing number of so-called forecasting challenges… Such initiatives are difficult to set up during unexpected outbreaks, and are therefore usually conducted on diseases known to occur seasonally, such as dengue and influenza. The Ebola Forecasting Challenge was a notable exception… Since the epidemic had ended in most places at that time, the challenge was based on simulated data designed to mimic the behaviour of the true epidemic instead of real outbreak data."

**Name what the existing evidence base cannot tell you** — challenges run on simulated data after the fact — which is exactly the gap a retrospective evaluation of genuinely real-time forecasts fills. Prior lessons are credited in a numbered list before the gap is claimed.

## Methods
- **Establish that the forecasts were genuinely prospective**, with the date and the publication mechanism: "We produced weekly sub-national real-time forecasts during the Ebola epidemic, starting on 28 November 2014. Plots of the forecasts were published on a dedicated web site and updated every time a new set of data were available." A forecast that was published at the time cannot be quietly revised later, which is what makes the evaluation meaningful.
- **Say what the model was used for operationally**, so the evaluation has stakes: the forecasts were produced for "an area that saw one of the greatest number of cases in the region and where our model informed bed capacity planning."
- **Define each metric with its formula, its scale and its extremes.** Sharpness is the model case:
  > "Sharpness is the ability of the model to generate predictions within a narrow range of possible outcomes. It is a data-independent measure, that is, it is purely a feature of the forecasts themselves."

  then the estimator and why it was chosen over the obvious one — "The MAD (i.e., the MADN without the normalising factor) is related to the interquartile range… a common measure of sharpness, but is more robust to outliers" — then the normalisation that makes it interpretable, "division by 0.675 ensures that if the predictive distribution is normal this yields a value equivalent to the standard deviation", then the degenerate cases: "The sharpest model would focus all forecasts on one point and have S = 0, whereas a completely blurred forecast would have S → ∞."

  **Give a metric's formula, its units, why not the obvious alternative, and what its extreme values mean.** A reader can then adopt it without re-deriving it.
- **Say that sharpness is data-independent.** It is the one property of a forecast that can be judged without knowing the outcome, which is why it must be reported alongside calibration rather than instead of it.
- **Name the software for each metric**: "The goftest package was used for the Anderson-Darling test and the scoringRules package for the RPS and DSS", with all scoring code "implemented in the R package accompanying the paper".
- **Compare against null models** — autoregressive and simpler variants — so "good" has a floor.

## Results
**Report the fitted quantity's trajectory with full uncertainty at several dates**, rather than a single headline:
> "one of a near-monotonic decline, from a median estimate of 2.9 (interquartile range (IQR) 2.1–4, 90% credible interval (CI) 1.2–6.9) in the first fitted week (beginning 10 August, 2014) to a median estimate of 1.3 (IQR 0.9–1.9, 90% CI 0.4–3.7) in early November, 0.9 (IQR 0.6–1.3, 90% CI 0.2–2.2) in early December, 0.6 in early January (IQR 0.3–0.8, 90% CI 0.1–1.5) and 0.3 at the end of the epidemic in early February (IQR 0.2–0.4, 90% CI 0.1–0.9)."

Two intervals per estimate (IQR and 90%) and a date for each — the reader can see both the central trend and how wide the uncertainty stayed.

**Report the result as a usable horizon, not a score.** The finding that matters to a decision-maker is how far ahead the forecasts could be trusted:
> "good probabilistic calibration was achievable at short time horizons of one or two weeks ahead but model predictions were increasingly unreliable at longer forecasting horizons. This suggests that forecasts may have been of good enough quality to inform decision making based on predictions a few weeks ahead of time but not longer."

**Translate an evaluation into a statement about what the forecast may be used for.** This is the single most transferable move in the paper.

**Present the metrics as a table with one row per model and one column per metric** — calibration, sharpness, bias, RPS, DSS, AE — so the trade-offs are visible rather than aggregated away, with "p-values for calibration highlighted in bold reflect predictive models with no evidence of miscalibration."

**Report whether the right model could have been identified at the time**, which is the question a forecaster actually faces:
> "Comparing forecasts based on the semi-mechanistic model to simpler null models showed that the best semi-mechanistic model variant performed better than the null models with respect to probabilistic calibration, and that this would have been identified from the earliest stages of the outbreak."

**Ask whether the evaluation would have been actionable in real time**, not only whether the model was good in hindsight.

## Literature
Numbered PLoS citations, concentrated in the Introduction where the forecasting-challenge literature is summarised and in the Discussion where ensemble methods and post-processing are brought in from weather forecasting — "Such ensemble forecasts have become a standard in weather forecasting and have more recently shown promise for infectious disease forecasts." The methodological borrowing is explicit: "Methods to assess probabilistic forecasts are now being used in other fields, but are not commonly applied in infectious disease epidemiology."

## Voice
First-person plural throughout, and unusually willing to evaluate the authors' own work critically — the forecasts assessed are their own, and the conclusion is that they were unreliable beyond two or three weeks. Claims are tied to the model class rather than generalised: "using the type of models we used, it was possible to reliably predict the epidemic for a maximum of one or two weeks ahead, but no longer."

## Discussion and limitations
Opens by arguing why probabilistic forecasting matters operationally, with the decision it serves:
> "In the context of infectious disease outbreaks, they allow the forecaster to go beyond merely providing the most likely future scenario and quantify how likely that scenario is to occur compared to other possible scenarios… Especially during acute outbreaks, decisions are often made based on so-called 'worst-case scenarios' and their likelihood of occurring. The ability to adequately assess the magnitude as well as the probability of such scenarios requires accuracy at the tails of the predictive distribution, in other words good calibration of the forecasts."

**Derive the choice of metric from the decision it supports.** Worst-case planning needs the tails, so calibration is the priority — not an abstract preference for proper scoring rules.

Then the proposed workflow, stated as a two-stage rule others can adopt: treat "probabilistic calibration as a prerequisite to the use of forecasts", and "Once a subset of models has been selected in an attempt to discard miscalibrated models, other criteria such as the RPS or DSS can be used to select the best model for forecasts, or to generate weights for ensemble forecasts."

Limitations are specific and concede the obvious objection first: "Other models may have performed better than the ones presented here. Because we did not have access to data that would have allowed us to assess the importance of different transmission routes (burials, hospitals an[d so on])…" — the limitation is tied to a data gap rather than left as a general caveat. The deterioration with horizon is explained rather than merely reported: it "reflects our lack of knowledge about the underlying processes shaping the epidemic at the time, from public health interven[tions onwards]".

Closes on the field-level argument: "As forecasts become a routine part of the toolkit in public health, standards for evaluation of performance will be important for assessing quality and improving credibility of mathematical models, and for elucidating difficulties and trade-offs when aiming to make the most useful and reliable forecasts."

## Data, code and funding
Exemplary and minimal: "All data and code are contained in an R package available at https://doi.org/10.5281/zenodo.2547701" — a single archived DOI containing both, shipped as an installable package. Ethics approval is stated with its reference number; every author's fellowship and grant number is itemised.

## Distinctive moves to borrow
1. **Evaluate your own real-time forecasts after the fact**, and say where they failed. Self-evaluation is the most credible form of forecast evaluation available.
2. **Establish prospectivity concretely** — the date forecasting began, and that the forecasts were published as they were made.
3. **Decompose "accuracy" into calibration, sharpness and bias**, and report all three; a sharp forecast that is wrong and a vague forecast that is right fail differently.
4. **Note which metrics are data-independent** (sharpness) and which require the outcome.
5. **Define each metric with formula, normalisation, why not the obvious alternative, and the meaning of its extremes.**
6. **Derive your choice of metric from the decision the forecast serves** — worst-case planning needs calibrated tails.
7. **Report the result as a usable forecast horizon**, not as a score.
8. **Ask whether the best model could have been identified at the time**, not only in hindsight.
9. **Table the metrics by model so trade-offs stay visible** rather than collapsing them into one number.
10. **Propose a two-stage selection rule** — discard miscalibrated models, then rank the survivors — that others can apply.
11. **Ship data and code as one archived, installable package** under a single DOI.

## Related files
For the multi-model hub evaluations this method underpins see [09-cramer-2022-covid-forecast-hub-evaluation](09-cramer-2022-covid-forecast-hub-evaluation.md), [10-reich-2019-flusight-multiyear](10-reich-2019-flusight-multiyear.md) and [51-sherratt-2023-european-forecast-hub](51-sherratt-2023-european-forecast-hub.md); for the scoring rule itself see [11-bracher-2021-weighted-interval-score](11-bracher-2021-weighted-interval-score.md) and for the scale it is applied on [52-bosse-2023-transformed-scales](52-bosse-2023-transformed-scales.md); for the real-time Ebola modelling this paper assesses see [44-finger-2019-diphtheria-rapid-response](44-finger-2019-diphtheria-rapid-response.md); for pre-registered forecasting see [53-bracher-2021-preregistered-forecasts](53-bracher-2021-preregistered-forecasts.md). Other *forecast evaluation* exemplars: see [71-wolffram-2023-nowcast-hub](71-wolffram-2023-nowcast-hub.md) for the hub design applied to nowcasts, pre-registered, with the evaluation target itself put to a sensitivity test.
