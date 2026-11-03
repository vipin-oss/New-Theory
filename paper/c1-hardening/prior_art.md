# Task 2: Prior-Art & Novelty Audit for Candidate C1

## 1. Executive Summary of Prior-Art Audit

We conducted a full-text and web-search audit to test whether any component of **Candidate C1** (*Thermodynamically Consistent Two-Phase Nonlocal Thermoelasticity with Integral-Consistent Robin Boundary Conditions: Variants V1 and V2*) has already been published between 1974 and 2026.

### Core Findings
1. **Eringen (1974)** (*Int. J. Eng. Sci.* 12:1063–1077) derived a symmetric integral nonlocal thermoelastic constitutive pair (his Eqs. 4.19–4.22) from a quadratic nonlocal free-energy functional on an unbounded/general domain using a **purely nonlocal ($\gamma = 0$) kernel**. However, Eringen (1974) did **not** formulate the two-phase local/nonlocal kernel ($\gamma \in (0,1)$), did **not** convert the integral law to a differential BVP with Robin Constitutive Boundary Conditions (CBCs) on bounded/half-space domains, did **not** formulate Variant V1 (two-phase elastic convolution with local thermal coupling) or the master two-phase family $\Psi_\lambda[\varepsilon,\theta]$, and did **not** analyze the thermodynamic failure of the post-1983 differential Form A approximation paired with local entropy.
2. **Fernández-Sáez, Zaera, Loya & Reddy (2016)** (*Int. J. Eng. Sci.* 99:107–116) and **Romano, Barretta, Diaco & Marotti de Sciarra (2017)** (*Int. J. Mech. Sci.* 121:151–156) derived the integral-to-differential Robin CBCs exclusively for **isothermal, static 1D structural mechanics (Euler–Bernoulli beams and bars)**. Neither paper considers temperature $\theta$, entropy $\eta$, Helmholtz free energy $\Psi[\varepsilon,\theta]$, Clausius–Duhem dissipation, non-Fourier heat conduction, or thermoelastic wave propagation.
3. **2024–2026 Elastic Wave Papers** — **Pham & Vu (2024)** (*Mech. Res. Commun.* 137:104266), **Nobili & Pramanik (2025)** (*Mech. Mater.* 202:105242), **Pramanik, Nobili & Manna (2026)** (*Int. J. Non-Linear Mech.* 180:105302), and the Hanoi-group wave papers **Anh & Vinh (2026)**, **Hue et al. (2026)**, and **Tran et al. (Aug 2026)** — are all **purely isothermal elastodynamic/hyperelastic wave papers** with zero thermal coupling.
4. **2016–2026 Spatial-Nonlocal Thermoelasticity Literature (29 audited papers in Task 1)**:
   - **0 / 29** formulate Variant V1 or Variant V2 ($\gamma \in (0,1)$).
   - **0 / 28** bounded/half-space BVPs impose integral-consistent Robin CBCs.
   - **12 / 25 (48.0%)** of coupled papers pair differential Form A stress with local constant-strain entropy/heating (violating the Second Law), while **13 / 25 (52.0%)** apply an identical $\gamma=0$ operator to stress, entropy, and heat flux so that nonlocality cancels identically out of the bulk heat PDE.

---

## 2. Detailed Comparison Against Key Prior Works

