# 03 — Keeling et al. (2001), *Science*
**"Dynamics of the 2001 UK foot and mouth epidemic: stochastic dispersal in a heterogeneous landscape"**
Keeling MJ, Woolhouse MEJ, Shaw DJ, Matthews L, Chase-Topping M, Haydon DT, Cornell SJ, Kappey J, Wilesmith J, Grenfell BT. *Science* 294(5543):813–817. doi:10.1126/science.1065973.

**Archetype:** the *real-time outbreak analysis at farm resolution* — an individual-based stochastic model fitted to a live national epidemic, written to inform control while the epidemic is still running.

## Structure
Science Research Article: one-paragraph abstract → unheaded opening (motivation, data, modelling decision) → **bold run-in topic headings inside the running text** — *Model formulation* · *Heterogeneities in transmission* · *Control strategies* · *Discussion* → References and Notes. There is no Methods section: the model is defined in **note 2 of the reference list**, and everything else is deferred to supplementary material cited as "(10)".

The run-in heading is the Science-family compromise worth knowing: the text reads continuously, but a reader scanning for the control analysis finds *Control strategies* in bold mid-paragraph. Use it where a journal forbids section headings but the paper has four distinct jobs.

## Opening move
> "Foot and mouth disease (FMD) is a highly transmissible viral infection, which can spread very rapidly among livestock. The current major epidemic in the UK has devastated the livestock industry and caused severe economic consequences for the country as a whole. The epidemic has generated a unique data set describing the spatial spread of an infectious disease between fixed nodes, i.e., livestock farms."

Pattern: **the disease → the live crisis → the data as an opportunity.** The third sentence is the move to steal — a national emergency is reframed as "a unique data set", which is what licenses a modelling paper rather than a veterinary one. The paragraph closes on what that buys: "an unusual opportunity to explore the impact of spatial and individual heterogeneities on the course of an epidemic and the importance of these variables for the design of appropriate disease control programs."

The second paragraph then states the modelling decision as a *question*, not a choice already made:
> "A key modeling decision is how to represent the local and regional spatial clustering of FMD cases (Fig. 1A), which precludes the use of standard models based on homogeneously mixed host populations (1)."

## Methods
- **Justify the unit of analysis biologically before choosing it.** "Because of the rapid transmission of the virus between livestock in the same farm, it is reasonable to treat the farm as the individual unit (4, 11–13), classifying each holding as either susceptible, incubating, infectious, or slaughtered." The compartments are named in words, in one clause, with no equations in the main text.
- **Name the two systematic uncertainties, separately from stochastic uncertainty**: "we only have a qualitative grasp of the multifaceted nature of FMD transmission between farms (5–8); key transmission parameters must therefore be derived by fitting the model to the epidemic data. Second, there are biases and various lacunae in the epidemiological and management data used to construct the model (9)."
- **Say why the obvious estimator was not trusted, and what was done instead**: "In principle, the necessary parameters can be estimated from the observed pattern of cases by maximum likelihood. However, we cannot rely only on this, because of spatial and temporal biases in the data (9). We therefore adopt a two-stage approach, generating an initial fit by maximum likelihood, then refining it by least squares fits to regional epidemics (10)."
- **Put the model equation in a numbered note**, with every symbol glossed epidemiologically: note 2 defines the daily infection probability over infectious farms, then explains "The kernel determines how the relative risk of infection changes with the distance between a susceptible and infectious farm; it is vital in determining the role of spatial heterogeneity and the rate of spread of the epidemic."
- **Give the fitted parameters as plain numbers with their units** (note 15): "Susceptibility for cattle is 15.2 and for sheep is 1", "all values are per animal, per day", with the incubation period "5 days" and infection-to-reporting "9 days".
- **Test the heterogeneity by model nesting, and report two criteria with their disagreement**: "fitting a nested series of simpler models omitting the farm-size and species effects (10). We use two criteria for significance: the first, the maximized log likelihood… However, the likelihood is too stringent a test for practical purposes because it measures variations in the spatiotemporal pattern of the epidemic at the farm level. We therefore also used a more heuristic measure: the sums of squares of deviations of observed and expected daily cases by county (10)." Naming the *weakness of your own strongest test* and adding a second one is the credibility move here.
- **State the robustness of the headline mechanism to its own parameterisation**: "Simulations show that the qualitative results presented are not sensitive to the precise shape of the transmission kernel."

## Results
Two features of the data are named before any model output, which sets up what the model has to reproduce:
> "First, there is marked variability in daily case reports— clear spikes and troughs indicate the likely importance of stochasticity in the epidemic dynamics. Second, the epidemic has a very long tail, fluctuating around four cases per day since mid-May."

