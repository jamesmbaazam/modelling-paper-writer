# 76 — Famulare et al. (2018), *PLoS Biology*
**"Assessing the stability of polio eradication after the withdrawal of oral polio vaccine"**
Famulare M, Selinger C, McCarthy KA, Eckhoff PA, Chabot-Couture G. *PLoS Biol* 16(4):e2002468. doi:10.1371/journal.pbio.2002468.

**Archetype:** *feasibility / threshold* — a multi-scale model, built from vaccine-trial shedding data and three field transmission studies, used to sort settings into those where a strategy is stable and those where it is not. The output is a threshold statistic, a local reproduction number, and three categories of setting defined by where it crosses one. The paper's answer to its own question is *it depends on sanitation and contact*, and it says exactly how.

## Structure
PLoS Biology: `Abstract` → `Author summary` → `Introduction` → `Methods` (*Overview* · *Within-host model*: shedding duration, concentration, oral susceptibility, waning · *Transmission model*: person-to-person, local reproduction number, calibration, additional assumptions) → `Results` → `Discussion` → supporting text and code.

**Methods come before Results and are long**, because the paper's evidence is the synthesis itself: each within-host component is fitted to digitised trial data, plotted against that data, and summarised in a list of observations before the next component is built on it.

## Opening move
The abstract poses the paper's two questions as questions:
> "If poliovirus is reintroduced after OPV cessation, under what conditions will OPV vaccination be required to interrupt transmission? Can conditions exist in which OPV and WPV reintroduction present similar risks of transmission?"

**State the question in the abstract in the form the answer will take** — *under what conditions* — so the reader expects a classification, not a number.

The Introduction sets up the paradox at the centre of the programme in two sentences:
> "Unique among current human vaccines, the live-attenuated Sabin poliovirus strains in OPV are transmissible. This transmissibility provides additional passive immunization that enhances the effectiveness of OPV for generating herd immunity. However, the attenuation of Sabin OPV is unstable and so it can, in rare instances, cause paralytic poliomyelitis and lead to outbreaks of circulating vaccine-derived poliovirus (cVDPV) with virulence and transmissibility comparable to that of WPV strains."

**The paper is positioned against earlier models by its direction of inference**:
> "In short, our model takes a bottom-up approach to modeling poliovirus transmission that complements existing work. Instead of drawing inferences about the unobserved conditions that affect transmission from observed outbreaks, we draw inferences about unobserved properties of possible outbreaks from observed conditions that directly affect transmission."

**Distinguish your approach from prior models by what it infers from what**, not by technique. The sentence makes clear why this model can say something about outbreaks that have not happened.

## Methods
- **Number the simplifying assumptions and say what the Results will do with them**: the oral–oral route is omitted, viral evolution is ignored, transmission is restricted to children's household and close contacts, and paralysis is not modelled — "In the Results, we explore how the limitations of a model with these assumptions are informative about the roles of transmission route, viral evolution, and contact structure in various settings."
- **Define a latent quantity operationally and say what it is not**: the "OPV-equivalent antibody titer" is inferred from shedding, and "This model is agnostic about the biophysical mechanisms of immunity that prevent fecal shedding and is not intended to represent immunoglobulin A concentration or other direct correlates of mucosal immunity."
- **Admit the limits of digitised data**: "In many cases, the data were digitized from published figures that do not report variation in the number of samples for each time point, and so our sample sizes at each time point are often approximate." And: "Because individual-level data were not available, we could not construct proper Kaplan-Meier estimates".
- **Fix what the data cannot separate, and say so**: "The interaction rate and fecal–oral dose parameters are not separately identifiable from the available data, and so we fixed the index-to-household-member interaction rate to once per day".
- **Choose calibration studies for their reporting, and say why a comprehensive review was not used**: the 18 transmission studies in a previous review "exhibit varying thoroughness in their reporting of pre-exposure immunity and contact relationships. In lieu of a comprehensive review, we based our transmission model on specific studies capable of identifying important model parameters."
- **Give each parameter biophysical meaning**: "each parameter has biophysical meaning and can in principle be measured directly in the absence of live poliovirus" — which is what lets the model be calibrated in future without an outbreak.
- **State what the threshold statistic can and cannot do**: "this iteration of the model cannot make predictions about the absolute probability or severity of outbreaks, for which model specification is critical. Rather, R loc is a useful threshold parameter for categorizing outbreak risk with data from contact-tracing studies."

## Results
**The threshold result is stated as a boundary across the whole physiological range**: "When all children have typical three-dose childhood immunity or more (N Ab ≥ 512), we estimated R loc < 1 over the entire physiological range and thus that WPV persistence is impossible under universal tOPV immunization."

**Settings are then sorted into three categories, each defined by the threshold**:
> "We identified three categories describing the transmission rate in different settings: low, where the fecal–oral route alone cannot sustain WPV transmission (R loc < 1 for all N Ab ≥ 1); moderate, where WPV epidemics can occur in immunologically naive communities but not where at least one-dose OPV-equivalent immunity is common (R loc ≥ 1 only for N Ab < 8); and high, where WPV can persist despite at least one-dose OPV-equivalent immunity in everyone"

**Each category is checked against history.** Low-transmission settings explain why IPV alone has worked in places with good sanitation; moderate ones match "the historical experience in middle- and high-development countries that WPV elimination rapidly follows the introduction of OPV vaccination"; the rarity of vaccine-derived outbreaks is reconciled with the model: "settings where the transmission rate for the Sabin strains is high have been rare."

