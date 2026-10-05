# 67 — Clapham et al. (2014), *Journal of the Royal Society Interface*
**"Within-host viral dynamics of dengue serotype 1 infection"**
Clapham HE, Tricou V, Van Vinh Chau N, Simmons CP, Ferguson NM. *J R Soc Interface* 11(96):20140094. doi:10.1098/rsif.2014.0094.

**Archetype:** *within-host dynamics* used to test a **mechanistic hypothesis about disease severity** — antibody-dependent enhancement — by asking which model parameters differ between primary and secondary infections. The model is a hypothesis-testing instrument, and its second use is to show that a proposed therapy would arrive too late.

## Structure
Royal Society format: `Abstract` → `Keywords` → numbered sections `1. Introduction` → `2.` model and data → `3.` results → `4. Discussion`. Compact, with the biological background carrying real weight because the hypothesis under test is immunological.

## Opening move
> "Dengue, the most common mosquito-borne viral infection of humans, is endemic across much of the world, including much of tropical Asia and is increasing in its geographical range."

The Introduction gives burden with both infections and illnesses — "approximately 400 million infections per year resulting in approximately 100 million apparent illnesses" — then the clinical spectrum, then builds to the puzzle:
> "Primary infection with one of the four dengue serotypes (DENV 1–4) is thought to lead to lifelong immunity to that serotype, but in addition to generate a temporary period of cross-protective immunity to all serotypes. However, **subsequent infection with a heterologous serotype is more likely to result in severe disease than primary infection.**"

**Then the candidate mechanism is explained in full, as a biological process, before it is modelled:**
> "The mechanism for this is not fully understood, but a leading hypothesis is antibody-dependent enhancement (ADE), whereby antibodies generated in the primary infection are not sufficient to neutralize the virus, but still attach to the virus particles and, as neutralized virus would be, are taken up by cells such as macrophages. Unlike virus bound to neutralizing antibody, virus bound to non-neutralizing antibody is capable of infecting macrophages, amplifying the viral replication process."

**Explain the hypothesis mechanistically enough that a reader can predict which model parameter it should move.** ADE says antibodies help virus enter cells — so if ADE operates, the viral entry rate should be higher in secondary infections. The test is set up before the model appears.

A rival hypothesis is also named rather than ignored: "A role is also hypothesized for 'original antigenic sin', in which there is preferential activation of memory T or B cells with lower than optimal avidity."

## Methods
- **State what varies and at which level**, which is the inferential design: parameters are allowed to vary "by patient or patient group", so between-individual heterogeneity and between-group differences are separated.
- **Fit to data from both infection types in one framework**: "We fit this model to measurements of plasma viral titre from cases of primary and secondary DENV 1 infection in Vietnam." A single serotype is used so that serotype differences cannot confound the primary/secondary comparison.
- **Test the alternative model specification and report what changes and what does not** (see Discussion below), rather than presenting one structure.

## Results
**Report the heterogeneity finding as a sufficiency claim:**
> "We show that variation in model parameters governing the immune response is sufficient to create the observed variation in virus dynamics between individuals."

**"Sufficient to create the observed variation" is a precise and modest claim** — it does not assert that immune variation *is* the cause, only that it can account for what is seen without further mechanisms.

**Name exactly which parameters had to vary, and what that implies**: "We found it was necessary to vary the immune response proliferation rate (η) and the IP between people to reproduce the variation in viral kinetics seen (the majority of which is seen in timing and magnitude of peak titres). This provides evidence for a key role of the immune response proliferation in shaping virus dynamics, supporting the conclusions of earlier theoretical work."

**Connect the estimated parameter difference back to the hypothesis in the same sentence:**
> "we find parameter differences between primary and secondary cases consistent with the theory of antibody-dependent enhancement (namely enhanced rates of viral entry to target cells in secondary cases)."

The parenthesis is essential — it says *which* parameter difference counts as evidence for ADE, so the reader can judge whether the inference follows.

**Report a parameter value that is biologically surprising, and say what it implies about the system:**
> "We found relatively high target cell densities… were required for the model to reproduce observed viral dynamics while keeping viral production rates per infected cell at reasonable levels. This is in keeping with tissue reservoirs playing an important role in pathogenesis, with virus produced in such reservoirs contributing substantially to viraemia seen in plasma."

A parameter the model needs in order to fit becomes evidence about anatomy the data do not measure. **Then the inference is immediately qualified**: "We find some evidence to support the role of target cell depletion… However, **this conclusion must remain tentative until more data are available**, in particular to allow the impact of infection on target cell lifetime to be estimated."

