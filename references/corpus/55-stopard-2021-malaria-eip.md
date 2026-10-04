# 55 — Stopard, Churcher & Lambert (2021), *PLoS Computational Biology*
**"Estimating the extrinsic incubation period of malaria using a mechanistic model of sporogony"**
Stopard IJ, Churcher TS, Lambert B. *PLoS Comput Biol* 17(2):e1008658. doi:10.1371/journal.pcbi.1008658.

**Archetype:** *parameter estimation*, mechanistically — the parameter is defined by a biological process, so the process is modelled at every scale that generates the data, and the parameter falls out of the fit. The counterpart to the statistical estimation in Lauer 2020 and Ganyani 2020, and the corpus's **multiscale model** exemplar.

## Structure
PLoS Comput Biol: `Abstract` → **`Author summary`** → `Introduction` (which teaches the parasite life cycle before any model) → `Methods`, organised by **biological scale** — parasite scale · mosquito scale · observation scale → `Results` → `Discussion` → `Supporting information` → `Data Availability`.

**Organising Methods by scale, from the parasite upward to the experiment, is the structural signature of a multiscale model.** Each section states what that level contributes to the observed data, so a reader can see exactly where each "hidden process" enters.

The supporting information is worth noting as a model of what to deposit: a **Mathematica notebook demonstrating the derivation**, the prior table, full posterior values, EIP estimates by temperature as a spreadsheet, and the Kaplan–Meier survival curves of the input data.

## Opening move
> "Malaria remains a leading cause of morbidity and mortality worldwide, with an extremely inequitable distribution: over 400,000 people, primarily children under the age of five in sub-Saharan Africa, die annually due to malaria."

Burden, with the inequity named rather than averaged away. Then the chain that makes *this* parameter the one worth estimating:
> "The widespread use of vector control tools that kill adult Anopheles mosquitoes is largely responsible for a historical decline in malaria incidence; a result foretold by early mathematical models, which predicted the sensitivity of malaria transmission to adult mosquito survival. For a newly infected mosquito to become infectious, it must survive the extrinsic incubation period (EIP). Since the EIP is long relative to mosquito life expectancy, only older mosquitoes can pass on infection meaning malaria transmission responds acutely to changes in survival."

**Four sentences from global burden to the specific parameter**, each link a mechanism: control works by killing mosquitoes → it works because the EIP is long relative to lifespan → therefore the EIP governs transmission. The paper has justified its estimand before naming its method.

**The gap is a mismatch between what the estimator measures and what the biology is:**
> "The EIP is typically estimated as the time for a given percentile, x, of infected mosquitoes to develop salivary gland sporozoites (the infectious parasite life stage), which is denoted by EIP_x. Many mechanisms, however, affect the observed sporozoite prevalence including the human-to-mosquito transmission probability and possibly differences in mosquito mortality according to infection status."

The conventional estimate is a property of the *observed data*; the quantity of interest is a property of the *parasite*. Everything that intervenes between them — who got infected at all, and who survived to be dissected — is confounded into the standard estimate.

## Methods
- **Teach the biology in sequence before modelling it**, with each stage named: female mosquitoes feed; a proportion "as determined by the human-to-mosquito transmission probability, ingest male and female Plasmodium gametocytes within the red blood cells (RBCs) of the blood-meal"; environmental change triggers gametogenesis; "Fertilisation occurs within the mosquito midgut, where gametes fuse into a single zygote, which differentiates into a motile ookinete". Every later model compartment has a named biological referent.
- **State a distributional assumption and then spell out everything it implies**, which is rarer and more valuable than stating it alone:
  > "that is, we assume that the time it takes a subsequent oocyst to burst into sporozoites is independent of the initial time taken for the oocyst to develop. **This assumption also implies the transitions of each parasite occur independently, meaning density dependent population dynamics do not occur.**"

  The second sentence names the biological consequence a reader would otherwise have to derive.
- **Give the parameterisation explicitly** so posteriors are interpretable: "We assume a parameterisation of the gamma distribution such that its mean is E(T_i) = α_i/β_i … α_i is the shape parameter and β_i is the rate parameter."
- **Say when an analytic result does not exist, and what you did instead**:
  > "An analytic form for the cumulative density function (CDF) of the sum of two gamma distributed random variables with different rate (β) parameters is currently not known. This aggregate distribution can, however, be approximated by a gamma distribution where the mean, λ, and variance, σ, match that of the true distribution."

  **Name the mathematical obstacle, then the approximation and the matching conditions.** A reader can judge the approximation because they know what it replaces.
- **Model the heterogeneity in the inoculum rather than assuming a uniform dose**: "When feeding on infectious blood, mosquitoes receive a heterogeneous load of gametocytes, with some receiving none at all. Additionally, not all parasites develop into the observed oocyst stage due to the innate immune resp[onse]…"

## Results
**Report the headline as a comparison against the incumbent method, in the units that matter**:
> "Fitting this model to experimental data, we find greater variation in the EIP than previously thought: we estimated the range between EIP₁₀ and EIP₉₀ (at 27°C) as 4.5 days compared to 0.9 days using existing statistical methods."

A fivefold difference in the *spread*, not the central estimate — and spread is what matters, because only mosquitoes that survive the EIP transmit. **State which feature of the distribution your method changes**, not merely that estimates differ.

