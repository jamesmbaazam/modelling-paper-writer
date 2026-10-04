# 60 — Watson et al. (2022), *The Lancet Infectious Diseases*
**"Global impact of the first year of COVID-19 vaccination: a mathematical modelling study"**
Watson OJ, Barnsley G, Toor J, Hogan AB, Winskill P, Ghani AC. *Lancet Infect Dis* 22(9):1293–1302. doi:10.1016/S1473-3099(22)00320-6.

**Archetype:** *vaccine impact* — a counterfactual the world cannot run, estimated by fitting a transmission model to what happened and then re-simulating without the intervention. The deliverable is deaths averted, globally and by income group, with the shortfall against agreed targets priced in the same units.

## Structure
Lancet structured abstract (**Background / Methods / Findings / Interpretation**) → **`Research in context`** panel → `Introduction` → `Methods` → `Results` → `Discussion` → back matter. The genre label is in the title — "a mathematical modelling study" — as the Lancet family requires.

## Opening move
> "The first COVID-19 vaccine outside a clinical trial setting was administered on Dec 8, 2020. To ensure global vaccine equity, vaccine targets were set by the COVID-19 Vaccines Global Access (COVAX) Facility and WHO. However, due to vaccine shortfalls, these targets were not achieved by the end of 2021."

**Three sentences establishing a date, a commitment, and a failure to meet it.** The analysis window then follows from the first sentence — exactly one year from the first dose — and the second and third set up the counterfactuals the paper will price.

**The `Research in context` panel gives the search string and characterises every prior study by its scope limit:**
> "We found eight published studies that estimated the impact of COVID-19 vaccination, including deaths averted from vaccination. None of the studies considered the global impact of COVID-19 vaccination, focusing instead on specific regions (Italy, California, North Carolina, Stockholm, subsets of states in the USA, New York City, and the WHO European Region). Furthermore, the study focusing on the WHO European region only quantified the direct impact of vaccination and did not estimate the indirect effects (ie, decreasing infection risk of both vaccinated and unvaccinated susceptible individuals)."

**List the places prior studies covered.** It is a checkable claim, and it makes "global" a substantive contribution rather than a boast. The second sentence names the *methodological* gap — direct effects only — with the indirect effect defined parenthetically.

**The novelty claim is specific, bounded and tied to who benefits:** "This study is, to the best of our knowledge, the first to use excess mortality estimates in this way, allowing for the impact of COVID-19 vaccination to be estimated more accurately **in countries with weaker surveillance systems**."

## Methods
- **State the counterfactual as the definition of the estimand**: "The impact of COVID-19 vaccination programmes was determined by estimating the additional lives lost if no vaccines had been distributed."
- **Fit to two different outcome measures and report both throughout**, rather than choosing one:
  > "A mathematical model of COVID-19 transmission and vaccination was separately fit to reported COVID-19 mortality and all-cause excess mortality in 185 countries and territories."

  **Running the whole analysis twice against two measures of the same underlying quantity** converts a data-quality worry into a reported sensitivity — and the gap between the two answers becomes a finding in its own right (below).
- **Define the policy counterfactuals by the targets that were actually set**, with their owners and thresholds: "the additional deaths that would have been averted had the vaccination coverage targets of 20% set by COVAX and 40% set by WHO been achieved by the end of 2021." The scenarios are not invented by the modellers; they are the commitments the world made.
- **Say explicitly why a model is needed at all** — the clearest statement of the counterfactual argument in the corpus:
  > "Directly measuring the impact of vaccination programmes on COVID-19 mortality is not possible as the counterfactual (ie, without vaccinations) cannot be observed. Mathematical models are a valuable tool for quantifying the impact of vaccination campaigns on epidemic dynamics."

## Results
**Report the headline under both outcome measures, with the fraction it represents:**
> "Based on official reported COVID-19 deaths, we estimated that vaccinations prevented 14·4 million (95% credible interval [CrI] 13·7–15·9) deaths from COVID-19 in 185 countries and territories between Dec 8, 2020, and Dec 8, 2021. This estimate rose to 19·8 million (95% CrI 19·1–20·4) deaths from COVID-19 averted when we used excess deaths as an estimate of the true extent of the pandemic, representing a global reduction of 63% in total deaths (19·8 million of 31·4 million) during the first year of COVID-19 vaccination."

Note the construction "**63% in total deaths (19·8 million of 31·4 million)**" — the percentage with its numerator and denominator in parentheses, so the reader can check the arithmetic and see the counterfactual total.

**Disaggregate by the political unit the policy question concerns**: "In COVAX Advance Market Commitment countries, we estimated that 41% of excess mortality (7·4 million [95% CrI 6·8–7·7] of 17·9 million deaths) was averted."

**Price the shortfall against each target separately, in percentage-of-deaths-averted terms:**
> "In low-income countries, we estimated that an additional 45% (95% CrI 42–49) of deaths could have been averted had the 20% vaccination coverage target set by COVAX been met by each country, and that an additional 111% (105–118) of deaths could have been averted had the 40% target set by WHO been met."

