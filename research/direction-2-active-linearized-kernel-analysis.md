# Active linearized boundary-observation kernel

**Date:** 1 November 2026
**Verdict: CONDITIONAL THEOREM PROVED**

The conditional theorem is the exact parity decomposition and kernel characterization in §4, together with the interior-vanishing implication in §5. It **does not** prove that either parity kernel is zero or construct a nonzero member. The full active three-channel kernel remains **unresolved**. The condition for an actual full-horizon base and derivative is the prior strict sufficient small-data hypothesis; it has not been verified for the unspecified experiment.

This is an Arena research analysis, not independent certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. The result is not a new continuum theory, a nonlinear identification theorem, or a claim of literature novelty.

## 1. Model, assumptions and active linearization

Use exactly the constants and experiment of `direction-2-boundary-initial-state-identification-novelty-audit.md`: \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(m(t)=g_*\sin^2(\pi t/T)/L\), \(g_*\ne0\), \(\theta_* >0\), \(a,k,\lambda,c,\kappa,A_0>0\), \(b\ne0\); \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\mu=\lambda\alpha\), \(d=b^2/D\). Let \(\bar f=L^{-1}\int_I f\) and \(Qf=f-\bar f\).

For the actual nonzero driving, the base at \(z_0=0\) solves

\[
\begin{aligned}
(v_b)_t&=\lambda(m-v_b),& (p_b)_t&=-\mu p_b+\lambda\beta Qy_b,\\
w_b&=m-v_b-\alpha p_b+\beta Qy_b,& E_b&=m'+r(p_b)_t,\\
(cI+d\theta_b Q)(y_b)_t-\kappa(y_b)_{xx}
&=-b\theta_b E_b+k\lambda w_b^2,& \theta_b&=\theta_*+y_b,
\end{aligned}\tag{1}
\]

with \(v_b(0)=p_b(0)=y_b(0)=0\), \(y_b=0\) at both ends. This base is driven, not a zero equilibrium. Set \(q=|g_*|/L\); throughout we assume \(q<s_*\), where \(s_*\) is the positive data-only threshold (6.3) of the existence investigation, and \(M>0\). This sufficient condition provides a unique positive active base, an open \(H^2\) neighborhood of zero in the **actual** weak-admissible set, and the derivative used below. Nothing shows the specified but numerically unknown parameters satisfy it. All other physical parameters, sensor locations and time interval are unchanged.

For any \(h\in H^2(I)\), the associated temperature variation \(Y\), centered memory \(P\), mean memory \(V\), and relative-strain variation \(W\) satisfy

\[
\begin{gathered}
V=e^{-\lambda t}\bar h,\quad P_t=-\mu P+\lambda\beta QY,\quad P(0)=Qh,\\
W=-V-\alpha P+\beta QY,\quad Y(0)=0,\quad Y|_{\partial I}=0,\\
(cI+d\theta_bQ)Y_t-\kappa Y_{xx}
=-dYQ(y_b)_t-bYE_b-b\theta_b rP_t+2k\lambda w_bW.\tag{2}
\end{gathered}
\]

All four active terms are retained. The state regularity is \(Y\in\mathcal E_T=H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)\cap H^1_0(I))\), with endpoint normal derivatives in \(L^2(0,T)\). The centered ODE is in \(H^1_tL^2_x\), and

\[
P(t)=e^{-\mu t}Qh+\lambda\beta\int_0^t e^{-\mu(t-s)}QY(s)\,ds.\tag{3}
\]

The exact derivative of the three **labeled** observations is

\[
D\mathcal O(0)h=A_0\bigl(-b\bar Y-ke^{-\lambda t}\bar h,\ \kappa Y_x(0,t),\ -\kappa Y_x(L,t)\bigr)\big|_{(\delta,T)}.\tag{4}
\]

## 2. Correcting the requested kernel equations

The user-specified condition \(\bar Y=0\) is **not** the actual force-kernel condition for a general \(h\). By (4), the exact three conditions, in their trace spaces and for almost every \(t\in J=(\delta,T)\), are

