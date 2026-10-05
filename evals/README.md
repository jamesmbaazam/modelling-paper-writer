# Evals

Regression suite for the `modelling-paper-writer` skill, run with `claude plugin eval`.
Each case is one realistic request; the graders are drawn from the `references/checklist.md` working checklist
and the *Hard rules* block in `SKILL.md`.

## Run

```bash
# from the skill root; three runs per case, with and without the skill loaded
claude plugin eval . --threshold 0.8 --judge-model sonnet

# cheaper full pass: one run per arm, four cases in parallel (~$3, ~6 min)
claude plugin eval . --runs 1 -j 4 --threshold 0.8

# one case, one run, cheap smoke test
claude plugin eval . --case abstract-lancet-id --runs 1

# by area
claude plugin eval . --tag hard-rules
```

The report lands in `evals/results/<timestamp>/report.html`. `Δ` is the score with the
skill minus the score without it; a case with Δ ≈ 0 and `skill-fired` failing means the
skill's description is not triggering on that phrasing.

## Cases

| Case | Checks | Tags |
|---|---|---|
| `abstract-lancet-id` | Structured abstract, five fields, ≤300 words, headline with labelled interval and comparator, no invented numbers | abstract, lancet |
| `limitations-branching-process` | Each limitation names the question it blocks; direction of bias; discharged vs live | discussion, limitations |
| `methods-seir-latex` | Compartments named in words, flows stated, LaTeX equations, every symbol glossed, fixed vs estimated, no middle-dot decimals | methods, equations |
| `results-sentences-rewrite` | Every number with a comparator; vague qualifiers replaced; graded verbs; no middle dots for PNAS | results, uncertainty |
| `gap-statement-rewrite` | "Little is known" and "first study" removed (LLM-judged, see below); checkable gap; "Here, we…" | introduction, anti-patterns |
| `no-invented-numbers` | Placeholders in the right shape; no plausible fabricated results | hard-rules, results |
| `no-invented-citations` | Every citation marked unverified (`[ref]` or `[Author YEAR?]`) because the user supplied none; no DOI, volume, page or journal; verify-this list present | hard-rules, introduction |
| `revision-preserve-voice` | UK spelling, tense and voice kept; edits shown; no scope creep | revision, hard-rules |
| `critique-methods-section` | ≥5 concrete reviewer requests; no unasked rewrite | critique, methods |
| `availability-statement` | GitHub link accepted, no Zenodo requirement; versions not invented; restricted data handled | availability, reproducibility |
| `scenario-table` | Baseline row first; stable labels; contact % by setting; combined scenario consistent | methods, scenarios |
| `ml-prediction-results` | External validation headline; comparator; calibration and operating point; no overclaim | ml, results |
| `intro-no-venue-no-panel` | Drafts an introduction without asking for a journal; no `Research in context` panel; placeholders for citations; no invented numbers | introduction, procedure |
| `guidance-recommendations` | "We recommend", never "must"; the cost of ignoring each recommendation; a negative recommendation; a bulleted summary | guidance, discussion |
| `negative-trigger-observational` | Skill does **not** fire on a non-modelling cohort study | trigger |

Every case except the negative trigger also has a `skill-fired` grader (`tool_used: Skill`),
which the runner treats as a plugin-fired indicator rather than part of the score.

Three more graders check the procedure, marked `arm: with-only` so they are reported in every
run but never scored (the runner's guidance is to score outcomes, not trajectories):
`read-corpus-file` (step 3 — a `references/corpus/NN-…` file was read; on every case except
the negative trigger), `read-ml-reference` (`references/ml-prediction.md` loaded for the
machine-learning case) and `read-guidance-reference` (`references/guidance-papers.md` loaded
for the guidance case). A run that scores well with one of these failing has skipped a step
and got lucky.

## Grader design

- `regex` graders carry the checks that must be stable across runs: field headings,
  LaTeX environments, absence of DOIs, absence of the banned phrases, absence of `2·5`-style
  decimals outside Lancet targets, presence of bracketed placeholders.
- `llm` graders carry the judgement calls, written as explicit PASS / FAIL conditions so a
  small judge model does not decide on formatting. If a case scores low with `skill-fired`
  passing, re-run with `--judge-model sonnet` before changing the skill.
- Rubrics must only ask for what a sandboxed judge can see. It cannot verify that a cited
  paper exists, so `no-invented-citations` checks the *form* of citations and the presence of a
  verify-this list, not their truth. The form it checks is the hard rule: `[Author YEAR]`
  unmarked is reserved for papers the *user* supplied, so in a case where the user supplied
  none, every citation must carry a `?` or be `[ref]`. Being in the corpus earns a paper
  nothing here — the corpus is a style corpus, not a bibliography, and which papers belong in
  a manuscript depends on what it argues. A run on 2026-10-03 caught this: the skill cited
  eleven recalled papers unmarked and wrote out one DOI.
- Rubrics must not contradict themselves or the skill. The first `gap-statement-rewrite`
  rubric forbade "specific numbers" while requiring "2024", and treated "to our
  knowledge, no estimate has…" as a first-study claim when `SKILL.md` §10 explicitly allows
  it. Four conditions, each observable, is the right size.
- Use `--judge-model sonnet` when a case fails: the haiku default splits votes on long
  rubrics even when the output is compliant.
- A `not_contains` regex must never target text that appears in the prompt. A good
  response quotes the original to show what it changed (the skill's revision rule asks for
  visible edits), so the phrase is present for the right reason. The first smoke test of
  `gap-statement-rewrite` failed exactly this way; those checks now live in the LLM rubric.
- Every prompt supplies the numbers the response needs, so "no invented numbers" is
  checkable: a number that cannot be traced to the brief is a fabrication. A number computed
  from the brief (a difference, a rate per 1,000, a predictive value, a date) or read from a
  supplied figure or file is not, and rubrics must not treat it as one.

## Adding a case

```bash
claude plugin eval init --bare <case-name>
```

Then fill in `prompt.md` (a realistic request with all needed numbers) and replace the
template grader. Copy `graders/skill-fired.md` from any existing case.
