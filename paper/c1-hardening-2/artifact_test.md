# Task 1 — The Artifact Test: Normalized vs. Unnormalized Kernels on Half-Space and Bounded Bar

**Verification script**: [`artifact_test.py`](./artifact_test.py)  
**Automated test suite**: [`test_c1_round2.py`](./test_c1_round2.py) (`test_symbolic_partition_of_unity_and_static_layer_artifact`, `test_bounded_bar_normalized_vs_unnormalized_kernels`, `test_neumann_kernel_ode_and_cbc_closure`)

---

## 1. Executive Verdict on the Static $1/\sqrt{\gamma}$ Surface Layer

In Round 1 (`paper/c1-hardening/physical_relevance.md`, Section 2), we derived that for a traction-free half-space $[0, \infty)$ under a uniform static temperature rise $\theta(x) \equiv \theta_0$, Variant V1 gives uniform strain $\varepsilon^{\text{V1}}(x) \equiv \frac{\beta\theta_0}{E}$, whereas Variant V2 gives a surface boundary layer $\varepsilon^{\text{V2}}(x) = \frac{\beta\theta_0}{E}\left[1 + \left(\frac{1}{\sqrt{\gamma}} - 1\right)e^{-x/(\sqrt{\gamma}\ell)}\right]$ with surface strain ratio $\varepsilon^{\text{V2}}(0)/\varepsilon^{\text{V1}}(0) = 1/\sqrt{\gamma}$ (equivalently $\varepsilon^{\text{V1}}(0)/\varepsilon^{\text{V2}}(0) = \sqrt{\gamma}$).

**That static $1/\sqrt{\gamma}$ surface thermal-expansion boundary layer is an artifact of using an unnormalized kernel truncated at the boundary.**

Specifically:
1. On a bounded domain $\Omega \subset \mathbb{R}^d$ (or half-space $[0, \infty)$), truncating the full-space Helmholtz kernel $K_\ell^{\text{unnorm}}(x, \xi) = \frac{1}{2\ell}e^{-|x-\xi|/\ell}$ without renormalization violates the partition-of-unity condition ($\int_\Omega K_\ell^{\text{unnorm}}(x, \xi)\,d\xi = w_\Omega(x) < 1$ near $\partial\Omega$, dropping to $1/2$ at $x = 0$). Consequently, the unnormalized two-phase operator fails to preserve constant fields:
   $$\mathcal{L}_{\gamma,\ell}^{\text{unnorm}}[1](x) = \gamma + (1-\gamma)w_\Omega(x) \neq 1 \quad \text{near }\partial\Omega.$$
   In Variant V1, $\sigma = \mathcal{L}_{\gamma,\ell}[E\varepsilon - \beta\theta] = 0$ has $E\varepsilon - \beta\theta_0 \equiv 0$ in the kernel of $\mathcal{L}_{\gamma,\ell}$ regardless of normalization because $\mathcal{L}_{\gamma,\ell}[0] = 0$. In Variant V2, $\sigma = \mathcal{L}_{\gamma,\ell}[E\varepsilon] - \beta\theta_0 = 0$ requires $\mathcal{L}_{\gamma,\ell}[E\varepsilon](x) = \beta\theta_0 \cdot 1$, so the boundary deficit in $\mathcal{L}_{\gamma,\ell}^{\text{unnorm}}[1](x)$ forces $\varepsilon^{\text{V2}}(x)$ to spike by $1/\sqrt{\gamma}$ at $x = 0$ purely to compensate for the missing half-kernel weight outside $\Omega$.
