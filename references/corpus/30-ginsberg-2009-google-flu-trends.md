# 30 — Ginsberg et al. (2009), *Nature*
**"Detecting influenza epidemics using search engine query data"**
Ginsberg J, Mohebbi MH, Patel RS, Brammer L, Smolinski MS, Brilliant L. *Nature* 457:1012–1014. doi:10.1038/nature07634.
**Citations:** ~4,400 (OpenAlex, Sept 2026).

**Archetype:** the *digital surveillance / data-driven nowcasting* paper — a purely correlational model over an enormous feature space, validated out of sample and sold on timeliness. Read together with [31-lazer-2014-parable-of-google-flu](31-lazer-2014-parable-of-google-flu.md), which is its post-mortem; the pair is the best teaching object in this corpus.

## Structure
A *Nature* Letter: one abstract paragraph, then ~2,500 words of continuous text with no headings at all, two figures, one table. Methods folded into the narrative; details in Supplementary Information.

## Opening move
> "Seasonal influenza epidemics are a major public health concern, causing tens of millions of respiratory illnesses and 250,000 to 500,000 deaths worldwide each year. In addition to seasonal influenza, a new strain of influenza virus against which no previous immunity exists and that demonstrates human-to-human transmission could result in a pandemic with millions of fatalities. Early detection of disease activity, when followed by a rapid response, can reduce the impact of both seasonal and pandemic influenza."

Pattern: **quantified burden → the worse contingency → the causal claim that makes speed valuable → "Here we present a method…".** The value proposition is stated as a *lag*, which is the only thing the method actually improves: estimates "with a reporting lag of about one day", against the CDC's "1–2-week reporting lag".

The abstract's final sentence is a bounded generalisation, not a boast: "This approach may make it possible to use search queries to detect influenza epidemics in areas with a large population of web search users." Note the conditional — the paper is explicit that the method needs a large search-using population.

## Methods — machine learning conventions
- **The model is deliberately, explicitly simple.** "We sought to develop a simple model… A single explanatory variable was used." The equation is given inline with every term glossed: `logit(I(t)) = α·logit(Q(t)) + ε`, "where I(t) is the percentage of ILI physician visits, Q(t) is the ILI-related query fraction at time t, α is the multiplicative coefficient, and ε is the error term. logit(p) is simply ln(p/(1 − p))."
- **The feature engineering is where the work is, and it is described as an automated procedure, not as insight**: "We designed an automated method of selecting ILI-related search queries, requiring no previous knowledge about influenza. We measured how effectively our model would fit the CDC ILI data in each region if we used only a single query as the explanatory variable… Each of the 50 million candidate queries in our database was separately tested in this manner."
- **Selection exploits structure in the data as an implicit regulariser**: "Our approach rewarded queries that showed regional variations similar to the regional variations in CDC ILI data: the chance that a random search query can fit the ILI percentage in all nine regions is considerably less than the chance that a random search query can fit a single location." Requiring agreement across nine regions is a defence against spurious fits — and the paper says so.
- **Model size chosen by out-of-sample fit, with the curve shown**: "we considered different sets of n top-scoring queries… and picked n such that we obtained the best fit against out-of-sample ILI data across the nine regions (Fig. 1)". Figure 1 plots mean correlation against number of queries, and n = 45 is read off the maximum.
- **Data preparation stated plainly, including what was excluded**: weekly counts normalised into a query fraction; "No data were provided for weeks outside of the annual influenza season, and we excluded such dates from model fitting, although our model was used to generate unvalidated ILI estimates for these weeks." That last clause is an honest flag that the model was being used outside its fitting domain — the exact circumstance in which it later failed during H1N1.
- **Validation is genuinely held out and quantified**: "The final model was validated on 42 points per region of previously untested data from 2007 to 2008, which were excluded from all previous steps. Estimates generated for these 42 points obtained a mean correlation of 0.97 (min = 0.92, max = 0.99, n = 9 regions)." An independent state-level check follows: Utah, correlation 0.90 across 42 points.
- Correlations are reported **with their min and max across regions and the n**, never as a bare average.

## The famous sentence
> "A steep drop in model performance occurs after adding query 81, which is 'oscar nominations'."

And in the text: other high-scoring queries "included topics like 'high school basketball', which tend to coincide with influenza season in the United States."

The paper **shows its spurious correlates** rather than hiding them. That is admirable disclosure — and it is also, as Lazer 2014 points out, the warning that the authors did not act on. If your feature-selection procedure surfaces nonsense predictors, report them *and* treat it as evidence about the procedure, not as a curiosity.

## Results
> "The model was able to obtain a good fit with CDC-reported ILI percentages, with a mean correlation of 0.90 (min = 0.80, max = 0.96, n = 9 regions)."
> "Google web search queries can be used to estimate ILI percentages accurately in each of the nine public health regions of the United States. Because search queries can be processed quickly, the resulting ILI estimates were consistently 1–2 weeks ahead of CDC ILI surveillance reports."
> "The early detection provided by this approach may become an important line of defence against future influenza epidemics in the United States, and perhaps eventually in international settings."

The claim is carefully limited to **estimating a CDC quantity faster**, not to forecasting or to replacing surveillance. The overreach that followed was largely other people's.

## Distinctive moves to borrow
**Copy:** the inline model with every symbol glossed; choosing model size by an out-of-sample curve you actually plot; validating on data excluded from *all* previous steps and reporting min/max across units; stating the improvement as a lag reduction; disclosing your spurious features.

**Do not copy:** fitting 50 million candidate features to ~1,100 weekly observations; treating a validated correlation with a target as evidence the relationship is structural; publishing without the search terms, which made replication impossible (see Lazer 2014); assuming the data-generating process is stationary when it is a commercial product under continuous modification.

## Related files
[31-lazer-2014-parable-of-google-flu](31-lazer-2014-parable-of-google-flu.md) is the critique; [34-yang-2015-argo-influenza](34-yang-2015-argo-influenza.md) is the successor that fixes the identified flaws and is explicit about doing so.
