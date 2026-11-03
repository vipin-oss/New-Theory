# Gate 1 — Novelty: FAIL / STOP

Audit date: 2026-11-03. Working title: *A thermodynamically consistent hierarchy of nonlocal generalized thermoelasticity: free-energy structure, well-posedness and dispersion*.

## Decision and exact scope

**Do not advance to Gate 2.** The proposed central contribution—deriving spatially nonlocal thermoelastic stress and entropy together from a free energy—is already present in the literature. The available evidence does **not** establish a distinct, new classification theorem beyond reciprocity plus heat-law admissibility. Several directly relevant primary sources also remain unread. Under the requested adversarial protocol, these are grounds to reject the current novelty claim, not to certify it by absence of a matching title.

This decision is deliberately narrower than saying that someone has already proved the entire proposed Cattaneo/GN-III/MGT hierarchy with the requested well-posedness and dispersion results. **That stronger statement has not been verified.** No single-source priority claim for the entire hierarchy is made here. A potentially new extension is not automatically a demonstrated new classification.

An earlier working draft of this file said PASS, claimed complete primary-source reading, and stated that all DOIs were verified. Those claims were unsupported. This final report supersedes them. In particular, a publisher PDF header is not Crossref verification; a truncated extraction is not a full-text reading; secondary equations are not a substitute for an unread primary paper. The earlier draft also attached the wrong DOI to the Bazarra paper and the wrong journal/year to the published Sidhardh paper. Corrected records follow.

## 1. Evidence standard and sequence

The Drive corpus and existing repository audits were consulted before the web sources. Source locations are recorded in `../drive-analysis/paper_table.csv`; earlier conclusions in `../c1-hardening-2/prior_art_comparison.md` are **same-agent audit records**, not independent review.

Reading status and bibliographic status are separate:

- **PRIMARY SECTIONS READ** means the indicated constitutive/governing sections were actually returned and inspected. It does not mean every page was read.
- **PARTIAL / UNVERIFIED** means important text is unavailable or was omitted by response truncation. No negative novelty conclusion is inferred from an abstract or an unread section.
- **CROSSREF VERIFIED** means the Crossref work record was retrieved and matched by title/authors, not merely that a DOI appeared elsewhere.
- **UNVERIFIED DOI** means that direct Crossref check was not completed for this report, even if a previous bibliography labels the source verified.

The audit stopped on failure. It is not an exhaustive systematic review and does not claim a completed verification of all 152 PDFs or all references in earlier folders.

## 2. Comparison table

“Classification” below means the proposed full cross-heat-law operator-pairing classification, not a general statement of thermodynamic admissibility. “Not found in sections read” is not a claim about unread sections.

