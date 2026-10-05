# 72 — Camacho et al. (2015), *PLoS Currents: Outbreaks*
**"Temporal changes in Ebola transmission in Sierra Leone and implications for control requirements: a real-time modelling study"**
Camacho A, Kucharski A, Aki-Sawyerr Y, White MA, Flasche S, Baguelin M, et al. *PLoS Curr* 7. doi:10.1371/currents.outbreaks.406ae55e83ec0b5193e30856b9235ed2.

**Archetype:** the *rapid-response capacity assessment* — a transmission model fitted district by district during an epidemic, used to estimate how transmission has changed and to convert a short forecast into the beds needed, set against the beds that exist. Published within weeks of its data, and checked in the paper against two weeks of data that arrived during review. Where Finger 2019 is an account written after the response, this is the response.

## Structure
*PLoS Currents: Outbreaks*: structured abstract (**Background / Methods / Results / Conclusions**) → `Introduction` → `Methods` → `Results` → discussion → a long `Appendix` (*Data* · *Model and parameters* · *Model fitting and inference* · *Forecasting and bed requirements* · sensitivity analysis).

**The main text is short and operational; the model lives in the appendix.** Methods in the body take four paragraphs — data, model, fitting, forecast and beds — and the appendix carries the compartment flowchart, the observation model, the sampler and the parameter derivations. **For a paper whose readers are responders, keep the body to what they need to judge the conclusion**, and put the machinery where modellers will look for it.

## Opening move
> "The devastating epidemic of Ebola virus disease (EVD) in West Africa has taken an enormous toll in terms of human suffering and economic loss. As of 18th January 2015, Sierra Leone is the worst affected country, with over 8000 confirmed and probable cases reported."

**The Introduction then defines the operational vocabulary the results will use** — treatment centres, holding centres and community care centres, each by what it does:
> "These units operate high levels of infection control and are used to isolate and provide clinical care to confirmed EVD patients. In addition, Ebola Holding Centres (EHCs) have been constructed as a first destination to assess the status of persons suspected of having EVD and isolate them until confirmatory blood testing, and a number of Community Care Centres (CCCs) - smaller, more lightly staffed - have been opened to help increase bed capacity and bring care closer to communities."

The distinction between assessment beds and treatment beds is the paper's main output, so it is established before any number appears.

**The aim is two questions, the second conditional on the first**: estimate how R varied by district, and, "As a large number of additional ETC and EHC beds were introduced in Sierra Leone in December 2014, we also used the model to estimate how many cases would be present in the community by the end of March 2015, and evaluate whether beds currently in place will be sufficient to meet demand."

## Methods
- **Name each data source's weakness, and give the rule for switching between them.** The WHO patient database is cleaned but lags; the ministry's situation reports are timely but rougher:
  > "The time at which this switch was made was determined for each district by comparing the weekly totals from the WHO/patient database and the MoHS SitReps in the 6 weeks preceding publication date of WHO data (11th January 2015). The earliest week where the number of confirmed and probable cases in the MoHS SitReps exceeded that in the WHO/patient database determines this switch. This was between 1 and 4 weeks before."

  **When two data sources are stitched together, state the rule and the result of applying it.** The switch is a decision that changes every recent estimate, and a rule makes it reproducible.
- **Fix what cannot be estimated, and say where the value came from**: "As it was not possible to estimate the extent of under-reporting, we fixed the proportion of symptomatic cases reported at 60%, based on recent estimates from the UN for Ebola Emergency Response and the National Emergency Response Centre."
- **Let transmission vary without explaining why**, and say why that is enough: a single time-varying transmission rate absorbs "external influences on transmission - such as variation in human behaviour and introduction of control measures".
- **Map model states onto the resource, bed type by bed type.** Assessment beds hold everyone in their first three days after notification, scaled up for suspected cases who turn out not to have Ebola; treatment beds hold confirmed cases until removal. The appendix gives the arithmetic: "we assumed that the bed demand in EHCs/CCCs was equal to the number of EVD cases in their first three days post-notification divided by the empirical proportion of EVD cases at that time."
- **Hold back data that arrive during review and use them to test the forecast**:
  > "While this paper was under review, we collected data for two more weeks (weeks ending 25th January and 2nd February 2015). Here, instead of re-fitting to the latest data we decided to assess how well our forecasts matched these two additional data points."

  **Treat data that arrive after submission as an out-of-sample test, not as an update.** The figures mark them differently — "Fitted data are plotted as filled circles and the two additional, non-fitted, data as open triangles."

## Results
**The headline estimate is dated, local and set against the threshold**:
> "In Western Area, which has had the most cases, we found that the median R decreased from 2.8 (interquartile range credible interval, IQR: 2.1-3.8) to 0.32 (0.20-0.47) between August and January and dropped below the critical epidemic control threshold of R = 1 in early December."

The interval is a 50% credible interval and is labelled as one each time — necessary, since readers will assume 95%.

**Sort the districts into regimes rather than reporting nine sets of numbers**: districts in decline (Western Area, Bo, Bombali, Port Loko, Tonkolili), one stalled at the threshold (Kambia), and three where R "has been oscillating around the control threshold since October" (Kono, Moyamba, Koinadugu), for which "resurgence of cases cannot be ruled out".

**Report where the forecast missed, in the Results**:
> "Comparing with the two additional weeks of data, we noted that the number of cases remained stable on the week ending 25th January 2015, but dropped below the lower bound of the interquartile range interval (IQR) of our forecast on the following week."

