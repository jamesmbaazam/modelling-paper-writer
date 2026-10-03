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
| `SKILL.md`                      | The skill itself: a six-step procedure, hard rules, the archetype table, the conventions as one-line imperatives, banned phrases and the working checklist (~370 lines / ~3,500 words, loaded on every invocation) |
| `references/ml-prediction.md`   | §7 rules, anti-patterns and checklist for machine learning / predictive modelling papers, loaded only for those archetypes                                                                                         |
| `references/guidance-papers.md` | §9 rules, anti-patterns and checklist for best-practice and guidance papers, loaded only for that archetype                                                                                                        |
| `references/evidence.md`        | The corpus quotations behind each rule, with the same section numbering as `SKILL.md`                                                                                                                              |
| `references/examples.md`        | Worked template passages (§12.1–§12.13): model definitions, abstract, gap statements, results sentences, limitations, methods paragraphs, parameter and scenario tables, availability statement                    |
| `references/corpus-index.md`    | Author YEAR → `references/corpus/` file, with venue and archetype                                                                                                                                                     |
| `evals/`                        | Regression suite for `claude plugin eval` (see `evals/README.md`)                                                                                                                                                  |
| `references/corpus/*.md`           | One style analysis per paper (37 files), with verbatim quotations                                                                                                                                                  |
| `references/corpus/papers.csv`     | Index: title, DOI, authors, methodological type, source URL, style file                                                                                                                                            |
| `docs/prompt.md`                | The original brief the skill was built from                                                                                                                                                                        |
| `CITATION.cff`                  | Machine-readable citation metadata                                                                                                                                                                                 |

## The corpus

37 papers spanning 2000–2024, from *Nature*, *Science*, *PNAS*, the *Lancet* family, *BMJ*,
*Nature Machine Intelligence*, *npj Digital Medicine*, *PLoS Computational Biology*,
*Statistics in Medicine*, *Ecology Letters*, *Ecological Monographs*, *Annals of Internal
Medicine*, *J. R. Soc. Interface* and *Wellcome Open Research*.

Diseases covered: COVID-19 (11 of 37 papers), influenza, measles, dengue, Ebola,
foot-and-mouth, and rodent-borne and other zoonoses. Malaria, tuberculosis and antimicrobial
resistance are mentioned in passing in two review papers but no corpus paper models them.

**Selection basis.** The papers are landmark, highly cited work from a narrow set of research
groups, chosen for writing quality rather than sampled systematically across venues or
subfields. Conventions derived from the 2000–2008 papers may not match current reviewer
expectations (e.g. citation density).

| Methodological type                   | Papers |
| ------------------------------------- | -----: |
| Hybrid (mathematical–statistical)     |     12 |
| Hybrid (statistical–machine learning) |      6 |
| Mathematical                          |      5 |
| Statistical                           |      5 |
| Hybrid (statistical–mathematical)     |      5 |
| Machine learning                      |      4 |

Five papers (Keeling 2001, Altizer 2006, Keeling & Rohani 2002, Grenfell 2001, Bjørnstad 2002) have no reachable open-access full text; those style
files are built on the verbatim abstract and bibliographic record, and say so at the top.

## What the skill covers

`SKILL.md` opens with a **procedure** (determine mode → establish archetype, venue and budget →
read the matching style file → draft or edit only the requested section → self-review against
the checklist → return text plus a note of placeholders and assumptions) and a block of **hard
rules** (never invent citations or numbers; never reuse corpus sentences; preserve the author's
voice in revision; journal typography is not a style rule). The conventions then follow this
structure, with the corpus evidence for each in `references/evidence.md` under the same
section numbers:

0. **Choosing the archetype** — fourteen paper types, each with a canonical exemplar and the
   shape its headline claim should take
1. **Structural patterns** — the six-move spine, journal templates (Nature/Science, PNAS,
   Lancet, PLoS, clinical, living formats), subheading craft
2. **Methodology conventions** — how much mathematics and where; assumptions; parameters and
   priors; scenarios; sensitivity analysis; software
3. **Results storytelling** — choosing the right interval; giving every number a comparator;
   recurring sentence shapes; grading verbs to evidence; reporting your own failures
4. **Literature integration** — citation density by archetype; stating a checkable gap; seven
   ways to position against prior work
5. **Voice and tone** — person and tense; hedging that carries information; precision
6. **Domain-specific conventions** — the R₀ paragraph; validation and scoring; identifiability;
   decision relevance; real-time analyses; data, code and funding statements
7. **Machine learning conventions** — train/test discipline, calibration, confronting bias in
   training data, what appraisers mark you down for, the two failure modes that killed Google
   Flu Trends
8. **Discussion and limitations** — six categories of limitation and how to write each
9. **Best-practice and guidance papers** — a distinct archetype with its own rules
10. **Anti-patterns**
11. **Working checklist**
12. **Worked examples** (in `references/examples.md`) — SIR/SEIR model definitions at three
    levels of formality with LaTeX and Word variants, an annotated abstract, weak→strong
    repairs, template methods and availability sections, and parameter and scenario tables

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
