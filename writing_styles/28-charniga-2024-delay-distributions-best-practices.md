# 28 — Charniga et al. (2024), *PLoS Computational Biology*
**"Best practices for estimating and reporting epidemiological delay distributions of infectious diseases"**
Charniga K, Park SW, Akhmetzhanov AR, Cori A, Dushoff J, Funk S, Gostic KM, Linton NM, Lison A, Overton CE, Pulliam JRC, Ward T, Cauchemez S, Abbott S.
*PLoS Comput Biol* 20(10):e1012520. doi:10.1371/journal.pcbi.1012520.

**Archetype:** the **checklist and reporting-standard paper** — the guidance archetype taken one step further than [[27-gostic-2020-practical-considerations-rt]]: the deliverables are two adoptable checklists and a decision flowchart, and the technical derivations are deliberately outsourced to a companion paper.

## Structure
Sections are **tasks in a workflow**, in the order a practitioner performs them:

`Introduction` (~8 ¶) → `Biases in delay data` (~4 ¶) → `Measuring epidemiological delays` (~3 ¶) → `Adjusting for common biases` (~4 ¶) → `Additional modeling recommendations` (7 short subsections) → `Reporting epidemiological delay distributions` (~3 ¶) → `Reporting the incubation period and serial interval` (~4 ¶) → `Other considerations` (4 subsections) → `Discussion` (~3 ¶).

The `Additional modeling recommendations` subsections are **imperative sentences**, one recommendation each:
*Fit multiple probability distributions · Visualize the distributions · Correctly convert parameters · Add subgroups or stratify estimates · Check model diagnostics*

A heading that is an instruction is scannable, quotable, and impossible to misread. Use this whenever a section exists to tell someone what to do.

Deliverables:
- **Table 1** — a three-column matrix: bias type × adjustment method × disease examples.
- **Tables 2–3** — the checklists, in item / details / examples / solutions columns.
- **Figs 1–2** — pedagogical diagrams (y-axis "observations of delays", circles and squares for primary and secondary events, brackets for censoring intervals).
- **Fig 3** — a decision flowchart branching on three data-collection scenarios.

## Opening move
> "Epidemiological delays are key quantities that inform public health policy and clinical practice. They are used as inputs for mathematical and statistical models, which in turn can guide control strategies. In recent work, we found that censoring, right truncation, and dynamical bias were rarely addressed correctly when estimating delays and that these biases were large enough to have knock-on impacts across a large number of use cases."

Pattern: **what the quantity is for → what depends on it → the empirical finding that motivates guidance.** The third sentence is the whole justification for the paper, and it is evidential rather than rhetorical: the authors *measured* how often the field gets this wrong, and how much it matters.

Note the phrase **"knock-on impacts"**: the argument is that an error in an input parameter propagates into every downstream model. Guidance papers about a parameter should always trace the error forward to the quantity people actually care about.

## Methodology conventions
- **Technical detail is deliberately outsourced, with a pointer**: "Technical details about these biases and how to adjust for them can be found in Park and colleagues." The paper then states its own distinct contribution explicitly (see Positioning below). Splitting derivation and guidance into two papers, and saying so, keeps both readable.
- **Almost no formal notation.** Delays are described in words — "the time between infection and symptom onset". No compartmental notation at all. Concepts that need a formalism get a *framing* instead: "Estimated event times for each case are included in the model as unobserved, or latent, variables."
- **Three named biases, defined once and used consistently**: censoring, right truncation, dynamical bias. Naming a small closed set of problems, then organising tables, figures and checklists around that same set, is what makes the paper usable.
- **A structural distinction is set up and then used throughout**: forward versus backward cohort approaches, and which biases each is susceptible to. This yields the paper's single strongest recommendation: "We recommend always analyzing delay distributions as forward distributions."
- Assumptions flagged with their caveat inline: the underlying delay distribution is assumed not to change over the epidemic, "although this may not always be the case"; and priors are named where they matter — "uniform prior distributions are used for both the primary and secondary event times".
- **Tools recommended by name, with a basis for the recommendation**: `coarseDataTools`, `epidist`, `EpiNow2`, `epitrix`, `epiparameter`; the Ward et al. approach is named "best performer" *on the basis of the companion paper's simulations*, not on assertion.

## Quantifying why it matters
The paper's evidence is **the size of the error introduced by doing it wrong**, taken from the literature and stated in the units of the parameter:

> "the mean incubation period for COVID-19 in early 2020 … was 3.49 days without adjusting for right truncation compared to 4.69 days when adjusted"
> "Park and colleagues found that ignoring right truncation for a fast-growing epidemic with relatively long delays could result in underestimation of the mean delay distribution by up to 50%"
> "Gostic and colleagues showed how mis-specifying the mean, variance, or form of the generation interval led to biased estimates of R_t when using 3 empirical methods on synthetic data. The bias was greatest early in the epidemic."

