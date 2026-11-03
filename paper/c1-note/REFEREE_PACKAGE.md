# Referee Package: External Theorems and Results Used with Exact Hypotheses

This document lists every external mathematical and continuum-thermodynamic theorem or result invoked in `paper/c1-note/main.tex` (*"Thermodynamic consistency of two-phase integral nonlocal thermoelasticity: reciprocity, boundary closure and kernel normalization"*), states its **exact hypotheses**, and verifies how those hypotheses are satisfied in our formulation.

---

## 1. Schwarz's Theorem on Symmetry of Second Fréchet Derivatives (Poincaré Lemma on Hilbert Space)

- **Where used in manuscript**: Proposition 1 (`sec2_model.tex`, Eq. (10); Appendix A.1, Eqs. (50)–(52)) and Theorem 1(a) (`sec3_theorem1.tex`, Eqs. (20)–(22); Appendix A.2, Eq. (54)).
- **Statement of External Theorem**: Let $\mathcal{H} = \mathcal{H}_1 \times \mathcal{H}_2$ be a real Banach or Hilbert space, let $U \subseteq \mathcal{H}$ be open, and let $\Psi : U \to \mathbb{R}$ be twice continuously Fréchet differentiable ($\Psi \in C^2(U; \mathbb{R})$). Then for every $z = (\varepsilon, \theta) \in U$ and all perturbations $h_1 = (\delta\varepsilon_1, \delta\theta_1), h_2 = (\delta\varepsilon_2, \delta\theta_2) \in \mathcal{H}$, the bilinear second Fréchet derivative $\mathrm{D}^2\Psi(z) : \mathcal{H} \times \mathcal{H} \to \mathbb{R}$ is symmetric:
  $$\mathrm{D}^2\Psi(z)[h_1, h_2] = \mathrm{D}^2\Psi(z)[h_2, h_1].$$
  In particular, a continuous linear map $F(\varepsilon, \theta) = (A\varepsilon + B\theta, C\varepsilon + D\theta)$ on $\mathcal{H}_1 \times \mathcal{H}_2 = L^2(\Omega) \times L^2(\Omega)$ with bounded linear operators $A, B, C, D \in \mathcal{B}(L^2(\Omega))$ is the Fréchet gradient of a $C^2$ functional $\Psi[\varepsilon, \theta]$ if and only if $A = A^*$, $D = D^*$, and $C = B^*$ in $\mathcal{B}(L^2(\Omega))$.
- **Exact Hypotheses**:
  1. $\mathcal{H} = L^2(\Omega) \times L^2(\Omega)$ is a real Hilbert space with inner product $\langle(\varepsilon_1, \theta_1), (\varepsilon_2, \theta_2)\rangle_{\mathcal{H}} = \langle\varepsilon_1, \varepsilon_2\rangle_{L^2(\Omega)} + \langle\theta_1, \theta_2\rangle_{L^2(\Omega)}$.
  2. The constitutive operators $\mathcal{L}_{\text{el}}, \mathcal{L}_{\text{th}}, \mathcal{L}_\eta, \mathcal{L}_c : L^2(\Omega) \to L^2(\Omega)$ are bounded linear operators on $L^2(\Omega)$.
  3. The candidate free energy functional $\Psi : \mathcal{H} \to \mathbb{R}$ is twice Fréchet differentiable on $\mathcal{H}$.
