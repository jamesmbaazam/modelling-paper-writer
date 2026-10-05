# 57 — Yakob et al. (2015), *Scientific Reports*
**"Mechanisms of hypervirulent *Clostridium difficile* ribotype 027 displacement of endemic strains: an epidemiological model"**
Yakob L, Riley TV, Paterson DL, Marquess J, Clements ACA. *Sci Rep* 5:12666. doi:10.1038/srep12666.

**Archetype:** *competing hypotheses* in its purest form — three biological mechanisms, each operationalised as **one parameter**, each swept across its plausible range, and ranked by which can reproduce the observed epidemiology. The clearest demonstration in the corpus of **ruling a mechanism out**.

## Structure
*Scientific Reports*: `Abstract` → unheaded introduction with **one sub-heading per candidate mechanism** → `Methods` → `Results` → `Discussion` (with a dedicated limitations passage).

**The introduction's sub-headings are the hypotheses themselves**, each a declarative sentence:
> *Hypervirulent strains are more infectious than endemic strains* · *Hypervirulent strains result in a higher rate of symptomatic disease* · *Hypervirulent strains can outcompete endemic strains in the host's gut*

**When a paper tests competing explanations, make each one a heading stated as a claim.** A reader can see the full hypothesis space before any modelling, and each section assembles the biological evidence for and against that mechanism specifically.

## Opening move
Burden first, with the clinical range that makes it matter: "It is reported to be the leading cause of infectious diarrhoea in healthcare facilities of developed nations… Disease severity ranges from asymptomatic infection to potentially fatal conditions including toxic megacolon, bowel perforation and sepsis."

Then the emergence is narrated with dates, places and speed:
> "In 2005, when performing a Europe-wide survey of 38 hospitals in 14 countries, the European Study Group of C. difficile found a novel ribotype (BI/NAP1/027) in Ireland, the Netherlands and Belgium. Within 3 years this PCR ribotype had spread to at least 16 European countries and was rapidly becoming one of the more prominent strains in North America."

**The gap is an absence of consensus, not of work**: "Over the past decade, research has been conducted to understand hypervirulence in C. difficile with no consensus reached on precise causative mechanisms." And the term under investigation is shown to be ill-defined: "Clear disambiguation between hypervirulent and typical strains is currently precluded by incomplete understanding of what causes some strains to generate outbreaks with substantial morbidity."

**Justify the choice of study organism on two grounds, one of them about data availability:**
> "We use ribotype 027 to demonstrate the invasion dynamics of hypervirulent strains because it was the causative agent of the largest recorded outbreak of C. difficile and because the considerable literature pertaining to this particular strain facilitates more accurate model parameterisation."

Importance *and* parameterisability. The second reason is the honest one and is rarely stated.

## Methods — assembling the hypotheses
Each mechanism gets a section that presents the supporting experimental evidence **and the evidence against it**:

- **Mechanism 1**, with the *in vitro* result and then the contradiction: "In vitro studies conducted by Merrigan and colleagues examined the accumulation of spores over the bacterial growth cycle and demonstrated that hypervirulent strains sporulated earlier and accumulated significantly more spores per total volume of culture than non-hypervirulent strains… However, due to recent evidence to the contrary, the notion of enhanced sporulation in hypervirulent strains remains contentious."
- **Mechanism 2**, with the clinical observation and the same even-handedness: "Studies conducted by Pépin and colleagues and Hubert et al. both describe a doubling in the rate of complicated cases (severe disease) during the rise of ribotype 027 in Canada… It is important to note that there is also contention surrounding the notion of more disease (relative to asymptomatic carriage) and worse disease outcomes from hypervirulent infections."
- **Mechanism 3**, with the experimental design that supports it described in enough detail to judge: "Four ribotype 027 clinical isolates and clinical isolates of four other strains (001, 002, 014 and 053) were pairwise tested in human fecal bioreactors and in a humanized microbiota mouse model. Ribotype 027 strains outcompeted endemic strains both in vitro and in vivo."

