# 36 — Roberts et al. (2021), *Nature Machine Intelligence*
**"Common pitfalls and recommendations for using machine learning to detect and prognosticate for COVID-19 using chest radiographs and CT scans"**
Roberts M, Driggs D, Thorpe M, Gilbey J, Yeung M, Ursprung S, Aviles-Rivero AI, Etmann C, McCague C, Beer L, Weir-McCall JR, Teng Z, Gkrania-Klotsas E, AIX-COVNET, Rudd JHF, Sala E, Schönlieb C-B. *Nat Mach Intell* 3:199–217. doi:10.1038/s42256-021-00307-0.
**Citations:** ~1,000 (OpenAlex, Sept 2026).

**Archetype:** the *systematic review that becomes a guidance document* — a critical appraisal (like `35`) whose second half is a structured set of recommendations addressed to distinct audiences. Combines the critique archetype with the best-practice archetype of §8.

## Structure
Abstract → Introduction → `Results` (screening, quality screening failures, dataset problems, methodology problems, reproducibility) → `Discussion` → **recommendations in five named domains** → Methods → Supplementary Discussion.

The five domains are declared explicitly and then used as the organising spine:
> "we offer recommendations in five distinct areas: (1) the data used for model development and common pitfalls; (2) the evaluation of trained models; (3) reproducibility; (4) documentation in manuscripts; and (5) the peer-review process."

Recommendations are then delivered under audience-specific headings — *Recommendations for data*, *Recommendations for authors*, and guidance for reviewers. **Addressing reviewers separately is unusual and effective**: it tells the community how to enforce the standard, not just how to meet it.

## Opening move
> "Machine learning methods offer great promise for fast and accurate detection and prognostication of coronavirus disease 2019 (COVID-19) from standard-of-care chest radiographs (CXR) and chest computed tomography (CT) images. Many articles have been published in 2020 describing new machine learning-based models for both of these tasks, but it is unclear which are of potential clinical utility."

And the verdict, in the abstract:
> "Our review finds that none of the models identified are of potential clinical use due to methodological flaws and/or underlying biases. This is a major weakness, given the urgency with which validated COVID-19 models are needed. To address this, we give many recommendations which, if followed, will solve these issues and lead to higher-quality model development and well-documented manuscripts."

Pattern: **promise stated generously → the problem stated flatly → the negative verdict → and immediately, the constructive turn.** "To address this, we give many recommendations" appears in the abstract, so the paper is never merely destructive.

The Introduction is similarly even-handed before it turns critical — it grants that "there is fantastic promise for applying machine learning methods to COVID-19 radiological imaging", lists five specific reasons no model is deployable, and notes that "researchers have answered the 'call to arms'".

## The named pitfalls
The paper's lasting contribution is a vocabulary for dataset failures, of which one term entered general use:

> "**Frankenstein datasets.** The issues of duplication and source become compounded when public 'Frankenstein' datasets are used, that is, datasets assembled from other datasets and redistributed under a new name. For instance, one dataset combined several other datasets without realizing that one…"

Others, each stated as a mechanism a reader can check for in their own work:
> "most of the images have been pre-processed and compressed into non-DICOM formats leading to a loss in quality and a lack of consistency/comparability."
> "The timing between imaging and RT–PCR tests was also largely undocumented, which has implications for the validity of the ground truth used. It is also important to recognize that a negative RT–PCR test does not necessarily mean that a patient does not have COVID-19."
> "it is likely that more interesting, unusual or severe cases of COVID-19 appear in publications."
> "All proposed models suffer from a high or unclear risk of bias in at least one domain."

And the one that is pure gold for anyone building an imaging classifier — **a confound that mimics the signal**:
> "researchers should be aware that algorithms might associate more severe disease not with CXR imaging features, but the view that has been used to acquire that CXR. For example, for patients that are sick and immobile, an anteroposterior CXR view is used…"

## Screening as evidence
The scale of the exclusion is itself the finding, and it is reported with a PRISMA flow diagram: 2,212 studies identified → 415 after initial screening → **62 included after quality screening**. The reasons are quantified against published checklists:
> "We found that 110 papers (51%) fail at least three of our identified mandatory criteria from the CLAIM checklist, with 23% failing two and 26% failing just one."
> "the two factors that lead to the lowest RQS results were omission of the following. (1) Feature reduction techniques in 52% of papers (2) Model validation in 61% of papers"

**Quantify how many papers fail each specific criterion.** A percentage attached to a named omission is far more useful than "reporting was poor".

## Recommendations
> "For authors, we recommend assessing their paper against appropriate established frameworks, such as RQS, CLAIM, transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD), PROBAST and Quality Assessment of Diagnostic Accuracy Studies (QUADAS)."
> "First, we advise caution over the use of public repositories, which can lead to high risks of bias due to source issues and Frankenstein datasets as discussed above. Furthermore, authors should aim to match demographics…"

The appraisal thresholds the reviewers themselves used are disclosed, so their judgements can be contested:
> "for the 'Were there a reasonable number of participants?' question of the analysis domain, we required a model to be trained on at least 20 events per variable for the size of the dataset to score a low risk of bias. However, events per variable may not…"

**Publish the threshold you applied.** It converts a subjective rating into a reproducible one.

## Voice
First-person plural, measured, and scrupulously fair to the papers being criticised — flaws are attributed to circumstances and to systemic incentives rather than to incompetence, and the authors note that excluded preprints "may possibly pass the systematic evaluation in a future revision". The verdict is nonetheless unhedged.

## Distinctive moves to borrow
1. **Coin a name for a failure mode** ("Frankenstein datasets") — it is how a critique gets adopted.
2. **Declare your recommendation domains as a numbered list in the text**, then use them as headings.
3. **Write recommendations for reviewers as well as for authors.**
4. **Quantify failures per named criterion**, with percentages.
5. **Disclose your own appraisal thresholds.**
6. Name the confound that could produce your outcome without the intended signal (the CXR view).
7. Put the constructive turn in the abstract, immediately after the negative verdict.

## Related files
Companion to [[35-wynants-2020-covid-prediction-models-review]]; shares the guidance architecture of [[27-gostic-2020-practical-considerations-rt]] and [[28-charniga-2024-delay-distributions-best-practices]].
