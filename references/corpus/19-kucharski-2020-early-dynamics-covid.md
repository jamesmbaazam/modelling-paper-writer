# 19 — Kucharski et al. (2020), *The Lancet Infectious Diseases*
**"Early dynamics of transmission and control of COVID-19: a mathematical modelling study"**
Kucharski AJ, Russell TW, Diamond C, Liu Y, Edmunds J, Funk S, Eggo RM. *Lancet Infect Dis* 20(5):553–558. PMC7158569.

**Archetype:** the *real-time Bayesian transmission-model* paper in a clinical journal — the dominant template for time-varying reproduction number estimation. Note how much of the structure is imposed by the journal, and how well that imposed structure works.

## Structure
`Summary` with mandated labels — **Background / Methods / Findings / Interpretation / Funding** → `Introduction` → **`Research in context`** panel (*Evidence before this study* / *Added value of this study* / *Implications of all the available evidence*) → `Methods` (*Data sources*, *Procedures*, *Role of the funding source*) → `Results` → `Discussion` → Contributors → Declaration of interests → Acknowledgements.

The `Research in context` panel is worth writing even for journals that do not require it: it forces you to state, in three short paragraphs, what was known, what you added, and what should now change.

## Opening move
> "An outbreak of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) has led to 95 333 confirmed cases as of March 5, 2020. Understanding the early transmission dynamics of the infection and evaluating the effectiveness of control measures is crucial for assessing the potential for sustained transmission to occur in new areas."

Pattern: **counted burden with a data-lock date → the decision the estimate serves.** The count is exact and dated, so the paper ages honestly.

## Methods
- Compartments described in a sentence, then delegated: "In the model, we divided individuals into four infection classes, as follows: susceptible, exposed (but not yet infectious), infectious, and removed", with a figure reference and appendix pointer.
- **No equations in the main text**; the appendix is cited to the page ("appendix pp 1–3", "pp 10–13").
- Distributional assumptions given with the distribution named and both moments: "The incubation period was assumed to be Erlang distributed with mean 5·2 days (SD 3·7)."
- Starting conditions stated as assumptions: "We assumed the outbreak started with a single infectious case on Nov 22, 2019."
- Inference method named precisely: "We used sequential Monte Carlo simulation to infer the transmission rate over time", with the free parameters enumerated.
- Sensitivity analyses listed by what was varied (initial case number, connectivity data source, pre-symptomatic transmission) and summarised by conclusion, not by table: they "produced the same conclusion about the decline in transmission".
- **Joint fitting to multiple data streams** — cases in Wuhan, internationally exported cases, evacuation flights — is the paper's methodological claim, and it is stated as such.

## Results
Medians with 95% credible intervals; middle-dot decimals per Lancet style; the CI parenthesis drops the "95% CI" label after first use.
> "We estimated that the median daily reproduction number (Rt) in Wuhan declined from 2·35 (95% CI 1·15–4·77) 1 week before travel restrictions were introduced on Jan 23, 2020, to 1·05 (0·41–2·39) 1 week after."
> "We estimated that 94·8% (95% CI 93·1–96·1%) of the Wuhan population were still susceptible on Jan 31, 2020."
> "Our results suggested there were around ten times more symptomatic cases in Wuhan in late January than were reported as confirmed cases, but the model did not predict the slowdown in cases that was observed in early February."

The last sentence is the model of intellectual honesty in this corpus: **report where your model fails in the Results, not only in the Discussion.**

## Literature
~24 references over ~2000 words. Positioning is explicit and specific, in the Research in context panel:
> "We identified no estimates of how R0 had changed in Wuhan since control measures were introduced in late January or estimates that jointly fitted data within Wuhan to international exported cases and evacuation flights."
Note the form: not "no one has studied X", but "we identified no estimates of [precisely specified quantity] using [precisely specified data combination]" — a claim that is checkable.

## Voice
Past tense for analysis, present for standing conclusions. Active, first-person plural throughout. Hedging carries real information: "COVID-19 transmission probably declined in Wuhan during late January, 2020"; "We found some evidence of a reduction".

## Discussion and limitations
> "There are several other limitations to our analysis. We used plausible biological parameters for SARS-CoV-2 based on current evidence, but these values might be refined as more comprehensive data become available."
Each limitation is paired with the mitigation attempted: "by fitting to multiple datasets … we have attempted to make the best possible use of the available evidence". Residual unknowns are named rather than glossed: "it remains unclear what the precise extent of such variation is for SARS-CoV-2."

## Data, code and funding
> "All data and code required to reproduce the analysis is available online" (GitHub).
> "The funder of the study had no role in study design, data collection, data analysis, data interpretation, or writing of the report. The corresponding author had full access to all the data in the study and had final responsibility for the decision to submit for publication."
An interactive online tool is released alongside: "We have made an online tool so that users can explore these risk estimates if new data become available."

## Distinctive moves to borrow
1. Write the `Research in context` panel first — it disciplines the whole paper.
2. Fit to several data streams and say why that is the contribution.
3. Report the model's failure to reproduce a feature of the data in the Results.
4. Convert dynamics into a decision-shaped probability: ">50% chance the infection will establish".

## Related files
Other *real-time transmission analysis* exemplars: see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md) for an individual-based model fitted to a live national epidemic while control decisions were still being made; [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md) for district-level transmission estimates turned into beds needed during an outbreak response; [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) for a widely used R_t estimator with two failing assumptions fixed, shipped in the package the field already uses; [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md) for a natural-experiment evaluation across Chinese cities, with a mechanistic counterfactual, written under emergency time pressure; [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md) for a living pipeline whose article versions its method alongside its software; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver; [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast whose corrected onsets feed a reproduction-number estimate, evaluated against later data.