The tail is then explained mechanistically in the same paragraph — the strongest piece of reasoning in the paper:
> "In a fully mixed system, the tail should decay exponentially fast because there are insufficient susceptibles to maintain the disease (1). However, with spatially localized infection, pockets of susceptibility remain, as well as virgin territory; these can be exploited by sparks of infection from outside the region (or 'smouldering' old infections in some cases) (10) to produce isolated local epidemics."

**Model fit is claimed qualitatively and the failures are stated in the same breath:**
> "There is very good overall agreement between the average of the model replicates and the reported cases (Fig. 1). The observed qualitative pattern of variability is also captured by the simulations—note, though, that we do not include day-to-day environmental stochasticity in the model. The average of our simulations slightly underestimates the epidemic, after the decline in early April."

and the two misfits are each given a candidate cause — "probably due to overreporting of cases (10)"; "probably because of small systematic secular changes in transmission not currently included in the model, such as the mid-May turnout of dairy cattle from winter housing onto pasture." Then the limits of the test itself are conceded: "Although this is not an independent comparison (because the parameters are estimated from the fit), the model's ability to capture the shape, spatial distribution, and variability of the epidemic is encouraging."

**Counterfactual control results are given as percentages of the observed policy**, in a table whose caption defines the baseline precisely ("as a percentage of the results from the full model using the observed control policy"): IP cull only 927% of cases, prompt cull 57%, intensive cull 45%. The headline is stated in plain counts too — "the epidemic would have been much larger, infecting around 20,000 properties (10)".

**A negative result about a popular intervention, with its mechanism:**
> "Even with optimistic assumptions about vaccine efficacy (10) and uptake (90% of farms vaccinated), this results in a much bigger epidemic and total of culled animals than the neighborhood cull (Table 1). Essentially, the delay between the decision to vaccinate and protection from the infection (30) (assumed to be 7 days)—together with the delay from infection to reporting—means that it is very difficult to get 'in front' of the disease and prevent its spread."

Optimistic assumptions plus a negative conclusion, with the delay named as the reason: the argument survives disagreement about the parameters.

**Forecasts are demoted explicitly and given as a distribution, not a date:**
> "Up to 20% of simulations last beyond spring 2002 if control measures are not maintained at a high level, whereas the majority of simulations die out during the autumn if control is pursued vigorously. These predictions are probabilistic and should be interpreted only qualitatively, first because of the simplicity of our model of transmission, and second, because of temporal variation in control effort (10) or environmental parameters."

## Literature
Numbered citations, sparse in the body and dense in the model notes — the *Science* pattern. Prior work is cited to establish agreement rather than to clear ground: "In qualitative agreement with simpler deterministic models (4), our results indicate that…"; "This echoes previous conclusions (4) against the use of vaccination during an epidemic as an alternative to neighborhood culling." Where the paper contradicts earlier work it says so and offers a reason: "This contrasts with conclusions from the 1967–68 foot and mouth epidemic (22), but may be due to the more minor role of aerosol transmission and pigs in the current epidemic (20)."

Note 26 defines the control vocabulary (IP, CP, DC culls) once, in the notes, so the main text can use the abbreviations without a glossary.

## Voice
First-person plural throughout, present tense for the model and past for the epidemic: "We developed", "we find", "we cannot rely only on this", "we believe that this is primarily attributable to the spatial nature of the infection". Hedges carry their reason: "probably because of", "may be attributable to biases in the data (9)", "may be due to the more minor role of aerosol transmission". The one explicit statement of the authors' own bias is worth copying: vaccine performance, "of which we have taken a rather optimistic view in this analysis (31)".

## Discussion and limitations
Opens by naming the registers the results speak to — "a number of important control issues about the epidemiology and control of FMD, as well as more general implications for spatiotemporal disease dynamics" — then gives **the applied result first, as an imperative**:
> "The main applied result is the importance of rapid implementation of properly focused disease control strategies (4, 11–13). If FMD or another highly contagious livestock disease enters a country, then the immediate priority must be to decrease the mixing rate (25)."

Limitations are distributed rather than boxed, and each names what it prevents:
- **Scope fence on the unit of prediction**: "We use the same national average disease dispersal kernel for all farms; we cannot therefore reliably predict the risk for an individual farm, but rather the model identifies areas that are potential 'hot spots' for infection."
- **Named omissions**: "regional variations in farming practices—for example, the spatial separation (35) and dispersion of individual holdings—not explicitly included in our current model"; "we do not include day-to-day environmental stochasticity in the model."
- **A null result reported as a null**: "Preliminary analysis of daily meteorological data and case reports has been unable to detect any clear association."
- **A decision handed back to the reader**: "Ultimately, a decision as to whether or not the epidemiological benefits justify investment in a substantial vaccination program must include a comprehensive economic analysis."

