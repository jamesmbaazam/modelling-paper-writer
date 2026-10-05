# Working checklist

Companion to `SKILL.md` (procedure step 5). Run this before returning any drafted or revised
section. Only the blocks relevant to the section and archetype apply. Section numbers refer to
`SKILL.md`.

**Before drafting**
- [ ] Archetype identified; the matching file in `references/corpus/` read.
- [ ] Venue, budget and heading scheme fixed where the section's shape depends on them;
      otherwise a default assumed and stated in the closing note.
- [ ] Headline claim written (for yourself) as one sentence in the right shape for the archetype.
- [ ] Abstract or full paper: `Research in context` triplet planned; returned only if required
      or asked.

**Methods**
- [ ] Model named, its class stated, structure described in words before any equation.
- [ ] Every assumption a declarative sentence with a reason and, where possible, a direction of bias.
- [ ] Parameter table with sources and a fixed/sampled/fitted column (`examples.md` §12.12).
- [ ] Baseline scenario declared; scenario grid enumerated exhaustively (`examples.md` §12.13).
- [ ] Sensitivity analyses named by what they vary, each reported with its conclusion.
- [ ] Priors justified; MCMC detail, software versions and data-lock date given.

**Results**
- [ ] Every estimate has the right kind of interval, labelled and used consistently.
- [ ] Every number has a comparator (baseline, capacity, reference scenario, prior literature).
- [ ] Policy-relevant quantile leads, not the mean.
- [ ] Where the model failed, that is in the Results.
- [ ] Verbs and modals graded to the design and to the evidence.
- [ ] Figures: parameters in captions; observed data overlaid on simulations; baseline in every panel.

**Discussion**
- [ ] Opens with the tension or the general lesson, not a restatement.
- [ ] Limitations signposted, categorised, each naming the question it blocks, discharged
      where possible, with scope fences; each becomes the next research question.
- [ ] Closes on a decision, a data priority, or a question.

**Back matter**
- [ ] Data and code: repository link (GitHub is acceptable; no DOI archive required); licence; language and version.
- [ ] Individual-level data shared and de-identified, or posterior samples published instead.
- [ ] Funder role, conflicts, preprint disclosure, per-author contributions.
- [ ] Reporting guideline named (§6) and its checklist attached.

**Hard rules**
- [ ] Every `[Author YEAR]` citation is one the user supplied. Everything else — including any
      corpus paper — is `[ref]` or `[Author YEAR?]` and appears on the verify list, never in the
      text as though it were settled. No journal, volume, page or DOI written from memory.
- [ ] No invented numbers or DOIs (a number computed from, or read from, the user's material is not invented, but its derivation is in the closing note); every placeholder listed for the user, with what is needed
      to fill it.
- [ ] No corpus sentence reused verbatim.
- [ ] Revision mode: voice, spelling and tense preserved; edits shown; scope not expanded.
- [ ] Nothing returned beyond the requested section; scaffolding kept out unless asked.

**ML or guidance archetype**: also run the checklist block in `ml-prediction.md` or
`guidance-papers.md`.
