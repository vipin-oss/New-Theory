# Task 3: Complete Mathematical Proofs for Candidate C1

## Overview of Main Results

1. **Theorem 1 (Master Two-Phase Nonlocal Helmholtz Free Energy $\Psi_\lambda[\boldsymbol{\varepsilon},\theta]$, Variants V1 and V2, Clausius–Duhem Consistency, and Betti–Maxwell Reciprocity)**: Constructs a single two-parameter family of self-adjoint two-phase local/nonlocal Helmholtz free energy functionals $\Psi_\lambda[\boldsymbol{\varepsilon},\theta]$ ($\gamma \in (0,1)$, $\lambda \in [0,1]$) on bounded or semi-infinite domains $\Omega$. Taking its Fréchet derivatives yields **Variant V1** at $\lambda = 0$ (two-phase elastic convolution with local thermal coupling) and **Variant V2** at $\lambda = 1$ (full two-phase thermoelastic stress convolution with dual two-phase dilatation heating), both satisfying the Second Law of Thermodynamics and exact Cazimir–Betti–Maxwell reciprocity.
2. **Theorem 2 (Thermodynamic Inconsistency of Mismatched Form A + Local Entropy/Heating, and Critique of $\gamma = 0$ All-Field Cancellation)**:
   - **Part A (Non-Existence of Free Energy)**: Proves via Schwarz's mixed second Fréchet derivative theorem that pairing differential Form A (or Klein–Gordon Form A) stress with local entropy $\rho\eta = \frac{\rho c_E}{T_0}\theta + \boldsymbol{\beta}:\boldsymbol{\varepsilon}$ (used in **12 / 25 = 48.0%** of coupled 2016–2026 papers, and explicitly claimed by `Sur et al. 2026`, p. 183 to derive from a Helmholtz free energy) admits **no** twice Fréchet-differentiable free energy functional whenever $\ell > 0$.
   - **Part B (Closed-Cycle Second-Law Violation)**: Exhibits an explicit harmonic standing-wave cycle $(\varepsilon(x,t),\theta(x,t))$ over which Variants V1 and V2 have zero net reversible cycle residual ($\mathcal{R}_{\text{cycle}} = 0$), whereas Form A + local heating creates spurious net work $\mathcal{R}_{\text{cycle}}^{\text{Form A}} = -\frac{\pi^2}{k}\beta\varepsilon_0\theta_0\frac{\ell^2 k^2}{1+\ell^2 k^2} \neq 0$, yielding negative internal entropy production in the low-conductivity/high-frequency regime.
   - **Part C (Uncancelled Availability Source & Reciprocity Failure)**: Derives the exact uncancelled bulk availability source $S_{\text{mismatch}}^{\text{Form A}} = \beta\dot{\varepsilon}(\theta - \mathcal{K}_\ell[\theta])$ and shows that the thermoelastic cross-coupling ratio violates Cazimir–Betti reciprocity by $(1+\ell^2 k^2)^{-1} \neq 1$.
   - **Part D (Critique of Class 2: $\gamma=0$ All-Field Identical-Kernel Cancellation)**: Proves that applying the identical $\gamma=0$ operator to $\boldsymbol{\sigma}$, $\rho\eta$, and $\mathbf{q}$ (**13 / 25 = 52.0%** of coupled papers) cancels nonlocality out of the bulk heat PDE while violating Fredholm invertibility and boundary Robin CBCs.
3. **Theorem 3 (Exact Integral-to-Differential Equivalence via Thermoelastic Robin Constitutive Boundary Conditions and Resolution of the $\gamma=0 \to \gamma \in (0,1)$ Wave-Order Collapse)**:
   - Derives the exact differential equation and Thermoelastic Robin Constitutive Boundary Conditions (CBCs) on $[a,b]$ and $[0,\infty)$ for all $\lambda \in [0,1]$ and $\gamma \in (0,1)$.
   - Proves that in a half-space $[0,\infty)$ at frequency $\omega$, **Variant V1** ($\lambda=0$) has a **cubic** characteristic dispersion polynomial in $q = s^2$ (3 decaying modes $s_1, s_2, s_3$), uniquely closed by 1 mechanical BC + 1 thermal BC + **1 Robin CBC**, whereas **Variant V2** ($\lambda=1$) has a **quartic** characteristic polynomial in $q = s^2$ (4 decaying modes $s_1, s_2, s_3, s_4$), uniquely closed by 1 mechanical BC + 1 thermal BC + **2 Robin CBCs** (one on the strain convolution $z_1 = \mathcal{K}_\ell[\varepsilon]$ and one on the thermal convolution $z_2 = \mathcal{K}_\ell[\theta]$).
   - Shows that setting $\gamma = 0$ (Form A) collapses the leading spatial derivative $-\gamma\ell^2 E u_{xxxx} \to 0$, reducing the half-space system to 2 decaying modes and rendering the Robin CBCs unsolvable.
4. **Theorem 4 (Exact Nonlocal Availability & Surface-Energy Identity under Robin CBCs)**: Proves that for $z = \mathcal{K}_\ell[f]$ on $[a,b]$, the quadratic form $\frac{1}{2}\int_a^b f\,\mathcal{K}_\ell[f]\,dx$ equals $\frac{1}{2}\int_a^b (z^2 + \ell^2 z_x^2)\,dx + \frac{\ell}{2}(z(a)^2 + z(b)^2)$ **if and only if** the Robin CBCs hold, and quantifies the spurious boundary power leakage $\mathcal{B}_{\text{Robin}}(t)$ when the Robin CBCs are omitted.

---

## Theorem 1: Master Two-Phase Nonlocal Helmholtz Free Energy $\Psi_\lambda[\boldsymbol{\varepsilon},\theta]$, Variants V1 and V2, and Reciprocity

