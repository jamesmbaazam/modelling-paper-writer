# 41 — Pawelek et al. (2012), *PLoS Computational Biology*
**"Modeling within-host dynamics of influenza virus infection including immune responses"**
Pawelek KA, Huynh GT, Quinlivan M, Cullinane A, Rong L, Perelson AS. *PLoS Comput Biol* 8(6):e1002588. doi:10.1371/journal.pcbi.1002588.

**Archetype:** the *within-host dynamics* paper — fit a system of ODEs for virus, target cells and immune effectors to serial measurements from infected hosts, and argue that a feature of the observed curve requires a particular mechanism. The unit of analysis is the individual host, not the population, but every convention in `SKILL.md` §2 and §3 still applies.

## Structure
PLoS Comput Biol: `Abstract` → **`Author Summary`** → `Introduction` → **`Results`** (model development *and* fitting — the model is derived here, not in Methods) → `Discussion` → `Materials and Methods` (*Experimental data*, fitting procedure) → `Supporting Information`.

**Note the unusual placement: the model is built in Results.** For a paper whose contribution *is* the model structure, deriving it in Results — term by term, each with its biological warrant — keeps the derivation next to the fits that justify it. `Materials and Methods` then carries only the experimental data and the fitting procedure. This is a defensible inversion when the modelling choice is the finding; it would be wrong when the model is a tool.

## Opening move
> "Despite vaccines and antiviral agents, influenza A virus infection remains a major public health problem worldwide. Seasonal and pandemic influenza results in approximately 3 to 5 million cases of severe illness and approximately 250,000 to 500,000 deaths worldwide."

Burden first, even in a within-host paper, because the mechanism has to matter to someone. The Introduction then teaches the immunology a modelling reader may not have — innate response, type I interferon, NK cells, the adaptive response and its timing ("in mice takes approximately 5 days to begin in the lung") — so that every model term later has a named biological referent.

**The gap is built by walking through prior models and saying what each established**, then naming precisely what is left:
> "By fitting a simple viral dynamic model to the data derived from 6 experimentally infected human volunteers, Baccam et al. showed that target cell limitation can explain the kinetics of influenza A virus infection in humans… **The relative contributions of target cell availability and immune responses to viral control remain unclear.**"

**Then an empirical result is used to motivate the new model**, which is the strongest form of motivation available:
> "Saenz et al. estimated the numbers of viral-antigen-positive cells in the lungs of ponies… The result indicated that up to 5% of bronchiole cells were infected at any one time, yielding an estimated total cell loss of about 27% by the end of the infection. This suggests mechanisms for viral control in addition to target cell depletion, and motivates the development of a model that includes a strong innate immune response to explain the clearance of virus during infection."

If only 27% of cells are lost, target-cell depletion cannot be what stops the infection. **A measurement that falsifies the incumbent model is better motivation than a gap in the literature.**

## Methods
- **Describe the experiment in the units the assay produced, with its schedule**: "Nasal secretions (NS) were collected daily for 10 days post-challenge and number of copies of influenza virus RNA per milliliter (ml) was quantified. Blood samples were also collected to quantify the fold changes in cytokine expression including IFN for days 1 through 5 post-challenge compared to the day prior to challenge."
- **Describe the shape of the data before the model**, naming every feature the model will have to reproduce: the peak at day 2, the wide variation in peak level, "a rapid and substantial decline (about 2 to 4 logs within 1 day)", then "All the ponies had a viral plateau and some experienced a minor but obvious second peak", then a second decline from day 6. The paper's whole argument is organised around these four features.
- **Justify each model term by the biology it stands for, and say what it omits**:
  > "Here, we assume the number of activated NK cells is proportional to the level of IFN and use the mass action term to represent the killing by NK cells. Note that killing by NK cells is an important, but not the only factor leading to the loss of infected cells. Cytokines or proteins released by other cells such as macrophages during the innate immune response can also promote increased lung epithelial apoptosis following influenza virus infection."
- **Justify a neglected term numerically rather than by convention**: "As in the previous models by Baccam et al. and Saenz et al., loss of virions due to infection has been neglected. Since an infected cell may produce as many as 20,000 virions, the loss of one virion to produce an infected cell can be neglected." The approximation is given its order of magnitude.
- **Report the detection limit and how values below it were handled** — essential for log-scale viral load data: "The horizontal dashed blue line represents the detection limit of the viral titer, i.e., 100 RNA copies per ml of nasal secretions. Data below the detection limit were plotted as 1 RNA copy per ml of nasal secretions."
- **Supply a schematic and a parameter table**: "A schematic diagram of Eq. (1) is shown in Figure 1. Variables and parameters are summarized in Table 1", with units and initial values per symbol.

## Results
**Fit per individual, not only to the average, and report both**: "We fit the predicted values of V(t) and F(t) in Eq. (1) to the viral load and IFN (fold change) kinetic data, respectively, of each pony… We also fit the model to the average data of the 6 ponies."

**Explain parameter uncertainty by the data rather than apologising for it:**
> "Note that the estimates of some parameters, such as the infection rate β and the viral production rate p, have large variations. This is expected because there is a large variation (up to 4 logs) in the peak viral load of the 6 ponies."

**Compare nested models by an information criterion and report the verdict per subject**: "Akaike Information Criterion (AICc)… Model 1 is supported over model 2 for each pony." The alternative model is defined by setting one parameter to zero — "Model 2 is Eq. (1) with κ = 0, i.e., no killing of infected cells by NK cells" — so the comparison isolates exactly the mechanism in question.