\[
\boxed{b\bar Y(t)+k e^{-\lambda t}\bar h=0,\quad Y_x(0,t)=0,\quad Y_x(L,t)=0.}\tag{5}
\]

Thus \(\bar Y=0\) is equivalent to \(\bar h=0\) **within** the force kernel, but neither has been shown to follow for even input. Enforcing it unconditionally would alter the inverse question by discarding possible force-cancellation directions. For odd \(h\) both means vanish automatically, as shown below. A zero force trace is not a direct observation of temperature mean alone: it includes mean memory.

Since \(Y\in H^1_tL^2_x\), \(\bar Y\in H^1(0,T)\). For a zero force record (5), its continuous representative satisfies, for every \(t\in J\),

\[
\bar Y(t)=-\frac{k}{b}e^{-\lambda t}\bar h,\qquad
(\bar Y)_t(t)=\frac{k\lambda}{b}e^{-\lambda t}\bar h\quad\text{a.e.}\tag{6}
\]

Thus \(e^{\lambda t}\bar Y\) is constant there, and the interval fixes the product \(b\bar Y+kV\), not the two terms separately. The flux traces vanish as \(L^2(J)\) functions, so their **distributional** time derivatives vanish on \(J\); regularity here does not justify treating \(Y_{xt}\) as an ordinary endpoint trace. Nor does (5) alone imply \(Y=0\), \(P=0\), vanishing before \(\delta\), analytic continuation, or backward uniqueness.

One further exact interior constraint follows by spatially integrating (2) and using both zero endpoint derivatives. For almost every \(t\in J\),

\[
cL(\bar Y)_t+d\int_I\theta_bQY_t\,dx
=-d\int_IYQ(y_b)_t\,dx-b\int_IYE_b\,dx
-br\int_I\theta_bP_t\,dx+2k\lambda\int_Iw_bW\,dx.\tag{7}
\]

This balance and (3) hold with the full history starting at zero. They are necessary, not a proof that the interior state vanishes. No additional ordinary time derivatives of the active coefficients or the endpoint fluxes are assumed.

## 3. Reflection invariance of the actual active trajectory

Let \(Rf(x)=f(L-x)\). The reduced operators, \(Q\), constant coefficients, prescribed \(m\), equal thermal bath values and initial data commute with reflection. If \((y_b,p_b,v_b)\) solves (1), then \((Ry_b,Rp_b,v_b)\) solves the same problem. The prior whole-weak-class uniqueness theorem, available under the stated sufficient hypothesis, gives

\[
Ry_b=y_b,\quad Rp_b=p_b,\quad R\theta_b=\theta_b,\quad Rw_b=w_b,\quad RE_b=E_b
\quad\text{a.e.}\tag{8}
\]

The same reasoning applies to the linear system: the reflection of the solution for \(h\) is the solution for \(Rh\); uniqueness comes from the linearized fixed-point equation. Define orthogonal projections \(h_e=(h+Rh)/2\), \(h_o=(h-Rh)/2\). They preserve \(H^2\). The corresponding temperature and centered-memory solutions \((Y_e,P_e)\), \((Y_o,P_o)\) have their named parity and add to \((Y,P)\). In particular \(\bar h_o=\bar Y_o=\bar P_o=0\) and \(V_o=0\).

## 4. Proved conditional theorem: exact parity subsystems and kernel split

**Theorem.** Under §1, with \(\mathcal H_e=H^2(I)\cap\{Rh=h\}\) and \(\mathcal H_o=H^2(I)\cap\{Rh=-h\}\), the full observation kernel is the direct sum

\[
\ker(D\mathcal O(0)|_{H^2})=K_e\oplus K_o,\tag{9}
\]

where \(K_e\) consists exactly of those \(h_e\in\mathcal H_e\) for which

\[
b\bar Y_e+ke^{-\lambda t}\bar h_e=0,\qquad (Y_e)_x(0,t)=0\quad\text{in }L^2(J),\tag{10}
\]

and \(K_o\) consists exactly of those \(h_o\in\mathcal H_o\) for which

\[
(Y_o)_x(0,t)=0\quad\text{in }L^2(J).\tag{11}
\]

These \(Y_e,Y_o\) solve the following **exact**, not frozen-coefficient, subsystems:

