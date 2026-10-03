# 33 — Han, Schmidt, Bowden & Drake (2015), *PNAS*
**"Rodent reservoirs of future zoonotic diseases"**
*PNAS* 112(22):7039–7044. doi:10.1073/pnas.1501598112. PMC4460448.
**Citations:** ~660 (OpenAlex, Sept 2026).

**Archetype:** the *classifier-as-discovery-engine* paper — boosted regression trees on species traits, used not to explain but to generate a ranked list of named candidates for field investigation. The clearest train/test discipline in this corpus.

## Structure
`Significance` → Abstract → Introduction → **`Results and Discussion`** (merged) → `Methods` (*Data · Analyses · Maps*) → Acknowledgements → Datasets S1–S5.

Merging Results and Discussion suits a paper whose findings need immediate ecological interpretation; the trait patterns and their meaning arrive together.

## Opening move
> "Forecasting reservoirs of zoonotic disease is a pressing public health priority. We apply machine learning to datasets describing the biological, ecological, and life history traits of rodents, which collectively carry a disproportionate number of zoonotic pathogens."

Pattern: **priority → "We apply machine learning to…" → why this taxon.** Two sentences. The method is named in the second word of the second sentence and never dwelt on.

## Methods — supervised learning conventions
- **Algorithm named and justified by properties of the data, not by fashion**: "generalized boosted regressions"/"boosted regression trees"; they "have particular use for comparative ecological studies because they accommodate multiple data types as covariates, nonrandom patterns of data missingness, and hidden, nonlinear interactions." Contrasted with classical comparative methods that assume independence. Framed as "Model-free approaches allow the data to speak for themselves."
- **Explicit train/test split, stated as a single unambiguous sentence**: "Datasets were partitioned into training (80% of all 2,277 species) and test (the remaining 20%) sets before analysis." The words *before analysis* are doing real work.
- **Cross-validation named with its purpose**: "10-fold cross-validation during model building to prevent overfitting."
- Tuning reported: "Built 800–10,000 trees for each analysis", Bernoulli or Poisson error depending on response type, with the full tuning-parameter table in Dataset S3.
- **Three response variables from one dataset** — binary reservoir status, count of zoonoses, binary "hyperreservoir" status — so the same features are interrogated three ways.
- Performance: "~90% accuracy" for classification, pseudo-R² for the count model (0.21). *Weaker than modern practice*: no AUC, no sensitivity/specificity, no confusion matrix in the main text. Compare Zoabi 2021 Zoabi, which reports auROC with bootstrap CIs and two explicit operating points.
- **Class imbalance handled by an explicit, conservative labelling decision that is disclosed**: 217 known reservoirs against 2,060 unlabelled species, all treated as negatives — "Unknown reservoirs (2,061 species) were designated nonreservoirs… we adopted a more conservative designation to develop predictive models, with baseline classification performance that can only improve with ongoing discoveries." The bias is named and its direction stated.
- **Sampling bias tested rather than assumed away**: literature citation counts used "as a proxy for sampling intensity", then a model of *studiedness* fitted and shown to be weak (pseudo-R² 0.07–0.17), supporting the conclusion that "the trait patterns of well-studied rodents and those of rodent reservoirs are not coincident." **Fit a model of your own sampling process and show it does not reproduce your result.**
- **Variable importance and partial dependence shown together**: "Marginal plots of the top 15 predictor variables… showing the marginal effect of each trait (shown in order of importance)."
- **Predictions converted into a named, countable, falsifiable list**: "Using the 90th percentile as a cutoff, we also identify 58 species predicted to be novel reservoirs and 159 species predicted to be novel hyperreservoirs", supplied in full as Dataset S4.

## Results
> "Our models predict reservoir status in this group with over 90% accuracy, identifying species with high probabilities of harboring undiscovered zoonotic pathogens based on trait profiles."
> "Rodent reservoirs reach sexual maturity and begin producing offspring at higher rates earlier in life compared with nonreservoirs."
> "Predicted hotspots of novel rodent reservoirs occur broadly, spanning arctic, temperate, tropical, and desert biomes… with hotspots occurring in the Middle East and Central Asia (China and Kazakhstan) and the Midwestern United States."

Narrative arc: **accuracy → the biological profile the model discovered → where those species live.** The middle step is what makes it science rather than prediction: the disparate important variables are unified into one interpretable concept — a **fast-paced life history** — instead of being listed.

## Voice
Active, first-person plural, past tense for what was done. Hedging is placed on mechanism, not on performance: "may serve as rules of thumb"; "we note that these results should be considered in light of decelerating species–area curves".

## Discussion and limitations
> "Clearly, the process of disease emergence from wild reservoirs into human hosts is complex, depending on many interacting factors."
Closing posture converts the model's output into a field-work agenda:
> "Moving forward, sorting out which reservoirs pose the greatest risk to humans, identifying the mechanisms leading to observed reservoir hotspots, and understanding the biological underpinnings… will require empirical ground-truthing that depends on detailed field work, experimentation, and continued surveillance."

**A predictive model's proper conclusion is an experiment someone can run.**

## Data, code and funding
Deposited in Dryad (10.5061/dryad.7fh4q), with five supplementary datasets: zoonoses and species list, predictor definitions, model tuning parameters and performance, the novel predictions, and a taxonomy translation table. Code not explicitly released; analysis in R with `gbm`.

## Distinctive moves to borrow
1. **State the train/test split in one sentence, and say it happened before analysis.**
2. **Model your own sampling bias and show it does not explain your signal.**
3. **Unify important variables into one interpretable concept**, don't list them.
4. Disclose a conservative labelling choice and state which way it biases performance.
5. **Ship the predictions as a named list** so the paper can be proved wrong.
6. Report a cutoff and justify it (90th percentile), rather than presenting continuous scores only.
