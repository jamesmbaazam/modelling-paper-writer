# To do

Working list from the 2026-09-13 critique of the skill. Ordered by priority; tick items off as
they are done. Line references are to `SKILL.md` as of commit `43f3359` (before the 2026-09-15 edits, which
added a *Hard rules* block near the top and shifted later lines down).

## 1. Restructure: procedure first, progressive disclosure for the rest

SKILL.md is ~1,420 lines / ~13,700 words (~22k tokens), loaded in full on every invocation.
It describes what good papers look like but never tells Claude what to do.

- [ ] Add an explicit procedure at the top of SKILL.md:
  1. Determine mode — draft from scratch / revise a pasted draft / critique only.
  2. Establish archetype (§0), target venue and word limit; ask if not inferable.
  3. Read the matching `writing_styles/NN-*.md` file (make this a required step, not a suggestion).
  4. Draft or edit the requested section only.
  5. Self-review against the §11 checklist before returning.
- [ ] Cut SKILL.md to ~300–400 lines: procedure, archetype table, rules as bolded imperatives,
      anti-patterns, checklist.
- [ ] Move corpus quotations that *justify* each rule into `references/evidence.md`
      (mirror the section numbering so rules and evidence stay linked).
- [ ] Move §12 worked examples into `references/examples.md` (or one file per archetype).
- [ ] Replace `NN` code references (`01`, `22`…, 225 occurrences) with `Author YEAR` inline so
      Claude does not need the index table to interpret them.

## 2. Guardrails for the failure modes that matter most

None of these exist in SKILL.md today; each is a one-liner.

- [x] Never invent a citation, DOI or author — use `[ref]` / `[Author YEAR]` placeholders and
      list what needs a source.
- [x] Never invent a number — if the user has not supplied a result, write
      `[X% (95% CrI [a–b])]`-style placeholders, not plausible values.
- [x] Do not reuse corpus sentences verbatim in a user's manuscript.
- [x] Revision mode: preserve the author's voice, spelling variant (UK/US) and tense; show
      edits rather than silently rewriting; do not expand beyond the requested section.
- [x] Journal typography: middle-dot decimals ("2·5", 13 occurrences) are Lancet-only; say so.
      Same for "to" vs en dash in intervals.

## 3. Internal inconsistencies

- [x] `SKILL.md:461` "Six ways to position against prior work" — lists seven.
- [x] `SKILL.md:912` "Four rules for writing them" — lists six.
- [x] `SKILL.md:681` "two appraisals of the field's failures" — names three.
- [x] §0 claim-shape list has "critique →" twice with different shapes (identifiability limit
      vs named failure mode). Split into two archetypes or merge.
- [x] `SKILL.md:112` files `01` Grais (*J R Soc Interface*) under "PLoS / methods journals".
- [x] `03` Keeling is in the index but not in the §0 archetype table, and is abstract-only, so
      cannot support the §1.2 Nature/Science structural claim it is cited for.
- [x] §10 bans "to the best of our knowledge"; §12.3 strong example uses "none, to our
      knowledge". State the actual rule: the *first-study* claim is banned, not the hedge.

## 4. Corpus and coverage claims

- [x] README lists tuberculosis, malaria and AMR as covered; no corpus paper models any of
      them (only passing mentions in `14` Baker and `29` Bhatt). Correct the README.
- [x] State the selection basis honestly: landmark/high-citation papers from a narrow set of
      groups; 11/37 are COVID-19.
- [ ] Add papers from the venues most users target: *Epidemics*, *Epidemiology & Infection*,
      *BMC Med*, *Math Biosci*, *Proc B*, *Vaccine*, *Eurosurveillance*, agency reports.
- [ ] Add missing archetypes: vaccine impact / cost-effectiveness, phylodynamics / genomic
      epi, serological inference, within-host, agent-based model documentation, reporting-delay
      nowcasting, rapid-response technical reports.
- [ ] Consider replacing the 5 abstract-only files (`03`, `05`, `06`, `17`, `18`) with
      open-access equivalents.
- [x] Flag date drift: rules derived from 2000–2008 papers (e.g. §4.1 "~1 citation per 300
      words") may not match current reviewer expectations.

## 5. Missing content

- [x] Title craft — nothing currently; corpus has good examples.
- [x] Abstract word limits and structured-abstract field budgets per journal (§1.2 names
      fields, not budgets).
- [x] Parameter table template (referenced repeatedly in §11, never shown).
- [x] Scenario-definition table template (§2.4 calls it "the most reusable artefact").
- [x] Figures and tables beyond §3.6's six bullets; main text vs supplementary split.
- [x] Complete the reporting-guideline list: CHEERS, ODD, PRISMA (review archetype),
      modelling-specific checklists (e.g. Bennett et al. 2012), alongside EPIFORGE / TRIPOD.
- [x] Equations in real toolchains: §12.1 uses `&nbsp;` + markdown italics. Provide LaTeX
      (`\begin{align}`) and Unicode/Word variants.
- [ ] (Optional, adjacent) response-to-reviewers and cover letter guidance.

## 6. Housekeeping

- [x] Description is 963 chars (limit ~1024) with no negative trigger; add e.g. "not for
      empirical or observational studies without a modelling component".
- [x] Move `prompt.md` to `docs/` — it is provenance, not skill content.
- [x] Add `evals/` with ~a dozen prompts and a rubric drawn from §11 (e.g. "write a
      limitations paragraph for this branching-process model", "rewrite this abstract for
      Lancet ID", "critique my methods section") so the restructure in §1 can be checked for
      regressions with `claude plugin eval` / `/skill-doctor`.
- [x] Replace `[[wikilinks]]` in `writing_styles/*.md` with relative paths Claude can open.
- [ ] Add a script or make target that regenerates the index table from `papers.csv`.
