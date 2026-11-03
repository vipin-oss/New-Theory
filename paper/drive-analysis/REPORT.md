# Drive Literature Analysis & New-Theory Decision Report (`REPORT.md`)

**VERDICT: GO — Candidate C1: *Variational Two-Phase Integral Nonlocal Generalized Thermoelasticity on Bounded and Semi-Infinite Domains: Free-Energy Reciprocity, Interpoint Availability Flux, and Boundary-Layer Wave Mechanics*.**

---

## 1. Executive Summary & Coverage Audit

1. **Complete Phase 1 Corpus Coverage (`152/152` PDFs + 157-page Review):**
   - Every one of the **152 PDF files** in the Google Drive `Papers` folder is `done` in [`papers_manifest.csv`](papers_manifest.csv) (`0 pending`, `0 text-extraction-failed`) and extracted across all 15 bibliographic and technical columns in [`paper_table.csv`](paper_table.csv) and [`paper_table.md`](paper_table.md):
     - **138 full-text PDF reads**,
     - **8 full visual rasterized reads** of scanned historical classics (including the two previously blocked Royal Society papers `Lamb_1917.pdf` and `Green_1991.pdf`, plus `Stoneley_1924.pdf`, `maxwell1867.pdf`, `Unknown_e.pdf` [Barnett et al. 1985], `Eringen_1966.pdf`, and Gurtin & Murdoch 1975+Addenda / 1978), and
     - **6 full-length monographs** (261–484 pp. each: Yang 2018, Müller & Ruggeri 1998, Povstenko 2015, Jou et al. 2010, Gorenflo et al. 2014, Eringen 2002).
   - All **157 pages** of Vipin Gupta's review manuscript *Waves in Thermoelastic and Multiphysics Continua: Generalized Heat Conduction, Coupled Fields and Size Effects* (`review paper.pdf`, dated November 3, 2026) were read section-by-section and mapped in [`review_map.md`](review_map.md).
2. **Core Scientific Discovery Across the 152 Papers + 2020–2026 Literature:**
   - Reading the entire corpus uncovered **two compounding mathematical defects** affecting virtually the entire 2019–2026 "nonlocal generalized thermoelastic wave" literature (including folder positions 151 and 152 and recent 2025–2026 external papers) and directly answering **Gap 8** (p. 93), **Gap 1** (p. 92), and **Questions R1, R2, R6** (p. 95) of `review paper.pdf` (as well as the unresolved nonlocal interpoint flux blocker in `paper/new-model/STATUS.md`):
     1. **Bulk Thermodynamic Reciprocity Defect (`Review Gap 8`):** Recent papers heuristically pair **Form A** nonlocal stress $(1-\xi^2\partial_x^2)\sigma = M_1\varepsilon - \beta\theta$ with the **constant-strain** energy equation $\rho c_\varepsilon\dot{\theta} + T_0\beta\dot{\varepsilon} = -\partial_x q$. Completing the square in the nonlocal Helmholtz free energy proves this pairing **violates Maxwell reciprocity** ($\delta^2\Psi/\delta\varepsilon\delta\theta \ne \delta^2\Psi/\delta\theta\delta\varepsilon$), injecting spurious internal power that **destroys energy conservation even in lossless Green–Naghdi Type II thermoelasticity**. Exact reciprocity yields two distinct variational theories: **Model V1** ($\mathcal{M}_\varepsilon$: strain-kernel nonlocality $\implies$ Form B stress + constant-strain entropy $c_\varepsilon$) and **Model V2** ($\mathcal{M}_{\varepsilon^{\mathrm{el}}}$: elastic-strain-kernel nonlocality $\implies$ Form A stress + constant-stress entropy $\rho c_\sigma\dot{\theta} + (T_0\beta/M_1)\dot{\sigma} = -\partial_x q$).
     2. **Bounded-Domain Integral Inequivalence & Missing Boundary-Layer Wave (`Questions R1, R2, R6`):** As proved for isothermal beams by Romano et al. (2017, Pos 47) and Yang (2018 Ch. 7.5, Pos 2) and extended to **isothermal** elastic/piezoelectric half-space waves by Vinh, Anh & Hue (2024 *Proc. R. Soc. A*; Jan & March 2026 *ZAMP* / *Arch. Appl. Mech.*), replacing the bi-exponential integral kernel on $[0,L]$ or $[0,\infty)$ with $(1-\xi^2\partial_x^2)$ is valid **if and only if** enforced alongside **homogeneous Robin Constitutive Boundary Conditions (CBCs)** $\partial_x w(0) - \xi^{-1}w(0) = 0$, $\partial_x w(L) + \xi^{-1}w(L) = 0$. In two-phase nonlocal thermoelasticity ($\gamma\in(0,1)$), this raises the dispersion relation to a **cubic in $k^2$ (3 wave modes / 6 waves)**, exciting an **evanescent nonlocal boundary-layer mode** $|\lambda_3| \sim (\sqrt{\gamma}\xi)^{-1}$ and introducing an **exact local interpoint nonlocal availability flux** $P_x^{\mathrm{nl}} = -(1-\gamma)\xi^2 M_1^{-1}w\,\partial_x\dot{w}$.

