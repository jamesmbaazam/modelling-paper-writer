# 49 — Verguet et al. (2015), *Vaccine*
**"Controlling measles using supplemental immunization activities: a mathematical model to inform optimal policy"**
Verguet S, Johri M, Morris SK, Gauvreau CL, Jha P, Jit M. *Vaccine* 33(10):1291–1296. doi:10.1016/j.vaccine.2014.11.050.

**Archetype:** *policy-timing optimisation* — use a transmission model not to project a scenario but to compute the value of a schedule parameter, and deliver it as a per-country table a programme manager can read off. The deliverable is an operational rule, not an estimate.

## Structure
Elsevier structured abstract (**Background / Methods / Results / Conclusions**) → `Keywords` → `1. Introduction` → `2. Methods` (*2.1 Modeling*, vaccine action, parameterisation, the analytical approximation) → `3. Results` → `4. Discussion` → limitations → conclusion.

**A short paper, six pages, with a single table carrying the deliverable.** Table 1 lists, per country, the routine first-dose coverage, the crude birth rate, and the required inter-campaign interval from both the computational and the analytical model. **When the output of a model is an operational parameter, the table *is* the paper** — everything else explains how the column was computed and when to distrust it.

## Opening move
The Introduction opens on the global target, then the shortfall, then narrows to the specific programme:
> "The fourth United Nations Millennium Development Goal aims to reduce under-five mortality rates by two thirds between 1990 and 2015. Despite accelerated progress, with a decline from about 12 million deaths in 1990 to about 7–8 million deaths in 2010, the goal is unlikely to be attained at current rates of decline. Measles has been a key contributor to this mortality."

Then the programme is described in operational detail, because the paper's recommendation will be expressed in its terms: routine first dose "at about 9 or 12 months of age", a recommended second dose, and in high-burden countries "often, only one dose is routinely given, but an opportunity for a second dose of measles vaccine is offered through supplemental immunization activities (SIAs)… During SIAs, children and adolescents are targeted regardless of their previous history of measles vaccination."

**Describe the intervention as it is actually delivered before modelling it.** The modelled quantity — time between campaigns — only means something once the reader knows what a campaign is and who it reaches.

The aim is then stated as a computation, not an exploration: "Specifically, we compute the maximum allowable time period between two consecutive SIAs to achieve measles control."

## Methods
- **Name the model, expand the acronym, and state its structure in two sentences**: "We developed DynaMICE (Dynamic Measles Immunization Calculation Engine), an age-stratified model of measles infection transmission in vaccinated and unvaccinated individuals. The population in the model can be susceptible to measles, infected with measles or recovered from measles (and hence have lifelong immunity)."
- **Describe the force of infection in words**: "The rate at which infection occurs in the susceptible population depends on the existing proportion of the population that is already infected, as well as the effective contact rate between different age groups."
- **State the ageing scheme explicitly**, because it drives everything in a childhood-vaccination model: "Individuals age discretely, in one-year increments, at the end of each year, between 0 and 100 years old."
- **Give vaccine effectiveness by dose and age, with the source, and the functional form it takes**:
  > "Vaccine effectiveness is assumed to be 85% for the first dose when vaccinating before one year of age, 95% after one year of age and 98% for two doses, as suggested by a recent meta-analysis. Vaccines are assumed to be 'all or nothing', so that individuals receiving the vaccine are either fully protected or not at all."

  **"All or nothing" versus "leaky" is a modelling choice with real consequences for predicted impact**, and it is named using the field's own term rather than buried in an equation.
- **List the assumptions that bound what the vaccine can do**: "We assume that vaccination gives lifetime protection if it successfully elicits an immune response, and that vaccinating already infected individuals does not increase the rate of infection clearance (i.e. the vaccine has no therapeutic action)."
- **Gloss every symbol in the figure caption**, so the schematic stands alone: "S = susceptible, I = infected, R = recovered, VS = vaccinated susceptible, VI = vaccinated infected, VR = vaccinated recovered, λ = force of infection, γ = infectiousness period of measles, κ = coverage…, τ = effectiveness…".
- **Develop an analytical approximation alongside the simulation**, and report both in the same table. The analytic column lets a reader reproduce the recommendation without the code, and agreement between the two is itself a check (`SKILL.md` §2, evidence in `evidence.md` §2.1: *give the analytic bound alongside the simulation where one exists*).

## Results
**Define "control" operationally in terms of what the simulation shows**, so the threshold is not a judgement call:
> "we see that there is resurgence of measles (occurrence of incidence peaks after year 50) when the inter-SIA period is over three years. Furthermore, the less frequent the SIA, the larger the resurgence. Conversely, an average inter-SIA period of three years or less suffices to control measles (no occurrence of incidence peaks after year 50)."

**Report the driver of the recommendation as a correlation across countries, then instantiate it**:
> "We see that the maximum time period required between two consecutive SIAs depends importantly on MCV1 coverage (Pearson correlation coefficient of 0.71). For example, countries like Ethiopia and Nigeria with lower coverage of MCV1 (66% and 42%, respectively) would require SIAs about every 2 years."

The general relationship and two named countries with their actual coverage figures — a programme manager in Nigeria can find themselves in the sentence.

**The headline is a negative result about the intervention as commonly deployed**, stated plainly in the abstract and again in the Discussion: "Our analysis indicates that a single SIA will not control measles transmission in any of the countries with high measles burden. However, regular SIAs at high coverage levels are a viable strategy to prevent measles outbreaks."

