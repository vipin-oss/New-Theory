# Round 2 Hardening Report — Candidate C1: Artifact Test, Prior-Art Audit, Self-Audit of Co-Authored Papers, Calibration Bounds, and Revised Scope Recommendation

**Branch**: `arena/6d6cb055-new-theory`  
**Directory**: `paper/c1-hardening-2/`  
**Status**: Pre-drafting Round 2 mathematical & physical hardening complete (`10/10` automated SymPy/NumPy/SciPy pytest checks passing across Round 1 + Round 2).

---

## Executive Summary of Round 2 Findings

Round 2 subjected every claim of Round 1 (`paper/c1-hardening/`) to four adversarial stress tests:

1. **Task 1 — The Artifact Test ([`artifact_test.md`](./artifact_test.md), [`artifact_test.py`](./artifact_test.py))**:
   - **What disappears**: The static $1/\sqrt{\gamma}$ surface thermal-expansion boundary layer under uniform temperature rise $\theta_0$ ($\varepsilon^{\text{V2}}(0)/\varepsilon^{\text{V1}}(0) = 1/\sqrt{\gamma}$) **is a kernel-truncation artifact** caused by using an unnormalized Helmholtz kernel $K_\ell^{\text{unnorm}}(x, \xi) = \frac{1}{2\ell}e^{-|x-\xi|/\ell}$ on a bounded/semi-infinite domain ($\int_0^\infty K_\ell^{\text{unnorm}}(0, \xi)\,d\xi = 1/2 \neq 1$). When replaced by **any** symmetric partition-of-unity normalized kernel satisfying $\int_\Omega K_\ell^{\text{norm}}(x, \xi)\,d\xi \equiv 1$ — including **(a1) the Borino–Failla–Parrinello (2003) / Polizzotto (2001) additive-defect normalized kernel $W_\ell^{\text{BFP}}(x, \xi)$** and **(a2) the reflecting / Neumann Green's-function kernel $K_\ell^{\text{Neu}}(x, \xi)$** — we have $\mathcal{L}_{\gamma,\ell}^{\text{norm}}[1](x) \equiv 1$, and consequently $\varepsilon^{\text{V1}}(x) = \varepsilon^{\text{V2}}(x) \equiv \frac{\beta\theta_0}{E}$ everywhere ($\varepsilon^{\text{V2}}(0)/\varepsilon^{\text{V1}}(0) = 1.000000000000000$ to $< 2.5 \times 10^{-15}$). **This static uniform-heating layer is dropped from Candidate C1's claims.**
   - **What survives**:
     - **Theorem 1** (V1/V2 global Second-Law consistency via $L^2(\Omega)$ self-adjointness of $\mathcal{L}_{\gamma,\ell}$, and the Maxwell/Clausius–Duhem violation of Camp 1) **survives unchanged** under all three kernels (`unnorm`, `bfp`, `neu`).
     - **Theorem 2** (necessity of two Constitutive Boundary Conditions to close the 2nd-order constitutive ODE on bounded domains) **survives** (Robin CBCs for $K_\ell^{\text{unnorm}}$, modified Robin CBCs for $W_\ell^{\text{BFP}}$, homogeneous Neumann CBCs $g' = \gamma f'$ for $K_\ell^{\text{Neu}}$), with V1 vs. V2 CBCs differing under normalized kernels whenever the boundary temperature gradient is non-zero ($\theta_{,x}\big|_{\partial\Omega} \neq 0$).
     - **Theorems 3 & 4** (quartic $N=4$ vs. cubic $N=3$ spatial dispersion degree in $q = k^2$, $\gamma \to 0$ singular perturbation mechanism explaining Camp 2's bulk operator cancellation, and bulk high-$k$ attenuation asymptotics) **survive unchanged** in the bulk.

2. **Task 2 — Prior-Art Comparison ([`prior_art_comparison.md`](./prior_art_comparison.md))**:
   - **What is already known and must be credited as background**:
     - Global nonlocality-residual thermodynamics ($\int_\Omega P\,dx = 0 \iff \mathcal{R} = \mathcal{R}^*$ on $L^2(\Omega)$) is due to **Edelen & Laws (1971)**, **Eringen (1974, Eq. 2.13)**, **Polizzotto (2001, 2003a)**, and **Borino, Failla & Parrinello (2003)**.
     - Equality of the thermal-stress kernel $\beta'(|x-x'|)$ in $t_{kl}$ and the dilational-entropy kernel $\beta'(|x-x'|)$ in $\rho\eta$ is **already proved in Eringen (1974), Eqs. (4.8)–(4.9)** (and its strain-gradient counterpart in **Giorgi & Morro 2025, Section 3.1, Eqs. 19–20**).
     - Isothermal two-phase ODE reduction and Robin / modified-kernel CBCs on bounded intervals $[0, L]$ are **already proved in Challamel & Wang (2008), Fernández-Sáez et al. (2016), Romano et al. (2017), Mikhasev & Nobili (2020), and Nobili & Pramanik (2025b, Eqs. 10–16)**.
   - **What C1 genuinely adds**:
     - Proving that the widespread post-2015 "Camp 1" shortcut ($(1 - \ell^2\partial_x^2)\sigma = E\varepsilon - \beta\theta$ paired with local $\rho\eta = \beta\varepsilon + \frac{\rho c_E}{T_0}\theta$, including Yu, Tian & Liu 2015 and Yu, Tian & Xiong 2016) violates Maxwell symmetry in **both** the Helmholtz $(\varepsilon, \theta)$ representation and Polizzotto's (2014) stress-gradient Gibbs $(\sigma, \theta)$ representation (where Gibbs consistency requires $\rho\eta^{\text{Gibbs}} = \frac{\beta}{E}\sigma + \frac{\rho c_\sigma}{T_0}\theta = \rho\eta^{\text{loc}} + \frac{\beta\ell^2}{E}\sigma_{,xx}$), and yields negative internal dissipation on closed cycles.
     - Formulating the explicit two-phase thermoelastic differential systems (**Variant V1** vs. **Variant V2**) and their thermoelastic CBCs under unnormalized and normalized kernels.
     - Proving the **quartic ($N=4$, 8th-order in space) vs. cubic ($N=3$, 6th-order in space)** spatial mode-count theorem (Theorem 3) and showing how Camp 2's bulk operator cancellation emerges as a singular perturbation limit as $\gamma \to 0^+$ via an escaping evanescent mode $q_4 \sim -1/(\gamma\ell^2)$.

