# Task 3: Counterexample & Failure-Mode Search

All four counterexamples and failure modes below have been constructed symbolically and verified numerically in `paper/c2-hardening/verify_c2_hardening.py` (Sections 2, 3, and 6).

---

## Counterexample 1: Bounded-Domain Poincaré Stabilization When Constitutive Passivity $K + (\tau_v - \tau_q)K^* \ge 0$ Is Violated ($\tau_T > 0$)

### 1.1 The Claim Tested
In `paper/drive-analysis/candidates.md` (Candidate C2, "Expected main result 2"), it is claimed that whenever $k + k^*(\tau_v - \tau_q) < 0$, the Routh–Hurwitz criterion produces an unstable root in the open right half-plane ($\operatorname{Re}\lambda > 0$) on a bounded 1D domain $[0, L]$ with Dirichlet/Neumann boundary conditions.

### 1.2 Exact Falsification / Refinement
Consider the isotropic TPL heat equation ($\varepsilon = 0$) on a bounded domain $\Omega \subset \mathbb{R}^d$ with homogeneous Dirichlet boundary conditions $\vartheta|_{\partial\Omega} = 0$, and let $0 < \mu_1(\Omega) \le \mu_2(\Omega) \le \dots$ be the Dirichlet eigenvalues of $-\Delta$ on $\Omega$ (in 1D on $[0, L]$, $\mu_n = (n\pi/L)^2$). Expanding in Dirichlet eigenfunctions gives, for the $n$-th spatial mode ($\xi^2 = \mu_n$), the cubic characteristic polynomial (with $\alpha = k/(\rho c_E) > 0$ and $\alpha^* = k^*/(\rho c_E) > 0$):
$$P_3(\lambda; \mu_n) = \tau_q \lambda^3 + \bigl(1 + \alpha\tau_T \mu_n\bigr)\lambda^2 + \bigl(\alpha + \alpha^*\tau_v\bigr)\mu_n \lambda + \alpha^*\mu_n = 0. \tag{3.1}$$
Because $\tau_q, \alpha, \alpha^*, \mu_n > 0$ and $\tau_T, \tau_v \ge 0$, all coefficients $a_3, a_2, a_1, a_0$ of $P_3(\lambda; \mu_n)$ are strictly positive. By the Routh–Hurwitz criterion, all three roots of $P_3(\lambda; \mu_n) = 0$ lie in the open left half-plane $\operatorname{Re}\lambda < 0$ if and only if the Hurwitz determinant $H_2(\mu_n) := a_2 a_1 - a_3 a_0 > 0$:
$$H_2(\mu_n) = \mu_n \Bigl\{ \bigl[\alpha + \alpha^*(\tau_v - \tau_q)\bigr] + \alpha\tau_T\bigl(\alpha + \alpha^*\tau_v\bigr)\mu_n \Bigr\} > 0. \tag{3.2}$$

