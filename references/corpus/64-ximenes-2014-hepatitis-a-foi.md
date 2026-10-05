# 64 — Ximenes et al. (2014), *PLoS ONE*
**"Modelling the force of infection for hepatitis A in an urban population-based survey: a comparison of transmission patterns in Brazilian macro-regions"**
Ximenes RAA, Martelli CMT, Amaku M, Sartori AMC, de Soárez PC, Novaes HMD, et al. *PLoS ONE* 9(5):e94622. doi:10.1371/journal.pone.0094622.

**Archetype:** *serological inference* with **the mixing assumption as the object of study** — three catalytic models with different contact structures are fitted to the same serosurvey and compared, rather than one model being fitted and reported. The methodological counterpart to Prayitno 2017's single constant-force model.

## Structure
PLoS structured abstract (**Background / Methods / Results / Conclusion**) → `Introduction` → `Methods` → `Results` → `Discussion`. The paper's distinguishing feature is in the Methods: it builds a ladder of models rather than one.

## Opening move
> "This study aimed to identify the transmission pattern of hepatitis A (HA) infection based on a primary dataset from the Brazilian National Hepatitis Survey in a pre-vaccination context. The national survey conducted in urban areas disclosed two epidemiological scenarios with low and intermediate HA endemicity."

**The pre-vaccination framing is the point.** A serosurvey taken before a vaccine is introduced is a baseline that can never be collected again, and the paper's value — stated in its own conclusion — is as a reference point for evaluating the programme that followed: "These estimates of HA force of infection stratified by age and endemicity levels are useful information to characterize the pre-vaccination scenario in Brazil."

**Two endemicity settings within one country** is the comparison that makes the analysis informative, and the regions are named explicitly: intermediate is "North, Northeast, Midwest and Federal District", low is "South and Southeast".

## Methods
- **Build a ladder of models, each adding one mechanism**, and say what each adds:
  > "We built up three models: fully homogeneous mixing model, with constant contact pattern; the highly assortative model and the highly assortative model with the additional component accounting for contacts with infected food/water."

  Homogeneous mixing → age-assortative mixing → assortative mixing plus an environmental transmission route. **Each step adds one named mechanism, so the contribution of each can be seen.** This is the structure `SKILL.md` §2 recommends for methods papers (`evidence.md` §2.1) — build complexity in visible steps, one per subsection — applied to a serological model.
- **Include an environmental route explicitly** for a faecal–orally transmitted pathogen, rather than folding it into the contact term. For hepatitis A, person-to-person and food- or water-borne transmission are different mechanisms with different control implications, and the third model separates them.
- **State the sample, its age span and its geographic coverage**: "The seroprevalence data from 7,062 individuals aged 5–69 years from all the Brazilian macro-regions were included."
- **Report the uncertainty method as well as the model**: "a SIR epidemic model together with a Monte Carlo method to estimate confidence intervals for the age-dependent curves."
- **Use 99% confidence intervals and say so**, rather than defaulting to 95%: "Curves of prevalence, force of infection (FOI) and the number of new infections with 99% confidence intervals (CIs) were compared."
- **Explain why the age range was extended mid-study**, which is unusually candid about how the analysis developed:
  > "In our preliminary modelling approach, the fitted curves of prevalence using a dataset comprising individuals aged 5–19 years from this national survey still presented an ascending trend of infection in the second decade of life. Therefore, we extended the detection of specific IgG serology for a subsample of the adult population to build a full mathematical model that encompassed all age strata."

  **The data did not cover the age range the model needed, so more serology was run.** Saying so makes the final design intelligible instead of arbitrary.

## Results
**Report the raw seroprevalence for both settings with intervals, before any modelled quantity**:
> "The anti-HAV IgG seroprevalence was 68.8% (95% CI, 64.8%–72.5%) and 33.7% (95% CI, 32.4%–35.1%) for the intermediate and low endemicity areas, respectively, according to the field data analysis."

The qualifier "according to the field data analysis" marks this as the observed quantity rather than the model output — a useful distinction when a paper reports both.

**Give the force of infection in explicit units, with the age band it peaks in, for each setting:**
> "a higher force of infection was identified in the 10- to 19-year-old age cohort (∼9,000 infected individuals per year per 100,000 susceptible persons) in the intermediate endemicity area, whereas a higher force of infection occurred in the 15- to 29-year-old age cohort (∼6,000 infected individuals per year per 100,000 susceptible persons) for the other macro-regions."

**"Infected individuals per year per 100,000 susceptible persons" is the force of infection written out in full.** The denominator is *susceptibles*, not population — the distinction that separates a force of infection from an incidence rate, and stating it prevents the commonest misreading.

**Report the quantity that matters for policy — who is still susceptible**: "At least half of the population aged 10- to 14-years-old and older was still susceptible to HA infection in the intermediate and low endemicity areas."

