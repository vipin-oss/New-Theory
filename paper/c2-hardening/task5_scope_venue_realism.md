# Task 5: Scope & Venue Realism

## 1. Realistic Assessment of Original Candidate C2 Against Target Venues

If Candidate C2 were submitted in its original form from `paper/drive-analysis/candidates.md` (claiming novelty for the bulk passivity condition $K + (\tau_v - \tau_q)K^* \succeq 0$, the 3D coupled Lyapunov functional, the Lumer–Phillips contraction semigroup proof, and the $\tau_T > 0$ vs. $\tau_T = 0$ wavefront classification), how would specialist referees at the target journals respond?

| Target Venue | Expected Referee Verdict on Original C2 | Why? |
| :--- | :--- | :--- |
| ***Mathematics and Mechanics of Solids*** (SAGE) | **Desk-Reject / Immediate Reject** | R. Quintanilla (Associate Editor / leading contributor, *Math. Mech. Solids* 24:4020–4031, 2019) and S. Chiriţă (*Math. Mech. Solids*, 2023) published the exact bulk MGT/TPL Lyapunov functional, 5-field contraction semigroup, and fading-memory passivity conditions in this very journal. |
| ***International Journal of Heat and Mass Transfer*** (Elsevier) | **Desk-Reject / Immediate Reject** | Quintanilla & Racke (2008, *IJHMT* 51:24–29), Fabrizio & Lazzari (2014, *IJHMT* 74:484–489), and Chiriţă, D'Apice & Zampoli (2016, *IJHMT* 102:226–232) were all published in *IJHMT* and already contain Eqs. (2.1), (2.4), (2.6) and the fading-memory Second-Law derivation. |
| ***Journal of Thermal Stresses*** (Taylor & Francis) | **Reject for Lack of Novelty** | Quintanilla (2009, *JTS* 32:1270–1278), Zampoli & Landi (2017, *JTS* 40:108–120), and Chiriţă (2018, 2024, 2025, *JTS*) have extensively covered bulk TPL stability and structural stability in *JTS*. |
| ***ZAMP*** / ***Applicable Analysis*** | **Reject** | Liu, Quintanilla & Wang (2022, *Appl. Anal.* 101:5376–5385) and Muñoz Rivera, Ochoa Ochoa & Quintanilla (2024, *Appl. Math. Optim.* 89:51) already proved coupled TPL contraction semigroup generation and analyticity. |
| ***Mechanics Research Communications*** / ***C. R. Mécanique*** | **Reject unless pivoted or sharply narrowed** | Even for a 5–6 page short communication, reproducing the Quintanilla–Racke (2008) / Quintanilla (2019) functional without a genuinely new theorem (such as the imperfect interface theory of C3 or the bounded-domain Poincaré stabilization dichotomy of Counterexample 1) would be flagged by any specialist reviewer. |

---

## 2. What Makes a Short Note (5–8 Pages) Referee-Proof at *Mech. Res. Commun.*, *J. Therm. Stresses*, *Wave Motion*, or *ZAMP*?

Our audit identifies **two distinct, publication-grade short-note configurations** that survive hostile refereeing:

### Option A (Primary Recommended Pivot: C2+C3 Synthesis, 6–8 pages)
* **Core Focus**: **Passivity-Consistent Kapitza–Spring Imperfect Interfaces in Three-Phase-Lag and MGT Thermoelasticity: Interfacial Lyapunov Stability, the $\tau_q^- \ne \tau_q^+$ Multiplier Obstruction, and Exact Scattering Unitarity.**
* **Why it is strong enough for *Wave Motion*, *Journal of Thermal Stresses*, *ZAMP*, or *Mechanics Research Communications***:
  1. **Genuine Mathematical Novelty**: Identifies and resolves a sharp, previously unnoticed structural obstruction — when two TPL/MGT media with distinct relaxation times $\tau_q^- \ne \tau_q^+$ meet at an interface $\Gamma$, the Quintanilla (2019) bulk multiplier $(1 + \tau_q^\pm\partial_t)$ fails to match across $\Gamma$ even for a welded interface (Counterexample 4, Eq. 3.10). We prove:
     - For $\tau_q^- = \tau_q^+ = \tau_q$, the exact 3D time-domain Lumer–Phillips contraction semigroup on $\Omega^- \cup \Omega^+$ with a Kapitza–spring interface $\Gamma$, including the explicit interfacial energy $\mathcal{E}_\Gamma(t)$ and dissipation rate $\mathcal{D}_\Gamma(t) \ge 0$.
     - For arbitrary $\tau_q^- \ne \tau_q^+$, how to restore time-domain Lyapunov contractivity via an Extended Irreversible Thermodynamics (EIT) state-space formulation (or a symmetric second-order cross-filter $(1+\tau_q^-\partial_t)(1+\tau_q^+\partial_t)$), AND how the physical time-harmonic Poynting–heat-flux vector $\mathbf{S}_{\text{avg}}$ bypasses the $(1-\mathrm{i}\omega\tau_q^\pm)$ multiplier to yield an unconditional scattering unitarity theorem $R_P + R_{SV} + R_T + T_P + T_{SV} + T_T + D_{\text{bulk}} + D_{\text{int}} = 1$.
  2. **Zero External Data Required**: Validated by symbolic computer-algebra proofs and a self-contained 1D/2D scattering solver verifying unitarity to $< 10^{-14}$.

### Option B (Narrowed-Scope Bulk Fallback: C2 Sharp Dichotomy Note, 5–6 pages)
* **Core Focus**: **Whole-Space Passivity versus Bounded-Domain Exponential Stability in Three-Phase-Lag Thermoelasticity: The Poincaré Stabilization Cutoff and High-Frequency Asymptotics.**
* **Why it is strong enough for *Mechanics Research Communications* or *Comptes Rendus Mécanique*** (if framed explicitly as a refinement/complement to Quintanilla & Racke 2008, Chiriţă et al. 2016, and Quintanilla 2019):
  1. **Honest Prior-Art Attribution**: Explicitly credits Quintanilla & Racke (2008), Chiriţă et al. (2016), Quintanilla (2019), and Liu, Quintanilla & Wang (2022) for the bulk Lyapunov functional and the constitutive passivity condition $k + k^*(\tau_v - \tau_q) \ge 0$.
  2. **New Mathematical Theorem**: Proves that when $\tau_T > 0$, constitutive passivity ($k + k^*(\tau_v - \tau_q) \ge 0$) is **strictly stronger** than bounded-domain exponential stability: derives the exact critical Dirichlet eigenvalue $\mu_{\text{crit}}(\varepsilon)$ (Eqs. 3.4 & 3.7) above which fourth-order thermal-rate dissipation $\tau_T\tau_q k|\nabla\dot{\theta}|^2$ stabilizes all modes on $\Omega$ via Poincaré's inequality even when $k + k^*(\tau_v - \tau_q) < 0$, and contrasts this with the $(1,1,1)$ vs. $(2,1,1)$ passivity breakdown on real physical materials (Table 4.1).
