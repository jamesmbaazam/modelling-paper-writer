# 18 — Bjørnstad, Finkenstädt & Grenfell (2002), *Ecological Monographs*
**"Dynamics of measles epidemics: estimating scaling of transmission rates using a time series SIR model"**
*Ecological Monographs* 72(2):169–184. doi:10.1890/0012-9615(2002)072[0169:DOMEES]2.0.CO;2.

**Archetype:** the *long-form statistical-model-and-estimation* paper — a monograph-length treatment that specifies a stochastic model, estimates every parameter from a large observational dataset, and reports how the estimates scale across the system. The reference implementation of the TSIR model.

## Structure
Full IMRaD at monograph length, with **ecology-journal `Key words`** after the abstract and two appendices: `Abstract` → `Introduction` → `Materials and Methods` (*Natural history and life cycle* — *The parasite* / *The host* · *The data* · *The model* — *A stochastic disease model* / *Estimation*) → `Results` (*Transmission* · *Colonization and immigration*) → `Discussion` (*Mixing, transmission, and R₀* · *Implicit age structure* · *Discrete time modeling*) → `Acknowledgments` → `Literature Cited` → `Appendix A`, `Appendix B`.

Two structural decisions are worth copying:
- **Methods opens with the biology, not the mathematics.** *Natural history and life cycle* runs for two pages on the virus, the host and the schooling calendar before a single symbol appears. Every modelling choice later in the section points back to a fact established here — the 2-week time step to "The characteristic time scale of the transmission dynamics is thus ;2 wk", the seasonal transmission to "Aggregation during school terms therefore induced strong seasonal forcing in the transmission rates."
- **The Discussion is organised by the assumption a critic would attack** — mixing, age structure, discrete time — not by the order of the results. Each subsection states the objection, then answers it.

**The companion-paper split is declared up front and honoured**: "In the companion paper (Grenfell et al. 2002), we show that this simple modeling framework for measles is capable of reproducing highly predictable fluctuations in large populations, and recurring episodic outbreaks in small populations." Say which questions the other paper answers, in the Introduction, and do not creep into them.

## Opening move
The Introduction opens on the ecological problem, not the disease, and only reaches measles in the fourth paragraph:
> "Over the last two decades, infectious diseases have gained increasing recognition as a key component in the dynamics of populations."

It then states the gap as two named challenges, which the paper answers in order:
> "Understanding the range of disease dynamics poses two challenges. First, we need to understand the relative and absolute importance of the regulatory (predator–prey-like interactions) and the stochastic forces (immigration probabilities and environmental and demographic stochasticity). The second challenge is to obtain reliable data, not only for large/dense populations, but also on small/sparse populations, for which data are difficult to obtain."

and justifies the system by how well it meets both:
> "Measles (and other human childhood diseases) provides a unique opportunity for understanding microparasitic dynamics, because it exhibits both endemic and episodic dynamics (Bartlett 1956), and because the data records are very good for both large and small host communities."

**The positioning is a precise statement of what prior work did not cover**, naming the authors it builds on rather than faulting them: "Recently, Ellner et al. (1998) integrated these approaches by developing 'semi-mechanistic' time series modeling of the data. Finkenstädt and Grenfell (2000) extended this to a fully mechanistic time series model. Both these and other statistical approaches to the nonlinear dynamics of measles have focused on the endemic behavior of epidemics in large communities." The contribution is then stated against exactly that boundary: "Here we use a mechanistic model that allows us to explore the balance between noise and determinism across the full range of endemic and episodic measles dynamics."

The Introduction ends with a **roadmap paragraph in the order the paper will follow** — "We first summarize the relevant natural history… We use the model first to understand endemic dynamics… We subsequently scale the model down…".