**Give each hypothesis its strongest evidence and its strongest objection before testing it.** A comparison is only credible if the loser was given a fair hearing.

**The modelling choices themselves:**
- **State the question the simulation answers**: "To offer unique perspective to the critical epidemiological question of which mechanism underlies the rapid global spread (and for many regions, the subsequent clonal dominance) of ribotype 027, we analysed the simulated invasion of hypervirulent C. difficile following its introduction into a human community."
- **Name the algorithm, the software and its version, and the published recipe followed**: "A Direct Gillespie algorithm was scripted in Matlab® software version 7.12… Following the numerical recipe outlined by Keeling and Rohani (2007), an exact stochastic analogue of the following set of ordinary differential equations was constructed."
- **Label the parameter table with the mechanism each parameter encodes.** Table 1 carries `MECHANISM 1`, `MECHANISM 2`, `MECHANISM 3` against the relevant rows, with ranges rather than point values — βh:β of 1–1.5, εh:ε of 1–1.5, α of 0–1 — and the note "Full range tested in simulations".

**Tagging parameters with the hypothesis they operationalise is the single most reusable device in this paper.** It makes the mapping from biology to mathematics auditable at a glance.

## Results
**Report the trivial result first and dismiss it**, so the informative comparison is clear: "Intuitively, the parameters governing these different mechanisms all had positive relationships with the probability of an invading strain establishing in the community. **However, comparing the influence of these parameters on the rate of invasion and the resultant equilibrium prevalence yielded strikingly different epidemiological patterns.**"

All three mechanisms help the strain invade — that is uninformative. The discrimination comes from *how* they help, across two outcomes.

**Compare on more than one outcome**, because a single summary would not separate the mechanisms: establishment probability, rate of spread, and equilibrium prevalence are each reported per mechanism.

**Explain the negative result mechanistically rather than just reporting it** — the best sentence in the paper:
> "When individuals colonized with endemic strains were susceptible to colonization with hypervirulent strains (the third modelled mechanism of hypervirulence) a much weaker relationship was found with likelihood of establishment, and no clear relationship was seen with the resulting equilibrium prevalence. **This is because the spread of the newly introduced strain is essentially independent of the resident strain endemicity when a resident strain-colonized gut is colonized just as readily as an uncolonized gut.**"

**Rule a mechanism out by showing it cannot reproduce the observation, across its whole parameter range:**
> "it appears that an ability of hypervirulent strains to displace endemic strains from the already-colonized host gut is the least likely mechanism facilitating dominance of ribotype 027. Despite testing a broad range of parameter values, from complete colonization resistance to susceptibility equivalent to an uncolonized individual, the newly introduced strain failed to reproduce the heightened prevalence level associated with emerging hypervirulent strains."

**The construction *despite testing a broad range of parameter values, from X to Y* is what makes a negative result credible** — the mechanism failed everywhere it could have worked, not merely at one setting.

**Then bound the negative claim precisely**, distinguishing what was ruled out from what was not:
> "This finding does not negate the possibility that hypervirulent strains are more competitive within-host than more typical strains; but it does suggests that this mechanism is not key to the successful invasion and clonal dominance of hypervirulent strains such as ribotype 027."

The biology may be real; it is the *epidemiological role* that is excluded. **Say which claim your negative result kills and which it leaves standing.**

**Report a finding that holds across all the hypotheses**, independent of which wins: "the current study demonstrated that direct competition between strains (inside the host's gut) is not a prerequisite for the sudden switching in prevailing strains; simulations of all alternative hypervirulence mechanisms clearly illustrated that previously dominant strains are not simply added to following new strain invasion, but are excluded through indirect (exploitative) competition." A conclusion that survives the unresolved comparison is worth more than the comparison itself.

