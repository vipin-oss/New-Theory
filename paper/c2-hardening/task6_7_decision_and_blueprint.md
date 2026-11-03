# Tasks 6 & 7: Kill / Pivot / Proceed Decision and Next-Step Blueprints

---

## Task 6: Explicit Decision Verdict

### Verdict on Candidate C2 as Originally Formulated: **PIVOT (Kill Standalone Bulk Passivity/Semigroup Claim; Pivot to C2+C3 Imperfect-Interface Synthesis or Narrowed Poincaré-Cutoff Note)**

1. **Why Original Candidate C2 Cannot Proceed Unchanged**:
   - **Fatal Prior-Art Overlap on Core Bulk Claims (Task 1)**:
     - The exact first-order-in-$\tau_q$ 3-lag bulk PDE, the stability condition $k + k^*(\tau_v - \tau_q) > 0$, $k\tau_T\tau_q \ge 0$, the 3D time-domain Lyapunov functional $F(t)$, and the parabolic infinite-propagation-speed classification for $\tau_T > 0$ were published verbatim by **Quintanilla & Racke (2008, *Int. J. Heat Mass Transfer* 51:24–29, Eqs. 1.1, 2.1, 2.4, 2.6)** (`Quintanilla_2008.pdf` in the Google Drive corpus).
     - The fading-memory / Second-Law cosine-transform derivation of $\operatorname{Re} G_{ij}(-\mathrm{i}\omega) \succeq 0$ for 3D anisotropic TPL heat conduction was published by **Chiriţă, D'Apice & Zampoli (2016, *Int. J. Heat Mass Transfer* 102:226–232)** and **Chiriţă & D'Apice (2023, *Math. Mech. Solids*)**.
     - The 3D anisotropic thermoelastic coupling via the mechanical filter $\hat{u}_i = u_i + \tau_q\dot{u}_i$, the 5-component Hilbert-space inner product, the Lumer–Phillips contraction semigroup theorem, and Routh–Hurwitz instability for $k + k^*(\tau_v - \tau_q) < 0$ were published by **Quintanilla (2019, *Math. Mech. Solids* 24:4020–4031)** (`Quintanilla_2019.pdf` in the Google Drive corpus), **D'Apice, Chiriţă & Zampoli (2016, *Arch. Mech.* 68:371–393)**, **Liu, Quintanilla & Wang (2022, *Appl. Anal.* 101:5376–5385)**, and **Muñoz Rivera, Ochoa Ochoa & Quintanilla (2024, *Appl. Math. Optim.* 89:51)**.
   - **Technical Corrections Identified in the C2 Sketch (Tasks 2 & 3)**:
     - Leaving the mechanical displacement $u_i$ unfiltered while filtering $\theta$ by $(1+\tau_q\partial_t)$ (as sketched in `candidates.md`) leaves a non-zero third-order coupling residual (Eq. 2.17 / Counterexample 2).
     - The 5-field energy norm degenerates to a seminorm in the Tzou DPL / Lord–Shulman limit $K^*_{ij} \to 0$ and at the critical MGT boundary $K_{ij} + (\tau_v - \tau_q)K^*_{ij} = 0, \tau_T = 0$ (Counterexample 3).
     - When $\tau_T > 0$, violating $k + k^*(\tau_v - \tau_q) \ge 0$ does **not** destabilize bounded domains whose fundamental Dirichlet eigenvalue exceeds $\xi_{\text{crit}}^2(\varepsilon)$ (Counterexample 1).