2. When the kernel is replaced by **any** symmetric partition-of-unity normalized kernel on $\Omega$ satisfying $\int_\Omega K_\ell^{\text{norm}}(x, \xi)\,d\xi \equiv 1$ — including both **(a1) the Borino–Failla–Parrinello (2003) / Polizzotto (2001) additive-defect normalized kernel $W_\ell^{\text{BFP}}(x, \xi)$** and **(a2) the reflecting / Neumann Green's-function kernel $K_\ell^{\text{Neu}}(x, \xi)$** — we have $\mathcal{L}_{\gamma,\ell}^{\text{norm}}[1](x) \equiv 1$ identically on $\Omega$.
3. Under both normalized kernels, the unique solution of $\mathcal{L}_{\gamma,\ell}^{\text{norm}}[E\varepsilon^{\text{V2}}](x) = \beta\theta_0$ on $[0, \infty)$ and on $[0, L]$ is the uniform free thermal expansion
   $$\varepsilon^{\text{V2}}(x) \equiv \frac{\beta\theta_0}{E} \equiv \varepsilon^{\text{V1}}(x), \qquad \frac{\varepsilon^{\text{V2}}(0)}{\varepsilon^{\text{V1}}(0)} = \frac{\varepsilon^{\text{V1}}(0)}{\varepsilon^{\text{V2}}(0)} \equiv 1.$$
   The static uniform-temperature surface layer **disappears completely** (to machine precision $< 2.5 \times 10^{-15}$ in our numerical Galerkin solver and identically in SymPy).

**Action taken**: In accordance with Task 1's instruction (*"If this effect is a kernel-truncation artifact rather than a physical prediction of V1 vs. V2, say so plainly and drop it from the claims"*), the static $1/\sqrt{\gamma}$ uniform-heating surface layer is **dropped from Candidate C1's claims**.

---

## 2. Mathematical Formulation of the Three Kernel Choices on $\Omega = [0, \infty)$ and $\Omega = [0, L]$

Let $\Omega$ be either the semi-infinite half-space $[0, \infty)$ or the bounded bar $[0, L]$. In all cases, the two-phase nonlocal operator has the form
$$\mathcal{L}_{\gamma,\ell}[f](x) = \gamma f(x) + (1-\gamma)\int_\Omega \mathcal{K}_\ell(x, \xi) f(\xi)\,d\xi, \qquad \gamma \in (0, 1).$$

### Kernel (b): Unnormalized Truncated Helmholtz Kernel $K_\ell^{\text{unnorm}}(x, \xi)$
$$\mathcal{K}_\ell(x, \xi) = K_\ell^{\text{unnorm}}(x, \xi) := \frac{1}{2\ell}e^{-|x-\xi|/\ell}.$$
- **Symmetry**: $K_\ell^{\text{unnorm}}(x, \xi) = K_\ell^{\text{unnorm}}(\xi, x)$ for all $x, \xi \in \Omega$.
- **Normalization weight $w_\Omega(x) := \int_\Omega K_\ell^{\text{unnorm}}(x, \xi)\,d\xi$**:
  $$w_{[0,\infty)}(x) = 1 - \frac{1}{2}e^{-x/\ell}, \qquad w_{[0,L]}(x) = 1 - \frac{1}{2}\left(e^{-x/\ell} + e^{-(L-x)/\ell}\right).$$
  At $x = 0$, $w_{[0,\infty)}(0) = \frac{1}{2} \neq 1$, so $\mathcal{L}_{\gamma,\ell}^{\text{unnorm}}[1](0) = \frac{1+\gamma}{2} < 1$.
- **Equivalent ODE and CBCs on $[0, L]$**: Because $(1 - \ell^2\partial_x^2)K_\ell^{\text{unnorm}}(x, \xi) = \delta(x-\xi)$, $g = \mathcal{L}_{\gamma,\ell}^{\text{unnorm}}[f]$ is equivalent to the constant-coefficient ODE
  $$(1 - \ell^2\partial_x^2)g(x) = (1 - \gamma\ell^2\partial_x^2)f(x), \qquad x \in (0, L),$$
  subject to the two **Robin Constitutive Boundary Conditions (CBCs)** (Fernández-Sáez et al. 2016; Romano et al. 2017):
  $$\left(\partial_x - \frac{1}{\ell}\right)g(0) = \gamma\left(\partial_x - \frac{1}{\ell}\right)f(0), \qquad \left(\partial_x + \frac{1}{\ell}\right)g(L) = \gamma\left(\partial_x + \frac{1}{\ell}\right)f(L).$$

---