### 2.1 Eringen (1974) — *Theory of Nonlocal Thermoelasticity* (*Int. J. Eng. Sci.* 12, 1063–1077)
- **Source Verification**: Verified 100% full text from Google Drive (`1tuZpa5qC4AmM7M2EKIi8Jk-Yu7vmwcow`, 15 pages).
- **What Eringen (1974) did**:
  - Postulated global balance of energy and the global Clausius–Duhem inequality with nonlocal energy localization residuals $\hat{\rho}$ and $\hat{e}$ satisfying $\int_V \hat{\rho}\,dv = 0$ and $\int_V \hat{e}\,dv = 0$ (Section 2, Eqs. 2.1–2.10).
  - Introduced a quadratic nonlocal Helmholtz free energy functional $\Sigma$ for a linear isotropic thermoelastic solid (Section 4, Eq. 4.16) and derived the integral constitutive equations (Eqs. 4.19–4.22, p. 1072):
    $$\sigma_{kl}(\mathbf{x},t) = \int_V \alpha(|\mathbf{x}-\mathbf{x}'|)\left[\lambda e_{rr}(\mathbf{x}',t)\delta_{kl} + 2\mu e_{kl}(\mathbf{x}',t) - \beta\theta(\mathbf{x}',t)\delta_{kl}\right]dv(\mathbf{x}'),$$
    $$\rho_0\eta(\mathbf{x},t) = \frac{\rho_0 c}{T_0}\theta(\mathbf{x},t) + \int_V \alpha(|\mathbf{x}-\mathbf{x}'|)\beta e_{kk}(\mathbf{x}',t)\,dv(\mathbf{x}'),$$
    where symmetry of the cross-coupling kernel $\alpha'(|\mathbf{x}-\mathbf{x}'|) = \alpha(|\mathbf{x}-\mathbf{x}'|)$ follows from the quadratic functional.
- **What Eringen (1974) did NOT do (Novelty Gap)**:
  1. **No two-phase kernel ($\gamma \in (0,1)$)**: Eringen (1974) used a purely nonlocal ($\gamma = 0$) kernel $\alpha(|\mathbf{x}-\mathbf{x}'|)$, which is a Fredholm operator of the first kind with no bounded inverse on $L^2(\Omega)$ (Romano et al., 2017).
  2. **No differential equivalent or Robin CBCs on bounded/half-space domains**: Eringen did not introduce the Helmholtz differential kernel $(1-\ell^2\nabla^2)^{-1}$ until Eringen (1983) (*J. Appl. Phys.* 54:4703, isothermal), and never derived the boundary conditions required when $(1-\ell^2\nabla^2)$ is applied on a half-space or finite interval.
  3. **No Variant V1 or master $\Psi_\lambda$ family**: Eringen (1974) did not consider the physically distinct regime where interatomic elastic bond forces are nonlocal ($\ell > 0$) while local lattice anharmonicity produces local thermal stress/entropy coupling ($\lambda = 0$, Variant V1), nor the continuous two-phase interpolation $\Psi_\lambda[\varepsilon,\theta]$.
  4. **No identification of the post-1983 Form A thermoelastic inconsistency**: Because differential Form A did not yet exist in 1974, Eringen (1974) could not address the widespread post-2016 practice of pairing $(1-\ell^2\nabla^2)\sigma = E\varepsilon - \beta\theta$ with local entropy $\rho\eta = (\rho c_E/T_0)\theta + \beta\varepsilon$.

---

### 2.2 Fernández-Sáez, Zaera, Loya & Reddy (2016) — *Int. J. Eng. Sci.* 99, 107–116
- **Source Verification**: Verified 100% full text via open-access repository (`https://core.ac.uk/download/pdf/44309567.pdf`).
- **What they did**:
  - Analyzed **isothermal, static** Euler–Bernoulli beam bending on $[0,L]$ with Eringen's pure-nonlocal ($\gamma=0$) exponential kernel $K(x,\xi) = \frac{1}{2\kappa}e^{-|x-\xi|/\kappa}$.
  - Showed that the integral relation $\varepsilon(x) = \int_0^L K(x,\xi)\frac{M(\xi)}{EI}\,d\xi$ is equivalent to the 2nd-order ODE $\varepsilon''(x) - \frac{1}{\kappa^2}\varepsilon(x) = -\frac{M(x)}{\kappa^2 EI}$ **if and only if** the two homogeneous Robin CBCs (their Eqs. 18–19),
    $$\varepsilon'(0) - \frac{1}{\kappa}\varepsilon(0) = 0, \qquad \varepsilon'(L) + \frac{1}{\kappa}\varepsilon(L) = 0,$$
    hold at the beam ends.
- **What they did NOT do (Novelty Gap)**:
  - Strictly **isothermal** and **static** ($\theta \equiv 0$, $\ddot{u} \equiv 0$, $\gamma = 0$).
  - Formulated only for a statically determinate bending moment $M(x)$ (stress-driven beam inversion), not for dynamic coupled thermoelastic wave propagation or strain-driven two-phase ($\gamma \in (0,1)$) continua.

---

### 2.3 Romano, Barretta, Diaco & Marotti de Sciarra (2017) — *Int. J. Mech. Sci.* 121, 151–156
- **Source Verification**: Verified 100% full text from Google Drive (`1Dab__2bTCYeYBJXqwKyWuYR399u02ve7`, 6 pages).
- **What they did**:
  - Formulated the two-phase local/nonlocal integral convolution on $[a,b]$ for **isothermal 1D elastostatics** (their Eq. 8, with local fraction $\alpha \in [0,1)$, denoted $\gamma \in (0,1)$ in our notation).
  - Proved Proposition 4.1 (their Eq. 19): the two-phase integral relation $f(x) = \alpha g(x) + \frac{1-\alpha}{2c}\int_a^b e^{-|x-y|/c}g(y)\,dy$ is equivalent to the differential equation $\frac{d^2 f}{dx^2} - \frac{1}{c^2}f = \alpha\frac{d^2 g}{dx^2} - \frac{1}{c^2}g$ **together with two non-homogeneous Robin Constitutive Boundary Conditions (CBCs)**:
    $$\frac{df(a)}{dx} - \frac{1}{c}f(a) = -\frac{\alpha}{c}g(a), \qquad \frac{df(b)}{dx} + \frac{1}{c}f(b) = \frac{\alpha}{c}g(b).$$
  - Showed in Section 5 (Table 1) that in **purely nonlocal ($\alpha=0$)** strain-driven elastostatics, the two Robin CBCs over-constrain standard statically determinate beam problems.
- **What they did NOT do (Novelty Gap)**:
  1. **Strictly isothermal and static**: Zero thermal fields, zero entropy, zero heat conduction, zero thermodynamics.
  2. **Did not analyze the dynamic wave-order transition at $\gamma > 0$ vs $\gamma = 0$**: In elastodynamics/thermoelastodynamics ($\rho\ddot{u} = \partial_x\sigma$), substituting the two-phase law $(1-\ell^2\partial_x^2)\sigma = (1-\gamma\ell^2\partial_x^2)\sigma^L$ into the equation of motion gives
     $$-\gamma\ell^2 E u_{xxxx} + (E - \rho\ell^2\partial_t^2)u_{xx} - \rho\ddot{u} - (1-\gamma\ell^2\partial_x^2_\lambda)(\beta\theta_x) = 0.$$
     When $\gamma = 0$ (Form A, used by all 29 audited thermoelastic papers), the 4th-order derivative $-\gamma\ell^2 E u_{xxxx}$ **vanishes**, collapsing the spatial order from 4 to 2 and making it impossible to satisfy the Robin CBCs in bounded/half-space wave BVPs. When $\gamma \in (0,1)$, the 4th-order term survives, generating an extra evanescent nonlocal boundary-layer mode $k_{\text{NL}}$ whose amplitude is uniquely fixed by the two-phase thermoelastic Robin CBC!

---

### 2.4 Recent Wave & Boundary-Condition Papers (2024–2026)

| Work | Verification Source | Exact Scope | Overlap with Candidate C1 |
|---|---|---|---|
| **Pham & Vu (2024)**, *Mech. Res. Commun.* 137, 104266 | Open-access full text (`fetch_page`) | Isothermal Rayleigh waves in a two-phase elastic half-space; derives secular equation and depressed-cubic approximate wave speed. | **None on thermoelasticity**: Purely isothermal elastodynamics; no thermal field, entropy, free energy, or heat equation. |
| **Nobili & Pramanik (2025)**, *Mech. Mater.* 202, 105242 | Open-access full text (`fetch_page`) | Isothermal hyperelastic soft biological tissue reinforced by a stiff thin boundary coating; derives asymptotic effective boundary conditions. | **None**: "Consistent BCs" means thin-coating asymptotic jumps in local hyperelasticity, not Eringen integral Robin CBCs or thermoelasticity. |
| **Pramanik, Nobili & Manna (2026)**, *Int. J. Non-Linear Mech.* 180, 105302 | Open-access full text (`fetch_page`) | Isothermal Rayleigh-type surface waves in a viscoelastic neo-Hookean half-space with membrane boundary conditions. | **None**: Purely isothermal local viscoelasticity. |
| **Anh & Vinh (2026)**, *Arch. Appl. Mech.* 96, 54 | Public abstract & reference list (`fetch_page`; full body paywalled — see `unverified.md`) | Isothermal reflection of harmonic plane waves in a two-phase nonlocal elastic half-space. | **Partial overlap on isothermal reflection mechanics only**: Studies isothermal 2D reflection with two-phase elasticity; zero thermoelasticity, zero entropy/heat coupling, zero thermodynamic inconsistency proofs. |
| **Hue, Anh, Vinh & Giang (2026)**, *Meccanica* 61, 14 | Public abstract & reference list (`fetch_page`; full body paywalled — see `unverified.md`) | Isothermal Rayleigh waves in an orthotropic two-phase nonlocal elastic half-space. | **None on thermoelasticity**: Purely isothermal orthotropic Rayleigh waves. |
| **Tran, Vinh, Anh & Hue (Aug 2026)**, *Wave Motion* 103737 | Public abstract (`fetch_page`; full body paywalled — see `unverified.md`) | Isothermal Rayleigh waves in an isotropic two-phase nonlocal elastic half-space using impedance matrix method. | **None on thermoelasticity**: Purely isothermal Rayleigh waves. |

---

## 3. Summary of What Remains Strictly Novel in Candidate C1

| Component of Candidate C1 | Prior Status in Literature (1974–2026) | Novelty Verdict |
|---|---|---|
| **1. Counted Proof of Constitutive Dilemma in 2016–2026 Nonlocal Thermoelasticity** | Unrecognized. All 25 coupled papers in our 29-paper census fall into either (a) Form A + local entropy (12/25 = 48%, violating the Second Law) or (b) $\gamma=0$ identical-kernel cancellation (13/25 = 52%, erasing bulk thermal nonlocality); `Sur et al. (2026)` p. 183 falsely claims (a) has a consistent Helmholtz free energy. | **Strictly Novel** |
| **2. Master Two-Phase Helmholtz Free Energy $\Psi_\lambda[\varepsilon,\theta]$ ($\gamma \in (0,1), \lambda \in [0,1]$) unifying V1 ($\lambda=0$) and V2 ($\lambda=1$)** | Eringen (1974) treated only $\gamma=0, \lambda=1$ on unbounded domains. Neither Variant V1 ($\gamma \in (0,1), \lambda=0$) nor Variant V2 ($\gamma \in (0,1), \lambda=1$) nor the continuous family $\Psi_\lambda$ appears anywhere in the 29 audited papers (0/29) or external literature. | **Strictly Novel** |
| **3. Non-Existence Theorem, Closed-Cycle Clausius–Duhem Violation, Availability Source, and Reciprocity Failure for Form A + Local Heating** | Never proved or quantified in the nonlocal thermoelasticity literature. | **Strictly Novel** |
| **4. Coupled Thermoelastic Robin Constitutive Boundary Conditions (CBCs) and Resolution of the $\gamma=0 \to \gamma \in (0,1)$ Wave-Order Collapse** | Isothermal static Robin CBCs were derived by Fernández-Sáez et al. (2016) and Romano et al. (2017); isothermal reflection was studied by Anh & Vinh (2026). **Coupled thermoelastic Robin CBCs** (where temperature $\theta(0,t)$ enters the mechanical Robin CBC explicitly in V2 and fixes the 3rd coupled thermoelastic branch $k_{\text{NL}}$) have **0/28** prior usage. | **Novel in Thermoelasticity** (must explicitly cite Romano et al. 2017, Fernández-Sáez et al. 2016, Pham & Vu 2024, and Anh & Vinh 2026 for the isothermal foundation) |
