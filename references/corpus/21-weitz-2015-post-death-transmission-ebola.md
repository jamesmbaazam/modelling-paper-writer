# 21 — Weitz & Dushoff (2015), *Scientific Reports*
**"Modeling post-death transmission of Ebola: challenges for inference and opportunities for control"**
*Sci Rep* 5:8751. doi:10.1038/srep08751. PMC4348651.

**Archetype:** the *identifiability / inference-critique* paper — a short, two-author, argument-driven contribution whose result is that a widely fitted quantity cannot be identified from the data everyone is using. The template for writing a negative or cautionary methodological result.

## Structure
Abstract → Introduction (unheaded) → `Results` with **findings as subheadings** → `Discussion` → `Methods` (last) → Author Contributions → Acknowledgements → ~25 references.

Results subheadings are full declarative claims:
- *The basic reproductive number, R₀, of EVD includes effects of post-death transmission*
- *Identifiability problems in estimating R₀*
- *Challenges in fitting early-stage epidemic data of EVD in West Africa*
- *Reduction in transmission risk after death can have substantial epidemiological benefits*

Read in sequence they are the paper's argument. Methods subheadings are plain: *SEIRD model of Ebola dynamics*; *Estimating R₀ for SEIR and SEIRD models given exponential distributions*; *Case data information*.

## Opening move
> "Multiple epidemiological models have been proposed to predict the spread of Ebola in West Africa. These models include consideration of counter-measures meant to slow and, eventually, stop the spread of the disease. Here, we examine one component of Ebola dynamics…"

Pattern: **a crowded modelling literature → what it has in common → "Here, we examine one component…".** The paper claims a narrow target deliberately; it is a critique of an assumption, not a rival model.

## Methods
- **Verbal statement before formal statement, always.** "In a conventional SEIR model, EVD transmission between infected and susceptible individuals occurs at an average rate βI over a period of infectiousness T_I" — then the R₀ expression follows.
- Notation is systematic and predictable: Greek letters for rates (β), compartment letters as subscripts (I, D), T for durations, f and ρ for fractions and relative risks.
- Unknowns are bounded by external evidence rather than fitted freely: "prior information is available to constrain the mean duration of the latent phase on the order of 8–12 days".
- Instead of one sensitivity analysis, the paper explores a **continuum of models** (varying T_D = 2, 4, 6 days and the post-death transmission fraction) precisely to demonstrate that many parameter combinations fit equally well. The exploration *is* the result.

## Results
Point estimates given plainly, with the identifiability caveat attached:
> "We find a point estimate of β_SEIR of 0.33 and a corresponding R₀ for the SEIR model of 1.95."
> "Importantly, the point-estimate of R₀ increases with increasing force of transmission post-death."
> "We find a negative relationship between the estimated pre- and post-death transmission rate."
> "This is a generic feature of epidemiological models."

The last sentence shows the paper's habit of **generalising each specific finding one level up**: this is not an Ebola quirk, it is a property of the model class. That is what makes a short cautionary paper worth citing.

The narrative arc: demonstrate the structural point analytically → show it bites on real West African incidence data → show that despite the non-identifiability one robust conclusion survives ("Despite this identifiability problem, we find robustly that…") → convert that into a control recommendation.

## Literature
Numbered brackets, dense in the Introduction. The gap is a gap in *evaluation*, not in awareness:
> "Yet, the implications of post-death transmission for inferences about epidemic spread have not been evaluated systematically."
Prior models are cited respectfully and treated as the object of study rather than as competitors.

## Voice
Present for general model properties, past/present-perfect for what this analysis found. Active, first-person plural: "we examine", "we apply", "we show", "we find". Hedging is about parameter space rather than about confidence: "potentially many combinations of transmission parameters", "would lead to corresponding uncertainty".

## Discussion and limitations
Limitations and results are the same material here, which is the point:
> "The relative importance of post-death transmission is difficult to estimate from epidemic growth rate data alone, and has important implications for estimates of key epidemiological quantities…"

## Distinctive moves to borrow
1. **Interrogate the apparently obvious.** "It might seem that the basic reproductive number of a SEIRD model should tautologically exceed that of a SEIR model. In fact, this will depend on how parameters are estimated." Setting up and then dissolving a plausible intuition is an efficient way to establish that a paper is needed.
2. **Turn non-identifiability into a positive claim.** Do not report a failed fit; report what the data can and cannot determine, and then find the conclusion that holds across the whole indeterminate set.
3. Escalate specific findings to the model class ("This is a generic feature of epidemiological models").
4. Close on control: the same parameter that cannot be identified is the one whose reduction would help most.
