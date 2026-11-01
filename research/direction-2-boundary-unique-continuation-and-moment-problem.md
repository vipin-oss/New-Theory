# Boundary continuation, memory and exact moment synthesis

## 1. A nonempty sign regime for the *actual* base

Use the frozen physical setup and constants of `direction-2-exact-adjoint-and-observability.md`; the explicit \(s_*\), \(K=\sqrt L\), \(C_B,W_s,W_R\) are given in `direction-2-exact-prior-art-and-overlap-audit.md`, (4), and `direction-2-active-base-existence-and-regularity.md`, (5)–(7). In one fixed consistent unit system, let \(q=|g_*|/L\) and
\[
C_y=2KC_B,\qquad C_w=W_s+2C_BW_R,\qquad
q_{\rm sign}=\frac{|br|\theta_*}{2(|br|C_y+2kC_w)},\qquad
0<q<\min\{s_*/2,q_{\rm sign}\}. \tag{1}
\]
All constants are finite and strictly positive, so this is a nonempty interval of **nonzero** load amplitudes for every fixed admissible material parameter set. The base fixed-point bound \(\|y_b\|_\infty\le C_yq\) and the audited Volterra bound \(\|w_b\|_\infty\le C_wq\) give
\[
\operatorname{sgn}(b)S(t,x)
=\lambda\alpha[|br|\theta_*+\operatorname{sgn}(b)(br y_b-2kw_b)]
\ge \tfrac12\lambda\alpha|br|\theta_*=:s_0>0 \tag{2}
\]
on all \([0,T]\times[0,L]\), using continuous representatives. In particular \(S(t,0)\) cannot vanish anywhere on \(J\) in this explicit smaller regime. At startup alone, \(S(0,x)=\lambda\alpha br\theta_*\ne0\) also follows from zero memory and \(g(0)=0\); continuity near zero by itself would **not** justify (2) on \(J\). We do not assert the user's unspecified amplitude satisfies (1), and do not replace the active base by equilibrium. Outside (1), endpoint nonvanishing during \(J\) has not been established.

The base structure yields \(M=c+d\theta_b\), \(S=\lambda\alpha(br\theta_b-2kw_b)\) and the displayed expression for \(B\) in the adjoint report. These shared fields give (2), but no known algebraic identity removes the independent unknown \(P\) from the parabolic equation. In particular \(SP\) is not a scalar potential times \(Y\).

## 2. A rigorous restricted-prior theorem

Let \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(q_n=2\pi n/L\), and \(k_n=\mathcal T\phi_n\). The already established active-base estimate is
\[
k_n=\frac a{q_n}+\rho_n,\quad a(t)=2A_0\sqrt{2/L}\,e^{-\mu t}S(t,0),\quad
\|\rho_n\|_{L^2(J)}=o(q_n^{-3/2}). \tag{3}
\]
By (2),
\[
\|a\|_{L^2(J)}\ge 2A_0\sqrt{2/L}\,s_0\left(\int_\delta^T e^{-2\mu t}dt\right)^{1/2}>0. \tag{4}
\]
Consequently there is a finite \(N_*=N_*(M,B,S,\delta)\) such that for **every fixed** \(n\ge N_*\),
\[
\|\rho_n\|_{L^2(J)}\le\|a\|_{L^2(J)}/(2q_n),\qquad
\|k_n\|_{L^2(J)}\ge\|a\|_{L^2(J)}/(2q_n)>0. \tag{5}
\]
This \(N_*\) is an existential, base-dependent cutoff, not a computable numerical value supplied by the little-o proof. Equivalently one can select any specific \(n\) for which the **actual** inequality in (5) is independently verified. The conclusion does not require knowledge of the sign of \(k_n(t)\) pointwise.

