# Contributing

Thanks for considering a contribution. The most useful ones are a report of the skill behaving
badly, a correction to a rule, and a suggestion for a paper the corpus should learn from. None of
these need code.

## Raising an issue

If the skill gave you bad advice, broke one of its own rules, cited a paper that does not exist,
or failed to install, or if you know a well-written paper the corpus should learn from, [open an
issue](https://github.com/jamesmbaazam/modelling-paper-writer/issues). The most useful issues
include:

- **For bad output:** the prompt you gave, what the skill returned, and what you expected instead.
  Name the rule it broke if you can.
- **For a rule you disagree with:** the rule, and a paper or reporting guideline that contradicts
  it.
- **For a paper suggestion:** the DOI, its type if you know it, and what it does with prose,
  structure or uncertainty that is worth copying. Writing quality is the criterion, not citation
  count. The maintainer adds papers to the corpus; you do not need to.

## Pull requests

Small pull requests are welcome: a wording fix, a corrected rule, or a new eval case.

- **Every rule needs a source.** A rule either cites the corpus paper that demonstrates it, with
  the quotation in `references/evidence.md`, or is marked ◆ and names the journal instruction,
  reporting guideline or practice it comes from.
- **Do not paste corpus sentences** into the rules or the worked examples.
- **Keep `SKILL.md` short.** It loads on every use; detail belongs in `references/`.
- **Add an eval case for a behaviour you fix.** Each case in `evals/` is a `prompt.md` plus
  graders (see [`evals/README.md`](evals/README.md)). A case that fails before your change and
  passes after is the most persuasive thing you can put in a pull request.

Before opening the pull request, run the consistency check (Python 3.9+, nothing to install):

```sh
python3 tools/corpus.py check
```

It must pass; CI runs it too. How the corpus is built and maintained is documented in
[`docs/reproducibility.md`](docs/reproducibility.md).

## Licence

Contributions are accepted under the MIT licence (see [LICENSE](LICENSE)).
