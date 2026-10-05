# 45 — Thompson et al. (2019), *Epidemics*
**"Improved inference of time-varying reproduction numbers during infectious disease outbreaks"**
Thompson RN, Stockwin JE, van Gaalen RD, Polonsky JA, Kamvar ZN, Demarsh PA, et al. *Epidemics* 29:100356. doi:10.1016/j.epidem.2019.100356.

**Archetype:** a *methods extension with guidance and software* — take a widely used estimator, name two of its assumptions that fail in practice, fix both, demonstrate the fix on three outbreaks, and ship it in the package the field already uses. The methodological contribution and the behavioural recommendation are inseparable.

## Structure
Elsevier format: **`Highlights`** (five single-line bullets) → `Keywords` → `Abstract` → numbered sections `1. Introduction` → `2. Methods` (*2.1 Estimating the serial interval distribution*, then the joint estimation) → `3. Results` (*3.1 Estimating the reproduction number* · *3.2 Uncertainty in estimates of R_t* · imported cases) → `4. Discussion`.

**The `Highlights` block is a format worth exploiting rather than enduring.** Five lines carry the problem, the claim, the contribution, the evidence and the software:
> "• Real-time estimation of reproduction numbers during outbreaks can guide control. • Using up-to-date serial interval data and accounting for imported cases is vital. • We develop a framework for estimating pathogen transmissibility appropriately. • We demonstrate it using data from outbreaks of influenza, Ebola and MERS. • Our approach is implemented in R package EpiEstim and online application EpiEstim App."

**Numbered sections and a numbered Results** let the Discussion refer back precisely, which matters when the argument is *this assumption fails, and here is what it costs*.

## Opening move
> "Accurate estimation of the parameters characterising infectious disease transmission is vital for optimising control interventions during epidemics. A valuable metric for assessing the current threat posed by an outbreak is the time-dependent reproduction number, i.e. the expected number of secondary cases caused by each infected individual."

The quantity is defined in the sentence that introduces it, and the serial interval is defined parenthetically where it first appears — "(the time between symptomatic cases in a transmission chain)". **Define both the estimand and the key input in the abstract**, because readers of a methods paper arrive with different vocabularies.

**The contribution is then stated as two numbered requirements**, which is the whole paper in one sentence:
> "Here we show that accurate inference of current transmissibility, and the uncertainty associated with this estimate, requires: (i) up-to-date observations of the serial interval to be included, and; (ii) cases arising from local transmission to be distinguished from those imported from elsewhere."

**State a methods contribution as the conditions for a valid estimate**, not as a new technique. It converts the paper into guidance that applies even to people who do not use the software.

The Introduction then establishes breadth of relevance by citing outbreaks in **humans, animals and plants** — Ebola, UK foot-and-mouth, and *Xylella fastidiosa* in Italy — which positions the method as general rather than COVID- or Ebola-specific, and teaches the threshold logic plainly: "If the value of R_t is and remains below one, the outbreak will die out. However, while R_t is larger than one, a sustained outbreak is likely."

## Methods
- **Describe the procedure as numbered steps before any mathematics**, and put the same steps in the schematic:
  > "We propose a two-step procedure to estimate the time-dependent reproduction number from data informing the serial interval and from data on the incidence of cases over time. The first step uses data on known pairs of index and secondary cases to estimate the serial interval distribution; the second step estimates the time-varying reproduction number jointly from incidence data and from the posterior distribution of the serial interval obtained in the first step."
- **Say what the data actually look like**, including their censoring: "The distribution of serial intervals can be estimated during an ongoing outbreak using interval-censored line list data – namely lower and upper bounds on timings of symptom onset in index and secondary cases."
- **Argue that the required data are routinely available**, which is what makes a method adoptable: "Serial interval data of this form are often collected during outbreaks, particularly in household studies from which chains of transmission can be reconstructed… Historical Ebola outbreaks provide a number of examples of this."
- **Figure 1 is a two-panel schematic of the inference**, not of the biology — step 1 from line list to serial interval posterior, step 2 from that posterior plus incidence to R_t. For a methods paper, diagram the flow of information.

## Results
**Validate against an independent published estimate of the same quantity, and name the methodological difference:**
> "The median reproduction number estimate for the first seven days of the outbreak (April 18th–April 24th 2009) was 3.3 – with 95% credible interval (95% CrI) given by (2.1,5.6) – and the mean estimate for this period was 3.4. These estimates are consistent with a previous estimate of the reproduction number over this time period of 3.3 from a study by Lessler et al. (2009). Those authors used a similar approach to quantify the serial interval distribution to the method used here, but estimated the reproduction number based on the initial exponential growth rate of the outbreak."

Agreement with a method that differs in its second step is stronger evidence than agreement with the same method.

**Describe the practice you are correcting, not just the assumption**: "In practical applications of that method, typically single serial interval distributions, estimated from previous outbreaks or based on early data from the ongoing outbreak, have been used to estimate R_t throughout an epidemic."

**Quantify the cost of the bad practice on real data, and name the papers that did it.** This is the paper's sharpest move:
> "we used data from the 2013–2016 Ebola outbreak in Liberia to show that failing to account for full uncertainty in the serial interval distribution may lead to underestimating the uncertainty surrounding reproduction number estimates. Moreover, ignoring recent data on the serial interval can dramatically impact estimates of the reproduction number and the uncertainty associated with those estimates. This is of practical importance – as an example, a number of studies conducted during and after the 2013-16 West African Ebola outbreak (e.g. Wiratsudakul et al., 2016; Bakker and Wallinga, 2016; Dalziel et al., 2018) used the same single serial interval estimate obtained near the beginning of the outbreak."