---

## 2. Candidate Comparison & Novelty Screening Summary

Full equations, folder comparisons, and 2020–2026 external citations are documented in [`gap_map.md`](gap_map.md) and [`candidates.md`](candidates.md).

| Rank | Candidate | Key Contribution | Closest Prior Art (Folder & 2020–2026 External) | Verdict |
|---:|---|---|---|---|
| **1** | **C1: Variational Two-Phase Integral Nonlocal Generalized Thermoelasticity on Bounded Domains** | Solves `Gap 8` + `Q. R1, R2, R6`: proves Form A/B free-energy reciprocity, derives exact interpoint nonlocal availability flux $P_x$ and Robin CBCs, resolves 6-wave boundary-layer mechanics and $\gamma\to 0^+$ singular breakdown. | Eringen 1974 (Pos 38, bulk Fourier); Romano et al. 2017 (Pos 47, static beams); Barak & Gupta 2023 (Pos 151/152, naive Form A without CBCs); Anh & Vinh Mar 2026 (`10.1007/s00419-026-03052-1`, isothermal SH only); Barretta et al. 2018/2019 (quasi-static beams). | **CLEAR GO** |
| **2** | **C2: Complete Positive-Real Passivity & 3D Availability Functional for the 3-Lag / MGT Template** | Solves `Gap 1 & Gap 2` + `Q. R8`: proves $\operatorname{Re} G(-i\omega)\ge 0 \iff k + k^*(\tau_v-\tau_q)\ge 0,\, k\tau_T\tau_q\ge 0$ and constructs explicit 3D anisotropic availability functionals for all $\varepsilon > 0$. | Quintanilla & Racke 2008 (Pos 52, uncoupled $\varepsilon=0$); Quintanilla 2019 (Pos 51, MGT only); El-Karamany & Ezzat 2016 (Pos 150, uniqueness); Chiriţă & Zampoli 2024 (`10.1080/01495739.2023.2285791`). | **GO (Runner-Up)** |
| **3** | **C3: Kapitza Interfacial Relaxation Entropy & Mode-Interference Apportionment** | Solves `Gap 4 & Gap 5`: derives non-negative interfacial entropy generation for lagged heat laws and separates bulk mode interference from Kapitza dissipation. | Sinha & Elsibai 1997 (Pos 48); Jiang et al. 2024 (`10.1016/j.compstruct.2024.118675`); Sept 2026 GaAs/AlGaAs DPL heterojunction (`S0735193326022566`). | **CONDITIONAL GO** |
| **4** | **C4: Bounded Retarded Klein–Gordon Space-Time Nonlocal Thermoelasticity** | Formulates causal retarded Bessel-kernel CBCs on $[0,L]$ extending Lazar & Agiasofitou 2022 (Pos 9). | Crowded 2025–2026 *unbounded differential* KG thermoelasticity surge (`10.1007/s00339-025-08329-w`; `10.1007/s10973-026-15539-8`). | **DEFER** |

---

## 3. Non-Circular Pilot Verification Results (`pilot/`)

All symbolic and numerical claims for **Candidate C1** (and the passivity lemma of **C2**) are verified in [`pilot/pilot.py`](pilot/pilot.py) and [`pilot/test_pilot.py`](pilot/test_pilot.py) (`7/7` automated `pytest` tests passing; exact numerical outputs in [`pilot/data.json`](pilot/data.json)):

