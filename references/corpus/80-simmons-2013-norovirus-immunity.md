# 80 — Simmons et al. (2013), *Emerging Infectious Diseases*
**"Duration of immunity to norovirus gastroenteritis"**
Simmons K, Gambhir M, Leon J, Lopman B. *Emerg Infect Dis* 19(8):1260–1267. doi:10.3201/eid1908.130472.

**Archetype:** *parameter estimation* that overturns a textbook value — the duration of immunity to norovirus, long quoted as six months to two years from 1970s challenge studies, re-estimated from community incidence with a transmission model and found to be four to nine years. The estimate is made robust not by one fit but by six models that differ in the assumptions nobody can check.

## Structure
EID research article: a one-paragraph abstract of under 150 words → unheaded introduction → `Methods` (*Model Design* · *Model Scenarios*, one subsection per model A–F · *Data and Model Fitting*) → `Results` → `Discussion` → technical appendix → the journal's required **biographical sketch** of the first author.

**The six models get a subsection each**, named for the one assumption they change — *Presymptomatic and Postsymptomatic Infectiousness (Low)*, *Innate Genetic Resistance*, *No Immune Boosting by Asymptomatic Infection* — so the robustness argument is visible in the table of contents.

## Opening move
> "Noroviruses (NoVs) are the most common cause of acute gastroenteritis (AGE) in industrialized countries."

then US burden as a ladder from cases to deaths, then the source of the accepted estimate and its weakness — the challenge doses "several thousand–fold greater than the small amount of virus capable of causing human illness".

**The decisive move is a back-of-envelope calculation showing the accepted value cannot be right**:
> "The point prevalence of immunity in the population (i.e., population immunity) can be approximated by the incidence of infection (or exposure) multiplied by the duration of immunity. If duration of immunity is truly <1 year and incidence is 5%, <5% of the population should have acquired immunity at any given time. However, challenge studies show population immunity levels on the order of 30%–45%, suggesting that our understanding of the duration of immunity is incomplete."

**Before building a model, show with arithmetic that the existing estimate contradicts other data.** Prevalence equals incidence times duration; three numbers, one inconsistency, and the reader is persuaded the paper is needed before any equation appears. The rival explanation — genetic resistance — is raised and set aside in the next sentence.

## Methods
- **Say what the model can and cannot estimate before fitting it**: "This approach does not consider multiple strains or the emergence of new variants, so we are effectively estimating minimum duration of immunity in the absence of major strain changes." The estimand is labelled a lower bound from the start.
- **Define immunity precisely, as the model represents it**: the recovered class "represents a type of immunity in which persons are subject to infection but not disease—they can become asymptomatically infected and shed virus in stool specimens, but symptoms of AGE do not develop."
- **Fit to two kinds of data at once**: age-specific incidence from a community cohort, and the proportion of adults immune, estimated from the challenge studies the paper reviews in a table.
- **Build one model per unverifiable assumption**: infectiousness of presymptomatic and asymptomatic people (none, low, high), a genetically resistant fifth of the population, strain-specific immunity, no immune boosting — "to represent the variety of possible infection processes to gain a more robust estimate of the duration of immunity."
- **Derive intervals by likelihood profile**, holding each parameter fixed at a series of values and refitting.
- **Test a complication and drop it when it does not change the answer**: seasonal forcing "did not qualitatively change our estimate of the duration of immunity, we excluded it in favor of a more parsimonious model."

## Results
**The range across models is the headline**: duration of immunity was "estimated at 4.1 (95% CI 3.2–5.1) to 8.7 (95% CI 6.8–11.3) years" in the abstract, and in the Discussion, "we estimate a mean duration of immunity ranging from ≈4 to 8 years."

**Choose the reported model on fit, and say how weak the choice is**: "Although model B was not a significantly better fit than A, D, or F, it did have the smallest negative log-likelihood, so we used model B for subsequent results, unless stated otherwise."

**Explain why the models do not diverge more**: "the transmission parameters… fell into 3 relative patterns… These differences in transmissibility partly explain why the duration of immunity estimates are not more divergent between models." **When structurally different models agree, say what compensates.**

**Report the secondary finding that matters for policy**: children under five were far more infectious, and R₀ within that age group far above one while below one for older people.

## Literature
Numbered EID citations. The challenge studies behind the old estimate are tabulated (Table 1) by study, strain, secretor status and outcome, so the reader can see the evidence base the paper is arguing against.

## Voice
First-person plural, past tense. The paper is direct about the size of its claim — "Our findings represent a substantial departure from current estimates of the duration of immunity to NoV" — and equally direct about its simplifications.

## Discussion and limitations
**Say in which direction the main simplification biases the estimate**:
> "If a person repeatedly became asymptomatically infected (moves from R to A class), that person would effectively be immune to disease for longer than a person without successive asymptomatic/subclinical infections. The duration of immunity estimates are therefore conservative with respect to total time a person is protected from disease."

**Show the conclusion survives the limitation most likely to break it**: new GII.4 variants escape immunity every few years, so a single-strain model may be compromised; but "that novel GII.4s emerge once every 4 years or so would still suggest a role for the duration of immunity on the scale of years."

**Explain why the old estimate was wrong, not only that it was**: "this analysis suggests that the large dose or type (GI.1) delivered to volunteers in the classic challenge studies was unrepresentative of natural exposure to common contemporary strains."

**Draw the vaccine implication, including where it conflicts with current practice**: vaccinating young children "is likely to result in both the greatest direct and indirect benefits. This conclusion is at odds with the current direction of vaccine development, which is increasingly focused on demonstrating safety and efficacy in older age groups."

**End with the study that would test the result**: "future trials could consider following-up at least a subset of participants for several years either for natural disease or by challenge, providing an empirical test of these modeling results."

## What to avoid from this paper
- **Text and table disagree.** Model C's R₀ is 3.34 in Table 3 and 7.16 in the text; model B's interval is 4.0–6.7 in the table and 4.0–7.6 in the text, and model C's lower bound differs too. Generate the numbers in the text from the same output as the table.

## Distinctive moves to borrow
1. **Show with arithmetic that the accepted estimate contradicts other data** — prevalence ≈ incidence × duration — before building a model.
2. **Set aside the rival explanation in a sentence**, with the reason.
3. **Label the estimand a bound** from the start when the model omits a mechanism that would lengthen it.
4. **Define the immune state as the model represents it.**
5. **Fit to two independent data types at once.**
6. **Build one model per unverifiable assumption**, and name each subsection for it.
7. **Choose the reported model on fit and say how weak the choice is.**
8. **Explain why structurally different models agree.**
9. **Give the direction of the main simplification's bias** — here, conservative.
10. **Explain why the old estimate was wrong**, not just that it was.
11. **Name the trial design that would test the result.**

## Related files
For reduced vaccine efficacy explained by the natural history of an enteric infection, by a group including the same senior author, see [74-lopman-2012-rotavirus-vaccine-efficacy](74-lopman-2012-rotavirus-vaccine-efficacy.md); for incubation and generation intervals estimated from routine data see [07-lauer-2020-incubation-period](07-lauer-2020-incubation-period.md) and [54-ganyani-2020-generation-interval](54-ganyani-2020-generation-interval.md). Other *parameter estimation* exemplars: see [55-stopard-2021-malaria-eip](55-stopard-2021-malaria-eip.md) for a parameter estimated mechanistically, by modelling every scale that generates the data.
