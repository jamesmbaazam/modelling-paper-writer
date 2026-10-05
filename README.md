# modelling-paper-writer

[![GitHub stars](https://img.shields.io/github/stars/jamesmbaazam/modelling-paper-writer?style=flat)](https://github.com/jamesmbaazam/modelling-paper-writer/stargazers)
[![Version](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjamesmbaazam%2Fmodelling-paper-writer%2Fmain%2FCITATION.cff&query=%24.version&label=version&color=blue)](CITATION.cff)

A [Claude Code](https://claude.com/claude-code) skill for writing, revising and critiquing
infectious disease mathematical, statistical and machine learning modelling papers, distilled
from the writing style of 81 well-written papers in the field.

The skill does not generate claims or results. It encodes *how* good papers in this field are put
together: how they structure sections, present models and assumptions, report estimates and
uncertainty, position themselves against prior work, and write limitations. It never invents
citations or numbers — where your results are missing, it leaves placeholders and lists them.

## What it covers

The skill first works out what kind of paper you are writing — one of twenty-two paper types,
from parameter estimation and scenario projection to forecast evaluation, clinical prediction and
rapid-response outbreak analysis — because that fixes the shape of the headline claim. It then
applies conventions for:

- **Structure** — titles, abstracts and their per-journal budgets, introductions, and journal
  templates
- **Methods** — how much mathematics to show, assumptions and their direction of bias, parameter
  and scenario tables, sensitivity analysis
- **Results** — the right interval, a comparator for every number, verbs graded to the evidence,
  reporting your own failures, figures and tables
- **Literature and voice** — a checkable gap, positioning against prior work, hedging that carries
  information
- **Domain conventions** — the R₀ paragraph, validation and scoring, identifiability, decision
  relevance, data and code availability, reporting guidelines
- **Machine learning and predictive models**, and **best-practice and guidance papers**, each with
  their own rules
- **Discussion and limitations**, and a list of phrases to avoid

It works in three modes: drafting a section, revising your text while keeping your voice, and
critiquing a manuscript as a reviewer would.

## Key files

| Path | Contents |
|---|---|
| `SKILL.md` | The skill: a six-step procedure, hard rules and the conventions (~370 lines, loaded on every use) |
| `references/` | Material loaded on demand: the evidence behind each rule, worked examples, the self-review checklist, and the machine-learning and guidance-paper rules |
| `references/corpus/` | One style analysis per corpus paper, with verbatim quotations |
| `evals/` | Test cases for `claude plugin eval` |
| `docs/reproducibility.md` | How the skill was built, the corpus, and how to build a skill like it |
| `CHANGELOG.md` | What changed in each version |

## Installing

**As a Claude Code plugin** (recommended — you get updates with `/plugin`):

```sh
/plugin marketplace add jamesmbaazam/modelling-paper-writer
/plugin install modelling-paper-writer@jamesmbaazam
```

**By cloning into your skills directory:**

```sh
git clone https://github.com/jamesmbaazam/modelling-paper-writer \
  ~/.claude/skills/modelling-paper-writer
```

Use `.claude/skills/` inside a project instead if you want it available only there.

**On claude.ai** (Settings → Capabilities → Skills → upload): build the archive with

```sh
python3 tools/package.py     # writes dist/modelling-paper-writer-<version>.zip
```

Claude picks the skill up automatically when you ask for help drafting, revising or reviewing a
modelling manuscript. You can also invoke it explicitly with `/modelling-paper-writer`.

## Contributing

Bug reports, rule corrections and paper suggestions are welcome — [open an
issue](https://github.com/jamesmbaazam/modelling-paper-writer/issues), or see
[CONTRIBUTING.md](CONTRIBUTING.md) for small pull requests.

## Author

**James Azam** ([@jamesmbaazam](https://github.com/jamesmbaazam)) — designed the skill, selected
and curated the corpus, defined the analytical framework the style summaries follow, and directed
its development.

If you find this skill helpful, please [star the
repo](https://github.com/jamesmbaazam/modelling-paper-writer) — it helps others find it.

If you use this skill in your work, please cite it — see [CITATION.cff](CITATION.cff), or:

> Azam, J. (2026). *modelling-paper-writer: a Claude Code skill for writing infectious
> disease modelling papers.* https://github.com/jamesmbaazam/modelling-paper-writer

## Licence

MIT — see [LICENSE](LICENSE).

The style analyses are original summaries containing short verbatim quotations from the papers
analysed, used for commentary and criticism. Copyright in the underlying papers rests with their
authors and publishers.
