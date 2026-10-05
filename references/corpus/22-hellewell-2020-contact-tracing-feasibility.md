# 22 — Hellewell et al. (2020), *The Lancet Global Health*
**"Feasibility of controlling COVID-19 outbreaks by isolation of cases and contacts"**
Hellewell J, Abbott S, Gimma A, Bosse NI, Jarvis CI, Russell TW, Munday JD, Kucharski AJ, Edmunds WJ, CMMID COVID-19 Working Group, Funk S, Eggo RM. *Lancet Glob Health* 8(4):e488–e496. PMC7097845.

**Archetype:** the *stochastic feasibility* paper — a branching-process model with no fitted data at all, used to map the parameter space in which a control strategy can or cannot work. The output is a boundary, not an estimate.

## Structure
Structured abstract (**Background / Methods / Findings / Interpretation / Funding**) → `Research in context` panel → `Introduction` → `Methods` (*Model structure*, *Transmission scenarios*, *Definition of outbreak control*, *Role of the funding source*) → `Results` → `Discussion` → `Data sharing` → Acknowledgements → Contributors → Declaration of interests.

The subheading **"Definition of outbreak control"** is the important one: when the outcome is a binary success/failure, define it formally in Methods and defend the definition.

## Opening move
> "Isolation of cases and contact tracing is used to control outbreaks of infectious diseases, and has been used for coronavirus disease 2019 (COVID-19). Whether this strategy will achieve control depends on characteristics of both the pathogen and the response. Here we use a mathematical model to assess if isolation and contact tracing are able to control onwards transmission from imported cases of COVID-19."

Pattern: **the strategy already in use → the conditional on which its success depends → "Here we use a mathematical model to assess if…".** The question is posed as a genuine yes/no whose answer depends on parameters — which is exactly what the model can answer and an estimate cannot.

## Methods
- Model named and specified in one sentence: "We implemented a branching process model, in which the number of potential secondary cases produced by each individual is drawn from a negative binomial distribution…" The negative binomial is chosen for overdispersion, and overdispersion later does real explanatory work in the Results.
- Figure 1 is a **schematic of the simulated process with an annotated worked example** — the reader sees one simulated chain before seeing any aggregate output.
- The parameter table distinguishes **"Sampled" vs "Fixed"** parameters and gives a reference for each. This one column tells the reader exactly where uncertainty is propagated and where it is not.
- Scenario grid stated exhaustively: R₀ ∈ {1.5, 2.5, 3.5}; initial cases ∈ {5, 20, 40}; short/long delay to isolation; pre-symptomatic transmission ∈ {0%, 15%, 30%}; subclinical ∈ {0%, 10%}. "We ran 1000 simulations of each combination…"
- A **baseline scenario is declared and used as the anchor for every comparison**: "We present results in relation to the baseline scenario of R₀ of 2·5, 20 initial cases, a short delay to isolation, 15% of transmission before symptom onset, and 0% subclinical infection."
- Optimistic assumptions are made explicit so the result reads as an upper bound: "Isolation was assumed to be 100% effective at preventing further transmission"; "The model included isolation of symptomatic individuals only—ie, no quarantine…"
- Appendix carries the non-baseline R₀ values and all sensitivity analyses.

## Results
The headline is a **threshold**, not a point estimate:
> "To achieve control of 90% of outbreaks, 80% of contacts needed to be traced and isolated for scenarios with a reproduction number of 2·5."
> "The delay from symptom onset to isolation had a major role in achieving control of outbreaks. At 80% of contacts traced, the probability of achieving control fell from 89% to 31%, with a long delay from onset to isolation."
> "At a reproduction number of 1·5, the effect of isolation was coupled with the chance of stochastic extinction resulting from overdispersion, which is why some outbreaks were controlled even at 0% contacts traced."
> "In many scenarios, between 25 and 100 symptomatic cases occurred in a week at the peak of the simulated outbreak."

Uncertainty is reported as **medians with 50% and 95% intervals across simulations** (stated in figure captions), and delays as medians with IQR. Note the third quote: an unexpected result is stated *and mechanistically explained in the same sentence*.

## Literature
Numbered citations, ~15 in a four-paragraph introduction. Prior epidemics are used as mechanistic analogies rather than as citations:
> "Isolation of cases and contact tracing becomes less effective if infectiousness begins before the onset of symptoms. For example, the severe acute respiratory syndrome (SARS) outbreak that began in southern China in 2003, was eventually able to be controlled through tracing contacts of suspected cases and isolating confirmed cases because the majority of transmission occurred after symptom onset."

Form: **principle → historical case that instantiates it → the mechanism that explains the case.** The reader now knows what would make COVID-19 different before being told.

## Voice
Past for what was done, present for what follows. Active, first-person plural: "We implemented", "we assumed", "we explored". Hedging tracks the conditionality of the whole exercise: "Whether this strategy will achieve control depends…", "is likely to be determined…", "both are likely to make the outbreak harder to control". Contribution claimed modestly: "Our analysis expands on this work by including…".

## Discussion and limitations
> "We simplified our model to determine the effect of contact tracing and isolation on the control of outbreaks…"
> "Our model did not include other control measures that might decrease the reproduction number and therefore also increase the probability of achieving control of an outbreak. At the same time, it assumed that isolation of cases and contacts is completely effective, and that all symptomatic cases are eventually reported. Relaxing these assumptions would decrease the probability that control is achieved."

The final clause is the move to steal: **state the direction in which each assumption biases the conclusion.** Optimistic assumptions plus a pessimistic conclusion is a strong argument; the reader is told so explicitly.

Practical limits are named too: "Practically, there is likely to be an upper bound on the number of cases that can be traced…"; and the outcome definition is revisited reflexively: the definition "might be narrowed where the goal is to keep the overall caseload of the outbreak low".

## Data, code and funding
> "No data were used in this study. The R code for the work is available at https://github.com/cmmid/ringbp."
> "The funders of the study had no role in study design, data collection, data analysis, data interpretation, writing of the Article, or the decision to submit for publication."
The model ships as an installable R package, not a script dump.

## Distinctive moves to borrow
1. **Declare a baseline scenario and vary one thing at a time from it.**
2. Label every parameter as sampled or fixed.
3. When you assume the best case and still find failure, say so explicitly — it converts a limitation into strength.
4. Define "control" formally, then question your own definition in the Discussion.

## Related files
Other *feasibility / threshold* exemplars: see [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md) for a feasibility threshold and an operational checklist from a very large individual-based simulation; [81-kucharski-2016-ebola-ring-vaccination](81-kucharski-2016-ebola-ring-vaccination.md) for a branching-process threshold on missed cases beyond which ring vaccination cannot contain an outbreak; [76-famulare-2018-polio-opv-cessation](76-famulare-2018-polio-opv-cessation.md) for a threshold statistic that sorts settings into three categories of outbreak risk, each checked against history; [79-golumbeanu-2022-malaria-tpp-emulator](79-golumbeanu-2022-malaria-tpp-emulator.md) for minimum coverage, efficacy and duration a new intervention must reach, found by searching an emulator of a simulation model.