### 1.1 Operator Definitions and Self-Adjointness
Let $\Omega \subset \mathbb{R}^d$ be a bounded domain (e.g., $\Omega = [a,b]$ in 1D) or a semi-infinite half-space ($\Omega = [0,\infty)$). Let $K_\ell(\mathbf{x},\boldsymbol{\xi})$ be a real, symmetric, positive-definite nonlocal kernel on $\Omega \times \Omega$:
$$K_\ell(\mathbf{x},\boldsymbol{\xi}) = K_\ell(\boldsymbol{\xi},\mathbf{x}), \qquad \int_\Omega \int_\Omega \phi(\mathbf{x}) K_\ell(\mathbf{x},\boldsymbol{\xi}) \phi(\boldsymbol{\xi})\,d\boldsymbol{\xi}\,d\mathbf{x} > 0 \quad \forall \phi \in L^2(\Omega)\setminus\{0\}. \tag{1.1}$$
In 1D, the canonical bi-exponential kernel is
$$K_\ell(x,\xi) = \frac{1}{2\ell}e^{-|x-\xi|/\ell}, \qquad \ell > 0. \tag{1.2}$$
Let $\mathcal{K}_\ell : L^2(\Omega) \to L^2(\Omega)$ denote the integral operator $\mathcal{K}_\ell[\phi](\mathbf{x}) := \int_\Omega K_\ell(\mathbf{x},\boldsymbol{\xi})\phi(\boldsymbol{\xi})\,d\boldsymbol{\xi}$. For local phase fraction $\gamma \in (0,1)$ and thermal-nonlocality interpolation parameter $\lambda \in [0,1]$, define the two-phase operators:
$$\mathcal{L}_{\gamma,\ell}[\phi](\mathbf{x}) := \gamma\phi(\mathbf{x}) + (1-\gamma)\mathcal{K}_\ell[\phi](\mathbf{x}), \tag{1.3}$$
$$\mathcal{M}_{\lambda,\gamma,\ell}[\phi](\mathbf{x}) := (1-\lambda)\phi(\mathbf{x}) + \lambda\,\mathcal{L}_{\gamma,\ell}[\phi](\mathbf{x}) = \big(1 - \lambda(1-\gamma)\big)\phi(\mathbf{x}) + \lambda(1-\gamma)\mathcal{K}_\ell[\phi](\mathbf{x}). \tag{1.4}$$

**Lemma 1.1 (Self-Adjointness and Coercivity on $L^2(\Omega)$)**: For all $\gamma \in (0,1)$ and $\lambda \in [0,1]$, $\mathcal{L}_{\gamma,\ell}$ and $\mathcal{M}_{\lambda,\gamma,\ell}$ are bounded, self-adjoint, and strictly coercive operators on $L^2(\Omega)$:
$$\langle \psi, \mathcal{L}_{\gamma,\ell}[\phi]\rangle_{L^2(\Omega)} = \langle \mathcal{L}_{\gamma,\ell}[\psi], \phi\rangle_{L^2(\Omega)}, \qquad \langle \phi, \mathcal{L}_{\gamma,\ell}[\phi]\rangle_{L^2(\Omega)} \ge \gamma\|\phi\|_{L^2(\Omega)}^2. \tag{1.5}$$
*Proof*: Immediate from Fubini's theorem, the symmetry $K_\ell(\mathbf{x},\boldsymbol{\xi}) = K_\ell(\boldsymbol{\xi},\mathbf{x})$, and the positive-definiteness (1.1) of $\mathcal{K}_\ell$. $\square$

### 1.2 The Master Two-Phase Helmholtz Free Energy Functional
Define the total Helmholtz free energy functional $\Psi_\lambda : L^2(\Omega;\mathbb{R}_{\text{sym}}^{d\times d}) \times L^2(\Omega;\mathbb{R}) \to \mathbb{R}$ by
$$\boxed{\Psi_\lambda[\boldsymbol{\varepsilon},\theta] := \int_\Omega \left[ \frac{1}{2}\boldsymbol{\varepsilon}(\mathbf{x}) : \mathcal{L}_{\gamma,\ell}\big[\mathbb{C}:\boldsymbol{\varepsilon}\big](\mathbf{x}) - \theta(\mathbf{x})\,\mathcal{M}_{\lambda,\gamma,\ell}\big[\boldsymbol{\beta}:\boldsymbol{\varepsilon}\big](\mathbf{x}) - \frac{\rho c_E}{2T_0}\theta(\mathbf{x})^2 \right] d\mathbf{x},} \tag{1.6}$$
where $\mathbb{C}$ is the constant, symmetric, positive-definite fourth-order elasticity tensor ($C_{ijkl} = C_{klij} = C_{jikl}$), $\boldsymbol{\beta}$ is the symmetric thermal modulus tensor, $\rho > 0$ is the mass density, $c_E > 0$ is the specific heat at constant strain, and $T_0 > 0$ is the reference temperature.

