---
name: modelling-paper-writer
description: Write, structure, or revise infectious disease mathematical and statistical modelling papers in the style of the field's best-written work. Use when drafting or editing any section of a modelling manuscript (abstract, introduction, methods, results, discussion, limitations, data/code availability), when choosing how to report estimates and uncertainty, when positioning work against prior literature, or when the user asks for help with an epidemiological modelling paper, preprint, or report. Covers transmission models, forecasting and forecast evaluation, parameter estimation, intervention and scenario analysis, decision analysis, reviews, best-practice guidance or reporting-standard papers, and machine learning / predictive modelling papers (risk mapping, digital surveillance, clinical prediction). Includes worked examples for model definitions, abstracts, methods, results, limitations and availability statements. Not for empirical or observational studies without a modelling component.
---

# Writing infectious disease modelling papers

*Developed by James Azam (https://github.com/jamesmbaazam). Licensed MIT.*

This skill distils the writing style of 37 well-written infectious disease modelling,
statistical and machine learning papers, from *Nature*, *Science*, *PNAS*, the *Lancet*
family, *BMJ*, *Nature Machine Intelligence*, *npj Digital Medicine*, *PLoS Computational
Biology*, *Statistics in Medicine*, *Ecology Letters*, *Ecological Monographs*, *Annals of
Internal Medicine*, *J. R. Soc. Interface* and *Wellcome Open Research*, spanning 2000–2024.
They cover COVID-19 (11 of 37), influenza, measles, dengue, Ebola, foot-and-mouth and
zoonotic spillover. The corpus is landmark, highly cited work from a narrow set of research
groups, chosen for writing quality rather than sampled systematically; conventions derived
from the 2000–2008 papers may predate current reviewer expectations. Per-paper analyses with verbatim quotations live in
`writing_styles/`; `writing_styles/papers.csv` indexes them with title, DOI, authors and
methodological type (see also the index at the end of this file).

Use it to draft, restructure or revise. When a specific paper in `writing_styles/` matches
the manuscript's archetype, read that file too — it has the sentence-level detail.

## Hard rules

These override everything below.

- **Never invent a citation, DOI or author.** Use `[ref]` or `[Author YEAR]` placeholders and
  list, at the end, every claim that still needs a source.
- **Never invent a number.** If the user has not supplied a result, write a placeholder in the
  shape the sentence needs — `[X% (95% CrI [a–b])]` — not a plausible value.
- **Never reuse corpus sentences verbatim** in the user's manuscript. The quotations in this
  file and in `writing_styles/` show the *move*; write the user's version of it.
- **In revision mode, preserve the author's voice**, spelling variant (UK/US) and tense.
  Show edits (before/after or tracked-change style) rather than silently rewriting, and do
  not expand beyond the section you were asked to touch.
- **Journal typography is not a style rule.** Middle-dot decimals (`2·5`) and "to" instead of
  an en dash in intervals are *Lancet* house style, reproduced here in quotations from Lancet
  papers; use ordinary decimal points and en dashes unless the target journal says otherwise.

**§12 holds worked example passages** for every convention below — how to define an SIR or SEIR
model at three levels of formality, an annotated abstract, before/after repairs for gap
statements, results sentences and limitations, and template methods and availability sections.

---

## 0. First decide the archetype

Almost every choice below follows from what kind of paper this is. Identify the archetype
before writing a word; the corpus contains fourteen, each with a canonical exemplar.

| Archetype | What it delivers | Exemplars |
|---|---|---|
| **Parameter estimation** | One well-defined quantity, cleanly estimated, translated into a decision | `07` Lauer (incubation period) |
| **Real-time transmission analysis** | R_t or transmission dynamics fitted to a live outbreak | `19` Kucharski, `26` Abbott, `16` Tian, `03` Keeling (abstract only) |
| **Scenario projection for policy** | A ladder of intervention scenarios, projected forward | `25` Davies (UK NPIs), `12` Ferguson (mitigation) |
| **Feasibility / threshold** | The parameter boundary at which a strategy works | `13` Ferguson (containment), `22` Hellewell (contact tracing) |
| **Policy counterfactual** | What a past intervention achieved, and what alternatives would have | `01` Grais, `20` Nouvellet |
| **Competing hypotheses** | Several mechanisms formalised, fitted and ranked | `24` Davies (B.1.1.7) |
| **Forecast evaluation** | Many models, one scoring rule, a verdict | `09` Cramer, `10` Reich, `11` Bracher |
| **Dynamical systems** | A system shown to sit in a different regime than assumed | `02` Ferrari, `04` Earn, `18` Bjørnstad, `17` Grenfell |
| **Methods / simulation benchmark / critique** | A tool, a validation, or a demonstration of what cannot be inferred | `08` Lee, `11` Bracher, `06` Keeling & Rohani, `21` Weitz, `23` Li |
| **Review** | A framework that organises a scattered literature | `14` Baker, `15` Heesterbeek, `05` Altizer |
| **Best-practice guidance** | Recommendations, checklists or reporting standards for a method others already use | `27` Gostic (R_t), `28` Charniga (delay distributions) |
| **Risk mapping / trait prediction** | A supervised model over covariates or traits, producing a surface or a ranked candidate list | `29` Bhatt (dengue), `32` Olival (spillover), `33` Han (rodents) |
| **Digital surveillance / nowcasting** | An estimate of a surveillance quantity, faster than surveillance | `30` Ginsberg (Google Flu Trends), `34` Yang (ARGO) |
| **Clinical prediction model** | A patient-level classifier with an intended point of care | `37` Zoabi (COVID symptoms) |
| **Critique / appraisal** | A verdict on a method or a whole literature, plus named failure modes | `31` Lazer, `35` Wynants, `36` Roberts |

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

### 1.1 The universal spine

Every paper in the corpus, whatever its journal, is built on the same six moves. Journal
format only changes where the moves live.

1. **Burden or urgency**, quantified and dated.
2. **The specific gap** — a quantity that is missing, a strategy whose effect is unknown, an
   expectation that the data violate.
3. **"Here, we…"** — one sentence naming the model class and the data.
4. **The headline result**, with its uncertainty, in the abstract. Never withhold it.
5. **The condition or caveat that bounds the result.**
6. **What should now change** — a decision, a data collection priority, or a research question.

An annotated abstract built on these six moves is worked in §12.2.

### 1.2 Journal templates

**Nature / Science (Articles, Reports).** No `Introduction`/`Results` headings. A dense
one-paragraph abstract, then continuous text broken by **short topic subheadings**
(`Seasonality and dynamics in Niamey`; `Modelling pandemic spread`; `Measuring the new
variant's growth rate`). Methods compressed at the end or absent; everything else in the
Supplementary Information, referenced inline. Science adds a structured editor's abstract
(`INTRODUCTION`/`RATIONALE`/`RESULTS`/`CONCLUSION`) and a summary box.
→ `02`, `04`, `12`, `13`, `16`, `17`, `20`, `24`

**PNAS.** `Significance` (≤120 words, plain language) → Abstract → Introduction →
**Results** → Discussion → **Materials and Methods last**. Results subheadings are
**claims, not topics**: *Model Accuracy Rankings Are Highly Variable*; *Forecast Performance
Degrades with Increasing Horizons*. Methods subheadings are the decisions a critic would
challenge: *Forecast Model Eligibility and Evaluation Period*.
→ `09`, `10`, `23`

**Lancet family.** Structured abstract (**Background / Methods / Findings / Interpretation /
Funding**) → **`Research in context`** panel (*Evidence before this study* / *Added value of
this study* / *Implications of all the available evidence*) → Introduction → Methods (with a
mandatory *Role of the funding source*) → Results → Discussion → Data sharing → Contributors
→ Declaration of interests.
→ `19`, `22`, `25`

*Write the `Research in context` panel first even when the journal does not require it.* Three
short paragraphs — what was known, what you added, what should change — will discipline the
whole manuscript.

**PLoS / methods journals.** Numbered sections and subsections (`2.1`, `2.2`) are appropriate
and normal when the contribution is methodological. PLoS also wants an **Author Summary**
written for the practitioner alongside the technical abstract.
→ `11`

**Royal Society journals (*J R Soc Interface*, *Proc B*).** Conventional IMRaD with
unnumbered subsections; the Methods can carry the full model specification in the main text.
→ `01`

**Clinical journals (Annals, etc.).** Fully labelled abstract including a mandated
single-sentence **`Limitation:`** field, plus a **Reproducible Research Statement**.
→ `07`

**Open/living formats (Wellcome Open Research).** Versioned article with an explicit
**`Amendments from Version N`** changelog, and separate `Data availability` and `Software
availability` sections, the latter split into *Development* and *Archived at time of
publication*.
→ `26`

### 1.3 Subheading craft

- **Mirror Methods and Results subheadings** when the paper has parallel analyses, so each can
  be read alone (`20` Nouvellet: *Potential impact of RDTs in a health-care unit* appears in
  both).
- **Make Results subheadings declarative** where the journal allows — read in sequence they
  should be the paper's argument (`09`, `21`).
- **Give a pre-empted objection its own heading.** `24` Davies has a Methods subsection titled
  *"Apparent growth of VOC 202012/01 not a result of testing artifacts"* — the most obvious
  alternative explanation is refuted where a sceptic will look for it.
- **Give a known bias its own Methods subsection** when it governs how output must be read
  (`26`: *The effect of changes in testing procedure*).
- **Define your outcome formally under its own heading** when it is binary
  (`22`: *Definition of outbreak control*).

### 1.4 Introduction shape

Four to six paragraphs; five moves:

1. The pathogen or system, with burden quantified and dated.
2. What is established — cited compactly, several references per sentence.
3. What follows from that, stated precisely enough to be contradicted.
4. The gap, stated as a checkable claim about the literature, not as "little is known".
5. The question, often as an explicit list ("Three key questions arose…", `01`), which
   Results and Discussion then answer in order.

Openings from the corpus, all following the same beat:

> "The current World Health Organization recommendations for response during measles epidemics
> focus on case management rather than outbreak response vaccination (ORV) campaigns, which may
> occur too late to impact morbidity and mortality… Here, we explore the potential impact of an
> ORV campaign conducted during the 2003–2004 measles epidemic in Niamey, Niger." (`01`)

> "A novel human coronavirus… was identified in China in December 2019. There is limited
> support for many of its key epidemiologic features, including the incubation period…, which
> has important implications for surveillance and control activities." (`07`)

> "Although vaccination has almost eliminated measles in parts of the world, the disease
> remains a major killer in some high birth rate countries of the Sahel. On the basis of measles
> dynamics for industrialized countries, high birth rate regions should experience regular annual
> epidemics. Here, however, we show that measles epidemics in Niger are highly episodic." (`02`)

> "Isolation of cases and contact tracing is used to control outbreaks of infectious diseases…
> Whether this strategy will achieve control depends on characteristics of both the pathogen and
> the response. Here we use a mathematical model to assess if…" (`22`)

The strongest opening in the corpus is the **expectation-violation** (`02`, `04`): derive what
the canonical theory predicts for your system, then show the data refuse it. Use it whenever
you can.

---

## 2. Methodology conventions

### 2.1 How much mathematics, and where

The corpus is nearly unanimous: **the main text carries the argument, not the algebra.**

- **General-science journals:** essentially no equations. Models are named and described
  ("a stochastic compartmental model stratified into 5-year age bands"; "variations on the
  susceptible–infectious–recovered (SIR) model"). Where symbols appear they are glossed in
  words on first use, and often *only* in a figure caption (`02`, `04`, `12`, `13`).
- **Methods and modelling journals:** displayed, numbered equations, referred to as
  "Equation (1)" or `(2.1)`. Build complexity in visible steps, one subsection per step —
  single interval score → weighted interval score; discrete → continuous (`11`).
- **A compact model block beats prose** when the model is a generative chain. `26` gives four
  lines (R_t process, renewal equation, delay convolution, negative binomial observation) and
  then glosses each line in a paragraph.
- **Give the analytic bound alongside the simulation** where one exists: "In theory, blanket
  prophylaxis … should be able to contain a pandemic with an R₀ of 1/[(1 − 0.6)(1 − 0.3)], or
  approximately 3.6" (`13`). It makes the simulation auditable.
- **Always re-express notation epidemiologically.** Never leave a β unexplained in biological
  terms: "where β_quartier is the transmission rate between children within the same quartier"
  (`01`).

Worked model-definition passages at all three levels of formality are in §12.1.

Reserve full formal treatment for **the one object that carries the argument** — the scoring
rule in `10` and `11`, the elasticity and EVPI formulas in `23`, the coupling derivation in
`06`. Everything else is named and cited.

### 2.2 Assumptions

Flat declarative sentences, in Methods, each with a reason or a source:

> "Once infected, the infectious process is assumed to be deterministic; children are infected
> but not infectious (latent) for 10 days and infectious for 6 days." (`01`)
> "We assumed that exposure always preceded symptom onset." (`07`)
> "We assumed the outbreak started with a single infectious case on Nov 22, 2019." (`19`)
> "For analytical tractability, we model a single generation of infection." (`20`)
> "We assume that 50% (see Supplementary Information for sensitivity analysis) of those infected
> are ill enough to be classified as clinical cases." (`12`)

Three rules:

1. **State the assumption, then the justification, then the pointer to where it is tested** —
   often all in one sentence, as in `12`.
2. **State the direction of the bias**, not merely its existence. "Relaxing these assumptions
   would decrease the probability that control is achieved" (`22`). "If the true delay … is
   shorter than our global delay, then we will overestimate onset case numbers, and vice versa"
   (`26`). This is the single most valuable habit in the corpus.
3. **Claim conservatism only when you can defend it**, and then repeat the word deliberately
   (`07`, `13`). Optimistic assumptions plus a pessimistic conclusion is a strong argument;
   say so explicitly.

Worked assumption-with-direction-of-bias: §12.4.

### 2.3 Parameters and priors

- Give the distribution, both moments, and the source: "The incubation period was assumed to be
  Erlang distributed with mean 5·2 days (SD 3·7)" (`19`).
- Justify distributional choice biologically, then test alternatives in an appendix:
  "we assumed that the incubation time follows a log-normal distribution, as seen in other acute
  respiratory viral infections" (`07`).
- **Label every parameter as sampled or fixed** in the parameter table (`22`). This one column
  tells the reader exactly where uncertainty is propagated. A template is §12.12.
- Synthesise rather than assert: R₀ "derived from a meta-analysis of studies and preprints
  published before Feb 26, 2020" (`25`).
- **When you change a prior, report the old one and why**: "This contrasts with our earlier
  approach which was to use a gamma prior with a mean of 2.6 and standard deviation 2" (`26`).
- State priors operationally where that is clearer than the parameterisation: "an inverse gamma
  prior with shape and scale values optimised to give a distribution with 98% of the density
  between 2 days and 21 days" (`26`).
- Give MCMC detail in full: chains, warmup, samples, and the convergence diagnostic (`26`).
- Where a parameter is unknowable, say so and route around it: "The natural history of any
  H5-based pandemic strain will not be known until it emerges, so we used parameter estimates
  for current human influenza subtypes, and used sensitivity analyses to investigate what effect
  deviation from these estimates would have on policy effectiveness" (`13`).

A full worked Bayesian-fit methods paragraph — observation model, priors with justification,
sampler settings, diagnostics, software versions — is §12.8.

### 2.4 Scenarios

- **Declare a baseline scenario and vary one thing at a time from it.** "We present results in
  relation to the baseline scenario of R₀ of 2·5, 20 initial cases, a short delay to isolation,
  15% of transmission before symptom onset, and 0% subclinical infection" (`22`).
- **Enumerate the grid exhaustively in Methods** before any result appears (`01`, `22`).
- **Define scenarios in a table as percentage changes to contacts by setting** for NPI work —
  school closure → school contacts 0%, home contacts 100% (`25`). This table is the most
  reusable artefact in an intervention paper; a template is §12.13.
- **Letter- or name-code your scenarios and never renumber them** (`08`: scenarios A–G ordered
  by increasing non-linearity, then used to index every table, figure and sentence).
- **Sweep effect sizes rather than picking one**, so conclusions can be stated as thresholds:
  10–100% in 10% increments (`23`); "optimal in 22 of 37 models if the effect is over 30%".
- **Present every result under two or more labelled scenarios** where the key parameter is
  genuinely uncertain, so readers can locate their own risk tolerance (`12`: R₀ = 1.7 and 2.0).

### 2.5 Sensitivity analysis

Report it, and report **its conclusion in the same sentence**:

> "As a sensitivity analysis, we also ran model projections with a seasonal component such that
> transmission is 20% higher in winter than in summer, but this did not qualitatively affect our
> results (fig. S24 and table S5)." (`24`)

Name each sensitivity analysis by what was varied, not by number: fever-only onset, mainland vs.
outside China, alternative distributions, alternative exposure lower bound (`07`). Where several
were run, summarise by conclusion rather than by table: they "produced the same conclusion about
decline in transmission" (`19`).

Design a **targeted secondary analysis** to kill a specific alternative explanation — a
regression with fixed effects isolating the effect of data revision (`10`); an explicit test that
variant growth is not a testing artifact (`24`).

### 2.6 Software and computation

Name the language, the version, the packages, and the versions of the packages:

> "coarseDataTools and activemonitr packages in the R statistical programming language, version
> 3.6.2" (`07`)
> "rpart, ipred, randomForest, twang" with R 2.6.1 (`08`)
> "the EpiNow2 R package (version 1.2.1)" (`26`)

Pin the data too: "Ground truth values obtained as of September 27, 2017" (`10`); data pulled
through a versioned API so the analysis is re-runnable. Generating the manuscript itself from
code (Sweave/knitr, `10`) means text and numbers cannot diverge.

---

## 3. Results storytelling

### 3.1 Uncertainty: pick the right interval and label it

Use the interval that matches the object, and keep the kinds distinct within a paper:

| Object | Interval | Example |
|---|---|---|
| Frequentist estimate | 95% CI | "5.1 days (95% CI, 4.5 to 5.8 days)" (`07`) |
| Bayesian posterior | 95% CrI / BCI | "odds ratio, 0.92; 95% credible interval (CrI), 0.77 to 1.10" (`24`) |
| Simulated future | 95% prediction interval | "350 000 deaths (170 000–480 000)" (`25`) |
| Simulation ensemble | median [IQR] or median with 50%/95% intervals | "7.6% [4.9–8.9]" (`01`); (`22`) |
| Across-model spread | mean ± SD, or range across methods | "5,615 ± 2,705 (SD)" (`23`); "43 to 90% (range of 95% credible intervals, 38 to 130%)" (`24`) |

Formatting conventions worth adopting: one decimal place for days; "to" rather than an en dash
inside a CI in clinical journals; drop the "95% CI" label after first use in a paragraph
(`19`); report the median rather than the mean for skewed simulation output.

**Report the policy-relevant quantile, not the mean.** The 97.5th percentile of the incubation
period sets a quarantine window, so it leads (`07`).

**Translate to natural frequencies** when the number is small: "101 out of every 10 000 cases
(99th percentile, 482) will develop symptoms after 14 days" (`07`).

**Where the result is a null, say so with an interval that spans both directions:**
"Our estimates of severity are uncertain and are consistent with anything from a moderate
decrease to a moderate increase" (`24`).

Weak-to-strong repairs for results sentences are worked in §12.5.

### 3.2 Give every number a comparator

Nothing in this corpus is "good" or "large" in the abstract. Every claim is anchored:

- to a **naïve baseline**, glossed in plain English: "a relative WIS of 0.61, which can be
  interpreted as achieving, on average, 39% less probabilistic error than the baseline forecast"
  (`09`); "the largest improvement upon baseline predictions (0.17)" (`10`);
- to a **capacity constraint**: "roughly 13–80 times ICU capacity in the UK, which we tallied at
  4562 beds" (`25`);
- to a **named reference scenario**: "reduced total COVID-19 deaths by 58% (95% PI 30–80)
  relative to the intensive interventions scenario" (`25`);
- to a **canonical system**: "fourfold that of historical London"; "over an order of magnitude
  higher than predicted from classical studies" (`02`);
- to a **historical epidemic**: 2009 H1N1 "took 132 days to reach the same number of cities in
  China" (`16`).

### 3.3 Sentence shapes that recur

**The gradient in one sentence.** "up to 38, 27 and 20% of cases averted for campaigns at 60, 90
and 120 days from the start of the epidemic, respectively" (`01`).

**Intervention → what it moves → what it does not move → the condition.** "School closure during
the peak of a pandemic can reduce peak attack rates by up to 40%, but has little impact on
overall attack rates, whereas case isolation or household quarantine could have a significant
impact, if feasible" (`12`). The "but only if…" clause is present in nearly every claim in the
policy papers, and it is what makes them credible.

**Verdict → "however" → the numbers.** "All methods displayed generally acceptable performance
under conditions of either non-linearity or non-additivity alone. However, under conditions of
both moderate non-additivity and moderate non-linearity, logistic regression had subpar
performance…" (`08`).

**The concessive inside the headline claim.** "The COVIDhub-ensemble was the only model that
ranked in the top half … for more than 75% of the observations it forecasted, although it made
the single best forecast less frequently than any other model" (`09`).

**Unexpected result plus its mechanism, in the same sentence.** "the effect of isolation was
coupled with the chance of stochastic extinction resulting from overdispersion, which is why
some outbreaks were controlled even at 0% contacts traced" (`22`).

### 3.4 Grade your verbs and modals to your evidence

- Design-appropriate verbs: interventions are **"associated with"** outcomes in observational
  designs; the model **"suggests"**; the response **"appears to have"** delayed growth (`16`).
- Counterfactual modals graded by how hypothetical the premise is: *would have* (under stated
  assumptions) → *could have* → *might have* (under a hypothetical technology) (`20`).
- Within a single sentence: "is found to be invariant … and also appears to be constant" (`18`)
  — two evidential strengths, no separate hedging clause.
- Claim **qualitative** agreement when that is what you have. "The model supports our dynamical
  hypothesis, capturing the qualitative pattern of episodic outbreaks" (`02`) is more persuasive
  than overclaiming fit.

**Never write "biased" without saying which way.** A direction is actionable; a bare claim of bias
is not. Give the condition, the direction, and where possible the magnitude and the timing:

> "If the mean generation interval is set too high, R_t values will typically be further from 1
> than the true value—too high when R_t>1 and too low when R_t<1." (`27`)
> "ignoring right truncation for a fast-growing epidemic with relatively long delays could result
> in underestimation of the mean delay distribution by up to 50%" (`28`)
> "The bias was greatest early in the epidemic." (`28`)

This applies to your own estimates, to your assumptions (§2.2), and to any method you criticise.

### 3.5 Report your own failures in the Results

The most trust-building habit in the corpus:

> "the model did not predict the slowdown in cases that was observed in early February." (`19`)
> "In some of the selected waves (e.g., North Dakota and Florida), the ensemble forecast showed
> inappropriate levels of uncertainty, with the 95% PIs covering the eventual observations less
> than 80% of the time." (`09`)

Put these in Results, not buried in Discussion.

### 3.6 Figures

- Overlay observed data on simulated trajectories so validation is visual and immediate (`01`).
- Put the fixed parameter values in the caption of the figure they generated (`04`).
- Use boxplots over replicates to argue about **dispersion**, not just central tendency (`08`).
- Build **pedagogical figures** for methods papers: show the object, then walk the reader through
  it line by line (`11`).
- Mark the boundary between estimates and estimates-from-partial-data in every real-time figure
  (`26`).
- Show a bifurcation diagram with your system's parameters *and* the canonical system's marked on
  the same axis (`02`, `04`).

---

## 4. Literature integration

### 4.1 Density

Numbered citations throughout the corpus; author-year only in the ecology journals. Density
varies by archetype, and is a deliberate choice:

- General-science policy papers: sparse, ~1 per 300–350 words (`12`).
- Empirical modelling papers: moderate, ~1 per 85–160 words (`10`, `19`).
- Dynamical-systems papers: dense, with clusters of 3–5 references carrying a whole body of work
  in one sentence (`02`).
- Reviews: ~150+ references; most sentences 1–2, synthesis paragraphs 5–8 (`14`).

Concentrate citations in the Introduction and where parameters are justified. Methods sections
cite sources of parameters and of methods, and little else.

### 4.2 How to state the gap

Never "little is known about X". State a **checkable claim**:

> "We identified no estimates of how R0 had changed in Wuhan since control measures were
> introduced in late January or estimates that jointly fitted data within Wuhan to international
> exported cases and evacuation flights." (`19`)
> "While multimodel comparisons exist in the literature for single-outbreak performance, here we
> compare a consistent set of models over seven influenza seasons." (`10`)
> "Yet, the implications of post-death transmission for inferences about epidemic spread have not
> been evaluated systematically." (`21`)
> "the effectiveness of travel restrictions and social distancing measures in preventing the
> spread of infection is uncertain." (`16`)

More weak-to-strong gap statements are worked in §12.3; a worked positioning paragraph is §12.7.

### 4.3 Seven ways to position against prior work

1. **Adjudicate a disagreement.** "Some previous studies suggest that reactive vaccination will
   not stop epidemics…; other analyses, however, point to the potential benefits…" (`01`)
2. **Claim rigour, not novelty.** "Our results are broadly consistent with other estimates…
   Our analysis … made more conservative assumptions…" (`07`)
3. **Displace the received view without demolishing it.** "Until now, Ebola outbreaks were
   thought to be easily controlled. The usual narratives … highlight the importance of safe
   funerals, prompt isolation and effective contact tracing. However, testing strategies can also
   have a crucial role…" (`20`)
4. **Attack the incumbent by its consequence.** "These hypotheses suggest that it should be
   difficult or impossible to predict the timing and nature of specific transitions… Here, we give
   an alternative explanation…" (`04`)
5. **Show correct work misapplied.** "the standard SIR model parameterized on observations from
   industrialized countries predicts highly persistent, annual dynamics… However, the following
   analysis … reveals starkly contrasting patterns to such extrapolations." (`02`)
6. **Diagnose non-adoption rather than non-existence.** "The suggestion to use such algorithms …
   is not new. However, these methods have not been widely applied … perhaps because of the
   'black box' nature of some of the algorithms…" (`08`)
7. **Claim a different audience and format, not new knowledge.** "Our paper goes beyond the work
   of Park and colleagues by offering practical guidelines, a suggested workflow, and checklists,
   for a broader technical audience, such as modelers at public health agencies." (`28`) Use this
   when the problem is diffusion of good practice rather than its absence — and describe the
   field as improving rather than deficient: "Methods for estimating epidemiological delays have
   been improving, especially during the COVID-19 pandemic…" (`28`).

### 4.4 Other integration habits

- **Anchor plausibility to relatives of the pathogen**: SARS and MERS incubation periods cited so
  a new estimate can be judged (`07`).
- **Use a historical epidemic as a mechanistic analogy**, with the mechanism spelled out: SARS was
  controllable "because the majority of transmission occurred after symptom onset" (`22`).
- **Quantify the field's own growth** rather than asserting it: "the number of published research
  articles on forecasting infectious diseases has tripled (Web of Science)" (`10`).
- **Turn the literature review into a table** when the field is decades old (`15`, Table 1;
  `10`, Table 1 of models with binary feature flags).
- **Cite preprints without apology** in fast-moving situations, dated (`25`).
- **In reviews, do not adjudicate.** "However the role of urbanization in vector-borne disease
  spread is complex: …. Nevertheless, …" (`14`).

---

## 5. Voice and tone

### 5.1 Person and tense

- **First-person plural, always.** "We developed", "We estimated", "We assumed", "we find".
  Never "I", rarely "the authors". Passive voice is reserved for the evaluation protocol, where
  it reads as impartiality ("forecasts are evaluated for accuracy at the end of the season",
  `10`), and for data provenance.
- **Tense:** present for biological facts, model structure and standing implications; past for
  what was done and observed. "The model tracks 66·4 million people" (present) but "We ran 200
  stochastic simulations" (past). Dynamical-systems papers use present throughout, including for
  the authors' own actions (`04`).

### 5.2 Hedging that carries information

Hedge the **inference**, not the number. Generic hedging ("may possibly suggest") is absent from
this corpus; every hedge names what is uncertain:

> "COVID-19 transmission probably declined in Wuhan during late January, 2020." (`19`)
> "unlikely to delay spread by more than 2–3 weeks unless more than 99% effective" (`12`)
> "only suggestive of potential trends" (`01`)
> "The most parsimonious explanation … is that people infected with VOC 202012/01 are more
> infectious …, although there is also reasonable support for a longer infectious period and
> multiple mechanisms may be operating." (`24`)

Hedge decisions rather than estimates when writing for policy:

> "Although it is essential to weigh the costs of extending active monitoring or quarantine
> against the potential or perceived costs of failing to identify a symptomatic case, there may
> be high-risk scenarios … where it could be prudent to extend the period of active monitoring."
> (`07`)

**Concede the alternative in the same paragraph as your choice.** "We preferred to motivate the
score through central predictive intervals … However, when applying …, formulation (4) may seem
more natural" (`11`). This construction does more for credibility than any amount of caution.

**Use scare quotes to flag terms you will not take at face value** — "big data", "historical
baseline" (`10`) — and to mark deliberate coinages on first use — 'sparks', 'core', 'satellite'
(`17`); 'true mass action' (`18`).

### 5.3 Precision over vagueness

Replace every vague quantifier with a number, a date, or a name.

- Not "many countries" → "over 100 countries in every continent except Antarctica" (`26`).
- Not "a large dataset" → "1,791 submission files with 556,050 specific predictions" (`09`).
- Not "a range of cities" → "60 cities … from London (3.3 × 10⁶ inhabitants) to Teignmouth
  (10 500 inhabitants)" (`18`).
- Not "recently" → "as of March 5, 2020" (`19`).
- Not "informs policy" → "healthcare staffing needs, school closures, and allocation of medical
  supplies" (`09`).

Date everything. A paper that says "recently" is unreadable in three years; a paper that says
"23 January 2020" is readable forever.

---

## 6. Domain-specific conventions

### 6.1 The R₀ paragraph

When the audience may not be modellers, teach the control logic once, from first principles, and
let every later result be an instance of it. `13` does it in five sentences: definition →
threshold → control target (eliminate a proportion 1 − 1/R₀ of transmission) → an exhaustive
enumeration of the three intervention classes. That enumeration then structures the paper.

Distinguish **R₀ / R_t / R_e** and say which you mean. Define the instantaneous reproduction
number explicitly when you use it, and cite the definitional literature (`26`).

### 6.2 Validation, out-of-sample evidence and scoring

*For supervised learning specifically — train/test discipline, calibration, bias in training
data, appraisal criteria — see §7.*

The field's analogue of train/test discipline. Report:

- **Out-of-sample validation, stated as such**: "although it was parameterized on the basis of
  observations from 1986 to 2002 in Niamey, the metapopulation model predicts the qualitative
  pattern of regional persistence at the national scale from 2001 to 2005" (`02`).
- **Prospectivity as a methodological claim**: forecasts were made in real time, teams could not
  refit, and the four post-hoc bug fixes are documented rather than hidden (`10`).
- **Independent validation of a fitted quantity**: an inferred infectiousness profile
  "remarkably consistent with viral shedding data from experimental infection studies" (`13`).
- **Accuracy and calibration separately.** Accuracy = WIS or MAE; calibration = empirical
  coverage of prediction intervals. They are different virtues; never conflate them (`09`).
- **Proper scoring rules**, named, cited and interpreted for the reader; report on an
  interpretable scale (geometric mean of scores; relative WIS), not on the raw log scale (`10`,
  `11`).
- **Simulation benchmarks**: fix a metric set (bias, SE, coverage, balance) and report it in the
  same order in every table; use the off-the-shelf configuration and defend that as the realistic
  user's configuration (`08`).
- **Model comparison**: rank competing structures on an explicit criterion (DIC) and **report the
  runners-up**, framing the winner as "the most parsimonious explanation" (`24`).
- **Robustness as a vote count** across models: "optimal in 22 of 37 models" (`23`).
- **Report robustness to implementation failure as a co-equal outcome to effectiveness** —
  for an operational recommendation, a policy that degrades gracefully is worth more than one that
  is optimal under ideal delivery (`13`).

A template data, code and funding-role statement is worked in §12.11.

### 6.3 Identifiability and the limits of inference

When parameters trade off, say so and make it the result:

> "We find a negative relationship between the estimated pre- and post-death transmission rate."
> "Despite this identifiability problem, we find robustly that…" (`21`)

Do not report a failed fit — report **what the data can and cannot determine**, then find the
conclusion that holds across the whole indeterminate set. Escalate the finding to the model
class: "This is a generic feature of epidemiological models" (`21`).

### 6.4 Decision relevance

- **Ask whether the disagreement matters.** Divergent projections are not automatically a
  problem; test whether they change the recommended action (`23`).
- **Price uncertainty in decision units.** EVPI/EVPXI turns "we need better data on X" into "9%
  of achievable case reduction, 82% of total EVPI" (`23`).
- **Attach a logistics or ethics checkpoint to every intervention you endorse**: "a household
  quarantine policy might pose ethical dilemmas unless excellent infection control was
  implemented" (`12`).
- **Convert model requirements into a numbered operational checklist with target values** —
  the six containment criteria in `13` are the most-quoted part of that paper.
- **Define a plain-language vocabulary for posterior probabilities, numerically, before use**:
  <5% subcritical → "definite" increase; >95% → "definite" decrease; 20–80% → "unsure" (`26`).
- **Say when the analysis was done and for whom**: "The results we present here summarise the key
  analyses and scenarios we presented to decision makers over February–March, 2020, which evolved
  continuously as new information became available" (`25`).

### 6.5 Real-time and living analyses

- Report the **data-lock date** for every count.
- Demote forecasts relative to estimates explicitly: "These forecasts are indicative only and
  should not be considered with a weight equal to the real-time estimates" (`26`).
- Version the article alongside the software, with an `Amendments from Version N` changelog
  (`26`).
- Ship a tool, not just an estimate: a Shiny app (`07`), an interactive site (`10`), an R package
  (`22`), a spreadsheet and Java program that let readers vary assumptions (`20`).

### 6.6 Data, code and funding statements

Match the best in the corpus:

> "All code and data are available at https://github.com/HopkinsIDD/ncov_incubation (release at
> time of submission at https://zenodo.org/record/3692048)." (`07`)
> "No data were used in this study. The R code for the work is available at
> https://github.com/cmmid/ringbp." (`22`)

Rules:
- **A GitHub link is not archival.** Pair every repository with a Zenodo (or equivalent) DOI
  pinned to the submitted version. `26` separates *Development* from *Archived at the time of
  publication*, and lists each package with its role.
- Name the language and version; follow a reporting guideline where one exists and name it
  in Methods (`09` follows EPIFORGE). Which one depends on the archetype:
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
  responsibility for the decision to submit for publication." (`19`)
- Disclose preprints and conflicts concretely (`07`, `10`).
- Give per-author contributions, including who wrote the draft (`02`, `26`).
- **Share the individual-level data where you can, de-identified**: "the data should be
  anonymized/de-identified to protect patient privacy according to local health data laws and
  regulations" (`28`). Line-list format, with everything needed to re-run the estimation.
- **Where raw data genuinely cannot be released, publish the minimum viable artefact** so
  downstream meta-analysis is still possible: "If data cannot be shared, we recommend at minimum
  providing samples of the posterior distribution in a permanent online repository…" (`28`).
- **Report the distribution, not just the point estimate** — central tendency, variability,
  credible intervals, and the contextual information needed to reuse the estimate (`28`).
- Where authors sit in government agencies, include the standard disclaimer: "The findings and
  conclusions in this report are those of the authors and do not necessarily represent the
  official position of the CDC … or the UK Department of Health and Social Care." (`28`)

---

## 7. Machine learning and predictive modelling conventions

For papers whose contribution is a fitted predictive model rather than a mechanistic one. The
corpus covers three ML sub-archetypes — risk mapping and trait-based prediction (`29` Bhatt,
`32` Olival, `33` Han), digital surveillance and nowcasting (`30` Ginsberg, `34` Yang), and
clinical prediction (`37` Zoabi, `08` Lee) — plus three appraisals of the field's failures
(`31` Lazer, `35` Wynants, `36` Roberts). Everything in §1–§6 still applies; this section adds
what is specific to learning from data.

### 7.1 Lead with the problem, not the algorithm

No paper in this corpus opens by naming a method. Bhatt (10,400 citations) opens "Dengue is a
systemic viral infection transmitted between humans by *Aedes* mosquitoes"; Han opens
"Forecasting reservoirs of zoonotic disease is a pressing public health priority." The algorithm
appears in one sentence, named and justified by a property of the *data*, never by novelty:

> "generalized boosted regressions… have particular use for comparative ecological studies
> because they accommodate multiple data types as covariates, nonrandom patterns of data
> missingness, and hidden, nonlinear interactions." (`33`)
> "our use of GAMs, an incorporation of smooth spline predictor functions into the generalized
> linear model (GLM) framework, allowed us to examine the functional form of our predictor
> variables." (`32`)
> "Gradient boosting is widely considered state of the art in predicting tabular data." (`37`)

**Never lead with the AUC either.** Bhatt's headline is 96 million infections, not 0.81.

A full worked supervised-learning methods paragraph is §12.9; a worked bias check is §12.10.

### 7.2 Structure Methods as the pipeline, in execution order

`29` Bhatt: *Assembly of the occurrence database and its quality control · Explanatory covariates ·
Predicting the probability of occurrence · Estimation of burden and populations at risk*.
`32` Olival: *Database · Phylogenetic signal · GAM fitting and selection · Model cross-validation ·
Data availability · Code availability*.

Each stage becomes independently auditable. This beats a generic Data/Model/Analysis split.

### 7.3 Train/test discipline — state it in one unambiguous sentence

> "Datasets were partitioned into training (80% of all 2,277 species) and test (the remaining
> 20%) sets before analysis." (`33`)
> "The final model was validated on 42 points per region of previously untested data from 2007 to
> 2008, **which were excluded from all previous steps**." (`30`)

The qualifying clauses — *before analysis*, *excluded from all previous steps* — are the whole
claim. Feature selection, tuning and threshold choice must all sit inside the training fold.

**Split along the axis you will extrapolate over:**
- **Temporally**, when the model will be used going forward. `37` trains on 22–31 March and tests
  on the *following week*; `34` uses a rolling two-year window "assuming we had access only to
  the historical CDC's ILI reports up to the previous week of estimation".
- **Geographically**, when the model will be applied to new places. `32` "systematically removed
  all species from 34 mammalian zoogeographic regions", refit, and tested the held-out region —
  then **hatched the failing regions on the published map**. Show where your model does not
  transfer.
- Random k-fold is the weakest of the three and is best used alongside one of the others.

Cross-validation is named with its purpose, not just performed: "10-fold cross-validation during
model building to prevent overfitting" (`33`).

### 7.4 Report performance honestly

- **Give uncertainty on the metric**, not a bare number: "AUC of 0.81 (±0.02 SD, n = 336)" (`29`);
  "0.90 auROC… with 95% CI: 0.892–0.905", from "bootstrap percentile method with 1000
  repetitions" (`37`).
- **Under class imbalance, report auPRC alongside auROC** (`37`, 9.2% positive).
- **Give two named operating points** rather than one threshold: "87.30% sensitivity and 71.98%
  specificity, or 85.76% sensitivity and 79.18% specificity" (`37`).
- **Every metric relative to a naive baseline**: "the number reported is the ratio of error of a
  given method to that of the naive method" (`34`). Add one summary statistic with CIs — `34`'s
  relative efficiency lets the paper say "at least twice as efficient as any other alternative"
  instead of reciting five metrics.
- **Benchmark fairly, and say what you did to make it fair**: "For fair comparison, all benchmark
  models (ii–iv) are dynamically trained with a 2-y moving window" (`34`).
- **Contextualise a modest fit rather than hiding it**: 27–49% deviance explained is "greater than
  or comparable to studies examining much narrower groups of mammal hosts" (`32`).
- **Assess calibration, not just discrimination.** Its absence is the single most common failing
  named by `35`: "Only five studies assessed calibration."
- Report the metric set in a fixed order across every table (`08`).

### 7.5 Confront bias in the training data explicitly

The strongest habit in the ML corpus, and the one that separates these papers from the ones
`35` and `36` condemn.

- **Put sampling effort in the model as a covariate**, then report how much signal it absorbs:
  "research effort had the strongest effect on the total number of viruses per host, explaining
  31.9% of the total deviance" (`32`).
- **Fit a model of your own sampling process and show it does not reproduce your result**: `33`
  models "studiedness" from citation counts, finds pseudo-R² of 0.07–0.17, and concludes "the
  trait patterns of well-studied rodents and those of rodent reservoirs are not coincident."
- **Retrain without the features you distrust and publish the cost**: "If we train and test our
  model while filtering out symptoms of high bias in advance, we obtain an auROC of 0.862"
  (`37`) — against 0.90 with them.
- **Score data quality and re-run on the high-quality subset** (`32`: detection method scored
  0–2, parallel stringent-data analysis).
- **Disclose a conservative labelling decision and its direction**: 2,061 unlabelled species
  "designated nonreservoirs… a more conservative designation… with baseline classification
  performance that can only improve with ongoing discoveries" (`33`).
- **Name the confound that could produce your outcome without the intended signal**: an imaging
  model "might associate more severe disease not with CXR imaging features, but the view that
  has been used to acquire that CXR" (`36`).
- **Turn an arbitrary modelling choice into an ensemble** instead of defending it: 336 BRT models
  spanning the pseudo-absence parameter space, reported as a mean with an SD (`29`).

### 7.6 Interpretation is a result, not a garnish

- Variable importance **and** partial dependence together: "Marginal plots of the top 15 predictor
  variables… showing the marginal effect of each trait (shown in order of importance)" (`33`);
  partial effect plots with 95% bands (`32`).
- **Unify the important variables into one interpretable concept** rather than listing them —
  `33` collapses its top traits into a *fast-paced life history*.
- Define any explanation method in one plain sentence before using it: "Originating in game
  theory, SHAP values partition the prediction result of every sample into the contribution of
  each constituent feature value" (`37`).
- **Report the covariate that did *not* matter**: "low precipitation was not found to strongly
  limit transmission" (`29`).
- **State the confound-adjustment inside the claim sentence**: bats host more zoonoses "after
  controlling for reporting effort and other predictor variables" (`32`).
- **Ship the predictions as a named, falsifiable list**: "we identify 58 species predicted to be
  novel reservoirs and 159 species predicted to be novel hyperreservoirs" (`33`), supplied in
  full as a dataset. A predictive paper's proper conclusion is an experiment someone can run.

### 7.7 Say which numbers are ordinal

> "our estimates of missing viruses and missing zoonoses per species are based on the current
> maximum observed research effort from the literature, and these estimates should be viewed as
> relative, not absolute." (`32`)

Localise uncertainty too: `29` names the countries where its burden estimates are least reliable
rather than issuing a blanket caveat.

### 7.8 What appraisers will mark you down for

Distilled from `35` (PROBAST/CHARMS over 51 studies, all rated high or unclear risk of bias) and
`36` (62 studies, none clinically usable). Treat as a pre-submission checklist:

- **Outcome leakage**: "one of the predictors (e.g., fever) was part of the outcome definition."
- **Excluding participants still in follow-up**, "yielding a highly selected study sample."
- **Case-control sampling reported as a cohort**, making prevalence unrepresentative.
- **Small samples with complex models** — "an increased risk of overfitting, particularly if
  complex modelling strategies were used." `36` required "at least 20 events per variable" to
  score low risk of bias.
- **No calibration assessment.**
- **External validation on an unrepresentative dataset**, which is not external validation.
- **Bespoke architectures without benchmarking**: "Every study used a different deep learning
  architecture… without benchmarking the used architecture against others."
- **"Frankenstein datasets"** — "datasets assembled from other datasets and redistributed under a
  new name" (`36`), with duplicated or mislabelled sources.
- **No usable model artefact**: "Thirty one studies did not include any usable equation, format,
  or reference for use or validation of their prediction model" (`35`).
- **Purely data-driven predictor selection**: "we recommend building on previous literature and
  expert opinion to select predictors, rather than selecting predictors in a purely data driven
  way; this is especially important for datasets with limited sample size" (`35`).

Follow a reporting guideline and say so — TRIPOD (TRIPOD+AI) for prediction models, PROBAST
for appraisal, CLAIM/RQS for imaging, EPIFORGE for forecasting. The full list by archetype is
in §6.6.

### 7.9 The two failure modes that killed Google Flu Trends

From `31`, and both are structural rather than statistical:

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
   procedure.** `30` disclosed that 'high school basketball' and 'oscar nominations' scored highly
   — and did not act on it. `31`: "This should have been a warning that the big data were
   overfitting the small number of cases."
3. **Build in recovery.** `34`'s advertised virtue is not accuracy but self-correction — rolling
   retraining, L1 reselection of terms, autoregressive structure — because the predecessor's fatal
   flaw was staying wrong for two years.

---

## 8. Discussion and limitations

### 8.1 Discussion shape

Open by naming what the work shows or the tension it exposes — **not** by restating the abstract:

> "This work illustrates the tension between the desire for long-term forecasts, which would be
> helpful for public-health practitioners, and the decline in forecast accuracy at longer horizons
> shown by all forecasting methods." (`09`)
> "The high seasonality of transmission in Niamey leads to more irregular measles dynamics than
> predictions that are based on historical data for industrialized countries… This emphasizes the
> potential dangers of extrapolating dynamics for these sorts of highly non-linear systems without
> a detailed understanding of local parameters." (`02`)

Then: interpretation → comparison with prior estimates → limitations → what should change. For a
multi-dimensional result, a bulleted "We summarize the key findings of the work as follows"
list is legitimate and effective (`09`).

Close on one of: a decision ("Ultimately the decision whether or not to intervene … depend[s]
upon the political will of public health authorities", `01`), a data-collection priority ("It will
be imperative to collect the most detailed data … early in the emergence of a pandemic, and to
analyse those data in real time", `12`), or a research question. Not on a summary.

### 8.2 Limitations

Signpost with a plain opener — "There are limitations to our analysis"; "This analysis has
several important limitations"; "Our approach is also subject to several limitations" — then work
through them. Six categories, and the corpus's best framings for each:

1. **Simplification.** "Our models inevitably simplify the complex processes… However, they
   provide an important initial evaluation…" (`20`); "as with all models, ours simplifies reality
   in a number of respects" (`01`).
2. **Data quality and provenance.** "Ground-truth data are not static. They can be later revised
   as more data become available" (`09`); "The length of stay in ICU … estimated using data from
   China, and differences in UK populations could affect our estimates" (`25`).
3. **Contested parameters.** "the precise values of these parameters and the impact of school
   closures remain the subject of scientific debate" (`24`).
4. **Design.** "This study has drawn inferences not from controlled experiments but from
   statistical and mathematical analyses… With that caveat, control measures were strongly
   associated with the containment of COVID-19" (`16`); "We could not investigate the impact of
   all elements of the national emergency response because many were introduced simultaneously"
   (`16`).
5. **Scope fences** — an explicit prohibition on a misreading you expect. "these results should
   not be used to extrapolate hypothetical accuracy in pandemic settings" (`10`); "We have
   considered a small number of intervention and vaccination scenarios, which should not be
   regarded as the only available options for policy-makers" (`24`); "it cannot speak to model
   performance for incident cases or hospitalizations" (`09`).
6. **Irreducible uncertainty**, distinguished from fixable gaps. "Lack of data prevent us from
   reliably modelling transmission in … residential institutions" (fixable) versus "it will be
   impossible to predict the exact characteristics of any future pandemic virus" (not) (`12`).

Six rules for writing them:

- **Name the specific question the limitation prevents you answering**, not just "the model is a
  simplification": "Because the model does not explicitly structure individuals by household, we
  are unable to evaluate the impact of measures based on household contacts, such as household
  quarantine" (`25`).
- **Discharge what you can**, by sensitivity analysis or by direction-of-bias argument, and say
  which limitations remain live.
- **Frame limitations as design choices where they were choices**: "In this study we used only
  the basic, off-the-shelf versions of each of the methods, since that is likely what most applied
  researchers would do" (`08`); "we did not specifically consider the operational cost or
  constraints" (`23`).
- **Pre-empt misuse.** Explain why the tempting follow-up analysis would not be valid: an
  observational study of which model features improve accuracy "would be confounded by other
  factors about how the model was built and validated" (`09`).
- **Disclose how your evidence was selected.** If your examples are illustrative rather than
  systematically sampled, say so: "we did not aim to provide a systematic review; rather, we
  provided insights based on our experiences. The examples presented in this work were selected
  to illustrate specific points" (`28`). Most guidance and review papers omit this; including it
  costs nothing and forecloses a fair criticism.
- **Name the hard boundary** — the failure that no amount of method can fix: "Even the most
  powerful inferential methods, extant and proposed, will fail to estimate R_t accurately if
  changes in sampling are not known and accounted for" (`27`).

A weak-to-strong limitations paragraph is worked in §12.6.

The most quotable statement of modelling's epistemic limits, for use when arguing what a model
can and cannot do:

> "By definition and design, models are not reality. The properties of stochasticity and
> non-linearity strongly influence the accuracy of absolute predictions over long time horizons.
> Even if the mechanisms involved are broadly understood and relevant data are available,
> predicting the exact future course of an outbreak is impossible due to changes in conditions in
> response to the outbreak itself, and due to the many chance effects in play." (`15`)

Immediately followed by the constructive turn: "The field has yet to explore where that horizon
is and whether computational tools and additional data … can stretch predictions to this limit."
**Always convert the limitation into the next research question in the following sentence.**

---

## 9. Best-practice and guidance papers

A distinct archetype with its own rules, exemplified by `27` (Gostic et al. on R_t estimation)
and `28` (Charniga et al. on delay distributions). The contribution is neither a new model nor a
new estimate: it is a diagnosis of how a method others already use goes wrong, plus recommendations.
Much of §1–§8 still applies, but the following overrides it.

### 9.1 Structure by problem or by task, not by IMRaD

Neither paper has `Methods`/`Results`/`Discussion`. Sections are **the problems a practitioner
hits, in the order they hit them** (`27`: *Generation interval misspecification · Adjusting for
delays · Adjusting for right truncation · Accounting for incomplete observation · Smoothing
windows*), or **the tasks in a workflow** (`28`: *Biases in delay data · Measuring epidemiological
delays · Adjusting for common biases · Reporting epidemiological delay distributions*).

**Write headings as imperatives where the section is an instruction**: *Fit multiple probability
distributions · Visualize the distributions · Correctly convert parameters · Add subgroups or
stratify estimates · Check model diagnostics* (`28`). An instruction heading is scannable,
quotable and impossible to misread.

### 9.2 Build the paper so the summaries alone are usable

`27` ends **every substantive section with a bulleted `Summary` box**: "The Cori method most
accurately estimates the instantaneous reproductive number in real time. It uses only past data
and minimal parametric assumptions." A reader can extract the complete recommendation set from
the boxes; a reader who needs the argument reads the sections. Design for both.

`28` goes further and makes **the checklist the deliverable** — Tables 2–3, in *item / details /
examples / solutions* columns, so a reader can work through their own manuscript against it.
Add a **decision flowchart that branches on what data the reader has** (`28`, Fig 3) rather than
prescribing one method for everyone.

### 9.3 Simulate the truth, then degrade the data one step at a time

`27`'s evidential engine, and the cleanest available template for evaluating any estimator:

1. Generate synthetic data from a known model (a deterministic or stochastic SEIR), so the true
   value of the target quantity is known by construction.
2. Test every method "under idealized conditions" first, where "all infections are observed
   instantaneously".
3. Then add **one real-world imperfection per section** — generation-interval misspecification,
   observation delays, right truncation, incomplete observation, smoothing — each in isolation.

Every section then answers one question of the form *"what does this specific data imperfection
do to the estimate, and by how much?"*, and the answer is checkable because the truth is known.

### 9.4 Quantify the cost of bad practice

Guidance is only persuasive if the error it prevents is sized. `28` uses three registers, often
within a few sentences:

- a **worked before/after pair** on a familiar parameter: "the mean incubation period for
  COVID-19 in early 2020 … was 3.49 days without adjusting for right truncation compared to
  4.69 days when adjusted";
- a **worst-case magnitude**: "underestimation of the mean delay distribution by up to 50%";
- a **downstream consequence** for a quantity readers care about more: mis-specified generation
  intervals "led to biased estimates of R_t", with "The bias was greatest early in the epidemic."

Trace the error forward to the thing people actually use. "Knock-on impacts" (`28`) is the frame.

### 9.5 Prescriptive but not imperious

- **"We recommend" appears more than twenty times in `28`; "must" does not appear.** Authority
  comes from specificity and repetition, not modal force.
- **Say what you do not recommend, with a structural reason**: "In its current form, we do not
  recommend using the method of Bettencourt and Ribeiro, given that unrealistic structural
  assumptions lead to bias" (`27`). Only publishable because the synthetic-data design makes it
  demonstrable — but where you can support it, it is the most useful sentence in the paper.
- Hedge **applicability**, not confidence: "may not always be the case", "should be assessed on a
  case-by-case basis", "likely a better use of available data".
- State consequences in plain conditional form: "Not or incorrectly accounting for censoring of
  event intervals can lead to biased estimates of a delay" (`28`).

### 9.6 Other conventions of the archetype

- **Name methods after their authors** — "the Cori method", "the method of Wallinga and Teunis",
  "the method of Bettencourt and Ribeiro" (`27`). More readable than acronyms, and it attributes.
- **Run each method in its canonical implementation, named**: "obtained using the R package
  EpiEstim … by translating code from references into the Stan language" (`27`). Recommend tools
  by name with a basis: `coarseDataTools`, `epidist`, `EpiNow2`, `epitrix`, `epiparameter` (`28`).
- **Count a method's parametric assumptions** as part of comparing it: "The only parametric
  assumption required by this method is the form of the generation interval" (`27`).
- **Name a small closed set of problems** — censoring, right truncation, dynamical bias (`28`) —
  and organise every table, figure, recommendation and checklist row around that same set.
- **Trace a formalism to its origin before using it.** `27` gives the renewal equation in its
  original demographic form, "where b(t) is the number of births at time t and n(a) is fecundity
  at age a", then re-expresses it epidemiologically. Showing provenance exposes assumptions.
- **Set up a conceptual distinction early and police it throughout**: instantaneous vs. case
  reproductive number, "intrinsic" vs. observed generation interval (`27`); forward vs. backward
  cohort approaches (`28`) — the latter yielding the paper's strongest single recommendation,
  "We recommend always analyzing delay distributions as forward distributions."
- **Split derivation from guidance across two papers, and say so**: "Technical details about these
  biases and how to adjust for them can be found in Park and colleagues" (`28`). Both stay readable.
- **Distribute limitations** through the sections rather than isolating them, and gather the
  residue in the conclusions — including the hard boundary no method can fix (§8.2).
- Write both the Abstract and the Author Summary at different levels: `27`'s Author Summary
  defines R_t from scratch ("whether an epidemic is growing, shrinking, or holding steady") where
  the Abstract assumes it.

---

## 10. Anti-patterns

Absent from every paper in this corpus. Do not write them.

- "Little is known about X" — state a checkable claim about what you searched for and did not find.
- "This is the first study to…" — the *first-study* claim is the problem, not the hedge. Claim
  scope or rigour instead; "none, to our knowledge, has…" attached to a checkable claim is fine
  (see §12.3).
- A number without a comparator, a unit, or an interval.
- "Recently", "many countries", "a large dataset", "informs policy" — all replaceable with a
  number, a date, or a name.
- Generic hedging ("may possibly indicate") — hedge the specific inference, or don't hedge.
- Limitations that only appear at the very end and are never discharged.
- "The model shows that X will happen" — models suggest, project under assumptions, or estimate.
- Equations in general-science main text; models named only by acronym in a methods journal.
- A GitHub link with no archived version DOI.
- A Discussion that restates the Results in the same order and adds nothing.
- Scenario sets presented as if they were the option set available to decision-makers.
- Burying the fact that the model failed to reproduce a feature of the data.
- "Biased" or "sensitive to X" with no direction, magnitude, or timing attached.
- Leading with the algorithm, or with the AUC, instead of with the problem and the burden.
- A performance metric with no uncertainty, no baseline, and no named operating point.
- A random train/test split for a model that will be used forward in time or in new places.
- Feature selection, tuning or threshold choice performed before the split.
- Discrimination reported without calibration.
- Sampling bias acknowledged in the Discussion but not modelled, tested, or adjusted for.
- Predictions that cannot be checked because the candidate list was never published.
- "External validation" on a dataset that is not representative of the target population.
- Recommendations with no stated cost of ignoring them.
- Illustrative examples presented as if they were a systematic review.
- A repository link offered in place of shareable data when posterior samples could have been
  published instead.

---

## 11. Working checklist

**Before drafting**
- [ ] Archetype identified; the matching file in `writing_styles/` read.
- [ ] Journal template chosen; heading scheme decided.
- [ ] Headline claim written as one sentence in the right shape for the archetype.
- [ ] `Research in context` panel drafted (whether or not the journal wants it).

**Methods**
- [ ] Model named, its class stated, structure described before any equation.
- [ ] Every assumption a declarative sentence with a reason and, where possible, a direction of bias.
- [ ] Parameter table with sources and a sampled/fixed column (template: §12.12).
- [ ] Baseline scenario declared; scenario grid enumerated exhaustively (template: §12.13).
- [ ] Priors stated with justification; MCMC/computation detail complete.
- [ ] Sensitivity analyses named by what they vary, each reported with its conclusion.
- [ ] Software, versions, packages, data-lock date.

**Results**
- [ ] Every estimate has the right kind of interval, labelled and used consistently.
- [ ] Every number has a comparator (baseline, capacity, reference scenario, prior literature).
- [ ] Policy-relevant quantile leads, not the mean.
- [ ] Where the model failed, that is in the Results.
- [ ] Verbs and modals graded to the design and to the evidence.
- [ ] Figures: parameters in captions; observed data overlaid on simulations; wide content readable.

**Discussion**
- [ ] Opens with the tension or the general lesson, not a restatement.
- [ ] Limitations signposted, categorised, discharged where possible, with scope fences for
      foreseeable misreadings.
- [ ] Each limitation converted into a research question in the next sentence.
- [ ] Closes on a decision, a data priority, or a question.

**Back matter**
- [ ] Data and code: repository **plus** archived DOI; licence; language and version.
- [ ] Individual-level data shared and de-identified, or posterior samples published instead.
- [ ] Funder role, conflicts, preprint disclosure, per-author contributions.
- [ ] Reporting guideline followed where one exists.

**Additionally, if this is a machine learning or predictive modelling paper (§7)**
- [ ] Problem and burden lead; algorithm named once and justified by a property of the data.
- [ ] Methods subheadings are the pipeline stages in execution order.
- [ ] Split stated in one sentence, and along the axis of intended extrapolation (temporal or
      geographic, not random) — with everything held out done *before* any tuning.
- [ ] Performance with an interval, against a naive baseline, plus calibration and (under
      imbalance) auPRC; benchmark fairness stated.
- [ ] Sampling bias modelled or tested, not merely acknowledged; the confound that could mimic
      your signal is named.
- [ ] Variable importance and partial effects; the null result reported; adjustment stated
      inside the claim sentence.
- [ ] Predictions released as a named, falsifiable list; ordinal quantities labelled as relative.
- [ ] Checked against §7.8; reporting guideline named (see the list in §6.6).
- [ ] Data, code, and trained hyperparameters in a repository with an archived DOI.

**Additionally, if this is a best-practice or guidance paper (§9)**
- [ ] Sections are problems or tasks; instruction sections have imperative headings.
- [ ] Every substantive section ends with a bulleted summary; the summaries alone are usable.
- [ ] Evidence comes from synthetic data with a known truth, degraded one imperfection per section.
- [ ] Every recommendation has the cost of ignoring it, quantified and traced downstream.
- [ ] Direction, magnitude and timing given for every bias.
- [ ] At least one explicit negative recommendation, with a structural reason.
- [ ] A closed, named set of problems, used consistently across all tables and figures.
- [ ] Checklist and/or decision flowchart branching on what data the reader has.
- [ ] Scope disclosed: illustrative examples labelled as such; the hard boundary named.

---

## 12. Worked examples

Templates demonstrating the conventions above. **All numbers, place names and results here are
illustrative** — they show the shape of a sentence, not a finding. Replace every value.

### 12.1 Defining a compartmental model

Write this at the level of formality the venue expects, but **always name the compartments in
words on first use and always state the flows between them.** Never assume "SIR" is self-explanatory.

**Level 1 — general-science journal, no equations** (`12`, `13`, `25` write like this):

> We used a compartmental transmission model in which each individual is in one of three
> states: susceptible to infection (S), infectious (I), or recovered and immune (R).
> Susceptible individuals become infectious at a rate proportional to the prevalence of
> infection in the population; infectious individuals recover at a constant rate and are then
> immune for the remainder of the simulated period. Full model equations and parameter values
> are given in the Supplementary Information.

**Level 2 — epidemiology or modelling journal, displayed equations** (`01`, `19`, `26`):

> We modelled transmission using a deterministic susceptible–infectious–recovered (SIR)
> framework. Individuals move from the susceptible class *S* to the infectious class *I* on
> infection, and from *I* to the recovered class *R* on recovery, with no loss of immunity over
> the period modelled:
>
> &nbsp;&nbsp;&nbsp;&nbsp;d*S*/d*t* = −β *S I* / *N*&nbsp;&nbsp;&nbsp;&nbsp;(1)
> &nbsp;&nbsp;&nbsp;&nbsp;d*I*/d*t* = β *S I* / *N* − γ *I*&nbsp;&nbsp;&nbsp;&nbsp;(2)
> &nbsp;&nbsp;&nbsp;&nbsp;d*R*/d*t* = γ *I*&nbsp;&nbsp;&nbsp;&nbsp;(3)
>
> where *N* = *S* + *I* + *R* is the total population size, assumed constant over the epidemic;
> β is the transmission rate, defined as the average number of effective contacts made by one
> infectious individual per day; and γ is the recovery rate, so that 1/γ is the mean infectious
> period. The basic reproduction number is *R*₀ = β/γ, the average number of secondary
> infections generated by a single infectious individual in an entirely susceptible population.
> We took the mean infectious period to be 6 days (1/γ = 6), following [ref], and estimated β by
> fitting to the observed case time series (§*Model calibration*). Simulations were initialised
> with one infectious individual in an otherwise fully susceptible population of *N* = 750,000.

Everything a reader needs is there: **flows named, every symbol glossed with its units or
meaning, the derived quantity they care about (*R*₀), which parameters were assumed versus
estimated, and the initial conditions.**

The same equations in the two toolchains manuscripts are actually written in. Match whichever
the user's draft uses; do not hand back markdown italics to someone working in LaTeX or Word.

*LaTeX / Overleaf / Quarto* (`align` numbers each line; use `\frac` only if the journal's
class file sets display equations at a readable size):

```latex
\begin{align}
  \frac{\mathrm{d}S}{\mathrm{d}t} &= -\beta \frac{S I}{N}, \label{eq:dS} \\
  \frac{\mathrm{d}I}{\mathrm{d}t} &= \beta \frac{S I}{N} - \gamma I, \label{eq:dI} \\
  \frac{\mathrm{d}R}{\mathrm{d}t} &= \gamma I, \label{eq:dR}
\end{align}
where $N = S + I + R$ is the total population size, $\beta$ is the transmission rate and
$\gamma$ is the recovery rate, so that $1/\gamma$ is the mean infectious period and
$R_0 = \beta/\gamma$.
```

*Word / Google Docs / plain text* (Unicode; paste into the equation editor or leave inline):

```text
dS/dt = −β S I / N                    (1)
dI/dt = β S I / N − γ I               (2)
dR/dt = γ I                           (3)
```

where N = S + I + R, β is the transmission rate, γ the recovery rate (1/γ the mean
infectious period) and R₀ = β/γ. In Word, use the built-in equation editor (Alt + =) with
the same symbols rather than italicised letters; in Google Docs, Insert → Equation.

**Adding a compartment — say what it buys you.** Do not extend a model silently:

> Because measles has a substantial latent period during which infected individuals are not yet
> infectious, we extended the model to include an exposed class *E*, giving an SEIR structure.
> Individuals move from *S* to *E* on infection, from *E* to *I* at rate σ (mean latent period
> 1/σ = 10 days), and from *I* to *R* at rate γ. Including *E* lengthens the generation
> interval and therefore slows the modelled epidemic for a given *R*₀; omitting it would cause
> us to overestimate how quickly an intervention must be deployed to have an effect.

The final clause is the important one: **state what the extra structure changes about the
answer**, not merely that it is more realistic.

**Stochastic or individual-based version:**

> Transmission was simulated stochastically in discrete time steps of Δ*t* = 0.25 days. In each
> step, a susceptible individual *i* becomes infected with probability 1 − exp(−λ_i Δ*t*), where
> λ_i is the instantaneous force of infection acting on that individual, comprising
> contributions from their household, their school or workplace, and random community contacts
> (`13`). Each simulation was run 1,000 times; we report the median and the 2.5th and 97.5th
> percentiles across runs.

### 12.2 An abstract, built move by move

The six-move spine of §1.1, annotated. Each move is one or two sentences:

> [1 — burden, quantified and dated] Measles caused an estimated 128,000 deaths worldwide in
> 2021, concentrated in countries with high birth rates and interrupted routine immunisation.
> [2 — the specific gap] Outbreak response vaccination is widely deployed in these settings, but
> the campaign timing at which it stops being cost-effective has not been quantified.
> [3 — "Here, we…"] Here we use an age-structured stochastic transmission model, fitted to
> weekly surveillance data from 42 districts between 2015 and 2022, to estimate the number of
> cases averted by campaigns launched at different points in an outbreak.
> [4 — headline result with uncertainty] We estimate that a campaign reaching 60% of children
> aged 6–59 months averts 34% (95% CrI 21–46) of cases when launched 60 days after the first
> reported case, falling to 11% (4–19) at 120 days.
> [5 — the bounding condition] The benefit depends critically on delay: campaigns launched more
> than 100 days after onset averted fewer than 15% of cases under every coverage level we
> considered.
> [6 — what should change] These results support pre-positioning vaccine stocks and
> pre-authorising campaign triggers, rather than optimising coverage targets once an outbreak
> is already established.

### 12.3 Gap statements: weak → strong

| Weak | Strong |
|---|---|
| "Little is known about the effectiveness of contact tracing." | "We identified no estimates of the tracing coverage required to control an outbreak with a reproduction number above 2, under realistic delays from symptom onset to isolation." |
| "No study has combined mobility and case data." | "Previous analyses have used either case notifications or mobility data; none, to our knowledge, has fitted both jointly, which is necessary to separate a decline in transmission from a decline in reporting." |
| "This is the first study to model X." | "While single-season comparisons exist, here we evaluate a consistent set of models across seven seasons, which is the shortest span over which between-season variation can be distinguished from between-model variation." |

The strong versions are **checkable claims** and each says *why the gap matters*.

### 12.4 An assumption, with its direction of bias

Weak:

> We assumed that isolation prevents all onward transmission.

Strong (`22`, `26`):

> We assumed that isolation prevents all onward transmission. This is optimistic: in practice
> some transmission occurs after isolation begins, particularly within households. Our estimates
> of the probability of control should therefore be read as an upper bound, and the tracing
> coverage we report as the minimum required.

**Every assumption gets three parts: the assumption, whether it is optimistic or pessimistic,
and what that does to the number the reader will quote.**

### 12.5 Results sentences: weak → strong

| Weak | Strong |
|---|---|
| "Vaccination reduced cases substantially." | "Vaccination at 60% coverage reduced cumulative cases by 34% (95% CrI 21–46) relative to no campaign." |
| "The model fitted the data well." | "The model reproduced the observed weekly incidence in 38 of 42 districts within the 95% prediction interval; it did not capture the secondary peak observed in three northern districts in 2019." |
| "Our estimate is higher than previous work." | "Our central estimate of 4.7 days is 1.2 days longer than the pooled estimate of 3.5 days reported previously, a difference attributable to our adjustment for right truncation." |
| "Performance was good (AUC 0.88)." | "The model achieved an auROC of 0.88 (95% CI 0.86–0.90) against a naive baseline of 0.61, with an auPRC of 0.44 (0.40–0.48) at an outcome prevalence of 8%." |
| "Interventions had a large effect." | "School closure reduced peak incidence by 31% but total cases by only 6%, and the effect on peak incidence fell below 10% if closure was delayed more than three weeks past the epidemic threshold." |

Recurring repairs: **attach an interval; name the comparator; give the unit; say what the effect
does *not* move; report where the model failed.**

### 12.6 A limitation, weak → strong

Weak:

> Our model is a simplification of reality and has several limitations.

Strong (`25`, `24`, `09`):

> Our analysis has three main limitations. First, because the model does not represent
> households explicitly, we cannot evaluate interventions that act at the household level, such
> as household quarantine; the interventions we do evaluate are therefore a subset of those
> available to decision-makers, and our scenario set should not be read as the option set.
> Second, severity parameters were taken from a different population and may not transfer; we
> repeated the main analysis across the published range and the ranking of interventions was
> unchanged, although the absolute burden estimates shifted by up to 20%. Third, we could not
> separate the effects of interventions introduced in the same week, so the individual
> contributions we report for those measures should be treated as a joint effect. Quantifying
> them separately would require staggered implementation across comparable settings, which did
> not occur.

Each limitation: **what it is → the specific question it prevents you answering → what you did
about it → what would be needed to resolve it.**

### 12.7 Positioning against prior work

> Previous analyses have reached opposing conclusions: two studies concluded that reactive
> campaigns cannot influence measles outbreaks because transmission is too rapid, while three
> others reported substantial benefit in high-burden settings. These analyses differ in the
> delay they assume between outbreak detection and campaign implementation, which has not
> previously been varied systematically. We therefore treat that delay as the primary axis of
> our scenario analysis.

The move: **name the disagreement, identify the assumption that explains it, then make that
assumption your independent variable.**

### 12.8 A methods paragraph for a mechanistic fit

> We fitted the model to weekly reported cases using a Bayesian approach implemented in Stan.
> Reported cases were assumed to arise from a negative binomial observation process with mean
> equal to modelled incidence multiplied by a reporting probability ρ, and overdispersion φ. We
> estimated three parameters: the transmission rate β, ρ, and φ. We placed a log-normal prior
> on *R*₀ with mean 12 and standard deviation 3, reflecting published estimates for measles in
> comparable settings [ref]; a Beta(2, 8) prior on ρ, corresponding to a prior belief that
> roughly 20% of cases are reported; and an exponential prior with mean 1 on φ. Four chains were
> run for 2,000 warm-up and 2,000 sampling iterations each; convergence was assessed using the
> R-hat diagnostic (all R-hat < 1.01) and by visual inspection of trace plots. Analyses used R
> 4.3.1 and cmdstanr 0.7.1.

Present: observation model, exactly what is estimated, every prior **with its justification**,
full sampler settings, convergence diagnostics, software with versions.

### 12.9 A methods paragraph for a supervised model

> We trained a gradient-boosted classifier (LightGBM 4.1.0) to predict test positivity from
> seven routinely collected variables. Because the model is intended for prospective use, we
> split the data temporally rather than at random: individuals tested between 1 March and 30
> April (n = 41,208; 9.4% positive) formed the training set and those tested between 1 and 14
> May (n = 12,663; 8.1% positive) the held-out test set. All feature selection, hyperparameter
> tuning and threshold choice were performed within the training period using five-fold
> cross-validation; the test period was not examined until the model was final. Hyperparameters
> were selected by random search over 200 configurations, optimising cross-validated auROC; the
> selected values are given in Table S2 and in the accompanying repository. Missing values were
> handled natively by the boosting algorithm rather than imputed. We report auROC and auPRC with
> 95% confidence intervals from 1,000 bootstrap resamples of the test set, calibration by
> decile of predicted risk, and sensitivity and specificity at two operating points chosen to
> reflect the two triage thresholds in current use.

Present: algorithm with version, **split rationale and its axis**, the sentence that puts all
tuning inside the training fold, tuning procedure and objective, missing-data handling, and a
metric set that includes calibration and named operating points.

### 12.10 Reporting a bias check

> Because species that have been studied more intensively are more likely to have known
> pathogens, apparent trait associations could reflect research effort rather than biology. We
> included the number of disease-related publications per species as a covariate, which
> accounted for 29% of explained deviance. We additionally fitted a model of research effort
> itself using the same trait predictors; it explained little variation (pseudo-*R*² = 0.11),
> indicating that the trait profile distinguishing reservoirs is not the trait profile
> distinguishing well-studied species.

**Name the alternative explanation, adjust for it inside the model, then test it directly.**

### 12.11 Data and code availability

> **Data availability.** The line-list used in this analysis, de-identified in accordance with
> national health data regulations, is available at https://github.com/[org]/[repo], archived at
> https://doi.org/10.5281/zenodo.[id]. Aggregate surveillance data are available from [source].
> Where individual-level data could not be released, posterior samples for all reported estimates
> are provided in the same repository.
> **Code availability.** All analysis code, model specifications and the hyperparameter
> configuration required to reproduce every figure and table are available at the same
> repository and archived under the same DOI. Analyses used R 4.3.1; package versions are pinned
> in the accompanying `renv.lock`.
> **Role of the funding source.** The funders had no role in study design, data collection, data
> analysis, data interpretation, or writing of the report. The corresponding author had full
> access to all the data and had final responsibility for the decision to submit for publication.

### 12.12 Parameter table

One row per parameter; the *Status* column is the one reviewers use to find where uncertainty
was and was not propagated (`22`). Put the table in Methods, not the supplement, unless it
exceeds a page.

> **Table 1. Model parameters.** Fixed parameters were held at the stated value in all
> simulations; sampled parameters were drawn from the stated distribution for each of the
> [N] simulation runs; fitted parameters were estimated from the data described in
> §*Model calibration* and are reported as posterior median (95% CrI).
>
> | Parameter | Symbol | Value or distribution | Status | Source |
> |---|---|---|---|---|
> | Basic reproduction number | *R*₀ | [2.5 (95% CrI 2.1–2.9)] | Fitted | This study |
> | Mean incubation period (days) | 1/σ | [Lognormal, median 5.1, 95% range 2.2–11.5] | Sampled | [Lauer 2020] |
> | Mean infectious period (days) | 1/γ | [6.0] | Fixed | [ref] |
> | Proportion of infections subclinical | *p*ₛ | [Uniform(0.2, 0.5)] | Sampled | [ref], sensitivity analysis §2.5 |
> | Population size | *N* | [750,000] | Fixed | [census source, year] |
> | Initial number infectious | *I*(0) | [20] | Fixed | Assumption; varied in Table S3 |

Rules the template encodes: every parameter has a plain-language name *and* a symbol; units
are in the name, not the value; a distribution is given with its parameters or its quantiles,
not just its family; a fixed value that is really an assumption says so and points to the
sensitivity analysis that varies it; a fitted parameter's row is also the place its estimate
appears in Methods, so the reader is not sent to Results to find it.

### 12.13 Scenario-definition table

For intervention and NPI work (`25`): define each scenario as a change to something the model
actually has (a contact rate, a delay, a coverage), relative to a named baseline, and give each
a label that is then used unchanged in every figure, table and sentence (`08`).

> **Table 2. Intervention scenarios.** Each scenario is defined by the percentage change in
> setting-specific contacts relative to the pre-intervention baseline (scenario A), applied
> from [date] for [duration]. All other parameters are as in Table 1.
>
> | Scenario | Description | Home | School | Work | Other | Start | Duration |
> |---|---|---|---|---|---|---|---|
> | A | Baseline (no intervention) | 100% | 100% | 100% | 100% | — | — |
> | B | School closure | 100% | 0% | 100% | 100% | [date] | [12 weeks] |
> | C | Physical distancing | 100% | 100% | 50% | 25% | [date] | [12 weeks] |
> | D | Shielding of over-70s | 100% | 100% | 100% | 25% (over-70s only) | [date] | [12 weeks] |
> | E | Combined B + C + D | 100% | 0% | 50% | 25% | [date] | [12 weeks] |

For threshold or feasibility work (`22`, `23`), the columns are instead the swept parameters,
with the baseline row first and the grid stated explicitly:

> | Scenario set | *R*₀ | Initial cases | Delay to isolation | Contacts traced | Runs per combination |
> |---|---|---|---|---|---|
> | Baseline | 2.5 | 20 | Short (median 3.4 d) | 80% | 1,000 |
> | Sweep | 1.5, 2.5, 3.5 | 5, 20, 40 | Short, long (median 8.1 d) | 0–100% in 20% steps | 1,000 |

Write the caption so the table is self-contained: what the numbers are changes to, what they
are relative to, and when they apply. Then never renumber or rename a scenario after the first
draft — downstream text, figure legends and supplementary tables all key off these labels.

---

## Index of `writing_styles/`

| # | File | Paper | Archetype |
|---|---|---|---|
| 01 | `01-grais-2008-measles-orv-niamey.md` | Grais et al. 2008, *J R Soc Interface* | Policy counterfactual |
| 02 | `02-ferrari-2008-measles-sub-saharan-africa.md` | Ferrari et al. 2008, *Nature* | Dynamical systems |
| 03 | `03-keeling-2001-uk-foot-and-mouth.md` | Keeling et al. 2001, *Science* † | Real-time outbreak analysis |
| 04 | `04-earn-2000-simple-model-complex-transitions.md` | Earn et al. 2000, *Science* | Theoretical unification |
| 05 | `05-altizer-2006-seasonality-review.md` | Altizer et al. 2006, *Ecol Lett* † | Review |
| 06 | `06-keeling-rohani-2002-spatial-coupling.md` | Keeling & Rohani 2002, *Ecol Lett* † | Methods (validate a shortcut) |
| 07 | `07-lauer-2020-incubation-period.md` | Lauer et al. 2020, *Ann Intern Med* | Parameter estimation |
| 08 | `08-lee-2010-ml-propensity-scores.md` | Lee, Lessler & Stuart 2010, *Stat Med* | Simulation benchmark |
| 09 | `09-cramer-2022-covid-forecast-hub-evaluation.md` | Cramer et al. 2022, *PNAS* | Forecast evaluation |
| 10 | `10-reich-2019-flusight-multiyear.md` | Reich et al. 2019, *PNAS* | Forecast evaluation |
| 11 | `11-bracher-2021-weighted-interval-score.md` | Bracher et al. 2021, *PLoS Comput Biol* | Pedagogical methods |
| 12 | `12-ferguson-2006-mitigating-pandemic.md` | Ferguson et al. 2006, *Nature* | Scenario projection |
| 13 | `13-ferguson-2005-containing-pandemic-sea.md` | Ferguson et al. 2005, *Nature* | Feasibility threshold |
| 14 | `14-baker-2021-infectious-disease-global-change.md` | Baker et al. 2021, *Nat Rev Microbiol* | Synthesis review |
| 15 | `15-heesterbeek-2015-models-global-health.md` | Heesterbeek et al. 2015, *Science* | Field-defining review |
| 16 | `16-tian-2020-china-transmission-control.md` | Tian et al. 2020, *Science* | Natural-experiment evaluation |
| 17 | `17-grenfell-2001-travelling-waves.md` | Grenfell et al. 2001, *Nature* † | Pattern + mechanism |
| 18 | `18-bjornstad-2002-tsir-measles.md` | Bjørnstad et al. 2002, *Ecol Monogr* † | Long-form estimation |
| 19 | `19-kucharski-2020-early-dynamics-covid.md` | Kucharski et al. 2020, *Lancet Infect Dis* | Real-time Bayesian model |
| 20 | `20-nouvellet-2015-rapid-diagnostics-ebola.md` | Nouvellet et al. 2015, *Nature* | Strategy comparison |
| 21 | `21-weitz-2015-post-death-transmission-ebola.md` | Weitz & Dushoff 2015, *Sci Rep* | Identifiability critique |
| 22 | `22-hellewell-2020-contact-tracing-feasibility.md` | Hellewell et al. 2020, *Lancet Glob Health* | Feasibility |
| 23 | `23-li-2017-essential-information-ebola.md` | Li et al. 2017, *PNAS* | Decision analysis / VoI |
| 24 | `24-davies-2021-b117-transmissibility.md` | Davies et al. 2021, *Science* | Competing hypotheses |
| 25 | `25-davies-2020-npi-uk.md` | Davies et al. 2020, *Lancet Public Health* | Scenario projection |
| 26 | `26-abbott-2020-rt-estimation-tool.md` | Abbott et al. 2020, *Wellcome Open Res* | Living methods + tool |
| 27 | `27-gostic-2020-practical-considerations-rt.md` | Gostic et al. 2020, *PLoS Comput Biol* | Best-practice guidance |
| 28 | `28-charniga-2024-delay-distributions-best-practices.md` | Charniga et al. 2024, *PLoS Comput Biol* | Checklist / reporting standard |
| 29 | `29-bhatt-2013-global-dengue-distribution.md` | Bhatt et al. 2013, *Nature* | Risk mapping (BRT) — dengue |
| 30 | `30-ginsberg-2009-google-flu-trends.md` | Ginsberg et al. 2009, *Nature* | Digital surveillance — influenza |
| 31 | `31-lazer-2014-parable-of-google-flu.md` | Lazer et al. 2014, *Science* | Critique — influenza |
| 32 | `32-olival-2017-zoonotic-spillover-traits.md` | Olival et al. 2017, *Nature* | Trait prediction — spillover |
| 33 | `33-han-2015-rodent-reservoirs.md` | Han et al. 2015, *PNAS* | Trait prediction (BRT) — rodent zoonoses |
| 34 | `34-yang-2015-argo-influenza.md` | Yang et al. 2015, *PNAS* | Nowcasting (LASSO) — influenza |
| 35 | `35-wynants-2020-covid-prediction-models-review.md` | Wynants et al. 2020, *BMJ* | Critical appraisal — COVID-19 |
| 36 | `36-roberts-2021-ml-covid-imaging-pitfalls.md` | Roberts et al. 2021, *Nat Mach Intell* | Appraisal + guidance — COVID-19 |
| 37 | `37-zoabi-2021-covid-symptom-prediction.md` | Zoabi et al. 2021, *npj Digit Med* | Clinical prediction — COVID-19 |

† Full text is paywalled with no reachable open-access copy; these five files are built on the
verbatim abstract and bibliographic record, and say so at the top. Their abstract-level analysis
is reliable; they make no claims about section structure or results prose.
