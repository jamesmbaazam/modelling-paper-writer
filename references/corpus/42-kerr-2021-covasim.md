# 42 — Kerr et al. (2021), *PLoS Computational Biology*
**"Covasim: An agent-based model of COVID-19 dynamics and interventions"**
Kerr CC, Stuart RM, Mistry D, Abeysuriya RG, Rosenfeld K, Hart GR, et al. *PLoS Comput Biol* 17(7):e1009149. doi:10.1371/journal.pcbi.1009149.

**Archetype:** the *agent-based model documentation* paper — describe a simulation model and its software as the contribution, in enough detail that someone else can run it, calibrate it and judge what it can be asked. The corpus's exemplar for the ◆ ODD-style model-documentation rule in `SKILL.md` §6.

## Structure
PLoS Comput Biol: `Abstract` → **`Author summary`** → `1 Introduction` → **numbered `2 Methods` with deep subsections** (demographics and networks · transmission and within-host viral dynamics · disease progression · interventions · diagnostics and contact tracing · multi-region modelling · calibration · *2.7 Software architecture* with *2.7.1 Performance*) → `3 Results` (an applied case study) → `4 Discussion` (*4.1 Limitations of Covasim* · *4.2 Future directions*) → availability.

Two structural decisions define the archetype:

- **Numbered, deeply nested sections.** A documentation paper is a reference work; readers arrive at §2.6.8 from a cross-reference, not from the start. The paper cross-references its own sections in the text ("this parameter must be calibrated by the user to match local epidemic data, as described in Section 2.6.8"), which only works if the sections are numbered.
- **A dedicated `Software architecture` section** covering language, dependencies, licence, distribution and performance. The model and the code are documented as one artefact.

## Opening move
> "The COVID-19 pandemic has created an urgent need for models that can project epidemic trends, explore intervention scenarios, and estimate resource needs. Here we describe the methodology of Covasim (COVID-19 Agent-based Simulator), an open-source model developed to help address these questions."

**Three named jobs, then the tool that does them.** The abstract then enumerates the model's contents as a list of capabilities rather than describing them in prose — demographics, "realistic transmission networks in different social layers, including households, schools, workplaces, long-term care facilities, and communities", age-specific outcomes, within-host viral dynamics, and an intervention set spelled out in three families. A reader deciding whether to adopt the model can answer that question from the abstract alone, which is what a documentation abstract is for.

**The Introduction situates the model in a taxonomy before claiming anything**, with the trade-off stated plainly:
> "Models for examining COVID-19 transmission and control measures can be broadly divided into two main types: compartmental models and agent-based models (also called individual-based or microsimulation models), with the former generally being simpler and faster, while the latter are generally more complex, detailed, and computationally expensive."

Then the gap that justifies the expensive option: "However, more detailed models are needed to evaluate scenarios based on complex intervention strategies. These strategies are important to evaluate in order to understand the epidemiological impact of reopening schools, businesses, and society." **An agent-based model needs an explicit argument for why the extra complexity is required**, and it is given in terms of the questions that cannot otherwise be asked.

## Methods
- **Give the default parameter value, what it corresponds to in familiar terms, where it came from, and where it does not apply** — the model paragraph worth copying wholesale:
  > "For a well-mixed population where each individual has an average of 20 contacts per day, a value of β = 0.016 corresponds to a doubling time of roughly 4–6 days and an R₀ of approximately 2.2–2.7, with the exact value depending on the population size, age structure, and other factors. The value of β = 0.016 that is currently used as the default in Covasim was based on calibrations to data from Washington and Oregon states. However, this default value is too low for high-transmission contexts such as New York City or Lombardy, and may be too high for low-transmission contexts such as India's first wave. Hence, this parameter must be calibrated by the user to match local epidemic data."

  Translating a transmission probability into a doubling time and an R₀ makes an otherwise opaque default auditable; naming the settings where it fails converts a default into guidance.
- **Give per-layer parameters, not a single global one**: "Default transmission probabilities are roughly 0.050 per contact per day for households, 0.010 for workplaces and schools" — because the layered network is the model's reason to exist.
- **Document the software stack by name**: Python 3.8 on SciPy, with NumPy, Pandas and Numba "for fast numerical computing", Matplotlib and Plotly for plotting, Sciris "for data structures, parallelization, and other utilities".
- **Explain an implementation decision in terms of the performance it buys**, with a magnitude:
  > "agents are not represented as individual objects, but rather as indices of one-dimensional state arrays. This avoids the need to use an explicit for-loop over each agent on every integration timestep, increasing performance by more than an order of magnitude."

  A documentation paper should say *why* the code is shaped as it is, not only what it does — and a figure contrasts the standard object-oriented layout with this one.

