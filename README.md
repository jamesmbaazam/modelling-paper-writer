# modelling-paper-writing-skill

A [Claude Code](https://claude.com/claude-code) skill for writing infectious disease
mathematical, statistical and machine learning modelling papers, distilled from the writing
style of 37 well-written papers in the field.

**Developed by [James Azam](https://github.com/jamesmbaazam).**

The skill does not generate claims or results. It encodes *how* good papers in this field are
put together: how they structure sections, present models and assumptions, report estimates and
uncertainty, position themselves against prior work, and write limitations.

## What's in here

| Path | Contents |
|---|---|
| `SKILL.md` | The skill itself — 12 sections consolidating the conventions, plus worked example passages |
| `writing_styles/*.md` | One style analysis per paper (37 files), with verbatim quotations |
| `writing_styles/papers.csv` | Index: title, DOI, authors, methodological type, source URL, style file |
| `prompt.md` | The original brief the skill was built from |
| `CITATION.cff` | Machine-readable citation metadata |

## The corpus

37 papers spanning 2000–2024, from *Nature*, *Science*, *PNAS*, the *Lancet* family, *BMJ*,
*Nature Machine Intelligence*, *npj Digital Medicine*, *PLoS Computational Biology*,
*Statistics in Medicine*, *Ecology Letters*, *Ecological Monographs*, *Annals of Internal
Medicine*, *J. R. Soc. Interface* and *Wellcome Open Research*.

Diseases covered: COVID-19, influenza, measles, dengue, malaria, Ebola, foot-and-mouth,
tuberculosis, rodent-borne and other zoonoses, and antimicrobial resistance.

| Methodological type | Papers |
|---|---:|
| Hybrid (mathematical–statistical) | 12 |
| Hybrid (statistical–machine learning) | 6 |
| Mathematical | 5 |
| Statistical | 5 |
| Hybrid (statistical–mathematical) | 5 |
| Machine learning | 4 |

Five papers (`03`, `05`, `06`, `17`, `18`) have no reachable open-access full text; those style
files are built on the verbatim abstract and bibliographic record, and say so at the top.

## What the skill covers

`SKILL.md` is organised as:

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
12. **Worked examples** — SIR/SEIR model definitions at three levels of formality, an annotated
    abstract, weak→strong repairs, and template methods and availability sections

## Installing

```sh
git clone https://github.com/jamesmbaazam/modelling-paper-writing-skill \
  ~/.claude/skills/modelling-paper-writer
```

Claude Code picks the skill up automatically and invokes it when you ask for help drafting or
revising a modelling manuscript. You can also invoke it explicitly with
`/modelling-paper-writer`.

## Adding a paper to the corpus

1. Write a style analysis as `writing_styles/NN-firstauthor-year-slug.md`, following the shape
   of the existing files: archetype, structure, opening move, methodology conventions, results
   storytelling, literature integration, voice, limitations, distinctive moves to borrow.
   Quote verbatim wherever possible, and link related files with `[[wikilinks]]`.
2. Add a row to `writing_styles/papers.csv`.
3. Fold any genuinely new convention into `SKILL.md` and add the paper to its index table.

## Author

**James Azam** ([@jamesmbaazam](https://github.com/jamesmbaazam)) — designed the skill, selected
and curated the 37-paper corpus, defined the analytical framework the style summaries follow,
and directed its development.

If you use this skill in your work, please cite it — see [CITATION.cff](CITATION.cff), or:

> Azam, J. (2026). *modelling-paper-writing-skill: a Claude Code skill for writing infectious
> disease modelling papers.* https://github.com/jamesmbaazam/modelling-paper-writing-skill

## Licence

MIT — see [LICENSE](LICENSE).

The style analyses are original summaries containing short verbatim quotations from the papers
analysed, used for commentary and criticism. Copyright in the underlying papers rests with their
authors and publishers.
