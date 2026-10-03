# 38 — Chen et al. (2019), *The Lancet Global Health*
**"Effect and cost-effectiveness of pneumococcal conjugate vaccination: a global modelling analysis"**
Chen C, Cervero Liceras F, Flasche S, Sidharta S, Yoong J, Sundaram N, Jit M. *Lancet Glob Health* 7(1):e58–e67. doi:10.1016/S2214-109X(18)30422-4.

**Archetype:** the *vaccine impact and economic evaluation* — couple an epidemiological model to a decision-analytic cost model, report health outcomes and costs under vaccination versus no vaccination, and translate the result into an incremental cost-effectiveness ratio against a named threshold. The corpus's exemplar for the ◆ CHEERS rule in `SKILL.md` §6.

## Structure
Lancet family, structured throughout: `Summary` (**Background / Methods / Findings / Interpretation / Funding**) → **`Research in context`** panel → `Introduction` → `Methods` (*Model overview and framework* · *Ecological model* · *Economic model* · costs and outcomes · sensitivity analyses · *Role of the funding source*) → `Results` → `Discussion` → back matter.

**The Methods subheadings are the two models and the seam between them**, which is the right scheme for any coupled model: name each component, then say explicitly how the output of one becomes the input of the other — "The second model, a decision-tree model, used outputs of the ecological model to predict a range of clinical presentations and economic outcomes."

## Opening move
> "Pneumonia is the single largest global cause of mortality from infectious disease in children younger than 5 years. In 2015, pneumonia killed an estimated 920 000 children (14·9% of all deaths in children younger than 5 years)."

Burden, quantified, dated, and given twice — absolute count and share of all under-5 deaths. The second number is what makes the first interpretable.

The Introduction then builds the decision the paper exists to inform, not merely a knowledge gap: vaccines exist and work, but "more than 40 countries have yet to introduce PCVs into their national immunisation schedules… include several countries with large populations, such as China and Nigeria", and "many low-income countries that have introduced PCVs are transitioning from eligibility for Gavi support and will therefore need to fund vaccination from national health-care budgets and, eventually, at higher prices."

**The gap is then stated as a methodological deficiency in existing studies, not as absence:**
> "However, for many countries, the cost-effectiveness of PCV introduction remains to be evaluated rigorously and in an internationally comparable manner. Existing studies either omit many of the effects of PCV introduction, such as herd protection and serotype replacement, or address only a subset of countries."

Two named omissions and a scope limit — each of which the paper then fixes. Compare the vague alternative, *the cost-effectiveness of PCVs is not well understood*, which commits to nothing and cannot be checked.

**The `Research in context` panel gives the search string**, which is the most checkable form a gap statement can take:
> "We searched PubMed without language or date restrictions for all records matching '(pneumococcal conjugate vaccine) and (cost-effectiveness) and (child*) and (global)' in any field. Our review identified 22 cost-effectiveness evaluations… We found three articles that estimated the impact of PCVs in low-income and middle-income countries, but no study assessing the cost-effectiveness of PCVs globally."

## Methods
- **Disambiguate a word that means two things in your readership's two fields**: "the term ecological is used here in the epidemiological rather than biological sense, wherein the unit of analysis is the population rather than the individual." One clause, inserted where the word first appears.
- **State the model's time and space footprint as a single sentence**: "The combined model followed 30 birth cohorts of children younger than 5 years from 2015 to 2045 in 180 countries."
- **List the simplifying assumptions that buy the simplification, in order**: the ecological model "simplified the long-term impact predictions, including serotype replacement and herd protection, from more elaborate susceptible-infectious-susceptible-type dynamic transmission models into a single predictive equation by making a number of assumptions: that vaccine serotypes will eventually be eliminated as a result of PCV use; that eliminated serotypes will be fully replaced in carriage by non-vaccine serotypes; and that the propensity of non-vaccine serotypes to cause invasive disease if carried remains the same in the post-PCV era."
- **Re-label the output to match what the assumptions permit** — the single most transferable move in this paper:
  > "Given the assumption of vaccine serotype elimination, model predictions should be treated as estimates of the maximum reduction in IPD that can be achieved through vaccination, rather than necessarily predictions of vaccine impact."

  The quantity is renamed (a *maximum achievable reduction*, not an *impact*), and the sentence after names the settings where the gap bites: "in settings with low vaccine coverage or intense transmission, vaccination might not be able to completely eliminate vaccine serotypes."