2. **Why the Replacement Direction Survives the Check That Killed C2**:
   - **Primary Replacement (Blueprint A — C2+C3 Synthesis on Passivity-Consistent Imperfect Interfaces in TPL/MGT Thermoelasticity)**:
     None of the prior-art papers (Quintanilla & Racke 2008; Chiriţă et al. 2016; Quintanilla 2019; Liu et al. 2022; Muñoz Rivera et al. 2024; Sinha & Elsibai 1997; Akbarzadeh & Pasini 2014; Barak et al. 2023) address:
     1. The **3D time-domain Lyapunov functional and Lumer–Phillips contraction semigroup** for a bimaterial TPL/MGT thermoelastic body with a **Kapitza–spring imperfect interface** $\Gamma$ ($\llbracket u_i\rrbracket \ne 0$, $\llbracket\theta\rrbracket \ne 0$),
     2. The **bimaterial phase-lag mismatch obstruction ($\tau_q^- \ne \tau_q^+$)** showing that the Quintanilla (2019) multiplier $(1+\tau_q^\pm\partial_t)$ cannot be matched across $\Gamma$ when $\tau_q^- \ne \tau_q^+$, and its exact resolution via a symmetric cross-filter / frequency-domain Poynting formulation,
     3. The **exact scattering unitarity identity** $R_P + R_{SV} + R_T + T_P + T_{SV} + T_T + D_{\text{bulk}} + D_{\text{int}} = 1$ with closed-form interfacial absorption $D_{\text{int}}(\omega) \ge 0$.
   - **Secondary Replacement (Blueprint B — Narrowed-Scope Bulk Short Note on the Poincaré Stabilization Cutoff and $(1,1,1)$-vs-$(2,1,1)$ Passivity Breakdown)**:
     If a purely bulk note is preferred, narrowing C2 to the newly discovered **Poincaré stabilization cutoff $\mu_1(\Omega) > \xi_{\text{crit}}^2(\varepsilon)$** (where bounded domains remain exponentially stable despite violating constitutive passivity $k + k^*(\tau_v - \tau_q) \ge 0$) + the **systematic failure of the $(2,1,1)$ hyperbolic TPL model under $\tau_T \le \tau_q/2$** properly cites Quintanilla & Racke (2008), Chiriţă et al. (2016), and Quintanilla (2019) as its starting point and proves genuinely new spectral and asymptotic results.

---

## Task 7: Next-Step Blueprints

We provide complete, ready-to-execute blueprints for **both** the Primary Recommended Pivot (**Blueprint A: C2+C3 Imperfect-Interface Synthesis**) and the Narrowed-Scope Bulk Fallback (**Blueprint B: C2 Poincaré-Cutoff & Wavefront Audit Note**).

---

### Blueprint A (Primary Recommendation): C2+C3 Synthesis Short Note (6–8 Pages)

#### 1. Working Title
> **Passivity-Consistent Imperfect Interfaces in Three-Phase-Lag and Moore–Gibson–Thompson Thermoelasticity: Interfacial Lyapunov Stability, the Phase-Lag Mismatch Obstruction, and Scattering Unitarity**

#### 2. Target Venues
* **Primary**: *Wave Motion* (Elsevier), *Journal of Thermal Stresses* (Taylor & Francis), or *Mechanics Research Communications* (Elsevier).
* **Secondary**: *Zeitschrift für angewandte Mathematik und Physik (ZAMP)* (Birkhäuser).

#### 3. Draft Abstract (~150 Words)
> While bulk well-posedness and thermodynamic passivity of three-phase-lag (TPL) and Moore–Gibson–Thompson (MGT) thermoelasticity are well established via the $(1+\tau_q\partial_t)$ multiplier method, realistic layered heterostructures and nanocomposites exhibit interfacial mechanical compliance and Kapitza thermal contact resistance. Here we formulate passivity-consistent imperfect transmission conditions across a material interface $\Gamma$ separating two anisotropic TPL/MGT thermoelastic media. First, we uncover a fundamental structural obstruction: when the adjacent media possess distinct heat-flux relaxation times ($\tau_q^- \ne \tau_q^+$), the standard $(1+\tau_q^\pm\partial_t)$-filtered Lyapunov functional fails to cancel interfacial power terms even for a perfectly welded contact. Second, for matched relaxation times ($\tau_q^- = \tau_q^+$) and memory-consistent Kapitza–spring jump laws, we construct an explicit Hilbert-space inner product on $\Omega^- \cup \Omega^+$ with interfacial energy storage $\mathcal{E}_\Gamma$ and prove contraction $C_0$-semigroup generation via the Lumer–Phillips theorem. Third, for arbitrary $\tau_q^- \ne \tau_q^+$, we prove that the unfiltered time-harmonic Poynting–heat-flux vector satisfies an exact scattering unitarity identity $R + T + D_{\text{bulk}} + D_{\text{int}} = 1$, verified numerically to machine precision ($< 10^{-14}$).

#### 4. Exact Mathematical Statements to Be Proved

