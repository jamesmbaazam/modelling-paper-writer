# 25 — Davies et al. (2020), *The Lancet Public Health*
**"Effects of non-pharmaceutical interventions on COVID-19 cases, deaths, and demand for hospital services in the UK: a modelling study"**
Davies NG, Kucharski AJ, Eggo RM, Gimma A, Edmunds WJ, CMMID COVID-19 working group. *Lancet Public Health* 5(7):e375–e385. PMC7266572.

**Archetype:** the *scenario projection for policy* paper — an age-structured stochastic model run under a ladder of intervention scenarios, written while the decisions it informs are still being made.

## Structure
Structured abstract (**Background / Methods / Findings / Interpretation / Funding**) → `Research in context` → `Introduction` → `Methods` (*Dynamic transmission model*, *Key model parameters*, *Intervention scenarios*, *Intervention timing and adherence*, *Further analyses of individual interventions*, *Intensive interventions and lockdowns*, *Role of the funding source*) → `Results` → `Discussion` → `Data sharing` → Acknowledgements → Contributors → Declaration of interests.

The Methods subheadings separate **model**, **parameters**, **scenarios** and **timing/adherence**. Timing and adherence get their own subheading because in an NPI paper they are the intervention, not a detail.

## Opening move
> "Non-pharmaceutical interventions have been implemented to reduce transmission of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) in the UK. Projecting the size of an unmitigated epidemic and the potential effect of different control measures has been crucial to support evidence-based policy making during the early stages of the epidemic."

Pattern: **what is already being done → why projection is needed to evaluate it.** The paper claims a supporting role to decision-making, and the Discussion later makes that literal.

## Methods
- Model described structurally before mathematically: "stochastic compartmental model stratified into 5-year age bands"; Figure 1 shows the state-transition diagram before any equation.
- **Table 1 defines every scenario as percentage changes to contacts by setting** (e.g. school closure → school contacts 0%, home contacts 100%). A scenario table in this form is the single most useful artefact in an NPI paper — it makes scenarios comparable and reproducible.
- Parameters are synthesised, not asserted: R₀ derived from "a meta-analysis of studies and preprints published before Feb 26, 2020", giving "R₀ was 2·7 (95% credible interval 1·6–3·9)". Contact matrices from "survey data collected in Great Britain in 2006", with the age of the data stated plainly.
- Assumptions given with a reason: subclinical cases "assumed…50% as infectious as preclinical and clinical infections"; "We assumed that lockdowns would reduce all contacts outside the home by 90% from their baseline values."
- Appendix referenced to the page throughout ("appendix pp 2–5", "appendix p 10"); 200 stochastic simulations per scenario.

## Results
Medians with **95% prediction intervals** (not confidence or credible — the quantity is a simulated future), and burden expressed in the units health systems use.
> "We projected a median unmitigated burden of 23 million (95% prediction interval 13–30) clinical cases and 350 000 deaths (170 000–480 000) due to COVID-19 in the UK by December, 2021."
> "This is roughly 13–80 times ICU capacity in the UK, which we tallied at 4562 beds, in the absence of any efforts to further expand capacity."
> "When school closures, physical distancing, shielding of older people, self-isolation of symptomatic individuals, and the combination intervention were timed to centre on the peak of the unmitigated epidemic, they each decreased the total number of cases by 20–30% and delayed the peak of the epidemic by 3–8 weeks on average."
> "We found that, when implemented alone, none of these shorter-duration interventions were able to decrease health-care need to below available capacity."
> "The recurrent lockdown scenario with the most stringent triggering threshold of 1000 ICU beds occupied by COVID-19 patients reduced total COVID-19 deaths by 58% (95% PI 30–80) relative to the intensive interventions scenario."

Two devices: **express projections against a capacity constraint** ("13–80 times ICU capacity") rather than as bare counts, and **state each comparison's reference scenario** ("relative to the intensive interventions scenario").

Results escalate in complexity: single interventions → combinations → intensive interventions → triggered recurrent lockdowns, each with its own figure.

## Literature
Numbered citations; preprints cited without apology, which is appropriate and honest in a fast-moving situation. Prior work is summarised as a consensus with a residual gap:
> "Several studies have explored the potential effect of control measures on the dynamics of COVID-19. These studies have broadly suggested that moderate measures could reduce epidemic size, but more intensive measures would be required to ensure health system capacity was not surpassed."
The `Research in context` panel then names the gap: "it remains unclear how different combinations of interventions, timings, and triggers for the introduction and lifting of control measures could affect the impact of the epidemic on health services."

## Voice
Past tense for what was run and found ("We projected", "We found", "We simulated"); present for model description ("The model tracks 66·4 million people"). Active with occasional purposeful passive ("Interventions were assumed to uniformly decrease the number of contacts"). Hedging is honest about the object: "would probably be more effective", "It remains unclear precisely how the timing, duration, and intensity of different measures … can reduce the impact".

## Discussion and limitations
> "The model presented here is subject to several limitations. Because the model does not explicitly structure individuals by household, we are unable to evaluate the impact of measures based on household contacts, such as household quarantine, where all members of a household with a suspected COVID-19 case remain in isolation."
> "The length of stay in ICU and the fractions of hospitalisation, ICU use, and death are estimated using data from China, and differences in UK populations could affect our estimates of health-care demand."

Each limitation names **the specific question the model therefore cannot answer** — a much more useful formulation than "the model is a simplification".

## Distinctive moves to borrow
1. **Table 1 as a contact-matrix scenario definition.** Percentages by setting; nothing left to prose.
2. Report projections relative to a hard capacity constraint.
3. Compare to reality where possible, and say why the comparison is imperfect: "Directly comparing these projections to the ongoing COVID-19 epidemic in the UK is complicated because enacted control measures have not exactly followed the scenarios outlined here. However, as a point of comparison, recent empirical estimates of the reproduction number in the UK are compatible with our assumptions."
4. **Say when the analysis was done and for whom**: "The results we present here summarise the key analyses and scenarios we presented to decision makers over February–March, 2020, which evolved continuously as new information became available." This dates the work honestly and pre-empts hindsight criticism.

## Related files
Other *scenario projection for policy* exemplars: see [12-ferguson-2006-mitigating-pandemic](12-ferguson-2006-mitigating-pandemic.md) for a large individual-based simulation organised around intervention options, with almost no equations; [47-ngonghala-2020-npi-math-assessment](47-ngonghala-2020-npi-math-assessment.md) for a stability analysis that precedes the scenarios, in the applied-mathematics register; [69-kerr-2021-test-trace-quarantine](69-kerr-2021-test-trace-quarantine.md) for scenarios run on a documented agent-based model and then checked against the months that followed; [78-rock-2022-hat-mandoul-update](78-rock-2022-hat-mandoul-update.md) for a model update that audits its own earlier projections against the data that followed.