- **Attach the sensitivity analysis to the assumption it relaxes, with a real-world anchor**: "Therefore, we present a sensitivity analysis based on the assumption that reduction in carriage due to vaccine serotypes is only 65% (as observed in Kilifi, Kenya), and PCV impact is thus only 65% of our model's base-case prediction."
- **Say where every parameter came from, including the awkward ones.** Posterior samples were available for carriage but not for disease, so: "For IPD, because no posterior distributions were reported, we fitted a binomial distribution to the reported regional PCV13 serotype coverage estimates to match reported means and 95% confidence intervals, and took 1000 bootstrap samples from those." Unpublished inputs are cited as personal communications with the institution named.
- **Borrow an empirical time course rather than assuming instant effect**: "the proportionate reduction in disease over time after vaccination follows the same time course as that observed in a multi-country review of post-vaccination data (ie, that 79% of the impact is achieved in the first year following introduction of PCV, and the full impact is established from year 2 onwards)."
- ◆ **Run both one-way and probabilistic sensitivity analyses** and say so in the abstract — standard practice for an economic evaluation, and what CHEERS expects.

## Results
**Give the denominator before the effect.** The burden without vaccination comes first — "we project more than 1·18 million deaths (95% credible interval 0·780 million to 1·76 million) and 457 million disease episodes (449 million to 465 million) annually before vaccination" — and only then the averted fraction: "Vaccination could prevent 34% of global deaths (0·399 million [0·208 million to 0·711 million]) and 12% of disease episodes."

**Report the percentage and the count together**, every time. A reader who cares about programme scale wants the count; a reader comparing interventions wants the fraction.

**Report costs and savings as separate signed quantities, not a net figure**: "Global vaccine costs (in 2015 international dollars) of $15·5 billion could be partially offset by health-care savings of $3·19 billion (2·62 billion to 3·92 billion) and societal cost savings of $2·64 billion (2·13 billion to 3·28 billion)." The reader can reassemble the net under their own perspective — and the costing year and currency are stated with the first figure.

**The headline equity finding is a ratio of two shares**, which is why it travels:
> "The 71 countries eligible for support from Gavi, the Vaccine Alliance, account for 83% of PCV13-preventable deaths but only 18% of global vaccination costs."

The same shape recurs in the Discussion — "PCV introduction throughout Africa requires only 12% of global PCV investments but accounts for 69% of the lives saved and 63% of the DALYs averted globally." **Two shares of two different totals, contrasted in one sentence**, is the most quotable construction available to a global-health modelling paper.

**Hedge a cost-effectiveness verdict to the strength of the threshold**: "PCV13 use is probably cost-effective in all six UN regions" in the abstract; then in the Discussion, the threshold is interrogated rather than assumed:
> "The ICER for PCV introduction is less than GDP per capita in almost all regions and countries. The GDP per capita threshold has been traditionally used as an indication of cost-effectiveness, but has been criticised. Using a more stringent threshold estimated by Woods and colleagues on the basis of the opportunity cost of health expenditure, PCV is cost-effective in 143 of 180 countries."

**Report the result under both thresholds and give the count under the stricter one.** An ICER is meaningless without the threshold it is judged against, and a paper that reports only the generous threshold invites the obvious objection.

## Literature
Numbered Lancet-style citations, moderate density, concentrated in the Introduction and in parameter justification. Prior work is characterised by what it left out rather than dismissed: "Previous economic evaluations have often ignored these effects or represented them using simplified assumptions, such as representing the indirect effects of PCV10 or PCV13 using the experience of PCV7 introduction in the USA." The novelty claim is bounded by date and scope — "To our knowledge, the only cost-effectiveness evaluations of PCV that consider more than a few countries were published in 2011 or earlier, and were restricted to Gavi-eligible countries alone" — which is a checkable claim rather than a first-study assertion.

