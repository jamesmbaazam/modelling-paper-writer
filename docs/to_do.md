# To do

Section 0 is the working list from the 2026-10-03 critique and the public-release pass.
Sections 1–6 are the 2026-09-13 critique, kept as a record; line references there were to
`SKILL.md` as of commit `43f3359`, so use section numbers rather than lines.

## 0. 2026-10-03 critique and public release

**Instruction conflicts** — done 2026-10-03
- [x] A1. `Research in context` panel: internal scaffolding only. Step 4 and `checklist.md`
      already said so; `evidence.md` §1.2 still told the reader to *write* it, now reworded to
      *plan with* it and to return it only when the journal requires the panel or the user asks.
- [x] A2. Procedure step 2 asks about venue and budget only for titles, abstracts, heading
      schemes and full papers; otherwise it assumes a default and states it in the closing
      note. `checklist.md` matches. No change needed.
- [x] A3. All five abstract-only exemplars carry † in §0 (enforced against `papers.csv` by
      `corpus.py check`), and each now opens with `## Section analysis unavailable — use a
      full-text exemplar`, naming two full-text substitutes for its archetype. The 32
      full-text files were renamed onto one canonical heading set matching the `SKILL.md` rule
      sections — `Structure`, `Opening move`, `Methods`, `Results`, `Literature`, `Voice`,
      `Discussion and limitations`, `Data, code and funding`, `Distinctive moves to borrow`,
      `Related files` — with distinctive titles kept as a trailing `— …` gloss (*Methods —
      screening as evidence*) and topical extras left alone. Step 3 now lists the headings,
      says to match on the prefix, and gives the fallback when a section is absent.
      `corpus.py check` errors on a missing core heading and notes the sections a paper's
      analysis genuinely lacks (Literature in 8 files, Voice in 6).
- [x] A4. `evidence.md` header now forbids reading it whole and gives the procedure: find the
      §N.M in its Contents, grep for that heading and the next, read that range only. The
      `SKILL.md` file table says the same. TOCs checked: `evidence.md` (1,222 lines) and
      `examples.md` (324) have complete ones; every other reference file is under 100 lines.