**Check that the headline is not an artefact of one condition**: "This pattern holds over the range of study temperatures included in the dataset."

**Give the covariate effect over its full observed range with both endpoints**: "Increasing temperature from 21°C to 34°C decreased the EIP₅₀ from 16.1 to 8.8 days."

**Explain why a second estimate differs from the conventional one, by naming the bias the model removes:**
> "accounting for potential differences in mortality is essential to avoid bias in parameter estimates: our estimates of the human-to-mosquito transmission probability, for example, were higher than those estimated by the logistic model. By modelling mosquito infection and survival in a single framework we could estimate malaria infection induced differences in mosquito survival, whilst accounting for mosquitoes that do not develop oocysts within the infectious blood fed group."

**Report an unresolved controversy as unresolved**, and say why you modelled it anyway: "The influence of parasite-induced mosquito mortality is still a source of debate and likely to vary depending on the parasite-vector system. Nonetheless, accounting for potential differences in mortality is essential to avoid bias."

## Literature
Numbered PLoS citations. The literature is used to supply the biology (life-cycle stages, immune responses, prior survival data from three published studies) rather than to review modelling approaches, and the acknowledgements credit the experimentalists whose data the paper reanalyses by name and laboratory — "we would like to thank Professor Matthew Thomas for useful insight and the Thomas lab at Penn State University for producing and publishing the high-quality data upon which our study is based."

**Credit the people who generated the data you reanalysed, by name.**

## Voice
First-person plural, present tense for the model and past for the fitting. Assumptions are flagged with "we assume" at the point of use. Claims about fit are deliberately modest — "demonstrated it can produce a reasonable visual fit to the data across a range of experimental protocols" — where a stronger claim would not be supported by a visual assessment.

## Discussion and limitations
Opens by naming the problem with the data-generating process, which is the paper's reason to exist:
> "Membrane feedings assays form the bulk of experiments used to determine key parasitological parameters of malaria transmission, but despite the seeming simplicity of these experiments, numerous hidden processes contribute to the observed data. Here, we applied a systems biology approach to develop a multiscale model of the temporal dynamics of sporogony (mSOS) that explicitly accounts for these underlying processes."

**"[D]espite the seeming simplicity of these experiments, numerous hidden processes contribute to the observed data" is the generic justification for mechanistic estimation**, and transfers to any assay-derived parameter.

**The central claim is about the definition of the estimate, not its value:**
> "By adopting a mechanistic approach, our EIP estimates are defined in terms of the underlying biology rather than characteristics of the raw experimental data."

An estimate defined by biology transfers across experimental protocols; one defined by the shape of a particular dataset does not. **Say what your estimate is a property of.**

Then the consequence for users and the route to it: "Our estimates indicate greater variation in the EIP than previously thought and highlight the importance of accounting for this variation when making epidemiological predictions… This variation could be included by embedding mSOS within transmission dynamics models of malaria."

Closes on what the method makes possible and what it would need, framed as a call for a working relationship rather than for data in the abstract:
> "The model we introduce here provides a new way to parse dissection data to probe the underlying biology. Our model, or ones like it, could be extended to incorporate more fine scale characteristics of parasite ecology, but to do so in a principled manner requires more fine scale data. As such, we foresee a great necessity and opportunity for closer collaboration between experimentalists and modellers in the future."

**Tie a request for better data to the specific extension it would enable**, rather than asking for more data generally.

## Data, code and funding
All data in a public GitHub repository, the derivation deposited as an executable notebook, priors and full posteriors supplied as supplementary tables, and a funder-role statement: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript."

**Depositing the derivation as a runnable notebook** — not only the fitting code — is unusual and worth copying for any paper whose contribution includes an analytic result.

## Distinctive moves to borrow
1. **Justify the estimand before the method**, in a chain of mechanisms from burden to parameter.
2. **State the mismatch between what the conventional estimator measures and what the quantity is**, naming the processes confounded into it.
3. **Organise Methods by biological scale**, saying what each level contributes to the observed data.
4. **Teach the life cycle before modelling it**, so every compartment has a biological referent.
5. **Spell out what a distributional assumption implies** — independence here means no density dependence — not just that it was made.
6. **Name a missing analytic result and the approximation that replaces it**, with the matching conditions.
7. **Report which feature of the distribution your method changes** — here the spread, fivefold — and check it holds across conditions.
8. **Give covariate effects across the full observed range**, with both endpoints.
9. **Explain a divergence from the incumbent estimate by naming the bias you removed.**
10. **Report an unresolved biological controversy as unresolved**, and justify modelling it anyway.
11. **Say what your estimate is a property of** — the biology, not the dataset — because that determines whether it transfers.
12. **Tie a request for better data to the specific extension it would enable.**
13. **Deposit the derivation as a runnable notebook**, and credit the experimentalists whose data you reanalysed.

## Related files
For statistical estimation of an interval from reported cases see [07-lauer-2020-incubation-period](07-lauer-2020-incubation-period.md) and [54-ganyani-2020-generation-interval](54-ganyani-2020-generation-interval.md); for the within-host scale modelled for its own sake see [41-pawelek-2012-within-host-influenza](41-pawelek-2012-within-host-influenza.md); for malaria immunity estimated from age-stratified data see [46-griffin-2015-malaria-immunity](46-griffin-2015-malaria-immunity.md); for how delay-distribution variance propagates into transmission estimates see [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md).