\[
\begin{aligned}
(P_e)_t&=-\mu P_e+\lambda\beta QY_e,& P_e(0)&=Qh_e,\\
W_e&=-e^{-\lambda t}\bar h_e-\alpha P_e+\beta QY_e,\\
(cI+d\theta_b Q)(Y_e)_t-\kappa(Y_e)_{xx}
&=-dY_eQ(y_b)_t-bY_eE_b-b\theta_b r(P_e)_t+2k\lambda w_bW_e;
\end{aligned}\tag{12}
\]

\[
\begin{aligned}
(P_o)_t&=-\mu P_o+\lambda\beta Y_o,& P_o(0)&=h_o,\\
W_o&=-\alpha P_o+\beta Y_o,\\
(c+d\theta_b)(Y_o)_t-\kappa(Y_o)_{xx}
&=-dY_oQ(y_b)_t-bY_oE_b-b\theta_b r(P_o)_t+2k\lambda w_bW_o.
\end{aligned}\tag{13}
\]

Both have zero initial and Dirichlet boundary values for \(Y\). The odd formula uses \(QY_o=Y_o\), \(Q(Y_o)_t=(Y_o)_t\); it still has nonconstant active coefficients and ODE feedback.

**Proof.** By (8) and uniqueness, parity is preserved. For an even \(Y_e\), \((Y_e)_x(L)=- (Y_e)_x(0)\); for an odd \(Y_o\), \((Y_o)_x(L)=(Y_o)_x(0)\), in the \(L^2\) trace sense. With \(F=\delta F_A\), \(Q_0=\delta Q_0\), \(Q_L=\delta Q_L\),

\[
\begin{aligned}
F&=-A_0[b\bar Y_e+ke^{-\lambda t}\bar h_e],\\
Q_0+Q_L&=2A_0\kappa (Y_e)_x(0),\\
Q_0-Q_L&=2A_0\kappa (Y_o)_x(0).
\end{aligned}\tag{14}
\]

The invertible transformation \((Q_0,Q_L)\leftrightarrow(Q_0+Q_L,Q_0-Q_L)\) separates the observations. All three vanish exactly when (10) and (11) hold. Equations (12)–(13) are the projected system (2), so (9) follows. □

**Consequences and limitations.** Force and flux sum see only even inputs; flux difference sees only odd inputs. Neither subsystem is automatically injective: both (10) and (11) are still infinite-dimensional inverse-source problems. In particular, the labeled heat-flux difference **can detect** an odd direction, so two fluxes are not redundant with force. However, we have not shown that it detects **every** nonzero odd direction. Reflection of a nonlinear state exchanges labeled fluxes; force-only ambiguity disappears for a particular reflected pair only if the two fluxes differ. A universal elimination of ambiguity is unproved.

## 5. A second partial theorem and the exact missing step

**Theorem (interior vanishing, not a boundary uniqueness theorem).** Under §1, if \(D\mathcal O(0)h=0\) and, additionally, the corresponding \(Y=0\) almost everywhere on **all** \((0,T)\times I\), then \(h=0\).

**Proof.** The force relation on \(J\) and \(Y=0\) give \(\bar h=0\), hence \(V=0\). From (3), \(P=e^{-\mu t}h\). With \(W=-\alpha P\), (2) gives

\[
\lambda\alpha\,[b r\theta_b-2k w_b]\,e^{-\mu t}h=0
\quad\text{a.e. on }(0,T)\times I.\tag{15}
\]

At \(t=0\), \(\theta_b=\theta_*\) and \(w_b=0\). The maximal-regularity solution satisfies \(y_b\in C([0,T];H^1_0(I))\), hence \(C_tC_x\) in one dimension; the ODE representations give \(p_b,v_b\in C_tC_x\), so \(w_b\in C_tC_x\). Thus \(br\theta_b-2kw_b\) is uniformly nonzero on \((0,\varepsilon)\times I\) for some \(\varepsilon>0\), because \(br\theta_*\ne0\). Equation (15) implies \(h=0\). □