## Discussion and limitations
**Declare the limit of the discrimination honestly**, including that the study cannot finish the job:
> "Transmission dynamics of the remaining alternative hypervirulence mechanisms (increased infectiousness and increased symptomatic disease) are much more similar and, therefore, will be much more difficult to disentangle. It is likely that distinguishing between the remaining alternatives will not be possible from comparisons of simulation output with longitudinal, ribotyped infection data, and will necessitate a much clearer clinical picture of C. difficile infection."

**State that two of your three hypotheses are not separable with any amount of the available data**, and name the kind of evidence that would separate them. This is an identifiability claim, and it is more useful than a forced ranking.

Then the model is positioned as infrastructure for when that evidence arrives: "When these data become available in the future and/or there is increasing evidence derived through alternative means that favours a particular mechanism of hypervirulence, the current model formulation offers an important epidemiological tool for contributing towards infection control strategy."

**The limitations are explicit about parameter provenance**, and generalise the problem rather than treating it as local:
> "Despite burgeoning interest in this pathogen of global health significance, basic metrics of the infection process, such as latent periods, are scant in the literature. Due to limited information on the life history of C. difficile infection, parameterisation of the current model has depended on numbers amassed from multiple studies across multiple epidemiological settings. This is a common issue with biologically realistic simulation modelling. While a substantial effort was made in preferentially selecting recent studies that better reflected the pathogen's modern epidemiology (published within the past 5 years) as sources of parameter estimates, this was not always possible."

**Name the rule you used to choose between conflicting parameter sources** — here, recency reflecting modern epidemiology — and admit where you could not follow it.

A further limitation concedes the structural simplification: that the mechanisms were treated as alternatives rather than as potentially co-occurring.

The novelty claim is scoped to two specific firsts rather than asserted broadly: "the current study constitutes the first epidemiological model of C. difficile transmission within the wider community as well as the first comparative analysis of alternative mechanisms of hypervirulence" — with the justification for the community focus given immediately before it ("recent studies have suggested that the community is a major source, if not the primary source, of infections experienced by the high-risk groups within healthcare settings").

## Distinctive moves to borrow
1. **Make each competing hypothesis a sub-heading stated as a claim**, and assemble its evidence before any modelling.
2. **Give each hypothesis its strongest objection too** — "remains contentious", "there is also contention surrounding" — so the comparison is fair.
3. **Operationalise each mechanism as one parameter**, and **tag the parameter table with the mechanism it encodes**.
4. **Sweep the full plausible range** rather than testing a point value, and say so in the table.
5. **Justify the study organism on importance *and* parameterisability.**
6. **Report the uninformative result first and dismiss it**, so the discriminating comparison stands out.
7. **Compare on several outcomes** — establishment, speed, equilibrium prevalence — because one would not separate the mechanisms.
8. **Explain a negative result mechanistically**, not just numerically.
9. **Say *despite testing a broad range of parameter values, from X to Y*** when ruling something out.
10. **Bound the negative claim**: distinguish the biology you did not disprove from the epidemiological role you did.
11. **Report what holds across all hypotheses**, independent of which wins.
12. **Declare when two hypotheses are not separable with available data**, and name the evidence that would separate them.
13. **State the rule you used to choose between conflicting parameter sources**, and where you could not follow it.

## Related files
For the other competing-hypotheses exemplars see [24-davies-2021-b117-transmissibility](24-davies-2021-b117-transmissibility.md), which ranks mechanisms by DIC and reports the runners-up, and [56-lavine-2021-endemicity](56-lavine-2021-endemicity.md), which separates components of one concept; for identifiability limits stated as the result see [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md); for stochastic simulation of invasion and extinction see [22-hellewell-2020-contact-tracing-feasibility](22-hellewell-2020-contact-tracing-feasibility.md) and [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md). Other *competing hypotheses* exemplars: see [74-lopman-2012-rotavirus-vaccine-efficacy](74-lopman-2012-rotavirus-vaccine-efficacy.md) for an efficacy gradient across income settings decomposed into the share each hypothesis explains, with one ruled out.
