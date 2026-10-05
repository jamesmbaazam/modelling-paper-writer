---
name: modelling-paper-writer
description: Writes, structures, revises and critiques infectious disease mathematical, statistical and machine learning modelling papers in the style of the field's best-written work. Use when drafting, editing or reviewing any section of a modelling manuscript (title, abstract, introduction, methods, results, discussion, limitations, data and code availability), when choosing how to report estimates and uncertainty, when positioning work against prior literature, or when the user asks for help with an epidemiological modelling paper, preprint or report. Covers transmission models, forecasting and forecast evaluation, parameter estimation, intervention and scenario analysis, decision analysis, reviews, best-practice guidance and reporting-standard papers, and machine learning or predictive modelling papers (risk mapping, digital surveillance, clinical prediction). Not for empirical or observational studies without a modelling component.
license: MIT
metadata:
  author: James Azam
  version: "1.0.0"
  repository: https://github.com/jamesmbaazam/modelling-paper-writer
---
# Writing infectious disease modelling papers

Rules distilled from 81 well-written infectious disease modelling, statistical and machine
learning papers (2000–2024; *Nature*, *Science*, *PNAS*, the *Lancet* family, *BMJ*, *PLoS
Comput Biol* and others; 25 of 81 are COVID-19). The corpus is landmark work from a narrow set
of groups, chosen for writing quality, not sampled systematically; rules from the 2000–2008
papers may predate current reviewer expectations. Rules marked ◆ come from reporting guidelines
or journal instructions rather than the corpus; check them against the current source.

| File | Holds | Read it when |
|---|---|---|
| `references/checklist.md` | The self-review checklist | Step 5, every time |
| `references/corpus/NN-*.md` | One style analysis per paper, with verbatim quotations, under the canonical headings listed in step 3 | Step 3: one file, never the folder; only the matching section unless the task is a full paper, abstract or critique |
| `references/corpus-index.md` | Author YEAR → file, venue, archetype, full-text status | §0 does not settle the exemplar |
| `references/corpus/papers.csv` | Title, DOI and authors per paper | You need a corpus paper's bibliographic detail for your own reference — never to build the user's reference list |
| `references/ml-prediction.md` | §7 rules, anti-patterns, checklist | Risk mapping, nowcasting, clinical prediction, ML critique |
| `references/guidance-papers.md` | §9 rules, anti-patterns, checklist | Best-practice guidance |
| `references/examples.md` | Worked passages §12.1–§12.13 | A rule points to §12.N |
| `references/evidence.md` | Corpus quotations behind each rule, same § numbers; §1.2 venue templates and budgets | Critiquing, a rule too terse to apply, the user asks *why*, a venue's headings. Never read it whole (1,200+ lines): take the §N.M you need from its Contents, `grep -n '^##'` for that heading and the next, and `Read` only that range |

## Procedure

1. **Determine the mode.** *Draft* from a brief; *revise* a pasted draft; or *critique* only.
   In critique mode do not rewrite unless asked. In revise mode follow the hard rules on voice.
2. **Establish the archetype (§0), and the venue and word budget (§1) only where the
   section's shape depends on them**: titles, abstracts, heading schemes and full papers. A
   Lancet abstract and a Nature abstract are different objects, so for those ask if the venue
   is not inferable. For any other section, do not ask: assume a sensible default and state it
   in the closing note. Ask about the archetype only if two candidates would give materially
   different text.