**Theorem — one-mode linear prior.** Under (1), fix one \(n\ge N_*\) and suppose the unknown is known in advance to belong to \(\{c\phi_n:c\in\mathbb R\}\). Then \(\mathcal T(c\phi_n)=c k_n\) is injective. The scalar is exactly determined by
\[
c=\frac{\langle\mathcal T(c\phi_n),k_n\rangle_{L^2(J)}}{\|k_n\|^2_{L^2(J)}}. \tag{6}
\]
The two labeled fluxes provide the same information on odd inputs, and the linearized force adds zero. This is a nonempty, exact **one-dimensional prior**, not recovery of arbitrary smooth, finite-sine, or odd \(H^2\) memory. Two unknown states must lie in the **same fixed line**; a union of distinct lines is not covered. No numerical physical base is assumed.

There is also a strictly local nonlinear restricted conclusion. For the actual full force-and-two-flux map \(\mathcal F\), the established small-load theory supplies \(C^2\) regularity on an \(H^2\) neighborhood. Define a bounded scalar output functional \(\ell\) that subtracts the two fluxes and pairs with \(k_n\), and \(F_n(c)=\ell(\mathcal F(c\phi_n)-\mathcal F(0))\). Then \(F_n'(0)=\|k_n\|^2>0\). Continuity of \(F_n'\) gives an \(\varepsilon_n>0\) such that \(F_n\) is strictly increasing on \((-\varepsilon_n,\varepsilon_n)\). Hence the full nonlinear observation is injective on this particular local one-dimensional segment. This does **not** establish local injectivity on any open infinite-dimensional \(H^2\) neighborhood, or between different modes. It is a direct scalar inverse-function argument, not a transfer of general linearized injectivity.

The one-column result is modest and is not a claim of a new theory or priority: prior reports already derived nonzero high columns under a sign assumption. Its value here is to combine that mechanism with the explicit actual-base regime (1), and to identify exactly what the prior restriction buys.

## 3. Actual Volterra reduction and boundary uniqueness attempts

Substituting the exact ODE solution gives, in \(L^2(Q_T)\),
\[
MY_t-\kappa Y_{xx}-BY-\gamma S(t,x)\int_0^te^{-\mu(t-s)}Y(s,x)ds
=S(t,x)e^{-\mu t}h(x),\quad Y(0)=0,\quad Y|_{\partial I}=0. \tag{7}
\]
The unknown \(h\) occurs as an inhomogeneous distributed source; the Volterra term contains the **actual whole history**. A forward Volterra resolvent can solve for \(Y\) given \(h\), but invertibility in the time variable does not prove that a single boundary trace determines \(h\). From \(\mathcal Th=0\), only \(Y_x(0,t)=Y_x(L,t)=0\) on \(J\) follows. Homogeneous Dirichlet and Neumann traces do not imply \(Y=0\) for an arbitrary *inhomogeneous* heat equation: for example, in an abstract test problem, \(Y=t x^2(L-x)^2\) with source \(F=Y_t-\kappa Y_{xx}\) is nonzero while both Dirichlet and Neumann endpoint traces vanish. This is not a physical invisible state and says only why a homogeneous scalar UC theorem cannot be applied to (7).

If an independent coupled boundary theorem did show \(Y=0\) on \(J\times I\), then (2) and the PDE give \(P=0\) there. For any \(t_0\in J\), (3) yields
\[
h=-\gamma\int_0^{t_0}e^{\mu s}Y(s)ds,\quad Y(t_0)=P(t_0)=0. \tag{8}
\]
This does not imply \(h=0\) without backward uniqueness or an injective pre-delay evolution. The sufficient fixed-delay Neumann condition in the adjoint report (12) would settle the pre-delay part, not the missing boundary theorem. Note that the natural half-interval reduction uses \(Y=0\) at \(x=L/2\) by oddness; no boundary condition for the ODE state is thereby introduced.

A boundary Carleman route would need an estimate that controls the unknown nondiffusive \(P\) from the boundary trace of \(Y\), including its nonzero value at the **start of observation** and the nonautonomous rough mass. Existing scalar source estimates do not close this: the right-hand side \(SP\) cannot be absorbed solely from \(Y=0\) at the boundary, and a weighted ODE estimate can leave an uncontrolled \(P(\delta)\) or time-slice term. The reachable graph might remove that term, but no estimate proving it has been found. A Laplace transform would additionally require a valid equation for time-dependent coefficient products; they do not become a simple diagonal algebraic resolvent. Time analyticity of \(S,M,B\) is not established from the smooth load. These are precise obstacles, not proofs of nonuniqueness.

