# 44 — Finger et al. (2019), *BMC Medicine*
**"Real-time analysis of the diphtheria outbreak in forcibly displaced Myanmar nationals in Bangladesh"**
Finger F, Funk S, White K, Siddiqui MR, Edmunds WJ, Kucharski AJ. *BMC Med* 17:58. doi:10.1186/s12916-019-1288-7.

**Archetype:** the *rapid-response outbreak analysis* — a model built and run under operational time pressure, with forecasts delivered to responders on dated occasions, written up afterwards as both an epidemiological analysis and an honest account of what the modelling was and was not able to do. The deliverable is a decision, not an estimate.

## Structure
BMC structured abstract (**Background / Methods / Results / Conclusions**) → `Background` → `Methods` (*Data*, delay adjustment, transmission model, fitting) → `Results` (the four forecasts in date order, then the operational impact) → `Discussion` → `Conclusions` → declarations.

**The distinguishing structural feature is the timeline figure.** Figure 1 plots the epidemic curve with the dates of the first case, the modellers' involvement, each of the four forecasts, and the decisions they fed — "Green lines show the timing of events relevant to analysis: reporting of the first case, involvement of modellers at LSHTM, MSF decision on bed numbers required and MSF handover of the treatment centre. Blue lines show the date on which each of the four LSHTM forecasts was communicated to MSF".

**For any real-time analysis, draw the timeline of what you knew when and what you said when.** It converts an unfalsifiable claim of usefulness into an auditable record, and it is the single most important figure in the paper.

## Opening move
The abstract establishes the setting, the scale and the collaboration before any method:
> "Between August and December 2017, more than 625,000 Rohingya from Myanmar fled into Bangladesh, settling in informal makeshift camps in Cox's Bazar district and joining 212,000 Rohingya already present. In early November, a diphtheria outbreak hit the camps, with 440 reported cases during the first month. A rise in cases during early December led to a collaboration between teams from Médecins sans Frontières—who were running a provisional diphtheria treatment centre—and the London School of Hygiene and Tropical Medicine with the goal to use transmission dynamic models to forecast the potential scale of the outbreak and the resulting resource needs."

**Name the operational partner, what they were doing, and what the modelling was for.** The purpose is "the potential scale of the outbreak and the resulting resource needs" — not understanding, not inference.

**The conditions of the work are stated as a general problem for the archetype**, which is what lifts the paper above a case report:
> "Such analysis can face multiple challenges in real time, including delays and variability in available data streams, limited pre-existing epidemiology studies and knowledge gaps about risk factors and immunity in the host population. Besides describing the modelling methodology and forecasts, we report on the practical implications of the analysis, examining the role real-time modelling of infectious disease dynamics can play in operations and decision-making in a complex humanitarian crisis."

**Two deliverables declared up front** — the forecasts, and an account of the role modelling played.

## Methods
- **Describe the data stream as it actually arrived, with its cadence and its anonymisation**: "From 9 December 2017 to 12 January 2018, we received daily anonymized line lists of suspected cases."
- **Give the counts by location with attack rates attached**: "a total of 2624 cases (495 from Kutupalong (attack rate 0.12%), 1868 from Balukhali (attack rate 0.97%) and 261 from other or unknown nearby locations) presented at the Diphtheria Treatment Centre in Balukhali run by MSF." The two camps differ by a factor of eight in attack rate, which is why everything downstream is stratified by location.
- **State the denominator and its provenance, with its uncertainty acknowledged by citation**: "The total refugee population had been estimated at around 608,000 in early December."
- **Adjust for reporting delay before fitting, using the data's own delay distribution**: "We first adjusted for delays between symptom onset and case presentation using the observed distribution of reporting delays from previously reported cases. We then fit a compartmental transmission model to the adjusted incidence stratified by age group and location."
- **Date every forecast and say to whom it went**: "Model forecasts with a lead time of 2 weeks were issued on 12, 20, 26 and 30 December and communicated to decision-makers." A real-time paper that does not date its outputs cannot be evaluated.

## Results
**Report each forecast against what actually happened, including the one that was wrong, in the abstract:**
> "The first forecast estimated that the outbreak would peak on 19 December in Balukhali camp with 303 (95% posterior predictive interval 122–599) cases and would continue to grow in Kutupalong camp, requiring a bed capacity of 316 (95% posterior predictive interval (PPI) 197–499). On 19 December, a total of 54 cases were reported, lower than forecasted. Subsequent forecasts were more accurate: on 20 December, we predicted a total of 912 cases (95% PPI 367–2183) and 136 (95% PPI 55–327) hospitalizations until the end of the year, with 616 cases actually reported during this period."

This is the model to copy for any real-time paper. The first forecast was badly wrong — 303 predicted against 54 observed — and it is reported in the abstract, with its interval, immediately followed by the improvement. **Reporting your own forecast failure in the abstract is the strongest possible evidence of good faith, and it costs nothing because the later forecasts were good.**

**Report the operationally relevant quantity, not just cases.** Bed capacity and hospitalisations are forecast alongside incidence, because those were the decisions: "helped support decision-making on operational aspects of the outbreak response, such as hospital bed and staff needs, and with advocacy for control measures."

**Describe the organisational effect honestly, including second-order effects**: the analysis "helped lead to a closer collaboration between key partners such as MSF and WHO."

