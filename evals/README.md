# Evals

Regression suite for the `modelling-paper-writer` skill, run with `claude plugin eval`.
Each case is one realistic request; the graders are drawn from the §11 working checklist
and the *Hard rules* block in `SKILL.md`.

## Run

```bash
# from the skill root; three runs per case, with and without the skill loaded
claude plugin eval . --threshold 0.8

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
| `no-invented-citations` | Placeholders or flagged citations only; no DOIs; list of claims needing sources | hard-rules, introduction |
| `revision-preserve-voice` | UK spelling, tense and voice kept; edits shown; no scope creep | revision, hard-rules |
| `critique-methods-section` | ≥5 concrete reviewer requests; no unasked rewrite | critique, methods |
| `availability-statement` | GitHub ≠ archival; Zenodo placeholder; versions not invented; restricted data handled | availability, reproducibility |
| `scenario-table` | Baseline row first; stable labels; contact % by setting; combined scenario consistent | methods, scenarios |
| `ml-prediction-results` | External validation headline; comparator; calibration and operating point; no overclaim | ml, results |
| `negative-trigger-observational` | Skill does **not** fire on a non-modelling cohort study | trigger |

Every case except the last also has a `skill-fired` grader (`tool_used: Skill`), which the
runner treats as a plugin-fired indicator rather than part of the score.

## Grader design

- `regex` graders carry the checks that must be stable across runs: field headings,
  LaTeX environments, absence of DOIs, absence of the banned phrases, absence of `2·5`-style
  decimals outside Lancet targets, presence of bracketed placeholders.
- `llm` graders carry the judgement calls, written as explicit PASS / FAIL conditions so a
  small judge model does not decide on formatting. If a case scores low with `skill-fired`
  passing, re-run with `--judge-model sonnet` before changing the skill.
- A `not_contains` regex must never target text that appears in the prompt. A good
  response quotes the original to show what it changed (the skill's revision rule asks for
  visible edits), so the phrase is present for the right reason. The first smoke test of
  `gap-statement-rewrite` failed exactly this way; those checks now live in the LLM rubric.
- Every prompt supplies the numbers the response needs, so "no invented numbers" is
  checkable: anything not in the brief is a fabrication.

## Adding a case

```bash
claude plugin eval init --bare <case-name>
```

Then fill in `prompt.md` (a realistic request with all needed numbers) and replace the
template grader. Copy `graders/skill-fired.md` from any existing case.