| Paper and bibliographic verification | Actual reading evidence | What is derived | Heat law | Nonlocality in stress and entropy/heat channels? | Proposed classification already known? |
|---|---|---|---|---|---|
| **Eringen (1974), Theory of nonlocal thermoelasticity**, IJES 12, 1063–1077. DOI `10.1016/0020-7225(74)90033-0`: CROSSREF VERIFIED | Drive `1tuZpa5qC4AmM7M2EKIi8Jk-Yu7vmwcow`: introduction and thermodynamic framework returned; middle of constitutive section omitted by tool truncation. Eqs. (4.8)–(4.9) are transcribed in the existing audit; not freshly verified against the omitted pages here | Nonlocal thermoelastic constitutive functionals from entropy inequality/objectivity. Earlier equation-level audit records the same thermal coupling kernel in stress and entropy | Classical / nonlocal Fourier according to earlier equation-level audit; middle equations PARTIALLY UNVERIFIED here | **Yes according to earlier audit**, with direct reinspection of the relevant middle pages still outstanding | Underlying reciprocity is prior art according to earlier audit; entire proposed generalized hierarchy/classification UNVERIFIED |
| **Eringen & Edelen (1972)**, On nonlocal elasticity; DOI/citation UNVERIFIED in this report | Drive `1a35X2xK_xpVoH_XyORNlCYRDXDHrza5U`; beginning/end extracted, middle truncated | Nonlocal balance/constitutive foundations in inspected material; details of thermodynamic restrictions not completely reinspected | UNVERIFIED for full paper | UNVERIFIED | UNVERIFIED |
| **Eringen, Nonlocal Continuum Field Theories**; book DOI/citation UNVERIFIED in this report | Source located in Drive `1M0bHTu64QzPRgQvIDbnP3oLJ0DB5YVnJ`; full relevant chapter not reinspected | Do not infer chapter contents from title or earlier broad labels | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| **Sidhardh, Patnaik & Semperlotti (2021)**, Thermodynamics of fractional-order nonlocal continua and its application to the thermoelastic response of beams, EJMA/Solids 88, 104238. DOI `10.1016/j.euromechsol.2021.104238`: CROSSREF VERIFIED. Preprint is dated 2020 | PRIMARY SECTIONS READ: arXiv `2003.10215`, especially §§2.2–2.3, Eqs. (24)–(33); chunks 5–6 rechecked | Derives stress and entropy from a common free energy of fractional strain and temperature; Eq. (31) contains mixed fractional-strain/temperature coupling; Eqs. (32a,b) give both constitutive channels | Integer-order Fourier; §2.3.1 explicitly discusses a particular fractional heat-flux law and its second-law difficulty | **Yes in fractional kinematics**: the same fractional strain is used in free energy and entropy, with nonlocal traction/momentum. Not the identical Eringen convolution-on-both-channels construction; heat flux itself remains local | General free-energy-derived consistent nonlocal thermoelasticity is already present. Exact proposed multi-law classification not found in the inspected sections |
| **Barretta, Čanađija, Luciano & Marotti de Sciarra (2018)**, Stress-driven modeling of nonlocal thermoelastic behavior of nanobeams, IJES 126, 53–67. DOI `10.1016/j.ijengsci.2018.02.012`: CROSSREF VERIFIED | PRIMARY SECTIONS READ: arXiv `1906.09626`, constitutive equations and beam reduction including Eqs. (22)–(25) | Stress-driven elastic strain under prescribed thermal strain, with constitutive boundary conditions | Prescribed static temperature; no coupled heat evolution in inspected formulation | Nonlocal elastic compliance; local prescribed thermal strain. Not a coupled entropy-channel construction | Not found in inspected formulation; cannot be cited as proof that all stress-driven thermoelastic literature lacks such a result |
| **Challamel, Grazide, Picandet, Perrot & Zhang (2016)**, A nonlocal Fourier's law and its application to the heat conduction of one-dimensional and two-dimensional thermal lattices, CR Mécanique 344, 388–401. DOI `10.1016/j.crme.2016.01.001`: CROSSREF VERIFIED | PRIMARY SECTIONS READ: governing equations, lattice continualization, sine-series solution, PDF chunks 0–2 | Nonlocal Fourier conduction and lattice-continuum approximation; heat equation with mixed space/time derivative | Nonlocal Fourier | Rigid conductor: no stress/entropy thermoelastic cross-coupling to classify | Not found in inspected sections; nonlocal heat law and benchmark limit are already known |
| **Bazarra, Fernández & Quintanilla (2024)**, Analysis of a one-dimensional nonlocal thermoelastic problem, ETNA 60. DOI `10.1553/etna_vol60s405`: CROSSREF VERIFIED; Crossref pages **405–420** | PRIMARY SECTIONS READ: model and Appendix A, UPCommons PDF chunks 0,1,5,6 | Fourier-coupled displacement/temperature PDE with nonlocal-stress differential relation; semigroup construction uses a gradient/micro-inertia velocity norm | Fourier | Local dilational entropy in inspected model; not the proposed reciprocal nonlocal stress/entropy constitutive pair with standard kinetic energy | Not found in inspected sections. Its PDE well-posedness must not be dismissed: a constitutive reciprocity objection is distinct from stability in its chosen energy norm |
| **Giorgi & Zullo (2026)**, Nonlinear and nonlocal models of heat conduction in continuum thermodynamics, CMT 38. DOI `10.1007/s00161-025-01443-3`: CROSSREF VERIFIED; online 2026-01-13 | PRIMARY SECTIONS READ: balance framework and rate-law/nonlocal heat sections; chunks 0,1,10–12, including Burgers conditions and start of §6 | Thermodynamic restrictions for rate-type heat laws and weakly nonlocal conduction with extra entropy flux | MCV, GN-III, Quintanilla/MGT, Burgers, GK discussed; only the sections actually read support detailed comparisons | Heat-conductor restrictions; no verified Eringen elastic kernel/entropy pairing theorem in sections read | Heat-law admissibility classification is substantially prior work. Exact coupled hierarchy not established as present or absent |
| **Marotti de Sciarra (2013)**; DOI/citation UNVERIFIED in this report | Drive `1A3Pmq0L_tsDvpNfGGvEvYBTujf5KfjNX`, beginning/end inspected; middle truncated | Variational thermoelastic formulation; no claim of complete constitutive verification here | GN-II according to earlier audit; full verification outstanding | UNVERIFIED | UNVERIFIED |
| **Romano et al. (2017)**; DOI/citation UNVERIFIED in this report | Drive `1Dab__2bTCYeYBJXqwKyWuYR399u02ve7`; earlier audit gives Robin CBCs; extraction here incomplete | Constitutive boundary conditions for integral elasticity according to earlier audit | Isothermal in earlier audit | No coupled heat-channel result verified here | UNVERIFIED for full-text conclusions |
| **Lazar & Agiasofitou (2022)**; DOI/citation UNVERIFIED in this report | Drive `1ca9aw_MAFTHYLyWX0Ln-ura9OtYlqDl_`; extraction incomplete | Nonlocal elastic wave framework in inspected material | No heat-law result verified here | UNVERIFIED beyond inspected material | UNVERIFIED |
| **Polizzotto; Borino; Benvenuti; Apuzzo** (sources listed below) | Relevant primary full texts NOT READ here; earlier secondary transcriptions are not primary verification | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| **Sellitto/Jou/Cimmelli; Ciarletta/Chiriţă** (sources listed below) | Relevant primary full texts NOT READ here | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| **Balta & Şuhubi (1977)**, Theory of nonlocal generalised thermoelasticity, IJES 15, 579–588. DOI `10.1016/0020-7225(77)90054-4`: CROSSREF VERIFIED | Found through the reference list in the Crossref record of Sidhardh et al.; primary full text NOT READ | UNVERIFIED: title is a search lead, not evidence for an equation or theorem | UNVERIFIED | UNVERIFIED | UNVERIFIED; important unresolved priority lead |