- **Verification of Hypotheses in Manuscript**:
  - For all three kernels considered on $\Omega = [0, L]$ ($K_\ell^{\text{unnorm}}$, $W_\ell^{\text{BFP}}$, and $K_\ell^{\text{Neu}}$) as well as on $\Omega = \mathbb{R}$, the integral operator $\mathcal{K}_\ell$ is a bounded self-adjoint linear operator on $L^2(\Omega)$ with operator norm $\|\mathcal{K}_\ell\|_{\mathcal{B}(L^2(\Omega))} \le 1$ (by Young's convolution inequality on $\mathbb{R}$ and Schur's test $\sup_{x\in[0,L]}\int_0^L |\mathcal{K}_\ell(x,\xi)|\,d\xi \le 1$ on $[0, L]$).
  - Consequently, $\mathcal{L}_{\gamma,\ell} = \gamma\mathcal{I} + (1-\gamma)\mathcal{K}_\ell \in \mathcal{B}(L^2(\Omega))$ is bounded and self-adjoint on $L^2(\Omega)$.
  - Setting $h_1 = (\delta\varepsilon, 0)$ and $h_2 = (0, \delta\theta)$ in $\mathrm{D}^2\Psi(\varepsilon, \theta)[h_1, h_2] = \mathrm{D}^2\Psi(\varepsilon, \theta)[h_2, h_1]$ yields $-\beta\langle\mathcal{L}_{\text{th}}\delta\theta, \delta\varepsilon\rangle_{L^2(\Omega)} = -\beta\langle\mathcal{L}_\eta\delta\varepsilon, \delta\theta\rangle_{L^2(\Omega)}$ for all $\delta\varepsilon, \delta\theta \in L^2(\Omega)$, which holds if and only if $\mathcal{L}_\eta = \mathcal{L}_{\text{th}}^*$.

---

## 2. Eringen's (1974) Nonlocal Clausius–Duhem Inequality and Energy-Balance Localization Theorem

- **Primary Source**: A. C. Eringen, *"Theory of nonlocal thermoelasticity"*, *International Journal of Engineering Science*, Vol. 12, No. 12, pp. 1063–1077 (1974), Section 2 (Eqs. (2.4)–(2.14)) and Section 3 (Eqs. (3.7)–(3.15)).
- **Where used in manuscript**: Section 1.1 (`sec1_introduction.tex`, Eq. (2)), Section 2.2 (`sec2_model.tex`, Eqs. (7)–(13)), and Section 3.1 (`sec3_theorem1.tex`).
- **Statement of External Theorem**: In a nonlocal thermoelastic body $\Omega$ where the local balances of energy and entropy contain nonlocality residuals $\hat{e}(x,t)$ and $\hat{h}(x,t)$ subject to the zero-body-average constraints $\int_\Omega \hat{e}\,dx = 0$ and $\int_\Omega \hat{h}\,dx = 0$, the global Second Law of Thermodynamics over the isolated body $\Omega$ requires
  $$\mathcal{D}_{\text{global}}(t) := \int_\Omega \left[-\rho(\dot{\psi} + \eta\dot{T}) + \sigma\dot{\varepsilon} - \frac{q}{T}\partial_x T\right]dx \ge 0$$
  for all independent admissible histories $(\varepsilon(x,t), \theta(x,t))$. For a quadratic nonlocal Helmholtz free energy functional $\Psi[\varepsilon, \theta]$ with symmetric kernels ($\alpha(|x-\xi|) = \alpha(|\xi-x|)$), the constitutive laws $\sigma = \delta\Psi/\delta\varepsilon$ and $\rho\eta = -\delta\Psi/\delta\theta$ ensure $\frac{d}{dt}\Psi[\varepsilon, \theta] = \int_\Omega (\sigma\dot{\varepsilon} - \rho\eta\dot{\theta})\,dx$ identically, reducing $\mathcal{D}_{\text{global}}(t)$ to $\int_\Omega (-\frac{q}{T}\partial_x T)\,dx \ge 0$.
- **Exact Hypotheses**:
  1. Small-strain kinematics $\varepsilon = \partial_x u$ and linearized temperature increment $|\theta|/T_0 \ll 1$ around uniform reference temperature $T_0 > 0$.
  2. Symmetry of the two-point attenuation kernels $\mathcal{K}_\ell(x, \xi) = \mathcal{K}_\ell(\xi, x)$ on $\Omega \times \Omega$.
  3. Zero global energy and entropy production by internal nonlocal interactions: $\int_\Omega \hat{e}\,dx = 0$ and $\int_\Omega \hat{h}\,dx = 0$.