3. **Task 3 — Census Wording & Unsoftened Self-Audit ([`revised_census.md`](./revised_census.md))**:
   - The 29 papers in `literature_audit.csv` are a **convenience sample** drawn from the user's personal Google Drive folder (`Papers`), **not** a random or exhaustive sample of the literature. All universal claims (*"100% of the literature"*, *"zero papers in the literature"*) are replaced with exact sample-bounded wording.
   - **13 of the 29 surveyed papers (`44.8%`) are co-authored by the user (Vipin Gupta)**:
     - **2 co-authored papers in Camp 1** (`Barak et al. 2023`, *Indian J. Phys.*, id 8; `Gupta et al. 2023a`, *Int. J. Numer. Methods Heat Fluid Flow*, id 9) suffer directly from the **Theorem 1 thermodynamic contradiction** (applying $(1-\ell^2\nabla^2)$ to thermal stress while keeping local dilational heating in the energy equation) and additionally enforce interface traction continuity at $x_3 = 0$ on the **local** stress $\sigma_{33}, \sigma_{31}$ instead of the physical Cauchy stress $t_{33}, t_{31}$, while omitting CBCs.
     - **11 co-authored papers in Camp 2** (`Yadav et al. 2022`, id 15; `Gupta, Barak & Das 2023b`, id 16; `Das et al. 2024`, id 17; `Gupta et al. 2024a`, id 18; `Gupta, Barak & Das 2024b`, id 19; `Das et al. 2025`, id 20; `Gupta et al. 2025`, id 21; `Aldandani et al. 2026a`, id 22; `Aldandani et al. 2026b`, id 23; `Das et al. 2026`, id 24; `Gupta et al. 2026`, id 25) apply an identical single-phase ($\gamma = 0$) nonlocal operator ($(1-\ell^2\nabla^2)$ or $(1-\xi^2\nabla^2+\tau^2\partial_t^2)$) to stress, entropy, and heat flux, **cancelling the nonlocal operator identically out of the bulk heat PDE** in all 11 papers and omitting integral CBCs at the half-space boundary $z = 0$.