**The key finding is a convergence in the absence of immunity**: in a high-transmission setting with insufficient immunity, "our model predicts that epidemic dynamics will be similar for all strains: R loc(Sabin) ≈ R loc(WPV) > 1 is determined by the number of social contacts and is insensitive to differences in infectiousness of the Sabin strains."

**Translate the threshold into something field teams can measure**: the fraction of index children, household members and contacts shedding after vaccination is given for each scenario, because "The fraction of vaccine recipients and unvaccinated contacts shedding is a direct probe of population immunity and the local transmission rate".

## Literature
Numbered PLoS citations. Earlier models are credited with agreement on the key conclusion — "Despite substantial methodological differences, all are in agreement that the Sabin strains will have reproduction numbers above one in high transmission rate settings with low population immunity" — before the paper's own innovation is named: "the key innovation of our work is its direct connection from individual-level measures of shedding and susceptibility obtained by stool surveys to assessment of community susceptibility."

A disagreement with one prior study is settled on design grounds: that study "lacked a control group of never-exposed subjects to contrast deeply waned and truly naive immunity."

## Voice
First-person plural, present tense for the model, past for the calibration. The register is precise and occasionally conversational ("we ignored fascinating questions about the effects of genetic evolution"). Conclusions about policy are separated from conclusions about the model: "we believe improved vaccines that produce infection-blocking immunity without the risks of Sabin OPV are required."

## Discussion and limitations
**Historical cases are read through the three categories**, one after another — the Netherlands (IPV sufficient), the United States (adequately protected now, not in 1960), Israel 2013 (moderate: wild virus persisted despite IPV, Sabin strains could not) — so the classification is tested against named events rather than asserted.

**The prediction is dated**:
> "Our model predicts that two or more children per family born after cessation are required to support Sabin 2 outbreaks in most high transmission rate settings. The median birth spacing in most bOPV-using countries is 24–36 months. Thus, we predict that between early 2018 and mid-2019, the risk of establishing type 2 cVDPV will increase substantially in many regions of the developing world that have not received post-cessation mOPV2 campaigns."

**Give the mechanism, the input and the date** — birth spacing turns a model threshold into a calendar window that later events could confirm or refute.

**The key limitation is stated once, plainly**: "while it can predict when the outbreak risk from OPV vaccination is negligible, it cannot address the absolute probability, severity, or geographic scope of outbreaks when they are possible without incorporating additional structural assumptions and calibration data about socially distant transmission."

**A misreading is headed off**: after arguing that Sabin OPV cannot guarantee protection, the paper adds "Regardless of the challenges detailed above, Sabin OPV vaccination is always preferable to natural infection by WPV or cVDPV. Thus, mass vaccination with OPV remains the most effective intervention to eliminate poliovirus transmission". **When a finding could be read as an argument against an intervention, say what it does not imply.**

## Data, code and funding
The digitised trial data, the model and the analysis code are in the supporting information and in a public repository, with an interactive visualisation of the primary data: "All relevant data and software are provided in the Supporting information files, and Interactive tools to explore the digitized primary data are available". Digitised data from published figures is itself a reusable product, and sharing it lets others check the synthesis.

## Distinctive moves to borrow
1. **Pose the question as *under what conditions*** when the answer is a classification.
2. **Distinguish your model by its direction of inference**, not its technique.
3. **Number the simplifying assumptions** and say how the Results use them.
4. **Define a latent quantity operationally**, and say what it does not represent.
5. **Admit approximate sample sizes from digitised figures.**
6. **Fix what cannot be identified**, and say which pair of parameters it is.
7. **Choose calibration studies for their reporting**, and say why.
8. **State what the threshold statistic cannot do** — absolute risk, severity, scope.
9. **Sort settings into categories defined by the threshold**, then test each against history.
10. **Translate the threshold into a measurable field quantity.**
11. **Date the prediction** using a demographic input such as birth spacing.
12. **Say what the finding does not imply** when it could be read against an intervention.
13. **Share digitised data and an interactive view of it.**

## Related files
For a multiscale model in which the parameter falls out of fitting every scale see [55-stopard-2021-malaria-eip](55-stopard-2021-malaria-eip.md); for outbreak-response vaccination modelled in a low-income setting see [01-grais-2008-measles-orv-niamey](01-grais-2008-measles-orv-niamey.md); for a vaccine campaign schedule computed from a transmission model see [49-verguet-2015-measles-sia](49-verguet-2015-measles-sia.md). Other *feasibility / threshold* exemplars: see [13-ferguson-2005-containing-pandemic-sea](13-ferguson-2005-containing-pandemic-sea.md) for a feasibility threshold and an operational checklist from a very large individual-based simulation; [81-kucharski-2016-ebola-ring-vaccination](81-kucharski-2016-ebola-ring-vaccination.md) for a branching-process threshold on missed cases beyond which ring vaccination cannot contain an outbreak; [22-hellewell-2020-contact-tracing-feasibility](22-hellewell-2020-contact-tracing-feasibility.md) for a branching-process boundary on when contact tracing can control an outbreak, with no fitted data; [79-golumbeanu-2022-malaria-tpp-emulator](79-golumbeanu-2022-malaria-tpp-emulator.md) for minimum coverage, efficacy and duration a new intervention must reach, found by searching an emulator of a simulation model.