Three registers of evidence in three sentences: a **worked before/after pair** on a familiar parameter, a **worst-case magnitude** from simulation, and a **downstream consequence** for a quantity readers care about more. Also note the last clause — "The bias was greatest early in the epidemic" — which tells the reader *when* the problem bites, i.e. exactly when the estimate is most needed.

Figures are referenced with an interpretation attached, never bare: "Right censoring is shown in Fig 1A. The intervals on the top and bottom of the panel are included in the analysis, but we do not know when the secondary events will occur."

## Positioning against prior work
Numbered citations, dense in the Introduction (~10 in the first four paragraphs), sparser in the guidance sections. The contribution is defined by **audience and format**, not by novelty:

> "Our paper goes beyond the work of Park and colleagues by offering practical guidelines, a suggested workflow, and checklists, for a broader technical audience, such as modelers at public health agencies."

The state of the field is described as improving rather than deficient:
> "Methods for estimating epidemiological delays have been improving, especially during the COVID-19 pandemic, and recent research has highlighted the importance of appropriately adjusting for 3 statistical issues inherent in the data collection process: censoring, right truncation, and dynamical bias."

This is the courteous and effective way to publish guidance: the problem is diffusion of good practice, not the absence of it.

## Voice
Active, first-person plural, and openly prescriptive: "We recommend always analyzing delay distributions as forward distributions"; "we formulate a checklist"; "we developed 2 checklists"; "we hope that our recommendations will provide clarity". **"We recommend" appears more than twenty times; "must" does not appear.** Authority is asserted through repetition and specificity, not through modal force.

Consequences are stated in plain conditional form: "Not or incorrectly accounting for censoring of event intervals can lead to biased estimates of a delay."

Hedges qualify applicability, not confidence: "may not always be the case", "likely a better use of available data", "should be taken into account", "Although such methods have been developed, they assume a fully sampled population".

## Discussion and limitations
Opens by re-establishing stakes, then names the methodological frontier:

> "A limitation of current methods for correcting common biases is that they do not fully account for time-varying changes in delay distributions. Future work on delay distributions or nowcasting should extend current methods or develop new methods to account for these changes."

And — importantly for any guidance paper — **fences its own scope and evidential basis**:

> "Also, we did not aim to provide a systematic review; rather, we provided insights based on our experiences. The examples presented in this work were selected to illustrate specific points."

Declaring that examples were *selected to illustrate* rather than sampled is an honest disclosure that most guidance papers omit. Say it.

## Reporting and data-sharing standards
The paper prescribes what to publish, which is itself a model for a data-availability section:

> "Code and data should be uploaded to repositories, such as GitHub or Zenodo, to ensure reproducibility of the analysis and facilitate re-use of the code. Apart from allowing others to reproduce, validate and potentially improve analyses, providing data along with estimates of delay distributions also ensures that the estimates can be integrated in future pooled estimation efforts…"
> "These data should ideally be provided in linelist format with all necessary information required for estimation … Importantly, the data should be anonymized/de-identified to protect patient privacy according to local health data laws and regulations. If data cannot be shared, we recommend at minimum providing samples of the posterior distribution in a permanent online repository…"

Three transferable rules: **share code and data**; **de-identify**; and when data genuinely cannot be shared, **publish posterior samples as the minimum viable artefact** so downstream meta-analysis is still possible. Reporting standards are given for central tendency, variability, credible intervals and contextual information — not just the point estimate.

Also present, and worth copying where authors sit in government agencies:
> "The findings and conclusions in this report are those of the authors and do not necessarily represent the official position of the CDC, US Department of Health and Human Services, NIHR, UK Health Security Agency, or the UK Department of Health and Social Care."

## Distinctive moves to borrow
1. **Make the checklist the deliverable.** Item / details / examples / solutions columns; a reader should be able to work through it against their own manuscript.
2. **Write section headings as imperatives** when the section is an instruction.
3. **Use a decision flowchart branching on what data the reader has**, rather than prescribing one method for everyone.
4. **Name a small closed set of problems** and organise every table, figure and recommendation around that same set.
5. **Quantify the cost of bad practice** in the parameter's own units, then trace it downstream.
6. **Split derivation and guidance into two papers** and state what each does.
7. **Disclose that your examples were selected to illustrate**, and that you did not do a systematic review.
8. **Specify the minimum shareable artefact** when raw data cannot be released.

## Related files
Direct companion to [[27-gostic-2020-practical-considerations-rt]], and cites it for downstream consequences. Delay distributions are an input to [[19-kucharski-2020-early-dynamics-covid]], [[26-abbott-2020-rt-estimation-tool]] and [[07-lauer-2020-incubation-period]] — the last of which is the kind of primary estimation paper these standards are written to improve.