**Use the model for a therapeutic question and report a negative answer:**
> "We conclude that the impact of antiviral therapy on virus dynamics is likely to be limited if therapy is only started at the onset of symptoms, owing to the typically late stage of viral pathogenesis reached by the time symptoms are manifested and thus treatment is started."

**The mechanism of the negative result is given, not just the result.** By the time dengue patients present, the viral trajectory has largely played out — so the finding is about the timing of clinical presentation rather than about the drug. That generalises to any antiviral in a short, self-limiting infection.

## Literature
Author–year citations in the Royal Society style. Earlier analyses of the same dataset are cited and their findings compared against the new model's ("Previous analysis of the dataset we use here found some evidence for DENV1 secondary infections being of shorter duration…"), and earlier theoretical work is credited where the new results agree with it.

## Voice
First-person plural, past tense, with hedges calibrated to the evidence: "sufficient to create", "consistent with", "some evidence to support", "must remain tentative", "likely to be limited". The paper repeatedly distinguishes what the model requires from what the biology is.

## Discussion and limitations
The limitations section is the strongest part of the paper and is organised around a single root cause — **one data type**:

> "Our analysis has a number of other limitations, principal among which is the fact we are solely analysing viral titre data. The absence of data on the target cell population or effector immune response necessarily limits model complexity with the assumptions about both necessarily needing to be kept simple."

**Name the one missing measurement that constrains everything else**, then trace its consequences:
> "One result of the simple representation of the immune response used is that the model predicts an early increase and plateau in immune response and sharp peaks in viraemia in the absence of substantial target cell depletion. This, together with the absence of data on target cell populations, means our conclusions about target cell population sizes and depletion are necessarily tentative."

**Then say what richer data would permit**, specifically: "With additional data, it may be possible to parametrize more complex models of the immune response, the different impacts of the innate and adaptive immune response and to include explicitly how immune responses are modified in secondary infection."

**The identifiability limit is reported with the discriminating consequence of each option** — the move `SKILL.md` §6 asks for (evidence in `evidence.md` §6.3):
> "In our results, we are not definitively able to distinguish between the two forms of action we considered (clearance of infected cells and of free virus). For the results presented above, we assumed that the immune response clears infected cells. We found broadly similar results (notably for the differences in parameter estimates between primary and secondary infection) for a model in which the immune response is assumed to directly clear free virus instead. **However, in this alternative model our estimates of the intrinsic virus life span are very short (a few hours), meaning any immune response targeting free virus needs to act within minute[s]…**"

Two mechanisms fit the data equally well; the paper reports that the headline result (the ADE-consistent difference) holds under both, and then uses a **biological implausibility** — an implied clearance timescale of minutes — to argue against one. **When two structures are statistically indistinguishable, check whether their parameter estimates are biologically possible.**

**The study designs that would resolve the gap are named**: "Two possible sources are household studies (where blood samples are taken from members of households in which an index case has been detected) and human challenge studies, should the latter receive ethical approval." — with the ethical caveat attached to the second.

## Distinctive moves to borrow
1. **Explain the hypothesis mechanistically enough to predict which parameter it should move**, before introducing the model.
2. **Name the rival hypothesis** even if you cannot test it.
3. **Hold the serotype constant** so the comparison of interest is not confounded.
4. **Claim sufficiency, not causation**: variation in these parameters *is sufficient to create* the observed variation.
5. **Say which parameters had to vary** to fit, and treat that as the evidence.
6. **State in parentheses which parameter difference counts as evidence for the hypothesis.**
7. **Read a biologically surprising fitted parameter as evidence about unmeasured anatomy** — then qualify it as tentative.
8. **Report a negative therapeutic result with its mechanism**, so it generalises beyond the drug.
9. **Organise limitations around the one missing measurement** and trace its consequences through the model.
10. **Report that two indistinguishable structures give the same headline result**, then discriminate between them on biological plausibility of the implied parameters.
11. **Name the study designs that would resolve the ambiguity**, with any ethical caveat attached.

## Related files
For within-host modelling joined to a clinical endpoint see [66-neant-2021-sars-cov-2-viral-kinetics](66-neant-2021-sars-cov-2-viral-kinetics.md); for the within-host exemplar built around immune mechanisms in an animal model see [41-pawelek-2012-within-host-influenza](41-pawelek-2012-within-host-influenza.md); for identifiability reported as the result see [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md); for population-level dengue burden and serology see [29-bhatt-2013-global-dengue-distribution](29-bhatt-2013-global-dengue-distribution.md) and [40-prayitno-2017-dengue-seroprevalence](40-prayitno-2017-dengue-seroprevalence.md).