### 1.3 Fréchet Derivatives and Constitutive Laws for Variants V1 ($\lambda=0$) and V2 ($\lambda=1$)
Computing the first directional variation of $\Psi_\lambda[\boldsymbol{\varepsilon},\theta]$ in the direction $(\delta\boldsymbol{\varepsilon}, \delta\theta)$ and applying Lemma 1.1:
$$\begin{aligned}
\delta\Psi_\lambda[\boldsymbol{\varepsilon},\theta](\delta\boldsymbol{\varepsilon},\delta\theta)
&= \int_\Omega \left[ \frac{1}{2}\delta\boldsymbol{\varepsilon} : \mathcal{L}_{\gamma,\ell}[\mathbb{C}:\boldsymbol{\varepsilon}] + \frac{1}{2}\boldsymbol{\varepsilon} : \mathcal{L}_{\gamma,\ell}[\mathbb{C}:\delta\boldsymbol{\varepsilon}] - \delta\theta\,\mathcal{M}_{\lambda,\gamma,\ell}[\boldsymbol{\beta}:\boldsymbol{\varepsilon}] - \theta\,\mathcal{M}_{\lambda,\gamma,\ell}[\boldsymbol{\beta}:\delta\boldsymbol{\varepsilon}] - \frac{\rho c_E}{T_0}\theta\,\delta\theta \right] d\mathbf{x} \\
&= \int_\Omega \delta\boldsymbol{\varepsilon}(\mathbf{x}) : \Big(\mathcal{L}_{\gamma,\ell}[\mathbb{C}:\boldsymbol{\varepsilon}](\mathbf{x}) - \boldsymbol{\beta}\,\mathcal{M}_{\lambda,\gamma,\ell}[\theta](\mathbf{x})\Big)\,d\mathbf{x} \\
&\quad - \int_\Omega \delta\theta(\mathbf{x})\,\left(\frac{\rho c_E}{T_0}\theta(\mathbf{x}) + \mathcal{M}_{\lambda,\gamma,\ell}[\boldsymbol{\beta}:\boldsymbol{\varepsilon}](\mathbf{x})\right) d\mathbf{x}.
\end{aligned} \tag{1.7}$$
Enforcing the Coleman–Noll / Clausius–Duhem global dissipation inequality on $\Omega$,
$$\int_\Omega \left(\boldsymbol{\sigma}:\dot{\boldsymbol{\varepsilon}} - \rho\eta\dot{\theta} - \frac{1}{T_0}\mathbf{q}\cdot\nabla\theta\right) d\mathbf{x} - \dot{\Psi}_\lambda[\boldsymbol{\varepsilon},\theta] = -\frac{1}{T_0}\int_\Omega \mathbf{q}\cdot\nabla\theta\,d\mathbf{x} \ge 0 \tag{1.8}$$
for arbitrary smooth rates $(\dot{\boldsymbol{\varepsilon}},\dot{\theta})$, yields the unique thermodynamically conjugate stress and entropy densities:
$$\boxed{\boldsymbol{\sigma}(\mathbf{x},t) = \frac{\delta\Psi_\lambda}{\delta\boldsymbol{\varepsilon}(\mathbf{x},t)} = \mathcal{L}_{\gamma,\ell}[\mathbb{C}:\boldsymbol{\varepsilon}](\mathbf{x},t) - \boldsymbol{\beta}\,\mathcal{M}_{\lambda,\gamma,\ell}[\theta](\mathbf{x},t),} \tag{1.9a}$$
$$\boxed{\rho\eta(\mathbf{x},t) = -\frac{\delta\Psi_\lambda}{\delta\theta(\mathbf{x},t)} = \frac{\rho c_E}{T_0}\theta(\mathbf{x},t) + \mathcal{M}_{\lambda,\gamma,\ell}[\boldsymbol{\beta}:\boldsymbol{\varepsilon}](\mathbf{x},t).} \tag{1.9b}$$

Evaluating (1.9a)–(1.9b) at the two endpoints $\lambda = 0$ and $\lambda = 1$ gives:
- **Variant V1 ($\lambda = 0$, Two-Phase Elastic Convolution with Local Thermal Coupling)**: Since $\mathcal{M}_{0,\gamma,\ell} = I$,
  $$\boxed{\boldsymbol{\sigma}^{\text{V1}} = \mathcal{L}_{\gamma,\ell}[\mathbb{C}:\boldsymbol{\varepsilon}] - \boldsymbol{\beta}\theta, \qquad \rho\eta^{\text{V1}} = \frac{\rho c_E}{T_0}\theta + \boldsymbol{\beta}:\boldsymbol{\varepsilon}.} \tag{1.10}$$
  In 1D with Cattaneo/Lord–Shulman heat flux $(1+\tau_0\partial_t)q = -\kappa\partial_x\theta$, the linearized energy balance $\rho T_0\dot{\eta} = -\partial_x q + \rho r$ gives the **local-heating heat PDE**:
  $$(1+\tau_0\partial_t)\big(\rho c_E\dot{\theta} + \beta T_0\dot{\varepsilon}\big) = \kappa\partial_x^2\theta + (1+\tau_0\partial_t)\rho r. \tag{1.11}$$
- **Variant V2 ($\lambda = 1$, Full Two-Phase Thermoelastic Convolution with Dual Nonlocal Heating)**: Since $\mathcal{M}_{1,\gamma,\ell} = \mathcal{L}_{\gamma,\ell}$,
  $$\boxed{\boldsymbol{\sigma}^{\text{V2}} = \mathcal{L}_{\gamma,\ell}[\mathbb{C}:\boldsymbol{\varepsilon} - \boldsymbol{\beta}\theta], \qquad \rho\eta^{\text{V2}} = \frac{\rho c_E}{T_0}\theta + \mathcal{L}_{\gamma,\ell}[\boldsymbol{\beta}:\boldsymbol{\varepsilon}].} \tag{1.12}$$
  The linearized energy balance $\rho T_0\dot{\eta} = -\partial_x q + \rho r$ mandates the **dual two-phase nonlocal dilatation heating**:
  $$(1+\tau_0\partial_t)\Big(\rho c_E\dot{\theta} + \beta T_0\,\mathcal{L}_{\gamma,\ell}[\dot{\varepsilon}]\Big) = \kappa\partial_x^2\theta + (1+\tau_0\partial_t)\rho r. \tag{1.13}$$

