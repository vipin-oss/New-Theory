# Task 2: Step-by-Step Derivation & Edge-Case Audit

All symbolic derivations in this document have been machine-verified in `paper/c2-hardening/verify_c2_hardening.py` (using SymPy and NumPy) and tested via `pytest` in `paper/c2-hardening/test_c2_hardening.py`.

---

## 1. Governing Equations and State-Space Formulation

Let $\Omega \subset \mathbb{R}^d$ ($d \in \{1,2,3\}$) be a bounded Lipschitz domain with boundary $\partial\Omega$. The linearized equations of anisotropic homogeneous three-phase-lag (TPL) / Green–Naghdi Type-III thermoelasticity (`review paper.pdf`, Eqs. 5–7 and 14) are:

1. **Balance of linear momentum**:
   $$\rho \ddot{u}_i = \sigma_{ij,j}, \qquad \sigma_{ij} = C_{ijkl}\varepsilon_{kl} - \beta_{ij}\theta, \qquad \varepsilon_{kl} = \frac{1}{2}(u_{k,l} + u_{l,k}), \tag{2.1}$$
   where $\rho > 0$ is the mass density, $C_{ijkl} = C_{klij} = C_{jikl}$ is a symmetric uniformly positive-definite elasticity tensor ($C_{ijkl}\varepsilon_{ij}\varepsilon_{kl} \ge c_0 |\varepsilon|^2$), and $\beta_{ij} = \beta_{ji}$ is the invertible/non-zero thermoelastic coupling tensor.

2. **Linearized entropy / energy balance**:
   $$\rho T_0 \dot{\eta} = -q_{i,i}, \qquad \rho T_0 \eta = \rho c_E \theta + T_0 \beta_{ij} u_{i,j}, \tag{2.2}$$
   where $T_0 > 0$ is the uniform reference temperature, $c_E > 0$ is the specific heat at constant strain, and $\theta = T - T_0$ is the temperature increment.

3. **Three-phase-lag (TPL) constitutive law for the heat flux** (`review paper.pdf`, Eq. 14, i.e. the $(1,1,1)$ Taylor model):
   $$\bigl(1 + \tau_q \partial_t\bigr) q_i = -K_{ij}\bigl(1 + \tau_T \partial_t\bigr)\theta_{,j} - K^*_{ij}\bigl(1 + \tau_v \partial_t\bigr)\vartheta_{,j}, \qquad \dot{\vartheta} = \theta, \tag{2.3}$$
   where $\vartheta(\mathbf{x},t) = \vartheta_0(\mathbf{x}) + \int_0^t \theta(\mathbf{x},s)\,ds$ is the Green–Naghdi thermal displacement, $K_{ij} = K_{ji} \succ 0$ is the thermal conductivity tensor, $K^*_{ij} = K^*_{ji} \succeq 0$ is the conductivity rate tensor, and $\tau_q > 0$, $\tau_T \ge 0$, $\tau_v \ge 0$ are the heat-flux, temperature-gradient, and thermal-displacement-gradient phase lags. Using $\dot{\vartheta} = \theta$, Eq. (2.3) takes the equivalent form:
   $$\bigl(1 + \tau_q \partial_t\bigr) q_i = -K^*_{ij}\vartheta_{,j} - \bigl(K_{ij} + \tau_v K^*_{ij}\bigr)\theta_{,j} - \tau_T K_{ij}\dot{\theta}_{,j}. \tag{2.4}$$

Applying $(1 + \tau_q \partial_t)$ to the energy balance (2.2) and substituting the divergence of (2.4) yields the coupled third-order-in-$\vartheta$ thermal evolution equation:
$$\rho c_E\bigl(\dot{\theta} + \tau_q\ddot{\theta}\bigr) + T_0 \beta_{ij}\bigl(\dot{u}_{i,j} + \tau_q\ddot{u}_{i,j}\bigr) = K^*_{ij}\vartheta_{,ij} + \bigl(K_{ij} + \tau_v K^*_{ij}\bigr)\theta_{,ij} + \tau_T K_{ij}\dot{\theta}_{,ij}. \tag{2.5}$$

---

## 2. Derivation 1: Frequency-Domain Passivity and Time-Domain Memory-Kernel Obstruction

### 2.1 Exact Real and Imaginary Parts of the Complex Dynamic Conductivity $G_{ij}(-\mathrm{i}\omega)$
For a time-harmonic field $\vartheta(\mathbf{x},t) = \operatorname{Re}\{\tilde{\vartheta}(\mathbf{x})e^{-\mathrm{i}\omega t}\}$ ($\omega \in \mathbb{R}\setminus\{0\}$, so $\partial_t \leftrightarrow s = -\mathrm{i}\omega$ and $\tilde{\vartheta} = \tilde{\theta}/(-\mathrm{i}\omega)$), Eq. (2.3) defines the complex dynamic thermal conductivity tensor $\tilde{q}_i = -G_{ij}(-\mathrm{i}\omega)\tilde{\theta}_{,j}$:
$$G_{ij}(-\mathrm{i}\omega) = \frac{K_{ij}(1 - \mathrm{i}\omega\tau_T) + K^*_{ij}\bigl(\frac{1}{-\mathrm{i}\omega} + \tau_v\bigr)}{1 - \mathrm{i}\omega\tau_q} = \frac{\bigl(K_{ij} + \tau_v K^*_{ij}\bigr) + \mathrm{i}\bigl(\frac{1}{\omega}K^*_{ij} - \omega\tau_T K_{ij}\bigr)}{1 - \mathrm{i}\omega\tau_q}. \tag{2.6}$$
Multiplying numerator and denominator by $(1 + \mathrm{i}\omega\tau_q)$ gives:
$$G_{ij}(-\mathrm{i}\omega) = \underbrace{\frac{\bigl[K_{ij} + (\tau_v - \tau_q)K^*_{ij}\bigr] + \omega^2 \tau_T \tau_q K_{ij}}{1 + \omega^2 \tau_q^2}}_{\operatorname{Re} G_{ij}(-\mathrm{i}\omega)} + \mathrm{i}\,\underbrace{\frac{\frac{1}{\omega}K^*_{ij} + \omega\bigl[\tau_q(K_{ij} + \tau_v K^*_{ij}) - \tau_T K_{ij}\bigr]}{1 + \omega^2 \tau_q^2}}_{\operatorname{Im} G_{ij}(-\mathrm{i}\omega)}. \tag{2.7}$$

