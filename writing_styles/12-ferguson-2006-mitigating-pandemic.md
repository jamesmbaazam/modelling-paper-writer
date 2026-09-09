# 12 — Ferguson et al. (2006), *Nature*
**"Strategies for mitigating an influenza pandemic"**
*Nature* 442:448–452. doi:10.1038/nature04795. PMC7095311.

**Archetype:** the *large individual-based policy simulation* in a general-science journal — a huge model, almost no equations, everything organised around intervention options.

## Structure
No numbered sections. Abstract (~250 words) then a continuous **Main** text (~4500 words) segmented by *topic of intervention*, in the order a decision-maker would consider them:
model parameterisation and baseline dynamics → border and travel restrictions → case-targeted interventions (antivirals, isolation) → household policies → school closure → vaccination → combination policies.

Methods are dissolved into the narrative; the parameter tables, sensitivity analyses, mathematical justification and spatial-spread videos all live in the Supplementary Information. "(see Supplementary Information)" appears roughly fifteen times and functions as a load-bearing structural device.

## Opening move
> "Development of strategies for mitigating the severity of a new influenza pandemic is now a top global public health priority. Influenza prevention and containment strategies can be considered under the broad categories of antiviral, vaccine and non-pharmaceutical (case isolation, household quarantine, school or workplace closure, restrictions on travel) measures. Mathematical models are powerful tools for exploring this complex landscape of intervention strategies and quantifying the potential costs and benefits of different options."

Pattern: **urgency → an exhaustive taxonomy of the option space → modelling as the only way to search that space.** Sentence two silently sets the paper's outline.

## Methodology conventions
- **Parameters in prose, with the sensitivity pointer inline**: "We assume that 50% (see Supplementary Information for sensitivity analysis) of those infected are ill enough to be classified as clinical cases."
- Key quantities are given as ranges tied to historical data: "We estimated the reproduction number, R₀, to have a value of 1.7–2.0 for the first wave of the 1918 pandemic."
- Structural assumptions given as empirical claims with a source: "For the United States, best estimates are that 30% of transmission occurs within the household, and 70% outside the household."
- **Every result is presented twice, once per transmissibility scenario** (moderate R₀ = 1.7, high R₀ = 2.0), so the reader can locate their own risk tolerance rather than being handed a single number.
- R₀ is used as a notation but always re-explained contextually; no other symbols appear in the main text.

## Results storytelling
Percentages and percentage-point reductions; ranges rather than CIs (the uncertainty is scenario uncertainty, not sampling uncertainty).
> "School closure during the peak of a pandemic can reduce peak attack rates by up to 40%, but has little impact on overall attack rates, whereas case isolation or household quarantine could have a significant impact, if feasible."
> "For the high transmissibility scenario, same-day treatment of 90% of cases reduces cumulative attack rates from 34% to 29% and peak daily attack rates from 1.9% to 1.6%…"
> "Household quarantine is also effective at reducing attack rates in the community (indeed, for low R₀ values, pandemic spread can be dramatically slowed), but only if compliance is high."
> "The epidemic peaks some 50–65 days after the first case."

Signature sentence shape: **intervention → the metric it moves → the metric it does *not* move → the condition on which it depends.** The "but only if…" clause is present in nearly every claim, and it is what makes the paper credible to policymakers.

## Literature integration
~24 references — sparse, roughly one per 350 words. Prior modelling is cited as foundation rather than rival:
> "Mathematical models are powerful tools for exploring this complex landscape of intervention strategies and quantifying the potential costs and benefits of different options[2–5]."
The paper claims contribution by *setting* (GB and US at national scale) and by *breadth of intervention comparison*, not by methodological novelty.

## Voice
Present tense for model assumptions ("We assume…"), past for simulated outcomes. Consistently active and first-person plural: "We parameterize an individual-based simulation model", "We examine intervention options", "We find that…". Hedging is quantitative and conditional rather than vague: "unlikely to delay spread by more than 2–3 weeks unless more than 99% effective".

## Limitations
> "Lack of data prevent us from reliably modelling transmission in the important contexts of residential institutions (for example, care homes, prisons) and health care settings…"
> "Although more detailed model validation and parameter estimation using data from past pandemics should be a priority for future research, it will be impossible to predict the exact characteristics of any future pandemic virus."

Two distinct kinds of limitation, cleanly separated: **missing data** (fixable) and **irreducible uncertainty about the future** (not fixable, and therefore an argument for the paper's scenario approach).

## Policy framing
Policy sits inside the results, not in a separate section, and is always conditioned on feasibility and ethics:
> "Given the expected increases in contact rates within the household which would result, a household quarantine policy might pose ethical dilemmas unless excellent infection control was implemented."
> "More widespread prophylaxis would be even more logistically challenging but might reduce attack rates by over 75%."

The paper closes on a call for data collection rather than on a recommendation:
> "It will be imperative to collect the most detailed data on the clinical and epidemiological characteristics of a new virus and the impact of control measures early in the emergence of a pandemic, and to analyse those data in real time to allow interventions to be tuned to match the virus the world faces."

## Distinctive moves to borrow
1. **"No magic bullet" framing**: "There is no single magic bullet which can control the outbreak, but … a combination of approaches could reduce transmission and save many lives."
2. Present all results under two labelled transmissibility scenarios throughout.
3. Attach a logistics or ethics checkpoint to every intervention you endorse.
4. Push all machinery to the SI and use the pointer as punctuation, so the main text reads as an argument about policy rather than about code.