4. **Task 4 — Calibration & Frequency-Regime Audit ([`calibration_analysis.md`](./calibration_analysis.md), [`calibration_audit.py`](./calibration_audit.py))**:
   - Using independent atomistic calibrations of $\ell$ for FCC Aluminum at $300\text{ K}$ (**Lazar, Agiasofitou & Böhlke 2022**, Tables 3 & 6: 2NN MEAM $\bar{\ell}_1 = 0.120272\text{ nm}$; **Eringen 1983**: $\ell = e_0 a = 0.157931\text{ nm}$), the ratio of the nonlocal length $\ell$ to the characteristic thermoelastic length $\ell^* = c_0/\omega^* = 15.19\text{ nm}$ is $\chi_{\text{nl}} = \ell/\ell^* = 0.0079\text{–}0.0104$ ($\chi_{\text{nl}}^2 \approx 6.3 \times 10^{-5}\text{–}1.1 \times 10^{-4}$).
   - Moreover, $\gamma \in (0, 1)$ has **no** independent experimental or unique $O(k^2\ell^2)$ phonon-dispersion calibration (only $\ell_{\text{eff}} = \sqrt{1-\gamma}\,\ell$ enters at $O(k^2\ell^2)$; Nobili & Pramanik 2025b).
   - Inside the frequency regime where Fourier heat conduction is physically defensible ($\omega\tau_q \lesssim 0.1 \implies f \lesssim 10.6\text{ GHz}$, or even up to the Zener peak $\Omega \le 1$, $f \le 67.3\text{ GHz}$), $(k\ell)^2 \le 10^{-4}$ and **the relative difference in bulk thermoelastic damping between V1, V2, and Camp 1 is $O(10^{-5}\text{–}10^{-4})$ ($0.001\%\text{–}0.013\%$)** — far below experimental measurability. The $O(1)$ damping divergence occurs only at multi-THz Brillouin-zone-edge frequencies ($\Omega \sim 100, \lambda \sim 0.8\text{ nm} \approx 2a$) where both Fourier heat conduction and continuum elasticity are invalid.

---

## Task 5 — Revised Scope Recommendation: Should C1 Be a Full Paper or a Focused Critical / Clarification Note?

### Honest Assessment After Dropping What Does Not Survive Tasks 1–4

After removing:
- the static $1/\sqrt{\gamma}$ uniform-heating surface layer (which Task 1 proved is an unnormalized kernel-truncation artifact),
- over-claims of novelty on Eringen's (1974) kernel-duality principle and Fernández-Sáez/Romano/Nobili–Pramanik's isothermal two-phase CBCs (Task 2),
- universal *"100% of the literature"* census claims (Task 3), and
- claims of large measurable bulk ultrasonic damping differences in Fourier-regime crystals (Task 4),

**Candidate C1 should NOT be pitched as a grand "New Physical Theory of Nonlocal Thermoelasticity" or an experimental nanoscale characterization paper.** Over-claiming it for a top flagship mechanics journal (*JMPS* or *IJES*) as a major new physical theory would invite immediate desk or referee rejection on two grounds: (i) Eringen (1974, Eqs. 4.8–4.9) already wrote the general integral kernel symmetry, and (ii) for calibrated $\ell \approx 0.12\text{ nm}$ in Al, the V1 vs. V2 difference is $O(10^{-4})$ in the Fourier regime and $0$ under static uniform heating with normalized kernels.

