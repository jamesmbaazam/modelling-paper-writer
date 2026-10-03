# Best-practice and guidance papers

Companion to `SKILL.md` §9. Read this for the best-practice guidance archetype
(recommendations or reporting standards for a method others use). These rules override
`SKILL.md` §1–§8 where they conflict; the corpus quotations behind them are in
`evidence.md` §9.

## Rules

- **Structure by the problems a practitioner hits, in the order they hit them, or by the
  tasks in a workflow** — not IMRaD. Instruction sections get imperative headings.
- **End every substantive section with a bulleted summary** so the summaries alone are
  usable; make the checklist the deliverable; add a decision flowchart branching on what
  data the reader has.
- **Simulate a known truth, then degrade the data one imperfection per section**, so every
  "what does this do to the estimate, and by how much?" is checkable.
- **Quantify the cost of bad practice** three ways: a before/after pair on a familiar
  parameter, a worst-case magnitude, and the downstream consequence for the quantity people
  actually use.
- **"We recommend", specifically and repeatedly; never "must".** Say what you do *not*
  recommend, with a structural reason. Hedge applicability, not confidence.
- **Name methods after their authors, run each in its canonical implementation, count its
  parametric assumptions, and organise everything around one small closed set of problems.**

## Anti-patterns

- Recommendations with no stated cost of ignoring them.
- Illustrative examples presented as if they were a systematic review.

## Checklist

Run with the `SKILL.md` §11 checklist before returning.

- [ ] Sections are problems or tasks; instruction sections have imperative headings.
- [ ] Every substantive section ends with a bulleted summary; the summaries alone are usable.
- [ ] Evidence comes from synthetic data with a known truth, degraded one imperfection per section.
- [ ] Every recommendation has the cost of ignoring it, quantified and traced downstream.
- [ ] Direction, magnitude and timing given for every bias.
- [ ] At least one explicit negative recommendation, with a structural reason.
- [ ] A closed, named set of problems, used consistently across all tables and figures.
- [ ] Checklist and/or decision flowchart branching on what data the reader has.
- [ ] Scope disclosed: illustrative examples labelled as such; the hard boundary named.
