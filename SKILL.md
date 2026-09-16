---
name: modelling-paper-writer
description: Write, structure, or revise infectious disease mathematical and statistical modelling papers in the style of the field's best-written work. Use when drafting or editing any section of a modelling manuscript (abstract, introduction, methods, results, discussion, limitations, data/code availability), when choosing how to report estimates and uncertainty, when positioning work against prior literature, or when the user asks for help with an epidemiological modelling paper, preprint, or report. Covers transmission models, forecasting and forecast evaluation, parameter estimation, intervention and scenario analysis, decision analysis, reviews, best-practice guidance or reporting-standard papers, and machine learning / predictive modelling papers (risk mapping, digital surveillance, clinical prediction). Includes worked examples for model definitions, abstracts, methods, results, limitations and availability statements. Not for empirical or observational studies without a modelling component.
---
# Writing infectious disease modelling papers

*Developed by James Azam (https://github.com/jamesmbaazam). Licensed MIT.*

Rules distilled from 37 well-written infectious disease modelling, statistical and machine
learning papers (2000–2024; *Nature*, *Science*, *PNAS*, the *Lancet* family, *BMJ*, *PLoS
Comput Biol* and others; 11 of 37 are COVID-19). The corpus is landmark work from a narrow set
of groups, chosen for writing quality, not sampled systematically; rules from the 2000–2008
papers may predate current reviewer expectations.

| File | What it holds | Read it when |
|---|---|---|
| `SKILL.md` (this file) | Procedure, rules as imperatives, anti-patterns, checklist | Always |
| `references/evidence.md` | The corpus quotations behind each rule, same § numbering | You need the sentence-level detail, or the user asks *why* |
| `references/examples.md` | Worked template passages (§12.1–§12.13) | Drafting a model definition, abstract, methods paragraph, limitations, tables, availability statement |
| `references/corpus-index.md` | Author YEAR → `writing_styles/` file | Finding the exemplar for an archetype |
| `writing_styles/NN-*.md` | One style analysis per paper, with verbatim quotations | Step 3 of the procedure |

## Procedure

1. **Determine the mode.** *Draft* from a brief; *revise* a pasted draft; or *critique* only.
   In critique mode do not rewrite unless asked. In revise mode follow the hard rules on voice.
2. **Establish the archetype (§0), target venue and word budget (§1.2).** If any of these is
   not inferable from the request, ask before drafting; a Lancet abstract and a Nature abstract
   are different objects.
3. **Read the matching `writing_styles/` file.** Find it via the archetype table below or
   `references/corpus-index.md`, then `Read` it. This is not optional: it holds the
   sentence-level moves this file only names. Read `references/examples.md` §12.N when a rule
   below points to it.
4. **Draft or edit the requested section only.** Do not produce a whole paper when asked for a
   paragraph, and do not add sections the user did not ask for.
5. **Self-review against §11** before returning. Fix what fails; where you cannot (missing
   numbers, missing sources), say so and list what the user must supply.
6. **Return the text, then a short note** of the placeholders left, the assumptions made, and
   anything the target journal will require that the user has not mentioned.

## Hard rules

These override everything below.

- **Never invent a citation, DOI or author.** Use `[ref]` or `[Author YEAR]` placeholders and
  list, at the end, every claim that still needs a source.
- **Never invent a number.** If the user has not supplied a result, write a placeholder in the
  shape the sentence needs — `[X% (95% CrI [a–b])]` — not a plausible value.
- **Never reuse corpus sentences verbatim** in the user's manuscript. The quotations in
  `references/` and `writing_styles/` show the *move*; write the user's version of it.
- **In revision mode, preserve the author's voice**, spelling variant (UK/US) and tense. Show
  edits (before/after or a change list) rather than silently rewriting, and do not expand
  beyond the section you were asked to touch.
- **Journal typography is not a style rule.** Middle-dot decimals (`2·5`) and "to" in place of
  an en dash inside intervals are *Lancet* house style, reproduced in quotations from Lancet
  papers; use ordinary decimal points and en dashes unless the target journal says otherwise.
- **Journal limits in §1.2 drift.** Verify them against the current author guidelines.

---

## 0. First decide the archetype

Almost every choice below follows from what kind of paper this is. Identify the archetype
before writing a word. → `evidence.md` §0

| Archetype | What it delivers | Exemplars (`writing_styles/`) |
|---|---|---|
| **Parameter estimation** | One quantity, cleanly estimated, translated into a decision | Lauer 2020 |
| **Real-time transmission analysis** | R_t or dynamics fitted to a live outbreak | Kucharski 2020, Abbott 2020, Tian 2020, Keeling 2001 (abstract only) |
| **Scenario projection for policy** | A ladder of intervention scenarios, projected forward | Davies 2020, Ferguson 2006 |
| **Feasibility / threshold** | The parameter boundary at which a strategy works | Ferguson 2005, Hellewell 2020 |
| **Policy counterfactual** | What a past intervention achieved, and what alternatives would have | Grais 2008, Nouvellet 2015 |
| **Competing hypotheses** | Several mechanisms formalised, fitted and ranked | Davies 2021 |
| **Forecast evaluation** | Many models, one scoring rule, a verdict | Cramer 2022, Reich 2019, Bracher 2021 |
| **Dynamical systems** | A system shown to sit in a different regime than assumed | Ferrari 2008, Earn 2000, Bjørnstad 2002, Grenfell 2001 |
| **Methods / simulation benchmark** | A tool, a validation, or a demonstration of what cannot be inferred | Lee 2010, Bracher 2021, Keeling & Rohani 2002, Weitz 2015, Li 2017 |
| **Review** | A framework that organises a scattered literature | Baker 2021, Heesterbeek 2015, Altizer 2006 |
| **Best-practice guidance** | Recommendations or reporting standards for a method others use | Gostic 2020, Charniga 2024 |
| **Risk mapping / trait prediction** | A supervised model producing a surface or a ranked candidate list | Bhatt 2013, Olival 2017, Han 2015 |
| **Digital surveillance / nowcasting** | A surveillance quantity estimated faster than surveillance | Ginsberg 2009, Yang 2015 |
| **Clinical prediction model** | A patient-level classifier with an intended point of care | Zoabi 2021 |
| **Critique / appraisal** | A verdict on a method or a literature, plus named failure modes | Lazer 2014, Wynants 2020, Roberts 2021 |

The archetype fixes the **shape of the headline claim**: estimation → a number with an
interval; feasibility → a threshold; scenario → a comparison against a named reference
scenario; counterfactual → a percentage averted relative to what happened; evaluation → a
score relative to a naïve baseline; dynamical → a regime; methods → a limit on what the data
can identify; guidance → a direction and magnitude of bias plus a recommendation; risk mapping
→ a burden or a named candidate list, never the AUC; nowcasting → a reduction in reporting lag
against a naive alternative; clinical prediction → a discrimination metric with an interval
and a named operating point; critique → a named failure mode.

---

## 1. Structure

**Titles** → `evidence.md` §1.0
- **Pick one of four shapes**: a claim (*Host and viral traits predict zoonotic spillover*);
  verb phrase + estimand + data (*Estimating the time-varying reproduction number… using…
  case counts*); quantity + pathogen + place (*The global distribution and burden of dengue*);
  or strategy/question (*Feasibility of controlling COVID-19 outbreaks by…*).
- **Name the estimand and the pathogen/place, not the model.** Method goes in a colon
  subtitle if anywhere; a claim title needs a claim the Discussion defends.
- **Lancet family appends `: a mathematical modelling study`**; 10–18 words; cut *A study of*,
  *Novel*, *Towards*, *Insights into*.

**Abstract** → `evidence.md` §1.1, `examples.md` §12.2
- **Build on the six-move spine**: burden (quantified, dated) → specific gap → "Here, we…"
  (model class + data) → headline result with uncertainty → the bounding caveat → what should
  now change. Never withhold the headline number.
- **Write to the budget from the first draft** (§1.2 table in `evidence.md`): Lancet 300 words
  in five fields, Nature 150, Science 125, PNAS 250 + 120-word Significance, BMJ 400
  structured, Annals 275 with a one-sentence `Limitation`. Findings is the field to protect.
- **Draft the Lancet `Research in context` panel first** (evidence before / added value /
  implications) even when the journal does not require it.

**Journal templates** → `evidence.md` §1.2
- **Nature/Science**: no IMRaD headings; short topic subheadings; Methods at the end or in SI.
- **PNAS**: Significance → Abstract → Intro → Results (declarative subheadings) → Discussion
  → Methods last.
- **Lancet**: structured abstract → Research in context → IMRaD with *Role of the funding
  source* → Data sharing → Contributors → Declarations.
- **PLoS / methods journals**: numbered subsections are fine; add an Author Summary.
- **Clinical journals**: fully labelled abstract; Reproducible Research Statement.

**Subheadings and introduction** → `evidence.md` §1.3–§1.4
- **Make Results subheadings declarative** where allowed; read in order they are the argument.
- **Give a pre-empted objection or a known bias its own heading** (*Apparent growth … not a
  result of testing artifacts*).
- **Introduction in five moves**: system + burden → what is established → what follows →
  the gap as a checkable claim → the questions, listed, answered in order later.
- **Use the expectation-violation opening when you can**: derive what canonical theory
  predicts for this system, then show the data refuse it.

---

## 2. Methods

**Mathematics** → `evidence.md` §2.1, `examples.md` §12.1
- **Main text carries the argument, not the algebra.** General-science journals: no
  equations, model named and described in words. Methods journals: displayed, numbered
  equations, complexity built one subsection per step.
- **Always name compartments in words on first use and state the flows**; never assume
  "SIR" is self-explanatory. Gloss every symbol epidemiologically (β is *the transmission
  rate between…*). Give the analytic bound alongside the simulation where one exists.
- **When you add a compartment, say what it changes about the answer**, not that it is more
  realistic.
- **Match the user's toolchain**: LaTeX `align` for LaTeX users, Unicode for Word
  (`examples.md` §12.1).

**Assumptions** → `evidence.md` §2.2, `examples.md` §12.4
- **One flat declarative sentence per assumption, with its reason and a pointer to where it
  is tested.**
- **State the direction of the bias**, not just its existence ("relaxing this would decrease
  the probability that control is achieved"). The single most valuable habit in the corpus.
- **Claim conservatism only when you can defend it**, then repeat the word deliberately.

**Parameters and priors** → `evidence.md` §2.3, `examples.md` §12.8, §12.12
- **Parameter table with name, symbol, value or distribution, fixed/sampled/fitted status,
  and source.** The status column is what reviewers use.
- **Give distribution, both moments, and source**; justify the family biologically; test
  alternatives in an appendix.
- **When you change a prior, report the old one and why.** Give MCMC detail in full: chains,
  warm-up, samples, diagnostic.
- **Where a parameter is unknowable, say so and route around it** with sensitivity analysis.

**Scenarios** → `evidence.md` §2.4, `examples.md` §12.13
- **Declare a baseline and vary one thing at a time from it**; enumerate the grid in Methods
  before any result.
- **Define NPI scenarios as percentage changes to contacts by setting, in a table**; label
  scenarios with stable codes and never renumber.
- **Sweep effect sizes** so conclusions can be thresholds; present key results under two or
  more labelled scenarios where the governing parameter is genuinely uncertain.

**Sensitivity and software** → `evidence.md` §2.5–§2.6
- **Report each sensitivity analysis with its conclusion in the same sentence**, named by
  what was varied. Design a targeted secondary analysis to kill a specific alternative
  explanation.
- **Name language, version, packages and their versions; pin the data-lock date.**

---

## 3. Results

**Uncertainty** → `evidence.md` §3.1, `examples.md` §12.5
- **Use the interval that matches the object and label it**: 95% CI (frequentist), 95% CrI
  (posterior), 95% PI (simulated future), median [IQR] or 50%/95% (ensemble), mean ± SD or
  range (across models). Keep the kinds distinct within a paper.
- **Lead with the policy-relevant quantile, not the mean** (the 97.5th percentile of the
  incubation period sets the quarantine window). Translate small probabilities to natural
  frequencies.
- **A null result gets an interval that spans both directions**, stated as such.

**Comparators and sentence shapes** → `evidence.md` §3.2–§3.3
- **Give every number a comparator**: a naive baseline glossed in plain English, a capacity
  constraint, a named reference scenario, a canonical system, or a historical epidemic.
  Nothing is "good" or "large" in the abstract.
- **Reusable shapes**: the gradient in one sentence (38, 27 and 20% at 60, 90 and 120 days);
  intervention → what it moves → what it does not → the condition ("but only if…");
  verdict → "however" → the numbers; the concessive inside the headline claim; unexpected
  result plus its mechanism in the same sentence.

**Verbs and failures** → `evidence.md` §3.4–§3.5
- **Grade verbs and modals to the design**: *associated with* for observational designs; the
  model *suggests*; *would have* → *could have* → *might have* as the premise gets more
  hypothetical. Claim qualitative agreement when that is what you have.
- **Never write "biased" or "sensitive to" without direction, and where possible magnitude
  and timing.**
- **Report where the model failed, in the Results**, not buried in the Discussion.

**Figures and tables** → `evidence.md` §3.6
- **Decide the main-text/supplement split before drafting**: main text gets one item per
  headline claim plus the parameter (and scenario) table — typically a fit/validation
  figure, a headline-result figure and a what-governs-it figure. Supplement gets full
  equations, remaining sensitivity analyses, diagnostics, breakdowns, the reporting checklist;
  cite every supplementary item from the sentence it supports.
- **Table for look-up and comparison across labelled scenarios; figure when the shape is the
  finding.** Never both for the same numbers.
- **Captions stand alone**: what is plotted and what the band is, under which parameters, and
  what to see. Observed data overlaid on simulations; parameters in the caption; baseline
  in every panel; one colour per scenario across the whole paper; axes labelled with quantity
  and unit.
- **Tables**: baseline row first, interval in the same cell as the estimate, unit in the
  header, precision the data support.

---

## 4. Literature

→ `evidence.md` §4, `examples.md` §12.3, §12.7
- **State the gap as a checkable claim** ("we identified no estimates that jointly fitted…"),
  never "little is known".
- **Position by one of seven moves**: adjudicate a disagreement; claim rigour not novelty;
  displace the received view without demolishing it; attack the incumbent by its consequence;
  show correct work misapplied; diagnose non-adoption rather than non-existence; claim a
  different audience and format.
- **Citation density is an archetype choice**: sparse in general-science policy papers,
  moderate in empirical modelling, dense clusters in dynamical-systems papers, 150+ in
  reviews. Concentrate them in the Introduction and where parameters are justified.
- **Anchor plausibility to relatives of the pathogen; use a historical epidemic as a
  mechanistic analogy with the mechanism spelled out; cite preprints, dated, without apology.**

---

## 5. Voice

→ `evidence.md` §5
- **First-person plural, always.** Passive only for the evaluation protocol and data
  provenance.
- **Present tense for biology, model structure and standing implications; past for what was
  done and observed.**
- **Hedge the inference, not the number**, and hedge decisions rather than estimates when
  writing for policy. Concede the alternative in the same paragraph as your choice.
- **Replace every vague quantifier with a number, a date or a name.** "Recently" is
  unreadable in three years; "23 January 2020" is readable forever.

---

## 6. Domain conventions

→ `evidence.md` §6, `examples.md` §12.11
- **Teach the R₀ control logic once, from first principles**, when readers may not be
  modellers; say which of R₀ / R_t / R_e you mean and define the instantaneous reproduction
  number explicitly.
- **Report validation as out-of-sample and say so**; separate accuracy from calibration;
  name and interpret proper scoring rules on an interpretable scale; rank competing model
  structures on an explicit criterion and report the runners-up.
- **When parameters trade off, make the identifiability limit the result** and find the
  conclusion that holds across the indeterminate set.
- **Make the decision relevance explicit**: test whether disagreement changes the action;
  price uncertainty in decision units (EVPI); attach a logistics or ethics checkpoint to every
  endorsed intervention; define a numeric vocabulary for posterior probabilities before use.
- **Real-time work**: data-lock date on every count; demote forecasts relative to estimates;
  version article and software together; ship a tool.
- **Availability**: GitHub is not archival — pair it with a Zenodo DOI pinned to the
  submitted version; name language, version, packages; share de-identified line lists, or
  posterior samples where raw data cannot be released; funder-role sentence; contributions.
- **Name the reporting guideline in Methods and attach its checklist**: Bennett 2012 or
  ISPOR-SMDM for any modelling study; EPIFORGE (forecasting); ODD (agent-based); CHEERS
  (economic); TRIPOD+AI / PROBAST / CLAIM (prediction); PRISMA (reviews); STROBE/RECORD
  (observational components).

---

## 7. Machine learning and predictive modelling

→ `evidence.md` §7, `examples.md` §12.9–§12.10. Everything in §1–§6 still applies.
- **Lead with the problem and the burden, never the algorithm or the AUC.** Name the method
  once and justify it by a property of the data.
- **Structure Methods as the pipeline in execution order** (database → covariates →
  fitting → validation → burden), each stage independently auditable.
- **State the train/test split in one unambiguous sentence** ("…excluded from all previous
  steps") and split along the axis you will extrapolate over — temporal or geographic, not
  random. Feature selection, tuning and thresholds live inside the training fold.
- **Report performance with an interval, against a naive baseline, with calibration, and
  (under imbalance) auPRC; give two named operating points; state what made the benchmark
  fair.** Metric set in a fixed order in every table.
- **Confront training-data bias explicitly**: put sampling effort in the model as a
  covariate; fit a model of your own sampling process and show it does not reproduce the
  result; retrain without distrusted features and publish the cost; name the confound that
  could mimic your signal.
- **Interpretation is a result**: importance *and* partial dependence; unify top variables
  into one concept; report the covariate that did not matter; state the adjustment inside
  the claim sentence; ship predictions as a named, falsifiable list.
- **Say which numbers are ordinal**, and localise uncertainty to the places it is largest.
- **Pre-submission appraisal (Wynants 2020, Roberts 2021)**: no outcome leakage, no
  case-control reported as cohort, ≥20 events per variable, calibration assessed, external
  validation on a representative set, architecture benchmarked, no "Frankenstein datasets",
  a usable model artefact, predictors chosen from prior knowledge not data alone.
- **Google Flu Trends lessons**: beat a boring benchmark or drop the claim; nonsense
  predictors surfacing is evidence about the procedure; build in recovery (rolling
  retraining) because platform data-generating processes change.

---

## 8. Discussion and limitations

→ `evidence.md` §8, `examples.md` §12.6
- **Open by naming what the work shows or the tension it exposes**, not by restating the
  abstract. Then interpretation → comparison with prior estimates → limitations → what
  should change. Close on a decision, a data priority, or a question — not a summary.
- **Signpost limitations plainly, then cover six categories**: simplification; data quality
  and provenance; contested parameters; design; scope fences against foreseeable
  misreadings; irreducible uncertainty (distinguished from fixable gaps).
- **Name the specific question each limitation prevents you answering**, not just that the
  model simplifies.
- **Discharge what you can** by sensitivity analysis or direction-of-bias argument, and say
  which limitations remain live.
- **Frame limitations as design choices where they were choices; pre-empt the tempting but
  invalid follow-up analysis; disclose how illustrative evidence was selected; name the hard
  boundary no method can fix.**
- **Convert each limitation into the next research question in the following sentence.**

---

## 9. Best-practice and guidance papers

→ `evidence.md` §9. Overrides §1–§8 where they conflict.
- **Structure by the problems a practitioner hits, in the order they hit them, or by the
  tasks in a workflow** — not IMRaD. Instruction sections get imperative headings.
- **End every substantive section with a bulleted summary** so the summaries alone are
  usable; make the checklist the deliverable; add a decision flowchart branching on what
  data the reader has.
- **Simulate a known truth, then degrade the data one imperfection per section**, so every
  "what does this do to the estimate, and by how much?" is checkable.
- **Quantify the cost of bad practice** three ways: a before/after pair on a familiar
  parameter, a worst-case magnitude, and the downstream consequence for the quantity people
  actually use.
- **"We recommend", specifically and repeatedly; never "must".** Say what you do *not*
  recommend, with a structural reason. Hedge applicability, not confidence.
- **Name methods after their authors, run each in its canonical implementation, count its
  parametric assumptions, and organise everything around one small closed set of problems.**

---

## 10. Anti-patterns

Absent from every paper in the corpus. Do not write them.

- "Little is known about X" — state a checkable claim about what you searched for and did not find.
- "This is the first study to…" — the *first-study* claim is the problem, not the hedge. Claim
  scope or rigour instead; "none, to our knowledge, has…" attached to a checkable claim is fine.
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

Run this before returning any drafted or revised section. Only the blocks relevant to the
section and archetype apply.

**Before drafting**
- [ ] Archetype identified; the matching file in `writing_styles/` read.
- [ ] Journal template and word budget chosen; heading scheme decided.
- [ ] Headline claim written as one sentence in the right shape for the archetype.
- [ ] `Research in context` panel drafted (whether or not the journal wants it).

**Methods**
- [ ] Model named, its class stated, structure described in words before any equation.
- [ ] Every assumption a declarative sentence with a reason and, where possible, a direction of bias.
- [ ] Parameter table with sources and a fixed/sampled/fitted column (`examples.md` §12.12).
- [ ] Baseline scenario declared; scenario grid enumerated exhaustively (`examples.md` §12.13).
- [ ] Priors stated with justification; MCMC/computation detail complete.
- [ ] Sensitivity analyses named by what they vary, each reported with its conclusion.
- [ ] Software, versions, packages, data-lock date.

**Results**
- [ ] Every estimate has the right kind of interval, labelled and used consistently.
- [ ] Every number has a comparator (baseline, capacity, reference scenario, prior literature).
- [ ] Policy-relevant quantile leads, not the mean.
- [ ] Where the model failed, that is in the Results.
- [ ] Verbs and modals graded to the design and to the evidence.
- [ ] Figures: parameters in captions; observed data overlaid on simulations; baseline in every panel.

**Discussion**
- [ ] Opens with the tension or the general lesson, not a restatement.
- [ ] Limitations signposted, categorised, discharged where possible, with scope fences for
      foreseeable misreadings.
- [ ] Each limitation names the question it blocks and becomes a research question in the next sentence.
- [ ] Closes on a decision, a data priority, or a question.

**Back matter**
- [ ] Data and code: repository **plus** archived DOI; licence; language and version.
- [ ] Individual-level data shared and de-identified, or posterior samples published instead.
- [ ] Funder role, conflicts, preprint disclosure, per-author contributions.
- [ ] Reporting guideline named (§6) and its checklist attached.

**Hard rules**
- [ ] No invented numbers, citations or DOIs; every placeholder listed for the user.
- [ ] No corpus sentence reused verbatim.
- [ ] Revision mode: voice, spelling and tense preserved; edits shown; scope not expanded.

**Additionally, for machine learning / predictive modelling papers (§7)**
- [ ] Problem and burden lead; algorithm named once and justified by a property of the data.
- [ ] Methods subheadings are the pipeline stages in execution order.
- [ ] Split stated in one sentence, along the axis of intended extrapolation, with everything
      held out *before* any tuning.
- [ ] Performance with an interval, against a naive baseline, plus calibration and (under
      imbalance) auPRC; benchmark fairness stated.
- [ ] Sampling bias modelled or tested, not merely acknowledged; the mimicking confound named.
- [ ] Variable importance and partial effects; the null result reported; adjustment stated
      inside the claim sentence.
- [ ] Predictions released as a named, falsifiable list; ordinal quantities labelled as relative.
- [ ] Checked against the §7 appraisal list; TRIPOD+AI or equivalent named.

**Additionally, for best-practice or guidance papers (§9)**
- [ ] Sections are problems or tasks; instruction sections have imperative headings.
- [ ] Every substantive section ends with a bulleted summary; the summaries alone are usable.
- [ ] Evidence comes from synthetic data with a known truth, degraded one imperfection per section.
- [ ] Every recommendation has the cost of ignoring it, quantified and traced downstream.
- [ ] Direction, magnitude and timing given for every bias.
- [ ] At least one explicit negative recommendation, with a structural reason.
- [ ] A closed, named set of problems, used consistently across all tables and figures.
- [ ] Checklist and/or decision flowchart branching on what data the reader has.
- [ ] Scope disclosed: illustrative examples labelled as such; the hard boundary named.
