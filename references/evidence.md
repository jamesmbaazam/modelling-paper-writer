# Evidence: the corpus behind each rule

Companion to `SKILL.md`. Section numbers here match the rule sections there: when
`SKILL.md` §3.2 says *give every number a comparator*, §3.2 here holds the corpus quotations
that justify it.

**Never read this file whole — it is over 1,200 lines.** Find the §N.M you need in the
Contents below, `grep -n '^##'` this file for that heading and the one after it, and `Read`
only that line range. Come here when a rule is too terse to apply, when the user asks *why*,
when you are critiquing, or when you need a venue's headings and budgets (§1.2).

Papers are cited as Author YEAR; `corpus-index.md` maps each to its file in
`references/corpus/`, where the per-paper analyses sit under the canonical headings listed in
`SKILL.md` step 3.

As in `SKILL.md`, **a rule marked ◆ does not come from the corpus** — it comes from journal
instructions, a reporting guideline, or general practice in the field. Those are the rules to
check against a current source before relying on them. Everything unmarked is attributed to a
corpus paper on the same line.

## Contents

- 0. First decide the archetype
- 1. Structural patterns
  - 1.0 Titles
  - 1.1 The universal spine
  - 1.2 Journal templates
  - 1.3 Subheading craft
  - 1.4 Introduction shape
- 2. Methodology conventions
  - 2.1 How much mathematics, and where
  - 2.2 Assumptions
  - 2.3 Parameters and priors
  - 2.4 Scenarios
  - 2.5 Sensitivity analysis
  - 2.6 Software and computation
- 3. Results storytelling
  - 3.1 Uncertainty: pick the right interval and label it
  - 3.2 Give every number a comparator
  - 3.3 Sentence shapes that recur
  - 3.4 Grade your verbs and modals to your evidence
  - 3.5 Report your own failures in the Results
  - 3.6 Figures and tables
- 4. Literature integration
  - 4.1 Density
  - 4.2 How to state the gap
  - 4.3 Seven ways to position against prior work
  - 4.4 Other integration habits
- 5. Voice and tone
  - 5.1 Person and tense
  - 5.2 Hedging that carries information
  - 5.3 Precision over vagueness
- 6. Domain-specific conventions
  - 6.1 The R₀ paragraph
  - 6.2 Validation, out-of-sample evidence and scoring
  - 6.3 Identifiability and the limits of inference
  - 6.4 Decision relevance
  - 6.5 Real-time and living analyses
  - 6.6 Data, code and funding statements
- 7. Machine learning and predictive modelling conventions
  - 7.1 Lead with the problem, not the algorithm
  - 7.2 Structure Methods as the pipeline, in execution order
  - 7.3 Train/test discipline — state it in one unambiguous sentence
  - 7.4 Report performance honestly
  - 7.5 Confront bias in the training data explicitly
  - 7.6 Interpretation is a result, not a garnish
  - 7.7 Say which numbers are ordinal
  - 7.8 What appraisers will mark you down for
  - 7.9 The two failure modes that killed Google Flu Trends
- 8. Discussion and limitations
  - 8.1 Discussion shape
  - 8.2 Limitations
- 9. Best-practice and guidance papers
  - 9.1 Structure by problem or by task, not by IMRaD
  - 9.2 Build the paper so the summaries alone are usable
  - 9.3 Simulate the truth, then degrade the data one step at a time
  - 9.4 Quantify the cost of bad practice
  - 9.5 Prescriptive but not imperious
  - 9.6 Other conventions of the archetype

## 0. First decide the archetype

Almost every choice below follows from what kind of paper this is. Identify the archetype
before writing a word; the corpus contains fourteen, each with a canonical exemplar.

| Archetype | What it delivers | Exemplars |
|---|---|---|
| **Parameter estimation** | One well-defined quantity, cleanly estimated, translated into a decision | Lauer 2020 (incubation period) |
| **Real-time transmission analysis** | R_t or transmission dynamics fitted to a live outbreak | Kucharski 2020, Abbott 2020, Tian 2020, Keeling 2001 |
| **Scenario projection for policy** | A ladder of intervention scenarios, projected forward | Davies 2020 (UK NPIs), Ferguson 2006 (mitigation) |
| **Feasibility / threshold** | The parameter boundary at which a strategy works | Ferguson 2005 (containment), Hellewell 2020 (contact tracing) |
| **Policy counterfactual** | What a past intervention achieved, and what alternatives would have | Grais 2008, Nouvellet 2015 |
| **Competing hypotheses** | Several mechanisms formalised, fitted and ranked | Davies 2021 (B.1.1.7) |
| **Forecast evaluation** | Many models, one scoring rule, a verdict | Cramer 2022, Reich 2019, Bracher 2021a |
| **Dynamical systems** | A system shown to sit in a different regime than assumed | Ferrari 2008, Earn 2000, Bjørnstad 2002, Grenfell 2001 |
| **Methods / simulation benchmark / critique** | A tool, a validation, or a demonstration of what cannot be inferred | Lee 2010, Bracher 2021a, Keeling & Rohani 2002, Weitz 2015, Li 2017 |
| **Review** | A framework that organises a scattered literature | Baker 2021, Heesterbeek 2015, Altizer 2006 |
| **Best-practice guidance** | Recommendations, checklists or reporting standards for a method others already use | Gostic 2020 (R_t), Charniga 2024 (delay distributions) |
| **Risk mapping / trait prediction** | A supervised model over covariates or traits, producing a surface or a ranked candidate list | Bhatt 2013 (dengue), Olival 2017 (spillover), Han 2015 (rodents) |
| **Digital surveillance / nowcasting** | An estimate of a surveillance quantity, faster than surveillance | Ginsberg 2009 (Google Flu Trends), Yang 2015 (ARGO) |
| **Clinical prediction model** | A patient-level classifier with an intended point of care | Zoabi 2021 (COVID symptoms) |
| **Critique / appraisal** | A verdict on a method or a whole literature, plus named failure modes | Lazer 2014, Wynants 2020, Roberts 2021 |

The archetype determines the shape of the headline claim:

- estimation → a number with an interval
- feasibility → a **threshold** ("containment is feasible if R₀ < 1.8")
- scenario → a **comparison against a named reference scenario**
- counterfactual → a **percentage averted relative to what happened**
- evaluation → a **score relative to a naïve baseline**
- dynamical → a **regime** ("within the chaotic domain of deterministic dynamics")
- methods / simulation benchmark → a **limit on what the data can identify**, or a validated
  tool with its failure conditions