* **Proposition 1 (The Bimaterial Phase-Lag Mismatch Obstruction for $\tau_q^- \ne \tau_q^+$)**:
  *Hypotheses*: Let $\Omega = \Omega^- \cup \Gamma \cup \Omega^+$ be a composite domain with smooth interface $\Gamma$, where $\Omega^\pm$ are governed by the coupled TPL/MGT thermoelastic system (2.1)–(2.4) with bulk parameters $(\rho^\pm, C_{ijkl}^\pm, \beta_{ij}^\pm, c_E^\pm, K_{ij}^\pm, K_{ij}^{*\pm}, \tau_q^\pm, \tau_T^\pm, \tau_v^\pm)$ satisfying the strict bulk passivity conditions $K_{ij}^\pm + (\tau_v^\pm - \tau_q^\pm)K_{ij}^{*\pm} \succeq 0$ and $\tau_T^\pm\tau_q^\pm K_{ij}^\pm \succeq 0$.
  *Conclusion*: The sum of the subdomain Quintanilla–Racke filtered energies $\mathcal{E}_{\text{bulk}}(t) = \mathcal{E}^-(t) + \mathcal{E}^+(t)$ (defined via $\hat{u}_i^\pm = (1+\tau_q^\pm\partial_t)u_i^\pm$) satisfies
  $$\frac{d}{dt}\mathcal{E}_{\text{bulk}}(t) = -\mathcal{D}_{\text{bulk}}^-(t) - \mathcal{D}_{\text{bulk}}^+(t) + \mathcal{P}_\Gamma(t),$$
  where, under standard continuity of traction $\sigma_{ij}^- n_j = \sigma_{ij}^+ n_j = t_i$ and normal heat flux $q_n^- = q_n^+ = q_n$, the interfacial power functional $\mathcal{P}_\Gamma(t)$ vanishes for all welded states ($\llbracket u_i\rrbracket = 0$, $\llbracket\theta\rrbracket = 0$) **if and only if $\tau_q^- = \tau_q^+$**. When $\tau_q^- \ne \tau_q^+$, $\mathcal{P}_\Gamma^{\text{welded}}(t)$ is given by the non-zero differential form (3.10) of order 3, which is sign-indeterminate.

* **Theorem 1 (Time-Domain Contraction Semigroup for Kapitza–Spring Imperfect Interfaces)**:
  *Hypotheses*: Assume $\tau_q^- = \tau_q^+ = \tau_q > 0$, strict bulk passivity and coercivity (2.23) in $\Omega^\pm$, and let $\Gamma$ be governed by the imperfect mechanical spring-dashpot and thermal Kapitza-displacement jump conditions:
  $$\sigma_{ij}^- n_j = \sigma_{ij}^+ n_j = K^{\text{mech}}_{ik}\bigl[\!\bigl[u_k\bigr]\!\bigr] + \eta^{\text{mech}}_{ik}\bigl[\!\bigl[\dot{u}_k\bigr]\!\bigr], \qquad -q_n^- = -q_n^+ = \frac{1}{T_0}\Bigl(H_\vartheta\bigl[\!\bigl[\vartheta\bigr]\!\bigr] + H_\theta\bigl[\!\bigl[\theta\bigr]\!\bigr]\Bigr) \quad \text{on }\Gamma,$$
  with symmetric matrices $K^{\text{mech}} \succ 0$, $\eta^{\text{mech}} \succeq 0$ and scalars $H_\vartheta > 0$, $H_\theta \ge 0$.
  *Conclusion*: On the composite Hilbert space $\mathcal{H}_\Gamma$ equipped with the total energy norm
  $$\mathcal{E}_{\text{total}}(t) = \mathcal{E}_{\text{bulk}}^-(t) + \mathcal{E}_{\text{bulk}}^+(t) + \frac{1}{2}\int_\Gamma \Bigl(K^{\text{mech}}_{ik}\bigl[\!\bigl[\hat{u}_i\bigr]\!\bigr]\overline{\bigl[\!\bigl[\hat{u}_k\bigr]\!\bigr]} + \frac{H_\vartheta}{T_0^2}\bigl|\bigl[\!\bigl[\hat{\vartheta}\bigr]\!\bigr]\bigr|^2\Bigr)\,d\Gamma,$$
  the composite evolution operator $\mathcal{A}_\Gamma$ is densely defined, satisfies $0 \in \varrho(\mathcal{A}_\Gamma)$, and obeys the exact dissipation law
  $$\frac{d}{dt}\mathcal{E}_{\text{total}}(t) = -\mathcal{D}_{\text{bulk}}^-(t) - \mathcal{D}_{\text{bulk}}^+(t) - \int_\Gamma \Bigl(\eta^{\text{mech}}_{ik}\bigl[\!\bigl[\dot{\hat{u}}_i\bigr]\!\bigr]\overline{\bigl[\!\bigl[\dot{\hat{u}}_k\bigr]\!\bigr]} + \frac{H_\theta}{T_0^2}\bigl|\bigl[\!\bigl[\hat{\theta}\bigr]\!\bigr]\bigr|^2\Bigr)\,d\Gamma \le 0.$$
  Hence $\mathcal{A}_\Gamma$ generates a contraction $C_0$-semigroup on $\mathcal{H}_\Gamma$.