## Voice
First-person plural, past for what was done and conditional for projections: "We estimate that global PCV13 use **could** prevent…", "Vaccination **could** prevent 34% of global deaths". The conditional is used consistently for every projected quantity and dropped for the data-derived ones, so the modal does real work.

## Discussion and limitations
Opens with the result restated in decision units, then the equity split, then the limitations — each one naming the direction of its effect:

- **An assumption that may not hold, with the evidence on both sides**: "The ecological model assumed that vaccine coverage and effectiveness will be high enough to achieve elimination of vaccine serotypes… Although some residual vaccine-type carriage following vaccination has been observed in African settings despite high vaccine coverage, we assumed that with such low residual vaccine-type carriage rates, our model would still perform better than other methods for predicting vaccine effect."
- **A data limitation whose bias runs in opposite directions in different groups** — unusually precise:
  > "we extrapolated vaccine prices from a few settings with publicly available prices… to other countries in the same income group. This approach probably overestimates prices for high-income countries and underestimates prices in middle-income countries with no access to pooled procurement mechanisms."

  and then the observation that makes the limitation itself a finding: "most countries yet to introduce PCV into their routine schedules are middle-income countries outside Latin America (ie, those with no access to pooled procurement), possibly indicating that high vaccine prices are a barrier to wider introduction."
- **An omission declared conservative, with the reason and the check**: lifetime costs of meningitis sequelae "were not considered in this analysis because of the unavailability of cost-of-illness studies. Therefore, our analysis is conservative. However, our deterministic and probabilistic sensitivity analyses confirmed that PCV13 was cost-effective globally across changes in disease burden and treatment cost."
- **A scope fence on the population modelled**: "our study focused only on populations younger than 5 years."

Closes on the policy mechanism rather than on research: the findings "underscore the importance of Gavi support and of mechanisms to support vaccine introduction at affordable prices for disadvantaged populations not eligible for Gavi support", with the actionable corollary that the analysis "provides an indication of prices that countries could seek to negotiate for in national tenders, although country purchasers are usually encouraged to use their own nationally derived thresholds".

## Data, code and funding
Funders named in the `Summary` (`Funding: World Health Organization; Gavi, the Vaccine Alliance; and the Bill & Melinda Gates Foundation`) with the Lancet-mandated *Role of the funding source*, equal-contribution authors flagged, and the appendix carrying the model structure.

## Distinctive moves to borrow
1. **Rename the output to what the assumptions actually license** — a *maximum achievable reduction*, not an *impact* — and name the settings where the two diverge.
2. **Give the search string in the gap statement.** A reader can run it.
3. **Name the two things previous work omitted** (herd protection, serotype replacement) and fix exactly those.
4. **Report the pre-intervention burden before the averted fraction**, and give percentage and count together.
5. **Keep costs and savings as separate signed quantities**, with currency and price year attached to the first figure.
6. **Contrast two shares of two different totals** — 83% of deaths, 18% of costs — to make an equity finding quotable.
7. ◆ **Judge the ICER against more than one threshold**, including a stricter one, and report how many countries survive it.
8. **Disambiguate a term that means different things to your two audiences**, at first use.
9. **State a bias that runs in opposite directions in different subgroups**, rather than calling it "uncertainty".
10. **Declare an omission conservative only when you can show it**, and cite the sensitivity analysis that does.
11. **Turn a data limitation into a substantive observation** where it legitimately is one (missing tender prices ⇒ price as a barrier to introduction).

## Related files
For the decision-analytic machinery under uncertainty see [23-li-2017-essential-information-ebola](23-li-2017-essential-information-ebola.md); for vaccination-policy modelling in a single country see [01-grais-2008-measles-orv-niamey](01-grais-2008-measles-orv-niamey.md); for the Lancet structure and `Research in context` convention see [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) and [25-davies-2020-npi-uk](25-davies-2020-npi-uk.md).