**Theorem 2.1 (Frequency-Domain Passivity of the $(1,1,1)$ TPL Law).** *For symmetric tensors $K_{ij}, K^*_{ij}$ and $\tau_q > 0$, the time-averaged thermal dissipation rate over any harmonic cycle at frequency $\omega \in \mathbb{R}\setminus\{0\}$,*
$$\mathcal{D}_{\text{th}}(\omega) = \frac{1}{2T_0}\operatorname{Re}\bigl(\tilde{q}_i \overline{(-\tilde{\theta}_{,i})}\bigr) = \frac{1}{2T_0}\bigl(\operatorname{Re} G_{ij}(-\mathrm{i}\omega)\bigr)\tilde{\theta}_{,j}\overline{\tilde{\theta}_{,i}}, \tag{2.8}$$
*is non-negative for all $\omega \in \mathbb{R}\setminus\{0\}$ and all complex vectors $\nabla\tilde{\theta} \in \mathbb{C}^d$ if and only if both of the following matrix inequalities hold:*
$$\varkappa_{ij} := K_{ij} + (\tau_v - \tau_q)K^*_{ij} \succeq 0 \qquad \text{and} \qquad \tau_T \tau_q K_{ij} \succeq 0. \tag{2.9}$$

*Proof.* Since $1 + \omega^2\tau_q^2 > 0$ for all $\omega \in \mathbb{R}$, $\operatorname{Re} G_{ij}(-\mathrm{i}\omega) \succeq 0$ for all $\omega \in \mathbb{R}\setminus\{0\}$ is equivalent to
$$\mathbf{z}^*\bigl[K + (\tau_v - \tau_q)K^*\bigr]\mathbf{z} + \omega^2\tau_T\tau_q\,\mathbf{z}^* K \mathbf{z} \ge 0 \qquad \forall \mathbf{z} \in \mathbb{C}^d,\ \forall \omega > 0.$$
Taking the limit $\omega \to 0^+$ yields $\mathbf{z}^*[K + (\tau_v - \tau_q)K^*]\mathbf{z} \ge 0$, and dividing by $\omega^2$ and taking $\omega \to \infty$ yields $\tau_T\tau_q\,\mathbf{z}^* K \mathbf{z} \ge 0$. Sufficiency is immediate since the sum of two non-negative quadratic forms is non-negative. $\square$