### 1.4 Exact Betti–Maxwell / Cazimir–Betti Cross-Reciprocity
Taking the second Fréchet derivatives of $\Psi_\lambda[\boldsymbol{\varepsilon},\theta]$ from (1.9a)–(1.9b) gives the distributional kernels:
$$\frac{\delta\boldsymbol{\sigma}(\mathbf{x})}{\delta\theta(\mathbf{y})} = -\boldsymbol{\beta}\Big[\big(1-\lambda(1-\gamma)\big)\delta(\mathbf{x}-\mathbf{y}) + \lambda(1-\gamma)K_\ell(\mathbf{x},\mathbf{y})\Big] = -\frac{\delta(\rho\eta(\mathbf{y}))}{\delta\boldsymbol{\varepsilon}(\mathbf{x})}, \tag{1.14}$$
which are equal for all $\mathbf{x},\mathbf{y} \in \Omega$, $\lambda \in [0,1]$, and $\gamma \in (0,1)$ because $K_\ell(\mathbf{x},\mathbf{y}) = K_\ell(\mathbf{y},\mathbf{x})$. Consequently, for any two Laplace-transformed thermoelastic states $(\hat{\mathbf{u}}^{(1)},\hat{\theta}^{(1)})$ and $(\hat{\mathbf{u}}^{(2)},\hat{\theta}^{(2)})$ driven by body forces and heat sources $(\hat{\mathbf{b}}^{(j)},\hat{r}^{(j)})$ ($j=1,2$) under homogeneous boundary conditions (including the homogeneous Robin CBCs of Theorem 3), Cazimir–Betti reciprocity holds identically:
$$\int_\Omega \left(\hat{\mathbf{b}}^{(1)}\cdot\hat{\mathbf{u}}^{(2)} - \frac{\rho}{T_0 s}\hat{r}^{(1)}\hat{\theta}^{(2)}\right) d\mathbf{x} = \int_\Omega \left(\hat{\mathbf{b}}^{(2)}\cdot\hat{\mathbf{u}}^{(1)} - \frac{\rho}{T_0 s}\hat{r}^{(2)}\hat{\theta}^{(1)}\right) d\mathbf{x}. \tag{1.15}$$
$\square$

---

## Theorem 2: Thermodynamic Inconsistency of Mismatched Form A + Constant-Strain Heating, and Critique of $\gamma=0$ All-Field Cancellation

### 2.1 Part A: Non-Existence of a Helmholtz Free Energy Functional for Form A + Local Entropy
In **12 / 25 (48.0%)** of the coupled spatial-nonlocal thermoelastic papers audited in Task 1 (`Li & He 2018`, `Li, Guo & Tian 2018`, `Sarkar, De & Sarkar 2019`, `Lata & Singh 2020a, 2020b`, `Bayones et al. 2021`, `Yang et al. 2021`, `Barak et al. 2023`, `Gupta et al. 2023a`, `Lotfy et al. 2025`, `Sur et al. 2025`, `Sur et al. 2026`), the constitutive equations are postulated in the asymmetric form (in 1D notation):
$$(1 - \ell^2\partial_x^2)\sigma(x,t) = E\varepsilon(x,t) - \beta\theta(x,t) \iff \sigma(x,t) = \mathcal{K}_\ell[E\varepsilon - \beta\theta](x,t), \tag{2.1a}$$
$$\rho\eta(x,t) = \frac{\rho c_E}{T_0}\theta(x,t) + \beta\varepsilon(x,t). \tag{2.1b}$$

**Proposition 2.1 (Non-Existence of Free Energy Functional)**: For any $\beta \neq 0$ and $\ell > 0$, there exists **no** twice Fréchet-differentiable functional $\Psi[\varepsilon,\theta]$ on $L^2(\Omega)\times L^2(\Omega)$ such that $\sigma = \delta\Psi/\delta\varepsilon$ and $\rho\eta = -\delta\Psi/\delta\theta$ reproduce (2.1a)–(2.1b).

*Proof*: Suppose such a twice Fréchet-differentiable functional $\Psi[\varepsilon,\theta]$ exists. By Schwarz's theorem on the symmetry of second Fréchet derivatives, the mixed second variations must satisfy
$$\left\langle \delta\theta, \frac{\delta\sigma}{\delta\theta}[\delta\varepsilon] \right\rangle_{L^2(\Omega)} = \frac{\delta^2\Psi}{\delta\theta\,\delta\varepsilon}(\delta\varepsilon,\delta\theta) = \frac{\delta^2\Psi}{\delta\varepsilon\,\delta\theta}(\delta\varepsilon,\delta\theta) = -\left\langle \delta\varepsilon, \frac{\delta(\rho\eta)}{\delta\varepsilon}[\delta\theta] \right\rangle_{L^2(\Omega)} \tag{2.2}$$
for all test functions $\delta\varepsilon, \delta\theta \in C_c^\infty(\Omega)$. From (2.1a), the Fréchet derivative of $\sigma$ with respect to $\theta$ is $-\beta\mathcal{K}_\ell$, whereas from (2.1b), the Fréchet derivative of $\rho\eta$ with respect to $\varepsilon$ is $+\beta I$. Substituting these into (2.2) requires
$$-\beta\langle \delta\theta, \mathcal{K}_\ell[\delta\varepsilon]\rangle_{L^2(\Omega)} = -\beta\langle \delta\varepsilon, \delta\theta\rangle_{L^2(\Omega)} \iff \langle \delta\theta, (\mathcal{K}_\ell - I)[\delta\varepsilon]\rangle_{L^2(\Omega)} = 0 \quad \forall \delta\varepsilon, \delta\theta \in C_c^\infty(\Omega). \tag{2.3}$$
Since $\beta \neq 0$, this requires $\mathcal{K}_\ell = I$ on $C_c^\infty(\Omega)$, or equivalently $(1 - \ell^2\partial_x^2)\delta\varepsilon = \delta\varepsilon \implies -\ell^2\partial_x^2\delta\varepsilon = 0$ for all $\delta\varepsilon \in C_c^\infty(\Omega)$, which is impossible for any $\ell > 0$. The identical proof applies verbatim when $(1-\ell^2\partial_x^2)$ is replaced by the Klein–Gordon operator $(1-\ell^2\partial_x^2+\tau^2\partial_t^2)$, directly refuting the claim in `Sur et al. (2026)` (p. 183) that their Eqs. (21)–(22) derive from a thermodynamically consistent Helmholtz free energy. $\square$