## 4. Infinite moments and exact separations

The odd sine basis is orthonormal in \(H_o\). For \(h=\sum h_n\phi_n\in H_o\), boundedness of \(\mathcal T\) proves
\[
\mathcal Th=\lim_{N\to\infty}\sum_{n=1}^Nh_nk_n\quad\text{in }L^2(J),\qquad
\langle\mathcal T^*f,\phi_n\rangle=\langle f,k_n\rangle. \tag{9}
\]
No termwise equality follows from zero of the limiting sum. For the exact dynamics, \(u_n=(Y,\phi_n),p_n=(P,\phi_n)\) satisfy
\[
\sum_m(M\phi_m,\phi_n)u_m'+\kappa q_n^2u_n=(BY,\phi_n)+\sum_m(S\phi_m,\phi_n)p_m,\quad p_n'+\mu p_n=\gamma u_n,\quad p_n(0)=h_n. \tag{10}
\]
The sums are the \(L^2\) limits of spectral projections, not independent modal ODEs; \(M,S,B\) need not be spatial constants. The boundary trace is the \(L^2(J)\) limit of the corresponding finite sine derivative sums by \(L^2_tH^2_x\) convergence and trace continuity. Equation (9) includes all pre-delay evolution of each column.

Actual questions remain distinct:

* **Synthesis injectivity:** \(\sum h_nk_n=0\) in \(L^2(J)\Rightarrow h=0\), exactly the \(H_o\) kernel problem.
* **Adjoint range:** each \(\phi_n\) is approximable by \(\mathcal T^*f\); this is equivalent to synthesis injectivity.
* **Output completeness:** \(\overline{\operatorname{span}}\{k_n\}=L^2(J)\), equivalently \(\ker\mathcal T^*=0\), a different property.
* **Minimality:** \(k_n\notin\overline{\operatorname{span}}\{k_m:m\ne n\}\) for each \(n\); it suffices for synthesis injectivity by biorthogonal tests, but is not necessary and is not known here.

All four are unproved for the actual infinite family. The nonzero columns in (5) do not prove finite independence, and positive rank of any finite truncation cannot rule out an infinite \(\ell^2\) relation. Conversely, approximate cancellations or numerical near-null vectors can converge weakly to zero and do not produce a nonzero exact state. A finite-dimensional prior spanned by prescribed \(\phi_{n_1},\ldots,\phi_{n_d}\) is identifiable **if and only if** its exact continuous-time Gram matrix \(((k_{n_i},k_{n_j}))\) is positive definite; no such multi-mode Gram is asserted or numerically invented.

## 5. Adversarial primary literature audit

The following labels describe inspection of named statements/proof passages, not exhaustive reading or a priority search. They do not certify an external theorem's proof independently.

