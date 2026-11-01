# Boundary identification of the initial memory state: prior-art and novelty audit

**Date:** 1 November 2026

**Final decision: INSUFFICIENT EVIDENCE**

## 1. Executive findings

The desired implication for the **full, labeled** force-and-two-flux observation on the actual weak-admissible set is **UNRESOLVED**. The exact linearized observation operator about the active trajectory is derived below; its kernel has not been characterized. The nonlinear terms have not been shown either to eliminate its possible nullspace or to preserve non-identifiability. No source inspected proves the exact fixed-experiment theorem, but inaccessible literature and the non-exhaustive search prevent a novelty claim.

There are two rigorous **conditional partial findings**, not a solution to the full inverse problem:

1. If the fixed loading satisfies the already-established strict small-data threshold, reflection gives distinct actual weak-admissible states with exactly the same **force trace alone**. The two labeled heat-flux traces are exchanged, not automatically unchanged. This proves neither injectivity nor non-injectivity of the requested three-component map.
2. Under that same strict condition, the local observation map is differentiable at zero initial memory along the **nonzero-loading trajectory**. Its derivative is a compact operator from \(L^2(0,L)\) to the frozen observation space. Consequently no uniform local \(L^2\)-to-\(L^2_t\) Lipschitz inverse estimate can hold in an \(H^2\)-neighborhood within the actual admissible set. There is also no inverse modulus in the strong \(H^2\) metric on that neighborhood. These statements do not preclude injectivity or a weaker \(L^2\) stability modulus.

The condition on the *given* loading has not been verified from numerical frozen parameters. No loading, parameter, boundary condition, initial topology, or sensor is changed; the condition is only a sufficient hypothesis under which previously proved actual admissibility is available. A result of this type is a natural consequence of reflection and compactness, and is not claimed novel. Its scientific value is to rule out particular recovery guarantees and to expose what must be proved for the real experiment.

This is an Arena research investigation, not an independent certification by the designated supervisor. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. Direction 1 remains rejected as a foundational continuum theory. No simulation, manuscript, new constitutive theory, or extra measurement is introduced.

## 2. Focused primary-literature investigation — performed before the inverse analysis

The search covered initial-state observability in hereditary systems; source and kernel recovery in viscoelastic and heat-memory equations; internal-state/response equivalence; sparse boundary flux; PDE–ODE and parabolic-memory observability; and nonlocal coupled systems. The following table separates actual inspected results from abstract-only information. “Not the same problem” does **not** prove novelty.

