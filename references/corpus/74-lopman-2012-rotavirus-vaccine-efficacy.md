# 74 — Lopman et al. (2012), *PLoS ONE*
**"Understanding reduced rotavirus vaccine efficacy in low socio-economic settings"**
Lopman BA, Pitzer VE, Sarkar R, Gladstone B, Patel M, Glasser J, et al. *PLoS One* 7(8):e41720. doi:10.1371/journal.pone.0041720.

**Archetype:** *competing hypotheses* about an observed gradient — vaccine efficacy above 90% in rich settings, around 50% in poor ones — adjudicated by a transmission model that is fitted to incidence, not to efficacy, and then asked to reproduce the trials. The candidate explanations are decomposed step by step, so the paper ends with a share of the gap attributed to each.

## Structure
PLoS ONE: a structured abstract with the unusual headings **Introduction / Methods / Results / Discussion** → `Introduction` → `Methods` (*Model* · *Scenarios* · *Efficacy*) → `Results` → `Discussion` → supporting information carrying the equations and the model diagram.

**The Methods are organised around the three settings being compared**, with each input (protection from natural infection, vaccine immunogenicity, incidence) taken from data specific to a high-, middle- or low-income setting. The comparison is the design.

## Opening move
> "These vaccines have great potential to prevent the severe morbidity and mortality from rotavirus, but studies consistently demonstrate a gradient of reduced efficacy in low socio-economic settings (SES) where the burden of severe rotavirus disease, particularly mortality, is greatest."

The puzzle is stated with the numbers that make it a puzzle — efficacy "exceeding 90%" in high-income trials, "72 to 83%" in middle-income settings, "39 to 49%" in low-income Asia and Africa — and then widened beyond one vaccine: the same pattern holds "With all existing live oral vaccines against enteric infections (including typhoid, cholera and oral polio)".

**The hypotheses are sorted into categories before any is tested**:
> "While the exact reasons for this phenomenon are unclear, a range of hypotheses has been proposed. These can be broadly categorized as (1) factors leading to a poor immune response to natural infection, (2) reduced immunogenicity of the vaccines, and (3) very high incidence rate of infection that overwhelms immunity from vaccination."

**Group the candidate explanations into a few categories a model can represent**, each mapped to an input that can be varied. Specific mechanisms (enteropathy, helminths, maternal antibody) are then listed under the categories they would act through.

## Methods
- **Take each setting's inputs from that setting's data**: natural-history estimates from a Mexican cohort represent high and middle SES and a South Indian cohort represents low SES, because "No studies of this type have been performed in higher income settings".
- **State the mechanistic assumption that links vaccine to model**: "Rotavirus immunization is by live oral vaccination, and mechanistically is believed to mimic immunity from natural infection. We assumed that each dose of vaccine acts like a single infection, without causing symptomatic disease." The whole result depends on this, and it is stated as an assumption in one sentence.
- **Fit to incidence, then predict efficacy.** The models are fitted to age-specific incidence by adjusting one infectivity parameter; efficacy is never a calibration target. That is what makes the later comparison with trials a test.
- **Simulate the trial, not the programme**: to isolate the direct effect, the force of infection is fixed at its pre-vaccination equilibrium, so vaccination cannot change transmission — "This approach is used to compare incidence in vaccinated and unvaccinated groups without allowing vaccination to affect the transmission dynamics, representing a trial scenario." **When comparing a model with trial estimates, compute the quantity the trial measures.**
- **Decompose the gap stepwise**: starting from the low-SES model, seroconversion is raised to middle and then high values, then the natural-history parameters are switched, then the force of infection. Each step's change in efficacy is that factor's contribution.
- **Report the outcome in the age band trials used**: "Efficacy in the 6 to 23 month age group is presented as the main outcome measure to facilitate comparison with the age group that was primarily followed for clinical outcomes in vaccine trials."

## Results
**The headline reproduces the gradient without having been fitted to it**: the model generated efficacy against severe disease "of 93%, 86% and 51% in high, middle and low SES, respectively."

**The decomposition assigns the gap**:
> "Starting from a baseline of 51% efficacy among 6 to 23 month-olds in low SES, efficacy was projected to improve to 58% and 65%, respectively, if immunogenicity of vaccination was increased to levels from middle and high income countries. The rest of the gap in efficacy (to 93% in high income settings) was a result of differences in the protection conferred by natural infection. Underlying incidence had no long-term impact on vaccine efficacy."

