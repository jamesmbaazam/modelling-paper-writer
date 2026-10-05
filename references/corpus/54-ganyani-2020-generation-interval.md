# 54 — Ganyani et al. (2020), *Eurosurveillance*
**"Estimating the generation interval for coronavirus disease (COVID-19) based on symptom onset data, March 2020"**
Ganyani T, Kremer C, Chen D, Torneri A, Faes C, Wallinga J, Hens N. *Euro Surveill* 25(17):2000257. doi:10.2807/1560-7917.ES.2020.25.17.2000257.

**Archetype:** *parameter estimation* of a quantity that **cannot be observed at all** — the generation interval runs between two infection events, neither of which is seen — recovered from symptom-onset data by modelling the unobserved layer explicitly. The corpus's **Eurosurveillance** exemplar and its example of the rapid-communication format.

## Structure
*Eurosurveillance* structured abstract with an **`Aim`** field between Background and Methods — **Background / Aim / Methods / Results / Conclusion** → `Keywords` → `Introduction` → `Methods` → `Results` → `Discussion`. Short: roughly 3,000 words of main text.

**The `Aim` field is worth writing even where a journal does not ask for it.** Ganyani's is two sentences and does something a Background cannot: it lists the quantities to be estimated *and* flags the methodological warning the paper will deliver — "We estimate the generation interval, serial interval, proportion of pre-symptomatic transmission and effective reproduction number of COVID-19. **We illustrate that reproduction numbers calculated based on serial interval estimates can be biased.**"

**A rapid communication earns its length by not repeating itself.** There is no literature review beyond what licenses the parameters, no figure that restates a table, and the Discussion opens directly on the numbers.

## Opening move
> "The 2019 coronavirus disease (COVID-19) outbreak that started in Wuhan, China in December 2019 has now been declared a pandemic. As at 22 April 2020, 2,573,143 cases of COVID-19 have been confirmed in 185 countries and territories around the world."

Dated to the day, which a rapid communication must be. Then the justification for estimating parameters at all is stated operationally: "public health officials depend on insights about key disease transmission parameters that are typically obtained from mathematical or statistical modelling."

**Every parameter is defined parenthetically at first use, in one pass** — the cleanest glossary paragraph in the corpus:
> "Examples of key parameters include the reproduction number (R) (average number of infections caused by an infectious individual), and distributions of the generation interval (time between infection events in an infector-infectee pair), serial interval (time between symptom onsets in an infector-infectee pair) and incubation period (time between moment of infection and symptom onset)."

Three intervals that are routinely confused, distinguished in a single sentence by *which two events each runs between*. **When your paper turns on the distinction between near-synonyms, define them together and by their endpoints**, not separately across the Introduction.

**Then say what each is good for**, so the reader knows why the distinction matters: "Estimates of the reproduction number together with the generation interval distribution can provide insight into the speed with which a disease will spread. On the other hand, estimates of the incubation period distribution can help guide determining appropriate quarantine periods."

## Methods
- **Name the two unobserved things you are estimating around.** The whole method is one sentence:
  > "We used outbreak data from clusters in Singapore and Tianjin, China to estimate the generation interval from symptom onset data while acknowledging uncertainty about the incubation period distribution and the underlying transmission network."

  Two layers of latency — who infected whom, and when each was infected — are both carried as uncertainty rather than fixed. **State which unobservables are integrated over**; that is the methodological claim.
- **Derive the secondary quantities from the primary estimate** rather than estimating each separately: "From those estimates, we obtained the serial interval, proportions of pre-symptomatic transmission and reproduction numbers." One coherent posterior produces all four, so they cannot contradict each other.
- **Use two independent outbreak datasets** from different countries and containment regimes, which turns a single estimate into a comparison.
- **Cite the data source with its URL and access date** in the table footnote: "Source: Tianjin Municipal Health Commission (http://www.tjbd.gov.cn/zjbd/gsgg/, as at 27 February)."

## Results
**Report both datasets side by side, every time, with intervals**:
> "The mean generation interval was 5.20 days (95% credible interval (CrI): 3.78–6.78) for Singapore and 3.95 days (95% CrI: 3.01–4.91) for Tianjin. The proportion of pre-symptomatic transmission was 48% (95% CrI: 32–67) for Singapore and 62% (95% CrI: 50–76) for Tianjin."

Two settings reported in parallel let the reader see which conclusions survive the difference between them — and the paper never collapses them into a pooled number.

**Report the standard deviation of the interval, not only its mean**: "a mean of 5.20 days (95% CrI: 3.78–6.78) and a SD of 1.72 days (95% CrI: 0.91–3.93)". A generation-interval *distribution* is what downstream R estimation consumes, and a mean alone is not usable — the point `SKILL.md` §2 makes about giving both moments (`evidence.md` §2.3).

**Rank the assumptions by how much they matter**, which is the most useful possible summary of a sensitivity analysis:
> "The sensitivity analyses showed that the assumptions made about the incubation period have only moderate impact on the results. On the other hand, assumptions made about the underlying transmission network (e.g. acknowledging possibly negative serial intervals) had a large impact on our results."