| Primary source, identifier and inspection | Relevant result and hypotheses | Exact relationship to Formulation A |
|---|---|---|
| **W. Green and S. Liu**, *Source reconstruction and stability via boundary control of abstract viscoelastic systems*, *Applicable Analysis* **101**, 4991–5005, DOI [10.1080/00036811.2021.1877682](https://doi.org/10.1080/00036811.2021.1877682); open preprint [arXiv:2004.10842v1](https://arxiv.org/html/2004.10842), §§1–3 and Theorems 1.1–1.3 inspected. | Theorem 1.1 transfers an assumed two-sided observability/regularity estimate for a memory-free second-order abstract system to its memory system for \(M\in H^2(0,T)\), \(T>T_0\). Theorems 1.2–1.3 recover a spatial source \(f\in\mathcal H\) from a single boundary observation, with \(H^1\)-time data, a known factor \(\sigma\in C^1\), \(\sigma(0)\ne0\), zero initial displacement/velocity, and the paper's self-adjoint, compact-resolvent and observation assumptions. A stability estimate and reconstruction formula follow. | This is close and strong prior art: unknown initial memory here also appears as a separable exponentially decaying source after elimination. But A is quasistatic and nonlinearly coupled to heat, includes the rank-one mass, delayed \(L^2\) force/flux observations and the unknown memory field itself; the wave observability premise (B) is not established. The theorem cannot simply be invoked. In particular, its stronger \(H^1_t\) observation norm is not our frozen \(L^2_t\) norm. |
| **S. A. Avdonin, S. A. Ivanov, J. M. Wang**, *Inverse Problems for the Heat Equation with Memory*, [arXiv:1612.02129v2](https://arxiv.org/html/1612.02129), journal record [DOI 10.3934/ipi.2019002](https://doi.org/10.3934/ipi.2019002). Open preprint §§1–3 and Theorem 4 inspected. | For a one-dimensional Gurtin–Pipkin equation with **zero initial temperature**, Dirichlet boundary input and boundary response operator, with kernel Laplace transform \(K(z)=a^2/z+O(z^{-2})\), \(a>0\), Theorem 4 gives the stated finite-horizon kernel uniqueness when \(T_*=Ta\le L\). | The unknown is a **time kernel**, and the data are a boundary response operator over admissible inputs, not one fixed displacement experiment with an unknown spatial initial internal state. Their result does not settle (A), but kernel identification by boundary thermal measurements is established. |
| **L. Ma, G. Wang, Y. Zhang**, *Sampling Observability for Heat Equations with Memory*, [arXiv:2411.14382v1](https://arxiv.org/html/2411.14382), 2024 preprint; Definitions 1.1, 1.3, 1.5 and Theorems 1.7, 1.9 inspected. | For the heat equation with a lower-order convolution term, \(M\in C^2\), and a known zero prehistory, Theorem 1.7 assumes backward uniqueness at selected instants and shows that a weighted geometric observation condition implies a two-sided estimate for the initial heat state in \(\mathcal H^{-4}\); the estimate implies a weaker geometric condition. Observations are spatial \(L^2\) restrictions at finitely many selected times. | The initial unknown is temperature, not a separate distributed ODE memory state; observation is in open spatial regions, not boundary flux time traces. Nonetheless it is direct prior art that memory, observability and weaker reconstruction norms are already studied. No theorem here supplies the target conclusion. |
| **W. Green, S. Liu, M. Mitkovski**, *Boundary Observability for the Viscoelastic Wave Equation*, *SIAM J. Control Optim.* **57** (2019), 1629–1645, DOI [10.1137/18M1180736](https://doi.org/10.1137/18M1180736). Primary [author PDF](https://www.math.wustl.edu/~awgreen/files/papers/visco-control-siamjco-2020.pdf) was indexed in search, but direct fetch failed in this session; the closely related open source above was checked directly. | The indexed paper describes boundary observability of a wave with a specified convolution kernel and initial displacement and velocity, under its geometric/time hypotheses. The full theorem's exact hypotheses were not independently inspected this session and are not relied on. | Strong duplication risk for hereditary observability, but the known-history wave state and boundary normal trace are not A's thermally coupled unknown initial memory profile. |
| **M. Fabrizio and J. M. Golden**, *Maximum and minimum free energies and the concept of a minimal state*, *Rendiconti di Matematica* **20** (2000), 131–165, [full-text record](https://www.researchgate.net/publication/235734418_Maximum_and_minimum_free_energies_and_the_concept_of_a_minimal_state). Definition 3.2 and displayed initial-history functional inspected in the indexed primary text; access is via an author-copy record, not a publisher download. | Definition 3.2 identifies states with equal constitutive responses under **all** admissible processes (and the other stated response); the displayed \(I_0(t,E_0)\) is a functional of the initial past history. The paper develops free-energy consequences for linear viscoelasticity under its own constitutive assumptions. | This is a pre-existing history-equivalence concept. Our equality under **one fixed experiment** and three sensors is a different, possibly coarser equivalence; it is not automatically a thermodynamic minimal state. One cannot infer recovery of an entire past from recovery of \(z_0\). |
| **L. Deseri, M. Fabrizio, J. M. Golden**, *The Concept of a Minimal State in Viscoelasticity: New Free Energies and Applications to PDEs*, *Arch. Ration. Mech. Anal.* **181** (2006), 43–96, DOI [10.1007/s00205-005-0406-1](https://doi.org/10.1007/s00205-005-0406-1). Publisher **abstract/preview only**, full theorem statements inaccessible. | The preview describes stress-response minimal states and a linear viscoelastic initial-boundary-value/semigroup framework; exact assumptions and theorem-level claims were not inspected and are not asserted here. | This is a major unresolved overlap source. Neither the preview nor its title establishes or excludes the exact three-sensor inverse result. Full-text comparison is required before a novelty claim. |
| **G. Amendola, M. Fabrizio, J. M. Golden**, *Thermodynamics of Materials with Memory: Theory and Applications*, Springer, 2012, DOI [10.1007/978-1-4614-1692-0](https://doi.org/10.1007/978-1-4614-1692-0). Publisher overview only; chapters unavailable. | The overview describes memory-state, well-posedness, controllability and inverse-problem chapters, but no exact theorem is verified from the preview. | Important potential overlap remains unchecked. Do not infer its theorem statements from its chapter titles. |
| **A. Lorenzi and V. G. Romanov**, *Recovering two Lamé kernels in a viscoelastic system*, *Inverse Problems and Imaging* **5** (2011), 431–464, DOI [10.3934/ipi.2011.5.431](https://doi.org/10.3934/ipi.2011.5.431). Publisher abstract/model only; full theorem not inspected. | The published abstract describes recovery of spatial factors of two factorized kernels from spatially resolved traction on a boundary subset, with fixed initial data. Precise theorem assumptions have not been independently verified. | Different unknown, dynamic three-dimensional equations, and different measurements; a prior-art lead, not a theorem-level basis for a claim here. |
| **F. Alabau-Boussouira**, *On the influence of the coupling on the dynamics of single-observed cascade systems of PDE's*, *Math. Control Relat. Fields* **5** (2015), 1–30, DOI [10.3934/mcrf.2015.5.1](https://doi.org/10.3934/mcrf.2015.5.1). Publisher abstract only; full theorem not inspected. | The preview reports examples where coupling causes an infinite-dimensional unobservable set and discusses weaker-norm estimates, including parabolic extensions. The detailed hypotheses were not inspected. | Useful warning: coupling to an observed component does not automatically imply observability. Not an applicable theorem for the rank-one active problem. |
| **G. Lin, N. Ou, Z. Zhang, Z. Zhang**, *Restoring the Discontinuous Heat Equation Source Using Sparse Boundary Data and Dynamic Sensors*, [arXiv:2310.01541v2](https://arxiv.org/html/2310.01541), journal DOI [10.1088/1361-6420/ad2904](https://doi.org/10.1088/1361-6420/ad2904). Open preprint §§1–2 inspected. | The model has an unknown characteristic-function source on a two-dimensional disk and boundary flux measurements. The introduction discusses prior sparse-sensor source uniqueness under their conditions; the paper also studies a different sensor-selection problem. We do not import an uninspected theorem. | Boundary-flux inverse-source work is established. Moving sensors and source shapes are not the frozen experiment and are not proposed here. |

The closest inspected rigorous source-recovery theorem, Green–Liu, is an especially important comparison because an initial internal state produces an exponential source term. We have **not** shown its assumptions hold for A. Other relevant source/kernel papers cited in these works and the inaccessible 2006/book chapters need theorem-level inspection. The search is targeted but non-exhaustive; no exact identity with an existing theorem and no publication gap are established.

## 3. Exact model, admissibility, and the inverse question

Let \(I=(0,L)\), \(\bar f=L^{-1}\int_0^L f\), \(Qf=f-\bar f\), \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\mu=\lambda\alpha\), \(d=b^2/D\). The unchanged system is

\[
\sigma_x=0,\quad \sigma=D\varepsilon-b(\theta-\theta_*)-kz,\quad
z_t=\lambda(\varepsilon-z),\quad
c\theta_t=\kappa\theta_{xx}-b\theta\varepsilon_t+k\lambda(\varepsilon-z)^2,
\quad\varepsilon=u_x.
\]

The boundary input is \(u(0,t)=0\), \(u(L,t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\), \(T=10/\lambda\); baths \(\theta(0,t)=\theta(L,t)=\theta_*\); \(\theta(0,x)=\theta_*\); \(\delta=T/100\). Define \(y=\theta-\theta_*\), \(m=g/L\), \(v=\bar z\), \(p=Qz\). The exact equations are

\[
\varepsilon=m+rp+\beta Qy,\quad w=\varepsilon-z=m-v-\alpha p+\beta Qy,
\]
\[
v_t=\lambda(m-v),\quad p_t=-\mu p+\lambda\beta Qy,\quad
(cI+d\theta Q)y_t-\kappa y_{xx}=-b\theta[m'+rp_t]+k\lambda w^2,
\]
\[
\sigma=Dm-b\bar y-kv.\tag{3.1}
\]

The domain is **exactly** \(\mathcal A_T^{\rm w}\) from the topology audit: initial \(z_0\in B_M\subset H^2(I)\), with exactly one solution in its specified weak-initial class, positive temperature, bounded variables, and required observations. It is not replaced by all \(H^2\) or by the small-data ball. The existence report and independent audit show a **subset** is admissible when the fixed amplitude satisfies their data threshold; they do not establish that this is the whole admissible set or that the unknown fixed parameters satisfy it.

For each \(z_0\in\mathcal A_T^{\rm w}\), define

\[
\mathcal O(z_0)=\bigl(A_0\sigma,\ A_0\kappa y_x(0,\cdot),\ -A_0\kappa y_x(L,\cdot)\bigr)|_{(\delta,T)}\in Y=L^2(\delta,T)^3.\tag{3.2}
\]

The exact question is \(\mathcal O(z_{0,1})=\mathcal O(z_{0,2})\Rightarrow z_{0,1}=z_{0,2}\) for **all** pairs in this actual set. The tautological relation \(z_1\sim z_2\iff\mathcal O(z_1)=\mathcal O(z_2)\) is always an equivalence relation and defines an injective map from the quotient into \(Y\), but this does not identify the classes, prove they are singletons, or make them constitutive minimal states. If the actual set were empty or a singleton, injectivity would be vacuous/trivial and not meaningful recovery.

Global injectivity, local injectivity, derivative kernel, stability and finite-precision identifiability are distinct. In particular, a zero derivative in some direction need not preclude nonlinear injectivity (e.g. \(x\mapsto x^3\)); an injective derivative in infinite dimensions does not establish a nonlinear inverse or global uniqueness without further estimates.

## 4. Actual active base and derivative

There is a common terminology trap. At \(z_0=0\), the **initial material state** is the reference state, but with the required \(g_*\ne0\), \(m(t)\not\equiv0\). Therefore \(y=0,p=0,v=0\) is not a full solution trajectory. Linearizing the zero-loading equilibrium instead would change the experiment. We linearize only the real active trajectory.

Let \(s_*\) be the positive explicit threshold (6.3) of `direction-2-formulation-A-existence-investigation.md`, in its stated fixed numerical units, and let \(q=|g_*|/L\). **For this section assume the existing sufficient condition \(0<q<s_*\).** Since \(M>0\), a sufficiently small open \(H^2\)-ball around zero lies in \(\mathcal A_T^{\rm w}\). This follows from the earlier fixed-horizon existence, positivity and whole-weak-class uniqueness theorem, not from redefining the admissible set. If the bound fails or is unknown, the existence of this base solution and its differentiability have not been established by this argument.

Denote the active base solution for \(z_0=0\) by \(y_b,p_b,v_b,w_b,\theta_b=\theta_*+y_b\), with \(E_b=m'+r(p_b)_t\). Let \(h\in H^2\), and set \(Y=Dy_b[h]\), \(P=Dp_b[h]\), \(V=Dv_b[h]\), \(W=Dw_b[h]\). Differentiation of (3.1) gives

\[
V(t)=e^{-\lambda t}\bar h,\quad P_t=-\mu P+\lambda\beta QY,\quad P(0)=Qh,\quad
W=-V-\alpha P+\beta QY,\tag{4.1}
\]
\[
(cI+d\theta_bQ)Y_t-\kappa Y_{xx}
=-dYQ(y_b)_t-bYE_b-b\theta_b rP_t+2k\lambda w_bW,\quad
Y(0)=0,\quad Y|_{x=0,L}=0.\tag{4.2}
\]

In particular, \(-dYQ(y_b)_t\) is required; it is not legitimate to replace \(\theta_b\) by \(\theta_*\) or \(w_b\) by zero throughout the active trajectory. The derivative of (3.2) is

\[
D\mathcal O(0)h=\left(A_0[-b\bar Y-k e^{-\lambda t}\bar h],\ A_0\kappa Y_x(0,t),\ -A_0\kappa Y_x(L,t)\right)_{(\delta,T)}.\tag{4.3}
\]

**Why this derivative exists under the strict condition.** Choose \(s_0\) with \(q<s_0<s_*\) and \(s_0-q<M\). The finite-horizon construction works uniformly for \(\|z_0\|_{H^2}\le s_0-q\) with one common closed ball of radius \(2C_Bs_0\) and a uniform contraction constant \(<1\). In the Banach space \(\mathcal E_T\), the fixed-point equation is \(y=\Phi(y,z_0)\): \(p,v\) are affine continuous functions of \((y,z_0)\), while the nonlinear products \(yQy_t\), \(yE\), and \(w^2\) are continuous polynomial maps into \(L^2_{t,x}\), since \(\mathcal E_T\hookrightarrow L^\infty_{t,x}\) and \(H^2(I)\hookrightarrow L^\infty(I)\). Thus \(\Phi\) is continuously Fréchet differentiable in both variables. At the base fixed point \(\|D_y\Phi\|<1\), so \(I-D_y\Phi\) has a bounded Neumann-series inverse. The Banach implicit-function theorem gives an \(H^2\to\mathcal E_T\) derivative; the trace and force maps are bounded, giving (4.3) in \(Y\). This uses the fixed-point extension on an open neighborhood, whose restriction is the **actual** observation map there. It does not establish differentiability throughout \(\mathcal A_T^{\rm w}\).

## 5. What symmetry proves — and what it does not

Write \((Rf)(x)=f(L-x)\). Reflection preserves all coefficients, both equal thermal baths, the mean, and the fixed displacement. If \((u,\theta,z,\sigma)\) solves for \(z_0\), then

\[
\theta^R(x,t)=\theta(L-x,t),\quad z^R(x,t)=z(L-x,t),\quad
u^R(x,t)=g(t)-u(L-x,t),\quad \sigma^R=\sigma
\]

solves for \(Rz_0\). Whole-weak-class uniqueness proves that it is the unique admissible solution. In particular, reflection preserves \(B_M\), \(H^2\), positivity and the actual admissibility predicate. Its effect on the **labeled** observations is

\[
\mathcal O(Rz_0)=(F_A(z_0),\ Q_L(z_0),\ Q_0(z_0)).\tag{5.1}
\]

Therefore the force trace is reflection-invariant. Under \(q<s_*\), take any nonzero \(h\in H^2\) odd about \(L/2\) and scale it small enough to satisfy the existing smallness condition and \(B_M\). Then \(h\) and \(-h=Rh\) are distinct actual weak-admissible states with **identical force** for the fixed nonzero loading. This is an exact nonlinear force-only non-injectivity statement.

It is **not** a full-map counterexample: by (5.1) the two fluxes exchange, and they need not be equal. Under the same strict condition, the base \(z_0=0\) is symmetric, so its solution is symmetric. The derivative respects parity. For \(Rh=-h\), \(\bar h=0\), \(RY=-Y\), the force variation vanishes and the heat-power variations obey \(\delta Q_L=-\delta Q_0\). For \(Rh=h\), \(RY=Y\), and \(\delta Q_L=\delta Q_0\); force can also respond. Thus labeled sum/difference channels separate parity at first order; neither heat-flux channel can be discarded merely because the bar is symmetric. This structure does not prove that the odd channel, the even channel, or their combination has trivial kernel. An antisymmetric perturbation would be fully invisible only if its remaining flux trace also vanished; that is **not proved**.

## 6. Conditional compactness obstruction to Lipschitz recovery

This section proves a negative stability statement for the exact active map, not a non-injectivity theorem. Continue to assume the **unchanged** \(g_*\ne0\) satisfies \(q<s_*\).

### 6.1 Uniform forward dependence in the weaker norm on a small admissible neighborhood

Fix \(s_0\in(q,s_*)\) and a radius \(\rho<\min\{M,s_0-q\}\). The earlier contraction proof supplies a common ball \(\|y\|_{\mathcal E_T}\le R_0=2C_Bs_0\), with contraction constant \(\gamma<1\), for all \(H^2\) inputs of norm at most \(\rho\). For the **same trial temperature** and two inputs \(z_1,z_2\), put \(h=z_1-z_2\). The memory representations give

\[
\Delta p(t)=e^{-\mu t}Qh,\quad \Delta v(t)=e^{-\lambda t}\bar h,\quad
\Delta E=-r\mu e^{-\mu t}Qh,\quad
\Delta w=-e^{-\lambda t}\bar h-\alpha e^{-\mu t}Qh.\tag{6.1}
\]

Both trial \(w\)'s are uniformly bounded, because \(z_i\) are uniformly \(H^2\)-bounded and the trial temperatures lie in the common ball. Therefore products \(y\Delta E\) and \((w_1+w_2)\Delta w\) are bounded in \(L^2_{t,x}\) by \(C\|h\|_2\). The linear memory-initial term is also bounded by \(C\|h\|_2\). The linear estimate and the uniform contraction give

\[
\|y[z_1]-y[z_2]\|_{\mathcal E_T}\le C\|z_1-z_2\|_{L^2(I)},\qquad
\|\mathcal O(z_1)-\mathcal O(z_2)\|_Y\le C'\|z_1-z_2\|_2.\tag{6.2}
\]

The second bound uses the \(H^2\) endpoint trace and the mean-stress formula. Constants are uniform on this explicitly sufficient neighborhood, not asserted on all of \(\mathcal A_T^{\rm w}\).

### 6.2 Fréchet derivative extends compactly from \(L^2\) to observations

Equations (4.1)–(4.2) and the same linearized contraction estimate give a bounded linear solution map \(h\mapsto Y\) from \(L^2(I)\) to \(\mathcal E_T\): source terms containing \(h\) are in \(L^2\), because \(y_b,w_b\in L^\infty\); the coefficient involving \((y_b)_t\in L^2\) multiplies \(Y\in L^\infty\). The inverse of \(I-D_y\Phi\) is bounded by the uniform contraction estimate. Thus (4.3), originally derived for \(H^2\) directions, extends continuously to \(L^2\).

For any \(3/2<s<2\), the embedding

\[
H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I))\ \hookrightarrow\hookrightarrow\ L^2(0,T;H^s(I))
\]

is compact by the standard Aubin–Lions compactness theorem: \(H^2\hookrightarrow\hookrightarrow H^s\hookrightarrow L^2\). Since \(H^s(I)\) has bounded endpoint derivative traces for \(s>3/2\), the two heat-flux maps are compact into \(L^2(\delta,T)\). The \(\bar Y\) force term is compact as well; \(h\mapsto e^{-\lambda t}\bar h\) is rank one. Hence

\[
D\mathcal O(0):L^2(I)\longrightarrow Y\quad\text{is compact}.\tag{6.3}
\]

A compact operator on infinite-dimensional \(L^2\) cannot be bounded below: take any \(L^2\)-orthonormal sequence \(h_n\in H^2(I)\); it converges weakly to zero and (6.3) gives \(\|D\mathcal O(0)h_n\|_Y\to0\).

Suppose a local Lipschitz estimate \(\|z_1-z_2\|_2\le C\|\mathcal O(z_1)-\mathcal O(z_2)\|_Y\) held for **all actual admissible states** in some \(H^2\)-neighborhood of zero. For each \(h\in H^2\), the pair \((\varepsilon h,0)\) is in that neighborhood for sufficiently small \(\varepsilon\). Divide the estimate by \(|\varepsilon|\) and let \(\varepsilon\to0\), using (4.3), to obtain \(\|h\|_2\le C\|D\mathcal O(0)h\|_Y\), contradicting the orthonormal sequence. Therefore such a local **uniform Lipschitz** estimate is impossible. A single direction may require a different sufficiently small \(\varepsilon\); the same constant \(C\) is what creates the contradiction.

### 6.3 No strong-\(H^2\) inverse modulus on that neighborhood

Let \(\phi_n\) be \(L^2\)-normalized Dirichlet sine functions. Define \(z_n=\rho\phi_n/\|\phi_n\|_{H^2}\), with the above fixed \(\rho>0\). Then all \(z_n\) and zero lie in the **actual** admissible set, \(\|z_n\|_{H^2}=\rho\), and \(\|z_n\|_2\to0\). By (6.2), \(\mathcal O(z_n)\to\mathcal O(0)\) in \(Y\). Thus no modulus \(\omega(r)\to0\) can satisfy \(\|z_1-z_2\|_{H^2}\le\omega(\|\mathcal O(z_1)-\mathcal O(z_2)\|_Y)\) on that neighborhood. This is independent of whether the map is injective. The sequence stays inside the frozen \(H^2\) a priori ball; it is a theoretical argument, not a numerical experiment.

These negative results are for the frozen \(L^2\)-time observations and the stated norms. They do not rule out uniqueness, an \(L^2\) logarithmic/Hölder modulus, estimates in weaker source norms, or stability with stronger observations; such alternatives are not added to the experiment and require separate proof. They also cannot be asserted for the actual unspecified amplitude unless \(q<s_*\) is verified.

## 7. Kernel, nonlinear inverse, and suitable methods

**Linearized kernel.** The precise unknown is \(h\in H^2\) for which the solution of (4.1)–(4.2) has all three traces in (4.3) zero on \((\delta,T)\). The result above proves only that the operator is compact and not bounded below; compact operators can be injective or have a nontrivial kernel. No nonzero fully invisible \(h\) has been constructed, and no trivial-kernel proof is given. The derivative force channel is invisible on the odd subspace, but the flux-difference channel can still see it. The derivative also mixes infinitely many spatial modes through \(Q\) and through the time- and space-dependent active base. Thus the three outputs are not demonstrably redundant, although parity identifies their symmetry roles.

**Nonlinear inverse.** For two actual solutions, subtraction yields the exact difference system

\[
P_t=-\mu P+\lambda\beta QY,\quad V(t)=e^{-\lambda t}\overline{z_{0,1}-z_{0,2}},\quad
W=-V-\alpha P+\beta QY,
\]
\[
M_{\theta_1}Y_t-\kappa Y_{xx}=-bY\varepsilon_{2t}-b\theta_1rP_t+k\lambda(w_1+w_2)W.
\tag{7.1}
\]

Equality of force and both flux traces adds three homogeneous observation conditions, with the mean term visible in force. The coefficients in (7.1) are solution-dependent, and zero boundary temperature plus zero boundary heat flux does not automatically give \(Y=0\) when the interior ODE supplies an unknown distributed source. No general unique-continuation theorem is applicable without checking those coefficients and the nonlocal coupling. Nonlinear \(w^2\) may expose directions invisible at first order, or may create indistinguishable pairs; neither behavior is established here.

**Approaches and specific barriers.**

- **Volterra/source reduction:** (4.1) exposes \(e^{-\mu t}Qh\) and \(e^{-\lambda t}\bar h\); inserting this into (4.2) yields a parabolic equation with causal memory and a spatially unknown, time-modulated source. Active coefficients and the \(Qy_t\) mass term remain. A boundary inverse-source theorem must be checked for these terms, delayed observations, and \(L^2\)-time traces.
- **Adjoint/density:** Define the actual linearized solution operator and its \(Y\)-adjoint. Trivial kernel is equivalent to density of its adjoint range in the input Hilbert space. One must derive transposed boundary terms and prove the density; the failure of a bounded-below estimate in §6 does not decide density.
- **Spectral/Laplace:** A stationary constant-coefficient base might permit spectral analysis, but the actual base is driven and time-dependent. No analytic-in-time continuation from \((\delta,T)\) or pole separation for the active coefficients has been proved. The exponentially relaxing ODE can produce clustered modes; a simple heat-equation moment argument is not automatically valid.
- **Carleman/unique continuation:** The spatial nonlocal mass, coupled ODE and actual weak coefficient regularity must be included in a verified inequality. Scalar heat Carleman or observability inequalities cannot simply be quoted for (7.1). Delayed boundary observations need their own treatment.
- **Nonlinear perturbation:** Even a proved injective compact derivative would not by itself yield local injectivity via a standard Banach inverse function theorem: §6 shows it has no bounded inverse in the desired \(L^2\) norms. A stronger, appropriate quantitative estimate or different argument would be needed.

These are conditional research routes, not demonstrated proof strategies with all hypotheses checked and not a claim of intractability.

## 8. Scientific importance, gap, and decision

1. **Question:** Can one fixed mechanical/thermal boundary record distinguish distributed initial internal states that store information about a material's earlier deformation? For this stated model, even basic uniqueness of the full map is not known here.
2. **Why memory state matters:** In the single-exponential realization \(z_0\) affects future stress, relaxation and heat generation. If identifiable with meaningful stability, it could inform prediction or assessment from passive boundary observations. It does not uniquely encode all possible past histories, and the model does not validate an actual material or preparation procedure.
3. **Already established:** The literature above includes minimal-state equivalence, viscoelastic boundary observability and source reconstruction, memory-kernel identification and parabolic-memory observability. Green–Liu's single-boundary source result is especially close conceptually, with different dynamics and data norms. Sparse heat-source recovery is also established in related models.
4. **Precise unresolved gap:** No inspected theorem determines whether (3.2) is injective on the actual \(\mathcal A_T^{\rm w}\), with the one fixed nonzero control, the labeled fluxes, the delay, the nonlinear rank-one mass and independent initial memory. This is a gap in **our verified comparison**, not evidence that no existing theorem or corollary covers it; key primary sources remain inaccessible.
5. **Strongest meaningful target:** A proof, or a constructive counterexample, for the full nonlinear map on the actual admissible set; ideally a sharp **weaker-than-Lipschitz** stability/instability characterization on a genuine, explicitly nonempty subset under the frozen observations. A local active-linearization kernel result would be a prerequisite, not a substitute for that theorem. The sufficient smallness condition must be verified for actual parameters or stated explicitly.
6. **Q1 importance:** A sharp theorem that resolves the full nonlinear single-experiment question and characterizes the weak observability mechanism could potentially interest specialists, but journal importance and novelty cannot be promised. A routine adaptation, parity-only observation, or merely proving a familiar compactness obstruction for this special bar would not by itself meet the requested scientific-importance gate.

**Final decision: INSUFFICIENT EVIDENCE.** The exact implication and linearized kernel remain open, the fixed-amplitude sufficient condition is unverified, and exact overlap with several important primary sources is unchecked. We have not identified a genuinely new theory or demonstrated publication novelty. Do not promote the question to a promising novel problem or claim it is already solved on the basis of this search. Dr. Vipin Gupta makes the final decision.
