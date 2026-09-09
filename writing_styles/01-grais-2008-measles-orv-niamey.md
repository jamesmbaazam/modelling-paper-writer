# 01 — Grais et al. (2008), *J. R. Soc. Interface*
**"Time is of the essence: exploring a measles outbreak response vaccination in Niamey, Niger"**
Grais RF, Conlan AJK, Ferrari MJ, Djibo A, Le Menach A, Bjørnstad ON, Grenfell BT. *J R Soc Interface* 5(18):67–74. PMC2605500.

**Archetype:** the *policy counterfactual* paper — a stochastic simulation model fitted to one real outbreak, then re-run under alternative intervention scenarios.

## Structure
`Abstract` → `1. Introduction` (~8 ¶) → `2. Methods` → `2.1 Study setting` → `2.2 Data sources` → `2.2.1 Population, surveillance and vaccine coverage` → `2.3 Model structure` → `2.4 Model calibration` → `2.4.1 Scenario analysis` → `3. Results` → `3.1 Scenario analysis` → `4. Discussion` (~12 ¶) → Acknowledgements → ~60 references.

Numbered, deeply nested headings (2.2.1, 2.4.1). Discussion is the longest section — roughly as long as Methods and Results combined. The scenario-analysis subheading is *repeated* in both Methods and Results, so the reader can pair specification with outcome.

## Opening move
> "The current World Health Organization recommendations for response during measles epidemics focus on case management rather than outbreak response vaccination (ORV) campaigns, which may occur too late to impact morbidity and mortality and have a high cost per case prevented. Here, we explore the potential impact of an ORV campaign conducted during the 2003–2004 measles epidemic in Niamey, Niger."

Pattern: **contested policy guidance → the specific epidemic that tests it → "Here, we…" + the counterfactual question.** The abstract's second sentence is always the "Here, we…" pivot.

The Introduction ends by posing an explicit numbered set of questions ("Three key questions arose…": what did the campaign achieve, what would earlier timing have achieved, what does the target age range change). Results and Discussion then answer them in order.

## Methodology conventions
- Displayed, section-numbered equations: `(2.1)`, `(2.2)`. Every symbol is glossed immediately in prose — "where *β*_quartier is the transmission rate between children within the same quartier".
- **Assumptions are flat declarative sentences**, never buried: "Once infected, the infectious process is assumed to be deterministic; children are infected but not infectious (latent) for 10 days and infectious for 6 days."
- Parameters are sourced, not invented: "Previous research on the data for this epidemic provided the estimates of the overall transmission rate within the city."
- Scenario grids are enumerated exhaustively in Methods before any result is shown: coverage 30–100% in 10% steps × delay 60/90/120 days × campaign duration 6/10/14 days.
- **Operational realism is written into the model**: a 15-day delay between the decision to intervene and implementation; scenarios chosen because they "were considered operationally feasible".
- Sensitivity is handled by the scenario grid itself rather than a separate sensitivity table.

## Results storytelling
Medians with interquartile ranges in **square brackets**; percentages carried alongside raw counts.
> "We estimate that a median of 7.6% [4.9–8.9] of cases were potentially averted as a result of the outbreak response, which vaccinated approximately 57% (84 563 of an estimated 148 600) of children in the target age range (6–59 months), 23 weeks after the epidemic started."
> "A target proportion of 50% of children (except ill children) resulted in up to 38, 27 and 20% of cases averted for campaigns at 60, 90 and 120 days from the start of the epidemic, respectively."
> "For a campaign with an objective of vaccinating 50% of non-infectious children aged 6 months to 15 years, up to 93% of cases were potentially averted at day 60, 81% at day 90 and 52% at day 120."

Note the recurring shape: **one sentence carries a whole 3-point gradient** ("38, 27 and 20% … at 60, 90 and 120 days, respectively"). Figures overlay observed histograms with simulated trajectories, so model validation is visual and immediate.

## Literature integration
Moderate density (2–3 citations per introductory paragraph), heaviest where parameters are justified. Prior work is positioned as *unresolved disagreement that this paper adjudicates*:
> "Some previous studies suggest that reactive vaccination will not stop epidemics because measles transmission is so rapid; other analyses, however, point to the potential benefits of vaccination interventions in high-burden settings."
Followed by the gap: "little research has focused on control of measles outbreaks in high-burden settings once epidemics have taken off."

## Voice
"We" throughout ("We developed", "We measured", "We estimate"). Present tense for biological facts, past for what was done, present for what the model implies. Hedges are specific rather than generic: "only suggestive of potential trends", "we would expect", "our results are also in agreement with".

## Limitations
Framed as the honest cost of abstraction, not as failure:
> "Our goal was to identify the key factors driving the number of potentially averted cases, and, as with all models, ours simplifies reality in a number of respects."
> "Although model simulations were in agreement with the observed epidemic dynamics, we did not consider the details of the spatial dynamics."
Each limitation closes by naming the analysis that would resolve it.

## Distinctive moves to borrow
1. **Title as thesis.** "Time is of the essence" states the finding before the abstract does.
2. **Nested spatial vocabulary** (quartier → CSI catchment → commune → city) reused consistently in data, model and results so the reader never re-learns the scale.
3. **Equations immediately re-expressed epidemiologically** — never leave a β unexplained in biological terms.
4. **Closing on the decision, not the model**: "Ultimately the decision whether or not to intervene … depend[s] upon the political will of public health authorities."