### Reading and metadata corrections

The Bazarra record is **not** `etna_vol60s422`; the title search resolves to `etna_vol60s405`. Crossref records 405–420; an earlier source note reported 405–421, so no silent reconciliation is attempted. Sidhardh et al. is published in **European Journal of Mechanics - A/Solids (2021)**, not IJSS (2020). Giorgi–Zullo's 2023 preprint URL does not establish a 2023 journal publication; the matched journal record is 2026. The exact equality of preprint and final journal versions has not been checked line by line.

## 3. Why the original novelty argument fails

### 3.1 The mechanical/entropy reciprocity is not heat-law-specific

The earlier Eringen audit transcribes a thermal-stress term `−∫β′(x,x′)T(x′)dx′` and an entropy term `+∫β′(x,x′)tr(e(x′))dx′`. If accurate, these already encode the claimed shared coupling kernel. Do not claim that adding a two-phase kernel to that same relation is a new reciprocity principle.

The basic bookkeeping illustrates the issue. For a quadratic free-energy functional with cross term `−<e,Bθ>`, differentiation gives thermal stress `−Bθ` and dilational entropy `B*e`. The adjoint relation comes from the cross term, independently of the later choice of Fourier, Cattaneo, GN, or MGT heat dynamics. This observation is **not a Gate 2 proof of the hierarchy**: domains, differentiability, energy-residual conventions, temperature linearization and internal thermal variables still need to be specified. It explains why simply restating reciprocity with a list of heat laws is not yet a new classification theorem.