## Results
**The Results section is a single worked case study**, which is the right way to demonstrate a tool: it shows the workflow end to end rather than listing features again. The case study names the place, the period, the calibration tool, the data source, and the three questions in order:
> "we used Optuna to calibrate Covasim to epidemiological and program data from January 27 to November 14 2020; these data are available from the Public Health Seattle King County data dashboard. We then ran the model with eight different calibrated parameter sets (with multiple parameter sets used to capture parametric uncertainty) to (a) estimate unobserved quantities, such as the number of new infections and the case detection rate; (b) estimate the impact of proposed new mobility restrictions (such as limiting indoor dining) scheduled to start on November 16, which we estimated would result in a 15% reduction in transmission; and (c) compare this scenario with counterfactual scenarios of either not implementing the scheduled restrictions, or by implementing them together with increased testing and contact tracing."

**Multiple calibrated parameter sets are used explicitly to carry parametric uncertainty** — the agent-based analogue of reporting a posterior rather than a point estimate — and the counterfactual set is stated as a set, with the do-nothing arm named.

## Literature
Numbered PLoS citations. Other COVID-19 models are cited by what they did rather than ranked ("Walker et al. used an age-structured stochastic 'susceptible, exposed, infectious, recovered' (SEIR) model to determine the global impact of COVID-19…"), and even data dashboards are credited with their limitation attached: "despite their limitations, data dashboards have proven crucial for understanding the current state of the epidemic on both global and local scales."

## Voice
First-person plural, present tense for what the software does and past for what the authors did. The register is unusually direct about engineering trade-offs, and the paper is willing to say a choice cost something:
> "choosing to implement Covasim in Python instead of C++ or Java significantly reduced development time and increased simplicity for users and developers; however, it imposed a large penalty on performance. While we were able to solve this by using Numba and vectorized state arrays in place of object-oriented agents, this implementation increased development time…"

## Discussion and limitations
Opens by naming the conditions the model was built under rather than the results — "requiring rapid, accurate predictions, often based on extremely limited data, with consequences of global scale" — then states the design priorities as an explicit, ordered list: "We prioritized five different factors when developing Covasim: rapid development process, computational performance, flexibility, simplicity for users, and simplicity for developers. Striking a balance between these factors required making certain tradeoffs."

**Naming the design priorities, and then showing where they conflicted, is what makes a software paper reviewable.**

`4.1 Limitations of Covasim` is a model limitations section done properly:
- **The structural limit, with a concrete instance**: "human contact patterns are intractably complex, and the algorithms that Covasim uses to approximate these are necessarily quite simplified."
- **Input uncertainty, narrowed to the parameters that actually matter for the model's main use**: "many of the parameters on which Covasim relies are still subject to large uncertainties. Most critically, the proportion of asymptomatics and their relative transmission intensity, and the proportion of presymptomatic transmission, strongly affect the number of tests required in order to achieve workable COVID-19 suppression via testing-based interventions."
- **Three named obstacles to validating the model at all**, the third of which is rarely admitted in print:
  > "(a) data quality issues (such as low case detection rates and under-reporting of deaths); (b) the difficulty of predicting future social and political responses that would significantly impact model projections (such as the timing of school and workplace reopening, or a sudden increase in testing rates…); and (c) the fact that model-based projections themselves have the potential to influence policy decisions, e.g., optimistic model projections may lead to relaxed policies, which in turn will lead to worse outcomes than predicted, while pessimistic model projections may lead to stricter policies, which in turn will lead to better outcomes than predicted."

  **Point (c) — that a policy model's own projections change the system it is projecting — is the deepest limitation available to this archetype**, and it is stated with both directions of the feedback spelled out.

## Data, code and funding
Exemplary for a software paper: installation route (`pip install covasim`), source repository, explicit licence ("released under the Creative Commons Attribution-ShareAlike 4.0 International Public License"), project website, "full documentation and a comprehensive set of tutorials" at a documentation site, and named versions for the stack. **A model-documentation paper must state how to install it, where the source is, what licence governs reuse, and where the tutorials are** — four facts, each a URL.

## Distinctive moves to borrow
1. **Argue for the model class before the model.** Agent-based models cost more; say which questions require them.
2. **Enumerate capabilities in the abstract** so a reader can decide whether to adopt the tool without reading on.
3. **Number the sections deeply and cross-reference them**, because a documentation paper is read out of order.
4. **Translate an opaque default parameter into familiar quantities** (doubling time, R₀), say which data it was calibrated to, and name the settings where it is wrong.
5. **Give per-layer parameters** when the layered structure is the contribution.
6. **Explain implementation choices by the performance they buy**, with a magnitude.
7. **Make the Results a single end-to-end case study**, naming place, period, calibration tool, data source and the questions in order.
8. **Carry parametric uncertainty with multiple calibrated parameter sets**, and say that is what they are for.
9. **State design priorities as an ordered list and show where they conflicted**, including what a choice cost.
10. **Name the obstacles to validation**, including that policy models change the behaviour they predict — in both directions.
11. **Give install route, source, licence and documentation URL** in the availability statement.

## Related files
For large individual-based policy simulation written for a general-science audience see [12-ferguson-2006-mitigating-pandemic](12-ferguson-2006-mitigating-pandemic.md) and [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md); for the farm-level individual-based model see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md); for the other corpus paper that documents a tool alongside its estimates see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md); for the contact-structured scenario tables Covasim's interventions implement see [25-davies-2020-npi-uk](25-davies-2020-npi-uk.md).