- **Verification of Hypotheses in Manuscript**:
  - Equations (1)–(3) in `main.tex` specify linearized kinematics and temperature variations $|\theta|/T_0 \ll 1$.
  - Every kernel in Section 5.1 ($K_\ell^{\text{unnorm}}$, $W_\ell^{\text{BFP}}$, $K_\ell^{\text{Neu}}$) satisfies $\mathcal{K}_\ell(x, \xi) = \mathcal{K}_\ell(\xi, x)$ for all $(x, \xi) \in [0, L]^2$, verified symbolically and numerically in `paper/c1-hardening-2/artifact_test.py` (`max |B_ij - B_ji| <= 3.25e-19`).

---

## 3. Equivalence of Integral Convolution and Second-Order Differential Operator with Robin/Neumann CBCs on $[0, L]$

- **Primary Sources**:
  - J. Fernández-Sáez, R. Zaera, J. A. Loya, and J. N. Reddy, *"Bending of Euler–Bernoulli beams using Eringen's integral formulation: a paradox resolved"*, *International Journal of Engineering Science*, Vol. 99, pp. 107–116 (2016), Section 2 (Eqs. (11)–(17)).
  - G. Romano, R. Barretta, M. Diaco, and F. Marotti de Sciarra, *"Constitutive boundary conditions for nonlocal integral models"*, *International Journal of Mechanical Sciences*, Vol. 121, pp. 151–156 (2017), Section 3 (Proposition 3.1, Eqs. (20)–(25)).
  - A. Nobili and R. Pramanik, *"Two-phase nonlocal integral elasticity as a natural framework for mechanics at the nanoscale"*, *International Journal of Engineering Science*, Vol. 215, Art. 104314 (2025), Sections 2–3.
- **Where used in manuscript**: Section 2.1 (`sec2_model.tex`, Eq. (6)) and Section 5.2 (Theorem 3, `sec5_boundary_closure.tex`, Eqs. (40)–(45); Appendix A.4, Eqs. (62)–(64)).
- **Statement of External Theorem**: Let $f \in L^2(0, L)$ and define $w(x) := \int_0^L \frac{1}{2\ell}\mathrm{e}^{-|x-\xi|/\ell} f(\xi)\,d\xi$. Then $w \in H^2(0, L)$ and $w$ is the unique solution in $H^2(0, L)$ of the boundary-value problem
  $$\begin{cases}
    (1 - \ell^2\partial_x^2)w(x) = f(x), & x \in (0, L), \\
    w'(0) - \dfrac{1}{\ell}w(0) = 0, & x = 0, \\[4pt]
    w'(L) + \dfrac{1}{\ell}w(L) = 0, & x = L.
  \end{cases}$$
  For the two-phase operator $g(x) = \gamma f(x) + (1-\gamma)w(x)$ ($\gamma \in (0, 1)$, $f \in H^2(0, L)$), eliminating $w = \frac{g - \gamma f}{1-\gamma}$ yields the equivalent second-order ODE $(1 - \ell^2\partial_x^2)g = (1 - \gamma\ell^2\partial_x^2)f$ on $(0, L)$ together with the two endpoint Constitutive Boundary Conditions $(\partial_x \mp \ell^{-1})(g - \gamma f)|_{x=0,L} = 0$.
- **Exact Hypotheses**:
  1. Bounded interval $\Omega = (0, L)$ with $0 < L < \infty$ and attenuation length $\ell > 0$.
  2. Source field $f \in L^2(0, L)$ (for the pure integral $w \in H^2(0, L)$) and $f \in H^2(0, L)$ (for the two-phase field $g = \gamma f + (1-\gamma)w \in H^2(0, L)$).
  3. Two-phase parameter $\gamma \in [0, 1)$.