Three studies are cited by name as instances of the problem. **Naming real papers that would be affected is what makes a methodological warning land** — done neutrally, as evidence that the practice is widespread rather than as criticism of those authors.

**Demonstrate across three pathogens with different structures** — H1N1 influenza in a school, Ebola, and MERS — chosen because the third has substantial importation, which is the second assumption being fixed.

## Literature
Author–year citations in the Elsevier style, dense, with multi-source parentheses. The treatment of the main alternative method is the model for how to compare estimators:
> "The most commonly used approach for estimating time-dependent reproduction numbers, other than the approach of Cori et al. (2013), is that of Wallinga and Teunis (2004). As described in the introduction, one caveat of the Wallinga and Teunis method is that it estimates the case reproduction number, which is not a measure of instantaneous transmissibility. If a policy-maker wishes to understand the impacts of control interventions in real-time, then an estimate of the case reproduction number is less useful than an estimate of the instantaneous reproduction number because the case reproduction number does not change immediately after interventions are altered; instead, it changes more smoothly and in a delayed manner."

**Distinguish the estimands before comparing the estimators**, and judge them by what a decision-maker needs. Then concede the development that softens the criticism: "although we note that extensions to the Wallinga and Teunis approach have been developed to relax this assumption of the original method."

**Cite the known impossibility result that explains your design choice**: "Some approaches have been proposed to estimate the serial interval and reproduction numbers jointly from time series data on the numbers of new cases … but it has been shown that it may not be possible to estimate both these quantities precisely from those data alone in the early stages of an outbreak … Our approach instead extends the framework of Cori et al. (2013), and relies on observations of transmission pairs in addition to the time series data to estimate the serial interval and the time-varying reproduction number in a two-step estimation process."

The two-step design is justified by an identifiability limit in the literature, not by preference.

## Voice
First-person plural, present and past. The paper is explicit that it is amending a specific prior method and says so repeatedly without disparagement — "Our approach builds on a well-established method (Cori et al., 2013) and addresses two important limitations of the approach as proposed in that study." Modals are graded: failing to account for uncertainty "may lead to underestimating"; using the latest data "may lead to very different, but more robust estimates".

## Discussion and limitations
Opens on why the quantity matters operationally, with a concrete contrast that justifies estimating R_t at all rather than watching incidence:
> "in circumstances in which the incidence of cases is still increasing, but the time-dependent reproduction number is dropping, there might be a very different outlook compared to if the incidence of cases and the reproduction number are both increasing."

Then the two fixes restated, the evidence, and the software. The limitation that matters most is given as a **usage warning with its direction of bias**, which is exactly the habit `SKILL.md` §3 requires (`evidence.md` §3.4):
> "It is worth noting that the pairs of index/secondary cases included in the estimation should be as representative as possible; in particular, if too recent index cases are considered, some of their secondary cases may not have been observed yet, leading to artificial underestimation of the serial interval."

A reader who adopts the method now knows the one way they are most likely to misuse it, and which way the error will run.

## Data, code and funding
The method ships in **the package the field already uses**, versioned — "available as an R software package (EpiEstim 2.2)" — plus "an interactive, user-friendly online interface (EpiEstim App), permitting its use by non-specialists". The abstract closes on adoptability rather than novelty: "Our tool is easy to apply for assessing the transmission potential, and hence informing control, during future outbreaks of a wide range of invading pathogens."

**Extending an established package rather than releasing a competitor is itself a design decision**, and it is stated as part of the contribution.

## Distinctive moves to borrow
1. **State a methods contribution as the conditions required for a valid estimate**, numbered, so it reads as guidance even for people who will not use your code.
2. **Use the `Highlights` block to carry problem, claim, contribution, evidence and software** — one line each.
3. **Define the estimand and its key input in the abstract**, parenthetically.
4. **Diagram the flow of information**, not the biology, in a methods paper.
5. **Argue that the data your method needs are routinely collected**, with examples; adoptability is part of the contribution.
6. **Validate against an independent estimate produced by a different second step.**
7. **Describe the practice you are correcting**, not only the assumption — what people actually do with the method.
8. **Name real published studies that the problem affects**, neutrally, as evidence of prevalence.
9. **Distinguish estimands before comparing estimators**, and judge them by what a decision-maker needs.
10. **Justify a design choice with a published identifiability limit** rather than preference.
11. **Give the usage warning with its direction of bias** — too-recent index cases underestimate the serial interval.
12. **Ship into the package the field already uses**, versioned, with a non-specialist interface.

## Related files
For the guidance paper that systematises these biases see [27-gostic-2020-practical-considerations-rt](27-gostic-2020-practical-considerations-rt.md) and [28-charniga-2024-delay-distributions-best-practices](28-charniga-2024-delay-distributions-best-practices.md); for the Bayesian pipeline that consumes these estimates in real time see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md); for delay correction before estimation see [43-mcgough-2020-nobbs-nowcasting](43-mcgough-2020-nobbs-nowcasting.md); for a real-time application where importation matters see [44-finger-2019-diphtheria-rapid-response](44-finger-2019-diphtheria-rapid-response.md). Other *real-time transmission analysis* exemplars: see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md) for an individual-based model fitted to a live national epidemic while control decisions were still being made; [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md) for district-level transmission estimates turned into beds needed during an outbreak response; [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md) for a natural-experiment evaluation across Chinese cities, with a mechanistic counterfactual, written under emergency time pressure; [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) for the real-time Bayesian estimate of a time-varying reproduction number, in a clinical journal's structure; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver; [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast whose corrected onsets feed a reproduction-number estimate, evaluated against later data.