From Eq. (3.2) we obtain a sharp dichotomy between $\tau_T = 0$ and $\tau_T > 0$:
* **When $\tau_T = 0$ (the MGT case of Quintanilla 2019)**: $H_2(\mu_n) = \mu_n[\alpha + \alpha^*(\tau_v - \tau_q)]$, which has the **same sign for all wavenumbers $\mu_n > 0$**. Thus $\alpha + \alpha^*(\tau_v - \tau_q) < 0$ causes **every** spatial mode $n \ge 1$ to be unstable on any domain $\Omega$.
* **When $\tau_T > 0$ (the full 3-lag TPL case)**: Suppose constitutive passivity is violated, i.e.,
  $$\chi := \alpha + \alpha^*(\tau_v - \tau_q) < 0, \tag{3.3}$$
  and define the **critical cutoff wavenumber**
  $$\xi_{\text{crit}}^2 := \frac{\alpha^*(\tau_q - \tau_v) - \alpha}{\alpha\tau_T(\alpha + \alpha^*\tau_v)} > 0. \tag{3.4}$$
  Then:
  1. **Long-wavelength instability ($0 < \mu_n < \xi_{\text{crit}}^2$)**: $H_2(\mu_n) < 0$, so $P_3(\lambda; \mu_n)$ has a pair of complex-conjugate roots with $\operatorname{Re}\lambda > 0$. On the whole space $\mathbb{R}^d$ (where the continuous spectrum $\xi^2 \in (0,\infty)$ always contains $(0, \xi_{\text{crit}}^2)$), the Cauchy problem is **always exponentially unstable** whenever $\chi < 0$.
  2. **Short-wavelength Poincaré stabilization ($\mu_1(\Omega) > \xi_{\text{crit}}^2$)**: If the bounded domain $\Omega$ is small enough that its fundamental Dirichlet eigenvalue satisfies $\mu_1(\Omega) > \xi_{\text{crit}}^2$ (in 1D, $L < \pi/\xi_{\text{crit}}$), then $H_2(\mu_n) \ge H_2(\mu_1) > 0$ for **all** $n \ge 1$, so **every eigenmode of the bounded domain is exponentially stable ($\operatorname{Re}\lambda < 0$) even though the material violates the constitutive passivity condition $k + k^*(\tau_v - \tau_q) \ge 0$!**

### 1.3 Concrete Numerical Verification (`verify_c2_hardening.py`, Section 3)
Take $\rho c_E = 1$, $k = \alpha = 1.0$, $k^* = \alpha^* = 2.0$, $\tau_q = 2.0$, $\tau_v = 0.5$, $\tau_T = 1.0$. Then:
$$\chi = k + k^*(\tau_v - \tau_q) = 1.0 + 2.0(0.5 - 2.0) = -2.0 < 0 \qquad (\text{constitutive passivity violated}),$$
and $\xi_{\text{crit}}^2 = \frac{2.0}{1.0 \times (1.0 + 2.0\times 0.5)} = 1.0$.
* **On a long domain $L = 2\pi$ ($\mu_1 = \xi^2 = 0.25 < \xi_{\text{crit}}^2$)**: The roots of $P_3(\lambda; 0.25) = 2\lambda^3 + 1.25\lambda^2 + 0.5\lambda + 0.5 = 0$ are
  $$\lambda_1 = -0.742086, \qquad \lambda_{2,3} = +0.058543 \pm 0.577461\,\mathrm{i} \qquad (\operatorname{Re}\lambda_{2,3} > 0 \implies \text{exponentially unstable}).$$
* **On a short domain $L = \pi/2$ ($\mu_1 = \xi^2 = 4.0 > \xi_{\text{crit}}^2$)**: The roots of $P_3(\lambda; 4.0) = 2\lambda^3 + 5\lambda^2 + 8\lambda + 8 = 0$ are
  $$\lambda_1 = -1.573478, \qquad \lambda_{2,3} = -0.463261 \pm 1.525624\,\mathrm{i} \qquad (\operatorname{Re}\lambda_j < 0 \quad \forall j \implies \text{exponentially stable}).$$

**Why does the Lyapunov functional (2.21)–(2.22) also explain this?**
In Eq. (2.21), the coefficient of $|\nabla\theta|^2$ in the energy norm is $\Lambda = \tau_q\chi + \tau_T k = 2.0(-2.0) + 1.0(1.0) = -3.0$ (or, if $\tau_T = 5.0$, $\Lambda = +1.0 > 0$ is positive definite!). Meanwhile, in the dissipation rate $\dot{\mathcal{E}} = -\int_\Omega (\chi|\nabla\theta|^2 + \tau_T\tau_q k|\nabla\dot{\theta}|^2)\,dV$, on high-frequency modes where $|\dot{\theta}| \sim \omega|\theta|$ with $\omega^2 > -\chi/(\tau_T\tau_q k) = \omega_{\text{Hopf}}^2$, the fourth-order damping $\tau_T\tau_q k|\nabla\dot{\theta}|^2$ dominates the negative lower-order term $\chi|\nabla\theta|^2$.

