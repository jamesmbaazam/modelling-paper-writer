# Changelog

All notable changes to this skill. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as applied to a skill: the **major**
version changes when the file layout or the instructions Claude follows change in a way that
breaks an existing install or an existing eval, the **minor** version when rules, corpus papers
or reference files are added, and the **patch** version for corrections that leave the
instructions intact.

`SKILL.md` (`metadata.version`), `.claude-plugin/plugin.json` and `CITATION.cff` must all carry
the same version; `python3 tools/corpus.py check` fails if they drift or if the version has no
section here.

Nothing has been released yet, so this file has one section. Development before the first
release is in the git history and in `docs/reproducibility.md`, not here; once 1.0.0 is tagged, every
later change gets an entry.

## [1.0.0] — unreleased

First release. A skill for writing, revising and critiquing infectious disease modelling papers,
distilled from 81 well-written mathematical, statistical and machine learning papers published
between 2000 and 2024.

### Added

- **`SKILL.md`**, ~370 lines, loaded on every invocation. A six-step procedure — determine the
  mode (draft, revise or critique), establish the archetype, read one corpus exemplar, draft or
  edit only what was asked, self-review, report placeholders and assumptions — then the
  conventions as one-line imperatives that point into `references/`.
- **Hard rules** that override the conventions: cite as `[Author YEAR]` only papers the user
  supplied, since the corpus is a style corpus and not a bibliography — a recalled paper is
  `[Author YEAR?]` and goes on the verify list, and no DOI, journal, volume or page is written
  from memory, in the text or the verify list; never invent a number;
  never reuse a corpus sentence verbatim in the user's manuscript; preserve the author's voice,
  spelling variant and tense in revision mode and show edits rather than rewriting silently; and
  treat *Lancet* house typography (middle-dot decimals, "to" inside intervals) as house style
  rather than a rule.
- **Twenty-two paper archetypes**, each with its exemplars and the shape its headline claim must
  take — estimation, real-time analysis, scenario projection, feasibility threshold, policy
  counterfactual, competing hypotheses, forecast evaluation, dynamical systems, methods
  benchmark, review, best-practice guidance, risk mapping, digital surveillance, clinical
  prediction and critique, vaccine impact and economic evaluation, phylodynamics and genomic epidemiology,
  serological inference, within-host dynamics, agent-based model documentation, nowcasting and
  reporting delays, and rapid-response outbreak analysis.
- **Rules for every section**: four title shapes; the abstract's six-move spine with per-venue
  word budgets; the five-move introduction; how much mathematics belongs in the main text and
  where; assumptions with their direction of bias; parameters, priors and the parameter table;
  scenario grids; sensitivity analysis reported with its conclusion; interval choice and
  labelling; comparators for every number; verbs and modals graded to the design; figures,
  tables and the main-text/supplement split; seven ways to position against prior work; voice
  and hedging; six categories of limitation; availability statements; and which reporting
  guideline to name.
- **Progressive disclosure through `references/`** so that detail loads only when it is needed:
  `evidence.md` holds the corpus quotations behind each rule under the same section numbers;
  `examples.md` the worked passages (§12.1–§12.13); `checklist.md` the self-review checklist;
  and `ml-prediction.md` and `guidance-papers.md` the machine-learning and
  best-practice-guidance archetypes, which load only for those paper types.
- **`references/corpus/`** — one style analysis per paper, with verbatim quotations, under a
  canonical heading set matching the rule sections (`Structure`, `Opening move`, `Methods`,
  `Results`, `Literature`, `Voice`, `Discussion and limitations`, `Data, code and funding`,
  `Distinctive moves to borrow`), so the procedure's grep for a section is deterministic. All 81
  papers are analysed from their full text; for the five that are paywalled (Keeling 2001,
  Altizer 2006, Keeling & Rohani 2002, Grenfell 2001, Bjørnstad 2002) the analysis was written
  from the publisher's PDF and its quotations checked against it at the time of writing, since
  automated verification can only reach their abstracts afterwards.
- **`references/corpus/papers.csv`** as the single source of truth for the corpus, with
  `references/corpus-index.md` generated from it.
- **Worked template passages**: compartmental model definitions at three levels of formality in
  both LaTeX and Unicode, an annotated abstract, weak→strong repairs for gap statements, results
  sentences and limitations, methods paragraphs for a Bayesian fit and for a supervised model, a
  bias check, availability statements, and parameter and scenario tables.
- **`tools/candidates.py`** and **`tools/fulltext.py`** — search Europe PMC for open-access
  candidates by archetype and venue (`--venue` lists infectious disease modelling papers in one
  journal), and pull a paper's full text, so a corpus addition is always written from the
  paper and never from memory.
- **`tools/corpus.py`** — regenerates the corpus index and checks the repo for drift: stale
  index, corpus files missing from `papers.csv`, missing canonical headings, archetype and
  full-text flags disagreeing with the §0 table, frontmatter breaking the Agent Skills spec,
  version strings disagreeing or missing a changelog section, exemplars of one archetype not
  linking each other, corpus counts in the README, citation file, manifest or changelog going
  stale, references to `SKILL.md` subsections that do not exist, and broken links.
- **`tools/verify_quotes.py`** and `docs/quote-verification.md` — every quotation of 30 or more
  characters checked against the paper's abstract and, where PubMed Central holds it, the full
  text; `--local-text` checks a paywalled paper against a local PDF extraction instead,
  compensating for the ligature, Greek-letter and running-head damage that pre-Unicode journal
  PDFs introduce. 1,548 verified, 0 not found, 152 unreachable, 218 checked by hand.
- **`evals/`** — 15 cases with graders, covering drafting, revision, critique, the hard rules and
  the negative trigger, for `claude plugin eval`.
- **`.claude-plugin/plugin.json` and `marketplace.json`**, so the skill installs as a plugin.
- **`docs/reproducibility.md`** — how the skill was built (the brief, both critiques, the corpus
  expansions), the corpus and its generated summary, the method for selecting, analysing and
  verifying papers, the maintainer workflow, and how to apply the method to build a similar
  skill. The README and contributing guide stay short and point to it.
