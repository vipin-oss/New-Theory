# Local MGT defect pilot and priority check

**Verdict: continue to nonlocal P4**

This is a *conditional research recommendation*, not a claim of originality or permission to add a kernel now. The local pilot has a defect-localized response and measurable relaxation sensitivity in one illustrative parameter set. Before nonlocal work, verify prior art and specify a published heterogeneous integral model and its interface/energy treatment. `Paper_10/03_Program` was inaccessible, so switching to that route cannot be justified or ruled out on implementation effort. No nonlocal kernel or new constitutive law was used in this pilot.

## Part A — published equations, fixed before computation

Use the local limit of the MGT thermoelastic equations (1)–(3) of Narayan Das, Soumen De and Nantu Sarkar, “Plane waves in Moore–Gibson–Thompson thermoelasticity considering nonlocal elasticity effect,” *Mathematics and Mechanics of Solids* **28**(9) (2023), 1978–1998, [10.1177/10812865221145737](https://doi.org/10.1177/10812865221145737). Their governing equations were inspected in the author-uploaded article; the original nonlocal parameter is set to zero, and the longitudinal one-dimensional specialization is used. They attribute the MGT theory to Ramón Quintanilla, “Moore–Gibson–Thompson thermoelasticity,” *Mathematics and Mechanics of Solids* **24** (2019), 4020–4031, [10.1177/1081286519862007](https://doi.org/10.1177/1081286519862007); original full text **unverified**.

For displacement u, temperature increment θ, thermal displacement α with α_t=θ, local stress σ, and heat flux q, the equations used in each uniform layer are exactly the standard MGT flux formulation

```text
σ = C u_x − β θ,                 ρ u_tt = σ_x,
c θ_t + β T0 u_xt = −q_x,       α_t = θ,
q + τ q_t = −K θ_x − K* α_x.
```

Here C is the longitudinal modulus, c volumetric heat capacity, T0 reference temperature, β thermoelastic coupling, K and K* the published flux coefficients, and τ the heat-flux relaxation time. Applying ∂t(1+τ∂t) to the heat balance gives `(K*+K∂t) θ_xx = (∂t+τ∂tt)(c θ_t+β T0 u_xt)`, i.e. the local 1D form of Das et al.'s thermal equation. The flux form with α is independently stated in the primary paper [Abouelregal et al., *Axioms* **12** (2023), 659, 10.3390/axioms12070659](https://doi.org/10.3390/axioms12070659). Nonzero-frequency harmonic solutions ensure compatibility with this flux and α_t=θ; no additional thermal-gradient or mechanical terms are added. C is an effective 1D longitudinal modulus, not a claim that lateral free-surface or a 3D plane-strain experiment was solved.

### Geometry, parameters, method and limitations

All numbers are **dimensionless illustrations**, not material measurements. Layers A and B have `(C,ρ,d)=(1,1,1)` and `(4,1,2)`; `c=1`, `T0=1`, `K=0.2`, `K*=0.1` throughout. The configuration is `(AB)^N A_d (BA)^N`; d=1 is the defect-free periodic stack `(AB)^(2N) A`, and d=2 is the single A-thickness defect. Both ends connect to identical semi-infinite *purely elastic* A leads; mechanical displacement and stress are continuous at the contacts and the thermoelastic stack is thermally insulated there, `q=0`. Within the stack, u, σ, θ and q are continuous. An elastic unit-displacement wave is incident from the left, with outgoing waves only in the leads. This is a specific mechanical port and thermal boundary choice, not open thermoelastic leads.

For the `exp(−iωt)` convention, let `s=−iω`, `h=(K+K*/s)/(1+τs)` and `y=(u,σ,θ,q)`. The local first-order system is

```text
u_x = (σ+βθ)/C,                 σ_x = ρ s² u,
θ_x = −q/h,                     q_x = −s[cθ+βT0(σ+βθ)/C].
```

Each layer uses `exp(M d)`, the standard exact local transfer matrix. To avoid the numerical instability of multiplying exponentially growing thermal modes, the code solves the matching equations for all interface states together (multiple shooting). The independent elastic reference uses a separate analytic 2×2 layer matrix. This does not certify arbitrary parameter ranges; no fitting or experimental validation was performed.

The elastic reference infinite-cell stop band, computed from `|tr(P_B P_A)/2|>1`, is **ω ∈ (1.230959, 1.910633)**. It is a lossless *reference* gap; the coupled dissipative system need not possess a strict real-frequency gap. Frequency below is angular frequency ω; ordinary frequency is ω/(2π). Transmission T is the outgoing/incident mechanical power ratio. FWHM is the separation of the two real-frequency points where T falls to **half its peak value**, without background subtraction; it is not a pole linewidth, a uniquely thermal damping rate, or a quality factor. The bracketing/optimization intervals and full numerical values are in `pilot.py` and `data.json`.

### Results: N=4 periods on each side

| β | τ | Peak ω | FWHM Δω | Peak T |
|---:|---:|---:|---:|---:|
| 0 | 0.1, 0.5, 1.0 | 1.570796 | 0.0039295 | 1.0000 |
| 0.10 | 0.1 | 1.575550 | 0.0080459 | 0.2535 |
| 0.10 | 0.5 | 1.576347 | 0.0091863 | 0.1947 |
| 0.10 | 1.0 | 1.577925 | 0.0072253 | 0.3219 |
| 0.25 | 0.1 | 1.600531 | 0.0288843 | 0.02692 |
| 0.25 | 0.5 | 1.605976 | 0.0351941 | 0.01837 |
| 0.25 | 1.0 | 1.613563 | 0.0202102 | 0.06259 |

A defect resonance **does exist in this illustrative finite stack**: for β=0.1 and τ=0.5, ω=1.576347 is inside the reference gap; its displacement profile grows toward the defect and falls toward both ends. Its frequency moves by 0.002376 (about 0.15%) and FWHM changes non-monotonically from 0.008046 to 0.009186 to 0.007225 as τ goes 0.1→0.5→1 with K and K* fixed. The τ effect is **small in frequency but not negligible in linewidth or peak transmission for these chosen numbers**. Increasing β from 0 to 0.25 at τ=0.5 shifts the peak upward and strongly reduces and broadens it. This is not a general trend or a calibrated physical prediction. At β=0, the mechanical result is independent of τ by decoupling.

Plots: [defect-free versus defect transmission](transmission.png), [relaxation/coupling sensitivity](sensitivity.png), [narrow resonance zoom](zoom.png), and [displacement profile](localization.png). Plots are sampled; the table uses scalar optimization and half-height root finding, so use the table for precision. No complex pole or eigenmode calculation was done; “localized resonance” refers to the measured finite, forced spatial profile rather than proof of a normal mode.

### Validation and finite-size convergence

* **No-defect:** `d=1` is algebraically `(AB)^(2N)A`; the test compares the product of local matrices to the periodic-cell power and checks the small-defect limit. No published numerical spectrum was replicated.
* **Elastic limit:** at β=0 the 4-state solution agrees with an independently coded standard analytic 2×2 elastic transfer matrix at five frequencies for both d=1 and d=2; tests require agreement to 10 decimal places. The elastic resonant ω=π/2 and T=1 serve as additional symmetry checks.
* **Power:** with these insulated ends, R+T+A=1. For harmonic fields, calculate `A = ∫[Re(1/h)|q|²/(2T0)] dx / P_inc`, `P_inc=ω²/2`, with numerical quadrature and layer solutions. This follows from the mechanical plus thermal flux `½ Re(−σ v* + θ* q/T0)`. `Re(1/h)≥0` here because `K−τ K*>0` for all tested τ. At β=0.1, τ=0.5 and resonance, `T=0.1947224`, `R=0.3058640`, `A=0.4994136`, and residual `1−T−R−A=1.8×10⁻¹⁵`. Across the nine reported peaks the maximum absolute residual was 2.5×10⁻¹⁴; additional test frequencies at τ=0.1, 0.5, 1 pass residual <10⁻⁹. This verifies this frequency-domain budget, not a general time-domain thermodynamic proof.
* **Cell-count sweep**, τ=0.5, β=0.1; N is per side:

| N | Peak ω | FWHM Δω | Peak T |
|---:|---:|---:|---:|
| 2 | 1.576402 | 0.0765683 | 0.85589 |
| 3 | 1.576344 | 0.0216629 | 0.57445 |
| 4 | 1.576347 | 0.0091863 | 0.19472 |
| 5 | 1.576353 | 0.0061212 | 0.02753 |
| 6 | 1.576356 | 0.0053543 | 0.00228 |

The frequency is nearly stable by N=3, but linewidth and peak transmission **have not converged** at N=6; loss and changing lead leakage make transmission tend downward. This is a finite-size sensitivity study, not proof of an infinite-stack limit. Do not assert a converged intrinsic linewidth or independent additive loss channels.

## Part B — targeted priority and Paper_10 access check

Search used primary papers and publisher pages for phononic defect/localized modes, GN-III/MGT/DPL thermoelastic stacks, and DPL plus dipolar-gradient defects. **No equivalent finite mechanically coupled GN/MGT/DPL defect-stack result was established by this quick search.** This is not proof that one does not exist; search coverage, citing papers, full texts and alternate terminology remain incomplete. Important nearby overlaps:

1. Jesús Manzanares-Martínez, Betsabé Manzanares-Martínez, Raúl Esquivel-Sirvent and Diego Soto-Puebla, “Defect-Induced Localization in One-Dimensional Thermal Wave Crystals,” *Crystals* **16**(7) (2026), 440, [10.3390/cryst16070440](https://doi.org/10.3390/cryst16070440). Publisher abstract and introductory/results snippets inspected; full equations/results not independently audited. A single defect in a finite periodic **Cattaneo–Vernotte thermal wave** structure, transfer matrix, localization, and layer-count/defect-thickness dependence are already published. It is heat-only, not evidence of a mechanically coupled MGT/GN/DPL rod result.
2. Arafa H. Aly and Ahmed Mehaney, “Modulation of the Band Gaps of Phononic Crystals with Thermal Effects,” *International Journal of Thermophysics* **36** (2015), 2967–2984, [10.1007/s10765-015-1952-x](https://doi.org/10.1007/s10765-015-1952-x). Abstract read; full paper **unverified**. One-dimensional elastic defect localization with temperature effects is already reported; the abstract does not establish coupled dynamic GN, MGT or DPL heat transport. Related chapter: Aly and Mehaney, “Phononic Crystals and Thermal Effects,” in *Photonic Crystals – A Glimpse of the Current Research Trends* (2019), [10.5772/intechopen.82068](https://doi.org/10.5772/intechopen.82068), sections/abstract inspected; exact thermal constitutive interpretation and relationship to the 2015 paper **unverified**.
3. Jun Jin, Ningdong Hu and Hongping Hu, “Size effects on the mixed modes and defect modes for a nano-scale phononic crystal slab,” *Applied Mathematics and Mechanics* **44** (2023), 21–34, [10.1007/s10483-023-2945-6](https://doi.org/10.1007/s10483-023-2945-6). Abstract read; full numerical details **unverified**. Elastic nonlocal strain-gradient slab defect modes are known; no basis to label it DPL-coupled.
4. Zhenzhao Shu, Gongye Zhang, Yu Cong and Shuitao Gu, “Size effects on a one-dimensional defective phononic crystal sensor,” *Smart Materials and Structures* **32** (2023), 115029, [10.1088/1361-665X/ad026c](https://doi.org/10.1088/1361-665X/ad026c). Author-uploaded abstract inspected; complete model **unverified**. Already treats 1D defective phononic transmission with simplified strain-gradient elasticity, using a stiffness matrix. It is not established as DPL thermoelasticity or the exact dipolar model of Paper_10.
5. Seyed Mahmoud Hosseini and Chuanzeng Zhang, “Nonlocal coupled thermoelastic wave propagation band structures of nano-scale phononic crystal beams based on GN theory with energy dissipation: An analytical solution,” *Wave Motion* **92** (2020), 102429, [10.1016/j.wavemoti.2019.102429](https://doi.org/10.1016/j.wavemoti.2019.102429). Publisher abstract/introduction inspected; full equations and whether any defect is studied **unverified**. GN-III/nonlocal periodic band structures are known; do not infer a defect result from its abstract.

**Paper_10 solver:** authenticated `gh api repos/vipin-oss/Paper_10` and `.../contents/03_Program` each returned HTTP 403 “Resource not accessible by integration”. Thus the files, data structures, existing results, publication status and modification effort are **unverified**. A finite-defect extension might be straightforward *if* an existing stable code already exposes per-layer scattering matrices, generalized mechanical/thermal interface conditions, and exterior ports; an infinite-Bloch-only solver or a gradient model needing additional traction conditions may require substantive work. This is a conditional engineering assessment, not an inspection or an estimate of effort. The locally supplied archive's `Paper 10.pdf` was inspected on its first page and is an unrelated 2013 paper; it is not evidence about the named repository. The targeted search found no verified publication matching **DPL + dipolar-gradient + defects** as a complete combination, but cannot certify that it is unpublished. Obtain repository access and inspect its manuscript and `03_Program/`, then search its references/citations before deciding between routes.

## Reproduction and outstanding gates

Run with Python 3 and NumPy, SciPy, Matplotlib: `OPENBLAS_NUM_THREADS=1 python pilot.py` then `OPENBLAS_NUM_THREADS=1 python -m unittest -v test_pilot.py`. Tested using Python 3.11, NumPy 2.4.6, SciPy 1.17.1 and Matplotlib 3.11.2: **4 tests passed**. `data.json` contains all reported values; plots regenerate from the same code. Install dependencies in an isolated environment. No external data or nonlocal solver is included.

Before further work: obtain Paper_10 access; read full primary literature for equivalent finite-stack modes and compare its specific DPL/dipolar operators; validate the chosen MGT parameters for an actual material and the physical thermal boundary; establish nonlocal interface/energy and numerical well-posedness separately; repeat with independent numerical methods and obtain independent review. No novelty, material validity, intrinsic Q or publication priority is certified.