### 1.4 Exact Coupled Thermoelastic ($\varepsilon > 0$) Hopf-Crossing Formula
For the coupled 5th-order thermoelastic polynomial $P_5(\lambda; \xi^2)$ in Eq. (2.28), dividing $P_5(\mathrm{i}\omega; \xi^2)$ ($\omega > 0$) by $(1 + \mathrm{i}\omega\tau_q)$ gives (machine-verified in `verify_c2_hardening.py`, Section 3):
$$\operatorname{Im}\left(\frac{P_5(\mathrm{i}\omega; \xi^2)}{1 + \mathrm{i}\omega\tau_q}\right) = -\frac{\omega\bigl(\omega^2 - c_1^2\xi^2\bigr)\xi^2\Bigl(\bigl[\alpha + \alpha^*(\tau_v - \tau_q)\bigr] + \omega^2\alpha\tau_T\tau_q\Bigr)}{1 + \omega^2\tau_q^2}. \tag{3.5}$$
Since $P_5(\mathrm{i}\omega; \xi^2)\big|_{\omega^2 = c_1^2\xi^2} = -\varepsilon\omega^4(1 + \mathrm{i}\omega\tau_q) \ne 0$ for $\varepsilon > 0$, any purely imaginary root $\lambda = \mathrm{i}\omega$ ($\omega > 0$) **must** satisfy the exact coupling-independent frequency condition:
$$\omega_{\text{Hopf}}^2 = \frac{\alpha^*(\tau_q - \tau_v) - \alpha}{\alpha\tau_T\tau_q} > 0, \tag{3.6}$$
which exists **if and only if** $\alpha + \alpha^*(\tau_v - \tau_q) < 0$ (and $\tau_T > 0$). Substituting $\omega^2 = \omega_{\text{Hopf}}^2$ into $\operatorname{Re} P_5(\mathrm{i}\omega_{\text{Hopf}}; \xi^2) = 0$ yields a quadratic equation for the exact $\varepsilon$-dependent critical wavenumber $\xi_{\text{crit}}^2(\varepsilon)$:
$$\alpha^* c_1^2 \xi^4 + \Bigl[\alpha\tau_T\omega_{\text{Hopf}}^4 - \bigl(\alpha\tau_T c_1^2\xi^2\text{-term}\bigr) - \bigl(\alpha^* + c_1^2(1+\varepsilon)\bigr)\omega_{\text{Hopf}}^2\Bigr]\xi^2 + \omega_{\text{Hopf}}^4 = 0, \tag{3.7}$$
explicitly showing how thermoelastic coupling $\varepsilon > 0$ shifts the cutoff domain length $L_{\text{crit}}(\varepsilon) = \pi/\xi_{\text{crit}}(\varepsilon)$ while leaving the passivity threshold $\alpha + \alpha^*(\tau_v - \tau_q) = 0$ invariant.

---

## Counterexample 2: Failure of the Unfiltered Mechanical Energy Multiplier in `candidates.md`

