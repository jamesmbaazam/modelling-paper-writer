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
- [x] F1. Done: third-person `description` at 938 of 1,024 characters, ending in a negative
      trigger, plus `license` and `metadata`. `corpus.py check` enforces the name pattern, the
      description length and the presence of `license`.
- [x] F2. Both manifests exist and `claude plugin validate .` passes. Manifest validation is
      now also in `corpus.py check` — required fields, `plugin.json` name matching the skill
      name, `skills: ["./"]`, and `marketplace.json` actually listing the plugin — so CI does
      not depend on the Claude CLI being installed. Verified by deleting `license` and renaming
      the plugin and watching all three errors fire.
- [~] F3. Versioning: nothing has been released, so the skill stays at **1.0.0** —
      `SKILL.md`, `plugin.json` and `CITATION.cff` now agree on it, and `CITATION.cff` no longer
      claims a `date-released` for a release that never happened. `CHANGELOG.md` added, stating
      what major, minor and patch mean for a skill and carrying one `## [1.0.0] — unreleased`
      section; pre-release development stays in the git history and in this file.
      `corpus.py check` fails if the three version strings drift, if the current version has no
      `## [version]` section, or if the changelog is not newest-first. **Remaining:** tag 1.0.0
      and date it in both files, once the evals (E) are done.
- [x] F4. Two workflows. `.github/workflows/check.yml` runs `corpus.py check` plus
      `claude plugin validate` on every push to main, every pull request and on demand.
      `.github/workflows/quotes.yml` runs `verify_quotes.py` monthly and on demand, kept
      separate because it fetches from Europe PMC and PMC — too slow for every push, and a
      network failure should not fail an unrelated PR. `verify_quotes.py` now exits non-zero
      when a quotation is absent from a full text it could reach, so CI catches a misquote.
- [x] F5. README now gives all three install routes — plugin marketplace (recommended), git
      clone into `~/.claude/skills/`, and the claude.ai upload zip — and states the quotation
      verification coverage, generated from the report. The stale "add a row to
      `corpus-index.md`" instruction is gone; that file is generated.
- [x] F6. `CONTRIBUTING.md`: setup and the five commands, which files are generated and must
      not be hand-edited, how to add a paper (canonical headings, required sections,
      `papers.csv` columns, the abstract-only requirements, regenerating, new archetypes), the
      rule that every rule is attributable or ◆, the instruction to count corpus claims that
      are countable, the eval convention, and the versioning rules.
- [x] F7. `tools/package.py` builds `dist/<skill>-<version>.zip` — 49 files, 202 KB, nested
      under one top-level directory — containing `SKILL.md`, `references/`, the licence,
      citation, README and changelog, and excluding `tools/`, `evals/`, `docs/`, `.github/`
      and `.claude-plugin/`. It refuses to build if `corpus.py check` fails, and `--list`
      prints the contents without building. `dist/` is gitignored.

**Cross-references** — found 2026-10-05 during Phase 5, left for a separate pass
- [ ] G1. Six corpus files cite `SKILL.md` subsections that the §1 restructure removed:
      `SKILL.md` now numbers only its top-level rule sections, and the §N.M numbering lives on
      in `evidence.md`. Stale: §2.1 (Ximenes 2014, Verguet 2015), §2.3 (Ganyani 2020), §3.4
      (Thompson 2019, Ngonghala 2020), §6.2 (McGough 2020). Point each to `SKILL.md` §N with
      its evidence in `evidence.md` §N.M, as files 66 and 67 now do, after checking that the
      §N.M in `evidence.md` holds the rule the file means. Then have `corpus.py check` reject
      any `SKILL.md` §N.M reference, so the drift cannot recur.
- [ ] G2. Back-links between exemplars of the same archetype. The expansion phases linked
      each new file to its older siblings but never the reverse, and some original files
      never linked each other: after Phase 6, 43 files lack a link to at least one later file
      in the same archetype (38 before it; the 34 first recorded here counted only the files
      up to id 44). Phase 5's share is Pawelek 2012 (→ Néant 2021, Clapham 2014) and Kerr
      2021a (→ Ajelli 2010, Kerr 2021b); Phase 6 added McGough 2020 (→ Günther 2021, Wolffram
      2023), Finger 2019 (→ Camacho 2015, Shi 2016), Bracher 2021b and Funk 2019 (→ Wolffram
      2023) and Zhao 2020 (→ Günther 2021, Camacho 2015). The worst cases are forecast
      evaluation (Cramer 2022 links none of its seven siblings), methods / simulation
      benchmark and real-time transmission analysis. Add a sentence to each `Related files`
      saying what the sibling adds, not a bare link; consider a `corpus.py check` note listing
      unlinked same-archetype pairs. Phase 6 is done, so this can now be done in one pass.

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
- [x] Add papers from the venues most users target — done 2026-10-03: Thompson 2019
      (*Epidemics*), Zhao 2020 (*Epidemiology & Infection*), Finger 2019 (*BMC Medicine*),
      Ngonghala 2020 (*Mathematical Biosciences*), Griffin 2015 (*Proc R Soc B*), Verguet 2015
      (*Vaccine*), plus Chen 2019 (*Lancet Glob Health*), Geoghegan 2020 (*Nature
      Communications*) and Prayitno 2017 (*PLoS NTD*). Eurosurveillance and agency reports are
      still absent: Europe PMC returns few Eurosurveillance modelling papers under the search
      used, and agency reports are mostly outside its index.