## Methods
- **Name the model, expand the acronym, and say what it is for**: "we develop a statistical SEIR … model (the TSIR 5 the time series SIR [Susceptible–Infected–Recovered] model) that has a dual role. First, it is a model that can be scaled by population size to produce endemic and episodic dynamics… Second, it provides a mechanistic bridge between theoretical models and empirical data."
- **Justify the time step from biology, not convenience**: "The natural time scale for the disease is ;2 wk. We therefore aggregate the weekly data into 2-wk intervals, and use this as the time step in the model."
- **Position the formulation against the field's default and say why you depart from it**: "In the theoretical literature, deterministic continuous-time, continuous-state-space formulations are the most common… We will, however, extend the discrete-time model of Finkenstädt and Grenfell (2000) to formulate a discrete state-space model that can accommodate small population sizes and disease recolonization."
- **Gloss every parameter by what it represents, and give the value that recovers the textbook case**: the force of infection is "the infection pressure experienced by one susceptible individual"; α "allows for the nonlinearities in contact rates that may arise due to spatial substructuring or other forms of nonhomogenous mixing"; and critically, the paper states that mass action corresponds to α = 1 — a reader can now interpret every later estimate of α without re-deriving anything.
- **Describe a derived quantity as a procedure, with its one assumption stated**: "The susceptible reconstruction is achieved by regressing cumulative births against cumulative case notifications… The only assumption necessary to make for this to work is that the reporting rate is constant through time."
- **Then relax the assumption you just stated**: "Since the 1944–1966 period showed significant changes in public health and socioeconomic patterns, it makes sense to allow for the possibility of smooth changes in reporting rates. We do this by using a locally linear regression of the cumulative–cumulative plot… Cross-validation is used to optimize the bandwidth."
- **Report a method's incidental benefits and its weak points in the same paragraph**: "There is a valuable spinoff of susceptible reconstruction… the slope of the (global or local) cumulative–cumulative regression is a direct reflection of the reporting rate." immediately followed by "Note that susceptible reconstruction will be less reliable in the earliest part of the time series. A corollary to this is that 'initial conditions' are harder to estimate if no allowance is made at the beginning of the series."
- **Describe the data's awkward history rather than smoothing it**: "In 1965 'greater London' was created, with completely new (and much larger) political boundaries. … In consequence, we only consider the London data up until the end of 1964."
- **State the reporting rate as a known imperfection with a number**: "The reporting is not complete during the period of mandatory notification. It is, however, rather good (reporting rate .50% in the prevaccination era…) and the underreporting can be corrected for through the process of susceptible reconstruction."

## Results
**Describe the raw data's regime shift before fitting anything**, so the reader knows what the model must reproduce:
> "The large cities exhibit fairly regular, generally biennial, endemic disease cycles with few or no fadeouts. Cities in the range 50 000 to ;300 000 inhabitants exhibit occasional and brief fadeouts. The smallest communities exhibit long fadeouts and irregular outbreaks."

**Every estimate carries a standard error, a correlation with its p-value, or a range** — and the test statistic is named each time: "The mean case count rises linearly with city size (Pearson correlation 5 0.996, P , 0.01)"; "The proportion of zeros declines exponentially up to a critical community size, after which no zeros are recorded (Spearman rank correlation 5 20.91, P , 0.01)"; "the fraction of susceptibles appears to be constant around 3.2% (SE 5 0.05)".

**Report model fit as a distribution across units, not a single number, and say what the gradient means:**
> "The mean R2 (here measured as 1 2 [residual deviance/null deviance]) for the 60 fitted models is 0.85. The model fit scales directly with population size from Teignmouth (R2 5 0.74) to London (R2 5 0.98). The Spearman rank correlation between the R2 and the population size is 0.92. This indicates that the short-term predictability of the dynamics increases with population size."

The definition of R² in parentheses is the detail that makes the number comparable to anyone else's.

**Report a weak effect as weak, and say so twice**: "There is weak evidence that a decreases with community size (weighted Pearson correlation r 5 0.28, P 5 0.03). However, the change appears to be ecologically unimportant." A significant p-value is explicitly declared ecologically unimportant — the clearest example in the corpus of separating statistical from substantive significance.

**Give the scaling relationship as a fitted equation with bracketed standard errors on each coefficient**, so it can be reused: `log(b̄) 5 3.64[60.39] 2 1.02[60.03] 3 log N`, with "where N is the community size" immediately after.

**Flag a discrepancy with the literature at the moment it arises, and defer it honestly**: "This is a smaller proportion susceptible than is generally estimated for measles in developed countries (Anderson and May 1991). We will return to this discrepancy in the discussion."