### 2.2 Comparison with the $(2,1,1)$ Second-Order-in-$\tau_q$ TPL Model
For Choudhuri's (2007) $(2,1,1)$ model $\bigl(1 + \tau_q\partial_t + \frac{\tau_q^2}{2}\partial_t^2\bigr)q_i = -K_{ij}(1 + \tau_T\partial_t)\theta_{,j} - K^*_{ij}(1 + \tau_v\partial_t)\vartheta_{,j}$, replacing $(1 - \mathrm{i}\omega\tau_q)$ by $(1 - \frac{1}{2}\omega^2\tau_q^2 - \mathrm{i}\omega\tau_q)$ yields (verified symbolically in `verify_c2_hardening.py`, Section 1):
$$\operatorname{Re} G^{(2,1,1)}_{ij}(-\mathrm{i}\omega) = \frac{\bigl[K_{ij} + (\tau_v - \tau_q)K^*_{ij}\bigr] + \omega^2\tau_q\bigl[\tau_T K_{ij} - \frac{\tau_q}{2}(K_{ij} + \tau_v K^*_{ij})\bigr]}{\bigl(1 - \frac{1}{2}\omega^2\tau_q^2\bigr)^2 + \omega^2\tau_q^2}. \tag{2.10}$$
Hence $\operatorname{Re} G^{(2,1,1)}_{ij}(-\mathrm{i}\omega) \succeq 0$ for all $\omega \in \mathbb{R}\setminus\{0\}$ if and only if (Chiriţă, D'Apice & Zampoli 2016):
$$\varkappa_{ij} = K_{ij} + (\tau_v - \tau_q)K^*_{ij} \succeq 0 \qquad \text{and} \qquad \kappa_{ij} := \tau_T K_{ij} - \frac{\tau_q}{2}\bigl(K_{ij} + \tau_v K^*_{ij}\bigr) \succeq 0. \tag{2.11}$$

### 2.3 Edge-Case Audit of the DC Pole $\omega \to 0$ and the Fading-Memory Obstruction
Notice a crucial analytic subtlety in Eq. (2.7) that was overlooked in `candidates.md`:
* While $\operatorname{Re} G_{ij}(-\mathrm{i}\omega)$ has a finite limit $\frac{K_{ij} + (\tau_v - \tau_q)K^*_{ij}}{1} = \varkappa_{ij}$ as $\omega \to 0$, the imaginary part $\operatorname{Im} G_{ij}(-\mathrm{i}\omega) \sim \frac{K^*_{ij}}{\omega}$ has a **first-order pole at $\omega = 0$** whenever $K^*_{ij} \ne 0$.
* In the Laplace domain ($p \in \mathbb{C}$, $\operatorname{Re} p > 0$), partial-fraction decomposition gives (verified in `verify_c2_hardening.py`, Section 1):
  $$G_{ij}(p) = \frac{\tau_T}{\tau_q}K_{ij} + \frac{1}{p}K^*_{ij} + \frac{K_{ij}\bigl(1 - \frac{\tau_T}{\tau_q}\bigr) + (\tau_v - \tau_q)K^*_{ij}}{1 + \tau_q p}. \tag{2.12}$$
* Taking the inverse Laplace transform for $q_i(t) = -\int_0^\infty \mathcal{K}_{ij}(s)\theta_{,j}(t-s)\,ds$ (with vanishing history for $t < 0$) yields the temperature-gradient memory kernel:
  $$\mathcal{K}_{ij}(s) = \frac{\tau_T}{\tau_q}K_{ij}\,\delta(s) + \underbrace{K^*_{ij}\,H(s)}_{\notin L^1(0,\infty)} + \frac{1}{\tau_q}\Bigl[K_{ij}\Bigl(1 - \frac{\tau_T}{\tau_q}\Bigr) + (\tau_v - \tau_q)K^*_{ij}\Bigr]e^{-s/\tau_q}H(s), \tag{2.13}$$
  where $H(s)$ is the Heaviside step function.
* **Consequence**: With respect to the temperature gradient $\nabla\theta$, $\mathcal{K}_{ij}(s)$ is **NOT** a Coleman–Gurtin fading-memory kernel in $L^1(0,\infty)$ because the Green–Naghdi Type-III term $K^*_{ij} H(s)$ does not decay as $s \to \infty$; it represents a permanent thermal-displacement elastic restoring force $-K^*_{ij}\nabla\vartheta$. Only when the constitutive law is written in terms of the **thermal displacement gradient history** $\beta_j(t-s) = \vartheta_{,j}(t-s)$ by integrating (2.4) via variation of constants:
  $$q_i(\mathbf{x},t) = e^{-t/\tau_q}q_i(\mathbf{x},0) - \frac{1}{\tau_q}\int_0^t e^{-s/\tau_q}\Bigl[K^*_{ij}\vartheta_{,j}(t-s) + \bigl(K_{ij} + \tau_v K^*_{ij}\bigr)\dot{\vartheta}_{,j}(t-s) + \tau_T K_{ij}\ddot{\vartheta}_{,j}(t-s)\Bigr]\,ds, \tag{2.14}$$
  is the memory kernel exponentially decaying ($e^{-s/\tau_q} \in L^1(0,\infty)$).
* Furthermore, the naive Clausius–Duhem inequality $-\frac{q_i}{T_0}\theta_{,i} \ge 0$ with a classical local free energy $\psi(\varepsilon_{ij},\theta)$ **fails identically** whenever $\tau_q > 0$ or $K^*_{ij} > 0$, because $\psi(\varepsilon_{ij},\theta)$ lacks the state variables $(\nabla\vartheta, \nabla\theta, \dot{\theta})$ (or $q_i$) needed to absorb the reactive energy stored in the $1/\omega$ pole and the $\tau_q$ relaxation mode.

---

## 3. Derivation 2: Time-Domain Lyapunov Functional, the Mechanical Filter Trap, and Lumer–Phillips Contraction Semigroup

### 3.1 The Unfiltered Mechanical Multiplier Trap in `candidates.md`
In `candidates.md` (Candidate C2, "Expected main result 2"), the state vector was written in terms of the **unfiltered** mechanical variables $(u_i, \dot{u}_i)$ alongside $(\vartheta, \theta, \dot{\theta})$. Let us prove why multiplying the unfiltered momentum equation (2.1) by $\dot{u}_i$ and the third-order TPL heat equation (2.5) by $\frac{1}{T_0}(\theta + \tau_q\dot{\theta})$ **fails to cancel the thermoelastic coupling**:
* The mechanical power identity from (2.1) multiplied by $\dot{u}_i$ is:
  $$\frac{d}{dt}\frac{1}{2}\int_\Omega \Bigl(\rho |\dot{\mathbf{u}}|^2 + C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}\Bigr)\,dV = \int_\Omega \beta_{ij}\theta \dot{u}_{i,j}\,dV. \tag{2.15}$$
* The thermal identity from (2.5) multiplied by $\frac{1}{T_0}(\theta + \tau_q\dot{\theta})$ contains the mechanical coupling term:
  $$-\int_\Omega \beta_{ij}\bigl(\dot{u}_{i,j} + \tau_q\ddot{u}_{i,j}\bigr)\bigl(\theta + \tau_q\dot{\theta}\bigr)\,dV. \tag{2.16}$$
* Adding (2.15) and (2.16) leaves an **indefinite, sign-indeterminate coupling residual** (verified symbolically in `verify_c2_hardening.py`, Section 2):
  $$\mathcal{R}_{\text{unfiltered}}(t) = -\tau_q\int_\Omega \beta_{ij}\Bigl(\ddot{u}_{i,j}\theta + \dot{u}_{i,j}\dot{\theta} + \tau_q\ddot{u}_{i,j}\dot{\theta}\Bigr)\,dV \ne 0. \tag{2.17}$$