Independently of the incomplete Eringen reinspection, Sidhardh et al. §§2.3.1–2.3.2 explicitly derives a consistent nonlocal thermoelastic free energy and both constitutive channels. Its fractional kinematics differ from Eringen convolution; that distinction must be kept, but the broad invention claim is untenable.

### 3.2 Separate necessary conditions do not establish a new coupled classification

Giorgi–Zullo supplies thermodynamic rate-law restrictions. Combining such restrictions with an inherited reciprocity condition may be useful synthesis. It does not establish a new necessary-and-sufficient joint theorem until one identifies what *interaction* between the spatial kernel and heat law creates a new obstruction or admissible regime, within a clearly bounded constitutive class.

The earlier draft's blanket condition “heat operator self-adjoint and positive” was not proved and is withdrawn. General passive operators need not be self-adjoint; internal-variable realizations and entropy-flux choices matter. Strict positivity versus semidefiniteness also requires explicit hypotheses. Class II bulk cancellation alone is not evidence of a second-law violation.

### 3.3 Remaining potential contributions are unestablished, not disproved

A sharp new theorem for noncommuting kernels, particular boundary domains, or genuinely coupled internal variables might survive. Likewise, nontrivial well-posedness/dispersion results may exist as extensions. None has been established as the requested new classification at this gate. Calling the full proposed family “absent from the literature” while Balta–Şuhubi and other relevant primary texts remain unread would violate the user's evidence rule.

## 4. Unverified-primary ledger

No statements about the following papers' detailed derivations or lack of a theorem are used as negative evidence. Unless explicitly marked Crossref verified above, their bibliographic identities/DOIs are also UNVERIFIED for this report.

- Polizzotto (2001), *Nonlocal elasticity and related variational principles*; Polizzotto's 2003 thermodynamic framework and later stress-gradient papers. Secondary discussion is in the old audit, but full primary texts were not read here.
- Borino–Failla–Parrinello (2003), symmetric nonlocal damage; Benvenuti–Borino–Tralli (2002). BFP kernel details quoted elsewhere in the repository do not certify primary reading here.
- Borino–Polizzotto thermoelastic uniqueness lead; Altan uniqueness lead; exact bibliographic identities remain to be checked.
- Barretta et al. (2019 and 2020), Apuzzo and collaborators. Reading the 2018 preprint does not verify these other papers.
- Sellitto–Cimmelli–Jou (2020), and Cimmelli/Sellitto/Jou heat-conduction papers; Jou et al. monograph in Drive `1ZrXqjUcROHI1e6VY8DtDvQbTqGw4RSuf`. Relevant full texts/chapters not read here.
- Ciarletta/Chiriţă nonlocal thermoelastic well-posedness lead; exact bibliographic identity and full text unverified.
- Quintanilla (2019), Bazarra–Fernández–Quintanilla (2021), El-Karamany–Ezzat (2016): Drive IDs `1iTN38f2sbbgON-QShcFved52u2ZNGjHJ`, `10nV2qgS3dZgZT-Nfffr9ChGOfB845u5n`, `1YSiwDQ1Vbo4xgTqOhbL0kLCfVlBrRi58`; full relevant texts not read here.
- Balta–Şuhubi (1977): metadata Crossref verified, primary text unverified. Neither its title nor secondary descriptions establish overlap with the requested theorem.
- Corpus-wide Class I/II counts in earlier audits were not independently reproduced in this gate; no new claim that all 29 primary papers were reread is made.

## 5. Verifiable source endpoints

The following Crossref work records were retrieved on the audit date and matched by title and author. Crossref establishes bibliography, **not** the scientific claims in a paper.