* **Theorem 2 (Unconditional Frequency-Domain Poynting Passivity and Scattering Unitarity for Arbitrary $\tau_q^- \ne \tau_q^+$)**:
  *Hypotheses*: Let $\Omega^-$ and $\Omega^+$ have **arbitrary** (possibly distinct) phase lags $\tau_q^- \ne \tau_q^+$ satisfying bulk passivity $\operatorname{Re} G_{ij}^\pm(-\mathrm{i}\omega) \succeq 0$ at frequency $\omega \in \mathbb{R}\setminus\{0\}$, and let $\Gamma$ obey general linear impedance/admittance jump relations
  $$\tilde{\sigma}_{ij}^- n_j = \tilde{\sigma}_{ij}^+ n_j = Z^{\text{mech}}_{ik}(-\mathrm{i}\omega)\bigl[\!\bigl[\tilde{v}_k\bigr]\!\bigr], \qquad -\tilde{q}_n^- = -\tilde{q}_n^+ = \frac{1}{T_0}Y_{\text{th}}(-\mathrm{i}\omega)\bigl[\!\bigl[\tilde{\theta}\bigr]\!\bigr] \quad \text{on }\Gamma,$$
  where $\tilde{v}_k = -\mathrm{i}\omega\tilde{u}_k$.
  *Conclusion*: The physical time-averaged thermoelastic energy flux $\mathbf{S}_{\text{avg}}(\mathbf{x};\omega) = \frac{1}{2}\operatorname{Re}\bigl(-\tilde{\boldsymbol{\sigma}}\cdot\overline{\tilde{\mathbf{v}}} + \frac{1}{T_0}\tilde{\mathbf{q}}\overline{\tilde{\theta}}\bigr)$ satisfies the exact bulk divergence identity $\nabla\cdot\mathbf{S}_{\text{avg}} = -\frac{1}{2T_0}(\operatorname{Re} G_{ij}^\pm(-\mathrm{i}\omega))\tilde{\theta}_{,i}\overline{\tilde{\theta}_{,j}} \le 0$ in $\Omega^\pm$ **without any $(1-\mathrm{i}\omega\tau_q^\pm)$ multiplier**, and its normal jump across $\Gamma$ is
  $$\bigl[\!\bigl[\mathbf{S}_{\text{avg}}\cdot\mathbf{n}\bigr]\!\bigr]_\Gamma = -D_{\text{int}}(\omega) := -\frac{1}{2}\Bigl[\bigl(\operatorname{Re} Z^{\text{mech}}_{ik}(-\mathrm{i}\omega)\bigr)\bigl[\!\bigl[\tilde{v}_k\bigr]\!\bigr]\overline{\bigl[\!\bigl[\tilde{v}_i\bigr]\!\bigr]} + \frac{\operatorname{Re} Y_{\text{th}}(-\mathrm{i}\omega)}{T_0^2}\bigl|\bigl[\!\bigl[\tilde{\theta}\bigr]\!\bigr]\bigr|^2\Bigr] \le 0$$
  if and only if $\operatorname{Re} Z^{\text{mech}}(-\mathrm{i}\omega) \succeq 0$ and $\operatorname{Re} Y_{\text{th}}(-\mathrm{i}\omega) \ge 0$. Consequently, any plane-wave or waveguide scattering problem satisfies the exact unitarity balance $R + T + D_{\text{bulk}}^- + D_{\text{bulk}}^+ + D_{\text{int}} = 1$.

#### 5. Section-by-Section Outline & Page Budget (Total: 7 Pages)
1. **Section 1: Introduction & Prior-Art Context** (1.0 page) — Review of TPL/MGT bulk stability (Quintanilla & Racke 2008; Chiriţă et al. 2016; Quintanilla 2019; Liu et al. 2022) and imperfect interface wave scattering (Sinha & Elsibai 1997; Akbarzadeh & Pasini 2014; Barak et al. 2023).
2. **Section 2: Bulk Passivity and the Bimaterial Phase-Lag Mismatch Obstruction** (1.5 pages) — Proof of Proposition 1 showing why $\tau_q^- \ne \tau_q^+$ breaks the filtered time-domain multiplier at an interface.
3. **Section 3: Time-Domain Interfacial Lyapunov Functional and Contraction Semigroup** (2.0 pages) — Proof of Theorem 1 via Lumer–Phillips and Lax–Milgram on $\Omega^-\cup\Gamma\cup\Omega^+$, plus the cross-filtered/EIT resolution for $\tau_q^- \ne \tau_q^+$.
4. **Section 4: Unconditional Frequency-Domain Poynting Unitarity** (1.5 pages) — Proof of Theorem 2 and derivation of the scattering matrix and interfacial absorption $D_{\text{int}}(\omega)$.
5. **Section 5: Physical Grounding & Numerical Verification** (1.0 page) — Concrete Si/Cu and NaF bimaterial interface benchmarks verifying $S_{\text{left}} - S_{\text{right}} = D_{\text{bulk}}^- + D_{\text{bulk}}^+ + D_{\text{int}}$ to $6.4 \times 10^{-15}$.