The extra premise \(Y=0\) in the interior is **not a measured condition** and has not been derived from the observations. On \(J\) alone, even if one could establish \(Y=0\), (3) gives

\[
P(t)=e^{-\mu(t-\delta)}P(\delta),\quad
P(\delta)=e^{-\mu\delta}Qh+\lambda\beta\int_0^\delta e^{-\mu(\delta-s)}QY(s)\,ds.\tag{16}
\]

Thus no inference \(P(t)=e^{-\mu t}Qh\) is justified without control of the earlier temperature history. Nor is the coefficient in (15) known to be uniformly nonzero on all of \(J\) merely from the previous positivity theorem. An exact missing qualitative estimate, sufficient with the theorem above, is the following **unproved** active-system boundary-to-interior statement:

\[
\text{for every }h\in H^2(I),\quad
(5)\ \Longrightarrow\ Y=0\ \text{in }L^2((0,T)\times I).\tag{17}
\]

It must include the delay and the full nonlocal/ODE history; (17) is stronger than necessary for trivial kernel, not asserted to be necessary. Alternatively prove the two independent uniqueness implications (10) \(\Rightarrow h_e=0\) and (11) \(\Rightarrow h_o=0\), without first proving (17). Either route would settle the actual linearized question. A weaker, meaningful conditional stability route would be an estimate of an appropriate weaker norm of each parity input by its corresponding measured channels, on an explicitly defined a priori class; an \(L^2\)-input Lipschitz estimate is impossible by §8.

## 6. Spatial spectral analysis with all active coefficients

The Dirichlet sine functions \(\phi_n=\sqrt{2/L}\sin(n\pi x/L)\), eigenvalues \(\nu_n=(n\pi/L)^2\), are a complete \(L^2\) basis. Reflection gives \(R\phi_n=(-1)^{n+1}\phi_n\), so even and odd **parity blocks** are invariant. This does not imply individual modes are invariant. Indeed, \(Q\phi_n=\phi_n-\bar\phi_n\) has a constant component when \(n\) is odd; the constant has an infinite odd-index sine expansion. Multiplication by the generally spatially dependent even functions \(\theta_b,w_b,E_b,Q(y_b)_t\) couples distinct sine modes of the same parity. No proof establishes a fixed diagonalizing eigenbasis for all times.

To make the coupling explicit, use \(L^2\) inner products and let

\[
\begin{gathered}
Y_j=(Y,\phi_j),\quad P_j=(P,\phi_j),\quad H_j=(h,\phi_j),\quad a_j=(1,\phi_j),\quad \bar Y=L^{-1}\sum_j a_jY_j,\\
B_{ij}=(\theta_b Q\phi_j,\phi_i),\quad H_{ij}=(\theta_b\phi_j,\phi_i),\quad
C_{ij}=((dQ(y_b)_t+bE_b)\phi_j,\phi_i),\\
K_{ij}=(w_b\phi_j,\phi_i),\quad K^Q_{ij}=(w_bQ\phi_j,\phi_i),\quad w_i=(w_b,\phi_i).
\end{gathered}
\]

Testing (2) with \(\phi_i\), and interpreting the sums as \(L^2\)-convergent expansions (or finite projections with their limits), yields for a.e. time

\[
\begin{aligned}
\dot P_i&=-\mu P_i+\lambda\beta(Y_i-a_i\bar Y),& P_i(0)&=H_i-a_i\bar h,\\
c\dot Y_i+d\sum_j B_{ij}\dot Y_j+\kappa\nu_iY_i
&=-\sum_j C_{ij}Y_j-br\sum_j H_{ij}\dot P_j\\
&\quad+2k\lambda\left[-e^{-\lambda t}\bar h\,w_i-\alpha\sum_jK_{ij}P_j+\beta\sum_jK^Q_{ij}Y_j\right].
\end{aligned}\tag{18}
\]

The variable-coefficient matrices are time dependent; they are block diagonal by reflection but not generally diagonal within each block. Equations (18) and (5) describe an infinite coupled moment system, but **completeness of that system is unproved**. Endpoint derivative traces are continuous maps from \(L^2_tH^2_x\), not necessarily termwise absolutely convergent series. Any modal boundary formula must be interpreted through convergent finite-mode approximants in the appropriate trace norm; distinct \(\nu_n\) are not a uniqueness proof.