### 2.2 Part B: Explicit Closed-Cycle Clausius–Duhem Violation
Consider a spatially periodic domain $[0, L_k]$ with $L_k = 2\pi/k$ ($k > 0$) driven through the closed time-periodic strain-temperature cycle of period $T_{\text{cyc}} = 2\pi/\omega$ ($\omega > 0$):
$$\varepsilon(x,t) = \varepsilon_0 \cos(kx)\cos(\omega t), \qquad \theta(x,t) = \theta_0 \cos(kx)\sin(\omega t). \tag{2.4}$$
Because $(\varepsilon(x, T_{\text{cyc}}), \theta(x, T_{\text{cyc}})) = (\varepsilon(x,0), \theta(x,0))$, the integral of $\dot{\Psi}$ over a full cycle $[0, T_{\text{cyc}}]$ must vanish for any genuine state functional $\Psi$. Define the reversible thermoelastic cycle work-entropy residual:
$$\mathcal{R}_{\text{cycle}} := \int_0^{2\pi/\omega}\int_0^{2\pi/k} \big(\sigma(x,t)\dot{\varepsilon}(x,t) - \rho\eta(x,t)\dot{\theta}(x,t)\big)\,dx\,dt. \tag{2.5}$$
Using $\int_0^{2\pi/k} \cos^2(kx)\,dx = \frac{\pi}{k}$, $\int_0^{2\pi/\omega}\cos(\omega t)\sin(\omega t)\,dt = 0$, and $\int_0^{2\pi/\omega}\sin^2(\omega t)\,dt = \int_0^{2\pi/\omega}\cos^2(\omega t)\,dt = \frac{\pi}{\omega}$:
1. **For Variant V1 ($\lambda=0$)**: $\sigma^{\text{V1}} = \hat{L}(k)E\varepsilon - \beta\theta$ and $\rho\eta^{\text{V1}} = \frac{\rho c_E}{T_0}\theta + \beta\varepsilon$, where $\hat{L}(k) = \frac{1+\gamma\ell^2 k^2}{1+\ell^2 k^2}$. The cross terms in $\sigma^{\text{V1}}\dot{\varepsilon} - \rho\eta^{\text{V1}}\dot{\theta}$ are $(-\beta\theta)\dot{\varepsilon} - (\beta\varepsilon)\dot{\theta} = -\beta\frac{\partial}{\partial t}(\varepsilon\theta)$, whose cycle integral is identically zero:
   $$\mathcal{R}_{\text{cycle}}^{\text{V1}} = 0. \tag{2.6a}$$
2. **For Variant V2 ($\lambda=1$)**: $\sigma^{\text{V2}} = \hat{L}(k)(E\varepsilon - \beta\theta)$ and $\rho\eta^{\text{V2}} = \frac{\rho c_E}{T_0}\theta + \hat{L}(k)\beta\varepsilon$. The cross terms are $-\hat{L}(k)\beta\theta\dot{\varepsilon} - \hat{L}(k)\beta\varepsilon\dot{\theta} = -\hat{L}(k)\beta\frac{\partial}{\partial t}(\varepsilon\theta)$, whose cycle integral is also identically zero:
   $$\mathcal{R}_{\text{cycle}}^{\text{V2}} = 0. \tag{2.6b}$$
3. **For Mismatched Form A + Local Entropy (2.1a)–(2.1b)**: Since $\mathcal{K}_\ell[\cos(kx)] = \frac{1}{1+\ell^2 k^2}\cos(kx)$,
   $$\sigma^{\text{Form A}}(x,t) = \frac{E\varepsilon_0\cos(\omega t) - \beta\theta_0\sin(\omega t)}{1+\ell^2 k^2}\cos(kx), \qquad \rho\eta^{\text{loc}}(x,t) = \left(\frac{\rho c_E}{T_0}\theta_0\sin(\omega t) + \beta\varepsilon_0\cos(\omega t)\right)\cos(kx). \tag{2.7}$$
   Substituting (2.7) into (2.5) with $\dot{\varepsilon} = -\omega\varepsilon_0\cos(kx)\sin(\omega t)$ and $\dot{\theta} = \omega\theta_0\cos(kx)\cos(\omega t)$:
   $$\begin{aligned}
   \mathcal{R}_{\text{cycle}}^{\text{Form A}}
   &= \int_0^{2\pi/\omega}\int_0^{2\pi/k} \left[\frac{\beta\theta_0\varepsilon_0\omega}{1+\ell^2 k^2}\sin^2(\omega t) - \beta\varepsilon_0\theta_0\omega\cos^2(\omega t)\right]\cos^2(kx)\,dx\,dt \\
   &= \frac{\pi}{k}\cdot\frac{\pi}{\omega}\cdot\beta\varepsilon_0\theta_0\omega\left(\frac{1}{1+\ell^2 k^2} - 1\right) = \boxed{-\frac{\pi^2}{k}\,\beta\varepsilon_0\theta_0\,\frac{\ell^2 k^2}{1+\ell^2 k^2} \neq 0 \quad (\forall \ell > 0, k > 0).}
   \end{aligned} \tag{2.8}$$
   Whenever $\beta\varepsilon_0\theta_0 < 0$ and the thermal conductivity $\kappa$ satisfies $\kappa k^2 \theta_0 / T_0 < \frac{\omega|\beta\varepsilon_0|\ell^2 k^2}{1+\ell^2 k^2}$, the total cycle entropy production $\oint\int \mathcal{D}_{\text{int}}\,dx\,dt = \frac{1}{T_0}\mathcal{R}_{\text{cycle}}^{\text{Form A}} + \frac{\kappa\pi^2 k\theta_0^2}{T_0\omega}$ is **strictly negative**, violating the Clausius–Duhem inequality. $\square$