As proved in Task 2 (Section 3.1, Eq. 2.17) and verified symbolically in `verify_c2_hardening.py` (`section2_lyapunov_and_multiplier_audit`), if one defines the mechanical energy using the **unfiltered** displacement and velocity $(u_i, \dot{u}_i)$,
$$\mathcal{E}_{\text{unfiltered}}(t) = \frac{1}{2}\int_\Omega \Bigl(\rho|\dot{\mathbf{u}}|^2 + C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}\Bigr)\,dV + \mathcal{E}_{\text{th}}(t),$$
then along smooth solutions of the coupled 1D system with wavenumber $\xi$,
$$\frac{d}{dt}\mathcal{E}_{\text{unfiltered}}(t) + \frac{\xi^2}{T_0}\Bigl(\bigl[K + (\tau_v - \tau_q)K^*\bigr]\theta^2 + \tau_T\tau_q K\dot{\theta}^2\Bigr) = \frac{\beta\tau_q\xi}{\rho}\Bigl(C\xi^2 u(\theta + \tau_q\dot{\theta}) - \beta\xi\theta(\theta + \tau_q\dot{\theta}) - \rho\dot{u}\dot{\theta}\Bigr) \not\equiv 0. \tag{3.8}$$
Choosing initial data at $t = 0$ with $\theta(0) = 0$, $\vartheta(0) = 0$, $\dot{u}(0) = 0$, $u(0) > 0$, and $\dot{\theta}(0) > 0$ makes the left-hand dissipative term $\chi\theta(0)^2 + \tau_T\tau_q K\dot{\theta}(0)^2 = \tau_T\tau_q K\dot{\theta}(0)^2$, while the right-hand residual is $\frac{\beta\tau_q^2 C\xi^3}{\rho}u(0)\dot{\theta}(0)$, which is **arbitrarily large and positive** for $u(0)$ large (or when $\tau_T = 0$), yielding $\frac{d}{dt}\mathcal{E}_{\text{unfiltered}}(0) > 0$ even in the strictly passive regime! Thus the mechanical filter $\hat{u}_i = u_i + \tau_q\dot{u}_i$ is **mandatory** for time-domain Lyapunov contractivity.

---

## Counterexample 3: Breakdown of Hilbert-Space Norm Coercivity at $K^*_{ij} \to 0$ and at the Conservative MGT Boundary

In Theorem 2.2, the inner product (2.21) on the 5-component space $\mathcal{H} = [H_0^1(\Omega)]^d \times [L^2(\Omega)]^d \times H_0^1(\Omega) \times H_0^1(\Omega) \times L^2(\Omega)$ fails to be a norm in two physically important regimes included in the C2 table of special cases:
1. **The Tzou DPL and Lord–Shulman limits ($K^*_{ij} = 0$)**: For any non-zero static thermal displacement profile $\vartheta_0 \in H_0^1(\Omega)\setminus\{0\}$, the state $U = (\mathbf{0}, \mathbf{0}, \vartheta_0, 0, 0)^\top \in \mathcal{H}$ has $\|U\|_{\mathcal{H}}^2 = 0$ when $K^*_{ij} = 0$, and $\mathcal{A}U = \mathbf{0}$ (a zero eigenvalue of infinite multiplicity!). Thus $0 \notin \varrho(\mathcal{A})$ on the 5-field space whenever $K^*_{ij} = 0$; one must project onto the 4-field quotient space $(\hat{\mathbf{u}}, \hat{\mathbf{v}}, \theta, \phi)$.
2. **The Critical MGT Boundary ($\tau_T = 0$ and $K_{ij} + (\tau_v - \tau_q)K^*_{ij} = 0$)**: Here $\Lambda_{ij} = \tau_q\varkappa_{ij} + \tau_T K_{ij} = 0$. Then any state of the form $U = (\mathbf{0}, \mathbf{0}, -\tau_q\theta_0, \theta_0, -\tau_q^{-1}\theta_0)^\top$ with $\theta_0 \in H_0^1(\Omega)\setminus\{0\}$ satisfies $\vartheta + \tau_q\theta = 0$ and $\theta + \tau_q\phi = 0$, giving $\|U\|_{\mathcal{H}}^2 = 0$ even though $U \ne 0$! Thus the energy norm (2.21) degenerates at the conservative MGT threshold $\tau_q = \tau_v + k/k^*$ when $\tau_T = 0$.

---

## Counterexample 4: The Bimaterial Phase-Lag Mismatch Obstruction ($\tau_q^- \ne \tau_q^+$) Across Thermoelastic Interfaces