**However, what DOES survive Tasks 1–4 forms a sharp, rigorous, and genuinely useful 10–14 pageFocused Critical & Foundational Clarification Paper (or Short Communication / Clarification Note):**
1. **A clean mathematical impossibility proof (Theorem 1b)** showing that the post-2015 "Camp 1" differential shortcut $(1 - \ell^2\partial_x^2)\sigma = E\varepsilon - \beta\theta$ paired with local constant-strain entropy $\rho\eta = \beta\varepsilon + \frac{\rho c_E}{T_0}\theta$ violates Maxwell symmetry in **both** the Helmholtz $(\varepsilon, \theta)$ framework and Polizzotto's (2014) stress-gradient Gibbs $(\sigma, \theta)$ framework (where Gibbs consistency requires $\rho\eta^{\text{Gibbs}} = \rho\eta^{\text{loc}} + \frac{\beta\ell^2}{E}\sigma_{,xx}$), and yields negative internal dissipation on closed cycles.
2. **A constructive unification of the three literature practices ("Camps 1, 2, 3")** as limiting or mismatched cases of the two Eringen-consistent two-phase ($\gamma \in (0, 1)$) differential realizations (**Variant V1** and **Variant V2**), explicitly proving:
   - the **quartic ($N=4$) vs. cubic ($N=3$) spatial dispersion degree theorem** (Theorem 3) and how Camp 2's bulk heat-operator cancellation emerges as a singular perturbation as $\gamma \to 0^+$ via the escaping evanescent root $q_4 \sim -1/(\gamma\ell^2)$;
   - the **exact boundary closure conditions (Theorem 2)** on bounded domains $[0, L]$ and half-spaces $[0, \infty)$ under unnormalized ($K_\ell^{\text{unnorm}}$), Borino–Failla–Parrinello normalized ($W_\ell^{\text{BFP}}$), and reflecting Neumann ($K_\ell^{\text{Neu}}$) kernels, demonstrating why naive unnormalized kernels create artificial $1/\sqrt{\gamma}$ static thermal boundary layers that vanish upon proper kernel normalization; and
   - an **order-of-magnitude physical calibration audit** (using Lazar, Agiasofitou & Böhlke 2022 for Al) showing why bulk nonlocal thermoelastic damping corrections are $O((k\ell)^2) \lesssim 10^{-4}$ inside the Fourier validity window, whereas the mathematical consequences (Second-Law well-posedness, PDE order $N=4$ vs. $N=3$, and boundary closure) are decisive for the mathematical correctness of boundary-value and wave-reflection problems.

### Recommended Format, Section Outline, and Realistic Target Venue Tier

- **Recommended Format**: **Focused Critical & Clarification Paper / Short Regular Article** (approx. 10–14 pages, 5 sections, no inflated physical claims).
- **Realistic Target Venue Tier**:
  - **Primary Q1/Q2 Specialty Continuum & Thermoelasticity Journals**:
    1. *Continuum Mechanics and Thermodynamics* (Springer) — **Best fit**: regularly publishes foundational clarifications on nonlocal/gradient thermodynamics (e.g., Lazar, Agiasofitou & Böhlke 2022) and already published the user's 2026 paper (`Gupta et al. 2026`, *CMT* 38:41), making a mathematical clarification of the thermodynamic and boundary-condition foundations of nonlocal thermoelasticity directly relevant to its readership.
    2. *Journal of Thermal Stresses* (Taylor & Francis) — **Strong fit**: the core audience of Camp 1 / Camp 2 / Camp 3 nonlocal thermoelastic wave papers.
    3. *Acta Mechanica* or *Mechanics Research Communications* (Elsevier) — **Good fit** for a concise, mathematically rigorous clarification note (following Pham & Vu 2024 in *Acta Mech.*).

### Concrete 5-Section Outline for the Reframed Clarification Paper