- **Verification of Hypotheses in Manuscript**:
  - In Theorem 3 (`sec5_boundary_closure.tex`) and Appendix A.4, $\Omega = [0, L]$ with $0 < \ell < \infty$, $\gamma \in (0, 1)$, and $f \in H^2(0, L)$ ($f = E\varepsilon - \beta\theta$ for Variant V1, $f = E\varepsilon$ for Variant V2).
  - Theorem 3 extends this exact elimination to the BFP-normalized kernel $W_\ell^{\text{BFP}}$ (where $w = \frac{g - \gamma_{\text{eff}}(x)f}{1-\gamma}$) and the Neumann Green's function $K_\ell^{\text{Neu}}$ (where $w$ satisfies $(1 - \ell^2\partial_x^2)w = f$ with homogeneous Neumann endpoint conditions $w'(0) = w'(L) = 0$).

---

## 4. Lax–Milgram Coercivity and Uniqueness for the Two-Phase Operator $\mathcal{L}_{\gamma,\ell}$ on $L^2(\Omega)$

- **Primary Sources**:
  - G. Mikhasev and A. Nobili, *"On the solution of the purely nonlocal theory of beam elasticity as a limiting case of the two-phase theory"*, *International Journal of Solids and Structures*, Vol. 190, pp. 47–57 (2020), Section 2.
  - A. Nobili and R. Pramanik, *Mechanics of Time-Dependent Materials*, Vol. 29, Art. 30 (2025).
- **Where used in manuscript**: Section 2.1 (`sec2_model.tex`, Eq. (5)), Section 5.1 (`sec5_boundary_closure.tex`, Eq. (39)), and Appendix A.4 (proof of Corollary 1).
- **Statement of External Theorem**: Let $\mathcal{K}_\ell : L^2(\Omega) \to L^2(\Omega)$ be a bounded self-adjoint positive-semidefinite integral operator ($\langle\mathcal{K}_\ell f, f\rangle_{L^2(\Omega)} \ge 0$ for all $f \in L^2(\Omega)$). Then for every $\gamma \in (0, 1)$, the two-phase operator $\mathcal{L}_{\gamma,\ell} = \gamma\mathcal{I} + (1-\gamma)\mathcal{K}_\ell$ is self-adjoint and strictly coercive on $L^2(\Omega)$:
  $$\langle\mathcal{L}_{\gamma,\ell}[f], f\rangle_{L^2(\Omega)} = \gamma\|f\|_{L^2(\Omega)}^2 + (1-\gamma)\langle\mathcal{K}_\ell[f], f\rangle_{L^2(\Omega)} \ge \gamma\|f\|_{L^2(\Omega)}^2 \qquad \forall\,f \in L^2(\Omega).$$
  By the Lax–Milgram theorem (or the Riesz representation theorem for coercive self-adjoint operators), $\mathcal{L}_{\gamma,\ell} : L^2(\Omega) \to L^2(\Omega)$ is a bijection with bounded inverse $\|\mathcal{L}_{\gamma,\ell}^{-1}\|_{\mathcal{B}(L^2(\Omega))} \le \gamma^{-1}$.
- **Exact Hypotheses**:
  1. $\gamma \in (0, 1)$.
  2. $\mathcal{K}_\ell$ is bounded, self-adjoint, and positive-semidefinite on $L^2(\Omega)$.
- **Verification of Hypotheses in Manuscript**:
  - For $K_\ell^{\text{unnorm}}(x, \xi) = \frac{1}{2\ell}\mathrm{e}^{-|x-\xi|/\ell}$, its Fourier transform on $\mathbb{R}$ is $\hat{K}_\ell(k) = (1 + \ell^2 k^2)^{-1} > 0$, so by Plancherel's theorem $\langle K_\ell^{\text{unnorm}}\tilde{f}, \tilde{f}\rangle_{L^2(\mathbb{R})} = \frac{1}{2\pi}\int_{\mathbb{R}} \frac{|\hat{\tilde{f}}(k)|^2}{1+\ell^2 k^2}\,dk \ge 0$ for the zero-extension $\tilde{f} = f\mathbf{1}_{[0,L]} \in L^2(\mathbb{R})$, proving positive-semidefiniteness on $L^2(0, L)$.
  - For $W_\ell^{\text{BFP}}$, $\langle W_\ell^{\text{BFP}}f, f\rangle_{L^2(0,L)} = \langle K_\ell^{\text{unnorm}}f, f\rangle_{L^2(0,L)} + \int_0^L \vartheta_\ell(x)f(x)^2\,dx \ge 0$ since $\vartheta_\ell(x) = \frac{1}{2}(\mathrm{e}^{-x/\ell} + \mathrm{e}^{-(L-x)/\ell}) > 0$.
  - For $K_\ell^{\text{Neu}}$, its cosine eigenwerte on $L^2(0, L)$ are $(1 + (n\pi\ell/L)^2)^{-1} > 0$ for all $n \ge 0$, so $\langle K_\ell^{\text{Neu}}f, f\rangle_{L^2(0,L)} \ge 0$.