**Give the magnitude of the sensitive assumption's effect**, with both endpoints: allowing negative serial intervals "decreased the estimated mean generation time from 5.20 days… to 3.86 days (95% CrI: 2.22–5.60)", and for Tianjin "the mean generation time decreased to 2.90 days (95% CrI: 1.85–4.12)". The corresponding pre-symptomatic proportions move from 48% to 66% and 62% to 77%.

**Offer competing explanations for a between-setting difference without choosing**: the lower Tianjin estimate may be because "there were already some negative serial intervals among the reported links in the Tianjin data, which may explain this lower estimate. The difference in these estimates could also be the result of differences in containment strategies."

**State the data requirement the analysis implies** — a finding about what future studies need, not about this one: "Sensitivity analyses showed that estimating these quantities from outbreak data requires detailed contact tracing information", elaborated as "when the data do not provide sufficient information on directionality of transmission, this lack of auxiliary information may cause problems for estimation."

## Literature
Numbered Eurosurveillance citations, sparse and purposeful. Prior estimates are cited to position the new ones; the one substantive engagement is with a paper whose conclusion this one reinforces: "As has been shown by other studies, e.g Hellwell et al., it is unlikely that these measures alone will suffice t[o control transmission]". **A rapid communication cites what it needs and stops.**

## Voice
First-person plural, past tense, flat and declarative. Hedges are attached to specific inferences ("may explain this lower estimate", "could also be the result of"), and the one strong claim is derived rather than asserted — see the Conclusion below.

## Discussion and limitations
Opens by restating the estimates with both moments and both datasets, then the sensitivity ranking, then four numbered limitations, each naming a direction or a consequence:

1. **A borrowed input, with the sensitivity analysis that bounds it**: "we rely on previous estimates for the incubation period. However, our sensitivity analyses showed that changing the incubation period distribution does not have a big impact on our estimates."
2. **A bias whose mechanism is spelled out**: "we do not account for incomplete or possible changes in reporting… Incomplete reporting means that cases are missing, with this leading to incomplete transmission networks. As the underlying transmission network has a large impact on our estimates, incomplete reporting may bias our estimates." The limitation is tied back to the assumption already shown to be the sensitive one.
3. **An omitted dynamic process**: "we do not acknowledge changes in contact patterns and thus behavioural change, which could shape realised generation interval distributions as well as serial interval distributions."
4. **A known theoretical effect, named**: "we do not account for contraction of the generation interval because of depletion of susceptibles."

**The conclusion is a control-policy inference derived from the parameter, with a comparison to two related pathogens:**
> "Our estimates of this proportion are high, ranging from 48% to 77%. This implies that the effectiveness of case finding and contact tracing in preventing COVID-19 infections will be considerably smaller compared with the effectiveness in preventing severe acute respiratory syndrome coronavirus (SARS-CoV) or Middle East respiratory syndrome coronavirus (MERS-CoV) infections, where pre-symptomatic transmission did not play an important role."

**Then the conclusion is qualified by the circumstances of the data collection** — a caveat that cuts against the paper's own headline, placed in the abstract rather than buried:
> "Notably, quarantine and other containment measures were already in place at the time of data collection, which may inflate the proportion of infections from pre-symptomatic individuals."

If contacts were already being isolated after symptom onset, the pre-symptomatic share is mechanically inflated. **Putting the inflating mechanism in the abstract, next to the number it inflates, is the single most honest move available to a rapid communication.**

## Distinctive moves to borrow
1. **Use the `Aim` field to state both what you estimate and the warning you will deliver.**
2. **Define near-synonymous intervals together, by the two events each runs between**, then say what each is used for.
3. **Name the unobservables you integrate over** — here the transmission network and the infection times — rather than fixing them silently.
4. **Derive secondary quantities from one posterior** so they stay mutually consistent.
5. **Report two settings in parallel and never pool them**, so the reader sees which conclusions survive.
6. **Give both moments of a distribution**, with intervals, because downstream users need the distribution.
7. **Rank your assumptions by how much they move the answer**, and give the magnitude for the sensitive one with both endpoints.
8. **Turn a sensitivity result into a data-collection requirement** for future studies.
9. **Offer competing explanations for a between-setting difference without adjudicating.**
10. **Tie each limitation back to the assumption already shown to matter most.**
11. **Derive the policy inference from the parameter**, and anchor it against related pathogens where the parameter differs.
12. **Put the mechanism that inflates your headline number in the abstract**, beside the number.

## Related files
For the other parameter-estimation exemplar, estimating an observable interval from reported cases, see [07-lauer-2020-incubation-period](07-lauer-2020-incubation-period.md); for the downstream consequence of getting the generation interval wrong see [27-gostic-2020-practical-considerations-rt](27-gostic-2020-practical-considerations-rt.md) and [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md); for the delay-distribution biases this paper navigates see [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md); for the contact-tracing feasibility conclusion it reinforces see [22-hellewell-2020-contact-tracing-feasibility](22-hellewell-2020-contact-tracing-feasibility.md). Other *parameter estimation* exemplars: see [55-stopard-2021-malaria-eip](55-stopard-2021-malaria-eip.md) for a parameter estimated mechanistically, by modelling every scale that generates the data.
