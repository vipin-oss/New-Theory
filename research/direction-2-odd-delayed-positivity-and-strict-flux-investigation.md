# Delayed positivity and strict boundary flux: audit and conditional tests

**Date:** 1 November 2026. **Decision: REFORMULATE.** The unchanged active experiment has a proved initial cooperative interval, but no verified overlap with its prescribed delayed observation window. A dimensionless, checkable sufficient condition for overlap and a sharper full-horizon small-load threshold are given below. Strict flux, cone exclusion on the actual window, and the full odd kernel remain unproved. No nonzero invisible input has been constructed; no new foundational continuum theory or demonstrated novelty is claimed.

This is an Arena single-agent recalculation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This report does not change the experiment or write a manuscript.

## 1. System and audit

Take the predecessor's hypotheses and notation: \(a,k,c,\kappa,\lambda,\theta_*>0\), \(b\ne0\), \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(d=b^2/D\), \(Qv=v-\bar v\). The symmetric loaded base has \(m(t)=g_*L^{-1}\sin^2(\pi t/T)\), \(q=|g_*|/L\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\). The odd input is \(h\in X_o=H^2(0,L)\cap L^2_o\), with bounded extension to \(H_o=L^2_o\). The genuine equations are
\[
M Y_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad Y(\cdot,0)=0,\ P(\cdot,0)=h,
\quad Y(0,t)=Y(L,t)=0,
\]
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b,\quad
\mathcal T h=2A_0\kappa Y_x(\cdot,0)|_J.
\]
No ODE boundary condition is imposed. In particular \(Y(\cdot,0)=0\) is initial data, not interior vanishing inferred from the two spatial endpoint conditions. We assume the prior sufficient base condition \(0<q<s_*\); it and all additional numerical inequalities below are **not verified for the actual experiment**. They are sufficient conditions, not changes to the prescribed loading.

The exact base identities, with \(v_b=\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds\), are
\[
p_b=\gamma\int_0^t e^{-\mu(t-s)}Qy_b(s)ds,\qquad
w_b=m-v_b-\alpha p_b+\beta Qy_b.
\]
These retain relaxation and the full thermal history. Since \(\operatorname{sgn}\gamma=\operatorname{sgn}b\),
\[
S\gamma\ge\lambda\alpha|\gamma|\{ |b|r\theta_*-|b|r\|y_b(t)\|_\infty-2k\|w_b(t)\|_\infty\}.
\]
This verifies the predecessor's sign, including negative \(b\). Its \(Y_*(t)=\sqrt2R_bt^{1/4}\) and \(W_*(t)=q\pi^2(t/T)^2(1+\lambda t/3)+2(|\beta|+\alpha|\gamma|t)Y_*(t)\) follow from the stated energy components, the one-dimensional boundary inequality and \(\|Qy\|_\infty\le2\|y\|_\infty\). The bound is conservative. Crucially \(R_b\) is a numerical fixed-unit norm combining dimensional components; it is not itself an invariant physical scalar. The old displayed inequalities are valid in the chosen normalization, not unchanged numerically under arbitrary changes of units. The existence report explicitly makes this fixed-units qualification. The early positive interval is not automatically a delayed one.

## 2. Unit-invariant delayed criterion and sinusoidal sharpening

Set \(\xi=x/L\), \(\sigma=t/T\), \(u=y_b/\theta_*\), \(\rho=\lambda T=10\), \(\eta=2k/(|b|r\theta_*)\), \(\zeta=|\beta|\theta_*\). The model gives dimensionless \(w_b,q,\eta,\zeta,\alpha,\rho\). Choose a **dimensionless** verifiable bound
\[
\mathfrak R\ge \|u_\sigma\|_{L^2((0,1)^2)},\qquad
\mathfrak R\ge \operatorname*{ess\,sup}_{\sigma\in(0,1)}\|u_\xi(\sigma)\|_{L^2(0,1)}.
\]
For example use the maximum of the rescaled componentwise existence bounds: if \(\|y_t\|_{L^2_{t,x}}\le R_t\), \(\sup_t\|y_x\|_{L^2_x}\le R_x\), take \(\mathfrak R=\max\{\sqrt{T/L}R_t/\theta_*,\sqrt L R_x/\theta_*\}\). Using \(R_t=R_x=R_b\) is allowed only after using their correct component units. Thus changes of physical units transform the dimensional components and scales together; the displayed \(\mathfrak R\) and every term below are invariant. If the prior fixed-unit constants cannot be converted without the normalization convention, \(\mathfrak R\) remains a separately verifiable base bound, not a fabricated number.