- [x] Add missing archetypes — all seven done 2026-10-03: Chen 2019 (vaccine impact and
      economic evaluation, the first exemplar behind the ◆ CHEERS rule), Geoghegan 2020
      (phylodynamics / genomic epidemiology), Prayitno 2017 (serological inference), Pawelek
      2012 (within-host), Kerr 2021a (agent-based model documentation, behind the ◆ ODD rule),
      McGough 2020 (nowcasting / reporting delays) and Finger 2019 (rapid-response outbreak
      analysis). `SKILL.md` §0 now has 22 archetype rows; the corpus is 49 papers.
- [x] Consider replacing the 5 abstract-only files (`03`, `05`, `06`, `17`, `18`) with
      open-access equivalents — **resolved by promotion, not replacement (2026-10-03).** The
      user supplied the publisher PDFs, so all five were analysed in full and rewritten under
      the canonical headings; the corpus goes from 32 to 37 papers usable for section-level
      work, and the †/abstract-only machinery is gone from `SKILL.md`, `corpus.py` and the
      generated files. `papers.csv` gains a third `full_text` value, `publisher pdf`, and
      `verify_quotes.py` gains `--local-text`; 207 new quotations were machine-checked against
      the PDFs before deletion, 3 more against the page images by eye.
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
- [x] Add a script or make target that regenerates the index table from `papers.csv` —
      `tools/corpus.py index`, which also writes the README corpus block (see C1).

## 7. Second expansion (approved 2026-10-04): two more exemplars per single-exemplar archetype

Ten archetypes had one exemplar each; the agreed plan adds two more to each, plus further
Sebastian Funk work on forecast evaluation. 24 papers in six phases.

- [x] Phase 1 — forecast evaluation: Funk 2019 (*PLoS Comput Biol*), Sherratt 2023 (*eLife*),
      Bosse 2023 (*PLoS Comput Biol*), Bracher 2021b (*Nat Commun*). Adding the last collided
      with the existing Bracher 2021 label, so the WIS paper became Bracher 2021a; `corpus.py
      check` now rejects duplicate labels.
- [x] Phase 2 — parameter estimation: Ganyani 2020 (*Eurosurveillance*, closing that venue
      gap), Stopard 2021 (*PLoS Comput Biol*); competing hypotheses: Lavine 2021 (*Science*),
      Yakob 2015 (*Sci Rep*).
- [x] Phase 3 — clinical prediction: Yadaw 2020 (*Lancet Digital Health*), Berenguer 2021
      (*Thorax*); vaccine impact: Watson 2022 (*Lancet Infect Dis*), Abbas 2020 (*Lancet Glob
      Health*). The two clinical-prediction files are a deliberate contrast: Yadaw's dual-split
      design is exemplary but its performance reporting omits calibration, auPRC, an interval
      on the AUC and a named operating point, so its file carries a *what to avoid* section;
      Berenguer is TRIPOD-compliant and supplies all four.
- [x] Phase 4 — phylodynamics: Grubaugh 2017 (*Nature*), Lemieux 2021 (*Science*);
      serological inference: Ximenes 2014 (*PLoS ONE*), Golden 2016 (*Parasites & Vectors*).
      Grubaugh supplies the bounded introduction count and the R₀<1-plus-importation
      reconciliation; Lemieux the marker-allele tracer and the limit that migration can
      outpace mutation. Ximenes compares three mixing structures rather than fitting one;
      Golden validates the serological marker before modelling it, and reads a two-phase
      force of infection as a record of the control programme.
- [x] Phase 5 — within-host: Néant 2021 (*PNAS*), Clapham 2014 (*J R Soc Interface*);
      agent-based model documentation: Ajelli 2010 (*BMC Infect Dis*), Kerr 2021b (*Nat
      Commun*). The new Kerr paper collided with the Covasim label, which became Kerr 2021a.
      Néant joins a viral-kinetic model to a survival endpoint and restates its conclusion so
      it survives a disputed R₀; Clapham tests antibody-dependent enhancement by which
      parameter must differ, and discriminates two equally good fits on the biological
      plausibility of their estimates. Ajelli supplies the synchronised head-to-head
      comparison that justifies choosing an agent-based model at all; Kerr 2021b is the
      application paper Covasim's documentation makes possible, cited in one sentence and
      validated against the months that followed. Ajelli and Kerr 2021b also sit under
      *Methods / simulation benchmark* and *Scenario projection for policy* respectively.
- [x] Phase 6 — nowcasting: Günther 2021 (*Biom J*), Wolffram 2023 (*PLoS Comput Biol*);
      rapid response: Camacho 2015 (*PLoS Curr*), Shi 2016 (*Environ Health Perspect*).
      Günther runs a nowcast daily for a health authority, names the missing-at-random
      assumption behind its onset imputation and builds the sensitivity analysis to break it,
      and says which outputs survive constant under-ascertainment. Wolffram is the
      pre-registered real-time comparison of eight nowcasting systems: it keeps the
      pre-registered target as primary, then shows with numbers why it was the wrong one, and
      decomposes the winner's success into two errors that cancelled. Camacho converts a
      district-level transmission model into beds needed against beds available, tests its
      forecast on two weeks of data that arrived during review, and gives each bias's
      direction separately for each output. Shi supplies the criteria an operational
      forecast must meet and a dated warning that moved a national campaign two months
      earlier; like Yadaw 2020 its file carries a *what to avoid* section (MAPE only, intervals
      from residual spread, no baseline, no code). Günther and Camacho also sit under
      *Real-time transmission analysis*, Wolffram under *Forecast evaluation*. With this phase
      the second expansion is complete: every archetype that had one exemplar now has three.