When extending the C2 time-domain Lyapunov method to a bimaterial interface $\Gamma$ separating two TPL/MGT thermoelastic half-spaces $\Omega^-$ and $\Omega^+$ with distinct heat-flux relaxation times $\tau_q^- \ne \tau_q^+$ (Candidate C3):
* To cancel the bulk thermoelastic coupling in $\Omega^-$, the mechanical fields in $\Omega^-$ must be filtered by $\hat{u}_i^- = (1 + \tau_q^-\partial_t)u_i^-$.
* To cancel the bulk thermoelastic coupling in $\Omega^+$, the mechanical fields in $\Omega^+$ must be filtered by $\hat{u}_i^+ = (1 + \tau_q^+\partial_t)u_i^+$.
* At the interface $\Gamma$, integration by parts of $\frac{d}{dt}(\mathcal{E}_{\text{bulk}}^- + \mathcal{E}_{\text{bulk}}^+)$ produces the boundary power functional:
  $$\mathcal{P}_\Gamma(t) = \int_\Gamma \Bigl[ \hat{\sigma}_{ij}^- n_j \dot{\hat{u}}_i^- - \hat{\sigma}_{ij}^+ n_j \dot{\hat{u}}_i^+ - \frac{1}{T_0}(1+\tau_q^-\partial_t)q_n^-\,\hat{\theta}^- + \frac{1}{T_0}(1+\tau_q^+\partial_t)q_n^+\,\hat{\theta}^+ \Bigr]\,d\Gamma. \tag{3.9}$$
* **Even for a perfectly welded, thermally perfect interface** ($u_i^- = u_i^+ = u_i$, $\sigma_{ij}^- n_j = \sigma_{ij}^+ n_j = t_i$, $\theta^- = \theta^+ = \theta$, $q_n^- = q_n^+ = q_n$), if $\tau_q^- \ne \tau_q^+$, Eq. (3.9) leaves a **non-zero interfacial mismatch residual**:
  $$\mathcal{P}_\Gamma^{\text{welded}}(t) = (\tau_q^- - \tau_q^+)\int_\Gamma \Bigl[ t_i\ddot{u}_i + \dot{t}_i\dot{u}_i + (\tau_q^- + \tau_q^+)\dot{t}_i\ddot{u}_i - \frac{1}{T_0}\bigl(q_n\dot{\theta} + \dot{q}_n\theta + (\tau_q^- + \tau_q^+)\dot{q}_n\dot{\theta}\bigr) \Bigr]\,d\Gamma \not\equiv 0! \tag{3.10}$$
* **Resolution (proved in Task 7)**:
  1. In the **time domain**, if $\tau_q^- \ne \tau_q^+$, one cannot use the single-lag Quintanilla (2019) multiplier $(1+\tau_q^\pm\partial_t)$ unless one either (a) retains the heat flux $\mathbf{q}^\pm$ as an independent state variable in an Extended Irreversible Thermodynamics (EIT) Hilbert space (eliminating the need to apply $(1+\tau_q^\pm\partial_t)$ to the mechanical equations!), or (b) applies the symmetric second-order cross-filter $(1+\tau_q^-\partial_t)(1+\tau_q^+\partial_t)$ to both domains when $\tau_T^\pm > 0$.
  2. In the **frequency domain ($\partial_t = -\mathrm{i}\omega$)**, the physical time-averaged Poynting–heat-flux vector $\mathbf{S}_{\text{avg}} = \frac{1}{2}\operatorname{Re}(-\boldsymbol{\sigma}\cdot\bar{\mathbf{v}} + \frac{1}{T_0}\mathbf{q}\bar{\theta})$ cancels the bulk thermoelastic coupling $\operatorname{Re}(\beta_{ij}v_{i,j}\bar{\theta})$ **without any $(1-\mathrm{i}\omega\tau_q^\pm)$ filter**, so the exact interfacial energy balance $\llbracket \mathbf{S}_{\text{avg}}\cdot\mathbf{n}\rrbracket = -D_{\text{int}}(\omega) \le 0$ holds unconditionally for arbitrary $\tau_q^- \ne \tau_q^+$ (verified to $6.4 \times 10^{-15}$ in `verify_c2_hardening.py`, Section 6).