- guidance → a **direction and magnitude of bias**, plus a recommendation ("if the mean
  generation interval is set too high, R_t values will typically be further from 1 than the
  true value")
- risk mapping → a **burden or a named candidate list**, never the AUC
- nowcasting → a **reduction in reporting lag**, benchmarked against a naive alternative
- clinical prediction → a **discrimination metric with an interval and a named operating point**
- critique / appraisal → a **named failure mode** ("big data hubris", "Frankenstein datasets")

---

## 1. Structural patterns

### 1.0 Titles

The corpus titles fall into four shapes. Pick the shape by archetype, then apply the rules.

| Shape | Pattern | Corpus examples |
|---|---|---|
| **Claim** | The finding as a declarative sentence | *Host and viral traits predict zoonotic spillover from mammals* (Olival 2017); *Improving propensity score weighting using machine learning* (Lee 2010) |
| **Object + verb phrase** | *Estimating / Evaluating / Detecting* + the quantity + the data or setting | *Estimating the time-varying reproduction number of SARS-CoV-2 using national and subnational case counts* (Abbott 2020); *Detecting influenza epidemics using search engine query data* (Ginsberg 2009); *Evaluating epidemic forecasts in an interval format* (Bracher 2021a) |
| **Quantity, pathogen, place** | The estimand and its scope, no verb | *The incubation period of coronavirus disease 2019 (COVID-19) from publicly reported confirmed cases* (Lauer 2020); *The global distribution and burden of dengue* (Bhatt 2013); *Estimated transmissibility and impact of SARS-CoV-2 lineage B.1.1.7 in England* (Davies 2021) |
| **Question or strategy** | *Strategies for…* / *Feasibility of…* / *The role of…* | *Strategies for containing an emerging influenza pandemic in Southeast Asia* (Ferguson 2005); *Feasibility of controlling COVID-19 outbreaks by isolation of cases and contacts* (Hellewell 2020); *The role of rapid diagnostics in managing Ebola epidemics* (Nouvellet 2015) |

Rules:

- **Name the pathogen and the place or population** unless the paper is general theory (Earn 2000,
  Altizer 2006, Baker 2021). Two of the four shapes carry them by construction.
- **Name the estimand, not the model.** *Estimating the time-varying reproduction number*
  (Abbott 2020), not *A Bayesian semi-mechanistic model for…*. The method goes in the subtitle if
  anywhere. The exception is a methods paper, where the method *is* the object (Bracher 2021a, Bjørnstad 2002).
- **A claim title needs a claim you will defend in the Discussion.** Olival 2017 can say *predict*
  because the paper reports out-of-sample performance; do not use the shape for a projection
  under assumptions.
- **Lancet family appends a genre label**: *: a mathematical modelling study* (Kucharski 2020, Davies 2020).
  Use it; the editors will add it if you do not. *BMJ* and *Annals* use *: systematic review*
  and similar (Wynants 2020).
- **Colon subtitles carry one of three things**: the method or data (Lauer 2020: *estimation and
  application*; Bjørnstad 2002: *estimating scaling of transmission rates using a time series SIR model*),
  the mechanism (Keeling 2001: *stochastic dispersal in a heterogeneous landscape*), or the payoff
  (Weitz 2015: *challenges for inference and opportunities for control*). Not a restatement of the
  main title.
- **A hook before the colon is allowed once per career** and only when it is exact: *Time is
  of the essence* (Grais 2008) is about the timing of a vaccination campaign; *The parable of Google
  Flu* (Lazer 2014) announces a cautionary tale. If the hook could sit on any paper, cut it.
- **Length**: the corpus runs 6–20 words, median 10, with half the titles between 8 and 13.
  *Nature* and *Science* are the shortest (median 9, longest 17 — Tian 2020); the *Lancet*
  family the longest, because the genre label is appended (11–19). Aim for the 8–13 band and
  treat anything past 18 as needing a reason. Every word should be one a reader would search
  for: no corpus title contains *A study of*, *An analysis of*, *Insights into*, *Towards* or
  *Novel*.
- **Do not put a number in the title** unless it is the finding (*the first 50 days* in Tian 2020
  is scope, and fine; *R₀ = 2·5* is not).

### 1.1 The universal spine

The empirical and policy papers in the corpus are built on the same six moves; journal
format only changes where the moves live. Reviews (Baker 2021, Heesterbeek 2015, Altizer 2006)
carry moves 1, 2 and 6 and replace the result with a framework — Altizer 2006 enumerates its
mechanisms where an empirical paper would give a result. The methods papers (Keeling & Rohani
2002, Bracher 2021a) replace move 1 with the modelling practice they are correcting.

1. **Burden or urgency**, quantified and dated.
2. **The specific gap** — a quantity that is missing, a strategy whose effect is unknown, an
   expectation that the data violate.
3. **"Here, we…"** — one sentence naming the model class and the data.
4. **The headline result**, with its uncertainty, in the abstract. Never withhold it.
5. **The condition or caveat that bounds the result.**
6. **What should now change** — a decision, a data collection priority, or a research question.

An annotated abstract built on these six moves is worked in examples.md §12.2.

### 1.2 Journal templates

◆ **Abstract and main-text budgets.** Journal instructions, not a corpus observation.
Typical limits for the venues in the corpus and the modelling venues users most often target. These drift; **verify against the current author
guidelines before drafting**; for an abstract, title or heading scheme, ask the user for the
target if it is not inferable. Write
to the budget from the first draft — an abstract cut from 400 words to 250 loses its
uncertainty statements first, which is the wrong thing to lose.

| Venue | Abstract | Fields | Main text | Other constraints |
|---|---|---|---|---|
| *Nature* | ≤150 words, unreferenced, one paragraph | Unstructured, but built on the §1.1 spine | ~3,000 words (Articles) | ≤6 display items; Methods separate, ≤3,000 words |
| *Science* | ≤125 words | Unstructured | ~2,500 (Reports) / ~4,500 (Research Articles) | Editor's summary written by the journal; supplementary materials carry the model |
| *PNAS* | ≤250 words | Unstructured | ~4,500 words | *Significance* ≤120 words, no jargon; Methods last |
| *Lancet* family (incl. *Lancet ID*, *Lancet Public Health*) | ≤300 words | Background / Methods / Findings / Interpretation / Funding | 3,500 words | *Research in context* panel; ≤30 refs; ≤5 tables + figures; *Role of the funding source* |
| *BMJ* | ≤400 words | Objectives / Design / Setting / Participants / Interventions / Main outcome measures / Results / Conclusions (adapt for modelling: Design → model type) | 4,000 words | *What is already known / What this study adds* box, ≤3 bullets each |
| *Annals of Internal Medicine* | ≤275 words | Background / Objective / Design / Setting / Participants / Measurements / Results / **Limitation** (one sentence) / Conclusion / Primary Funding Source | ~3,500 words | Reproducible Research Statement |
| *PLoS Computational Biology*, *PLoS Medicine* | ≤300 words | Unstructured (*PLoS Med*: Background / Methods and findings / Conclusions) | No limit (*PLoS Med* ~3,500–4,500) | *Author Summary* ~150–200 words; *PLoS Med* also wants a three-question *Author summary* box |
| *Nature Machine Intelligence*, *npj Digital Medicine* | ≤150 words | Unstructured | ~3,000 / no firm limit | TRIPOD+AI checklist expected |
| *J R Soc Interface*, *Proc B* | ≤200 words | Unstructured | ~5,000 (*Interface*) / ~5,000 (*Proc B*) | Electronic supplementary material referenced inline |
| *Epidemics* | ≤250 words | Unstructured | No firm limit | Highlights (3–5 bullets, ≤85 chars each) |
| *Eurosurveillance* | ≤250 words | Background / Aim / Methods / Results / Conclusion | 3,500 words | Rapid communications: ≤1,500 words, ≤150-word abstract |
| *Wellcome Open Research* | ≤300 words | Optional structure | No limit | Versioning; separate Data and Software availability |

Field budgets inside a 300-word Lancet-style abstract, from Kucharski 2020, Hellewell 2020, Davies 2020: **Background**
50–70 words (moves 1–2 of §1.1), **Methods** 70–90 (move 3, plus data, period, scenarios),
**Findings** 100–130 (moves 4–5, with intervals), **Interpretation** 40–60 (move 6),
**Funding** one line. Findings is the field to protect when cutting.

**Nature / Science (Articles, Reports).** No `Introduction`/`Results` headings. A dense
one-paragraph abstract, then continuous text broken by **short topic subheadings**
(`Seasonality and dynamics in Niamey`; `Modelling pandemic spread`; `Measuring the new
variant's growth rate`). Methods compressed at the end or absent; everything else in the
Supplementary Information, referenced inline. Science adds a structured editor's abstract
(`INTRODUCTION`/`RATIONALE`/`RESULTS`/`CONCLUSION`) and a summary box.
→ Ferrari 2008, Earn 2000, Ferguson 2006, Ferguson 2005, Tian 2020, Grenfell 2001, Nouvellet 2015, Davies 2021

**PNAS.** `Significance` (≤120 words, plain language) → Abstract → Introduction →
**Results** → Discussion → **Materials and Methods last**. Results subheadings are
**claims, not topics**: *Model Accuracy Rankings Are Highly Variable*; *Forecast Performance
Degrades with Increasing Horizons*. Methods subheadings are the decisions a critic would
challenge: *Forecast Model Eligibility and Evaluation Period*.
→ Cramer 2022, Reich 2019, Li 2017

**Lancet family.** Structured abstract (**Background / Methods / Findings / Interpretation /
Funding**) → **`Research in context`** panel (*Evidence before this study* / *Added value of
this study* / *Implications of all the available evidence*) → Introduction → Methods (with a
mandatory *Role of the funding source*) → Results → Discussion → Data sharing → Contributors
→ Declaration of interests.
→ Kucharski 2020, Hellewell 2020, Davies 2020

*Plan with the `Research in context` triplet first even when the journal does not require
it.* Three short paragraphs — what was known, what you added, what should change — will
discipline the whole manuscript. It is scaffolding for your own drafting: return it to the
user only when the target journal requires the panel or the user asks for it.

**PLoS / methods journals.** Numbered sections and subsections (`2.1`, `2.2`) are appropriate
and normal when the contribution is methodological. PLoS also wants an **Author Summary**
written for the practitioner alongside the technical abstract.
→ Bracher 2021a

**Royal Society journals (*J R Soc Interface*, *Proc B*).** Conventional IMRaD with
unnumbered subsections; the Methods can carry the full model specification in the main text.
→ Grais 2008

**Clinical journals (Annals, etc.).** Fully labelled abstract including a mandated
single-sentence **`Limitation:`** field, plus a **Reproducible Research Statement**.
→ Lauer 2020

**Open/living formats (Wellcome Open Research).** Versioned article with an explicit
**`Amendments from Version N`** changelog, and separate `Data availability` and `Software
availability` sections, the latter split into *Development* and *Archived at time of
publication*.
→ Abbott 2020

### 1.3 Subheading craft

- **Mirror Methods and Results subheadings** when the paper has parallel analyses, so each can
  be read alone (Nouvellet 2015: *Potential impact of RDTs in a health-care unit* appears in
  both).
- **Make Results subheadings declarative** where the journal allows — read in sequence they
  should be the paper's argument (Cramer 2022, Weitz 2015).
- **Give a pre-empted objection its own heading.** Davies 2021 has a Methods subsection titled
  *"Apparent growth of VOC 202012/01 not a result of testing artifacts"* — the most obvious
  alternative explanation is refuted where a sceptic will look for it.
- **Give a known bias its own Methods subsection** when it governs how output must be read
  (Abbott 2020: *The effect of changes in testing procedure*).
- **Define your outcome formally under its own heading** when it is binary
  (Hellewell 2020: *Definition of outbreak control*).

### 1.4 Introduction shape

Four to six paragraphs; five moves:

1. The pathogen or system, with burden quantified and dated.
2. What is established — cited compactly, several references per sentence.
3. What follows from that, stated precisely enough to be contradicted.
4. The gap, stated as a checkable claim about the literature, not as "little is known".
5. The question, often as an explicit list ("Three key questions arose…", Grais 2008), which
   Results and Discussion then answer in order.

Openings from the corpus, all following the same beat:

> "The current World Health Organization recommendations for response during measles epidemics
> focus on case management rather than outbreak response vaccination (ORV) campaigns, which may
> occur too late to impact morbidity and mortality… Here, we explore the potential impact of an
> ORV campaign conducted during the 2003–2004 measles epidemic in Niamey, Niger." (Grais 2008)

> "A novel human coronavirus… was identified in China in December 2019. There is limited
> support for many of its key epidemiologic features, including the incubation period…, which
> has important implications for surveillance and control activities." (Lauer 2020)

> "Although vaccination has almost eliminated measles in parts of the world, the disease
> remains a major killer in some high birth rate countries of the Sahel. On the basis of measles
> dynamics for industrialized countries, high birth rate regions should experience regular annual
> epidemics. Here, however, we show that measles epidemics in Niger are highly episodic." (Ferrari 2008)

> "Isolation of cases and contact tracing is used to control outbreaks of infectious diseases…
> Whether this strategy will achieve control depends on characteristics of both the pathogen and
> the response. Here we use a mathematical model to assess if…" (Hellewell 2020)

The hardest opening to argue with is the **expectation-violation** (Ferrari 2008, Earn 2000): derive what
the canonical theory predicts for your system, then show the data refuse it. Use it whenever
you can.

---

## 2. Methodology conventions

### 2.1 How much mathematics, and where

Across the corpus the depth of mathematics tracks the venue, not the complexity of the
model: **the main text carries the argument, not the algebra.**

- **General-science journals:** essentially no equations. Models are named and described
  ("a stochastic compartmental model stratified into 5-year age bands"; "variations on the
  susceptible–infectious–recovered (SIR) model"). Where symbols appear they are glossed in
  words on first use, and often *only* in a figure caption (Ferrari 2008, Earn 2000, Ferguson 2006, Ferguson 2005).
- **Methods and modelling journals:** displayed, numbered equations, referred to as
  "Equation (1)" or `(2.1)`. Build complexity in visible steps, one subsection per step —
  single interval score → weighted interval score; discrete → continuous (Bracher 2021a).
- **A compact model block beats prose** when the model is a generative chain. Abbott 2020 gives four
  lines (R_t process, renewal equation, delay convolution, negative binomial observation) and
  then glosses each line in a paragraph.
- **Give the analytic bound alongside the simulation** where one exists: "In theory, blanket
  prophylaxis … should be able to contain a pandemic with an R₀ of 1/[(1 − 0.6)(1 − 0.3)], or
  approximately 3.6" (Ferguson 2005). It makes the simulation auditable.
- **Always re-express notation epidemiologically.** Never leave a β unexplained in biological
  terms: "where β_quartier is the transmission rate between children within the same quartier"
  (Grais 2008).

Worked model-definition passages at all three levels of formality are in examples.md §12.1.

Reserve full formal treatment for **the one object that carries the argument** — the scoring
rule in Reich 2019 and Bracher 2021a, the elasticity and EVPI formulas in Li 2017, the coupling derivation in
Keeling & Rohani 2002. Everything else is named and cited.

### 2.2 Assumptions

Flat declarative sentences, in Methods, each with a reason or a source:

> "Once infected, the infectious process is assumed to be deterministic; children are infected
> but not infectious (latent) for 10 days and infectious for 6 days." (Grais 2008)
> "We assumed that exposure always preceded symptom onset." (Lauer 2020)
> "We assumed the outbreak started with a single infectious case on Nov 22, 2019." (Kucharski 2020)
> "For analytical tractability, we model a single generation of infection." (Nouvellet 2015)
> "We assume that 50% (see Supplementary Information for sensitivity analysis) of those infected
> are ill enough to be classified as clinical cases." (Ferguson 2006)

Three rules:

1. **State the assumption, then the justification, then the pointer to where it is tested** —
   often all in one sentence, as in Ferguson 2006.
2. **State the direction of the bias**, not merely its existence. "Relaxing these assumptions
   would decrease the probability that control is achieved" (Hellewell 2020). "If the true delay … is
   shorter than our global delay, then we will overestimate onset case numbers, and vice versa"
   (Abbott 2020). The habit recurs across archetypes (also Gostic 2020, Lauer 2020).
3. **Claim conservatism only when you can defend it**, and then repeat the word deliberately
   (Lauer 2020, Ferguson 2005). Optimistic assumptions plus a pessimistic conclusion is a strong argument;
   say so explicitly.

Worked assumption-with-direction-of-bias: examples.md §12.4.

### 2.3 Parameters and priors

- Give the distribution, both moments, and the source: "The incubation period was assumed to be
  Erlang distributed with mean 5·2 days (SD 3·7)" (Kucharski 2020).
- Justify distributional choice biologically, then test alternatives in an appendix:
  "we assumed that the incubation time follows a log-normal distribution, as seen in other acute
  respiratory viral infections" (Lauer 2020).
- **Label every parameter as sampled or fixed** in the parameter table (Hellewell 2020). This one column
  tells the reader exactly where uncertainty is propagated. A template is examples.md §12.12.
- Synthesise rather than assert: R₀ "derived from a meta-analysis of studies and preprints
  published before Feb 26, 2020" (Davies 2020).
- **When you change a prior, report the old one and why**: "This contrasts with our earlier
  approach which was to use a gamma prior with a mean of 2.6 and standard deviation 2" (Abbott 2020).
- State priors operationally where that is clearer than the parameterisation: "an inverse gamma
  prior with shape and scale values optimised to give a distribution with 98% of the density
  between 2 days and 21 days" (Abbott 2020).
- Give MCMC detail in full: chains, warmup, samples, and the convergence diagnostic (Abbott 2020).
- Where a parameter is unknowable, say so and route around it: "The natural history of any
  H5-based pandemic strain will not be known until it emerges, so we used parameter estimates
  for current human influenza subtypes, and used sensitivity analyses to investigate what effect
  deviation from these estimates would have on policy effectiveness" (Ferguson 2005).

A full worked Bayesian-fit methods paragraph — observation model, priors with justification,
sampler settings, diagnostics, software versions — is examples.md §12.8.

### 2.4 Scenarios

- **Declare a baseline scenario and vary one thing at a time from it.** "We present results in
  relation to the baseline scenario of R₀ of 2·5, 20 initial cases, a short delay to isolation,
  15% of transmission before symptom onset, and 0% subclinical infection" (Hellewell 2020).
- **Enumerate the grid exhaustively in Methods** before any result appears (Grais 2008, Hellewell 2020).
- **Define scenarios in a table as percentage changes to contacts by setting** for NPI work —
  school closure → school contacts 0%, home contacts 100% (Davies 2020). This table is the most
  reusable artefact in an intervention paper; a template is examples.md §12.13.
- **Letter- or name-code your scenarios and never renumber them** (Lee 2010: scenarios A–G ordered
  by increasing non-linearity, then used to index every table, figure and sentence).
- **Sweep effect sizes rather than picking one**, so conclusions can be stated as thresholds:
  10–100% in 10% increments (Li 2017); "optimal in 22 of 37 models if the effect is over 30%".
- **Present every result under two or more labelled scenarios** where the key parameter is
  genuinely uncertain, so readers can locate their own risk tolerance (Ferguson 2006: R₀ = 1.7 and 2.0).

### 2.5 Sensitivity analysis

Report it, and report **its conclusion in the same sentence**:

> "As a sensitivity analysis, we also ran model projections with a seasonal component such that
> transmission is 20% higher in winter than in summer, but this did not qualitatively affect our
> results (fig. S24 and table S5)." (Davies 2021)

Name each sensitivity analysis by what was varied, not by number: fever-only onset, mainland vs.
outside China, alternative distributions, alternative exposure lower bound (Lauer 2020). Where several
were run, summarise by conclusion rather than by table: they "produced the same conclusion about
decline in transmission" (Kucharski 2020).

Design a **targeted secondary analysis** to kill a specific alternative explanation — a
regression with fixed effects isolating the effect of data revision (Reich 2019); an explicit test that
variant growth is not a testing artifact (Davies 2021).

### 2.6 Software and computation

Name the language, the version, the packages, and the versions of the packages:

> "coarseDataTools and activemonitr packages in the R statistical programming language, version
> 3.6.2" (Lauer 2020)
> `rpart`, `ipred`, `randomForest` and `twang` with R 2.6.1, each package named where its method is described (Lee 2010)
> "the EpiNow2 R package (version 1.2.1)" (Abbott 2020)

Pin the data too: "All scores were based on ‘ground truth’ values of wILI data obtained as of September 27, 2017" (Reich 2019); data pulled
through a versioned API so the analysis is re-runnable. Generating the manuscript itself from
code (Sweave/knitr, Reich 2019) means text and numbers cannot diverge.

---

## 3. Results storytelling

### 3.1 Uncertainty: pick the right interval and label it

Use the interval that matches the object, and keep the kinds distinct within a paper:

| Object | Interval | Example |
|---|---|---|
| Frequentist estimate | 95% CI | "5.1 days (95% CI, 4.5 to 5.8 days)" (Lauer 2020) |
| Bayesian posterior | 95% CrI / BCI | "odds ratio, 0.92; 95% credible interval (CrI), 0.77 to 1.10" (Davies 2021) |
| Simulated future | 95% prediction interval | "350 000 deaths (170 000–480 000)" (Davies 2020) |
| Simulation ensemble | median [IQR] or median with 50%/95% intervals | "7.6% [4.9–8.9]" (Grais 2008); (Hellewell 2020) |
| Across-model spread | mean ± SD, or range across methods | "5,615 ± 2,705 (SD)" (Li 2017); "43 to 90% (range of 95% credible intervals, 38 to 130%)" (Davies 2021) |

Formatting conventions worth adopting: one decimal place for days; "to" rather than an en dash
inside a CI in clinical journals; drop the "95% CI" label after first use in a paragraph
(Kucharski 2020); report the median rather than the mean for skewed simulation output.

**Report the policy-relevant quantile, not the mean.** The 97.5th percentile of the incubation
period sets a quarantine window, so it leads (Lauer 2020).

**Translate to natural frequencies** when the number is small: "101 out of every 10 000 cases
(99th percentile, 482) will develop symptoms after 14 days" (Lauer 2020).

**Where the result is a null, say so with an interval that spans both directions:**
"Our estimates of severity are uncertain and are consistent with anything from a moderate
decrease to a moderate increase" (Davies 2021).

Weak-to-strong repairs for results sentences are worked in examples.md §12.5.

### 3.2 Give every number a comparator

The headline claims collected here are all anchored to something; none rests on "good" or
"large" alone:

- to a **naïve baseline**, glossed in plain English: "a relative WIS of 0.61, which can be
  interpreted as achieving, on average, 39% less probabilistic error than the baseline forecast"
  (Cramer 2022); "the largest improvement upon baseline predictions (0.17)" (Reich 2019);
- to a **capacity constraint**: "roughly 13–80 times ICU capacity in the UK, which we tallied at
  4562 beds" (Davies 2020);
- to a **named reference scenario**: "reduced total COVID-19 deaths by 58% (95% PI 30–80)
  relative to the intensive interventions scenario" (Davies 2020);
- to a **canonical system**: "fourfold that of historical London"; "over an order of magnitude
  higher than predicted from classical studies" (Ferrari 2008);
- to a **historical epidemic**: 2009 H1N1 "took 132 days to reach the same number of cities in
  China" (Tian 2020).

### 3.3 Sentence shapes that recur

**The gradient in one sentence.** "up to 38, 27 and 20% of cases averted for campaigns at 60, 90
and 120 days from the start of the epidemic, respectively" (Grais 2008).

**Intervention → what it moves → what it does not move → the condition.** "School closure during
the peak of a pandemic can reduce peak attack rates by up to 40%, but has little impact on
overall attack rates, whereas case isolation or household quarantine could have a significant
impact, if feasible" (Ferguson 2006). The "but only if…" clause is present in nearly every claim in the
policy papers, and it is what makes them credible.

**Verdict → "however" → the numbers.** "All methods displayed generally acceptable performance
under conditions of either non-linearity or non-additivity alone. However, under conditions of
both moderate non-additivity and moderate non-linearity, logistic regression had subpar
performance…" (Lee 2010).

**The concessive inside the headline claim.** "The COVIDhub-ensemble was the only model that
ranked in the top half … for more than 75% of the observations it forecasted, although it made
the single best forecast less frequently than any other model" (Cramer 2022).

**Unexpected result plus its mechanism, in the same sentence.** "the effect of isolation was
coupled with the chance of stochastic extinction resulting from overdispersion, which is why
some outbreaks were controlled even at 0% contacts traced" (Hellewell 2020).

### 3.4 Grade your verbs and modals to your evidence

- Design-appropriate verbs: interventions are **"associated with"** outcomes in observational
  designs; the model **"suggests"**; the response **"appears to have"** delayed growth (Tian 2020).
- Counterfactual modals graded by how hypothetical the premise is: *would have* (under stated
  assumptions) → *could have* → *might have* (under a hypothetical technology) (Nouvellet 2015).
- Within a single sentence: "is found to be invariant … also appears to be constant" (Bjørnstad 2002)
  — two evidential strengths, no separate hedging clause.
- Claim **qualitative** agreement when that is what you have. "The model supports our dynamical
  hypothesis, capturing the qualitative pattern of episodic outbreaks" (Ferrari 2008) is more persuasive
  than overclaiming fit.

**Never write "biased" without saying which way.** A direction is actionable; a bare claim of bias
is not. Give the condition, the direction, and where possible the magnitude and the timing:

> "If the mean generation interval is set too high, R_t values will typically be further from 1
> than the true value—too high when R_t>1 and too low when R_t<1." (Gostic 2020)
> "ignoring right truncation for a fast-growing epidemic with relatively long delays could result
> in underestimation of the mean delay distribution by up to 50%" (Charniga 2024)
> "The bias was greatest early in the epidemic." (Charniga 2024)

This applies to your own estimates, to your assumptions (§2.2), and to any method you criticise.

### 3.5 Report your own failures in the Results

Reporting your own model's failures, in the Results:

> "the model did not predict the slowdown in cases that was observed in early February." (Kucharski 2020)
> "In some of the selected waves (e.g., North Dakota and Florida), the ensemble forecast showed
> inappropriate levels of uncertainty, with the 95% PIs covering the eventual observations less
> than 80% of the time." (Cramer 2022)

Put these in Results, not buried in Discussion.

### 3.6 Figures and tables

**Which display items, and where.** ◆ Main-text slots are scarce (≤5 in the *Lancet*
family, ≤6 in *Nature* — journal instructions, so verify them), so decide the split before
drafting:

- **Main text** carries one item per headline claim, plus the parameter table (examples.md §12.12) and,
  for intervention papers, the scenario table (examples.md §12.13). ◆ A workable default
  allocation, not a figure census of the corpus: one *model fit or validation* figure (data
  overlaid on simulation), one *headline result* figure (the estimate, threshold, ranking or
  projection), and one *what governs it* figure (sensitivity or mechanism). A schematic of the
  model structure is worth a slot only when the structure is the contribution or unfamiliar
  (Weitz 2015, Li 2017).
- **Supplementary material** carries the full equations if the journal does not want them in
  Methods (§2.1), every sensitivity analysis not summarised in a main figure, convergence
  diagnostics, per-region or per-model breakdowns, and the completed reporting checklist.
  Reference each supplementary item from the exact sentence it supports; a supplement that
  is never cited in the main text is not evidence.
- **Figure or table?** A table when the reader will look up a value or compare across a
  labelled set of scenarios or models (Cramer 2022, Davies 2020); a figure when the shape — a trajectory, a
  threshold, a distribution — is the finding. Never both for the same numbers.

**Captions.** A caption must let the figure be read without the text: what is plotted (and
what the interval or band is — §3.1), under which scenario or parameter values (Earn 2000), and
what the reader should see. ◆ Start with a declarative sentence where the journal allows it — illustrative shape, not a
corpus quotation: *Contact tracing controls most outbreaks when R₀ = 1.5 but few when
R₀ = 3.5* — then the panel-by-panel key.

**Design rules.** Those attributed to a paper are the corpus's; those marked ◆ are general
practice:

- Overlay observed data on simulated trajectories so validation is visual and immediate (Grais 2008).
- Put the fixed parameter values in the caption of the figure they generated (Earn 2000).
- Use boxplots over replicates to argue about **dispersion**, not just central tendency (Lee 2010).
- Build **pedagogical figures** for methods papers: show the object, then walk the reader through
  it line by line (Bracher 2021a).
- Mark the boundary between estimates and estimates-from-partial-data in every real-time figure
  (Abbott 2020).
- Show a bifurcation diagram with your system's parameters *and* the canonical system's marked on
  the same axis (Ferrari 2008, Earn 2000).
- Put the baseline or reference scenario in every panel so each comparison is visible without
  flipping between panels (Hellewell 2020, Davies 2020).
- ◆ Use one colour or line style per scenario or model *across the whole paper*, keyed to the
  scenario labels (examples.md §12.13), and do not reassign it between figures.
- ◆ Log-scale the y-axis for growth-phase incidence and say so in the caption; linear for
  cumulative or peak quantities readers will want to compare in absolute terms.
- ◆ Label axes with the quantity and its unit, not the variable name (*Daily reported cases*,
  not *I(t)*).
- ◆ **Tables**: one row per scenario or model, one column per outcome, the baseline row first,
  intervals in the same cell as the point estimate — `2,340 (95% CrI 1,810–2,910)` — and the
  unit in the column header. Round to the precision the data support; a table full of
  four-significant-figure posterior medians overstates what the model knows.

---

## 4. Literature integration

### 4.1 Density

Numbered citations throughout the corpus; author-year only in the ecology journals. Density
varies by archetype, and is a deliberate choice:

- General-science policy papers: sparse, ~1 per 300–350 words (Ferguson 2006).
- Empirical modelling papers: moderate, ~1 per 85–160 words (Reich 2019, Kucharski 2020).
- Dynamical-systems papers: dense, with clusters of 3–5 references carrying a whole body of work
  in one sentence (Ferrari 2008).
- Reviews: ~150+ references; most sentences 1–2, synthesis paragraphs 5–8 (Baker 2021).

Concentrate citations in the Introduction and where parameters are justified. Methods sections
cite sources of parameters and of methods, and little else.

### 4.2 How to state the gap

Never "little is known about X", nor its disguises ("estimates remain scarce", "evidence is
limited", "remains poorly understood"). State a **checkable claim**:

> "We identified no estimates of how R0 had changed in Wuhan since control measures were
> introduced in late January or estimates that jointly fitted data within Wuhan to international
> exported cases and evacuation flights." (Kucharski 2020)
> "While multimodel comparisons exist in the literature for single-outbreak performance, here we
> compare a consistent set of models over seven influenza seasons." (Reich 2019)
> "Yet, the implications of post-death transmission for inferences about epidemic spread have not
> been evaluated systematically." (Weitz 2015)
> "the effectiveness of travel restrictions and social distancing measures in preventing the
> spread of infection is uncertain." (Tian 2020)

More weak-to-strong gap statements are worked in examples.md §12.3; a worked positioning paragraph is examples.md §12.7.

### 4.3 Seven ways to position against prior work

1. **Adjudicate a disagreement.** "Some previous studies suggest that reactive vaccination will
   not stop epidemics…; other analyses, however, point to the potential benefits…" (Grais 2008)
2. **Claim rigour, not novelty.** "Our results are broadly consistent with other estimates…
   Our analysis … made more conservative assumptions…" (Lauer 2020)
3. **Displace the received view without demolishing it.** "Until now, Ebola outbreaks were
   thought to be easily controlled. The usual narratives … highlight the importance of safe
   funerals, prompt isolation and effective contact tracing. However, testing strategies can also
   have a crucial role…" (Nouvellet 2015)
4. **Attack the incumbent by its consequence.** "These hypotheses suggest that it should be
   difficult or impossible to predict the timing and nature of specific transitions… Here, we give
   an alternative explanation…" (Earn 2000)
5. **Show correct work misapplied.** "the standard SIR model parameterized on observations from
   industrialized countries predicts highly persistent, annual dynamics… However, the following
   analysis … reveals starkly contrasting patterns to such extrapolations." (Ferrari 2008)
6. **Diagnose non-adoption rather than non-existence.** "The suggestion to use such algorithms …
   is not new. However, these methods have not been widely applied … perhaps because of the
   'black box' nature of some of the algorithms…" (Lee 2010)
7. **Claim a different audience and format, not new knowledge.** "Our paper goes beyond the work
   of Park and colleagues by offering practical guidelines, a suggested workflow, and checklists,
   for a broader technical audience, such as modelers at public health agencies." (Charniga 2024) Use this
   when the problem is diffusion of good practice rather than its absence — and describe the
   field as improving rather than deficient: "Methods for estimating epidemiological delays have
   been improving, especially during the COVID-19 pandemic…" (Charniga 2024).

### 4.4 Other integration habits

- **Anchor plausibility to relatives of the pathogen**: SARS and MERS incubation periods cited so
  a new estimate can be judged (Lauer 2020).
- **Use a historical epidemic as a mechanistic analogy**, with the mechanism spelled out: SARS was
  controllable "because the majority of transmission occurred after symptom onset" (Hellewell 2020).
- **Quantify the field's own growth** rather than asserting it: "the number of published research
  articles on forecasting infectious diseases has tripled (Web of Science)" (Reich 2019).
- **Turn the literature review into a table** when the field is decades old (Heesterbeek 2015, Table 1;
  Reich 2019, Table 1 of models with binary feature flags).
- **Cite preprints without apology** in fast-moving situations, dated (Davies 2020).
- **In reviews, do not adjudicate.** "However the role of urbanization in vector-borne disease
  spread is complex: …. Nevertheless, …" (Baker 2021).

---

## 5. Voice and tone

### 5.1 Person and tense

- **First-person plural, always.** "We developed", "We estimated", "We assumed", "we find".
  Never "I", rarely "the authors". Passive voice is reserved for the evaluation protocol, where
  it reads as impartiality ("forecasts are evaluated for accuracy at the end of the season",
  Reich 2019), and for data provenance.
- **Tense:** present for biological facts, model structure and standing implications; past for
  what was done and observed. "The model tracks 66·4 million people" (present) but "We ran 200
  stochastic simulations" (past). Dynamical-systems papers use present throughout, including for
  the authors' own actions (Earn 2000).

### 5.2 Hedging that carries information

Hedge the **inference**, not the number. The hedges in the passages collected here all name
what is uncertain; none is the contentless kind ("may possibly suggest"):

> "COVID-19 transmission probably declined in Wuhan during late January, 2020." (Kucharski 2020)
> "unlikely to delay spread by more than 2–3 weeks unless more than 99% effective" (Ferguson 2006)
> "only suggestive of potential trends" (Grais 2008)
> "The most parsimonious explanation … is that people infected with VOC 202012/01 are more
> infectious …, although there is also reasonable support for a longer infectious period and
> multiple mechanisms may be operating." (Davies 2021)

Hedge decisions rather than estimates when writing for policy:

> "Although it is essential to weigh the costs of extending active monitoring or quarantine
> against the potential or perceived costs of failing to identify a symptomatic case, there may
> be high-risk scenarios … where it could be prudent to extend the period of active monitoring."
> (Lauer 2020)

**Concede the alternative in the same paragraph as your choice.** "We preferred to motivate the
score through central predictive intervals … However, when applying …, formulation (4) may seem
more natural" (Bracher 2021a). This construction does more for credibility than any amount of caution.

**Use scare quotes to flag terms you will not take at face value** — "big data", "historical
baseline" (Reich 2019) — and to mark deliberate coinages on first use — 'sparks', 'core', 'satellite'
(Grenfell 2001); 'true mass action' (Bjørnstad 2002).

### 5.3 Precision over vagueness

Replace every vague quantifier with a number, a date, or a name.

- Not "many countries" → "over 100 countries in every continent except Antarctica" (Abbott 2020).
- Not "a large dataset" → "1,791 submission files with 556,050 specific predictions" (Cramer 2022).
- Not "a range of cities" → "60 cities … from London (3.3 × 10⁶ inhabitants) to Teignmouth
  (10 500 inhabitants)" (Bjørnstad 2002).
- Not "recently" → "as of March 5, 2020" (Kucharski 2020).
- Not "informs policy" → "healthcare staffing needs, school closures, and allocation of medical
  supplies" (Cramer 2022).

Date everything. A paper that says "recently" is unreadable in three years; a paper that says
"23 January 2020" is readable forever.

---

## 6. Domain-specific conventions

### 6.1 The R₀ paragraph

When the audience may not be modellers, teach the control logic once, from first principles, and
let every later result be an instance of it. Ferguson 2005 does it in five sentences: definition →
threshold → control target (eliminate a proportion 1 − 1/R₀ of transmission) → an exhaustive
enumeration of the three intervention classes. That enumeration then structures the paper.

Distinguish **R₀ / R_t / R_e** and say which you mean. Define the instantaneous reproduction
number explicitly when you use it, and cite the definitional literature (Abbott 2020).

### 6.2 Validation, out-of-sample evidence and scoring

*For supervised learning specifically — train/test discipline, calibration, bias in training
data, appraisal criteria — see §7.*

The field's analogue of train/test discipline. Report:

- **Out-of-sample validation, stated as such**: "although it was parameterized on the basis of
  observations from 1986 to 2002 in Niamey, the metapopulation model predicts the qualitative
  pattern of regional persistence at the national scale from 2001 to 2005" (Ferrari 2008).
- **Prospectivity as a methodological claim**: forecasts were made in real time, teams could not
  refit, and the four post-hoc bug fixes are documented rather than hidden (Reich 2019).
- **Independent validation of a fitted quantity**: an inferred infectiousness profile
  "remarkably consistent with viral shedding data from experimental infection studies" (Ferguson 2005).
- **Accuracy and calibration separately.** Accuracy = WIS or MAE; calibration = empirical
  coverage of prediction intervals. They are different virtues; never conflate them (Cramer 2022).
- **Proper scoring rules**, named, cited and interpreted for the reader; report on an
  interpretable scale (geometric mean of scores; relative WIS), not on the raw log scale (Reich 2019,
  Bracher 2021a).
- **Simulation benchmarks**: fix a metric set (bias, SE, coverage, balance) and report it in the
  same order in every table; use the off-the-shelf configuration and defend that as the realistic
  user's configuration (Lee 2010).
- **Model comparison**: rank competing structures on an explicit criterion (DIC) and **report the
  runners-up**, framing the winner as "the most parsimonious explanation" (Davies 2021).
- **Robustness as a vote count** across models: "optimal in 22 of 37 models" (Li 2017).
- **Report robustness to implementation failure as a co-equal outcome to effectiveness** —
  for an operational recommendation, a policy that degrades gracefully is worth more than one that
  is optimal under ideal delivery (Ferguson 2005).

A template data, code and funding-role statement is worked in examples.md §12.11.

### 6.3 Identifiability and the limits of inference

When parameters trade off, say so and make it the result:

> "We find a negative relationship between the estimated pre- and post-death transmission rate."
> "Despite this identifiability problem, we find robustly that…" (Weitz 2015)

Do not report a failed fit — report **what the data can and cannot determine**, then find the
conclusion that holds across the whole indeterminate set. Escalate the finding to the model
class: "This is a generic feature of epidemiological models" (Weitz 2015).

### 6.4 Decision relevance

- **Ask whether the disagreement matters.** Divergent projections are not automatically a
  problem; test whether they change the recommended action (Li 2017).
- **Price uncertainty in decision units.** EVPI/EVPXI turns "we need better data on X" into "9%
  of achievable case reduction, 82% of total EVPI" (Li 2017).
- **Attach a logistics or ethics checkpoint to every intervention you endorse**: "a household
  quarantine policy might pose ethical dilemmas unless excellent infection control was
  implemented" (Ferguson 2006).
- **Convert model requirements into a numbered operational checklist with target values** —
  the six containment criteria in Ferguson 2005.
- **Define a plain-language vocabulary for posterior probabilities, numerically, before use**:
  <5% subcritical → "definite" increase; >95% → "definite" decrease; 20–80% → "unsure" (Abbott 2020).
- **Say when the analysis was done and for whom**: "The results we present here summarise the key
  analyses and scenarios we presented to decision makers over February–March, 2020, which evolved
  continuously as new information became available" (Davies 2020).

### 6.5 Real-time and living analyses

- Report the **data-lock date** for every count.
- Demote forecasts relative to estimates explicitly: "These forecasts are indicative only and
  should not be considered with a weight equal to the real-time estimates" (Abbott 2020).
- Version the article alongside the software, with an `Amendments from Version N` changelog
  (Abbott 2020).
- Ship a tool, not just an estimate: a Shiny app (Lauer 2020), an interactive site (Reich 2019), an R package
  (Hellewell 2020), a spreadsheet and Java program that let readers vary assumptions (Nouvellet 2015).

### 6.6 Data, code and funding statements

Two statements worth matching:

> "All code and data are available at https://github.com/HopkinsIDD/ncov_incubation (release at
> time of submission at https://zenodo.org/record/3692048)." (Lauer 2020)
> "No data were used in this study. The R code for the work is available at
> https://github.com/cmmid/ringbp." (Hellewell 2020)

Rules:
- **A GitHub link is not archival.** Pair every repository with a Zenodo (or equivalent) DOI
  pinned to the submitted version. Abbott 2020 separates *Development* from *Archived at the time of
  publication*, and lists each package with its role.
- Name the language and version; follow a reporting guideline where one exists and name it
  in Methods (Cramer 2022 follows EPIFORGE). Which one depends on the archetype:
  - **Any modelling study** — Bennett et al. 2012 (*BMC Med Res Methodol*) reporting guideline
    for infectious disease modelling; ISPOR-SMDM Modeling Good Research Practices (Caro et
    al. 2012) where the model informs a health-economic or policy decision.
  - **Forecasting** — EPIFORGE 2020.
  - **Agent- or individual-based models** — the ODD protocol (Grimm et al. 2020) for the model
    description, usually as a supplement.
  - **Economic evaluation / cost-effectiveness** — CHEERS 2022.
  - **Prediction models** — TRIPOD (TRIPOD+AI for machine learning); PROBAST for appraising
    them; CLAIM for imaging.
  - **Systematic reviews** — PRISMA 2020; PRISMA-ScR for scoping reviews.
  - **Observational data components** — STROBE (RECORD for routinely collected data), when the
    data-collection part of the paper is substantial enough to be reviewed on its own terms.
  Attach the completed checklist as a supplement; reviewers at *Lancet*, *BMJ* and *PLoS*
  journals will ask for it.
- Lancet-family funding boilerplate, worth reproducing anywhere: "The funder of the study had no
  role in study design, data collection, data analysis, data interpretation, or writing of the
  report. The corresponding author had full access to all the data in the study and had final
  responsibility for the decision to submit for publication." (Kucharski 2020)
- Disclose preprints and conflicts concretely (Lauer 2020, Reich 2019).
- Give per-author contributions, including who wrote the draft (Ferrari 2008, Abbott 2020).
- **Share the individual-level data where you can, de-identified**: "the data should be
  anonymized/de-identified to protect patient privacy according to local health data laws and
  regulations" (Charniga 2024). Line-list format, with everything needed to re-run the estimation.
- **Where raw data genuinely cannot be released, publish the minimum viable artefact** so
  downstream meta-analysis is still possible: "If data cannot be shared, we recommend at minimum
  providing samples of the posterior distribution in a permanent online repository…" (Charniga 2024).
- **Report the distribution, not just the point estimate** — central tendency, variability,
  credible intervals, and the contextual information needed to reuse the estimate (Charniga 2024).
- Where authors sit in government agencies, include the standard disclaimer: "The findings and
  conclusions in this report are those of the authors and do not necessarily represent the
  official position of the CDC … or the UK Department of Health and Social Care." (Charniga 2024)

---

## 7. Machine learning and predictive modelling conventions

For papers whose contribution is a fitted predictive model rather than a mechanistic one. The
corpus covers three ML sub-archetypes — risk mapping and trait-based prediction (Bhatt 2013,
Olival 2017, Han 2015), digital surveillance and nowcasting (Ginsberg 2009, Yang 2015), and
clinical prediction (Zoabi 2021, Lee 2010) — plus three appraisals of the field's failures
(Lazer 2014, Wynants 2020, Roberts 2021). Everything in §1–§6 still applies; this section adds
what is specific to learning from data.

### 7.1 Lead with the problem, not the algorithm

Most of the ML corpus opens on the problem, not the method. Bhatt 2013 opens "Dengue is a
systemic viral infection transmitted between humans by *Aedes* mosquitoes"; Han 2015 opens
"Forecasting reservoirs of zoonotic disease is a pressing public health priority." The algorithm
appears in one sentence, named and justified by a property of the *data*, never by novelty:

> "generalized boosted regressions… have particular use for comparative ecological studies
> because they accommodate multiple data types as covariates, nonrandom patterns of data
> missingness, and hidden, nonlinear interactions." (Han 2015)
> "our use of GAMs, an incorporation of smooth spline predictor functions into the generalized
> linear model (GLM) framework, allowed us to examine the functional form of our predictor
> variables." (Olival 2017)
> "Gradient boosting is widely considered state of the art in predicting tabular data." (Zoabi 2021)

**Never lead with the AUC either.** Bhatt's headline is 96 million infections, not 0.81.

The exception in the corpus is Lee 2010, which opens on the method — "Machine learning
techniques such as classification and regression trees (CART) have been suggested as promising
alternatives to logistic regression" — because the method *is* the subject: a simulation
benchmark's problem is a claim in the methodological literature, not a disease burden. Open on
the method only when you are evaluating methods.

A full worked supervised-learning methods paragraph is examples.md §12.9; a worked bias check is examples.md §12.10.

### 7.2 Structure Methods as the pipeline, in execution order

Bhatt 2013: *Assembly of the occurrence database and its quality control · Explanatory covariates ·
Predicting the probability of occurrence · Estimation of burden and populations at risk*.
Olival 2017: *Database · Phylogenetic signal · GAM fitting and selection · Model cross-validation ·
Data availability · Code availability*.

Each stage becomes independently auditable. This beats a generic Data/Model/Analysis split.

### 7.3 Train/test discipline — state it in one unambiguous sentence

> "Datasets were partitioned into training (80% of all 2,277 species) and test (the remaining
> 20%) sets before analysis." (Han 2015)
> "The final model was validated on 42 points per region of previously untested data from 2007 to
> 2008, **which were excluded from all previous steps**." (Ginsberg 2009)

The qualifying clauses — *before analysis*, *excluded from all previous steps* — are the whole
claim. Feature selection, tuning and threshold choice must all sit inside the training fold.

**Split along the axis you will extrapolate over:**
- **Temporally**, when the model will be used going forward. Zoabi 2021 trains on 22–31 March and tests
  on the *following week*; Yang 2015 uses a rolling two-year window "assuming we had access only to
  the historical CDC's ILI reports up to the previous week of estimation".
- **Geographically**, when the model will be applied to new places. Olival 2017 "systematically removed
  all species from 34 mammalian zoogeographic regions", refit, and tested the held-out region —
  then **hatched the failing regions on the published map**. Show where your model does not
  transfer.
- Random k-fold is the weakest of the three and is best used alongside one of the others.

Cross-validation is named with its purpose, not just performed: "10-fold cross-validation during
model building to prevent overfitting" (Han 2015).

### 7.4 Report performance honestly

- **Give uncertainty on the metric**, not a bare number: "AUC of 0.81 (±0.02 SD, n = 336)" (Bhatt 2013);
  "0.90 auROC… with 95% CI: 0.892–0.905", from "bootstrap percentile method with 1000
  repetitions" (Zoabi 2021).
- **Under class imbalance, report auPRC alongside auROC** (Zoabi 2021, 9.2% positive).
- **Give two named operating points** rather than one threshold: "87.30% sensitivity and 71.98%
  specificity, or 85.76% sensitivity and 79.18% specificity" (Zoabi 2021).
- **Every metric relative to a naive baseline**: "the number reported is the ratio of error of a
  given method to that of the naive method" (Yang 2015). Add one summary statistic with CIs — Yang 2015's
  relative efficiency lets the paper say "at least twice as efficient as any other alternative"
  instead of reciting five metrics.
- **Benchmark fairly, and say what you did to make it fair**: "For fair comparison, all benchmark
  models (ii–iv) are dynamically trained with a 2-y moving window" (Yang 2015).
- **Contextualise a modest fit rather than hiding it**: 27–49% deviance explained is "greater than
  or comparable to studies examining much narrower groups of mammal hosts" (Olival 2017).
- **Assess calibration, not just discrimination.** Its absence is one of the six recurring
  failings named by Wynants 2020: "Only five studies assessed calibration."
- Report the metric set in a fixed order across every table (Lee 2010).

### 7.5 Confront bias in the training data explicitly

The habit that most clearly separates the ML papers in this corpus from the ones Wynants 2020
and Roberts 2021 condemn.

- **Put sampling effort in the model as a covariate**, then report how much signal it absorbs:
  "research effort had the strongest effect on the total number of viruses per host, explaining
  31.9% of the total deviance" (Olival 2017).
- **Fit a model of your own sampling process and show it does not reproduce your result**: Han 2015
  models "studiedness" from citation counts, finds pseudo-R² of 0.07–0.17, and concludes "the
  trait patterns of well-studied rodents and those of rodent reservoirs are not coincident."
- **Retrain without the features you distrust and publish the cost**: "If we train and test our
  model while filtering out symptoms of high bias in advance, we obtain an auROC of 0.862"
  (Zoabi 2021) — against 0.90 with them.
- **Score data quality and re-run on the high-quality subset** (Olival 2017: detection method scored
  0–2, parallel stringent-data analysis).
- **Disclose a conservative labelling decision and its direction**: 2,061 unlabelled species
  "designated nonreservoirs… a more conservative designation… with baseline classification
  performance that can only improve with ongoing discoveries" (Han 2015).
- **Name the confound that could produce your outcome without the intended signal**: an imaging
  model "might associate more severe disease not with CXR imaging features, but the view that
  has been used to acquire that CXR" (Roberts 2021).
- **Turn an arbitrary modelling choice into an ensemble** instead of defending it: 336 BRT models
  spanning the pseudo-absence parameter space, reported as a mean with an SD (Bhatt 2013).

### 7.6 Interpretation is a result, not a garnish

- Variable importance **and** partial dependence together: "Marginal plots of the top 15 predictor
  variables… showing the marginal effect of each trait (shown in order of importance)" (Han 2015);
  partial effect plots with 95% bands (Olival 2017).
- **Unify the important variables into one interpretable concept** rather than listing them —
  Han 2015 collapses its top traits into a *fast-paced life history*.
- Define any explanation method in one plain sentence before using it: "Originating in game
  theory, SHAP values partition the prediction result of every sample into the contribution of
  each constituent feature value" (Zoabi 2021).
- **Report the covariate that did *not* matter**: "low precipitation was not found to strongly
  limit transmission" (Bhatt 2013).
- **State the confound-adjustment inside the claim sentence**: bats host more zoonoses "after
  controlling for reporting effort and other predictor variables" (Olival 2017).
- **Ship the predictions as a named, falsifiable list**: "we also identify 58 species predicted to be
  novel reservoirs and 159 species predicted to be novel hyperreservoirs" (Han 2015), supplied in
  full as a dataset. A predictive paper's proper conclusion is an experiment someone can run.

### 7.7 Say which numbers are ordinal

> "our estimates of missing viruses and missing zoonoses per species are based on the current
> maximum observed research effort from the literature, and these estimates should be viewed as
> relative, not absolute." (Olival 2017)

Localise uncertainty too: Bhatt 2013 names the countries where its burden estimates are least reliable
rather than issuing a blanket caveat.

### 7.8 What appraisers will mark you down for

Distilled from Wynants 2020 (PROBAST/CHARMS over 51 studies, all rated high or unclear risk of bias) and
Roberts 2021 (62 studies, none clinically usable). Treat as a pre-submission checklist:

- **Outcome leakage**: "one of the predictors (e.g., fever) was part of the outcome definition."
- **Excluding participants still in follow-up**, "yielding a highly selected study sample."
- **Case-control sampling reported as a cohort**, making prevalence unrepresentative.
- **Small samples with complex models** — "an increased risk of overfitting, particularly if
  complex modelling strategies were used." Roberts 2021 required "at least 20 events per variable" to
  score low risk of bias.
- **No calibration assessment.**
- **External validation on an unrepresentative dataset**, which is not external validation.
- **Bespoke architectures without benchmarking**: "Every study used a different deep learning
  architecture… without benchmarking the used architecture against others."
- **"Frankenstein datasets"** — "datasets assembled from other datasets and redistributed under a
  new name" (Roberts 2021), with duplicated or mislabelled sources.
- **No usable model artefact**: "Thirty one studies did not include any usable equation, format,
  or reference for use or validation of their prediction model" (Wynants 2020).
- **Purely data-driven predictor selection**: "we recommend building on previous literature and
  expert opinion to select predictors, rather than selecting predictors in a purely data driven
  way; this is especially important for datasets with limited sample size" (Wynants 2020).

Follow a reporting guideline and say so — TRIPOD (TRIPOD+AI) for prediction models, PROBAST
for appraisal, CLAIM/RQS for imaging, EPIFORGE for forecasting. The full list by archetype is
in §6.6.

### 7.9 The two failure modes that killed Google Flu Trends

From Lazer 2014, and both are structural rather than statistical:

**Big data hubris** — "the often implicit assumption that big data are a substitute for, rather
than a supplement to, traditional data collection and analysis." The arithmetic: "the methodology
was to find the best matches among 50 million search terms to fit 1152 data points. The odds of
finding search terms that match the propensity of the flu but are structurally unrelated, and so
do not predict the future, were quite high." Result: "part flu detector, part winter detector."

**Algorithm dynamics** — the data-generating process is a commercial product under continuous
modification: "In improving its service to customers, Google is also changing the data-generating
process." Any model built on a platform's output inherits that instability.

Three practical consequences:
1. **Beat a boring benchmark or don't publish the claim.** "Even 3-week-old CDC data do a better
   job of projecting current flu prevalence than GFT."
2. **If your feature selection surfaces nonsense predictors, that is evidence about the
   procedure.** Ginsberg 2009 disclosed that 'high school basketball' and 'oscar nominations' scored highly
   — and did not act on it. Lazer 2014: "This should have been a warning that the big data were
   overfitting the small number of cases."
3. **Build in recovery.** Yang 2015's advertised virtue is not accuracy but self-correction — rolling
   retraining, L1 reselection of terms, autoregressive structure — because the predecessor's fatal
   flaw was staying wrong for two years.

---

## 8. Discussion and limitations

### 8.1 Discussion shape

Open by naming what the work shows or the tension it exposes — **not** by restating the abstract:

> "This work illustrates the tension between the desire for long-term forecasts, which would be
> helpful for public-health practitioners, and the decline in forecast accuracy at longer horizons
> shown by all forecasting methods." (Cramer 2022)
> "The high seasonality of transmission in Niamey leads to more irregular measles dynamics than
> predictions that are based on historical data for industrialized countries… This emphasizes the
> potential dangers of extrapolating dynamics for these sorts of highly non-linear systems without
> a detailed understanding of local parameters." (Ferrari 2008)

Then: interpretation → comparison with prior estimates → limitations → what should change. For a
multi-dimensional result, a bulleted "We summarize the key findings of the work as follows"
list is legitimate and effective (Cramer 2022).

Close on one of: a decision ("Ultimately the decision whether or not to intervene … depend[s]
upon the political will of public health authorities", Grais 2008), a data-collection priority ("It will
be imperative to collect the most detailed data … early in the emergence of a pandemic, and to
analyse those data in real time", Ferguson 2006), or a research question. Not on a summary.

### 8.2 Limitations

Signpost with a plain opener — "There are limitations to our analysis"; "This analysis has
several important limitations"; "Our approach is also subject to several limitations" — then work
through them. Six categories, and the corpus's best framings for each:

1. **Simplification.** "Our models inevitably simplify the complex processes… However, they
   provide an important initial evaluation…" (Nouvellet 2015); "as with all models, ours simplifies reality
   in a number of respects" (Grais 2008).
2. **Data quality and provenance.** "Ground-truth data are not static. They can be later revised
   as more data become available" (Cramer 2022); "The length of stay in ICU … estimated using data from
   China, and differences in UK populations could affect our estimates" (Davies 2020).
3. **Contested parameters.** "the precise values of these parameters and the impact of school
   closures remain the subject of scientific debate" (Davies 2021).
4. **Design.** "This study has drawn inferences not from controlled experiments but from
   statistical and mathematical analyses… With that caveat, control measures were strongly
   associated with the containment of COVID-19" (Tian 2020); "We could not investigate the impact of
   all elements of the national emergency response because many were introduced simultaneously"
   (Tian 2020).
5. **Scope fences** — an explicit prohibition on a misreading you expect. "these results should
   not be used to extrapolate hypothetical accuracy in pandemic settings" (Reich 2019); "We have
   considered a small number of intervention and vaccination scenarios, which should not be
   regarded as the only available options for policy-makers" (Davies 2021); "it cannot speak to model
   performance for incident cases or hospitalizations" (Cramer 2022).
6. **Irreducible uncertainty**, distinguished from fixable gaps. "Lack of data prevent us from
   reliably modelling transmission in … residential institutions" (fixable) versus "it will be
   impossible to predict the exact characteristics of any future pandemic virus" (not) (Ferguson 2006).

Six rules for writing them:

- **Name the specific question the limitation prevents you answering**, not just "the model is a
  simplification": "Because the model does not explicitly structure individuals by household, we
  are unable to evaluate the impact of measures based on household contacts, such as household
  quarantine" (Davies 2020).
- **Discharge what you can**, by sensitivity analysis or by direction-of-bias argument, and say
  which limitations remain live.
- **Frame limitations as design choices where they were choices**: "In this study we used only
  the basic, off-the-shelf versions of each of the methods, since that is likely what most applied
  researchers would do" (Lee 2010); "we did not specifically consider the operational cost or
  constraints" (Li 2017).
- **Pre-empt misuse.** Explain why the tempting follow-up analysis would not be valid: an
  observational study of which model features improve accuracy "would be confounded by other
  factors about how the model was built and validated" (Cramer 2022).
- **Disclose how your evidence was selected.** If your examples are illustrative rather than
  systematically sampled, say so: "we did not aim to provide a systematic review; rather, we
  provided insights based on our experiences. The examples presented in this work were selected
  to illustrate specific points" (Charniga 2024). Most guidance and review papers omit this; including it
  costs nothing and forecloses a fair criticism.
- **Name the hard boundary** — the failure that no amount of method can fix: "Even the most
  powerful inferential methods, extant and proposed, will fail to estimate R_t accurately if
  changes in sampling are not known and accounted for" (Gostic 2020).

A weak-to-strong limitations paragraph is worked in examples.md §12.6.

A compact statement of modelling's epistemic limits, for use when arguing what a model can
and cannot do:

> "By definition and design, models are not reality. The properties of stochasticity and
> non-linearity strongly influence the accuracy of absolute predictions over long time horizons.
> Even if the mechanisms involved are broadly understood and relevant data are available,
> predicting the exact future course of an outbreak is impossible due to changes in conditions in
> response to the outbreak itself, and due to the many chance effects in play." (Heesterbeek 2015)

Immediately followed by the constructive turn: "The field has yet to explore where that horizon
is and whether computational tools and additional data … can stretch predictions to this limit."
**Always convert the limitation into the next research question in the following sentence.**

---

## 9. Best-practice and guidance papers

A distinct archetype with its own rules, exemplified by Gostic 2020 (Gostic et al. on R_t estimation)
and Charniga 2024 (Charniga et al. on delay distributions). The contribution is neither a new model nor a
new estimate: it is a diagnosis of how a method others already use goes wrong, plus recommendations.
Much of §1–§8 still applies, but the following overrides it.

### 9.1 Structure by problem or by task, not by IMRaD

Neither paper has `Methods`/`Results`/`Discussion`. Sections are **the problems a practitioner
hits, in the order they hit them** (Gostic 2020: *Generation interval misspecification · Adjusting for
delays · Adjusting for right truncation · Accounting for incomplete observation · Smoothing
windows*), or **the tasks in a workflow** (Charniga 2024: *Biases in delay data · Measuring epidemiological
delays · Adjusting for common biases · Reporting epidemiological delay distributions*).

**Write headings as imperatives where the section is an instruction**: *Fit multiple probability
distributions · Visualize the distributions · Correctly convert parameters · Add subgroups or
stratify estimates · Check model diagnostics* (Charniga 2024). An instruction heading is scannable,
quotable and impossible to misread.

### 9.2 Build the paper so the summaries alone are usable

Gostic 2020 ends **every substantive section with a bulleted `Summary` box**: "The Cori method most
accurately estimates the instantaneous reproductive number in real time. It uses only past data
and minimal parametric assumptions." A reader can extract the complete recommendation set from
the boxes; a reader who needs the argument reads the sections. Design for both.

Charniga 2024 goes further and makes **the checklist the deliverable** — Tables 2–3, in *item / details /
examples / solutions* columns, so a reader can work through their own manuscript against it.
Add a **decision flowchart that branches on what data the reader has** (Charniga 2024, Fig 3) rather than
prescribing one method for everyone.

### 9.3 Simulate the truth, then degrade the data one step at a time

Gostic 2020's evidential engine, and a template for evaluating any estimator:

1. Generate synthetic data from a known model (a deterministic or stochastic SEIR), so the true
   value of the target quantity is known by construction.
2. Test every method "under idealized conditions" first, where "all infections are observed
   instantaneously".
3. Then add **one real-world imperfection per section** — generation-interval misspecification,
   observation delays, right truncation, incomplete observation, smoothing — each in isolation.

Every section then answers one question of the form *"what does this specific data imperfection
do to the estimate, and by how much?"*, and the answer is checkable because the truth is known.

### 9.4 Quantify the cost of bad practice

Guidance is only persuasive if the error it prevents is sized. Charniga 2024 uses three registers, often
within a few sentences:

- a **worked before/after pair** on a familiar parameter: "the mean incubation period for
  COVID-19 in early 2020 … was 3.49 days without adjusting for right truncation compared to
  4.69 days when adjusted";
- a **worst-case magnitude**: "underestimation of the mean delay distribution by up to 50%";
- a **downstream consequence** for a quantity readers care about more: mis-specified generation
  intervals "led to biased estimates of R_t", with "The bias was greatest early in the epidemic."

Trace the error forward to the thing people actually use. "Knock-on impacts" (Charniga 2024) is the frame.

### 9.5 Prescriptive but not imperious

- **"We recommend" appears more than twenty times in Charniga 2024; "must" does not appear.** Authority
  comes from specificity and repetition, not modal force.
- **Say what you do not recommend, with a structural reason**: "In its current form, we do not
  recommend using the method of Bettencourt and Ribeiro, given that unrealistic structural
  assumptions lead to bias" (Gostic 2020). Only publishable because the synthetic-data design makes it
  demonstrable — but where you can support it, it is the recommendation readers act on.
- Hedge **applicability**, not confidence: "may not always be the case", "should be assessed on a
  case-by-case basis", "likely a better use of available data".
- State consequences in plain conditional form: "Not or incorrectly accounting for censoring of
  event intervals can lead to biased estimates of a delay" (Charniga 2024).

### 9.6 Other conventions of the archetype

- **Name methods after their authors** — "the Cori method", "the method of Wallinga and Teunis",
  "the method of Bettencourt and Ribeiro" (Gostic 2020). More readable than acronyms, and it attributes.
- **Run each method in its canonical implementation, named**: "obtained using the R package
  EpiEstim … by translating code from references into the Stan language" (Gostic 2020). Recommend tools
  by name with a basis: `coarseDataTools`, `epidist`, `EpiNow2`, `epitrix`, `epiparameter` (Charniga 2024).
- **Count a method's parametric assumptions** as part of comparing it: "The only parametric
  assumption required by this method is the form of the generation interval" (Gostic 2020).
- **Name a small closed set of problems** — censoring, right truncation, dynamical bias (Charniga 2024) —
  and organise every table, figure, recommendation and checklist row around that same set.
- **Trace a formalism to its origin before using it.** Gostic 2020 gives the renewal equation in its
  original demographic form, "where b(t) is the number of births at time t and n(a) is fecundity
  at age a", then re-expresses it epidemiologically. Showing provenance exposes assumptions.
- **Set up a conceptual distinction early and police it throughout**: instantaneous vs. case
  reproductive number, "intrinsic" vs. observed generation interval (Gostic 2020); forward vs. backward
  cohort approaches (Charniga 2024) — the latter yielding the paper's strongest single recommendation,
  "We recommend always analyzing delay distributions as forward distributions."
- **Split derivation from guidance across two papers, and say so**: "Technical details about these
  biases and how to adjust for them can be found in Park and colleagues" (Charniga 2024). Both stay readable.
- **Distribute limitations** through the sections rather than isolating them, and gather the
  residue in the conclusions — including the hard boundary no method can fix (§8.2).
- Write both the Abstract and the Author Summary at different levels: Gostic 2020's Author Summary
  defines R_t from scratch ("whether an epidemic is growing, shrinking, or holding steady") where
  the Abstract assumes it.