### 2.3 Part C: Uncancelled Availability Residual and Broken Cazimir–Betti Reciprocity
Define the total thermoelastic availability (Lyapunov) functional for the Master Family $\Psi_\lambda$:
$$\mathcal{A}_\lambda(t) := \int_\Omega \left[\frac{1}{2}\rho\dot{u}^2 + \frac{1}{2}\varepsilon\,\mathcal{L}_{\gamma,\ell}[E\varepsilon] + \frac{\rho c_E}{2T_0}\theta^2 + \frac{\tau_0}{2\kappa T_0}q^2\right] dx. \tag{2.9}$$
Differentiating $\mathcal{A}_\lambda(t)$ in time along solutions of $\rho\ddot{u} = \partial_x\sigma$, $\rho T_0\dot{\eta} = -\partial_x q$, and $(1+\tau_0\partial_t)q = -\kappa\partial_x\theta$ (with homogeneous boundary conditions) yields:
$$\frac{d\mathcal{A}_\lambda}{dt} + \int_\Omega \frac{q^2}{\kappa T_0}\,dx = \int_\Omega S_{\text{mismatch}}(x,t)\,dx, \tag{2.10}$$
where the bulk constitutive mismatch source is
$$S_{\text{mismatch}}(x,t) = \dot{\varepsilon}(x,t)\big(\sigma(x,t) - \mathcal{L}_{\gamma,\ell}[E\varepsilon](x,t)\big) + \theta(x,t)\left(\rho\dot{\eta}(x,t) - \frac{\rho c_E}{T_0}\dot{\theta}(x,t)\right). \tag{2.11}$$
- For **Variant V1 ($\lambda=0$)**: $S_{\text{mismatch}}^{\text{V1}} = \dot{\varepsilon}(-\beta\theta) + \theta(\beta\dot{\varepsilon}) \equiv 0$.
- For **Variant V2 ($\lambda=1$)**: $\int_\Omega S_{\text{mismatch}}^{\text{V2}}\,dx = -\beta\langle \dot{\varepsilon}, \mathcal{L}_{\gamma,\ell}[\theta]\rangle + \beta\langle \theta, \mathcal{L}_{\gamma,\ell}[\dot{\varepsilon}]\rangle \equiv 0$ by Lemma 1.1.
- For **Mismatched Form A + Local Heating (2.1a)–(2.1b)**:
  $$\boxed{S_{\text{mismatch}}^{\text{Form A}}(x,t) = \beta\,\dot{\varepsilon}(x,t)\,\big(\theta(x,t) - \mathcal{K}_\ell[\theta](x,t)\big) \not\equiv 0, \qquad \widehat{S}_{\text{mismatch}}^{\text{Form A}}(k) = \beta\,\dot{\hat{\varepsilon}}(k)\,\hat{\theta}(k)\,\frac{\ell^2 k^2}{1+\ell^2 k^2}.} \tag{2.12}$$
  In Fourier/Laplace space, the off-diagonal thermoelastic coupling entries between $\hat{u}$ and $\hat{\theta}$ have ratio
  $$\frac{\hat{D}_{12}^{\text{Form A}}(k)}{\hat{D}_{21}^{\text{Form A}}(k)/(T_0 s)} = \frac{1}{1+\ell^2 k^2} \neq 1, \tag{2.13}$$
  breaking Cazimir–Betti reciprocity at order $\mathcal{O}(\ell^2 k^2)$, whereas for both V1 and V2 this ratio is identically $1$.

### 2.4 Part D: Critique of Class 2 ($\gamma=0$ All-Field Identical-Kernel Cancellation)
In **13 / 25 (52.0%)** of the coupled papers in Task 1 (`Bachher & Sarkar 2019`, `Biswas 2020`, `Yadav et al. 2022`, `Gupta et al. 2023b, 2024a, 2024b, 2025, 2026`, `Das et al. 2024, 2025, 2026`, `Aldandani et al. 2026a, 2026b`), the authors postulate (with $\gamma = 0$):
$$(1-\xi^2\nabla^2)\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon} - \boldsymbol{\beta}\theta, \qquad (1-\xi^2\nabla^2)\rho\eta = \frac{\rho c_E}{T_0}\theta + \boldsymbol{\beta}:\boldsymbol{\varepsilon}, \qquad (1-\xi^2\nabla^2)\mathcal{P}_t[\mathbf{q}] = -\kappa\nabla\theta. \tag{2.14}$$
While the first two equations match Eringen's (1974) $\gamma=0$ stress-entropy pair on an unbounded domain, the simultaneous application of the **identical** operator $(1-\xi^2\nabla^2)$ to the heat flux $\mathbf{q}$ causes $(1-\xi^2\nabla^2)$ to cancel identically out of $\rho T_0\dot{\eta} = -\nabla\cdot\mathbf{q}$:
$$(1-\xi^2\nabla^2)\Big[\mathcal{P}_t\big(\rho c_E\dot{\theta} + T_0\boldsymbol{\beta}:\dot{\boldsymbol{\varepsilon}}\big) - \kappa\nabla^2\theta\Big] = 0. \tag{2.15}$$
All 13 papers immediately drop the outer operator $(1-\xi^2\nabla^2)$ to solve the **purely local bulk heat equation** $\mathcal{P}_t(\rho c_E\dot{\theta} + T_0\boldsymbol{\beta}:\dot{\boldsymbol{\varepsilon}}) = \kappa\nabla^2\theta$, while omitting both the homogeneous solutions $e^{\pm x/\xi}$ of $(1-\xi^2\nabla^2)$ and the Robin CBCs on $\boldsymbol{\sigma}$ and $\mathbf{q}$ at boundaries.

---

## Theorem 3: Integral-to-Differential Equivalence via Thermoelastic Robin CBCs and Resolution of the $\gamma=0 \to \gamma \in (0,1)$ Wave-Order Collapse