The figure exceeding 100% is reported without softening — it means more than twice as many deaths again could have been averted — and the units are stated precisely enough that the reader can see why that is coherent rather than an error.

## Literature
Numbered Lancet citations, concentrated in the Introduction and the `Research in context` panel. Prior work is positioned by scope and by method rather than by quality.

## Voice
First-person plural, past tense for the analysis, conditional for the counterfactuals: "could have been averted", "would have been", "we predict that vaccine impact estimates would increase". Every counterfactual claim carries a modal; every fitted estimate does not. The Interpretation makes the equity claim in plain terms: "inadequate access to vaccines in low-income countries has limited the impact in these settings".

## Discussion and limitations
Opens by naming the two mechanisms behind the result — individual protection against severe disease and population-level protection against infection — with the variant caveat attached inline: "the population-level benefit afforded by mild protection against SARS-CoV-2 infection (**before the emergence of the omicron [B.1.1.529] variant**)".

The limitations are unusually good, and each is reasoned rather than listed:

- **A timing mismatch between the analysis window and the target deadline, with an argument that it barely matters**: "these targets were set to be reached by the end of 2021, whereas our modelling endpoint was Dec 8, 2021… Hence, some countries might have moved closer to achieving the targets, or achieved them, by the end of the year. However, any recent vaccination drives would have had consequently negligible impact given the delay in developing protection."
- **The counterfactual assumption named as the dominant source of variation in the answer** — the most important limitation in any impact study:
  > "Deriving estimates of vaccine impact is heavily dependent on the counterfactual scenario chosen. In our counterfactual, we assumed the same time-varying levels of SARS-CoV-2 transmission as estimated in our model fits. Consequently, the largest impact was observed in countries that delivered the most vaccinations to date and simultaneously relaxed interventions, allowing SARS-CoV-2 transmission to increase. However, several countries with slower vaccination roll-out as well as countries adopting a zero-COVID strategy maintained stronger interventions to suppress transmission and thus observed smaller impacts of their vaccination programmes as a result."

  **State which countries your counterfactual flatters and which it penalises, and why.** The estimate is not biased by accident; it is a consequence of a stated assumption, and the direction is given per country type — then extended into a prediction: "As these countries start to reopen, we predict that vaccine impact estimates would increase."
- **A data-quality problem turned into a result.** The discrepancy between the two fits is located, not merely reported:
  > "The discrepancy between vaccine impact estimates based on excess mortality and COVID-19 deaths was concentrated in settings with lower death registration and certification. This substantial discrepancy underpins the crucial need for continued investment in civil registration and vital statistics to prevent biases in mort[ality estimates]."

  **The difference between two analyses becomes evidence about surveillance systems**, and the recommendation that follows is about data infrastructure rather than about vaccines.
- **The lower bound is kept in play** so the conclusion does not depend on the contested measure: "even when relying on model fits based on reported COVID-19 deaths, we estimated that more than 14 million deaths were averted."

## Distinctive moves to borrow
1. **Define the window by the intervention's own start date** — one year from the first dose outside a trial.
2. **Characterise every prior study by its scope limit, by name**, so "global" is a checkable contribution.
3. **Name the methodological gap** (direct effects only) and define the missing mechanism parenthetically.
4. **Say why the counterfactual cannot be observed**, in one sentence, as the justification for modelling.
5. **Fit to two outcome measures and report both**, turning a data-quality worry into a reported range.
6. **Take your policy counterfactuals from commitments that were actually made**, with their owners and thresholds.
7. **Give percentages with numerator and denominator in parentheses**, so the counterfactual total is visible.
8. **Disaggregate by the political unit the decision concerns** — here COVAX eligibility and income group.
9. **Report a figure above 100% without softening it**, if the units make it coherent.
10. **Name the counterfactual assumption as the dominant source of variation**, and say which settings it flatters and which it penalises.
11. **Locate the discrepancy between two analyses** and let it become a finding about data systems.
12. **Keep the conservative estimate in play** so the headline does not rest on the contested measure alone.

## Related files
For vaccine impact carried through to an incremental cost-effectiveness ratio see [38-chen-2019-pneumococcal-cost-effectiveness](38-chen-2019-pneumococcal-cost-effectiveness.md); for how input revisions move impact estimates see [61-abbas-2020-hpv-input-revisions](61-abbas-2020-hpv-input-revisions.md); for campaign-timing policy from a transmission model see [49-verguet-2015-measles-sia](49-verguet-2015-measles-sia.md); for the counterfactual-against-what-happened structure see [01-grais-2008-measles-orv-niamey](01-grais-2008-measles-orv-niamey.md) and [20-nouvellet-2015-rapid-diagnostics-ebola](20-nouvellet-2015-rapid-diagnostics-ebola.md); for the Lancet scenario-projection conventions see [25-davies-2020-npi-uk](25-davies-2020-npi-uk.md).