Closes on a numbered research agenda rather than a summary — spatially explicit simulation as "an essential tool", then "First… Second, it is crucial to quantify the spatial infection kernel… Third, we need to understand the essential natural history of infection and the strength of individual heterogeneities in transmission", ending on the operational requirement: "good disease surveillance, rapid diagnosis—with the associated development of new methods—and quick intervention."

## The abstract, verbatim
> "Foot-and-mouth is one of the world's most economically important livestock diseases. We developed an individual farm-based stochastic model of the current UK epidemic. The fine grain of the epidemiological data reveals the infection dynamics at an unusually high spatiotemporal resolution. We show that the spatial distribution, size, and species composition of farms all influence the observed pattern and regional variability of outbreaks. The other key dynamical component is long-tailed stochastic dispersal of infection, combining frequent local movements with occasional long jumps. We assess the history and possible duration of the epidemic, the performance of control strategies, and general implications for disease dynamics in space and time."

Seven sentences, each doing one job — a template worth borrowing as an outline (the structure, not the sentences):

1. **Why anyone should care, in one clause.** "one of the world's most economically important livestock diseases." Importance is asserted in the register the audience uses (economic, not epidemiological).
2. **What was built, with its two defining adjectives.** "an individual farm-based stochastic model" — unit of analysis and stochasticity, both named. Note "of the current UK epidemic": the paper is explicitly about a live event.
3. **Why the data make the analysis possible.** The data resolution is the enabling condition, and "unusually" claims novelty for the dataset rather than for the method.
4. **The first finding, as a list of drivers.**
5. **The second finding, named as a mechanism**, with a plain-English gloss in the same sentence: "long-tailed" is the technical claim, "frequent local movements with occasional long jumps" is what a policymaker remembers.
6. **What is delivered, in three registers** — retrospective, prospective/operational, and general-theoretical. A modelling paper that offers all three is hard to dismiss as either purely academic or purely operational.

Two verbs do careful work: **"assess"** (not "predict") for duration and control performance, and **"possible duration"** — a live-epidemic forecast is framed as a range of possibilities from the first mention.

## Distinctive moves to borrow
1. **Heterogeneity is the finding, not a nuisance parameter.** The title puts "heterogeneous landscape" in it, and the paper quantifies the heterogeneity rather than controlling for it: "the present work quantifies the key role of cattle and the epidemiological importance of large mixed farms in this epidemic."
2. **Explain the feature of the data your model exists to explain.** The long tail is set up as a puzzle, shown to be impossible under mixing, and then resolved by spatial structure.
3. **Describe fat-tailed dispersal in words as well as parameters.** "Frequent local movements with occasional long jumps" does more work than the kernel's exponent.
4. **Report the counterfactual as a percentage of what actually happened**, with the baseline defined in the table caption.
5. **Take the optimistic view of the intervention you are about to reject**, and say that you have.
6. **Demote your own forecast in the sentence that gives it**, and give it as a distribution over outcomes.
7. **Attack your own best test.** Reporting that the likelihood is "too stringent a test for practical purposes" and adding a county-level criterion is more persuasive than either test alone.

## Related files
For the same group's approach to spatial measles dynamics see [17-grenfell-2001-travelling-waves](17-grenfell-2001-travelling-waves.md) and [18-bjornstad-2002-tsir-measles](18-bjornstad-2002-tsir-measles.md); for the spatial-coupling methodology underlying this family of models see [06-keeling-rohani-2002-spatial-coupling](06-keeling-rohani-2002-spatial-coupling.md). For large individual-based policy simulation written up in the same journal family see [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md) and [12-ferguson-2006-mitigating-pandemic](12-ferguson-2006-mitigating-pandemic.md); for a modern real-time analysis with the same demote-the-forecast discipline see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md). Other *real-time transmission analysis* exemplars: see [72-camacho-2015-ebola-sierra-leone-beds](72-camacho-2015-ebola-sierra-leone-beds.md) for district-level transmission estimates turned into beds needed during an outbreak response; [45-thompson-2019-improved-rt-inference](45-thompson-2019-improved-rt-inference.md) for a widely used R_t estimator with two failing assumptions fixed, shipped in the package the field already uses; [16-tian-2020-china-transmission-control](16-tian-2020-china-transmission-control.md) for a natural-experiment evaluation across Chinese cities, with a mechanistic counterfactual, written under emergency time pressure; [19-kucharski-2020-early-dynamics-covid](19-kucharski-2020-early-dynamics-covid.md) for the real-time Bayesian estimate of a time-varying reproduction number, in a clinical journal's structure; [48-zhao-2020-lassa-nigeria](48-zhao-2020-lassa-nigeria.md) for R estimated from public surveillance counts and then regressed on an environmental driver; [70-gunther-2021-nowcasting-bavaria](70-gunther-2021-nowcasting-bavaria.md) for an operational nowcast whose corrected onsets feed a reproduction-number estimate, evaluated against later data.
