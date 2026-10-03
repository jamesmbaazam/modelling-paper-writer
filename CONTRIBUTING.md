# Contributing

Thanks for considering a contribution. The most useful ones are a new paper in the corpus, a
correction to a rule the corpus does not actually support, and a failing eval case that shows the
skill behaving badly.

## Setup

There is nothing to install. The tooling is Python 3.9+, standard library only.

```sh
python3 tools/corpus.py check     # must pass before every commit; CI runs it on every push
python3 tools/corpus.py index     # regenerate the generated files after editing papers.csv
python3 tools/verify_quotes.py    # check every quotation against the published paper (network)
claude plugin eval .              # run the eval suite in evals/
python3 tools/package.py          # build the claude.ai upload zip into dist/
```

`corpus.py check` is the gate. It verifies that the generated files are current, that each corpus
file carries the canonical headings `SKILL.md` greps for, that `papers.csv` agrees with the
`SKILL.md` archetype table and preamble counts, that every `Author YEAR` citation names a real
corpus paper, that the frontmatter and plugin manifests are valid, that the three version strings
agree with the changelog, and that no markdown link is broken. Its `note:` lines are
informational — they list sections a paper's analysis genuinely lacks.

## Two files are generated — do not edit them by hand

- `references/corpus-index.md`
- the block in `README.md` between `<!-- corpus:begin -->` and `<!-- corpus:end -->`

Both come from `references/corpus/papers.csv` via `python3 tools/corpus.py index`.
`docs/quote-verification.md` is generated too, by `tools/verify_quotes.py`.

## Adding a paper to the corpus

The corpus is chosen for **writing quality**, not for citation count or importance. A paper earns
a place if it does something with prose, structure or the handling of uncertainty that is worth
copying. Papers with reachable open-access full text are much more useful than paywalled ones:
five of the current 37 could only be analysed from their abstracts, and those files cannot
support any claim about section structure or results prose.

1. **Write the style analysis** as `references/corpus/NN-firstauthor-year-slug.md`, following an
   existing file. Use the canonical `##` headings, which match the `SKILL.md` rule sections:

   `Structure` · `Opening move` · `Methods` · `Results` · `Literature` · `Voice` ·
   `Discussion and limitations` · `Data, code and funding` · `Distinctive moves to borrow` ·
   `Related files`

   `Structure`, `Opening move`, `Methods`, `Results` and `Distinctive moves to borrow` are
   required; the rest only where the paper has something to show. Add a trailing gloss when the
   section deserves a name of its own (`## Methods — screening as evidence`), and add topical
   sections of your own freely — the canonical prefix is what the skill's procedure greps for.
   Quote verbatim wherever you can, and link related files with relative markdown links.

2. **Add a row to `references/corpus/papers.csv`.** The columns are `id`, `label`, `year`,
   `venue`, `archetype`, `role`, `full_text`, `method_type`, `title`, `authors`, `doi`, `url`,
   `file`. `label` is the `Author YEAR` form used throughout the rule files and must be unique;
   `archetype` must be one of the `SKILL.md` §0 categories (semicolon-separated if more than
   one); `full_text` is `yes` or `abstract only`. If it is `abstract only`, the file must carry
   a **Basis of this analysis** note and a `## Section analysis unavailable` section pointing to
   a full-text exemplar for the same archetype.

3. **Regenerate** with `python3 tools/corpus.py index`.

4. **If the paper introduces a new archetype**, add a row to the `SKILL.md` §0 table with its
   headline-claim shape. Every archetype needs at least one full-text exemplar; `check` enforces
   this.

5. **Fold any genuinely new convention into `SKILL.md`** as a one-line imperative, with the
   supporting quotation in `references/evidence.md` under the same section number. A rule nobody
   can trace to a quotation does not belong in the skill.

6. **Run `python3 tools/corpus.py check`, `python3 tools/verify_quotes.py` and
   `claude plugin eval .`** before opening the pull request.

## Changing or adding a rule

- **Every rule is attributable.** Either a corpus paper demonstrates it — cite the paper on the
  same line and put the quotation in `evidence.md` — or it comes from outside the corpus, in
  which case mark it ◆ and name the source. Journal instructions, reporting guidelines and
  general practice are all ◆.
- **Do not state a claim about the corpus you have not checked.** Several early rules asserted
  patterns the corpus contradicts: a title-length band that excluded half the titles, and a claim
  that no corpus paper opens by naming a method when one does. Where a claim is countable from
  `papers.csv`, count it.
- **Keep `SKILL.md` under 500 lines** (`check` enforces it). It loads on every invocation, so
  detail belongs in `references/`, which loads on demand.
- **Never paste a corpus sentence into a template.** The worked passages in `examples.md` are
  written from scratch, with illustrative numbers, and say so.

## Evals

`evals/` holds one directory per case, each with a `prompt.md` and graders. Add a case whenever
you fix a behaviour, so it cannot come back. A case that fails before your change and passes
after is the most persuasive thing you can put in a pull request.

## Versioning

`SKILL.md` (`metadata.version`), `.claude-plugin/plugin.json` and `CITATION.cff` must agree, and
the version needs a section in `CHANGELOG.md`; `check` enforces both. Bump the **major** version
when the file layout or the instructions change in a way that breaks an existing install or eval,
the **minor** version when rules, corpus papers or reference files are added, and the **patch**
version for corrections that leave the instructions intact.

## Licence

Contributions are accepted under the MIT licence (see [LICENSE](LICENSE)). The style analyses are
original summaries containing short verbatim quotations used for commentary and criticism;
copyright in the underlying papers rests with their authors and publishers. Do not add a corpus
file that reproduces substantial portions of a paper.