3. **Read one `references/corpus/` file — never the folder.** Pick it from §0 (the exemplar
   closest to the user's venue and design) or `references/corpus-index.md`. This is not
   optional: it holds the sentence-level moves this file only names. Every corpus file is now
   built on the paper's full text. For one section,
   `grep -n '^## '` the file and read only the heading that matches, plus `## Distinctive
   moves to borrow`. Every full-text file uses the same canonical headings, which match the
   rule sections below: `Structure`, `Opening move`, `Methods`, `Results`, `Literature`,
   `Voice`, `Discussion and limitations`, `Data, code and funding`, `Distinctive moves to
   borrow` — some carry a trailing `— …` gloss, so match on the prefix. A file may add
   topical sections of its own; read one if its title names what you need. If the section you
   want is absent, read `## Structure` and `## Distinctive moves to borrow` and take the
   sentence-level detail from `evidence.md` instead. For ML or guidance archetypes, also read
   the reference file named in §7 or §9.
4. **Draft or edit the requested section only.** Do not produce a whole paper when asked for a
   paragraph, and do not add sections, panels or boxes the user did not ask for. Scaffolding
   this file recommends (the headline-claim sentence, the `Research in context` triplet) is for
   your own planning; return it only if the journal requires it or the user asks.
5. **Self-review against `references/checklist.md`**, running the blocks that apply. Fix
   what fails; where you cannot (missing numbers, missing sources), say so and list what the
   user must supply.
6. **Return the text, then a short note** of the placeholders left, the assumptions made, and
   anything the target journal will require that the user has not mentioned.

## Hard rules

These override everything below.

- **Never invent a citation, DOI or author.** Cite as `[Author YEAR]` only papers the user
  supplied. Anything else is `[ref]`, or `[Author YEAR?]` when you recall a specific paper;
  the `?` marks it unverified, however sure you feel. Never write a DOI, journal, volume or
  page from memory — not in the text, and not in the verify list either. After the text, list
  every citation for the user to verify and every claim that still has no source. A verify-list
  entry is the author, the year, and a short phrase for what the paper is about; that is enough
  for the user to find it, and anything more is something you would be inventing.
- **The corpus is a style corpus, not a bibliography.** Which papers belong in the manuscript
  is decided by what it argues, not by what this skill happens to have analysed. A corpus
  paper gets cited only if it genuinely belongs in *this* literature, and then it is a recalled
  citation like any other — `[Author YEAR?]`, on the verify list. The `Author YEAR` labels
  throughout `references/` attribute the *rules* to their source; they are not a reading list
  for the user.
- **Never invent a number.** If the user has not supplied a result, write a placeholder in the
  shape the sentence needs — `[X% (95% CrI [a–b])]` — not a plausible value.
- **Never reuse corpus sentences verbatim** in the user's manuscript. The quotations under
  `references/` show the *move*; write the user's version of it.
- **In revision mode, preserve the author's voice**, spelling variant (UK/US) and tense. Show
  edits (before/after or a change list) rather than silently rewriting, and do not expand
  beyond the section you were asked to touch.
- **Journal typography is not a style rule.** Middle-dot decimals (`2·5`) and "to" in place of
  an en dash inside intervals are *Lancet* house style, reproduced in quotations from Lancet
  papers; use ordinary decimal points and en dashes unless the target journal says otherwise.
- **Journal limits (`evidence.md` §1.2) drift.** Verify them against the current author
  guidelines, and say in the closing note that you have not.

---

## 0. First decide the archetype

Almost every choice below follows from what kind of paper this is, and the archetype fixes
the shape of the headline claim. Identify it before writing a word. → `evidence.md` §0

| Archetype | Headline claim shape | Exemplars (`references/corpus/`) |
|---|---|---|
| **Parameter estimation** | A number with an interval, translated into a decision | Lauer 2020, Ganyani 2020, Stopard 2021, Simmons 2013 |
| **Real-time transmission analysis** | A dated R_t or growth estimate with an interval | Kucharski 2020, Abbott 2020, Tian 2020, Keeling 2001, Thompson 2019, Zhao 2020, Günther 2021, Camacho 2015 |
| **Scenario projection for policy** | A comparison against a named reference scenario | Davies 2020, Ferguson 2006, Ngonghala 2020, Kerr 2021b, Rock 2022 |
| **Feasibility / threshold** | The parameter threshold at which a strategy works | Ferguson 2005, Hellewell 2020, Famulare 2018, Golumbeanu 2022, Kucharski 2016 |
| **Policy counterfactual** | A percentage averted relative to what happened | Grais 2008, Nouvellet 2015, Verguet 2015, Rock 2022 |
| **Competing hypotheses** | The best-supported mechanism, with the runners-up | Davies 2021, Lavine 2021, Yakob 2015, Lopman 2012 |
| **Forecast evaluation** | A score relative to a naïve baseline | Cramer 2022, Reich 2019, Bracher 2021a, Funk 2019, Sherratt 2023, Bosse 2023, Bracher 2021b, Wolffram 2023 |
| **Dynamical systems** | A regime, different from the one assumed | Ferrari 2008, Earn 2000, Bjørnstad 2002, Grenfell 2001, Griffin 2015 |
| **Methods / simulation benchmark** | A limit on what the data can identify | Lee 2010, Bracher 2021a, Bosse 2023, Keeling & Rohani 2002, Weitz 2015, Li 2017, Ajelli 2010 |
| **Review** | A framework that organises a scattered literature | Baker 2021, Heesterbeek 2015, Altizer 2006, Jackson 2014 |
| **Best-practice guidance** | A direction and magnitude of bias, plus a recommendation | Gostic 2020, Charniga 2024, Thompson 2019 |
| **Risk mapping / trait prediction** | A burden or a named candidate list, never the AUC | Bhatt 2013, Olival 2017, Han 2015 |
| **Digital surveillance / nowcasting** | A reduction in reporting lag against a naive alternative | Ginsberg 2009, Yang 2015 |
| **Clinical prediction model** | A discrimination metric with an interval and a named operating point | Zoabi 2021, Yadaw 2020, Berenguer 2021 |
| **Critique / appraisal** | A named failure mode | Lazer 2014, Wynants 2020, Roberts 2021 |
| **Vaccine impact / economic evaluation** | Deaths and DALYs averted, and an ICER against a named threshold | Chen 2019, Watson 2022, Abbas 2020 |
| **Phylodynamics / genomic epidemiology** | Introductions partitioned by what they led to | Geoghegan 2020, Grubaugh 2017, Lemieux 2021 |
| **Serological inference** | A force of infection, and cumulative exposure by age | Prayitno 2017, Ximenes 2014, Golden 2016, Hay 2024 |
| **Within-host dynamics** | The mechanism a feature of the viral curve requires | Pawelek 2012, Néant 2021, Clapham 2014 |
| **Agent-based model documentation** | A model others can install, calibrate and interrogate | Kerr 2021a, Kerr 2021b, Ajelli 2010 |
| **Nowcasting / reporting delays** | A corrected present, scored against the eventual truth | McGough 2020, Günther 2021, Wolffram 2023 |
| **Rapid-response outbreak analysis** | A dated forecast of cases and the resources they need | Finger 2019, Camacho 2015, Shi 2016 |

---

## 1. Structure

**Titles** → `evidence.md` §1.0
- **Pick one of four shapes**: a claim (*Host and viral traits predict zoonotic spillover*);
  verb phrase + estimand + data (*Estimating the time-varying reproduction number… using…
  case counts*); quantity + pathogen + place (*The global distribution and burden of dengue*);
  or strategy/question (*Feasibility of controlling COVID-19 outbreaks by…*).
- **Name the estimand and the pathogen/place, not the model.** Method goes in a colon
  subtitle if anywhere; a claim title needs a claim the Discussion defends.
- **Lancet family appends `: a mathematical modelling study`**. Aim for 8–13 words (the
  corpus median is 10; *Nature* and *Science* run shortest); cut *A study of*, *Novel*,
  *Towards*, *Insights into*.

**Abstract** → `evidence.md` §1.1, `examples.md` §12.2
- **Build on the six-move spine**: burden (quantified, dated) → specific gap → "Here, we…"
  (model class + data) → headline result with uncertainty → the bounding caveat → what should
  now change. Never withhold the headline number.
- ◆ **Write to the budget from the first draft** (§1.2 table in `evidence.md`): Lancet 300 words
  in five fields, Nature 150, Science 125, PNAS 250 + 120-word Significance, BMJ 400
  structured, Annals 275 with a one-sentence `Limitation`. Findings is the field to protect.
- **For an abstract or full paper, plan with the Lancet `Research in context` triplet**
  (evidence before / added value / implications), one sentence each, even when the journal
  does not require the panel. It is scaffolding: return it only if the journal requires it or
  the user asks.

**Journal templates** → `evidence.md` §1.2. Read it before setting a heading scheme
(Nature/Science topic subheadings, PNAS Methods last, Lancet back matter, PLoS Author Summary).

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
- ◆ **Match the user's toolchain**: LaTeX `align` for LaTeX users, Unicode for Word
  (`examples.md` §12.1).

**Assumptions** → `evidence.md` §2.2, `examples.md` §12.4
- **One flat declarative sentence per assumption, with its reason and a pointer to where it
  is tested.**
- **State the direction of the bias**, not just its existence ("relaxing these assumptions
  would decrease the probability that control is achieved"). It recurs across archetypes
  (Hellewell 2020, Abbott 2020, Gostic 2020, Lauer 2020).
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
- ◆ **Decide the main-text/supplement split before drafting**: main text gets one item per
  headline claim plus the parameter (and scenario) table — as a default, a fit/validation
  figure, a headline-result figure and a what-governs-it figure. Supplement gets full
  equations, remaining sensitivity analyses, diagnostics, breakdowns, the reporting checklist;
  cite every supplementary item from the sentence it supports.
- **Table for look-up and comparison across labelled scenarios; figure when the shape is the
  finding.** Never both for the same numbers.
- **Captions stand alone**: what is plotted and what the band is, under which parameters, and
  what to see. Observed data overlaid on simulations; parameters in the caption; baseline in
  every panel.
- ◆ **Also conventional, but not from the corpus**: one colour per scenario across the whole
  paper; axes labelled with quantity and unit, not variable name; tables with the baseline row
  first, the interval in the same cell as the estimate, the unit in the header, and the
  precision the data support.

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
- ◆ **Name the reporting guideline in Methods and attach its checklist**: Bennett 2012 or
  ISPOR-SMDM for any modelling study; EPIFORGE (forecasting); ODD (agent-based); CHEERS
  (economic); TRIPOD+AI / PROBAST / CLAIM (prediction); PRISMA (reviews); STROBE/RECORD
  (observational components).

---

## 7. Machine learning and predictive modelling

For the risk-mapping, nowcasting, clinical-prediction or ML critique archetypes, `Read`
`references/ml-prediction.md` before drafting: it adds rules, anti-patterns and a checklist
block. Everything in §1–§6 and §8 still applies.

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

For the best-practice guidance archetype, `Read` `references/guidance-papers.md` before
drafting. Its rules override §1–§8 where they conflict.

---

## 10. Banned phrases

Do not write these. The corpus's strongest papers avoid them, and the near-misses prove the
rule: Earn 2000 calls the causes of measles transitions "still poorly understood", but only
after stating what *is* "well known" and naming the exact phenomenon left unexplained. The
vague gap is banned, not the words.

- "Little is known about X" and its disguises ("estimates remain scarce", "evidence is
  limited", "X remains poorly understood") standing as the gap statement. State what you
  searched for and did not find, or set the unknown against what is known.
- "This is the first study to…". Claim scope or rigour instead; "none, to our knowledge,
  has…" attached to a checkable claim is fine.
- "Recently", "many countries", "a large dataset", "informs policy". Use a number, date or name.
- Generic hedging ("may possibly indicate"). Hedge the specific inference, or don't hedge.
- "The model shows that X will happen". Models suggest, project under assumptions, or estimate.
- A scenario set presented as if it were the option set available to decision-makers.