**One of the three hypotheses is ruled out in a single sentence** — high incidence "had no long-term impact" — and the other two are given shares. This is the competing-hypotheses shape in miniature: the best-supported explanation, the runner-up, and the one that fails.

**Report absolute benefit alongside relative efficacy, where they disagree**: from 6 to 23 months, "71 cases of severe RV-GE per year were estimated to be prevented for every 1000 vaccinated children in low SES, while 63 cases per 1000 vaccinated were prevented in high SES" — lower efficacy, more cases prevented, because the disease is commoner. The pattern reverses at older ages, and the paper says why.

## Literature
Numbered PLoS citations. Trial and observational efficacy estimates are cited setting by setting in the Discussion, so the reader can check each prediction against the study it should match.

## Voice
First-person plural, past tense. The causal language is careful: the model "can be explained by", factors "compromise efficacy", and the agreement with trials is "reassuring regarding the validity of our assumptions" rather than proof of them.

## Discussion and limitations
**Validation is presented as a numbered set of predictions, each matched to observations**: "First and foremost, the model predicts higher VE with increasing SES"; second, the gap between efficacy against severe and against all disease; third, the apparent waning in low-income settings. Each is compared with the trials, and the misfit is reported: "The model does not fully capture how quickly VE falls; in clinical trials, VE declined by the second year of life and in the model, it fell in the third."

**An observed pattern is reinterpreted by mechanism**:
> "However, waning – traditionally defined as loss of immunity over time – is not an influential feature of the model (as waning occurs on a scale of >40 years). Even without loss of immunity, VE as measured by clinical trials or cohort studies, can, in some circumstances, fall with increasing age."

The model explains why efficacy appears to wane: severe disease continues into third and fourth infections in low-income settings, which two doses do not mimic. **When a fitted model reproduces a pattern by a different mechanism from the one usually assumed, say so explicitly** — the policy implication (an additional dose, not a booster against waning) follows from the mechanism.

**Limitations name the assumption most likely to matter and how it could fail**: "We have assumed that the immune response to natural infection and vaccination, immunogenicity of vaccines, and background rotavirus incidence are independent factors, and this may be an important limitation", with the specific route — concomitant gut infections that would raise incidence and depress immunogenicity together. Age versus number of prior infections is flagged as confounded, with its consequence: "If, for instance, under 1 year-olds are more susceptible to severe disease regardless of the number of previous infections, just delaying age at infection will reduce severe disease."

**A borrowed parameter is flagged as unrepresentative, with the mitigation**: mixing was taken from Great Britain, "These data are unlikely to represent mixing patterns in either Mexico or India. We account for this, at least in part, by allowing the parameter q to vary."

## Distinctive moves to borrow
1. **State the puzzle with the numbers that make it one**, and show it extends beyond the case at hand.
2. **Group hypotheses into categories a model can represent**, each tied to a variable input.
3. **Fit to one data type and predict another**, so the agreement is a test, not a fit.
4. **Simulate the trial's estimand** — fix the force of infection to isolate the direct effect.
5. **Decompose a gap stepwise** and give each factor its share.
6. **Rule a hypothesis out in one sentence** when the decomposition does.
7. **Report absolute benefit where it disagrees with relative efficacy.**
8. **List the model's predictions and match each to an observation**, including the one it gets wrong.
9. **Reinterpret an observed pattern by mechanism** when the model reproduces it another way, and draw the policy implication from the mechanism.
10. **Name the independence assumption that matters most** and the route by which it could fail.

## Related files
For the duration of immunity to another enteric virus, estimated with an age-structured model fitted to incidence by a group including the same lead author, see [80-simmons-2013-norovirus-immunity](80-simmons-2013-norovirus-immunity.md); for vaccine impact estimated by re-simulating without the vaccine see [60-watson-2022-covid-vaccination-impact](60-watson-2022-covid-vaccination-impact.md). Other *competing hypotheses* exemplars: see [57-yakob-2015-cdifficile-displacement](57-yakob-2015-cdifficile-displacement.md) for three mechanisms, one parameter each, ranked by whether they can reproduce the data; [24-davies-2021-b117-transmissibility](24-davies-2021-b117-transmissibility.md) for several mechanisms for one observation, each formalised, fitted and compared, with the winner chosen on an explicit criterion; [56-lavine-2021-endemicity](56-lavine-2021-endemicity.md) for rival explanations framed as immunity components that wane at different rates.