### 3.2 Correct Filtered State-Space Formulation and Exact Lyapunov Identity
Following Quintanilla (2019, Eqs. 3.6–3.12) and Muñoz Rivera, Ochoa Ochoa & Quintanilla (2024, Eqs. 1.1–2.14), apply the linear filter
$$\hat{f} := (1 + \tau_q \partial_t)f = f + \tau_q \dot{f}$$
to the mechanical displacement $u_i$, defining the filtered displacement $\hat{u}_i := u_i + \tau_q \dot{u}_i$ and filtered velocity $\hat{v}_i := \dot{\hat{u}}_i = \dot{u}_i + \tau_q \ddot{u}_i$, as well as $\hat{\vartheta} := \vartheta + \tau_q \theta$ and $\hat{\theta} := \theta + \tau_q \dot{\theta} = \dot{\hat{\vartheta}}$. Applying $(1 + \tau_q\partial_t)$ to the momentum equation (2.1) gives:
$$\rho \dot{\hat{v}}_i = \bigl(C_{ijkl}\hat{\varepsilon}_{kl} - \beta_{ij}(\theta + \tau_q\dot{\theta})\bigr)_{,j}, \qquad \hat{\varepsilon}_{kl} = \frac{1}{2}(\hat{u}_{k,l} + \hat{u}_{l,k}). \tag{2.18}$$
Adjoining $\phi := \dot{\theta}$, the coupled system on $\Omega \times (0,\infty)$ with homogeneous Dirichlet boundary conditions $\hat{u}_i|_{\partial\Omega} = 0$, $\vartheta|_{\partial\Omega} = 0$, $\theta|_{\partial\Omega} = 0$ is written for the 5-component state vector $U = (\hat{\mathbf{u}}, \hat{\mathbf{v}}, \vartheta, \theta, \phi)^\top$ as:
$$\frac{dU}{dt} = \mathcal{A}U = \begin{pmatrix} \hat{\mathbf{v}} \\ \frac{1}{\rho}\bigl(C_{ijkl}\hat{u}_{k,l} - \beta_{ij}(\theta + \tau_q\phi)\bigr)_{,j} \\ \theta \\ \phi \\ \frac{1}{\rho c_E \tau_q}\Bigl[-\rho c_E \phi - T_0 \beta_{ij}\hat{v}_{i,j} + K^*_{ij}\vartheta_{,ij} + (K_{ij} + \tau_v K^*_{ij})\theta_{,ij} + \tau_T K_{ij}\phi_{,ij}\Bigr] \end{pmatrix}. \tag{2.19}$$