---

### Blueprint B (Narrowed-Scope Bulk Fallback): C2 Sharp Dichotomy Short Note (5–6 Pages)

If a purely bulk note is preferred without introducing interfaces, C2 must be narrowed to the newly discovered **Poincaré stabilization cutoff vs. constitutive passivity dichotomy** (Counterexample 1) and the **$(1,1,1)$-vs-$(2,1,1)$ physical passivity audit** (Task 4).

#### 1. Working Title
> **Whole-Space Passivity versus Bounded-Domain Exponential Stability in Three-Phase-Lag Thermoelasticity: Poincaré Cutoff Wavenumbers and High-Frequency Asymptotics**

#### 2. Target Venues
* **Primary**: *Mechanics Research Communications* (Elsevier) or *Comptes Rendus Mécanique*.
* **Secondary**: *Journal of Thermal Stresses* (Taylor & Francis).

#### 3. Draft Abstract (~150 Words)
> In three-phase-lag (TPL) heat conduction and thermoelasticity, the inequality $k + k^*(\tau_v - \tau_q) \ge 0$ (together with $k\tau_T\tau_q \ge 0$) is widely regarded as the necessary and sufficient threshold for thermodynamic compatibility and exponential stability (Quintanilla & Racke, 2008; Chiriţă et al., 2016; Liu et al., 2022). In this note, we prove a sharp dichotomy between whole-space constitutive passivity and bounded-domain modal stability whenever the temperature-gradient phase lag $\tau_T > 0$. While violating $k + k^*(\tau_v - \tau_q) \ge 0$ always induces long-wavelength instability on $\mathbb{R}^d$, fourth-order thermal-rate dissipation $\tau_T\tau_q k|\nabla\dot{\theta}|^2$ stabilizes all spatial modes above an explicit critical wavenumber $\xi_{\text{crit}}^2(\varepsilon)$. Consequently, any bounded domain $\Omega$ whose fundamental Dirichlet eigenvalue satisfies $\mu_1(\Omega) > \xi_{\text{crit}}^2(\varepsilon)$ remains exponentially stable despite violating constitutive passivity. We derive the exact $\varepsilon$-coupled Hopf bifurcation locus, establish the five-branch high-frequency ($\xi\to\infty$) Puiseux asymptotics, and audit published physical parameter sets for Cu, Si, cryogenic NaF, and biological tissue.

#### 4. Exact Mathematical Statements to Be Proved
* **Theorem 1 (Whole-Space Passivity vs. Bounded-Domain Poincaré Cutoff for $\tau_T > 0$)**: Proves that for $k + k^*(\tau_v - \tau_q) < 0$ and $\tau_T > 0$, the uncoupled and coupled TPL systems on a bounded Dirichlet domain $\Omega$ are exponentially stable if and only if $\mu_1(\Omega) > \xi_{\text{crit}}^2(\varepsilon)$ (Eqs. 3.4 & 3.7), where the Hopf frequency $\omega_{\text{Hopf}}^2 = \frac{k^*(\tau_q - \tau_v) - k}{k\tau_T\tau_q}$ is independent of the thermoelastic coupling $\varepsilon > 0$.
* **Theorem 2 (Complete 5-Branch High-Frequency Puiseux Asymptotics)**: Establishes Eqs. (2.29)–(2.36) for all five dispersion branches in both the regularized parabolic regime ($\tau_T > 0$, proving $\kappa_\infty = \frac{\tau_q}{\tau_T}\kappa_{\infty,\text{Fourier}}$) and the hyperbolic MGT regime ($\tau_T = 0$).
* **Proposition 1 (Incompatibility of the $(2,1,1)$ Hyperbolic TPL Model with $\tau_T \le \tau_q/2$)**: Proves Eq. (4.1) and demonstrates via Table 4.1 & Table 4.2 that standard physical parameter sets for Cu, Si, NaF, and biological tissue satisfy $(1,1,1)$ passivity but violate $(2,1,1)$ passivity.