| Verification Test | Method / Benchmark | Quantitative Result (`pilot/data.json`) | Figure |
|---|---|---|---|
| **1. Symbolic Free-Energy & Passivity Proofs** | SymPy exact PDE/flux differentiation & complex algebra | Availability balance residual `== 0` identically; $\operatorname{Re} G(-i\omega) = \frac{k + k^*(\tau_v-\tau_q) + k\tau_T\tau_q\omega^2}{1+\omega^2\tau_q^2}$ verified; mismatched Form A leftover power $\ne 0$ isolated. | — |
| **2. Non-Circular Cross-Check Against Direct Integral Solver** | 6-wave differential + Robin-CBC solver vs. independent Legendre spectral-Galerkin Fredholm integral solver ($L=1, \omega=2.2, \gamma=0.35, \xi=0.08, \varepsilon=0.08$, MGT) | Relative $L^\infty$ agreement: **`4.75e-15`** on $\hat{u}(x)$, **`4.88e-13`** on $\hat{\sigma}(x)$. | [`fig1_integral_residual.png`](pilot/fig1_integral_residual.png) |
| **3. Exact Integral Constitutive Law Residual on $[0,L]$** | Substituting computed fields directly into exact analytical convolution $\int_0^L K_\xi(x,x')\phi(x')\,dx'$ | 6-wave + Robin CBC: **`7.41e-16`** (machine zero). Literature's naive 4-wave differential shortcut: **`2.23e-1` (`22.3%` boundary error)**. | [`fig1_integral_residual.png`](pilot/fig1_integral_residual.png) |
| **4. Conservative GN-II Spatial Availability Flux Constancy** | Spatial drift $\max_x |\langle P_x(x)\rangle - \langle P_x(0)\rangle|$ across driven slab | Variational V1: **`1.67e-16`**; Variational V2 (repaired Form A): **`2.22e-16`**; V1 omitting nonlocal flux $P_x^{\mathrm{nl}}$: **`4.71e-3`**; Literature mismatched Form A: **`2.96e-3`**. | [`fig2_reciprocity_energy_conservation.png`](pilot/fig2_reciprocity_energy_conservation.png) |
| **5. High-Frequency Cutoff Damping & Singular $\gamma\to 0^+$ Limit** | Frequency sweep $\omega/\omega^*\in[0.03, 40]$ and mixture sweep $\gamma\in[10^{-4}, 0.9]$ | V1 vs. V2 vs. Form A diverge by $>10\times$ in $Q^{-1}(\omega)$ above $\omega^*$; at $\gamma=10^{-4}$, $|\lambda_3|\xi = 98.39$ matches $\gamma^{-1/2} = 100.0$ within `1.61%` while boundary strain jump grows $\propto\gamma^{-1/2}$. | [`fig3_dispersion_and_damping_cutoff.png`](pilot/fig3_dispersion_and_damping_cutoff.png), [`fig4_singular_mixture_limit.png`](pilot/fig4_singular_mixture_limit.png) |

---

## 4. Scope-Checked Target Journals & Next Steps Toward Manuscript

Scope-appropriate venues for a full mathematical + mechanics article developing **Candidate C1** (extending 1D slab/half-space results to 2D oblique P-SV reflection/Rayleigh waves and welded bimaterial interfaces):
- ***Proceedings of the Royal Society A*** (directly published Vinh & Anh 2024 `480:20230814` on nonlocal wave well-posedness and Green & Naghdi 1991 `432:171`);
- ***International Journal of Engineering Science*** (published Eringen 1972/1974, Romano & Barretta 2017, Fernández-Sáez et al. 2017, Barretta et al. 2018);
- ***Journal of Elasticity*** or ***Zeitschrift für angewandte Mathematik und Physik (ZAMP)*** (published Green & Lindsay 1972, Green & Naghdi 1993, Hue–Vinh–Anh Jan 2026);
- ***Journal of Thermal Stresses*** or ***Archive of Applied Mechanics*** (published Anh & Vinh Mar 2026 `96:59`).

*(Scope fit does not imply acceptance probability or independent peer-review endorsement; see [`unverified.md`](unverified.md) for all epistemic boundaries.)*

## 5. Deliverable Index in `paper/drive-analysis/`

- [`papers_manifest.csv`](papers_manifest.csv) — 152/152 manifest (`100% done`).
- [`paper_table.csv`](paper_table.csv) & [`paper_table.md`](paper_table.md) — 15-column full-paper extractions for all 152 Drive PDFs.
- [`review_map.md`](review_map.md) — Complete 157-page section-by-section map of `review paper.pdf`.
- [`gap_map.md`](gap_map.md) — Thematic clustering, 6 corpus contradictions, and 14-gap 2026 screening matrix.
- [`candidates.md`](candidates.md) — Mathematical specifications and ranking of Candidates C1–C4.
- [`unverified.md`](unverified.md) — Verification ledger and explicit epistemic limits.
- [`pilot/`](pilot/) — `pilot.py`, `test_pilot.py`, `data.json`, `README.md`, `requirements.txt`, and `fig1`–`fig4` PNGs.
- [`drive-analysis.zip`](drive-analysis.zip) — Clean distributable archive of all deliverables above (zero Drive PDFs).
