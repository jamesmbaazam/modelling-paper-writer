# 81 — Kucharski et al. (2016), *Emerging Infectious Diseases*
**"Effectiveness of ring vaccination as control strategy for Ebola virus disease"**
Kucharski AJ, Eggo RM, Watson CH, Camacho A, Funk S, Edmunds WJ. *Emerg Infect Dis* 22(1):105–108. doi:10.3201/eid2201.151410.

**Archetype:** *feasibility / threshold* in the shortest format the corpus holds — an EID **Dispatch** of about 1,200 words. A branching-process model, parameterised from Guinean transmission chains, asks whether ring vaccination could have contained the West African Ebola epidemic, and answers with a threshold: it depends on the proportion of cases missed by contact tracing. The model is in the technical appendix; the article is the argument.

## Structure
EID Dispatch: a two-sentence abstract (EID allows 50 words) → unheaded introduction → **`The Study`** → **`Conclusions`** → technical appendix → biographical sketch. There is no Methods or Discussion heading: the Dispatch format folds methods, results and limitations into *The Study*.

**Every paragraph does one job**: model structure; ring vaccination as simulated; the result; mass vaccination as a comparator; a second, partial-control scenario; doses; limitations. In a format this short, the paragraph is the unit of structure.

## Opening move
The abstract is the whole finding, with its condition:
> "Using an Ebola virus disease transmission model, we found that addition of ring vaccination at the outset of the West Africa epidemic might not have led to containment of this disease. However, in later stages of the epidemic or in outbreaks with less intense transmission or more effective control, this strategy could help eliminate the disease."

**The gap is a question the trial could not answer**: the ring-vaccination trial suggested high efficacy, but "it remains unclear whether prompt ring vaccination, as opposed to large-scale mass vaccination, could have contained the EVD epidemic in West Africa, and under what circumstances it could be effective in controlling future outbreaks." An efficacious vaccine is not the same as an effective strategy.

## Methods
- **Build the model's key structure from an observed pattern**: transmission chains showed that index cases, "defined as those that could not be linked to an already known transmission chain, had a reproduction number of R m = 7", against 0.66 for cases within known chains. The model has two kinds of case because the data do.
- **Make the threshold parameter the thing contact tracing controls**: a probability ρ that a secondary case is missed and seeds a new cluster. The result is then expressed in terms a response team can act on.
- **Check the model reproduces the epidemic before using it**: when half of cases were missed, the overall reproduction number "was ≈1.5, which was similar to values observed in early 2014 in West Africa".
- **State every intervention parameter and the arithmetic it implies**: vaccine efficacy 80%, coverage of the ring 70%, so "The reproduction number within a ring was therefore reduced by a factor of 1 – (0.8 × 0.7) = 0.44 once the vaccine became effective".
- **Define the outcome as a probability of failure**: the proportion of simulated outbreaks that became large (more than 500 clusters).

## Results
**The threshold result, with its mechanism in the next sentence**:
> "We found that if more than a few cases were missed, large outbreaks could occur under ring vaccination. This event could occur because missed cases, which had a higher reproduction number, would not be inside the ring when vaccination was introduced."

**Say what the failing strategy still achieved**: "Although ring vaccination failed to contain the outbreak in this scenario, it still reduced disease transmission". **A strategy that fails to contain can still reduce; report both.**

**Compare against the alternative strategy on the same terms**: mass vaccination, reducing transmission by the same factor for every case whether in a ring or missed, "was more effective in containing outbreaks, even if many cases were missed."

**Run a second, better-controlled scenario from the data**: excluding funeral and hospital transmission from the Guinean chains gives R_m = 2.5, and "In this partial control scenario, outbreaks could be controlled with ring vaccination, even if 40% of cases were missed." The same strategy fails early in the epidemic and works later; the threshold moves with the setting.

**Say what could not be estimated, and why**: doses for mass vaccination could not be estimated, "and thus could not perform an economic analysis of different strategies, because this would depend on the potential for long-distance transmission events and populations in different areas."

## Literature
Fourteen numbered citations, one under the Dispatch limit of 15: the trial, the smallpox precedent, a prior population-level modelling study, the transmission-chain data, and the sources of the delay distributions. Every citation is load-bearing.

## Voice
First-person plural. The modal verbs carry the argument — "might not have led to containment", "could help eliminate", "could occur" — and they are consistent between abstract, body and conclusions.

## Discussion and limitations
The limitations paragraph does three things in seven sentences. It names the assumption most likely to be wrong and the direction behavioural change would push it — "if an effective vaccine became available, persons at risk might be more likely to engage with public health efforts" — names an ascertainment bias that may have inflated the key parameter — "cases that generate many secondary infections are more likely to be designated as index cases" — and then characterises the result as a whole:

> "Our estimates are therefore likely to represent a reasonable worst-case scenario."

**Characterise the overall direction of your assumptions in one phrase**, after listing them, so the reader knows how to use the number.

**The conclusion restates the condition, not just the finding**: "if standard measures are not working because many cases are not in known transmission chains, as in West Africa in early 2014, ring vaccination might be insufficient to contain the outbreak", and turns it into planning advice — "mass vaccination, or hybrid strategies involving mass and ring vaccinations, might need to be considered alongside ring vaccination".

## Distinctive moves to borrow
1. **Use the short format's paragraphs as structure**, one job each.
2. **Put the whole finding and its condition in a two-sentence abstract.**
3. **Distinguish an efficacious vaccine from an effective strategy** in the gap statement.
4. **Build the model's structure from an observed pattern** — two kinds of case because the chains show two.
5. **Make the threshold parameter one a response team controls.**
6. **Check the model reproduces the epidemic** before using it.
7. **Show the arithmetic of the intervention effect.**
8. **Give the mechanism of failure** in the sentence after the result.
9. **Report what a failing strategy still achieved.**
10. **Show the threshold moving with the setting** — early versus partial control.
11. **Say what could not be estimated and why.**
12. **Characterise your assumptions as a whole** — here, a reasonable worst case.

## Related files
For a capacity forecast from the same group during the same epidemic see [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md); for the real-time forecasts this group issued and later scored see [50-funk-2019-real-time-forecast-assessment](50-funk-2019-real-time-forecast-assessment.md); for identifiability of Ebola transmission routes see [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md). Other *feasibility / threshold* exemplars: see [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md) for a feasibility threshold and an operational checklist from a very large individual-based simulation; [76-famulare-2018-polio-opv-cessation](76-famulare-2018-polio-opv-cessation.md) for a threshold statistic that sorts settings into three categories of outbreak risk, each checked against history; [22-hellewell-2020-contact-tracing-feasibility](22-hellewell-2020-contact-tracing-feasibility.md) for a branching-process boundary on when contact tracing can control an outbreak, with no fitted data; [79-golumbeanu-2022-malaria-tpp-emulator](79-golumbeanu-2022-malaria-tpp-emulator.md) for minimum coverage, efficacy and duration a new intervention must reach, found by searching an emulator of a simulation model.
