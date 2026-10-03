# 17 — Grenfell, Bjørnstad & Kappey (2001), *Nature*
**"Travelling waves and spatial hierarchies in measles epidemics"**
*Nature* 414(6865):716–723. doi:10.1038/414716a.

**Archetype:** the *pattern-detection-plus-mechanism* paper — find a spatio-temporal pattern in an exceptional dataset using a method that respects the data's non-stationarity, then reproduce the pattern with a mechanistic model and say what the pattern requires about population structure.

## Structure
Nature Article: one-paragraph abstract → unheaded introduction → **named section headings that are claims or objects, not IMRaD labels** — *Local measles dynamics* · *Travelling waves and wavelet phase angles* · *A 'forced forest fire' model for measles waves* → unheaded discussion → **Methods at the end** → two **Boxes** carrying the technical load.

The two boxes are the structural move worth stealing:
- **Box 1, *Wavelet time series analysis*** — a tutorial on the method for readers who do not have it, written so the main text never has to stop and explain. It ends with the method's own limitations.
- **Box 2, *Making waves*** — the mechanistic model, its two equations, its parameters, and the three simulation scenarios. The main text states what the model shows; the box says how it was built.

**Put the method tutorial and the model in boxes when the main argument is empirical.** The reader following the pattern never leaves the thread, and the reader who wants to rebuild the model has everything in one place.

## Opening move
> "Spatio-temporal travelling waves are striking manifestations of predator–prey and host–parasite dynamics. However, few systems are well enough documented both to detect repeated waves and to explain their interaction with spatio-temporal variations in population structure and demography."

Pattern: **the phenomenon is famous → almost nobody has the data to study it properly → we do.** The gap is about *evidence*, not about ignorance, and it is checkable.

The introduction then narrows in three steps, each naming the obstacle it clears: empirical observations of waves "are comparatively rare—especially repeated periodic waves"; detection fails "because of a lack of spatio-temporal data at the appropriate resolution"; and more subtly, "spatial heterogeneities in population density or demography and temporal changes in parameters … can significantly alter the detection and dynamics of spatio-temporal waves." The data are then introduced as the thing that clears all three: childhood infections "provide sufficiently detailed spatio-temporal data on disease incidence and host demography to address these issues."

**The methodological problem is stated as a property of the data, before the method is named:**
> "The detection of temporal and spatio-temporal oscillations in time series is greatly complicated by non-stationary temporal variations in dynamical behaviour (such as changes in mean, variance, period of oscillations, and so on). In particular, trends or sudden jumps in cycle period complicate the search for temporal and spatial patterns, since conventional frequency-domain analyses assume stationarity."

Only then: "We apply wavelet time series analysis to describe the non-stationarity…". The method is earned by the assumption it relaxes, which is the most persuasive way to introduce one.

## Methods
- **Describe the data to the resolution that matters, with the awkward bit included**: "For the pre-vaccination era, before 1966, weekly measles case data are available for 945 cities and towns and 457 rural districts… In 1974, boundary changes agglomerated the spatial data into 354 administrative areas. To achieve consistent time series across both pre-vaccination and vaccine era, we have therefore binned the pre-vaccination data into the post-1974 boundaries." The administrative-boundary problem is disclosed, with the fix and what each analysis uses.
- **Explain what the method buys over the standard one, in one sentence**: "By contrast, the essence of the wavelet approach is locality in time as well as frequency." And for the phase analysis: "This contrasts with standard multivariate spectral analysis, which can capture phase relationships at different periods, but does not allow a description of how they change with time."
- **Say which parameters were estimated and which were chosen** — the single most important sentence in Box 2: "We stress that, whereas spatial coupling rates have been chosen somewhat arbitrarily and for illustrative purposes, all other parameters are estimated from data."
- **Give the arbitrary choices their actual numbers anyway** (Methods: α = 0.97, the 26 biweekly transmission values, "The biweekly birth rate, B, is set at 100 for small population units and 2,000 for large ones"), so the simulation is reproducible even where it is illustrative.
- **Simplify explicitly and say what the simplification costs**: "we assume that the population size is the same at all locations—this is not critical, but it makes interpretation easier."
- **Put the method's limitations inside the method box**: "like many 'local' statistical methods, they need a lot of data—features can be detected only at a given time and frequency if the underlying process is sufficiently well sampled. It is also important to try a variety of wavelet functions. A number of continuous and discrete functions can capture the basic patterns shown here; however, the Morlet function gives the clearest picture."