**Translate a parameter into an interpretable quantity for the reader who will not read the equations.** The immigration rate becomes waiting times — "For the smallest community (Teignmouth; population 10 000) it is ;0.2 (95% CI 5 0.14, 0.27). In expectation, this yields less than one immigrant event about every 3 mo" — and the spark probability becomes odds: "the odds of sparking off an epidemic is ,1:5 with the low number, and about 1:1 with the high number".

**Explain a wide interval rather than apologising for it:**
> "The confidence intervals are, however, huge for bigger cities; Liverpool (population 764 000), for instance, has an estimated rate of 2.9, that may be as low as 2.0 and as high as 20. The wide confidence intervals in big cities reflect how their dynamic trajectories provide relatively small amounts of information about the immigration process."

**Disclose a threat to a parameter, with the forward reference that contains it**: "important issues remain unresolved with respect to estimating coupling; B. Finkenstädt, O. N. Bjørnstad, and B. T. Grenfell, unpublished manuscript, use detailed statistical simulation to show that the relationship between immigration rate and population size may be spurious. Bias in this parameter, fortunately, does not affect the other estimates (see Appendix B)." The limitation is named, and then bounded.

## Literature
Author–year citations in the ecology convention, and very dense: the Discussion's first sentence carries fourteen references in a single parenthesis. Synthesis paragraphs routinely cite 5–8 sources. Unpublished work is cited by name with its status ("B. Finkenstadt and B. Grenfell, unpublished results"; "K. Glass and B. Grenfell, unpublished manuscript"), which lets the paper lean on results the reader cannot yet check while making that visible.

The field's own claim is weighed rather than asserted: "we would argue that measles provides a less cluttered path between data and mechanistic models than most other systems" — hedged with "we would argue", which is how to make a strong comparative claim honestly.

## Voice
First-person plural, past tense for what was done and present for what holds: "We develop a model", "We fitted the model to data from 60 cities", "The mixing parameter (a) is found to be nearly independent". Two habits stand out:

- **Scare quotes on every term being used in a specific or borrowed sense**, defined on first use: "true mass action", "pseudo mass action", "Type 1 dynamics" sensu Bartlett 1957, the disease "'regulating'" the susceptible population, a "chain of transmission", "initial conditions". There is even a usage note in the Introduction — "(Note, that we use the word 'endemic' according to the epidemiological tradition, which is unrelated to the biogeographic usage)."
- **A light touch where the register allows it**, in a monograph that can afford it: "Our aim in the following will be somewhat more modest than to review the population ecology, demography, and behavioral ecology (sociology) of the host of this particular morbillivirus. We will, instead, give a brief sketch of the important properties of the British people, as seen from the point of view of the single-strand of replicating RNA."

Evidential strength is graded within a single sentence — the abstract's "is found to be invariant … and the mean proportion of susceptible individuals also appears to be constant" marks a firm result and a softer one without a separate hedging clause.

## Discussion and limitations
Opens on the field, not the findings, then states what the paper added and what it deliberately left to the companion paper. The organising claim is a scaling statement: "An overarching finding is that certain parameters scale in a simple fashion across three orders of magnitude of host population sizes. Other parameters/descriptors are fully invariant across the same range."

**A finding is tested against intuition, and the conflict is resolved mechanistically** — the best passage in the paper:
> "Viewed in this context, our results suggest at first glance an 'urban population density' common across small towns and large cities. Generally, this flies in the face of intuition about human diseases, since we would expect a markedly higher density of contacts in large cities… However, for measles, the scaling of b̄ with population size is likely to arise because the effective density of the core group, children in school classes and their epidemiologically coupled preschool sibs, vary much less with urban population size than the overall density of adult contacts. Thus, social organization appears to render the density and size of the core group for disease transmission remarkably invariant."