---

## 5. Singular Perturbation of Polynomial Roots for $\gamma \to 0^+$ (Puiseux / Implicit Function Theorem Expansion)

- **Primary Source**: Standard algebraic singular perturbation theory (applied in G. Mikhasev and A. Nobili, *Int. J. Solids Struct.*, Vol. 190, pp. 47–57, 2020, Section 3).
- **Where used in manuscript**: Theorem 2(b) (`sec4_mode_count.tex`, Eq. (33); Appendix A.3, Eq. (61)).
- **Statement of External Theorem**: Consider a polynomial family $P(q; \gamma) = \sum_{m=0}^4 a_m(\gamma)q^m$ whose coefficients $a_m(\gamma)$ are smooth functions of $\gamma \in [0, 1)$ such that $a_4(\gamma) = \gamma c_4$ ($c_4 \neq 0$) and $a_3(0) \neq 0$. Under the rescaling $Q = \gamma\ell^2 q$, the rescaled polynomial $\tilde{P}(Q; \gamma) := \gamma^3 P(Q/(\gamma\ell^2); \gamma)$ satisfies $\tilde{P}(Q; 0) = Q^3(c_4\ell^{-8}Q + a_3(0)\ell^{-6})$. If $Q_4(0) = -\frac{\ell^2 a_3(0)}{c_4} \neq 0$ is a simple root of $\tilde{P}(Q; 0)$ ($\partial_Q\tilde{P}(Q_4(0); 0) \neq 0$), then by the Analytic Implicit Function Theorem there exists a unique analytic branch $Q_4(\gamma) = Q_4(0) + \gamma Q_4'(0) + \frac{1}{2}\gamma^2 Q_4''(0) + O(\gamma^3)$ for sufficiently small $|\gamma|$, yielding the singular root $q_4(\gamma) = \frac{Q_4(\gamma)}{\gamma\ell^2} = O(\gamma^{-1})$.
- **Exact Hypotheses**:
  1. $a_4(\gamma) = \gamma\ell^4 E\kappa$ with $\ell, E, \kappa > 0$.
  2. Non-degeneracy of the cubic limit coefficient: $a_3(0) = \ell^2\kappa(E - \rho\omega^2\ell^2) \neq 0$, i.e., $\omega \neq c_0/\ell$.
  3. Simplicity of the root $Q_4(0) = -1$ of $\tilde{P}(Q; 0) = E\kappa Q^3(1+Q) = 0$: $\partial_Q\tilde{P}(-1; 0) = -E\kappa \neq 0$.
- **Verification of Hypotheses in Manuscript**:
  - In Theorem 2(b) (`sec4_mode_count.tex`, Eq. (33)) and Appendix A.3 (Eq. (61)), the non-resonance hypothesis $\omega \neq c_0/\ell$ is stated explicitly.
  - At $Q_4(0) = -1$, $\partial_Q\tilde{P}(-1; 0) = -E\kappa < 0$, so the Implicit Function Theorem applies directly and yields Eq. (33), verified symbolically by `sympy` and numerically to machine precision in `paper/c1-hardening/verify_c1.py` (`test_c1.py`).