## Literature
Numbered BMC citations, concentrated in the Background. The literature is drawn from two distinct bodies — the humanitarian and political record of the crisis (an advisory commission report, an MSF retrospective mortality survey, UNICEF statistics) and prior real-time modelling (the RAPIDD Ebola forecasting challenge, real-time Ebola transmission analysis in Sierra Leone). **A humanitarian analysis cites grey literature and agency reports as primary sources**, with access dates, because that is where the setting is documented.

A striking parameter source: UK live births 1900–1930 is cited to inform assumptions about susceptibility in an unvaccinated population — **where no local data exist, a historical analogue is used and declared**.

## Voice
First-person plural, past tense, and unusually plain about constraints: "we were aware that", "it would have been difficult to confidently conclude", "With more time available, it would have been possible to…". Claims about impact are hedged to the authors' actual knowledge — modelling "helped support decision-making", "can play a role" — and the final verdict on the archetype is deliberately modest: "Although modelling is only one component of the evidence base for decision-making in outbreak situations, suitable analysis and forecasting techniques can be used to gain insights into an ongoing outbreak."

## Discussion and limitations
The limitations section is the best part of the paper and is organised as a causal chain explaining the one bad forecast:

- **The structural reason the early estimates were fragile**: "During the initial exponential growth phase of an epidemic, it is generally not possible to estimate the marginal posteriors for all key unknown transmission and reporting parameters without imposing priors on at least some of them. We therefore constrained prior susceptibility and the proportion of cases reported."
- **Exactly which parameters were fixed, in plain terms**: "we fixed the proportion of cases susceptible and natural history parameters—equivalent for Dirac delta priors—and imposed a strong prior on the proportion of cases reported."
- **Why that choice was made at the time, and which error it was guarding against**: "our choice to impose an informative prior on the reporting rate was driven by the uncertainty surrounding the recent incidence data points in real time. Owing to the initially very long reporting delays, we were aware that the newest raw data could give a false impression of a declining epidemic, creating the risk of substantially underestimating epidemic magnitude in our forecasts."
- **A retrospective re-analysis under the alternative assumption, with the result reported against the authors' own interest**:
  > "To retrospectively assess the sensitivity of our results to the prior assumptions, we recalibrated our model with flat priors on reporting, leading to lower estimates of the reporting rate… Although in retrospect the forecasts using flat priors capture the outbreak dynamics well and anticipate the epidemic peak, it would have been difficult to confidently conclude the epidemic had peaked in real time, given that such a conclusion would be heavily reliant on very recent data points, which were known to be less reliable."

  The alternative specification would have performed better, and the paper says so — then explains why it would not have been adoptable in real time. **This distinction between what was knowable then and what is knowable now is the central epistemic move of the archetype.**
- **And the honest caveat on the counterfactual**: "it would still have been possible to conclude which model performs best only a posteriori."
- **Omitted mechanisms, each with an argument about whether it mattered**: time-varying R and reporting rate were not modelled; the vaccination campaign "is, however, unlikely to have had an impact within the time frame analysed here given the delay to protection, incubation period following infection and the delay in reporting following onset."
- **A fixed-population assumption with its real-world violation named**: "we assumed a fixed population size. In reality, there can be a substantial influx of people into camps during outbreaks, as well as movement within and between camps."
- **A structural consequence of determinism**: "the deterministic model we used attributed any uncertainty to the fitted parameters and the reporting process, rather than stochasticity in transmission."

## Data, code and funding
Data and materials declared available with the article and its supplementary files; funders named with grant number and a non-influence statement ("Funders did not have any influence on the design of this study, the analysis or the interpretation and presentation of the results"); an abbreviations list; and contributions itemised in a way that makes the operational collaboration visible — the field liaisons "acted as liaison with field staff from MSF, provided data and in situ information, were involved in interpreting the results and **incorporated model results into the operational decision-making processes**."

**Ethics is handled by naming the exemption and the body that sets it**: "This research fulfilled the exemption criteria set by the MSF Ethics Review Board for a posteriori analyses of routinely collected clinical data and thus did not require MSF Ethics Review Board review."

## Distinctive moves to borrow
1. **Draw the timeline**: epidemic curve, dates of each forecast, and the decisions they fed. It makes the claim of usefulness auditable.
2. **Report your worst forecast in the abstract**, with its interval and the observed value, followed by the improvement.
3. **Forecast the operational quantity** — beds, staff, hospitalisations — not only cases.
4. **Date every output and name who received it.**
5. **Say which parameters you fixed and why, in the conditions you were working under**, not as a generic limitation.
6. **Re-run with the alternative priors afterwards and report the result even when it beats yours** — then explain why it was not adoptable in real time.
7. **Separate what was knowable then from what is knowable now**, explicitly.
8. **Argue about whether an omitted mechanism mattered** (the vaccination campaign's timing) rather than merely listing it.
9. **Declare the collaboration in the contributions**, including who carried the results into decisions.
10. **Cite grey literature and agency reports as primary sources** for a humanitarian setting, with access dates; use a declared historical analogue where no local parameter exists.
11. **Close on the modest, defensible claim**: modelling is one component of the evidence base.

## Related files
For real-time transmission analysis in a research rather than operational setting see [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) and [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md); for the delay adjustment this paper applies see [43-mcgough-2020-nobbs-nowcasting](43-mcgough-2020-nobbs-nowcasting.md) and [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md); for identifiability during exponential growth see [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md); for outbreak-response vaccination in a comparable setting see [01-grais-2008-measles-orv-niamey](01-grais-2008-measles-orv-niamey.md).