**Describe the shape of the epidemiological shift rather than only its direction**: "In the more socioeconomically developed macroregion (South and Southeast), considered low HAV endemicity, the age of virus exposure occurred later compared to the intermediate endemicity areas"; and the peak observed prevalence "was highest at 30–39 years… [whereas] the highest observed prevalence was achieved two decades later (50–59 years) in the low endemicity setting."

**Two decades of difference in peak age, within one country** — the kind of comparison that only a multi-region survey supports, and the basis for the conclusion that the risk is shifting to older ages where disease is more severe.

## Literature
Numbered PLoS citations. Prior Brazilian surveys are cited for comparison with the new prevalence estimates, and international examples are brought in for the methodological argument about evaluating vaccination (below).

## Voice
First-person plural, past tense, and careful to distinguish observed from modelled quantities throughout ("according to the field data analysis", "The model herein predicted", "the observed prevalence").

## Discussion and limitations
Opens by naming the method and what it enabled, rather than restating results: "The mathematical modelling approach used in this work… allowed for the comparison of the rates of HA infection by age according to the two endemicity levels in Brazil."

**The limitation is stated, then bounded with the figure that bounds it:**
> "limitation of the analysis is using the serosurvey data from an urban population that did not include rural and institutionalised populations. Nevertheless, these models used seroprevalence data from a representative sample of the Brazilian urban population, **which accounts for 84% of the total population of the country**."

**Quantify the population your sampling frame covers** rather than leaving the exclusion unbounded.

**The most valuable passage is a methodological argument about how the next study should be designed** — the paper reasons forward from its own role as a baseline:
> "Assuming the potential upcoming addition of the HA vaccine to the routine immunisation schedule in Brazil, there is a need to discuss the best methodological approach for evaluating the impact of this intervention at the population level. In general, a decrease in the incidence of disease, as reported by surveillance systems, is used to evaluate the protective effect of vaccination… However, the usefulness of this design depends on the quality of the HA surveillance system. In Brazil, HA cases are generally underreported, and not all cases are laboratory confirmed or investigated."

Then **two specific obstacles that would defeat the conventional evaluation design**, the second of which is a genuine measurement trap:
> "First, asymptomatic infections may go undetected if case notification is the outcome measure. **Second, the serological marker of infection is the same as the HA vaccine.**"

If vaccination and infection produce the same antibody, post-vaccination serosurveys cannot distinguish them — so the obvious evaluation method fails. **Then the alternative design is proposed and justified**: "One alternative would be to design repeated serosurveys of unvaccinated people to determine the age distribution pattern of HA infection… Therefore, the force of infection could be obtained by modelling the prevalence data."

**Argue forward from your own study to the design of the evaluation that should follow**, naming the measurement traps that would invalidate the conventional approach.

## Distinctive moves to borrow
1. **Fit a ladder of models that differ in one mechanism each** — homogeneous, assortative, assortative plus environmental — rather than one model.
2. **Separate the environmental transmission route** for a pathogen that has one, instead of folding it into contact.
3. **Frame a pre-vaccination serosurvey as an irreplaceable baseline**, and say what it is a baseline for.
4. **Compare two endemicity settings within one country**, naming the regions in each.
5. **Write the force of infection in full units** — infections per year per 100,000 *susceptibles* — so the denominator is unambiguous.
6. **Distinguish observed from modelled quantities** with an explicit tag on each.
7. **Report the proportion still susceptible by age**, which is what a vaccination programme needs.
8. **Describe the shift in peak age of infection**, not just the direction of change.
9. **Explain why the study design changed mid-analysis** when the preliminary fit showed the age range was too narrow.
10. **Quantify the population your sampling frame represents** when bounding a coverage limitation.
11. **Name the measurement traps that would defeat the obvious evaluation design**, especially where a vaccine and an infection share a serological marker, and propose the design that avoids them.
12. **Use 99% intervals and say so**, where the application warrants more conservative bounds.

## Related files
For the single-model serological exemplar see [40-prayitno-2017-dengue-seroprevalence](40-prayitno-2017-dengue-seroprevalence.md); for age-seroprevalence used to monitor an elimination programme see [65-golden-2016-onchocerciasis-seroprevalence](65-golden-2016-onchocerciasis-seroprevalence.md); for immunity acquisition estimated from age-stratified clinical data see [46-griffin-2015-malaria-immunity](46-griffin-2015-malaria-immunity.md); for the vaccination-impact evaluation this paper's baseline would serve see [61-abbas-2020-hpv-input-revisions](61-abbas-2020-hpv-input-revisions.md) and [49-verguet-2015-measles-sia](49-verguet-2015-measles-sia.md). Other *serological inference* exemplars: see [77-hay-2024-influenza-infection-histories](77-hay-2024-influenza-infection-histories.md) for lifetime infection histories reconstructed from multi-strain serology, with the estimand renamed seroincidence.
