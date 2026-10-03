# modelling-paper-writer

[![GitHub stars](https://img.shields.io/github/stars/jamesmbaazam/modelling-paper-writer?style=flat)](https://github.com/jamesmbaazam/modelling-paper-writer/stargazers)
[![Version](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjamesmbaazam%2Fmodelling-paper-writer%2Fmain%2FCITATION.cff&query=%24.version&label=version&color=blue)](CITATION.cff)

A [Claude Code](https://claude.com/claude-code) skill for writing infectious disease
mathematical, statistical and machine learning modelling papers, distilled from the writing
style of 37 well-written papers in the field.

The skill does not generate claims or results. It encodes *how* good papers in this field are
put together: how they structure sections, present models and assumptions, report estimates and
uncertainty, position themselves against prior work, and write limitations.

## What's in here

| Path                            | Contents                                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SKILL.md`                      | The skill itself: a six-step procedure, hard rules, the archetype table, the conventions as one-line imperatives, banned phrases and pointers into `references/` (~350 lines / ~3,500 words, loaded on every invocation) |
| `references/ml-prediction.md`   | §7 rules, anti-patterns and checklist for machine learning / predictive modelling papers, loaded only for those archetypes                                                                                         |
| `references/guidance-papers.md` | §9 rules, anti-patterns and checklist for best-practice and guidance papers, loaded only for that archetype                                                                                                        |
| `references/evidence.md`        | The corpus quotations behind each rule, with the same section numbering as `SKILL.md`                                                                                                                              |
| `references/examples.md`        | Worked template passages (§12.1–§12.13): model definitions, abstract, gap statements, results sentences, limitations, methods paragraphs, parameter and scenario tables, availability statement                    |
| `references/corpus-index.md`    | Author YEAR → `references/corpus/` file, with venue and archetype                                                                                                                                                     |
| `evals/`                        | Regression suite for `claude plugin eval` (see `evals/README.md`)                                                                                                                                                  |
| `references/corpus/*.md`           | One style analysis per paper (37 files), with verbatim quotations                                                                                                                                                  |
| `references/corpus/papers.csv`     | Index: title, DOI, authors, methodological type, source URL, style file                                                                                                                                            |
| `docs/prompt.md`                | The original brief the skill was built from                                                                                                                                                                        |
| `docs/quote-verification.md`    | Every corpus quotation checked against the published paper, per paper and per rule file                                                                                                                            |
| `tools/`                        | `corpus.py` (regenerate the index and the README block; check the repo for drift) and `verify_quotes.py`                                                                                                            |
| `CHANGELOG.md`                  | What changed in each version, and the versioning rules                                                                                                                                                             |
| `CITATION.cff`                  | Machine-readable citation metadata                                                                                                                                                                                 |

## The corpus

The venues are *Nature*, *Science*, *PNAS*, the *Lancet* family, *BMJ*, *Nature Machine
Intelligence*, *npj Digital Medicine*, *PLoS Computational Biology*, *Statistics in Medicine*,
*Ecology Letters*, *Ecological Monographs*, *Annals of Internal Medicine*, *Scientific Reports*,
*Nature Reviews Microbiology*, *J. R. Soc. Interface* and *Wellcome Open Research*. Diseases
covered: COVID-19, influenza, measles, dengue, Ebola, foot-and-mouth, and rodent-borne and
other zoonoses. Malaria, tuberculosis and antimicrobial resistance are mentioned in passing in
two review papers but no corpus paper models them.

**Selection basis.** The papers are landmark, highly cited work from a narrow set of research
groups, chosen for writing quality rather than sampled systematically across venues or
subfields. Conventions derived from the 2000–2008 papers may not match current reviewer
expectations (e.g. citation density).

<!-- corpus:begin — generated by tools/corpus.py index -->

**37 papers spanning 2000–2024**, 11 of them on COVID-19.

| Methodological type | Papers |
|---|--:|
| Hybrid (mathematical-statistical) | 17 |
| Hybrid (statistical-machine learning) | 6 |
| Mathematical | 5 |
| Statistical | 5 |
| Machine learning | 4 |

5 papers (Keeling 2001, Altizer 2006, Keeling & Rohani 2002, Grenfell 2001, Bjørnstad 2002) have no reachable open-access full text; those style files are built on the verbatim abstract and the bibliographic record, say so at the top, and point to a full-text substitute for the same archetype.

**Quotation coverage:** 538 verified, 0 not found, 185 unchecked, 6 reviewed by hand — every quotation of 30 or more characters checked against the paper's abstract and, where PubMed Central holds it, the full text (`python3 tools/verify_quotes.py`; report in [`docs/quote-verification.md`](docs/quote-verification.md)). *Unchecked* means no open full text was reachable, not that the quotation is wrong.

<!-- corpus:end -->

## What the skill covers

`SKILL.md` opens with a **procedure** (determine mode → establish archetype, venue and budget →
read the matching style file → draft or edit only the requested section → self-review against
the checklist → return text plus a note of placeholders and assumptions) and a block of **hard
rules** (never invent citations or numbers; never reuse corpus sentences; preserve the author's
voice in revision; journal typography is not a style rule). The conventions then follow this
structure, with the corpus evidence for each in `references/evidence.md` under the same
section numbers:

0. **First decide the archetype** — fifteen paper types, each with its exemplars and the
   shape its headline claim must take
1. **Structure** — four title shapes; the abstract's six-move spine and per-venue word
   budgets; subheading craft; the five-move introduction. Journal templates (Nature/Science,
   PNAS, Lancet, PLoS, clinical, living formats) sit in `references/evidence.md` §1.2
2. **Methods** — how much mathematics and where; assumptions and their direction of bias;
   parameters, priors and the parameter table; scenarios; sensitivity analysis; software
3. **Results** — choosing the right interval; giving every number a comparator; recurring
   sentence shapes; grading verbs to evidence; reporting your own failures; figures, tables
   and the main-text/supplement split
4. **Literature** — stating a checkable gap; seven ways to position against prior work;
   citation density by archetype
5. **Voice** — person and tense; hedging that carries information; precision over vagueness
6. **Domain conventions** — the R₀ paragraph; validation and scoring; identifiability;
   decision relevance; real-time analyses; availability statements; which reporting guideline
   to name
7. **Machine learning and predictive modelling** (in `references/ml-prediction.md`) —
   train/test discipline, calibration, confronting bias in training data, what appraisers mark
   you down for, the two failure modes that killed Google Flu Trends
8. **Discussion and limitations** — six categories of limitation and how to write each
9. **Best-practice and guidance papers** (in `references/guidance-papers.md`) — a distinct
   archetype with its own rules, which override the rest where they conflict
10. **Banned phrases**

The self-review checklist is `references/checklist.md`, and the worked passages are
`references/examples.md` §12.1–§12.13: SIR/SEIR model definitions at three levels of formality
with LaTeX and Word variants, an annotated abstract, weak→strong repairs for gaps, results
sentences and limitations, template methods and availability sections, and parameter and
scenario tables.

## Installing

```sh
git clone https://github.com/jamesmbaazam/modelling-paper-writer \
  ~/.claude/skills/modelling-paper-writer
```

Claude Code picks the skill up automatically and invokes it when you ask for help drafting or
revising a modelling manuscript. You can also invoke it explicitly with
`/modelling-paper-writer`.

## Adding a paper to the corpus

1. Write a style analysis as `references/corpus/NN-firstauthor-year-slug.md`, following the shape
   of the existing files: archetype, structure, opening move, methodology conventions, results
   storytelling, literature integration, voice, limitations, distinctive moves to borrow.
   Quote verbatim wherever possible, and link related files with relative markdown links.
2. Add a row to `references/corpus/papers.csv` and to `references/corpus-index.md`.
3. Fold any genuinely new convention into `SKILL.md` as a one-line imperative, with the
   supporting quotation in `references/evidence.md` under the same section number.
4. Run `claude plugin eval .` to check nothing regressed.

## Author

**James Azam** ([@jamesmbaazam](https://github.com/jamesmbaazam)) — designed the skill, selected
and curated the 37-paper corpus, defined the analytical framework the style summaries follow,
and directed its development.

If you find this skill helpful, please [star the repo](https://github.com/jamesmbaazam/modelling-paper-writer) —
it helps others find it.

If you use this skill in your work, please cite it — see [CITATION.cff](CITATION.cff), or:

> Azam, J. (2026). *modelling-paper-writer: a Claude Code skill for writing infectious
> disease modelling papers.* https://github.com/jamesmbaazam/modelling-paper-writer

## Licence

MIT — see [LICENSE](LICENSE).

The style analyses are original summaries containing short verbatim quotations from the papers
analysed, used for commentary and criticism. Copyright in the underlying papers rests with their
authors and publishers.