**Name the mechanism by which a programme could fool itself** — the most valuable sentence in the paper:
> "The model also suggests that a single SIA may give the impression of having controlled measles due to a post-vaccination 'honeymoon'. Such potentially unexpected effects can have disastrous consequences on plans for national elimination or even global eradication goals. This underscores the importance of using predictive models that account for transmission events, rather than relying solely on surveillance based on reported cases, to inform decision making about vaccination."

A model earns its place when it explains why the observable data will mislead. **If your model shows that surveillance alone would give the wrong answer, say so explicitly — that is the argument for modelling.**

## Literature
Numbered Elsevier citations, sparse. Prior models are credited and the increment stated precisely: "Several models of measles transmission have been previously developed in order to explore the potential impact of different vaccination strategies, including the impact of mass immunization campaigns. Here, we build on these models to explore the impact and optimal timing of periodic measles immunization campaigns, which have been the main focus of measles control efforts in the highest burden countries." **Not a new model class — a new question put to an established one**, and the justification is that the question is the one the programmes actually face.

## Voice
First-person plural, present tense for model behaviour, conditional for recommendations: "would require SIAs about every 2 years", "may be most effective", "can guide country policymakers". The conclusions are addressed to a named audience — country policymakers and WHO guideline-setters — rather than to the literature.

## Discussion and limitations
Opens by restating the two-part finding (single campaigns fail, regular campaigns work, with periodicity set by demographics and routine coverage), then the honeymoon mechanism, then the positioning, then the policy implication:
> "This suggests that a country-specific approach to SIA timing may be most effective, with the recommended length of time between SIAs dependent on local demographics and routine coverage. Our computer model and the associated simplified analytical formula offer a way for country policymakers to determine when measles SIAs should be implemented."

The limitations are four, each with a reason, and three with the mitigation attempted:
- **A parameter held constant across settings, with the reason it could not be localised and the sensitivity analysis run instead**: "we used an average estimate of the basic reproduction number of measles, and hence did not capture local variations in the intensity of measles transmission… However, estimating this number separately for each setting is hindered by the lack of reliable data for measles case notifications due to underreporting and great disparity in reporting quality. As sensitivity analysis, we reported on the inter-SIA period required for the selected high burden countries with a lower reproduction number R₀ of 12."
- **An unmodelled correlation, with the real-world mechanism that creates it**: "the model does not take into account potential correlation between MCV1 and SIA coverage, and the fact that often children with better access to health systems and hence more likely to have received MCV1 can be easier to reach through SIA." This would make campaigns less effective than modelled — the direction is implicit and would have been better stated.
- **A refusal to forecast inputs that cannot be forecast**: "Neither does it account for changes in immunization and birth rates into the future, as these are largely uncertain to forecast."
- **A scope fence distinguishing two goals that are routinely conflated**, with the mechanisms the model lacks for the second, and a generous note about the field:
  > "though the model captures the conditions necessary for measles control, it is not intended to realistically model measles elimination (i.e. zero indigenous transmission events). Elimination goals depend on monitoring measles importations, vaccine coverage in hard-to-reach groups and stochastic one-off events, none of which are captured by the model (and rarely so by most models published in the literature). One could however examine the potential of an imported case to invade the population."

Closes by stating which conclusions survive the limitations rather than claiming they all do: "Despite these limitations, the broad conclusions of the model appear robust, particularly the need for regular SIAs to control measles in low routine coverage se[ttings]."

**Naming the specific conclusion that is robust, rather than asserting robustness generally, is the right way to end a limitations section.**

## Distinctive moves to borrow
1. **Make the deliverable a table of an operational parameter by country**, with the inputs that determine it in adjacent columns.
2. **Describe the intervention as delivered** — who is targeted, at what age, regardless of history — before modelling it.
3. **State the aim as a computation** ("we compute the maximum allowable time period"), not as an exploration.
4. **Name the vaccine-action assumption in the field's own vocabulary** ("all or nothing" versus leaky) and give effectiveness by dose and age with its source.
5. **Define control operationally** by what the simulation shows, with the horizon stated.
6. **Report the driver as a correlation across settings, then instantiate it** with two named countries and their real coverage.
7. **Give the analytical approximation alongside the simulation, in the same table**, so the recommendation is reproducible without the code.
8. **Say when surveillance alone would mislead** — the honeymoon effect — because that is the argument for using a model at all.
9. **Position as a new question put to established models**, not a new model.
10. **Separate control from elimination explicitly**, list the mechanisms your model lacks for the second, and say what could be done instead.
11. **Close by naming which conclusion is robust**, not by asserting robustness.

## Related files
For outbreak-response vaccination rather than scheduled campaigns see [01-grais-2008-measles-orv-niamey](01-grais-2008-measles-orv-niamey.md); for the measles dynamics that make campaign timing matter see [02-ferrari-2008-measles-sub-saharan-africa](02-ferrari-2008-measles-sub-saharan-africa.md), [18-bjornstad-2002-tsir-measles](18-bjornstad-2002-tsir-measles.md) and [04-earn-2000-simple-model-complex-transitions](04-earn-2000-simple-model-complex-transitions.md); for vaccine impact carried through to an economic evaluation see [38-chen-2019-pneumococcal-cost-effectiveness](38-chen-2019-pneumococcal-cost-effectiveness.md); for converting model output into a numbered operational checklist see [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md). Other *policy counterfactual* exemplars: see [20-nouvellet-2015-rapid-diagnostics-ebola](20-nouvellet-2015-rapid-diagnostics-ebola.md) for three strategies compared on several metrics at two scales, with an answer that depends on context.