Each Discussion subsection then takes one modelling assumption and discharges it:
- **Age structure**: the mismatch is stated precisely — "While the school aggregation is an on/off process, the seasonal transition changes more gradually" — a mechanism is proposed, and external support is cited (Earn et al. 2000), which "develop this further to show that age structure can theoretically be collapsed to a simple homogenous-mixing model by making the transmission parameters variable with time", so that "the nonstructured model with transformed transmission coefficients may be thought of as having an implicit age structure."
- **Discrete time**: the objection is attributed to the critic who made it ("Mollison and Din (1993) argued that the characteristic time scale of measles might be somewhat less than 14 d"), then answered with a re-analysis at a different time step, *including the cost of that re-analysis*: "(This inevitably introduces an additional level of sampling error because the output interval [10 d] is not a multiple of the observational interval [7 d]. The results appear to be qualitatively robust to this added error)." The conclusion is quantitative: "we find that most parameter estimates are unaffected. The mixing coefficient, a, is still close to unity (mean 5 0.96, SE 5 0.01)".
- **Time-independent immigration**: "In the model, we assumed time independence of the immigration intensity. This is likely to be overly simplified because the dynamics of measles in England and Wales are highly synchronized between cities… A consequence of time-varying immigration intensities will be that the recolonization process will be more predictable than assumed in our model." The assumption, why it is wrong, **and the direction of the consequence**.
- **An unresolved conflation named as future work**: "'Immigration' of infection to a town may in fact occur by direct movement of nonresident infected individuals or via temporary excursions by local susceptible individuals. In our current model formulation, we treat these as synonymous. Teasing out any differences arising from these two modes of spatial transmission is an important area for future work."

Closes by claiming the contribution at its real size — a first step and a record scale, not a solution:
> "Here, we have developed a mechanistic time-series model that makes a first step towards unifying these approaches. The model captures the short-term (generation step) behavior of our 60 city data set remarkably well. In particular, it allows us to explore, in the largest such analysis to date, the scaling of epidemiological parameters with population size across three orders of magnitude in host population size."

## Data, code and funding
Funders are named with grant numbers in `Acknowledgments`, reviewers are thanked by name ("We thank Ben Bolker, Roger Nisbet, and one anonymous reviewer"), and a **data URL is given in a footnote** to the methods — an early example of pointing readers at the dataset rather than describing it only.

## Distinctive moves to borrow
1. **Open Methods with the natural history**, and make every later modelling choice point back to a fact established there.
2. **Give the parameter value that recovers the standard model** — mass action corresponds to α = 1 — so every estimate is interpretable on sight.
3. **State a method's single assumption, then immediately relax it** and say how.
4. **Report fit as a distribution across units with its definition in parentheses**, and interpret the gradient rather than the mean.
5. **Declare a statistically significant effect ecologically unimportant** when it is. The p-value is not the finding.
6. **Publish the scaling law as an equation with standard errors on every coefficient**, so others can reuse it.
7. **Convert parameters into waiting times and odds** for readers who will not read the equations.
8. **Explain wide intervals by what the data cannot tell you**, rather than apologising.
9. **Organise the Discussion by the assumption a critic would attack**, one subsection each: state the objection, re-analyse, report the cost of the re-analysis, give the quantitative verdict.
10. **Give the direction of the consequence for every simplification** — "the recolonization process will be more predictable than assumed in our model".
11. **Declare the companion paper's scope in the Introduction** and stay out of it.
12. **Scare-quote and define every borrowed or specialised term on first use**, including a note where a word means something different in a neighbouring field.

## Related files
The companion paper's spatial analysis is [17-grenfell-2001-travelling-waves](17-grenfell-2001-travelling-waves.md), whose Box 2 model is this one; the contrasting high-birth-rate regime where these scaling results break down is [02-ferrari-2008-measles-sub-saharan-africa](02-ferrari-2008-measles-sub-saharan-africa.md); the dynamical unification that this paper's age-structure discussion leans on is [04-earn-2000-simple-model-complex-transitions](04-earn-2000-simple-model-complex-transitions.md); the coupling formalism is [06-keeling-rohani-2002-spatial-coupling](06-keeling-rohani-2002-spatial-coupling.md); for a modern Bayesian equivalent of susceptible reconstruction and reporting-rate estimation see [26-abbott-2020-rt-estimation-tool](26-abbott-2020-rt-estimation-tool.md).