1. **Section 1 — Introduction & Survey of Three Divergent Practices in Nonlocal Thermoelasticity**
   - Review Eringen's (1974) integral thermoelasticity (Eqs. 4.8–4.9) and the post-1983 shift to differential Helmholtz equations.
   - Document the three divergent constitutive practices in a surveyed sample of 29 nonlocal thermoelasticity papers (including both external papers and a transparent self-audit of the authors' own prior Camp 1 and Camp 2 works): Camp 1 (Form A stress + local entropy), Camp 2 (all-field single-phase operator cancellation), and Camp 3 (elastic-only nonlocality).
2. **Section 2 — Thermodynamic Admissibility in Helmholtz and Gibbs Representations (Theorem 1)**
   - Review Polizzotto's (2001, 2003a) self-adjoint nonlocality-residual framework on $L^2(\Omega)$ and Eringen's (1974) kernel-duality rule.
   - Derive the two thermodynamically admissible two-phase ($\gamma \in (0, 1)$) differential realizations: **Variant V1** (thermo-mechanically nonlocal) and **Variant V2** (mechanically nonlocal).
   - Prove **Theorem 1b**: Camp 1 violates Fréchet-derivative symmetry in both the Helmholtz $(\varepsilon, \theta)$ and Polizzotto (2014) stress-gradient Gibbs $(\sigma, \theta)$ representations (deriving the missing $\frac{\beta\ell^2}{E}\sigma_{,xx}$ Gibbs entropy correction) and exhibits negative internal dissipation $\Delta\mathcal{D}_{\text{cycle}} < 0$ on closed harmonic cycles.
3. **Section 3 — Bounded Domains, Kernel Normalization, and Constitutive Boundary Conditions (Theorem 2 & Artifact Analysis)**
   - Extend the isothermal CBC framework (Fernández-Sáez et al. 2016; Romano et al. 2017; Nobili & Pramanik 2025b) to two-phase thermoelasticity on $[0, L]$ and $[0, \infty)$.
   - Compare unnormalized ($K_\ell^{\text{unnorm}}$), Borino–Failla–Parrinello normalized ($W_\ell^{\text{BFP}}$), and reflecting Neumann ($K_\ell^{\text{Neu}}$) kernels.
   - Prove that the static $1/\sqrt{\gamma}$ surface strain spike under uniform heating is a kernel-truncation artifact of $K_\ell^{\text{unnorm}}$ that vanishes identically ($\varepsilon^{\text{V1}} \equiv \varepsilon^{\text{V2}} \equiv \frac{\beta\theta_0}{E}$) under both $W_\ell^{\text{BFP}}$ and $K_\ell^{\text{Neu}}$, while genuine V1 vs. V2 boundary differences persist under non-zero temperature gradients ($\theta_{,x} \neq 0$).
4. **Section 4 — Spatial Mode-Count Theorem ($N=4$ vs. $N=3$) and the $\gamma \to 0$ Singular Perturbation (Theorems 3–4)**
   - Prove that Variant V1 is 8th-order in space (quartic in $q = k^2$, 4 wave-mode pairs) whereas Variant V2 and Camp 1 are 6th-order (cubic in $q = k^2$, 3 wave-mode pairs).
   - Prove how Camp 2's bulk heat-operator cancellation arises as the $\gamma \to 0^+$ singular limit of V1 via the escaping evanescent mode $q_4 \sim -1/(\gamma\ell^2)$.
   - Compare high-$k$ attenuation scaling ($\alpha_1^{\text{Camp 1}} \propto k^{-2}$ vs. $\alpha_1^{\text{V1,V2}} \to \text{const} > 0$).
5. **Section 5 — Physical Calibration Audit (FCC Aluminum & Silicon) and Concluding Guidelines**
   - Present the exact scale audit using Lazar, Agiasofitou & Böhlke's (2022) 2NN MEAM characteristic length $\bar{\ell}_1 = 0.1203\text{ nm}$ for Al ($\chi_{\text{nl}} = \ell/\ell^* = 7.92 \times 10^{-3}$).
   - Show transparently that inside the Fourier-defensible frequency regime ($\omega\tau_q \lesssim 0.1$), bulk damping differences between V1, V2, and Camp 1 are $O((k\ell)^2) \lesssim 10^{-4}$, and summarize practical guidelines for choosing consistent equations and boundary conditions in future nonlocal thermoelasticity studies.

---

## Summary of Deliverable Files in `paper/c1-hardening-2/`

| File | Description |
| :--- | :--- |
| [`REPORT.md`](./REPORT.md) | Consolidated Round 2 hardening report and Task 5 revised scope recommendation |
| [`artifact_test.md`](./artifact_test.md) | Task 1 analytical & numerical proof that the static $1/\sqrt{\gamma}$ surface layer is a truncation artifact, plus survivor classification table |
| [`prior_art_comparison.md`](./prior_art_comparison.md) | Task 2 comparison with Eringen (1974), Polizzotto (2001–2016), Borino et al. (2003), Yu et al. (2015, 2016), Giorgi & Morro (2025), and Nobili & Pramanik (2025a,b) |
| [`revised_census.md`](./revised_census.md) | Task 3 convenience-sample wording corrections and unsoftened equation-level self-audit of all 13 co-authored papers by V. Gupta |
| [`calibration_analysis.md`](./calibration_analysis.md) | Task 4 calibration & Fourier-validity audit for FCC Aluminum (Lazar et al. 2022; Eringen 1983) and Silicon |
| [`artifact_test.py`](./artifact_test.py) | Symbolic (SymPy) and numerical (split-triangle piecewise-constant Galerkin) verification script for Task 1 |
| [`calibration_audit.py`](./calibration_audit.py) | Quantitative dispersion & Fourier-regime calibration audit script for Task 4 |
| [`test_c1_round2.py`](./test_c1_round2.py) | Automated pytest suite for Round 2 (`4/4` tests passing; `10/10` combined with Round 1) |