The direct memory term in (3) has the **same** \(e^{-\mu t}\) factor for every centered spatial mode, not one distinct rate per mode. Its multiplier in the temperature forcing is \(\lambda\alpha[br\theta_b(t,x)-2kw_b(t,x)]\), which is time and space dependent, and feedback contributes the convolution in (3). The mean memory has \(e^{-\lambda t}\); since \(0<\alpha<1\), \(\mu\ne\lambda\), but these two exponents alone do not separate the unknown modes from the active parabolic response on \(J\). No indistinguishable mode or complete temporal-moment family has been established.

## 7. Primary literature reassessment and transfer test

This is a focused non-exhaustive reassessment. “Not applicable as stated” is not a proof of novelty or of impossibility of adapting a result.

1. **W. Green and S. Liu**, *Source reconstruction and stability via boundary control of abstract viscoelastic systems*, *Applicable Analysis* **101** (2022), 4991–5005, DOI [10.1080/00036811.2021.1877682](https://doi.org/10.1080/00036811.2021.1877682), [arXiv:2004.10842](https://arxiv.org/html/2004.10842), Theorems 1.1–1.3 directly inspected. They assume a self-adjoint compact-resolvent abstract spatial operator, a memory-free two-sided observation estimate (B), \(M\in H^2(0,T)\), \(T>T_0\), and for source recovery a known \(\sigma\in C^1\) with \(\sigma(0)\ne0\), zero initial displacement and velocity. Theorem 1.2 gives a two-sided \(\|f\|\) versus \(H^1_t\)-observation estimate; Theorem 1.3 gives a reconstruction series. A's equation is first order in heat, has a time-dependent nonlocal mass and feedback, and does not meet or establish (B); its prescribed data are delayed \(L^2_t\), not their \(H^1_t\) norm. The proof cannot be imported merely because (3) has an exponential source.
2. **W. Green, S. Liu and M. Mitkovski**, *Boundary Observability for the Viscoelastic Wave Equation*, *SIAM J. Control Optim.* **57** (2019), 1629–1645, DOI [10.1137/18M1180736](https://doi.org/10.1137/18M1180736). The author PDF remains inaccessible in this environment, so its precise theorem statement is **not independently verified**. Green–Liu's inspected introduction says their previous work treated a Dirichlet-Laplacian viscoelastic wave and boundary Neumann observations, using a Riesz sequence perturbation. That is a reliable contextual attribution, not a verification of the earlier paper's theorem assumptions. Wave observation and its exact-observability estimate do not establish the required parabolic–ODE kernel.
3. **S. A. Avdonin, S. A. Ivanov and J. M. Wang**, *Inverse problems for the heat equation with memory*, DOI [10.3934/ipi.2019002](https://doi.org/10.3934/ipi.2019002), [arXiv:1612.02129](https://arxiv.org/html/1612.02129), Theorem 4 inspected in the prior audit. Under its stated transform asymptotics and finite-propagation restriction, equality of boundary response operators determines the convolution kernel over a time interval. It concerns zero initial temperature and a varying boundary input/response operator, not a single initial-memory profile in (2); neither the unknown nor the data match.
4. **G. Lin, Z. Zhang and Z. Zhang**, *Theoretical and numerical studies of inverse source problem for the linear parabolic equation with sparse boundary measurements*, [arXiv:2111.02285v1](https://arxiv.org/html/2111.02285), Theorem 1 and Assumption 1.1 inspected. For their symmetric elliptic operator and semi-discrete, piecewise-constant-in-time spatial source, Theorem 1 also requires their spectral Assumption 2.4 and boundary flux equality on \(\Gamma\times(0,\infty)\). It recovers the paper's specified sources and time mesh. A's unknown drives an exponential, active variable-coefficient coupled source plus memory, with only \(J\); the theorem's source class and observation interval are not satisfied. It is evidence of related source uniqueness, not a result for (2).
5. **L. Ma, G. Wang and Y. Zhang**, *Sampling Observability for Heat Equations with Memory*, [arXiv:2411.14382v1](https://arxiv.org/html/2411.14382), Definition 1.3 and Theorem 1.7 inspected. Their heat-memory equation begins with known zero prehistory. For \(C^2\) memory and backward uniqueness at the selected times, a geometric condition gives a two-sided \(\mathcal H^{-4}\) estimate from spatial observations at selected times. The paper explicitly notes that backward uniqueness may fail for general memory kernels. Its initial unknown is the heat state, not independent \(P(0)\), and its interior observations are not the prescribed boundary data. It does not justify extending zero observations backward through \(\delta\).
6. **D. P. Jha and R. K. George**, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), §3 Carleman statement (44)–(46) inspected. Under their moving-control weight/geometric and delay-compatibility assumptions and a bounded delay operator, their stated estimate has a moving interior observation term and a history remainder, for their delayed heat operator. It is not a boundary Cauchy-data theorem for (2). A finite-exponential memory realization is a useful conceptual comparison, but the rank-one \(\theta_bQY_t\), exact coefficient regularity, initial memory and boundary traces require a new argument. We do not assert their later theorem's uninspected proof or transfer its conclusions.
7. **S. Vessella**, *Quantitative estimates of unique continuation for parabolic equations, determination of unknown time-varying boundaries and optimal stability estimates*, [arXiv:0710.2192v1](https://arxiv.org/html/0710.2192). The paper's §3.2 Theorem 3.2.3 presents a local parabolic Carleman estimate under its ellipticity and coefficient assumptions, and §3.3 treats quantitative continuation. Its principal operator is local; (2) contains \(\theta_b\overline{Y_t}\) and the independent ODE \(P\), which acts as a distributed unknown source. A scalar homogeneous boundary-unique-continuation conclusion cannot be asserted from that theorem without an estimate that controls those terms. This is a specific obstruction, not a claim that nonlocal continuation is impossible.

No inspected theorem proves either (10) or (11) for the prescribed active trajectory. Important full-text gaps, including the 2019 wave paper, remain. No extrapolation from abstracts has been used as a theorem.

## 8. Significance, stability and verdict

* **Compactness:** the preceding audit established, under the same strict condition, the derivative extends compactly \(L^2(I)\to L^2(J)^3\). A compact map can have zero or nonzero kernel.
* **Injectivity:** \(K_e=K_o=\{0\}\) is exactly the open question. The conditional parity theorem neither assumes nor proves it.
* **Approximate observability:** here this means the qualitative statement \(\ker D\mathcal O(0)=\{0\}\); in the \(L^2\) extension it is equivalent to density of the adjoint range. It is not the quantitative bounded-below estimate often called exact observability. An injectivity result only on \(H^2\) does not automatically establish injectivity of the \(L^2\) extension.
* **Conditional stability:** a modulus on an a priori set is a separate assertion. By compactness no uniform \(L^2\)-input Lipschitz lower bound with the frozen \(L^2\)-time outputs holds on the infinite-dimensional neighborhood. This does not exclude logarithmic/Hölder bounds or bounds in a weaker norm; none is proved here.
* **Practical recovery:** measurement noise, sensor accuracy and model mismatch would demand quantitative stability and validation, not merely a trivial kernel. No numerical experiment is undertaken.

A valid trivial-kernel theorem would resolve a crucial necessary first-order question for the prescribed experiment and provide an operator-theoretic basis for further inverse work, while not proving nonlinear injectivity. A genuine nonzero kernel construction would identify an infinitesimally invisible perturbation, but would not by itself prove nonlinear non-injectivity. Either could be scientifically meaningful if genuinely new and rigorously compared with prior work; neither novelty nor publication significance is established.

**Final verdict: CONDITIONAL THEOREM PROVED.** The theorem proves the exact parity split (9) and the separate interior-vanishing implication; it is conditional on the previous explicit sufficient smallness hypothesis and, in §5, an additional unmeasured interior premise. It does **not** determine whether the full prescribed active linearized kernel is trivial or nontrivial. The key unresolved task is a valid uniqueness or counterexample for (10) and (11), with the actual delayed observations and all active terms retained.