Define the Hilbert space
$$\mathcal{H} := \bigl[H_0^1(\Omega)\bigr]^d \times \bigl[L^2(\Omega)\bigr]^d \times H_0^1(\Omega) \times H_0^1(\Omega) \times L^2(\Omega) \tag{2.20}$$
endowed with the inner product (for $U = (\hat{\mathbf{u}}, \hat{\mathbf{v}}, \vartheta, \theta, \phi)^\top$ and $U^\# = (\hat{\mathbf{u}}^\#, \hat{\mathbf{v}}^\#, \vartheta^\#, \theta^\#, \phi^\#)^\top$):
$$\begin{aligned}
\langle U, U^\#\rangle_{\mathcal{H}} := \frac{1}{2}\int_\Omega \Bigg\{ &\rho\,\hat{v}_i\overline{\hat{v}_i^\#} + C_{ijkl}\hat{\varepsilon}_{ij}\overline{\hat{\varepsilon}_{kl}^\#} + \frac{\rho c_E}{T_0}(\theta + \tau_q\phi)\overline{(\theta^\# + \tau_q\phi^\#)} \\
&+ \frac{1}{T_0}K^*_{ij}(\vartheta_{,i} + \tau_q\theta_{,i})\overline{(\vartheta^\#_{,j} + \tau_q\theta^\#_{,j})} + \frac{1}{T_0}\Bigl(\tau_q\bigl[K_{ij} + (\tau_v - \tau_q)K^*_{ij}\bigr] + \tau_T K_{ij}\Bigr)\theta_{,i}\overline{\theta^\#_{,j}} \Bigg\}\,dV,
\end{aligned} \tag{2.21}$$
and associated energy $\mathcal{E}(t) := \langle U(t), U(t)\rangle_{\mathcal{H}}$.

**Theorem 2.2 (Exact Dissipation Identity and Lumer–Phillips Contraction Semigroup).**
1. *Let $\rho, c_E, T_0, \tau_q > 0$, $C_{ijkl} \succ 0$, $K^*_{ij} \succeq 0$, and define $\varkappa_{ij} := K_{ij} + (\tau_v - \tau_q)K^*_{ij}$. For any $U \in D(\mathcal{A})$:*
   $$\frac{d}{dt}\mathcal{E}(t) = \operatorname{Re}\langle \mathcal{A}U, U\rangle_{\mathcal{H}} = -\frac{1}{2T_0}\int_\Omega \Bigl(\varkappa_{ij}\,\theta_{,i}\overline{\theta_{,j}} + \tau_T \tau_q K_{ij}\,\phi_{,i}\overline{\phi_{,j}}\Bigr)\,dV. \tag{2.22}$$
2. *The bilinear form (2.21) defines a norm on $\mathcal{H}$ equivalent to the standard product norm on $[H_0^1(\Omega)]^d \times [L^2(\Omega)]^d \times H_0^1(\Omega) \times H_0^1(\Omega) \times L^2(\Omega)$ if and only if*
   $$K^*_{ij} \succ 0 \qquad \text{and} \qquad \Lambda_{ij} := \tau_q \varkappa_{ij} + \tau_T K_{ij} = \tau_q\bigl[K_{ij} + (\tau_v - \tau_q)K^*_{ij}\bigr] + \tau_T K_{ij} \succ 0. \tag{2.23}$$
3. *Under the strict passivity conditions $\varkappa_{ij} \succeq 0$, $\tau_T\tau_q K_{ij} \succeq 0$, and the coercivity condition (2.23), the operator $\mathcal{A}$ with domain*
   $$D(\mathcal{A}) = \Bigl\{ U \in \mathcal{H} : \hat{\mathbf{v}} \in [H_0^1(\Omega)]^d,\ \phi \in H_0^1(\Omega),\ \bigl(C_{ijkl}\hat{u}_{k,l} - \beta_{ij}(\theta+\tau_q\phi)\bigr)_{,j} \in [L^2(\Omega)]^d,\ K^*_{ij}\vartheta_{,ij} + (K_{ij}+\tau_v K^*_{ij})\theta_{,ij} + \tau_T K_{ij}\phi_{,ij} \in L^2(\Omega) \Bigr\} \tag{2.24}$$
   *is densely defined, dissipative ($\operatorname{Re}\langle \mathcal{A}U, U\rangle_{\mathcal{H}} \le 0$), and satisfies $0 \in \varrho(\mathcal{A})$ (hence $\operatorname{Ran}(I - \mathcal{A}) = \mathcal{H}$). By the Lumer–Phillips theorem, $\mathcal{A}$ generates a strongly continuous semigroup of contractions $e^{t\mathcal{A}}$ on $\mathcal{H}$.*

*Proof.*
1. **Dissipation identity (2.22)**: Expanding $\operatorname{Re}\langle \mathcal{A}U, U\rangle_{\mathcal{H}}$ and integrating by parts using the boundary conditions $\hat{\mathbf{v}}|_{\partial\Omega} = \mathbf{0}$, $\theta|_{\partial\Omega} = \phi|_{\partial\Omega} = 0$:
   - The mechanical terms yield $\operatorname{Re}\int_\Omega \bigl[\beta_{ij}(\theta + \tau_q\phi)\overline{\hat{v}_{i,j}}\bigr]\,dV$.
   - The thermal capacity term $\frac{\rho c_E}{T_0}(\dot{\theta} + \tau_q\dot{\phi})\overline{(\theta + \tau_q\phi)}$ substitutes (2.5) to yield
     $$\operatorname{Re}\int_\Omega \Bigl[-\beta_{ij}\hat{v}_{i,j}\overline{(\theta + \tau_q\phi)} - \frac{1}{T_0}\bigl(K^*_{ij}\vartheta_{,j} + (K_{ij} + \tau_v K^*_{ij})\theta_{,j} + \tau_T K_{ij}\phi_{,j}\bigr)\overline{(\theta_{,i} + \tau_q\phi_{,i})}\Bigr]\,dV.$$
   - The thermoelastic coupling terms $\pm \operatorname{Re}\int_\Omega \beta_{ij}(\theta + \tau_q\phi)\overline{\hat{v}_{i,j}}\,dV$ **cancel identically**.
   - Combining the remaining thermal gradient terms with the derivatives of the $K^*_{ij}$ and $\Lambda_{ij}$ terms in (2.21) gives:
     $$\begin{aligned}
     &\operatorname{Re}\int_\Omega \Bigl[K^*_{ij}(\theta_{,i} + \tau_q\phi_{,i})\overline{(\vartheta_{,j} + \tau_q\theta_{,j})} + \bigl(\tau_q[K_{ij} + (\tau_v - \tau_q)K^*_{ij}] + \tau_T K_{ij}\bigr)\phi_{,i}\overline{\theta_{,j}} \\
     &\qquad\qquad - \bigl(K^*_{ij}\vartheta_{,i} + (K_{ij} + \tau_v K^*_{ij})\theta_{,i} + \tau_T K_{ij}\phi_{,i}\bigr)\overline{(\theta_{,j} + \tau_q\phi_{,j})}\Bigr]\,dV \\
     &= -\int_\Omega \Bigl(\bigl[K_{ij} + (\tau_v - \tau_q)K^*_{ij}\bigr]\theta_{,i}\overline{\theta_{,j}} + \tau_T\tau_q K_{ij}\phi_{,i}\overline{\phi_{,j}}\Bigr)\,dV,
     \end{aligned}$$
     where the cross terms $K^*_{ij}\vartheta_{,i}\overline{\theta_{,j}}$ and $\tau_q K^*_{ij}\vartheta_{,i}\overline{\phi_{,j}}$ and $\phi_{,i}\overline{\theta_{,j}}$ cancel identically (machine-verified in `verify_c2_hardening.py`, Section 2).
2. **Coercivity of $\langle \cdot, \cdot\rangle_{\mathcal{H}}$**: By Korn's and Poincaré's inequalities on $[H_0^1(\Omega)]^d$, $\int_\Omega C_{ijkl}\hat{\varepsilon}_{ij}\overline{\hat{\varepsilon}_{kl}}\,dV$ is equivalent to $\|\hat{\mathbf{u}}\|_{H_0^1}^2$. On the thermal components $(\vartheta, \theta, \phi)$, let $\mathbf{x} = \nabla\vartheta$ and $\mathbf{y} = \nabla\theta$. The quadratic form in $(\mathbf{x}, \mathbf{y})$ is $(\mathbf{x} + \tau_q\mathbf{y})^\top K^*(\mathbf{x} + \tau_q\mathbf{y}) + \mathbf{y}^\top \Lambda \mathbf{y}$. This block quadratic form is positive definite on $\mathbb{R}^d \times \mathbb{R}^d$ if and only if $K^* \succ 0$ and its Schur complement $\Lambda \succ 0$: specifically, by Young's inequality, for any $\delta \in (0,1)$,
   $$(\mathbf{x} + \tau_q\mathbf{y})^\top K^*(\mathbf{x} + \tau_q\mathbf{y}) + \mathbf{y}^\top \Lambda \mathbf{y} \ge (1 - \delta)\mathbf{x}^\top K^*\mathbf{x} + \mathbf{y}^\top\Bigl(\Lambda - \frac{1-\delta}{\delta}\tau_q^2 K^*\Bigr)\mathbf{y},$$
   which is strictly coercive in $|\nabla\vartheta|^2 + |\nabla\theta|^2$ for $1 - \delta > 0$ sufficiently small whenever $K^* \succ 0$ and $\Lambda \succ 0$. Similarly, $|\theta + \tau_q\phi|_{L^2}^2 + c_\Lambda \|\nabla\theta\|_{L^2}^2 \ge |\theta + \tau_q\phi|_{L^2}^2 + c_\Lambda \mu_1(\Omega)\|\theta\|_{L^2}^2$ controls $\|\theta\|_{H_0^1}^2 + \|\phi\|_{L^2}^2$ since $\tau_q > 0$.
3. **Surjectivity $0 \in \varrho(\mathcal{A})$**: Given $F = (\mathbf{f}_1, \mathbf{f}_2, f_3, f_4, f_5)^\top \in \mathcal{H}$, solving $\mathcal{A}U = F$ gives immediately from the 1st, 3rd, and 4th rows:
   $$\hat{\mathbf{v}} = \mathbf{f}_1 \in [H_0^1(\Omega)]^d, \qquad \theta = f_3 \in H_0^1(\Omega), \qquad \phi = f_4 \in H_0^1(\Omega). \tag{2.25}$$
   Substituting $(\theta, \phi) = (f_3, f_4)$ into the 2nd row gives the decoupled elliptic elasticity system for $\hat{\mathbf{u}} \in [H_0^1(\Omega)]^d$:
   $$-\bigl(C_{ijkl}\hat{u}_{k,l}\bigr)_{,j} = -\rho f_{2,i} - \bigl(\beta_{ij}(f_3 + \tau_q f_4)\bigr)_{,j} \in [H^{-1}(\Omega)]^d, \tag{2.26}$$
   which has a unique solution $\hat{\mathbf{u}} \in [H_0^1(\Omega)]^d$ by Lax–Milgram (since $C_{ijkl}$ is symmetric positive definite and Korn's inequality holds on $[H_0^1(\Omega)]^d$). Substituting $(\hat{\mathbf{v}}, \theta, \phi) = (\mathbf{f}_1, f_3, f_4)$ into the 5th row gives the decoupled elliptic equation for $\vartheta \in H_0^1(\Omega)$:
   $$-K^*_{ij}\vartheta_{,ij} = -\rho c_E \tau_q f_5 - \rho c_E f_4 - T_0\beta_{ij}f_{1,i,j} + (K_{ij} + \tau_v K^*_{ij})f_{3,ij} + \tau_T K_{ij}f_{4,ij} \in H^{-1}(\Omega), \tag{2.27}$$
   which has a unique solution $\vartheta \in H_0^1(\Omega)$ by Lax–Milgram since $K^*_{ij} \succ 0$. Thus $0 \in \varrho(\mathcal{A})$, and since $\mathcal{H}$ is reflexive and $\mathcal{A}$ is dissipative, Lumer–Phillips (via Pazy 1983, Thm. 1.4.3 & Thm. 4.6) guarantees that $\overline{D(\mathcal{A})} = \mathcal{H}$ and $\mathcal{A}$ generates a contraction $C_0$-semigroup on $\mathcal{H}$. $\square$

---

## 4. Derivation 3: Complete High-Frequency Asymptotics ($\xi \to \infty$) and Wavefront Classification

Consider 1D plane-wave perturbations $(\hat{u}, \vartheta)(x,t) = (\tilde{u}, \tilde{\vartheta})e^{\lambda t + \mathrm{i}\xi x}$ ($\xi > 0$) in a homogeneous isotropic medium with $c_1^2 = (\lambda_{\text{L}} + 2\mu_{\text{L}})/\rho$, $\alpha = k/(\rho c_E)$, $\alpha^* = k^*/(\rho c_E)$, and dimensionless thermoelastic coupling $\varepsilon = \frac{\beta^2 T_0}{\rho c_E(\lambda_{\text{L}} + 2\mu_{\text{L}})} > 0$. Factoring out the trivial $\lambda = 0$ translation mode, the exact 5th-order characteristic polynomial is:
$$P_5(\lambda; \xi) = \bigl(\lambda^2 + c_1^2\xi^2\bigr)\Bigl[\tau_q\lambda^3 + \bigl(1 + \alpha\tau_T\xi^2\bigr)\lambda^2 + \bigl(\alpha + \alpha^*\tau_v\bigr)\xi^2\lambda + \alpha^*\xi^2\Bigr] + \varepsilon c_1^2\xi^2\lambda^2\bigl(\tau_q\lambda + 1\bigr) = 0. \tag{2.28}$$

**Theorem 2.3 (Complete 5-Branch High-Frequency Asymptotics as $\xi \to \infty$).**

### Case I: $\tau_T > 0$ and $\tau_q > 0$ (Regularized Parabolic-Elastic Regime)
As $\xi \to \infty$, the 5 roots of $P_5(\lambda; \xi) = 0$ split into three distinct asymptotic families (machine-verified in `verify_c2_hardening.py`, Section 4):

1. **One Parabolic Diffusive Thermal Branch ($\lambda_1 \sim -O(\xi^2)$)**:
   $$\lambda_{\text{diff}}(\xi) = -\frac{\alpha \tau_T}{\tau_q}\xi^2 + \frac{\alpha(\tau_q - \tau_T) + \tau_q(\alpha^*\tau_v + \varepsilon c_1^2\tau_q)}{\alpha \tau_T \tau_q} + O(\xi^{-2}). \tag{2.29}$$
   Because $|\lambda_{\text{diff}}(\xi)|/\xi = \frac{\alpha\tau_T}{\tau_q}\xi \to \infty$ as $\xi \to \infty$, the thermal branch has **infinite wavefront propagation speed** (regularized parabolic diffusion with effective high-frequency diffusivity $D_{\text{eff}} = \frac{k\tau_T}{\rho c_E\tau_q}$).

2. **Two Propagating Quasi-Elastic Wave Branches ($\lambda_{2,3} \sim \pm\mathrm{i} c_1 \xi - O(1)$)**:
   $$\lambda_{\text{mech},\pm}(\xi) = \pm \mathrm{i} c_1 \xi - \gamma_{\text{mech},\infty} + O(\xi^{-1}), \qquad \gamma_{\text{mech},\infty} = \frac{\varepsilon c_1^2 \tau_q}{2\alpha \tau_T} = \frac{\varepsilon \rho c_E c_1^2}{2 k}\cdot\frac{\tau_q}{\tau_T} > 0. \tag{2.30}$$
   These modes propagate with finite wavefront speed $v_{\text{mech}} = c_1$ and experience finite high-frequency spatial attenuation:
   $$\kappa_\infty(\tau_q, \tau_T) = \frac{\gamma_{\text{mech},\infty}}{c_1} = \frac{\varepsilon \rho c_E c_1}{2 k}\cdot\frac{\tau_q}{\tau_T} = \frac{\tau_q}{\tau_T}\,\kappa_{\infty,\text{Fourier}}. \tag{2.31}$$

3. **Two Non-Propagating Thermal Relaxation Branches ($\lambda_{4,5} \sim O(1)$)**:
   $$\lim_{\xi\to\infty}\lambda_{4,5}(\xi) = \text{roots of } \alpha\tau_T \lambda^2 + (\alpha + \alpha^*\tau_v)\lambda + \alpha^* = 0, \tag{2.32}$$
   which are strictly negative real (or complex-conjugate with negative real part $\operatorname{Re}\lambda = -\frac{\alpha+\alpha^*\tau_v}{2\alpha\tau_T} < 0$) for all $\alpha, \alpha^*, \tau_T > 0, \tau_v \ge 0$.

---

### Case II: $\tau_T = 0$ and $\tau_q > 0$ (Strictly Hyperbolic MGT Thermoelastic Regime)
When $\tau_T = 0$, the $\alpha\tau_T\xi^2\lambda^2$ term vanishes and the principal part of $P_5(\lambda;\xi)$ is homogeneous of degree 5 in $(\lambda, \xi)$:
$$P_5^{\text{principal}}(\lambda, \xi) = \tau_q \lambda \Bigl[\bigl(\lambda^2 + c_1^2\xi^2\bigr)\bigl(\lambda^2 + c_T^2\xi^2\bigr) + \varepsilon c_1^2\xi^2\lambda^2\Bigr], \qquad c_T^2 := \frac{\alpha + \alpha^*\tau_v}{\tau_q} = \frac{k + k^*\tau_v}{\rho c_E \tau_q}. \tag{2.33}$$
As $\xi \to \infty$, the 5 roots of $P_5(\lambda;\xi)\big|_{\tau_T=0} = 0$ split into:

1. **Four Propagating Coupled Thermoelastic Wave Branches ($\lambda_{1,2,3,4} = \pm\mathrm{i} v_\pm \xi - \gamma_\pm + O(\xi^{-1})$)**:
   The two finite wavefront speeds $0 < v_- < \min(c_1, c_T) \le \max(c_1, c_T) < v_+ < \infty$ are the positive roots of the hyperbolic characteristic biquadratic:
   $$\bigl(v^2 - c_1^2\bigr)\bigl(v^2 - c_T^2\bigr) - \varepsilon c_1^2 v^2 = 0 \implies v_\pm^2 = \frac{1}{2}\Bigl[c_1^2(1+\varepsilon) + c_T^2 \pm \sqrt{\bigl(c_1^2(1+\varepsilon) + c_T^2\bigr)^2 - 4 c_1^2 c_T^2}\Bigr], \tag{2.34}$$
   with high-frequency temporal damping rate (machine-verified in `verify_c2_hardening.py`, Section 4):
   $$\gamma_\pm = \frac{v_\pm^4 - c_1^2(1+\varepsilon)v_\pm^2 - \alpha^*(v_\pm^2 - c_1^2)}{5\tau_q v_\pm^4 - 3\bigl[c_1^2(1+\varepsilon)\tau_q + \alpha + \alpha^*\tau_v\bigr]v_\pm^2 + (\alpha + \alpha^*\tau_v)c_1^2} = \frac{\bigl[\alpha + \alpha^*(\tau_v - \tau_q)\bigr]\bigl(v_\pm^2 - c_1^2\bigr)}{2\tau_q^2\bigl(v_+^2 - v_-^2\bigr)\cdot (\pm v_\pm^2)} > 0, \tag{2.35}$$
   where the second equality uses $c_1^2(1+\varepsilon)v_\pm^2 - v_\pm^4 = c_T^2(v_\pm^2 - c_1^2)$ from (2.34). Notice that $\gamma_\pm > 0$ if and only if $\alpha + \alpha^*(\tau_v - \tau_q) > 0$, i.e. $k + k^*(\tau_v - \tau_q) > 0$!

2. **One Non-Propagating GN-III Thermal-Displacement Relaxation Branch ($\lambda_5 \sim O(1)$)**:
   $$\lambda_5(\xi) = -\frac{\alpha^*}{\alpha + \alpha^*\tau_v} + O(\xi^{-2}) = -\frac{k^*}{k + k^*\tau_v} + O(\xi^{-2}) < 0. \tag{2.36}$$

---

## 5. Audit of the Six Degenerate Limiting Cases

| Limit | Parameter Specialization | Limiting PDE System | Behavior of Passivity Condition (2.9) | Behavior of Energy Norm (2.21) & Semigroup |
| :--- | :--- | :--- | :--- | :--- |
| **1. Classical Biot–Fourier** | $\tau_q, \tau_T, \tau_v \to 0$, $K^*_{ij} \to 0$ | $\rho\ddot{u}_i = (C_{ijkl}\varepsilon_{kl} - \beta_{ij}\theta)_{,j}$, $\rho c_E\dot{\theta} + T_0\beta_{ij}\dot{u}_{i,j} = K_{ij}\theta_{,ij}$ | Reduces to $K_{ij} \succeq 0$. | 5-field space $\mathcal{H}$ collapses to 3-field space $[H_0^1]^d\times [L^2]^d\times L^2(\Omega)$ ($\vartheta$ and $\phi$ drop out); parabolic-hyperbolic contraction semigroup. |
| **2. Lord–Shulman (Cattaneo)** | $\tau_T, \tau_v \to 0$, $K^*_{ij} \to 0$, $\tau_q > 0$ | $\rho\ddot{\hat{u}}_i = (C_{ijkl}\hat{\varepsilon}_{kl} - \beta_{ij}\hat{\theta})_{,j}$, $\rho c_E(\dot{\theta} + \tau_q\ddot{\theta}) + T_0\beta_{ij}\dot{\hat{u}}_{i,j} = K_{ij}\theta_{,ij}$ | Reduces to $K_{ij} \succeq 0$ (strictly passive for all $\tau_q > 0$). | **Degeneracy in (2.21)**: $K^*_{ij} \to 0$ causes $K^*_{ij}(\vartheta_{,i}+\tau_q\theta_{,i})(\vartheta_{,j}+\tau_q\theta_{,j}) \to 0$, so $\|\cdot\|_{\mathcal{H}}$ loses control of $\vartheta$ and must be quotiented to the 4-field space $(\hat{\mathbf{u}}, \hat{\mathbf{v}}, \theta, \phi)$! |
| **3. Tzou Dual-Phase-Lag (DPL)** | $K^*_{ij} \to 0$, $\tau_v \to 0$, $\tau_q, \tau_T > 0$ | $\rho c_E(\dot{\theta} + \tau_q\ddot{\theta}) + T_0\beta_{ij}\dot{\hat{u}}_{i,j} = K_{ij}(\theta + \tau_T\dot{\theta})_{,ij}$ | Reduces to $K_{ij} \succeq 0$ and $\tau_T\tau_q K_{ij} \succeq 0$ (unconditionally passive for all $\tau_q, \tau_T > 0$, agreeing with Quintanilla 2002 / Fabrizio & Lazzari 2014). | Same 5-to-4 field reduction as Lord–Shulman ($K^*_{ij} \to 0$ eliminates $\vartheta$ from the norm and operator domain; $0 \in \varrho(\mathcal{A})$ in Eq. 2.27 requires $K^*_{ij} \succ 0$ on the 5-field space). |
| **4. Green–Naghdi Type II (Undamped)** | $K_{ij} \to 0$, $\tau_q, \tau_T, \tau_v \to 0$, $K^*_{ij} \succ 0$ | $\rho\ddot{u}_i = (C_{ijkl}\varepsilon_{kl} - \beta_{ij}\theta)_{,j}$, $\rho c_E\ddot{\vartheta} + T_0\beta_{ij}\ddot{u}_{i,j} = K^*_{ij}\vartheta_{,ij}$ | $\varkappa_{ij} = 0$ and $\tau_T\tau_q K_{ij} = 0$: **conservative** ($\dot{\mathcal{E}} \equiv 0$, no thermal dissipation). | Reduces to a unitary group on the 4-field space $(u_i, \dot{u}_i, \vartheta, \theta) \in [H_0^1]^d\times [L^2]^d\times H_0^1\times L^2$. |
| **5. Green–Naghdi Type III** | $\tau_q, \tau_T, \tau_v \to 0$, $K_{ij} \succ 0, K^*_{ij} \succ 0$ | $\rho c_E\ddot{\vartheta} + T_0\beta_{ij}\ddot{u}_{i,j} = K^*_{ij}\vartheta_{,ij} + K_{ij}\dot{\vartheta}_{,ij}$ | Reduces to $K_{ij} \succeq 0$. | $\Lambda_{ij} = \tau_q K_{ij} \to 0$ in (2.21) as $\tau_q \to 0$: the 5-field norm collapses to the 4-field GN-III norm $\frac{1}{2}\int (\rho|\dot{u}|^2 + C\varepsilon^2 + \frac{\rho c_E}{T_0}\theta^2 + \frac{1}{T_0}K^*|\nabla\vartheta|^2)dV$ with $\dot{\mathcal{E}} = -\frac{1}{T_0}\int K|\nabla\theta|^2 dV$. |
| **6. Moore–Gibson–Thompson (MGT)** | $\tau_T \to 0, \tau_v \to 0$, $\tau_q > 0$, $K_{ij}, K^*_{ij} \succ 0$ | $\rho c_E(\dot{\theta} + \tau_q\ddot{\theta}) + T_0\beta_{ij}\dot{\hat{u}}_{i,j} = K^*_{ij}\vartheta_{,ij} + K_{ij}\theta_{,ij}$ | Reduces to $K_{ij} - \tau_q K^*_{ij} \succeq 0$ (Quintanilla 2019, Lemma 3.1). | Strictly hyperbolic 5-field contraction semigroup when $K_{ij} - \tau_q K^*_{ij} \succ 0$. **Degenerates at the conservative boundary $K_{ij} = \tau_q K^*_{ij}$** where $\Lambda_{ij} = \tau_q(K_{ij} - \tau_q K^*_{ij}) = 0$ and $\|\cdot\|_{\mathcal{H}}$ loses control of $\|\nabla\theta\|_{L^2}$! |