**Claims the repo contradicts** — done 2026-10-03
- [x] B1. `SKILL.md` §10 was already reworded (it now cites Earn 2000's "still poorly
      understood" as the near-miss that proves the rule). Five further absolutes in
      `evidence.md` were unverifiable or false and are now scoped to what the corpus shows:
      the six-move spine (reviews carry only moves 1, 2 and 6; abstract-only papers can be
      checked only for what their abstracts show), generic hedging, numbers without a
      comparator, the main-text-algebra claim, and "no paper opens by naming a method" —
      which Lee 2010, in the same section's own sub-corpus, contradicts. That exception is
      now stated, with the reason: a simulation benchmark's problem *is* a methodological
      claim, so open on the method when you are evaluating methods.
- [x] B2. README's section list rebuilt to the current `SKILL.md`: fifteen archetypes, the
      current section names (§1 Structure with titles and abstract budgets, §10 Banned
      phrases), journal templates located in `evidence.md` §1.2, §7 and §9 marked as loading
      from `references/`, and the checklist and worked examples named as separate files. Also
      corrected the `SKILL.md` row, which still claimed the checklist was inside it.
- [x] B3. Already corrected: §2's preamble now says all five guardrails are in the *Hard
      rules* block.
- [x] B4. Eight superlatives removed from `evidence.md` and two from corpus-file headings
      ("the most quotable passage in the corpus", "the exemplar in this corpus"). The
      calibration rule no longer calls it Wynants 2020's "single most common failing" — that
      paper names six recurring failings without ranking them. Superlatives inside quotations
      are left alone.

**Structure** — done 2026-10-03
- [x] C1. `references/corpus/papers.csv` is the single source: 13 columns including label,
      year, venue, archetype, role and full_text. `tools/corpus.py index` generates
      `references/corpus-index.md` *and* the corpus block in `README.md` (between
      `<!-- corpus:begin -->` markers); `tools/corpus.py check` fails on drift. It now also
      verifies the paper count, year range and COVID-19 count stated in `SKILL.md`'s preamble,
      and that every `Author YEAR` citation in the rule files names a real corpus paper —
      `EXTERNAL_LABELS` holds the deliberate exceptions (currently Bennett 2012, cited for a
      ◆ reporting-guideline rule). Verified by temporarily breaking each: a stale README block,
      a wrong preamble count, an added CSV row and a mistyped label all fail the check.
      The `role` column was reviewed and kept: 29 of 37 roles say something the archetype does
      not ("Living methods + tool" for Abbott 2020), so it is not duplication.
- [x] C2. Merged in `papers.csv` — one "Hybrid (mathematical-statistical)" at 17 papers. The
      README still showed the old 12/5 split, which is what prompted generating that table
      rather than maintaining it by hand.
- [x] C3. Done: `writing_styles/` → `references/corpus/`, every path updated. Two deliberate
      exceptions, both historical records that would be falsified by editing them:
      `docs/prompt.md` (the original brief, quoted verbatim) and the §1–§6 entries in this file.

**Content and provenance** — done 2026-10-03
- [x] D1. The hard rule was already in `SKILL.md`: cite as `[Author YEAR]` only papers the
      user supplied or that `papers.csv` holds, `[Author YEAR?]` for anything recalled, and
      list every citation to verify. The checklist only said "no invented citations", so it now
      carries the full rule — recalled citations are marked and go on the verify list, never
      into the text as settled. `corpus.py check` enforces the repo's own half of this: every
      `Author YEAR` in a rule file must name a real corpus paper (C1).
- [x] D2. The ◆ convention is now defined in `evidence.md` as well as `SKILL.md`, and applied
      to ten rules that are journal instructions or general practice rather than corpus
      observations: abstract and main-text budgets, main-text display-item limits, the default
      figure allocation, declarative captions, log scaling, colour consistency, axis labelling
      and table formatting. EVPI needed no mark — it is Li 2017's, cited on the line.
      Also corrected one rule the corpus contradicts: titles were said to run "10–18 words,
      under 15 for *Nature*/*Science*", but the measured range is 6–20 (median 10, half between
      8 and 13), and *Nature*/*Science* reach 17 (Tian 2020). The banned title words were
      checked and do hold — none appears in any corpus title.
- [x] D3. `tools/verify_quotes.py` and `docs/quote-verification.md` already existed; re-run
      after this session's edits with no change and no misquotes: **538 verified, 0 not found,
      185 unchecked (no open full text reachable), 6 reviewed by hand**. Coverage is now stated
      in the README, generated from the report by `corpus.py index` so it cannot go stale —
      verified by editing the totals line and watching `check` fail. The README file table also
      gained rows for `docs/quote-verification.md` and `tools/`.

**Evals**
- [ ] E1. Grade that a corpus file was read (`tool_used: Read`).
- [ ] E2. Case for no unnecessary venue question and no `Research in context` leakage.
- [ ] E3. Grade that `references/ml-prediction.md` loads for ML; add a guidance-archetype case.
- [ ] E4. Run the suite and commit a baseline summary.

**Public release (Agent Skills spec + Claude Code plugin standards)**
- [ ] F1. Frontmatter: third-person description ≤1024 chars, `license`, `metadata`.
- [ ] F2. `.claude-plugin/plugin.json` and `marketplace.json`; pass `claude plugin validate`.
- [~] F3. Versioning: nothing has been released, so the skill stays at **1.0.0** —
      `SKILL.md`, `plugin.json` and `CITATION.cff` now agree on it, and `CITATION.cff` no longer
      claims a `date-released` for a release that never happened. `CHANGELOG.md` added, stating
      what major, minor and patch mean for a skill and carrying one `## [1.0.0] — unreleased`
      section; pre-release development stays in the git history and in this file.
      `corpus.py check` fails if the three version strings drift, if the current version has no
      `## [version]` section, or if the changelog is not newest-first. **Remaining:** tag 1.0.0
      and date it in both files, once C–F are done.
- [ ] F4. CI: validate manifests, frontmatter, links and index on every push.
- [ ] F5. README: install routes (marketplace, git clone, claude.ai upload), corpus
      verification status.
- [ ] F6. `CONTRIBUTING.md` for adding papers.
- [ ] F7. Packaging script that builds the upload zip without the dev files.

## 1. Restructure: procedure first, progressive disclosure for the rest

SKILL.md is ~1,420 lines / ~13,700 words (~22k tokens), loaded in full on every invocation.
It describes what good papers look like but never tells Claude what to do.

- [x] Add an explicit procedure at the top of SKILL.md:
  1. Determine mode — draft from scratch / revise a pasted draft / critique only.
  2. Establish archetype (§0), target venue and word limit; ask if not inferable.
  3. Read the matching `writing_styles/NN-*.md` file (make this a required step, not a suggestion).
  4. Draft or edit the requested section only.
  5. Self-review against the §11 checklist before returning.
- [x] Cut SKILL.md to ~300–400 lines: procedure, archetype table, rules as bolded imperatives,
      anti-patterns, checklist.
- [x] Move corpus quotations that *justify* each rule into `references/evidence.md`
      (mirror the section numbering so rules and evidence stay linked).
- [x] Move §12 worked examples into `references/examples.md` (or one file per archetype).
- [x] Replace `NN` code references (`01`, `22`…, 225 occurrences) with `Author YEAR` inline so
      Claude does not need the index table to interpret them.
- [x] 2026-10-03 token pass: SKILL.md ~4,900 → ~3,500 words. Moved §7 (ML) and §9 (guidance)
      with their checklist blocks to `references/ml-prediction.md` and
      `references/guidance-papers.md`; folded headline shapes into the §0 table; cut §10 to
      banned phrases; journal templates now only in `evidence.md` §1.2; exemplars read one
      file (or one section) at a time.

## 2. Guardrails for the failure modes that matter most

All five are now in the *Hard rules* block of `SKILL.md`.

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