From zero initial temperature, Cauchy–Schwarz and the spatial boundary condition,
\[
\|u(\sigma)\|_\infty\le \mathcal Y(\sigma):=\sqrt2\,\mathfrak R\sigma^{1/4}.
\]
The old estimates imply a unit-invariant sufficient criterion at a given \(s\in(0,1]\):
\[
\mathcal Y(s)+\eta\{q\pi^2s^2(1+\rho s/3)+2\zeta(1+\alpha\rho s)\mathcal Y(s)\}\le1/2. \tag{A}
\]
The left side is nondecreasing, so (A) gives \(S\gamma\ge\frac12\lambda\alpha|\gamma||b|r\theta_*\) for all \(0\le\sigma\le s\). In particular if (A) holds **strictly** at \(s=0.01\), continuity of the explicit left side yields an \(\varepsilon>0\) and strict positive coupling on \((\delta,\delta+\varepsilon)\); equality alone need not give overlap. If (A) holds at \(s=1\), it gives the entire window. These are explicit conditional conclusions, not experimentally verified statements.

The actual sinusoid gives a sharper computable alternative without invented data. Since \((m-v_b)(t)=\int_0^t e^{-\lambda(t-s)}m'(s)ds\), define
\[
F_\rho(\sigma)=\pi\int_0^\sigma e^{-\rho(\sigma-s)}|\sin(2\pi s)|ds.
\]
This uses the exact forcing and is no worse than its own triangle estimate \(\pi^2\sigma^2\); it is not claimed always smaller than every other bound. Also using the exponential ODE kernel instead of replacing it by one gives
\[
\|w_b(T\sigma)\|_\infty\le qF_\rho(\sigma)+2\zeta(2-e^{-\alpha\rho\sigma})\mathcal Y(\sigma).
\]
Consequently, for any \(s\), the explicit test
\[
\sup_{0\le v\le s}\Big[\mathcal Y(v)+\eta\{qF_\rho(v)+2\zeta(2-e^{-\alpha\rho v})\mathcal Y(v)\}\Big]\le1/2 \tag{B}
\]
gives the same uniform lower bound through \(Ts\). Strict inequality at \(s=.01\) gives a delayed subinterval by continuity; the condition at \(s=1\) gives the whole horizon. One can alternatively evaluate the exact signed convolution before taking its absolute value, or a certified bound on the actual base; neither is evaluated here.

### Full-horizon constant audit

The existence report supplies \(\theta_b\ge\theta_*/2\) under its small-load assumptions and \(\|w_b\|_\infty\le C_wq\), \(C_w=W_s+2C_BW_R\), \(W_s=2+(1+2\alpha)S_L\), \(W_R=2|\beta|(1+\alpha\lambda T)K_x\). With these exact constants and their fixed-unit normalization,
\[
S\gamma\ge\lambda\alpha|\gamma|\bigl(|b|r\theta_*/2-2kC_wq\bigr).
\]
The predecessor's \(q_{\rm nd}=|b|r\theta_*/(8kC_w)\) indeed gives a strict lower bound exceeding one quarter of the nominal factor. For mere strict positivity the sufficient threshold sharpens to \(q<|b|r\theta_*/(4kC_w)\), jointly with \(q<s_*\) and every condition used for \(\theta_b\ge\theta_*/2\). At equality the estimate only yields nonnegativity. This is a sharper consequence of the same bound, not a verified parameter value or a necessary condition.

## 3. Comparison, regularity and genuine trace

On \(I_-=(0,L/2)\), oddness gives a Dirichlet temperature at the midpoint. Set \(Z=\operatorname{sgn}\gamma P\), \(C_+=\operatorname{sgn}\gamma S\). Whenever \(S\gamma\ge0\), the equations are
\[
M Y_t-\kappa Y_{xx}=BY+C_+Z,\qquad Z_t+\mu Z=|\gamma|Y.
\]
For \(\operatorname{sgn}\gamma h\ge0\) on \(I_-\), the predecessor's negative-part argument is valid at the stated regularity: \(Y_-\in L^2H^1_0\), \(-Y_-/M\) is an admissible time-dependent spatial test by \(M\ge m_0>0\), \(M_x\in L^\infty_tL^2_x\); use time integration and standard truncation/density to justify the chain rule \(Y_t(-Y_-)=\tfrac12\partial_t\|Y_-\|_2^2\). Dividing the PDE before testing avoids differentiating \(M\) in time. The diffusion cross term is controlled by one-dimensional \(\|Y_-\|_\infty^2\le2\|Y_-\|_2\|(Y_-)_x\|_2\), Young's inequality and \(\|M_x\|_2^4\in L^1_t\). The \(BY\) term is bounded with \(\|B(t)\|_2^4\|Y_-\|_2^2\), integrable because \(B\in L^\infty_tL^2_x\) in the active base class. The coupling contributes no positive adverse term when \(Z\ge0\), and in general is bounded by \(C\|Y_-\|_2\|Z_-\|_2\); the ODE yields \(-|\gamma|YZ_-\le|\gamma|Y_-Z_-\). Gronwall with zero negative initial parts gives \(Y,Z\ge0\). The initial sign interval and the full-horizon conditional result from the predecessor are thereby confirmed.

The active estimates include \(B\in L^2_{t,x}\) globally and, on positive-time strips, \(B\in L^6_{t,x}\cap L^\infty_tL^2_x\cap L^2_tL^\infty_x\); \(M,S\in L^\infty\), \(M\in C_tH^1_x\), and the earlier spatial-Lipschitz and time-Hölder improvements hold on \(J\). These do not imply bounded \(B\). For a.e. \(t\), \(Y(t)\in H^2\cap H^1_0\), hence its derivative has a genuine endpoint trace and nonnegative \(Y\) implies \(Y_x(t,0)\ge0\). This is an \(L^2\)-time trace, not a pointwise-in-time classical flux or a strict inequality. No boundary trace of \(Y_t\) or \(Y_{xx}\) is asserted.

## 4. Strict flux and exactly what would follow

If \(S\gamma\) stays uniformly positive from zero through a time beyond \(\delta\), and \(h\) has the above cone sign and is nonzero, then \(Z(t)\ge e^{-\mu t}Z(0)\) a.e. In the actual \(H^2\) input class a nonzero nonnegative \(Z(0)\) is positive on some interior interval, so the heat source is positive there for positive times; for the \(L^2\) extension it is only positive on a set of positive measure. However the missing step is a rigorously applicable positivity-improving propagation and boundary point lemma for the actual time-variable coefficients, unbounded-in-spacetime potential, weak solution and a.e. derivative trace. The integrating factor based on \(\|B/M\|_\infty\in L^1_t\) on positive-time strips removes an adverse zero-order part, but by itself does not prove Hopf or propagation from measurable forcing. Applying a scalar strong maximum principle before proving the coupled source nonnegative would be invalid.

**Conditional cone theorem.** Suppose, in addition to the base hypotheses and sign on \([0,t_1]\) with \(t_1>\delta\), an applicable scalar positivity-improvement and boundary lemma is proved for this precise solution and coefficient class, yielding \(Y_x(t,0)>0\) on a positive-measure subset of \((\delta,t_1)\) for every nonzero input in the cone. Then \(\ker\mathcal T\) meets that cone only at zero, and likewise for its negative. These extra analytic assumptions are not verified. The claim is narrower than linear-space injectivity: two positive outputs can cancel after subtraction, and strict positivity of generators does not give independence of their span. No conclusion follows for sign-changing \(h\), arbitrary sums, or the full odd kernel. Positivity merely before \(\delta\) gives no observation-window conclusion.

## 5. Primary theorem checks and gaps

* Ekström–Tysk, [*A boundary point lemma for Black–Scholes type operators*, Theorem 1.1](https://www2.math.uu.se/~johantys/Hopf), was inspected in the primary text. It states a uniform-parabolic boundary lemma in the paper's classical Black–Scholes setting, assumes strict interior comparison near the boundary point at earlier times, and concludes a strictly positive inward **liminf quotient**. It is stated for their homogeneous non-divergence operator, not for our source-driven weak solution with rough potential. Uniform ellipticity alone does not supply the strict-interior hypothesis, the right solution class, or the coupled propagation. Thus it cannot be directly invoked here. Their theorem is presented as a known result and cites earlier sources; no independent proof of this classical theorem is supplied there.
* Feehan, [*Maximum principles for boundary-degenerate linear parabolic differential operators*](https://arxiv.org/html/1306.5197), introduction and operator/solution setting inspected. It treats a specific non-divergence operator and boundary-degenerate structure, with stated classical/Sobolev or viscosity solution frameworks. This is not by itself an application to the source-driven coupled system; the precise theorem and proof needed to bridge the actual weak boundary trace were not verified. No claim of applicability is made.
* Gaitan, [Theorem 2.2 and Assumption 2.1](https://arxiv.org/html/0706.1422), and Jha–George, [Lemma 3.5, Lemma 3.7 and Proposition 3.8](https://arxiv.org/html/2506.22221), were checked in the predecessor: respectively a scalar time-independent-conductivity Carleman estimate with residual and a constant-principal delay/memory result with moving interior observation and a remainder. Neither supplies the needed actual endpoint-flux strictness or coupled kernel theorem. See that report for exact mismatch and inspected proof scope.

The intended Feehan PDF and Nazarov PDF fetches failed, though Feehan HTML was accessible. This narrow search is not exhaustive. No theorem is inferred from an abstract, and no literature nonexistence claim is made.

## 6. Backward adjoint, Gram test and pre-delay state

The predecessor's transposition construction is an actual weak construction, not merely a formal Riesz label. For \(f\in L^2(J)\), solve the zero-initial forward source problem and represent its bounded endpoint functional. The resulting \((z,w)\in L^2_{t,x}^2\) satisfies distributionally
\[
-\partial_t(Mz)-\kappa z_{xx}-Bz-\gamma w=0,\qquad -w_t+\mu w-Sz=0,\quad w(T)=0,
\]
and the boundary data \(z(0,t)=2A_0\mathbf1_Jf\), \(z(L,t)=0\) and temperature terminal condition are encoded by the forward-residual duality, not asserted as classical traces. In particular \(w\in H^1_tL^2_x\), \(w(0)=\int_0^T e^{-\mu t}S(t)z(t)dt\), and
\[
\langle\mathcal T h,f\rangle=\langle h,\Pi_o w(0)\rangle.
\]
For nonnegative \(f\), neither \(z\ge0\) nor a sign of \(\Pi_o w(0)\) follows merely from this identity: full-domain one-end boundary data and signed \(S,\gamma\), weak transposition and odd projection all matter. If a separately justified positivity-preserving backward theorem on the half-interval supplies a strictly positive dual pairing with every nonzero cone input, it yields the conditional cone exclusion above; such a theorem is not proved here. Density of the adjoint range would give all-input injectivity, but is open.

With \(D_\delta h=P(\delta)\), \(U h=Y(\delta)\), \(E=\ker D_\delta\), \(N=E\cap\ker U\), and \(F_*=U(E)\), the predecessor's finite-dimensional criterion is exact: for a basis \(v_i\) of \(F_*\) and \(e_i\in E\) with \(Ue_i=v_i\), \(G_{ij}=\langle\mathcal T e_i,\mathcal T e_j\rangle\) is positive definite iff the vertical flux kernel \(F_0\) is zero. A basis of all \(E\) tests instead \(E\cap\ker\mathcal T\), including \(N\). Cone signs of some vectors do not prove Gram rank, and no matrix or rank has been computed.

The delayed memory identity \(D_\delta=e^{-\mu\delta}I+K_\delta\), \(K_\delta:H_o\to H^2\cap H^1_0\) bounded, implies \(P(\delta)\in H^s\iff h\in H^s\) for \(0\le s\le2\): subtract the \(H^2\) term and multiply by the nonzero scalar. This is ordinary spatial Sobolev regularity, not preservation of endpoint compatibility or smoothing of arbitrary \(h\). Compactness makes \(D_\delta\) Fredholm, not necessarily injective. The previous explicit condition \(\|K_\delta\|<e^{-\mu\delta}\) implies invertibility by Neumann series, but is unverified. The joint backward implication \((Y(\delta),P(\delta))=(0,0)\Rightarrow h=0\) also remains open: a forward energy upper bound does not provide a backward lower bound. Nor does \(P(\delta)=0\) follow from zero measured flux.

## 7. Sixteen-item status table

| # | Question | Status | Reason |
|---|---|---|---|
| 1 | Base formulas and signs | Verified under prior existence assumptions | Exact convolution and \(S\gamma\) bound retain both signs of \(b\). |
| 2 | Prior fixed-unit estimates | Correct with qualification | Numerical combined norm is not invariant under changing units. |
| 3 | Dimensionless delayed test | Conditional | (A) or (B), strict at 0.01, gives overlap; no actual bound supplied. |
| 4 | Sinusoidal sharpening | Conditional | Exact forcing and exponential kernel give (B); no numerical evaluation. |
| 5 | Full-horizon \(q_{\rm nd}\) | Verified conditionally | Prior 1/8 threshold works; 1/4 suffices for strict sign with all base assumptions. |
| 6 | Weak cooperative comparison | Proved on sign interval | Negative-part tests and integrable coefficients; not a coupled maximum principle for signed sources. |
| 7 | Boundary flux nonnegative | Proved a.e. on sign interval | Genuine \(H^2\) endpoint derivative; delayed overlap conditional. |
| 8 | Strict interior positivity | Open for actual weak class | Positivity-improving theorem and hypotheses not established. |
| 9 | Strict endpoint flux | Open | Applicable boundary lemma and a.e. trace connection missing. |
| 10 | Sign-cone kernel exclusion on \(J\) | Conditional | Requires overlap and strict-flux result, both unverified. |
| 11 | Signed inputs and linear spans | Open | Cancellation prevents cone inference. |
| 12 | Backward adjoint cone | Open | Actual transposition equations known; positivity not proved. |
| 13 | Finite vertical Gram criterion | Proved criterion, rank open | Positive definiteness equivalent to \(F_0=0\), no rank computed. |
| 14 | Memory Sobolev equivalence | Proved | Nonzero identity plus \(H^2\) correction. |
| 15 | \(D_\delta\) and joint state injectivity | Open | Fredholm/conditional Neumann test; no backward uniqueness established. |
| 16 | Full odd flux kernel / nonzero invisible input | Open / not constructed | Neither all-input uniqueness nor an exact counterexample is known. |

The next specific task is to verify a primary positivity-improvement and boundary point theorem in the actual nonautonomous weak class, or prove an appropriate barrier/heat-kernel result, together with a certified dimensionless base bound showing delayed sign. Neither a potentially publishable conditional theorem nor an observation-state reduction would by itself establish a new continuum theory.

**Final verdict: REFORMULATE — DELAYED POSITIVITY AND STRICT-FLUX EXCLUSION REMAIN CONDITIONAL.**