## Results
**Build from one well-understood case to the national picture.** London alone (Fig. 1), then two cities whose disagreement is the clearest possible demonstration of the method — "The phase analysis is well illustrated by the pre-vaccination records for Norwich and Cambridge, because epidemics in these relatively close cities (90 km apart) were out of phase during the 1950s" — then all 954 locations. A reader who understands the Norwich–Cambridge figure understands the whole paper.

**State the prediction the pattern must satisfy before showing the pattern:**
> "For instance, phase-locked fluctuations … should result in zero phase-difference across the map, whereas travelling waves should generate a phase difference that increases with distance."

This is the move that converts a map into a test.

**Numbers carry their uncertainty and their units**: the wave is "particularly well defined up to 30 km from London (Fig. 3c) with a wave speed of around 5 km per week"; "Most, though not all, places lag behind London (88% have negative phase difference)"; the correlation of phase difference with distance is "r = −0.59, 99% bootstrap limits: −0.75 to −0.39"; coherence "dropped to around 75 km during the 1970s" and "only significant to 35 km" later.

**Separate two metrics that could be conflated, and say what the difference means:**
> "Phase coherence effectively measures the relative timing of epidemics. A complementary approach is to consider the synchrony of the epidemic time series … which also reflects how their relative amplitudes covary… However, the synchrony of epidemics is significantly less than their phase coherence, especially in the vaccine era. This indicates that vaccination induces stronger variations in the amplitude of epidemics than in their relative phase."

**Mark speculation as speculation, and keep it short**: "We speculate that this may arise from the unusual annual dynamics of Liverpool (which are due to high local birth rates), effectively 'subsidizing' the growth of the epidemic in Manchester and Leeds"; "Such regional heterogeneities are likely to be an interesting line of inquiry in future work."

**Caveat a result at its weakest point rather than in a limitations section**: "the subsequent increase to 4 years in the late 1980s and 90s should be interpreted cautiously, since it may reflect the secular decline at the end of the time series, caused by the major increase in vaccination uptake over this period."

**Refute the obvious alternative explanation where it arises:**
> "Wave-like spatio-temporal behaviour might also result if there were a hierarchical trend of reduced infection rate as we move from large cities to smaller centres. However, in practice, the basic reproductive ratio of measles infection, R₀, was relatively constant across the towns and cities of England and Wales, contradicting this alternative explanation."

## The three-step argument worth copying wholesale
The spine of the second half is a **conceptual model → numbered hypotheses → simulation answering them in the same order**:

1. A conceptual model given as three numbered mechanistic steps — susceptible build-up; the large town where "measles is endemic throughout the inter-epidemic trough, so that a new epidemic occurs as soon as the effective reproductive ratio of infection exceeds unity"; and "By contrast, in the small town, infection goes extinct locally after an epidemic; therefore, another epidemic cannot happen until an infective 'spark' is received, generally originating in a larger (endemic) community."
2. "This reasoning prompts the following hypotheses:" — three numbered, falsifiable predictions, including the corollary that coupling large centres "should generate highly synchronized epidemics" and that distant centres "should have a stronger tendency than nearer towns to move onto the 'opposite' biennial attractor."
3. "We tested these conjectures using a mechanistic model… The model generates a picture in tight agreement with our conceptual scenario. **First**… **Second**… **Third**…" — answered in the order they were posed.

The payoff is a one-sentence reinterpretation of the phenomenon: **"Thus, the observed travelling waves are best seen as repeated and very fast invasion waves, extending from endemic core areas into epidemic satellite regions."**

## Literature
Numbered superscript citations, dense and clustered in the *Nature* manner — "Travelling waves, arising essentially from activator–inhibitor dynamics¹⁻³, are predicted by theory in a range of host–natural enemy systems¹,⁴⁻⁸" carries five references in one clause. Prior work is used to set up the contradiction the paper resolves: "Previous theory indicates that seasonally driven epidemics will either be completely synchronized across large coupled centres or more irregular in small centres buffeted by demographic noise. **This prediction is at odds with the observed waves.**"

Earlier findings are credited rather than displaced: "Theory predicts, and previous time-series analyses have confirmed, that vaccination should generate an increase in the epidemic period. Here we use the temporal dimension of the wavelet analysis to reveal the progressive nature of this increase." The contribution claimed is *resolution*, not discovery — the same move as "Previous studies have documented reductions in synchrony of measles epidemics as a result of vaccination. The present analysis reveals the detailed architecture of the change."

