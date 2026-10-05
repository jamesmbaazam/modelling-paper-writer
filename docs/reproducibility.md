# Reproducibility: how this skill was built, and how to build one like it

This document is for anyone who wants to audit where the skill's rules come from, maintain its
corpus, or apply the same method to another field. Using the skill, or contributing a fix to it,
does not require any of it — see the [README](../README.md) and
[CONTRIBUTING.md](../CONTRIBUTING.md).

**Contents.** [1. What the skill is made of](#1-what-the-skill-is-made-of) ·
[2. How it was built](#2-how-it-was-built) · [3. The corpus](#3-the-corpus) ·
[4. The method in detail](#4-the-method-in-detail) ·
[5. Maintaining the skill](#5-maintaining-the-skill) ·
[6. Building a similar skill](#6-building-a-similar-skill)

---

## 1. What the skill is made of

The skill is four layers, each derived from the one beneath it, with tooling that checks they
still agree.

| Layer | Files | What it holds |
|---|---|---|
| Corpus | `references/corpus/papers.csv`, `references/corpus/*.md` | One row and one style analysis per paper, written from its full text, with verbatim quotations |
| Evidence | `references/evidence.md` | The quotations that justify each rule, under the same section numbers as `SKILL.md` |
| Rules | `SKILL.md`, `references/ml-prediction.md`, `references/guidance-papers.md`, `references/checklist.md`, `references/examples.md` | A procedure, hard rules, one-line imperatives, a self-review checklist and worked template passages |
| Behaviour | `evals/` | Realistic requests with graders, run with and without the skill loaded |

`SKILL.md` loads on every invocation and is kept short; everything else loads only when the
procedure points to it (progressive disclosure). `tools/corpus.py check` keeps the layers
consistent, and `tools/verify_quotes.py` checks every quotation against the published paper.

## 2. How it was built

### 2.1 The brief

The original request ([`docs/prompt.md`](prompt.md)) was to build a skill for writing infectious
disease mathematical, statistical and machine learning modelling papers "by learning from the
examples of papers with good writing styles": first summarise each paper's writing style into its
own file, then consolidate the styles into one skill. Each summary was to cover six dimensions:

1. **Structural patterns** — section organisation, flow, typical subheadings
2. **Methodology conventions** — algorithms, notation, assumptions
3. **Results storytelling** — interpretation, significance, links back to the question
4. **Literature integration** — citation style, positioning, reference density
5. **Voice and tone** — formality, technical depth, clarity versus precision
6. **Domain-specific conventions** — for example train/test splits and cross-validation

and the skill was to give concrete examples where needed (an SIR model, with S, I and R defined
and the flows between them stated).

### 2.2 First version

The author supplied a list of 37 papers. Each was summarised against the six dimensions and the
summaries were consolidated into a single `SKILL.md` of about 1,420 lines and 13,700 words, loaded
in full on every invocation. Five of the 37 could only be analysed from their abstracts.

### 2.3 First critique and restructure (September 2026)

A critique on 2026-09-13 found that the skill described what good papers look like but never told
Claude what to do, and that it was too long to load on every call. It also found internal
inconsistencies (lists announced as six that held seven), papers cited by numeric code (225
occurrences) rather than by name, coverage claims the corpus did not support (tuberculosis and
antimicrobial resistance listed as covered when no paper modelled them), and no guardrails
against the failures that matter most in a writing assistant.

The restructure that followed:

- **Procedure first.** `SKILL.md` now opens with six steps: determine the mode (draft, revise,
  critique) → establish the archetype, venue and budget → read the matching corpus file → draft or
  edit only what was asked → self-review → return the text with a note of placeholders and
  assumptions.
- **Hard rules** for the failure modes: never invent a citation or a number (use placeholders),
  never reuse a corpus sentence in a user's manuscript, preserve the author's voice in revision,
  and treat journal house typography as house style rather than a rule.
- **Progressive disclosure.** The quotations justifying each rule moved to `evidence.md`, the
  worked examples to `examples.md`, and the machine-learning and guidance-paper rules to their own
  files, cutting `SKILL.md` to about a quarter of its length.
- **Names, not codes.** Every numeric code became `Author YEAR`.
- **Evals.** A regression suite of realistic requests, graded against the checklist and the hard
  rules.

### 2.4 Second critique and release preparation (October 2026)

A second critique on 2026-10-03 looked for instructions that conflicted, claims the corpus
contradicted, and anything that would block a public release. It found, among others, a title
length rule ("10–18 words") that excluded half the corpus — the measured range was 6–20, median 10
— and a claim that no paper opens by naming a method, which Lee 2010 contradicts. The response
set three conventions that now run through the repository:

- **Count what is countable.** A claim about the corpus is checked against `papers.csv` or the
  files before it is written.
- **Attribute every rule.** A rule either cites the corpus paper that demonstrates it, with the
  quotation in `evidence.md`, or is marked ◆ as coming from a journal instruction, reporting
  guideline or general practice.
- **One source of truth.** `papers.csv` holds every fact about the corpus; the index and the
  corpus block below are generated from it, and `corpus.py check` fails if they drift.

Release work added the plugin manifests, the changelog and versioning rules, continuous
integration, the packaging script and a contributing guide, and built `verify_quotes.py` to check
every quotation against the published text.

### 2.5 Expanding the corpus (October 2026)

The corpus grew from 37 to 81 papers in four stages.

1. **Full text for the abstract-only papers.** The author supplied the publisher PDFs for the five
   abstract-only papers; each was re-analysed from the full text, and its quotations were checked
   against the PDF text before the PDFs were set aside.
2. **Missing archetypes and missing venues.** Papers were added for seven archetypes the corpus
   lacked (vaccine impact and economic evaluation, phylodynamics, serological inference,
   within-host dynamics, agent-based model documentation, nowcasting, rapid-response outbreak
   analysis) and for the journals first modelling papers most often target. The corpus reached 49.
3. **Three exemplars per archetype.** An expansion approved on 2026-10-04 added two more exemplars
   to each of the ten archetypes that had only one, plus further forecast-evaluation papers, in six
   phases of four papers each. The corpus reached 73.
4. **Four requested venues.** Two papers each from *PLoS ONE*, *PLoS Biology*, *Infectious Diseases
   of Poverty* and *Emerging Infectious Diseases*. The corpus reached 81.

Each paper went through the same workflow (section 4): a shortlist from real Europe PMC records,
the full text read before the paper was accepted, a style analysis written from the full text,
every quotation verified, and the paper linked to the others of its archetype. Not every
shortlisted paper was kept: one was rejected because the analysis showed nothing worth copying —
no uncertainty, and parameter ranges that never reached the results.

### 2.6 Integrity passes

Expanding the corpus exposed drift that only a check can prevent, and each kind now has one:

- **Label collisions.** A second Bracher 2021 and a second Kerr 2021 made citations ambiguous;
  labels are now disambiguated with a letter (Bracher 2021a/b) and must be unique.
- **Stale section references.** After the restructure, corpus files still cited `SKILL.md`
  subsections that no longer existed; references must now cite `SKILL.md` §N for a rule and
  `evidence.md` §N.M for its evidence.
- **One-way links.** Each new paper linked its older siblings but never the reverse; every
  exemplar must now link every other exemplar of its archetype, in both directions.
- **Stale counts.** The README, citation file, plugin manifest and changelog kept saying 37 papers
  and fifteen archetypes; these counts are now checked against the corpus.
- **Uniform records.** One venue spelled two ways (*PNAS*) was normalised, and edits to
  `papers.csv` preserve its existing line endings so that diffs show only real changes.

## 3. The corpus

**Selection basis.** The papers are landmark, highly cited work from a narrow set of research
groups, chosen for writing quality rather than sampled systematically across venues or subfields.
A paper earns a place if it does something with prose, structure or the handling of uncertainty
that is worth copying. Conventions derived from the 2000–2008 papers may not match current
reviewer expectations (citation density, for example).

**Venues.** High-impact general science — *Nature*, *Science*, *PNAS*, the *Lancet* family
(*Lancet Infectious Diseases*, *Lancet Global Health*, *Lancet Public Health*, *Lancet Digital
Health*), *BMJ*, *Nature Communications*, *Nature Machine Intelligence*, *npj Digital Medicine*,
*eLife* — and the journals a first modelling paper actually targets: *PLoS Computational Biology*,
*PLoS ONE*, *PLoS Biology*, *PLoS Neglected Tropical Diseases*, *PLoS Currents*, *Epidemics*,
*Eurosurveillance*, *Emerging Infectious Diseases*, *Epidemiology & Infection*, *Infectious
Diseases of Poverty*, *BMC Medicine*, *BMC Infectious Diseases*, *Parasites & Vectors*, *Vaccine*,
*Mathematical Biosciences*, *Proc. R. Soc. B*, *J. R. Soc. Interface*, *Statistics in Medicine*,
*Biometrical Journal*, *Environmental Health Perspectives*, *Thorax*, *Annals of Internal
Medicine*, *Ecology Letters*, *Ecological Monographs*, *Nature Reviews Microbiology*, *Scientific
Reports* and *Wellcome Open Research*.

**Diseases.** COVID-19, influenza, measles, dengue, malaria, Ebola, Lassa fever, Zika, polio,
rotavirus, norovirus, hepatitis A, HPV, *Clostridioides difficile*, diphtheria, pneumococcal
disease, gambiense human African trypanosomiasis, onchocerciasis, foot-and-mouth, and rodent-borne
and other zoonoses. Tuberculosis and antimicrobial resistance are mentioned in passing in two
review papers, but no corpus paper models them.

**Archetypes.** Twenty-two paper types, from parameter estimation to rapid-response outbreak
analysis, each with the shape its headline claim must take; the table is `SKILL.md` §0, and
[`references/corpus-index.md`](../references/corpus-index.md) lists every paper with its venue,
archetype and role.

<!-- corpus:begin — generated by tools/corpus.py index -->

**81 papers spanning 2000–2024**, 25 of them on COVID-19.

| Methodological type | Papers |
|---|--:|
| Hybrid (mathematical-statistical) | 37 |
| Statistical | 19 |
| Mathematical | 12 |
| Hybrid (statistical-machine learning) | 8 |
| Machine learning | 5 |

Every paper is analysed from its full text. For 5 of them (Keeling 2001, Altizer 2006, Keeling & Rohani 2002, Grenfell 2001, Bjørnstad 2002) that full text is paywalled, so the analysis was written from the publisher's PDF and its quotations checked against it then rather than on every run.

**Quotation coverage:** 1548 verified, 0 not found, 152 unchecked, 218 reviewed by hand — every quotation of 30 or more characters checked against the paper's abstract and, where PubMed Central holds it, the full text (`python3 tools/verify_quotes.py`; report in [`docs/quote-verification.md`](quote-verification.md)). *Unchecked* means no open full text was reachable, not that the quotation is wrong.

<!-- corpus:end -->

## 4. The method in detail

### 4.1 Selecting a paper

- **Real records only.** `python3 tools/candidates.py` searches Europe PMC by archetype, and
  `--venue "<Europe PMC journal title>"` lists infectious disease modelling papers in one journal.
  It prints label, year, venue, citations, DOI and PMCID, so no paper enters the corpus from
  memory. The `--venue` search widens the modelling terms (short abstracts rarely say
  "mathematical model") and filters for infectious disease (general journals otherwise return
  unrelated modelling).
- **Read before accepting.** The search cannot judge writing quality, so its output is a
  shortlist. `python3 tools/fulltext.py <PMCID>` puts the full text in `tools/.cache/`, and the
  paper is read in full before it is accepted.
- **Prefer open full text.** Its quotations can be re-checked on every run; a paywalled paper's can
  be checked only once, by whoever holds the PDF.
- **Fill gaps deliberately.** Expansions targeted archetypes with too few exemplars, journals the
  corpus under-represented, and diseases beyond COVID-19, which already made up a third of the
  corpus.

### 4.2 Writing a style analysis

Each file is `references/corpus/NN-firstauthor-year-slug.md`, written from the full text:

- a header with the title and full citation, and an **Archetype** paragraph saying what kind of
  paper it is and what it adds to the corpus;
- the canonical sections, which match the `SKILL.md` rule sections so the procedure can find
  them by heading: `Structure` · `Opening move` · `Methods` · `Results` · `Literature` · `Voice` ·
  `Discussion and limitations` · `Data, code and funding` · `Distinctive moves to borrow` ·
  `Related files`. The first four and `Distinctive moves to borrow` are required; a trailing gloss
  is allowed (`## Methods — screening as evidence`);
- verbatim quotations, each followed by the move it demonstrates, stated as an imperative. The
  quotations are short and used for commentary and criticism; an analysis never reproduces
  substantial portions of a paper, whose copyright rests with its authors and publishers;
- a *What to avoid from this paper* section where a well-written paper still has a weakness worth
  naming (a missing calibration report, a priority claim, text and tables that disagree);
- `Related files`, linking every other exemplar of the same archetype with a clause saying what
  each adds.

### 4.3 Recording it

`references/corpus/papers.csv` has one row per paper with the columns `id`, `label`, `year`,
`venue`, `archetype`, `role`, `full_text`, `method_type`, `title`, `authors`, `doi`, `url`, `file`.
`label` is the `Author YEAR` form the rule files cite and must be unique; `archetype` is one or
more `SKILL.md` §0 categories, separated by semicolons; `full_text` is `yes` for open full text or
`publisher pdf` for a paywalled paper analysed from the PDF.

### 4.4 Verifying quotations

`python3 tools/verify_quotes.py` fetches each paper's abstract from Europe PMC and, where PubMed
Central holds it, the full text; splits every quotation of 30 or more characters at ellipses and
editorial brackets; and searches for each fragment after normalising case, punctuation and
whitespace. A quotation is *verified* when every fragment is found, *not found* when the source
is the full text and a fragment is missing, and *unchecked* when only the abstract was reachable.
For a `publisher pdf` paper, extract the PDF text to `tools/.cache/local_<id>.txt` and run
`--local-text <id>` before losing access to the PDF; afterwards its quotations are reported as
*reviewed*, with the few the tool cannot match listed in `REVIEWED` in the script. A *not found*
is a transcription error to fix, not a judgement call: in practice it is usually a dropped
parenthesis or citation marker that needed an ellipsis.

### 4.5 From analyses to rules

- A rule is a one-line imperative in `SKILL.md`, with the quotation that justifies it in
  `evidence.md` under the same section number. A rule nobody can trace to a quotation does not
  belong in the skill.
- Rules from journal instructions, reporting guidelines or general practice are marked ◆ and name
  their source. The journal budgets in `evidence.md` §1.2 are ◆ and were checked against the
  journals' current author guidelines; where a guideline could not be reached, the row gives the
  structure observed in the corpus and says to check the budget.
- Worked passages in `examples.md` are written from scratch with illustrative numbers; no corpus
  sentence is pasted into a template.
- `SKILL.md` stays under 500 lines, because it loads on every invocation.

### 4.6 Testing behaviour

Each eval case in `evals/` is a realistic request with graders drawn from the checklist and the
hard rules, run with and without the skill loaded (`claude plugin eval .`; see
[`evals/README.md`](../evals/README.md)). A behaviour that is fixed gets a case, so it cannot come
back.

## 5. Maintaining the skill

**Commands** (Python 3.9+, standard library only):

```sh
python3 tools/corpus.py check     # must pass before every commit; CI runs it on every push
python3 tools/corpus.py index     # regenerate the generated files after editing papers.csv
python3 tools/verify_quotes.py    # check every quotation against the published paper (network)
python3 tools/candidates.py       # shortlist open-access candidates in Europe PMC, by archetype
python3 tools/candidates.py --venue "PloS one"   # infectious disease modelling papers in one journal
python3 tools/fulltext.py PMC123  # pull a paper's open-access full text into tools/.cache/
python3 tools/package.py          # build the claude.ai upload zip into dist/
claude plugin eval .              # run the eval suite
```

**Generated files — do not edit by hand:** `references/corpus-index.md` and the corpus block in
section 3 of this document (both from `papers.csv` via `corpus.py index`), and
`docs/quote-verification.md` (from `verify_quotes.py`).

**Adding a paper:**

1. Shortlist with `candidates.py`, pull the full text with `fulltext.py`, and read it (4.1).
2. Write the style analysis (4.2).
3. Add the row to `papers.csv` (4.3); if the paper's archetype is new, add a row to the `SKILL.md`
   §0 table with its headline-claim shape, and add the paper to its archetype's row either way.
4. Link it with every other exemplar of its archetype, in both directions.
5. Run `corpus.py index`, `verify_quotes.py` and `corpus.py check`, and update the counts the check
   reports.
6. Fold any genuinely new convention into `SKILL.md` as a one-line imperative, with its quotation
   in `evidence.md`.

**What `corpus.py check` enforces:** the generated files are current; each corpus file has the
canonical headings; `papers.csv` agrees with the `SKILL.md` archetype table and preamble counts;
the paper count, archetype count and size of `SKILL.md` stated in the README, `CITATION.cff`,
`plugin.json` and the changelog are current; every `Author YEAR` citation names a corpus paper;
labels are unique; exemplars of the same archetype link each other; no file cites a `SKILL.md`
subsection; `SKILL.md` is under 500 lines; the frontmatter and manifests are valid; the three
version strings agree with the changelog; and no markdown link is broken.

**Versioning.** `SKILL.md` (`metadata.version`), `.claude-plugin/plugin.json` and `CITATION.cff`
must agree, and the version needs a section in `CHANGELOG.md`. Bump the **major** version when
the file layout or the instructions change in a way that breaks an existing install or eval, the
**minor** version when rules, corpus papers or reference files are added, and the **patch**
version for corrections that leave the instructions intact.

## 6. Building a similar skill

The method transfers to any field where good writing can be learned from exemplars: clinical
trials, health economics, ecology, software papers.

1. **Write the brief as dimensions.** Decide what a style analysis must cover (here, the six in
   2.1) before reading any paper.
2. **Assemble the corpus from real records.** Search a bibliographic database rather than recalling
   papers; select on writing quality; read each paper in full before accepting it.
3. **Analyse from full text into a fixed template**, with headings that match the sections of the
   skill you will write, so the skill can find the right passage by heading.
4. **Keep one source of truth** for the corpus (a CSV) and generate everything else from it.
5. **Derive rules with attribution.** Each rule cites the paper that demonstrates it or is marked as
   coming from outside the corpus. Count before you claim.
6. **Put a procedure first.** The skill should say what to do, in order, before it says what good
   looks like; keep the always-loaded file short and move evidence and examples into files loaded
   on demand.
7. **Write hard rules for the failures that matter most** in your field — for a writing assistant,
   invented citations and invented numbers.
8. **Verify every quotation** against the source text, automatically where the text is open.
9. **Check for drift** with a script that fails on any inconsistency between the corpus, the rules
   and the documents that describe them, and run it in CI.
10. **Test behaviour with evals** run with and without the skill, and add a case for every fix.
11. **Critique and iterate.** Both major revisions here came from a structured critique of the
    whole skill; record each critique's findings and their resolutions in a to-do file
    ([`docs/to_do.md`](to_do.md)) so the history is auditable.

**What transfers from `tools/`.** `corpus.py` is generic once its paths, column names and
canonical headings are changed. `verify_quotes.py` works for any field indexed by Europe PMC and
PubMed Central; other fields need a different full-text source. `candidates.py` encodes this
field's search terms and journals and would be rewritten. `package.py` needs only its file list.

**Lessons from this build.**

- An abstract is not enough to analyse a paper's writing; obtain the full text.
- Claims about the corpus drift as it grows unless a script checks them; every count stated in
  prose eventually went stale here until it was checked.
- Search tools return noise for general journals and miss short abstracts; tune the query per
  venue and read everything the search returns before trusting it.
- Even well-written exemplars have weaknesses; naming them (*what to avoid*) teaches as much as the
  moves worth copying.
- Links between related exemplars decay in one direction; enforce both.