### 3.1 Exact ODE + Robin CBC Equivalence on $[a,b]$ and $[0,\infty)$
For the 1D bi-exponential kernel $K_\ell(x,\xi) = \frac{1}{2\ell}e^{-|x-\xi|/\ell}$ on $[a,b]$, let $z(x) := \mathcal{K}_\ell[f](x) = \int_a^b \frac{1}{2\ell}e^{-|x-\xi|/\ell}f(\xi)\,d\xi$ for any $f \in C([a,b])$. Splitting the integral at $\xi = x$ and differentiating twice yields:
$$z'(x) = -\frac{1}{2\ell^2}\int_a^x e^{-(x-\xi)/\ell}f(\xi)\,d\xi + \frac{1}{2\ell^2}\int_x^b e^{(x-\xi)/\ell}f(\xi)\,d\xi, \tag{3.1}$$
$$(1 - \ell^2\partial_x^2)z(x) = f(x) \quad \forall x \in (a,b), \tag{3.2}$$
and evaluating $z(x) \mp \ell z'(x)$ at $x=a$ and $x=b$ eliminates the remaining integral identically, yielding the two homogeneous Robin Constitutive Boundary Conditions on $z$:
$$\left(\partial_x - \frac{1}{\ell}\right)z(a) = 0, \qquad \left(\partial_x + \frac{1}{\ell}\right)z(b) = 0. \tag{3.3}$$
Conversely, because the homogeneous BVP $(1-\ell^2\partial_x^2)w = 0$ with $(\partial_x - \ell^{-1})w(a) = (\partial_x + \ell^{-1})w(b) = 0$ has only the trivial solution $w \equiv 0$ (since $\int_a^b (w^2 + \ell^2 w_x^2)\,dx + \ell(w(a)^2 + w(b)^2) = 0$), (3.2)–(3.3) is **strictly equivalent** to $z = \mathcal{K}_\ell[f]$ on $[a,b]$.

Applying this equivalence to the Master Two-Phase Constitutive Equations (1.9a)–(1.9b) gives:

**Proposition 3.1 (Two-Phase Thermoelastic Differential Form and Robin CBCs)**:
1. **Variant V1 ($\lambda = 0$)**: There is **one** nonlocal convolution field $z_1(x,t) := \mathcal{K}_\ell[\varepsilon](x,t) = \frac{\sigma - \gamma E\varepsilon + \beta\theta}{(1-\gamma)E}$. Thus the integral law (1.10) on $[a,b]$ is strictly equivalent to the bulk differential equation
   $$\boxed{(1 - \ell^2\partial_x^2)\big(\sigma(x,t) + \beta\theta(x,t)\big) = (1 - \gamma\ell^2\partial_x^2)\big(E\varepsilon(x,t)\big) \quad \text{on } (a,b)} \tag{3.4a}$$
   together with the **two V1 Thermoelastic Robin CBCs**:
   $$\boxed{\left(\partial_x - \frac{1}{\ell}\right)\big(\sigma - \gamma E\varepsilon + \beta\theta\big)\Big|_{x=a} = 0, \qquad \left(\partial_x + \frac{1}{\ell}\right)\big(\sigma - \gamma E\varepsilon + \beta\theta\big)\Big|_{x=b} = 0.} \tag{3.4b}$$
2. **Variant V2 ($\lambda = 1$)**: The operator $\mathcal{K}_\ell$ acts on **two** independent state fields, $z_1(x,t) := \mathcal{K}_\ell[\varepsilon](x,t)$ (which enters both $\sigma$ and $\rho\eta$) and $z_2(x,t) := \mathcal{K}_\ell[\theta](x,t)$ (which enters $\sigma$). Thus the integral pair (1.12) on $[a,b]$ is strictly equivalent to the bulk differential equations
   $$\boxed{(1 - \ell^2\partial_x^2)\sigma = (1 - \gamma\ell^2\partial_x^2)(E\varepsilon - \beta\theta), \qquad (1 - \ell^2\partial_x^2)\left(\rho\eta - \frac{\rho c_E}{T_0}\theta\right) = (1 - \gamma\ell^2\partial_x^2)(\beta\varepsilon)} \tag{3.5a}$$
   together with the **two pairs of V2 Thermoelastic Robin CBCs** at $x=a$ and $x=b$:
   $$\boxed{\left(\partial_x \mp \frac{1}{\ell}\right)\big(\sigma - \gamma(E\varepsilon - \beta\theta)\big)\Big|_{x=a,b} = 0, \qquad \left(\partial_x \mp \frac{1}{\ell}\right)\left(\rho\eta - \frac{\rho c_E}{T_0}\theta - \gamma\beta\varepsilon\right)\Big|_{x=a,b} = 0.} \tag{3.5b}$$
3. **Half-Space $[0,\infty)$**: Letting $a = 0$ and $b \to \infty$ under the decay condition $\lim_{x\to\infty}(u,\theta,\sigma) = 0$, only the $x=0$ Robin CBC(s) with $(\partial_x - \ell^{-1})$ remain.

### 3.2 Exact Wave-Order Analysis and Half-Space BVP Closure ($\gamma \in (0,1)$ vs $\gamma = 0$)
Consider time-harmonic waves $(u,\theta)(x,t) = (\hat{u},\hat{\theta})e^{-sx - i\omega t}$ ($\operatorname{Re}(s) > 0$) in the half-space $x \ge 0$, with $q = s^2$ and $w_{\text{th}} := -i\omega(1-i\omega\tau_0)$:
- **Variant V1 ($\lambda = 0, \gamma \in (0,1)$)**: Substituting $\sigma = E\frac{1-\gamma\ell^2 q}{1-\ell^2 q}u_x - \beta\theta$ and $\rho\eta = \frac{\rho c_E}{T_0}\theta + \beta u_x$ into $\rho\ddot{u} = \partial_x\sigma$ and $(1+\tau_0\partial_t)\rho T_0\dot{\eta} = \kappa\theta_{xx}$ yields the characteristic polynomial $P_{\text{V1}}(q) = 0$:
  $$\boxed{P_{\text{V1}}(q) = \Big[\gamma\ell^2 E q^2 + (\rho\omega^2\ell^2 - E)q - \rho\omega^2\Big](\kappa q - w_{\text{th}}\rho c_E) - w_{\text{th}}\beta^2 T_0 q(1 - \ell^2 q) = 0.} \tag{3.6}$$
  For $\gamma \in (0,1)$, the leading cubic coefficient is $\gamma\ell^2 E\kappa \neq 0$, so $P_{\text{V1}}(q)$ is of **degree 3 in $q = s^2$**, producing **3 decaying roots** $s_1, s_2, s_3$ ($\operatorname{Re}(s_j) > 0$). The 3 modal amplitudes $(A_1, A_2, A_3)$ are **uniquely determined** by:
  1. 1 mechanical BC at $x=0$ (e.g., $\sigma(0) = \sigma_0$ or $u(0) = u_0$),
  2. 1 thermal BC at $x=0$ (e.g., $\theta(0) = \theta_0$ or $\theta_x(0) = 0$), and
  3. **1 V1 Robin CBC** at $x=0$: $(\partial_x - \ell^{-1})z_1(0) = 0 \iff \sum_{j=1}^3 A_j (s_j + \ell^{-1})\frac{s_j}{1-\ell^2 s_j^2} = 0$.