**Refuse a comparison that would not be valid, and say why** — a rare and valuable move:
> "We did not statistically compare the fits of model 1 with the Saenz et al. fits because the objective functions minimized during data fitting are different. Saenz et al. incorporated the percentage of infected cells in their fitting. We did not include this because the data of the percentage of infected cells were from a different study."

The informal comparison is then reported as what it is: "The errors listed in Table 3 and the fitted curves show that our fits improve those using the Saenz et al. model."

**Argue from what competing models *cannot* produce** — the paper's central argument, and the reason the odd features of the data were catalogued up front:
> "The target cell limited model and the Saenz et al. model cannot generate bimodal virus titer peaks. Adding the effect of IFN and a time delay in its production into the target cell limited model was shown to be able to generate bimodal peaks. However, the fits obtained by Baccam et al. using this model did not agree well with the data. Our fits using model 1 generated an obvious bimodal behavior."

**Then tie the reproduced feature to a measured covariate**: "The level of IFN peaked around day 2 and then declined rapidly, concordant with the emergence of viral plateau/second peak." The mechanism is not merely sufficient in simulation; its driver was measured in the same animals.

## Literature
Numbered PLoS citations, dense in the Introduction and Discussion, where independent evidence for the model's assumptions is assembled from other systems: NK depletion studies in mice, severe human H1N1 cases "associated with reduction of NK cells rather than effector CD8+ T cells", vaccination raising activated NK levels, and a knockout experiment — "Gazit et al. showed that influenza virus infection was lethal in mice when the NK receptor NCR1 was knocked out."

**Assemble external evidence for a modelled mechanism from experiments you did not do.** A within-host model term is a biological claim, and the Discussion is where it is defended with other people's experiments.

## Voice
First-person plural, past for the work and present for the model's behaviour. Assumptions are flagged with "we assume" at the point of use, and their limits immediately after. Claims are scaled to the design: the model "can explain" the rapid decline, an immune response "is needed in our model" — the qualifier *in our model* appearing wherever the claim is about model necessity rather than biological necessity.

## Discussion and limitations
Opens by stating what the new model adds against the specific mechanism it introduces, then defends that mechanism with external evidence (above), then qualifies the assumption that carried it: "In our model, we assumed that the level of activated NK cells is proportional to that of IFN, whose levels were measured in the study. There is evidence supporting that NK cells have similar dynamics to IFN and virus during influenza virus infection."

The closing paragraph maps each observed feature to the mechanism the model says produced it — the cleanest possible summary for a within-host paper:
> "by fitting mathematical models to the viral load and IFN data we illustrate that both the innate and adaptive immune responses are needed to explain the viral load change during influenza virus infection. The first post-peak viral decline (about 2 to 4 logs within 1 day) can be explained by the lysis of infected epithelial cells, mediated by cytokines and cells such as NK cells, during the innate immune response. The subsequent viral plateau/second peak is generated in our model by the loss of the IFN-induced antiviral effect and the increased availability of target cells as cells lose their antiviral state. An adaptive immune response is needed in our model to explain the eventual viral clearance."

Sensitivity analyses are supplied as supporting figures, varying one parameter at a time with the rest fixed, and the alternative model specifications are plotted against the same data.

Closes on the translational reason the mechanism matters: "A detailed and quantitative study of the within-host dynamics of virus, cells, and cytokines may provide more information for future research in influenza pathogenesis, treatment, and vaccination."

## Distinctive moves to borrow
1. **Catalogue the features of the data before the model**, then organise the argument around reproducing each one.
2. **Motivate a new model with a measurement that falsifies the incumbent** — only 27% of cells lost, so target-cell depletion cannot explain clearance.
3. **Build the model in Results, term by term with its biological warrant**, when the model structure is the contribution.
4. **Define the null model by setting one parameter to zero**, so model comparison isolates the mechanism in dispute, and report the criterion per subject.
5. **Argue from what rival models cannot produce**, not only from your own goodness of fit.
6. **Tie a reproduced feature to a measured covariate** so the mechanism is not merely sufficient in simulation.
7. **Refuse an invalid comparison and explain why** the objective functions differ — then report the informal comparison as informal.
8. **Justify a neglected term with its order of magnitude** (one virion against 20,000 produced).
9. **Explain wide parameter estimates by the variation in the data**, naming the range.
10. **Report the assay's detection limit and how censored values were plotted.**
11. **Say "in our model" wherever the claim is about model necessity**, not biological necessity.
12. **Defend each modelled mechanism with other people's experiments** in the Discussion.

## Related files
For the population-level counterpart where infectiousness profiles matter see [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md) and [07-lauer-2020-incubation-period](07-lauer-2020-incubation-period.md); for fitting a mechanistic model to time series with explicit model comparison see [24-davies-2021-b117-transmissibility](24-davies-2021-b117-transmissibility.md) and [18-bjornstad-2002-tsir-measles](18-bjornstad-2002-tsir-measles.md); for identifiability limits in mechanistic fitting see [21-weitz-2015-post-death-transmission-ebola](21-weitz-2015-post-death-transmission-ebola.md). Other *within-host dynamics* exemplars: see [67-clapham-2014-dengue-within-host](67-clapham-2014-dengue-within-host.md) for a within-host model used to test antibody-dependent enhancement; [66-neant-2021-sars-cov-2-viral-kinetics](66-neant-2021-sars-cov-2-viral-kinetics.md) for viral kinetics joined to a survival endpoint, so the kinetic parameter predicts death.