**The bed result is given as a turning point with its exceptions**: "Our results suggest that bed capacity has remained below what was needed since the outset of the Ebola outbreak in most areas, but that this is now changing… However, three districts still suffer from a lack of treatment beds (Kambia, Koinadugu, Kono)". Table 2 puts beds available beside beds needed now and at the end of March, district by district — Kambia, for instance, with no treatment beds against a need of 10 (interquartile range 9–12).

## Literature
Numbered citations, few and functional: the empirical incubation and infectious periods, the reporting-delay estimates, the inference library, and the group's own companion analyses. The data sources — WHO situation reports, ministry situation reports, the bed register — are cited as primary sources, and the bed register is deposited with a DOI.

## Voice
First-person plural, past tense for the analysis, conditional for the forecast ("could continue to decline", "cannot be ruled out", "could be envisaged"). The prose is plain and the modals are graded to the regimes: confident where R is well below one, guarded where it straddles it.

## Discussion and limitations
**The recommendation is specific and already adjusted for feasibility**:
> "Although opening new ETCs in those areas may not be possible in the coming weeks, rapid opening of new EHCs/CCCs and transfer of confirmed cases to ETUs in neighbouring districts could be envisaged."

**Advise within the constraint the reader faces.** Treatment centres take weeks to open; the paper recommends what can be done in days.

**A tempting causal reading is declined, with the reason it cannot be tested**:
> "However, since we did not include an explicit mechanism by which bed capacity affected transmission in the model we could not measure the extent to which the decline in the reproduction number resulted from more treatment and holding centres versus other factors, such as changes in community behaviour and burial practice. Indeed, the expansion of bed capacity is likely to partly reflect a general increase in awareness and control efforts. However, such factors are far more difficult to measure than beds."

The last sentence names the trap: beds are the intervention that can be counted, so they will be credited with the decline. **When an intervention coincides with a fall in transmission, say what the model can and cannot attribute, and name the confounder that is harder to measure.**

**A simplification is defended by what the estimand needs**: multiple transmission routes cannot be separated from one incidence curve, "However, knowledge of such factors is not necessary to calculate the change in overall reproduction number over time, and hence understand the average trend in population transmission patterns in real-time."

**The direction of each known bias is given, separately for each output**:
> "We assumed that the time from onset to hospitalisation and the proportion of reported cases remained constant over time. However, a two-week operation to uncover hidden EVD cases in Western Area occurred at the end of December 2014 and could have lead to a reduction in the time to hospitalisation and to an increase in the proportion of reported cases. We anticipate that this would reduce our estimate of the reproduction number but increase bed requirements, because cases would stay longer in isolation."

One violated assumption moves the two outputs in opposite directions, and the sentence says so. The appendix does the same for the case fatality ratio, and quantifies it: a lower CFR "would not affect our conclusions regarding the temporal changes in the reproduction number, it would affect our estimates of the number of beds required", by 22% — and then notes that the bed estimates "can already be seen as conservative" because all cases, including unreported ones, were assumed to present.

**The forecast's assumption is checked against the held-out weeks, district by district**: "Our forecast approach assumes that the situation remains unchanged from what is inferred from the last data-point. Comparing our forecasts with two additional weeks of data, we found that this assumption held for the districts showing a steady decline in the number of cases".

## Data, code and funding
The bed register is deposited on figshare with a DOI; the situation reports and WHO data are public and their URLs given; the inference library is open source with its repository named. Weekly updated fits and forecasts are published online. The author list includes members of a field medical team, the joint inter-agency task force in Freetown and Epicentre alongside the modellers, and the work was funded by a humanitarian-research programme whose funders "had no role in study design".

## Distinctive moves to borrow
1. **Keep the body operational and put the model in the appendix** when the readers are responders.
2. **Define the operational vocabulary** — here, the bed types — before the results depend on it.
3. **State the rule for switching between data sources and what applying it gave.**
4. **Fix what cannot be estimated, and cite where the value came from.**
5. **Map model states onto the resource, one resource type at a time**, including the people who occupy beds but turn out not to be cases.
6. **Use data that arrive during review as an out-of-sample test**, and plot them differently from fitted data.
7. **Label a 50% interval as such every time.**
8. **Sort units into regimes** instead of listing every estimate.
9. **Report the forecast's miss in the Results.**
10. **Give the recommendation within the reader's constraint** — what can be opened in days, not weeks.
11. **Decline the causal credit an intervention will get**, and name the harder-to-measure confounder.
12. **Give the direction of each bias separately for each output**, especially when they move in opposite directions.
13. **Say when an estimate is already conservative**, and why.

## Related files
For the rapid-response analysis written up after the response, with forecasts dated against decisions, see [44-finger-2019-diphtheria-rapid-response](44-finger-2019-diphtheria-rapid-response.md); for the retrospective scoring of this group's real-time Ebola forecasts in the same country see [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md); for an operational forecast that drove resource decisions in an endemic setting see [73-shi-2016-dengue-forecast-singapore](73-shi-2016-dengue-forecast-singapore.md); for identifiability of Ebola transmission routes from one incidence curve see [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md); for real-time reproduction-number estimation see [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) and [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md). Other *real-time transmission analysis* exemplars: see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md) for an individual-based model fitted to a live national epidemic while control decisions were still being made; [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) for a widely used R_t estimator with two failing assumptions fixed, shipped in the package the field already uses; [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md) for a natural-experiment evaluation across Chinese cities, with a mechanistic counterfactual, written under emergency time pressure; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver; [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast whose corrected onsets feed a reproduction-number estimate, evaluated against later data.