### Kernel (a1): Borino–Failla–Parrinello (2003) / Polizzotto (2001) Additive-Defect Normalized Kernel $W_\ell^{\text{BFP}}(x, \xi)$
Following Polizzotto (2001, *Int. J. Solids Struct.* 38:7359–7380), Borino, Failla & Parrinello (2003, *Int. J. Solids Struct.* 40:3621–3645, Eq. 11), and Marotti de Sciarra (2009, *Comput. Methods Appl. Mech. Engrg.*, Eq. 5), a non-normalized symmetric kernel $K_\ell^{\text{unnorm}}(x, \xi)$ on a bounded domain $\Omega$ is converted into a **symmetric, constant-field-preserving** attenuation kernel by placing the boundary truncation deficit $1 - w_\Omega(x)$ into the local Dirac delta weight:
$$W_\ell^{\text{BFP}}(x, \xi) := \left(1 - w_\Omega(x)\right)\delta(x - \xi) + K_\ell^{\text{unnorm}}(x, \xi), \qquad w_\Omega(x) = \int_\Omega K_\ell^{\text{unnorm}}(x, \eta)\,d\eta.$$
Substituting $W_\ell^{\text{BFP}}$ into the two-phase operator yields:
$$\mathcal{L}_{\gamma,\ell}^{\text{BFP}}[f](x) = \gamma_{\text{eff}}(x) f(x) + (1-\gamma)\int_\Omega K_\ell^{\text{unnorm}}(x, \xi) f(\xi)\,d\xi,$$
where the spatially varying effective local phase fraction is
$$\gamma_{\text{eff}}(x) := \gamma + (1-\gamma)\left(1 - w_\Omega(x)\right) = \begin{cases} 1 - \frac{1-\gamma}{2}\left(2 - e^{-x/\ell}\right), & \Omega = [0, \infty), \\[4pt] 1 - (1-\gamma)w_{[0,L]}(x), & \Omega = [0, L]. \end{cases}$$
- **Symmetry (Self-Adjointness on $L^2(\Omega)$)**: Since $(1 - w_\Omega(x))\delta(x-\xi)$ is diagonal and $K_\ell^{\text{unnorm}}(x, \xi) = K_\ell^{\text{unnorm}}(\xi, x)$, $\mathcal{L}_{\gamma,\ell}^{\text{BFP}}$ is **strictly self-adjoint on $L^2(\Omega)$**:
  $$\langle \mathcal{L}_{\gamma,\ell}^{\text{BFP}} f, g\rangle_{L^2(\Omega)} = \langle f, \mathcal{L}_{\gamma,\ell}^{\text{BFP}} g\rangle_{L^2(\Omega)}, \qquad \langle \mathcal{L}_{\gamma,\ell}^{\text{BFP}} f, f\rangle_{L^2(\Omega)} \ge \gamma \|f\|_{L^2(\Omega)}^2.$$
  *(Note: Naive multiplicative row-scaling $\tilde{K}(x,\xi) = K_\ell^{\text{unnorm}}(x,\xi)/w_\Omega(x)$ breaks symmetry $\tilde{K}(x,\xi) \neq \tilde{K}(\xi,x)$ and therefore violates Polizzotto's thermodynamic self-adjointness axiom; this is precisely why Polizzotto 2001 and Borino et al. 2003 introduced $W_\ell^{\text{BFP}}$.)*
- **Exact Partition of Unity**:
  $$\mathcal{L}_{\gamma,\ell}^{\text{BFP}}[1](x) = \gamma + (1-\gamma)\left(1 - w_\Omega(x)\right) + (1-\gamma)\int_\Omega K_\ell^{\text{unnorm}}(x, \xi)\,d\xi \equiv 1 \quad \forall x \in \Omega.$$
- **Equivalent ODE and Modified Robin CBCs on $[0, L]$**: Writing $w(x) = \int_0^L K_\ell^{\text{unnorm}}(x, \xi)f(\xi)\,d\xi = \frac{g(x) - \gamma_{\text{eff}}(x)f(x)}{1-\gamma}$, the auxiliary nonlocal integral $w(x)$ still satisfies $(1 - \ell^2\partial_x^2)w = f$ and the Robin CBCs $(\partial_x \mp \ell^{-1})w = 0$ at $x = 0, L$. Thus $g = \mathcal{L}_{\gamma,\ell}^{\text{BFP}}[f]$ satisfies the variable-coefficient 2nd-order ODE
  $$(1 - \ell^2\partial_x^2)\left[g(x) - \gamma_{\text{eff}}(x)f(x)\right] = (1-\gamma)f(x), \qquad x \in (0, L),$$
  subject to the **modified Robin CBCs**:
  $$\left(\partial_x - \frac{1}{\ell}\right)\left[g(x) - \gamma_{\text{eff}}(x)f(x)\right]\Big|_{x=0} = 0, \qquad \left(\partial_x + \frac{1}{\ell}\right)\left[g(x) - \gamma_{\text{eff}}(x)f(x)\right]\Big|_{x=L} = 0.$$
  When $f(x) \equiv f_0$ is constant and $g(x) \equiv f_0$, $g(x) - \gamma_{\text{eff}}(x)f_0 = (1-\gamma)w_\Omega(x)f_0$, which satisfies both the interior ODE and the modified Robin CBCs identically!

---

### Kernel (a2): Reflecting / Neumann Green's-Function Normalized Kernel $K_\ell^{\text{Neu}}(x, \xi)$
A second classical way to normalize the Helmholtz kernel on a bounded domain while keeping constant-coefficient interior PDEs (used by Ren & Truskinovsky 2000; Challamel et al. 2014; and discussed in the modified-kernel boundary framework of Nobili & Pramanik 2025, Eqs. 14–16) is to define $K_\ell^{\text{Neu}}(x, \xi)$ as the Green's function of $(1 - \ell^2\partial_x^2)$ on $\Omega$ with **homogeneous Neumann boundary conditions** $\partial_x K_\ell^{\text{Neu}}\big|_{\partial\Omega} = 0$ (physically corresponding to specularly reflecting image sources at the boundaries):
- **On the half-space $\Omega = [0, \infty)$**:
  $$K_\ell^{\text{Neu}}(x, \xi) = \frac{1}{2\ell}\left(e^{-|x-\xi|/\ell} + e^{-(x+\xi)/\ell}\right).$$
- **On the bounded bar $\Omega = [0, L]$**:
  $$K_\ell^{\text{Neu}}(x, \xi) = \frac{\cosh\!\left(\frac{\min(x,\xi)}{\ell}\right)\cosh\!\left(\frac{L - \max(x,\xi)}{\ell}\right)}{\ell\sinh(L/\ell)}.$$
- **Symmetry and Positive-Definiteness**: $K_\ell^{\text{Neu}}(x, \xi) = K_\ell^{\text{Neu}}(\xi, x)$ is the Green's function of the self-adjoint positive-definite Neumann operator $(1 - \ell^2\partial_x^2)$ on $L^2(\Omega)$, so $\mathcal{L}_{\gamma,\ell}^{\text{Neu}}$ is strictly self-adjoint and coercive on $L^2(\Omega)$.
- **Exact Partition of Unity**: By integration by parts, $\int_\Omega K_\ell^{\text{Neu}}(x, \xi)\,d\xi = 1 - \ell^2\left[\partial_\xi K_\ell^{\text{Neu}}(x, \xi)\right]_{\partial\Omega} \equiv 1$, hence
  $$\mathcal{L}_{\gamma,\ell}^{\text{Neu}}[1](x) \equiv 1 \quad \forall x \in \Omega.$$
- **Equivalent ODE and Homogeneous Neumann CBCs on $[0, L]$**: Because $(1 - \ell^2\partial_x^2)K_\ell^{\text{Neu}}(x, \xi) = \delta(x-\xi)$ in $(0, L)$ and $\partial_x K_\ell^{\text{Neu}}(0, \xi) = \partial_x K_\ell^{\text{Neu}}(L, \xi) = 0$, $g = \mathcal{L}_{\gamma,\ell}^{\text{Neu}}[f]$ is equivalent to the **exact constant-coefficient 2nd-order interior ODE**:
  $$(1 - \ell^2\partial_x^2)g(x) = (1 - \gamma\ell^2\partial_x^2)f(x), \qquad x \in (0, L),$$
  subject to the **homogeneous Neumann Constitutive Boundary Conditions**:
  $$g'(0) = \gamma f'(0), \qquad g'(L) = \gamma f'(L).$$

---

## 3. Analytic & Numerical Comparison on $[0, \infty)$ and $[0, L]$

### 3.1 Analytical Proof for Static Uniform Heating $\theta(x) \equiv \theta_0$, $\sigma(x) \equiv 0$
On either $\Omega = [0, \infty)$ or $\Omega = [0, L]$ with traction-free ends ($\sigma \equiv 0$) and uniform temperature change $\theta(x) \equiv \theta_0$:
- **Variant V1**: $\sigma(x) = \mathcal{L}_{\gamma,\ell}[E\varepsilon^{\text{V1}} - \beta\theta_0](x) = 0$. Since $\mathcal{L}_{\gamma,\ell}$ is strictly positive-definite on $L^2(\Omega)$ ($\langle \mathcal{L}_{\gamma,\ell} f, f\rangle \ge \gamma\|f\|_{L^2}^2 > 0$ for $\gamma > 0$), $\ker(\mathcal{L}_{\gamma,\ell}) = \{0\}$, so for **all three kernels** (`unnorm`, `bfp`, `neu`):
  $$\varepsilon^{\text{V1}}(x) \equiv \frac{\beta\theta_0}{E}.$$
- **Variant V2**: $\sigma(x) = \mathcal{L}_{\gamma,\ell}[E\varepsilon^{\text{V2}}](x) - \beta\theta_0 = 0$, i.e. $\mathcal{L}_{\gamma,\ell}[E\varepsilon^{\text{V2}}](x) = \beta\theta_0 \cdot 1$.
  - Under **Kernel (a1) $W_\ell^{\text{BFP}}$** and **Kernel (a2) $K_\ell^{\text{Neu}}$**, $\mathcal{L}_{\gamma,\ell}[1](x) \equiv 1$. By positive-definiteness (uniqueness of solution in $L^2(\Omega)$), the unique solution is the constant field:
    $$\varepsilon^{\text{V2, BFP}}(x) = \varepsilon^{\text{V2, Neu}}(x) \equiv \frac{\beta\theta_0}{E} \equiv \varepsilon^{\text{V1}}(x) \implies \frac{\varepsilon^{\text{V2}}(0)}{\varepsilon^{\text{V1}}(0)} \equiv 1.$$
  - Under **Kernel (b) $K_\ell^{\text{unnorm}}$**, $\mathcal{L}_{\gamma,\ell}^{\text{unnorm}}[1](x) \neq 1$. Solving $(1 - \gamma\ell^2\partial_x^2)\varepsilon^{\text{V2}} = \frac{\beta\theta_0}{E}$ with the unnormalized Robin CBCs gives:
    $$\varepsilon^{\text{V2, unnorm}}_{[0,\infty)}(x) = \frac{\beta\theta_0}{E}\left[1 + \left(\frac{1}{\sqrt{\gamma}} - 1\right)e^{-x/(\sqrt{\gamma}\ell)}\right], \qquad \frac{\varepsilon^{\text{V2, unnorm}}_{[0,\infty)}(0)}{\varepsilon^{\text{V1}}(0)} = \frac{1}{\sqrt{\gamma}},$$
    and on $[0, L]$:
    $$\frac{\varepsilon^{\text{V2, unnorm}}_{[0,L]}(0)}{\varepsilon^{\text{V1}}(0)} = 1 + \frac{1-\gamma}{\gamma + \sqrt{\gamma}\coth\!\left(\frac{L}{2\sqrt{\gamma}\ell}\right)}.$$

### 3.2 Numerical Verification Table on Bounded Bar $[0, L]$ ($L = 10\ell$, $\gamma = 0.25$, $N = 200$ Piecewise-Constant Split-Triangle Galerkin Cells)
From [`artifact_test.py`](./artifact_test.py) ($E = 1, \beta = 1, \theta_0 = 1$, where $1/\sqrt{\gamma} = 2.0$):

| Quantity | (b) Unnormalized Kernel $K_\ell^{\text{unnorm}}$ | (a1) BFP Normalized Kernel $W_\ell^{\text{BFP}}$ | (a2) Neumann Normalized Kernel $K_\ell^{\text{Neu}}$ |
| :--- | :---: | :---: | :---: |
| Self-adjointness defect $\max_{i,j}|B_{ij} - B_{ji}|$ | $1.63 \times 10^{-19}$ | $1.63 \times 10^{-19}$ | $3.25 \times 10^{-19}$ |
| Partition-of-unity error $\max_x |\mathcal{L}_{\gamma,\ell}[1](x) - 1|$ | $0.368836$ | $6.66 \times 10^{-16}$ | $4.44 \times 10^{-16}$ |
| Uniform heating $\varepsilon^{\text{V1}}(0) / (\beta\theta_0/E)$ | $1.000000000000000$ | $1.000000000000000$ | $1.000000000000000$ |
| Uniform heating $\varepsilon^{\text{V2}}(0) / (\beta\theta_0/E)$ | $2.000268$ (exact $1.999999997$) | $1.000000000000000$ | $1.000000000000000$ |
| Surface strain ratio $\varepsilon^{\text{V2}}(0)/\varepsilon^{\text{V1}}(0)$ (uniform $\theta_0$) | **$2.000268 \approx 1/\sqrt{\gamma}$** | **$1.000000000000000$** | **$1.000000000000000$** |
| Max discrepancy $\max_{x\in[0,L]}|\varepsilon^{\text{V1}}(x) - \varepsilon^{\text{V2}}(x)|$ (uniform $\theta_0$) | $0.967480$ | **$1.78 \times 10^{-15}$** | **$2.44 \times 10^{-15}$** |
| Max discrepancy $\max_{x\in[0,L]}|\varepsilon^{\text{V1}}(x) - \varepsilon^{\text{V2}}(x)|$ (linear gradient $\theta(x) = 1 + 0.2(x/L - 0.5)$) | $1.083580$ | $8.33 \times 10^{-3}$ | $2.90 \times 10^{-2}$ |

### 3.3 What Happens Under a Non-Uniform Temperature Gradient ($\theta_{,x} \neq 0$) With Normalized Kernels?
For a non-uniform temperature field $\theta(x)$ with $\theta'(0) \neq 0$ (e.g., steady heat conduction $\theta(x) = \theta_0 + G(x - L/2)$ across the bar), $\varepsilon^{\text{V1}}(x) = \frac{\beta}{E}\theta(x)$ is linear in $x$, whereas $\mathcal{L}_{\gamma,\ell}^{\text{norm}}[\theta](x) \neq \theta(x)$ near the boundaries because $\theta'(0) = G \neq 0$ violates the homogeneous Neumann CBC $\theta'(0) = 0$ (for $K_\ell^{\text{Neu}}$) or the modified Robin condition (for $W_\ell^{\text{BFP}}$). Specifically, under $K_\ell^{\text{Neu}}$:
$$(1 - \gamma\ell^2\partial_x^2)\varepsilon^{\text{V2, Neu}} = \frac{\beta}{E}(1 - \ell^2\partial_x^2)\theta = \frac{\beta}{E}\theta(x), \qquad (\varepsilon^{\text{V2, Neu}})'(0) = \frac{\beta G}{\gamma E} \neq \frac{\beta G}{E}.$$
This produces a gradient-driven boundary layer of amplitude
$$\Delta\varepsilon_{\text{grad}}(0) = \varepsilon^{\text{V2, Neu}}(0) - \varepsilon^{\text{V1}}(0) \sim \left(\frac{1-\gamma}{\sqrt{\gamma}}\right)\frac{\beta \ell G}{E} = \left(\frac{1-\gamma}{\sqrt{\gamma}}\right)\frac{\ell}{L}\frac{\beta \Delta\theta}{E},$$
which is suppressed by the geometric ratio $\ell / L \ll 1$ (unlike the unphysical $O(1)$ truncation artifact under uniform heating).

---

## 4. Complete Classification: What in Candidate C1 Survives vs. Disappears Under Kernel Normalization

| C1 Result / Claim from Round 1 | Status Under Unnormalized $K_\ell^{\text{unnorm}}$ | Status Under BFP Normalized $W_\ell^{\text{BFP}}$ | Status Under Neumann Normalized $K_\ell^{\text{Neu}}$ | Verdict |
| :--- | :---: | :---: | :---: | :---: |
| **Theorem 1a**: Variant V1 and Variant V2 are globally thermodynamically compatible with the Second Law ($\int_\Omega D_{\text{int}}\,dx = \int_\Omega \frac{\kappa}{T_0}|\nabla\theta|^2\,dx \ge 0$) | Holds ($\mathcal{L}_{\gamma,\ell}^{\text{unnorm}}$ self-adjoint on $L^2(\Omega)$) | **SURVIVES** ($\mathcal{L}_{\gamma,\ell}^{\text{BFP}}$ self-adjoint on $L^2(\Omega)$) | **SURVIVES** ($\mathcal{L}_{\gamma,\ell}^{\text{Neu}}$ self-adjoint on $L^2(\Omega)$) | **SURVIVES** for all symmetric kernels |
| **Theorem 1b**: Camp 1 ($(1-\ell^2\partial_x^2)\sigma = E\varepsilon - \beta\theta$ paired with local $\rho\eta = \beta\varepsilon + \frac{\rho c_E}{T_0}\theta$) violates Maxwell symmetry and global Clausius–Duhem inequality | Holds | **SURVIVES** (differential statement independent of boundary normalization) | **SURVIVES** (differential statement independent of boundary normalization) | **SURVIVES** |
| **Theorem 2a**: Integral-to-differential reduction on bounded $\Omega$ requires 2 Constitutive Boundary Conditions (CBCs) to close the elevated ODE order | Holds with Robin CBCs $(\partial_x \mp \ell^{-1})w = 0$ | **SURVIVES** with modified Robin CBCs $(\partial_x \mp \ell^{-1})[g - \gamma_{\text{eff}}f] = 0$ | **SURVIVES** with homogeneous Neumann CBCs $g' = \gamma f'$ at $\partial\Omega$ | **SURVIVES** (specific CBC form depends on kernel choice) |
| **Theorem 2b**: V1 and V2 have non-equivalent CBCs whenever $\theta$ or $\theta_{,x}$ is non-trivial at $\partial\Omega$ | Holds even for constant $\theta_0 \neq 0$ | **Modified**: Equivalent for constant $\theta_0$; non-equivalent only when $\theta_{,x} \neq 0$ | **Modified**: Equivalent for constant $\theta_0$; non-equivalent only when $\theta'(0) \neq 0$ | **SURVIVES only for $\theta_{,x} \neq 0$** |
| **Static $1/\sqrt{\gamma}$ Surface Thermal-Expansion Layer** under uniform $\theta_0$ ($\varepsilon^{\text{V2}}(0)/\varepsilon^{\text{V1}}(0) = 1/\sqrt{\gamma}$) | Present ($1/\sqrt{\gamma}$) | **DISAPPEARS** ($\varepsilon^{\text{V2}}(x) \equiv \varepsilon^{\text{V1}}(x)$, ratio $= 1$) | **DISAPPEARS** ($\varepsilon^{\text{V2}}(x) \equiv \varepsilon^{\text{V1}}(x)$, ratio $= 1$) | **ARTIFACT — DROPPED FROM CLAIMS** |
| **Theorem 3**: Bulk dispersion polynomial degree in $q = k^2$ is **quartic** ($N=4$ mode pairs) for V1 vs. **cubic** ($N=3$ mode pairs) for V2 and Camp 1, with singular perturbation at $\gamma \to 0$ | Holds | **SURVIVES** ($w_\Omega(x) = 1$ in bulk $\mathbb{R}$, so bulk symbol $\hat{\mathcal{L}}(k)$ is identical) | **SURVIVES** (bulk symbol $\hat{\mathcal{L}}(k)$ is identical) | **SURVIVES** |
| **Theorem 4**: Bulk wave dispersion and high-$k$ quasi-elastic attenuation formulas on $\mathbb{R}$ | Holds | **SURVIVES** | **SURVIVES** | **SURVIVES** (subject to Task 4 calibration bounds) |