| Source and inspected location | Structure, data, result | Why it does not settle the actual problem |
|---|---|---|
| Wang–Zhang–Zuazua, [analytic memory](https://arxiv.org/html/2101.10615), (1.1), Proposition 2.4 proof and Theorem 2.6 / Lemma 2.7 proof: **FULL TEXT AND RELEVANT PROOF INSPECTED** | \(\partial_ty-\Delta y+\int_0^t M(t-s)y(s)ds=0\); analytic nonzero time kernel, \(y_0\in L^2\), interior space-time set satisfying their moving observation condition. Inequality controls \(\|y_0\|_{\mathcal H^{-4}}\), hence uniqueness. Proof exploits time analyticity and the observation geometry. | Initial unknown is heat state, not independent ODE memory; source \(S(t,x)e^{-\mu t}h\), spatially/time-dependent coefficients and endpoint flux are absent. Their analytic kernel is not proof of analyticity of the active system. |
| Jha–George, [delay and memory](https://arxiv.org/html/2506.22221), Theorem 3.10 proof (76)–(80), Assumptions 3.9, 3.11–3.12: **FULL TEXT AND RELEVANT PROOF INSPECTED** | Parabolic–ODE memory with moving **interior** control; estimate combines ODE and parabolic weights, with short-time closure and assumed adjoint UC/compactness–uniqueness. | UC is an explicit assumption, not an automatic consequence; geometry, initial state and coefficients do not map to the fixed endpoint trace. The proof's terminal remainder illustrates the unresolved history term. |
| Apraiz–Lecaros–Zamorano, [coupled parabolic/ODE factorization](https://arxiv.org/html/2610.26157), Theorem 2.3 proof (16)–(17): **FULL TEXT AND RELEVANT PROOF INSPECTED** | Kelvin–Voigt heat–ODE factorization, bounded spatial coefficient, weighted interior observation and time-slice term; estimates used for inverse coefficient recovery. | Their proof retains a snapshot term; it is not a boundary-only reachable-memory initial-data theorem and does not justify discarding \(P(\delta)\). |
| Olive, [boundary approximate controllability](https://arxiv.org/html/2609.09982), Theorem 1.1, Remark 1.3 and Appendix A: **THEOREM STATEMENT INSPECTED, PROOF NOT FULLY INSPECTED** | Autonomous semigroup with compact resolvent, complete adjoint root vectors and relatively bounded observation; spectral test characterizes infinite-time UC; analyticity yields finite-time property in the paper's diffusive systems. | Actual problem is nonautonomous and includes a nondiffusive ODE block; compact-resolvent and complete root-vector hypotheses are not shown, nor finite-time analyticity. An eigenfunction test cannot be imported. |
| Halanay–Pandolfi, [Coleman–Gurtin memory](https://arxiv.org/html/1404.2745), Theorems 2–3 and §2.1–§3: **FULL TEXT AND RELEVANT PROOF INSPECTED** | \(C^1\) convolution kernel multiplying the Laplacian, scalar heat initial datum, boundary or interior control; approximate controllability and, under a nonzero resolvent condition, failure of null controllability. Their proof uses a Volterra transformation and diagonal Laplacian modes. | The target is a scalar temperature state, not recovery of an independent distributed initial ODE memory. Null-controllability failure is not an invisible input for our observation. Actual time/space multipliers obstruct their diagonal reduction. |
| Li–Li–Zhou, [delayed source flux](https://arxiv.org/html/2609.10071), Theorem 1.3, §5 Lemmas 5.1–5.2: **FULL TEXT AND RELEVANT PROOF INSPECTED** | Scalar separated source \(f(x)g(t)\), \(g\) sector-holomorphic and \(g(0)\ne0\), spectral prior \(f\in\operatorname{Dom}(A^\sigma)\), \(\sigma>d/4\), geometry hypothesis, delayed boundary measurement of \(\partial_t\partial_\nu u\). Their double-log estimate gives uniqueness. | \(SP\) is coupled and not a known separated source; actual coefficient analyticity, observation regularity and all geometric/spectral assumptions are not established. Their delayed analytic-continuation proof cannot be silently applied. |
| Hào–Oanh, [parabolic initial state from boundary observations](https://doi.org/10.1515/jiip-2015-0055): **ABSTRACT OR METADATA ONLY** | Scalar parabolic initial recovery and boundary observation; abstract reports variational adjoint and numerical reconstruction. | Precise spaces, boundary type and uniqueness proof not accessed. Exact overlap remains unresolved; no theorem conclusion is inferred from the abstract. |

No located theorem has been shown to prove the actual coupled reachable-graph boundary result. This is a targeted search, not exhaustive; neither absence of overlap nor novelty is asserted.

## 6. Exact physical invisible-state search

A genuine construction must choose \(h\in X_o\setminus\{0\}\), solve (7) with its unmodified active coefficients and establish zero in \(L^2(J)\), not merely at sampled times. The most explicit candidate equation is (9), an infinite synthesis null relation with coefficients constrained to be an admissible \(H^2\) state. No such relation or invariant subspace has been constructed. The sign bound (2) and nonzero high columns rule out individual high sines, not signed combinations. The compact perturbation form of \(D_\delta\) only gives finite-dimensionality of possible pre-delay losses; it does not create one. Neither an abstract source counterexample nor a manufactured coefficient case is a physical invisible state.