## Voice
First-person plural and present tense for what the paper does ("Here, we demonstrate", "We apply", "We focus first", "We observe from Fig. 2"), past for the historical system. Hedges are graded and attached to specific claims: "possibly crudely reflects", "may reflect", "We speculate that", "This is preliminary evidence that". Coinages are introduced in scare quotes and then used freely — 'sparks', 'core', 'satellite', 'baby booms', 'forced forest fire', the 'opposite' biennial attractor — which is how a paper's vocabulary ends up in everyone else's citations.

## Discussion and limitations
Opens by naming what makes the system exceptional rather than by restating results: the "measles dynamical 'clockwork' and the intricacy of the human demographic record allow us this unusual opportunity to quantify the impact of spatio-temporal heterogeneities on epidemic dynamics."

Limitations appear as the agenda for the next paper, each a named mechanism rather than a general caveat:
> "Of course, towns are not connected only locally in terms of the movement of infection: an important area for future work is to consider how long-range 'jumps' of infection obscure local waves and move the system closer to mean-field behaviour. We shall also consider how regional spatial structure interacts with population size and birth rate to influence the hierarchical pattern of waves."

The methodological contribution is then generalised beyond the disease — "Spatial and temporal non-stationarity is the norm in ecology" — and the paper closes on the structural claim its title implies: the spatial hierarchy of host population structure is a *prerequisite* for these waves, not merely compatible with them.

## The abstract, verbatim
> "Spatio-temporal travelling waves are striking manifestations of predator–prey and host–parasite dynamics. However, few systems are well enough documented both to detect repeated waves and to explain their interaction with spatio-temporal variations in population structure and demography. Here, we demonstrate recurrent epidemic travelling waves in an exhaustive spatio-temporal data set for measles in England and Wales. We use wavelet phase analysis, which allows for dynamical non-stationarity—a complication in interpreting spatio-temporal patterns in these and many other ecological time series. In the pre-vaccination era, conspicuous hierarchical waves of infection moved regionally from large cities to small towns; the introduction of measles vaccination restricted but did not eliminate this hierarchical contagion. A mechanistic stochastic model suggests a dynamical explanation for the waves—spread via infective 'sparks' from large 'core' cities to smaller 'satellite' towns. Thus, the spatial hierarchy of host population structure is a prerequisite for these infection waves."

Note how much work the last two sentences do: a mechanism in a dash-clause with the vocabulary the field adopted, then "Thus," and a claim about what the system *requires*.

## Distinctive moves to borrow
1. **Justify a method by the assumption it relaxes.** "which allows for dynamical non-stationarity" earns more trust than any amount of description, and the assumption it relaxes is stated as a property of the data first.
2. **Turn the map into a test.** Say what each competing hypothesis predicts for the statistic before you show it.
3. **Numbered conceptual model → numbered hypotheses → results answering them in order.** The cleanest way to keep a mechanistic argument auditable.
4. **Refute the leading alternative explanation with an independent fact** (R₀ constant across town sizes), in the paragraph where a sceptic would raise it.
5. **Lead with the two cases that disagree.** Norwich and Cambridge, 90 km apart and out of phase, do more to demonstrate the method than the national map.
6. **Put the method tutorial and the model in boxes** so the main text can stay on the argument.
7. **State which parameters are estimated and which are illustrative**, in one sentence, inside the model description.
8. **Use a policy change as a natural experiment on dynamics**, and report the effect as partial where it is partial — vaccination "restricted but did not eliminate this hierarchical contagion".
9. **Coin a small vocabulary and mark it** ('sparks', 'core', 'satellite'). Two or three quoted terms, defined once, will carry the paper into other people's citations.
10. **Escalate the final sentence to a structural claim** about what the system requires, not just what it does.

## Related files
The same team's dataset and modelling framework appear in [18-bjornstad-2002-tsir-measles](18-bjornstad-2002-tsir-measles.md), which is the TSIR reference implementation this paper's Box 2 builds on; the contrasting high-birth-rate, weakly coupled regime is [02-ferrari-2008-measles-sub-saharan-africa](02-ferrari-2008-measles-sub-saharan-africa.md); the coupling formalism is [06-keeling-rohani-2002-spatial-coupling](06-keeling-rohani-2002-spatial-coupling.md); the unifying dynamical account is [04-earn-2000-simple-model-complex-transitions](04-earn-2000-simple-model-complex-transitions.md); for the same group writing a live spatial epidemic see [03-keeling-2001-uk-foot-and-mouth](03-keeling-2001-uk-foot-and-mouth.md).