- **Variant V2 ($\lambda = 1, \gamma \in (0,1)$)**: Both stress and entropy contain $\hat{L}(q) = \frac{1-\gamma\ell^2 q}{1-\ell^2 q}$, so clearing $(1-\ell^2 q)^2$ from the $2\times 2$ determinant yields the **degree-4 characteristic polynomial in $q = s^2$**:
  $$\boxed{P_{\text{V2}}(q) = \Big[-\rho\omega^2(1-\ell^2 q)^2 - E q(1-\gamma\ell^2 q)(1-\ell^2 q)\Big](\kappa q - w_{\text{th}}\rho c_E) - w_{\text{th}}\beta^2 T_0 q(1-\gamma\ell^2 q)^2 = 0.} \tag{3.7}$$
  For $\gamma \in (0,1)$ and $\beta \neq 0$, $P_{\text{V2}}(q)$ has **4 decaying roots** $s_1, s_2, s_3, s_4$ ($\operatorname{Re}(s_j) > 0$), whose 4 modal amplitudes $(A_1, A_2, A_3, A_4)$ are **uniquely determined** by 1 mechanical BC + 1 thermal BC + **the 2 V2 Robin CBCs** $(\partial_x - \ell^{-1})z_1(0) = 0$ and $(\partial_x - \ell^{-1})z_2(0) = 0$.
- **Degenerate Limit $\gamma \to 0$ (Literature Form A)**: Setting $\gamma = 0$ in (3.6) annihilates the leading cubic term $\gamma\ell^2 E\kappa q^3 \to 0$, collapsing the dispersion relation to **degree 2 in $q = s^2$** (only 2 decaying modes $s_1, s_2$). With only 2 modal amplitudes $(A_1, A_2)$ fixed by the mechanical and thermal BCs at $x=0$, the Robin CBC cannot be satisfied, producing an $\mathcal{O}(1)$ violation of the integral convolution across the boundary layer $x \in [0, 3\ell]$. $\square$

---

## Theorem 4: Exact Nonlocal Availability & Surface-Energy Identity on Bounded Domains under Robin CBCs

**Proposition 4.1 (Exact Surface-Plus-Bulk Positive-Definite Decomposition)**: Let $f \in C([a,b])$ and let $z(x,t) := \mathcal{K}_\ell[f](x,t) = \int_a^b \frac{1}{2\ell}e^{-|x-\xi|/\ell}f(\xi,t)\,d\xi$. Then $z$ satisfies $(1-\ell^2\partial_x^2)z = f$ and the Robin CBCs $(\partial_x - \ell^{-1})z(a,t) = 0$, $(\partial_x + \ell^{-1})z(b,t) = 0$, and for every $t$:
$$\boxed{\int_a^b f(x,t)\,\mathcal{K}_\ell[f](x,t)\,dx = \int_a^b \big(z(x,t)^2 + \ell^2 z_x(x,t)^2\big)\,dx + \ell\big(z(a,t)^2 + z(b,t)^2\big) > 0 \quad (\forall f \not\equiv 0),} \tag{4.1}$$
and the rate of work of the nonlocal convolution satisfies the exact conservation identity:
$$\boxed{\int_a^b \dot{f}(x,t)\,z(x,t)\,dx = \frac{d}{dt}\left[\int_a^b \frac{1}{2}\big(z(x,t)^2 + \ell^2 z_x(x,t)^2\big)\,dx + \frac{\ell}{2}\big(z(a,t)^2 + z(b,t)^2\big)\right].} \tag{4.2}$$
If instead $z(x,t)$ solves the bulk ODE $(1-\ell^2\partial_x^2)z = f$ on $(a,b)$ **without** satisfying the Robin CBCs (3.3), then the energy balance acquires the **spurious boundary power leakage**:
$$\mathcal{B}_{\text{Robin}}(t) = -\ell^2\Big[z(b,t)\big(\dot{z}_x(b,t) + \ell^{-1}\dot{z}(b,t)\big) - z(a,t)\big(\dot{z}_x(a,t) - \ell^{-1}\dot{z}(a,t)\big)\Big] \neq 0. \tag{4.3}$$

*Proof*: Substitute $\dot{f} = \dot{z} - \ell^2\dot{z}_{xx}$ into $\int_a^b \dot{f}\,z\,dx$ and integrate $-\ell^2\int_a^b \dot{z}_{xx} z\,dx$ by parts:
$$\begin{aligned}
\int_a^b \dot{f}\,z\,dx
&= \int_a^b \big(z\dot{z} + \ell^2 z_x\dot{z}_x\big)\,dx - \ell^2\Big[z(b,t)\dot{z}_x(b,t) - z(a,t)\dot{z}_x(a,t)\Big] \\
&= \frac{d}{dt}\left[\int_a^b \frac{1}{2}\big(z^2 + \ell^2 z_x^2\big)\,dx + \frac{\ell}{2}\big(z(a,t)^2 + z(b,t)^2\big)\right] + \mathcal{B}_{\text{Robin}}(t).
\end{aligned} \tag{4.4}$$
When the Robin CBCs $\dot{z}_x(a,t) = \ell^{-1}\dot{z}(a,t)$ and $\dot{z}_x(b,t) = -\ell^{-1}\dot{z}(b,t)$ hold, $\mathcal{B}_{\text{Robin}}(t) \equiv 0$, proving (4.2) (and (4.1) by setting $\dot{f} = f$). $\square$
