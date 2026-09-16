# 18 — Bjørnstad, Finkenstädt & Grenfell (2002), *Ecological Monographs*
**"Dynamics of measles epidemics: estimating scaling of transmission rates using a time series SIR model"**
*Ecol Monogr* 72(2):169–184. doi:10.1890/0012-9615(2002)072[0169:DOMEES]2.0.CO;2

> **Basis of this analysis.** The full text is paywalled with no open-access copy (checked via PMC, Europe PMC, Unpaywall, OpenAlex and Semantic Scholar, September 2026). This file is built on the **verbatim abstract** and the bibliographic record. *Ecological Monographs* abstracts are long and structured, so the abstract carries an unusual amount of the paper's method and results.

**Archetype:** the *long-form statistical-model-and-estimation* paper — a monograph-length treatment that specifies a stochastic model, estimates every parameter from a large observational dataset, and reports how the estimates scale across the system. The reference implementation of the TSIR model.

## The abstract, verbatim
> "Before the development of mass-vaccination campaigns, measles exhibited persistent fluctuations (endemic dynamics) in large British cities, and recurrent outbreaks (episodic dynamics) in smaller communities. The critical community size separating the two regimes was ∼300 000–500 000. We develop a model, the TSIR (Time-series Susceptible–Infected–Recovered) model, that can capture both endemic cycles and episodic outbreaks in measles. The model includes the stochasticity inherent in the disease transmission (giving rise to a negative binomial conditional distribution) and random immigration. It is thus a doubly stochastic model for disease dynamics. It further includes seasonality in the transmission rates. All parameters of the model are estimated on the basis of time series data on reported cases and reconstructed susceptible numbers from a set of cities in England and Wales in the prevaccination era (1944–1966). The 60 cities analyzed span a size range from London (3.3 × 10⁶ inhabitants) to Teignmouth (10 500 inhabitants). The dynamics of all cities fit the model well. Transmission rates scale with community size, as expected from dynamics adhering closely to frequency dependent transmission ('true mass action'). These rates are further found to reveal strong seasonal variation, corresponding to high transmission during school terms and lower transmission during the school holidays. The basic reproductive ratio, R₀, is found to be invariant across the observed range of host community size, and the mean proportion of susceptible individuals also appears to be constant. Through the epidemic cycle, the susceptible population is kept within a 3% interval. The disease is, thus, efficient in 'regulating' the susceptible population—even in small cities that undergo recurrent epidemics with frequent extinction of the disease agent. Recolonization is highly sensitive to the random immigration process. The initial phase of the epidemic is also stochastic (due to demographic stochasticity and random immigration). However, the epidemic is nearly 'deterministic' through most of the growth and decline phase."

## What the abstract teaches
This abstract is effectively a miniature paper, and its ordering is the ordering a long methods paper should use:

**Phenomenon (2 sentences).** The two dynamical regimes are named and given technical labels in parentheses — "persistent fluctuations (endemic dynamics)" / "recurrent outbreaks (episodic dynamics)" — and the quantity that separates them is given with its value: "The critical community size separating the two regimes was ∼300 000–500 000."

**Model, built up one component per sentence (4 sentences).** Each sentence adds one feature and names the consequence of adding it:
- what it must do: "can capture both endemic cycles and episodic outbreaks";
- the first source of stochasticity, with its distributional consequence stated in parentheses: "the stochasticity inherent in the disease transmission (giving rise to a negative binomial conditional distribution)";
- the second: "and random immigration";
- the label that summarises both: "It is thus a doubly stochastic model for disease dynamics";
- the last ingredient: "It further includes seasonality in the transmission rates."
**Naming the model's class in one word ("doubly stochastic") after building it up is a very efficient move** — it gives the reader a handle for everything that came before.

**Data and estimation (3 sentences).** The scope of estimation is claimed explicitly — "*All* parameters of the model are estimated on the basis of time series data" — and the latent state is named as reconstructed rather than observed ("reconstructed susceptible numbers"). The dataset is then bounded by its extremes: "The 60 cities analyzed span a size range from London (3.3 × 10⁶ inhabitants) to Teignmouth (10 500 inhabitants)." Giving the largest and smallest unit by name is more informative than a mean.

**Results, ordered from fit to scaling to invariance (6 sentences).**
- Fit first, in four words: "The dynamics of all cities fit the model well."
- The scaling result, with its theoretical interpretation attached in the same sentence: "Transmission rates scale with community size, as expected from dynamics adhering closely to frequency dependent transmission ('true mass action')."
- The seasonal result, with its mechanistic reading: "strong seasonal variation, corresponding to high transmission during school terms and lower transmission during the school holidays."
- **The invariance results — the paper's most cited findings — stated as invariances**: "The basic reproductive ratio, R₀, is found to be invariant across the observed range of host community size, and the mean proportion of susceptible individuals also appears to be constant." Note the graded confidence within one sentence: "is found to be invariant" for the stronger result, "also appears to be constant" for the weaker.
- The quantitative version of the invariance: "the susceptible population is kept within a 3% interval."
- The interpretation, with the concessive that makes it surprising: "The disease is, thus, efficient in 'regulating' the susceptible population—even in small cities that undergo recurrent epidemics with frequent extinction of the disease agent."

**Where stochasticity matters (3 sentences).** The abstract closes by partitioning the epidemic into phases and saying which parts are stochastic and which are effectively deterministic: "Recolonization is highly sensitive to the random immigration process. The initial phase of the epidemic is also stochastic… However, the epidemic is nearly 'deterministic' through most of the growth and decline phase." This is a genuinely useful modelling conclusion — it tells the next modeller where they can afford a deterministic approximation.

## Framing conventions to take from this paper
- **Build the model one sentence per component, and name the class at the end.**
- **State how much of the model is estimated** ("All parameters…") and which quantities are reconstructed rather than observed.
- **Report invariances as findings.** A parameter that does *not* vary across a two-orders-of-magnitude size range is a stronger result than one that does.
- **Grade your verbs within a sentence** ("is found to be" vs "also appears to be") to signal differing evidential strength without a separate hedging clause.
- **Say where stochasticity matters and where it does not.** Partitioning the epidemic into stochastic and near-deterministic phases is directly actionable for anyone building on the model.
- Quotation marks used to flag terms being used in a technical or slightly figurative sense: 'true mass action', 'regulating', 'deterministic'.

## Related files
The TSIR model is applied in [02-ferrari-2008-measles-sub-saharan-africa](02-ferrari-2008-measles-sub-saharan-africa.md); the same dataset yields the spatial results in [17-grenfell-2001-travelling-waves](17-grenfell-2001-travelling-waves.md); the dynamical regimes it fits are the subject of [04-earn-2000-simple-model-complex-transitions](04-earn-2000-simple-model-complex-transitions.md).