1. Eringen: https://api.crossref.org/works/10.1016%2F0020-7225(74)90033-0
2. Sidhardh et al.: https://api.crossref.org/works/10.1016%2Fj.euromechsol.2021.104238 (identified through a title query).
3. Barretta et al.: https://api.crossref.org/works/10.1016%2Fj.ijengsci.2018.02.012
4. Challamel et al.: https://api.crossref.org/works/10.1016%2Fj.crme.2016.01.001
5. Bazarra et al.: https://api.crossref.org/works/10.1553%2Fetna_vol60s405 (identified through a title query).
6. Giorgi–Zullo: https://api.crossref.org/works/10.1007%2Fs00161-025-01443-3
7. Balta–Şuhubi: https://api.crossref.org/works/10.1016%2F0020-7225(77)90054-4

Primary section access:

- https://arxiv.org/pdf/2003.10215 — chunks 5–6 contain Eqs. (24)–(33); other constitutive/beam sections were inspected earlier in this attempt.
- https://arxiv.org/pdf/1906.09626 — chunks 0–2 inspected.
- https://comptes-rendus.academie-sciences.fr/mecanique/item/10.1016/j.crme.2016.01.001.pdf — chunks 0–2 inspected.
- https://upcommons.upc.edu/server/api/core/bitstreams/9bed272d-34aa-45af-8a38-efcec4317bf1/content — chunks 0,1,5,6 inspected.
- https://www.researchgate.net/profile/Claudio-Giorgi/publication/376609221_NONLINEAR_AND_NONLOCAL_MODELS_OF_HEAT_CONDUCTION_IN_CONTINUUM_THERMODYNAMICS/links/65804573aff8b16813b6bb10/NONLINEAR-AND-NONLOCAL-MODELS-OF-HEAT-CONDUCTION-IN-CONTINUUM-THERMODYNAMICS.pdf — chunks 0,1,10–12 inspected. This is a manuscript copy; version equivalence not certified.

Drive extraction limitation: tool responses omitted middle text even when their internal extraction said `truncated: false`. The available download tool schema does **not** expose a `return_download_url` parameter; no such unsupported argument was invented. A public Drive link led to sign-in. This report therefore records the reading gap rather than pretending that the missing pages were inspected.

## 6. Status of requested downstream work

| Gate | Status |
|---|---|
| 1 — Novelty | **FAIL: claimed central novelty overlaps prior work; distinct full classification not established; primary-source gaps remain** |
| 2 — Mathematics | **NOT STARTED**, obeying the stop instruction |
| 3 — New physics | **NOT STARTED** |
| 4 — Benchmarks | **NOT STARTED** |
| 5 — Manuscript | **NOT STARTED** |

**Proved in this attempt:** no new classification, semigroup, or dispersion theorem. **Checked numerically:** no new simulation or convergence test. **Verified bibliographically:** seven matched Crossref records. **Claimed but not established:** novelty of the exact coupled generalized hierarchy. No LaTeX manuscript was written or compiled; no compilation-success claim is made. No acceptance forecast or journal-quartile determination is made.

## 7. Five hardest claims a referee would attack

1. **Novelty:** What is genuinely new beyond Eringen's stress–entropy reciprocity and established free-energy-derived nonlocal thermoelastic models?
2. **Classification:** What precise constitutive class makes the proposed conditions necessary and sufficient, rather than merely sufficient within one ansatz?
3. **Priority coverage:** How can absence of a generalized hierarchy be asserted before reading Balta–Şuhubi, Polizzotto, and the other directly relevant sources?
4. **Thermodynamic interpretation:** Why does a constitutive defect imply failure under the chosen physical power/energy conventions, rather than a different micro-inertia or nonlocal-residual formulation? Bulk cancellation and stable Lyapunov dynamics must not be conflated with inconsistency.
5. **Substantive physics:** Which demonstrable new observable survives comparison with consistent prior models, constitutive boundary conditions, and a justified length/time-scale regime? No such result was computed in this attempt.

These are same-agent criticisms, **not independent peer review**.

**FINAL VERDICT: kill — central free-energy/reciprocity novelty is inherited, a distinct coupled classification has not been established, and unresolved primary-source gaps prohibit a Gate 1 pass.**
