# 31 — Lazer, Kennedy, King & Vespignani (2014), *Science*
**"The Parable of Google Flu: Traps in Big Data Analysis"**
*Science* 343(6176):1203–1205. doi:10.1126/science.1248506.
**Citations:** ~2,600 (OpenAlex, Sept 2026).

**Archetype:** the *critique* — a short Policy Forum piece that diagnoses why a celebrated data-driven model failed, and generalises the diagnosis into named, portable failure modes. The template for writing a criticism that is useful rather than merely correct.

## Structure
~2,000 words. Named-concept headings, each introducing a term the paper is coining or repurposing:
`Big Data Hubris` → `Algorithm Dynamics` → `Transparency, Granularity, and All-Data` (with sub-labelled lessons: *Transparency and Replicability*, and further lessons on study of the algorithm and on combining methods).

**The headings are the contribution.** "Big data hubris" and "algorithm dynamics" are the phrases that got cited thousands of times. If your critique identifies a recurring failure, give it a short name and put that name in a heading.

## Opening move
> "In February 2013, Google Flu Trends (GFT) made headlines but not for a reason that Google executives or the creators of the flu tracking system would have hoped. Nature reported that GFT was predicting more than double the proportion of doctor visits for influenza-like illness (ILI) than the Centers for Disease Control and Prevention (CDC), which bases its estimates on surveillance reports from laboratories across the United States. This happened despite the fact that GFT was built to predict CDC reports. Given that GFT is often held up as an exemplary use of big data, what lessons can we draw from this error?"

Pattern: **a dated, specific, verifiable failure → the sharpest possible statement of the paradox ("built to predict CDC reports") → a question, not an accusation.** The paper opens by asking what can be learned, which licenses everything critical that follows.

Then it immediately widens the scope so the piece is not merely about one product:
> "The problems we identify are not limited to GFT. Research on whether search or social media can predict x has become commonplace and is often put in sharp contrast with traditional methods and hypotheses. Although these studies have shown the value of these data, we are far from a place where they can supplant more traditional methods or theories."

## The two named failure modes

**1. Big data hubris.** Defined immediately after being named:
> "'Big data hubris' is the often implicit assumption that big data are a substitute for, rather than a supplement to, traditional data collection and analysis."
Then the authors declare their own priors before criticising, which disarms the obvious rejoinder:
> "We have asserted that there are enormous scientific possibilities in big data. However, quantity of data does not mean that one can ignore foundational issues of measurement, construct validity and reliability, and dependencies among data."
Then the arithmetic that makes the criticism unanswerable:
> "Essentially, the methodology was to find the best matches among 50 million search terms to fit 1152 data points. The odds of finding search terms that match the propensity of the flu but are structurally unrelated, and so do not predict the future, were quite high."
And the killer observation — that the original paper reported the evidence against itself:
> "GFT developers, in fact, report weeding out seasonal search terms unrelated to the flu but strongly correlated to the CDC data, such as those regarding high school basketball. This should have been a warning that the big data were overfitting the small number of cases, a standard concern in data analysis."
Then the epigram: **"In short, the initial version of GFT was part flu detector, part winter detector."**

**2. Algorithm dynamics** — the deeper and more original point:
> "All empirical research stands on a foundation of measurement. Is the instrumentation actually capturing the theoretical construct of interest? Is measurement stable and comparable across cases and over time? Are measurement errors systematic?"
> "Algorithm dynamics are the changes made by engineers to improve the commercial service and by consumers in using that service."
> "In improving its service to customers, Google is also changing the data-generating process."
> "GFT bakes in an assumption that relative search volume for certain terms is statically related to external events, but search behavior is not just exogenously determined, it is also endogenously cultivated by the service provider."

The generalisation is stated so it outlives the example: "Blue team issues are not limited to Google. Platforms such as Twitter and Facebook are always being re-engineered, and whether studies conducted even a year ago on data collected from these platforms can be replicated in later or earlier periods is an open question." A companion category, "red team" dynamics, covers deliberate manipulation by the people being measured.

## Evidence conventions
Criticism is quantified, dated, and structural rather than anecdotal:
> "GFT also missed by a very large margin in the 2011–2012 flu season and has missed high for 100 out of 108 weeks starting with August 2011."
> "These errors are not randomly distributed. For example, last week's errors predict this week's errors (temporal autocorrelation), and the direction and magnitude of error varies with the time of year (seasonality). These patterns mean that GFT overlooks considerable information that could be extracted by traditional statistical methods."
> "Even 3-week-old CDC data do a better job of projecting current flu prevalence than GFT."

**The strongest form of a critique is a benchmark the target loses to.** "Three-week-old CDC data" is devastating precisely because it is so unambitious.

Alternative explanations are considered and dismissed on evidence, not by assertion: media panic "may have been a factor, [but] it cannot explain why GFT has been missing high by wide margins for more than 2 years", since the 2009 model "has weathered other media panics".

## Constructive turn
The piece refuses to conclude that the enterprise is worthless, and does so explicitly with a rhetorical question and a one-word answer:
> "does this mean that the current version of GFT is not useful? No, greater value can be obtained by combining GFT with other near–real time health data. For example, by combining GFT and lagged CDC data, as well as dynamically recalibrating GFT, we can substantially improve on the performance of GFT or the CDC alone."
> "This is no substitute for ongoing evaluation and improvement, but, by incorporating this information, GFT could have largely healed itself and would have likely remained out of the headlines."

Replicability is raised as a community standard rather than a personal failing:
> "The supporting materials for the GFT-related papers did not meet emerging community standards. Neither core search terms were identified nor larger search corpus provided."
> "GFT has never documented the 45 search terms used, and the examples that have been released appear misleading."

## Distinctive moves to borrow
1. **Name the failure mode and put the name in a heading.** A critique that supplies vocabulary gets cited; one that supplies only a correction does not.
2. **Open with a question, not a verdict.**
3. **State your own positive commitments before criticising** ("We have asserted that there are enormous scientific possibilities in big data").
4. **Do the arithmetic**: 50 million features, 1,152 observations. One ratio can carry an entire argument.
5. **Beat the target with an embarrassingly simple benchmark.**
6. **Quote the target's own paper against itself** — fairly, using something it disclosed.
7. **Consider and eliminate the defendant's best excuse** on evidence.
8. **End constructively**, with the fix, so the piece reads as method-building rather than score-settling.

## Related files
Critiques the method of [[30-ginsberg-2009-google-flu-trends]]; the constructive successor is [[34-yang-2015-argo-influenza]]. For the same critical function performed on a whole literature rather than one model, see [[35-wynants-2020-covid-prediction-models-review]] and [[36-roberts-2021-ml-covid-imaging-pitfalls]].
