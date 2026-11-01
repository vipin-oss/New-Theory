# Actual delayed boundary identification: direct, moment and counterexample investigation

**Final verdict: STRUCTURAL OBSTRUCTION IDENTIFIED.** This means the rigorously demonstrated obstruction in §6—finite column data and arbitrarily accurate operator-norm information, even together with the actual leading profile and high-frequency rate, do not decide the infinite-dimensional kernel. It is **not** a proof that the active PDE–ODE itself is noninjective or that no proof is possible. Neither full odd-channel linear injectivity nor an actual invisible initial state was obtained. The required numerical comparison could not be performed because no physical parameter set or active-base coefficient data are supplied; no values are invented.

The investigation proves, conditionally on the inherited active-base and strong-forward hypotheses, a sharper actual-operator high-frequency tail and singular-value bound (§5); an exact finite-data obstruction (§6); and an actionable **sufficient**, but unverified, moment-control criterion with an explicit tail-versus-Gram threshold (§7). A nonzero-load smallness regime proves nonvanishing of every sufficiently high **individual** mode, not full injectivity (§2). These are mathematical results for the existing inverse problem, not a new continuum theory, a novelty claim, or a nonlinear identification result.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is an Arena research investigation, not separate human certification. Direction 1 remains rejected. The literature search and proof attempts are targeted, not exhaustive.

## 1. Exact active model and evidence base

The specified reports on formulation A, existence, active linearization, parity, boundary unique continuation, positivity, delayed states, exact kernels, high-frequency analysis, separation, and the latest adjoint audit were inspected. Their full histories and hypotheses remain frozen. The starting commit and clean branch were verified. Let
\[
I=(0,L),\quad T=10/\lambda,\quad \delta=T/100,\quad J=(\delta,T),\quad
D=a+k,\quad r=k/D,\quad \alpha=a/D,\quad\beta=b/D,\quad
\gamma=\lambda\beta,\quad\mu=\lambda\alpha,\quad d=b^2/D,\quad Qv=v-\bar v.
\]
The fixed signs are \(a,k,c,\kappa,\lambda,A_0,\theta_*>0\), \(b\ne0\). The displacement is \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\), and the mean strain is \(m(t)=g_*L^{-1}\sin^2(\pi t/T)\). The exact actual even base satisfies
\[
\begin{aligned}
(v_b)_t&=\lambda(m-v_b),& (p_b)_t&=-\mu p_b+\gamma Qy_b,\\
w_b&=m-v_b-\alpha p_b+\beta Qy_b,& E_b&=m'+r(p_b)_t,\\
(cI+d\theta_bQ)(y_b)_t-\kappa(y_b)_{xx}&=-b\theta_bE_b+k\lambda w_b^2,
&\theta_b&=\theta_*+y_b,
\end{aligned} \tag{1}
\]
with \(v_b(0)=p_b(0)=y_b(0)=0\) and \(y_b|_{\partial I}=0\). The genuine active coefficients are
\[
M=c+d\theta_b,\qquad S=\lambda\alpha(br\theta_b-2kw_b),\qquad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{2}
\]
For \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), and \(h\in H\), the odd linearized system is
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\quad P(\cdot,0)=h,\quad Y(0,t)=Y(L,t)=0,
\quad \mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{3}
\]
There is no endpoint condition on \(P\) or an arbitrary input \(h\in X=H^2(I)\cap H\). The \(L^2\) extension is not a claim that every \(H\) vector is a nonlinear admissible state. The user's question about distinct nonlinear states is stronger than injectivity of this linearization; neither conclusion is inferred from the other.

**Conditional framework.** Assume the inherited base exists on \([0,T]\), remains positive, and the strong linear forced problem is well posed with \(Y\in\mathcal E=H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\), \(P\in H^1_tL^2_x\), and the audited estimate. Assume \(0<m_0\le M\le m_1\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\), \(S\in C_tH^1_x\cap H^1_tL^2_x\cap L^2_tH^2_x\), and even parity. A sufficient small-load bound exists in the earlier forward report but is not verified numerically for the experiment; no parameter values are supplied. All results for (3) depend on these hypotheses. The analysis below does not imply global existence, positive temperature, admissibility, or analyticity from the loading alone.

## 2. Coefficients: what the actual equations do and do not imply

| Property | Derivation | Required assumptions | Status |
|---|---|---|---|
| Reflection symmetry | Reflect (1) about \(L/2\); identical data and uniqueness give even \(y_b,p_b,w_b,E_b,M,B,S\). | Whole-class base uniqueness | Conditional proof. |
| Positive mass | \(M=c+d\theta_b\), \(d\ge0\); positivity follows from the base temperature bound. | Base positivity | Conditional proof. |
| \(S(0,x)\) | \(y_b=p_b=v_b=m=0\) at \(0\), so \(S(0,x)=\lambda\alpha br\theta_*\ne0\), sign \(\operatorname{sgn}b\). | Initial base and material signs | Conditional proof. |
| Initial sign interval | \(S\in C_tH^1_x\hookrightarrow C_tC_x\), hence \(|S|\ge s_0>0\) for small positive time. | Base regularity | Conditional proof; overlap with \(J\) unverified. |
| \(M_t\) | \(M_t=d(y_b)_t\in L^2\). | Base strong class | Conditional proof; no endpoint trace inferred. |
| Base spatial boundary | \(y_b=0\), so \(\theta_b=\theta_*\) and \(M=c+d\theta_*\) at \(x=0,L\). | Dirichlet trace | Conditional proof; no \(P\) trace follows. |
| \(S\) sign on all \(J\) | Requires a quantitative base estimate, e.g. (4) below. | Additional explicit smallness | Not established for unspecified data. |
| \(B\) | Terms in (2) belong to \(L^2_{t,x}\); stronger positive-time regularity is available in earlier audits. Its pointwise value at \(t=0\) is not defined by these spaces. | Base strong class | Conditional proof; no unproved initial trace, global \(B_x\) or time analyticity claimed. |
| Time analytic / separable / monotone coefficients | \(m\) is smooth, but (1) is nonlinear and contains nonlocal \(Q\); this alone does not supply those properties for the active base. | Further theorems needed | Not established. |

**A nonzero-load symbolic regime.** Suppose the fixed-point base bounds already established for sufficiently small \(q=|g_*|/L\) have the form \(\|y_b\|_{L^\infty_{t,x}}\le C_yq\), \(\|w_b\|_{L^\infty_{t,x}}\le C_wq\), with data-only constants uniform for the small-load ball. If
\[
0<q<\min\left\{s_*,\frac{|b|r\theta_*}{2(|b|r C_y+2kC_w)}\right\}, \tag{4}
\]
then \(\operatorname{sgn}(b)S\ge\frac12\lambda\alpha |b|r\theta_*\) throughout \([0,T]\times I\). Indeed the perturbation of \(br\theta_*\) is bounded by \((|b|rC_y+2kC_w)q\). The interval in (4) is nonempty for finite constants and nonzero \(b\); it retains a nonzero prescribed sinusoidal load. It is a **sufficient symbolic regime**, not a verified statement about the unspecified numerical experiment. It is not a theorem that sign-definite coupling alone identifies all signed inputs.

Write \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(k_n=\mathcal T\phi_n\). The audited actual expansion is
\[
k_n=\frac{a_J}{q_n}+\rho_n,\quad
 a_J(t)=2A_0\sqrt{2/L}e^{-\mu t}S(t,0),\quad
\|\rho_n\|_{L^2(J)}\le C_\eta q_n^{-3/2+\eta},\quad 0<\eta<\tfrac12. \tag{5}
\]
Under (4), \(a_J\ne0\); hence for \(q_n^{1/2-\eta}\ge 2C_\eta/\|a_J\|\),
\[
\|\mathcal T\phi_n\|\ge \frac{\|a_J\|}{2q_n}>0. \tag{6}
\]
Thus each sufficiently high individual sine direction is separated from zero in this symbolic parameter regime. This is a conditional, one-dimensional result, **not** separation of arbitrary superpositions, and the threshold is not evaluated numerically. All \(\phi_n\in X\); scaling them to fit a local nonlinear admissible neighborhood requires the separately verified forward-admissibility condition and does not make (6) a nonlinear theorem.

## 3. Three direct proof attempts on the actual equations

Assume \(\mathcal Th=0\); then the established trace gives \(Y_x(0,t)=0\) a.e. on \(J\), and oddness gives \(Y_x(L,t)=Y_x(0,t)\). The Dirichlet traces also vanish. These boundary equalities alone do not erase \(SP\).

### Attempt A: scalar boundary unique continuation and Carleman

Divide the actual PDE by \(M\):
\[
Y_t-\frac{\kappa}{M}Y_{xx}-\frac BM Y=\frac SM P. \tag{7}
\]
A homogeneous scalar boundary-unique-continuation theorem would require a right side controlled by \(Y\) in its hypotheses. Here the forcing contains an unknown \(P\), and the exact identity below includes the free \(h\). A scalar Carleman estimate with \(F=SP/M\) would at most give an estimate with a weighted \(P\)-term on the right. Treating \(P\) as a scalar potential times \(Y\) is invalid. Even if the Volterra integral of \(Y\) can be absorbed, the term \(e^{-\mu t}S h\) remains and an estimate must exploit its structure or obtain a separate observation/snapshot. Existing cited centered-weight ODE estimates retain a center-time term; nothing here controls that unknown term from one flux.

Under the additional *hypothesis* that a boundary-to-interior lemma yields \(Y=0\) on all of \((0,T)\times I\), initial nonvanishing of \(S\) does force \(h=0\), because \(P=e^{-\mu t}h\) and \(S e^{-\mu t}h=0\). This is a valid conditional chain, not a proof that the boundary lemma is true. The weakest additional assumption cannot be identified uniquely: boundary-to-interior continuation is sufficient, but may not be necessary if another method separates the kernel.

### Attempt B: exact elimination of memory and early-history recovery

The exact equation is
\[
MY_t-\kappa Y_{xx}=BY+e^{-\mu t}S h+
\gamma S(t)\int_0^t e^{-\mu(t-r)}Y(r)dr. \tag{8}
\]
All terms are in \(L^2_{t,x}\) under the stated strong class. At \(\delta\),
\[
P(t)=e^{-\mu(t-\delta)}P(\delta)+\gamma\int_\delta^t e^{-\mu(t-r)}Y(r)dr,
\quad P(\delta)=e^{-\mu\delta}h+\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr. \tag{9}
\]
The first integral in (8) is a causal Volterra term; the pre-delay term in (9) is an unknown reachable state, not zero and not separately observed. Inverting a forward Volterra equation for a *known interior field* does not invert the map from one boundary flux. Evaluation of (8) at the boundary is unjustified: \(Y_t,Y_{xx},B\) and \(h\in L^2\) need not have boundary traces. Therefore neither boundary values nor the initial nonzero constant \(S(0)\) directly yield \(h\).

For completeness, full interior \(Y\) on a sufficiently short interval \((0,\varepsilon)\) determines \(h\) by the established weighted formula, because \(|S|\ge s_0\) there. This is an **additional observation**, not a delayed-boundary result. Positivity of \(S\) near zero alone cannot be transferred to \(J\).

### Attempt C: eliminating temperature, time continuation, and backward uniqueness

Because \(\gamma\ne0\), formally \(Y=(P_t+\mu P)/\gamma\). Under additional regularity this yields
\[
M(P_{tt}+\mu P_t)-\kappa(P_{txx}+\mu P_{xx})
=B(P_t+\mu P)+\gamma SP. \tag{10}
\]
It is a mixed parabolic–ODE evolution with \(P(0)=h\), \(P_t(0)=-\mu h\), and formal boundary conditions on \(P_t+\mu P\), not a scalar heat equation with standard data. For general \(h\in H\), the second time derivative, \(P_{xx}\), and their boundary traces in (10) are not established; the formula is only distributional/formal and supplies no independent boundary equation for \(h\).

Time analyticity of an output would allow zero on \(J\) to extend to earlier times; the active time-dependent coefficients and coupled evolution have not been proved analytic or quasianalytic. Smooth sinusoidal forcing is insufficient. Even an independently proved analyticity property would still require a proof that full-time zero output forces \(h=0\). Parabolic backward uniqueness normally concerns a **known full interior state**, not one Cauchy trace of an inhomogeneous equation; no such inference is justified here. The actual reflection merely identifies the other endpoint derivative, it does not create an independent odd-channel signal.

## 4. Pre-delay state map: what is actually retained

Define \(U_\delta h=Y(\delta)\), \(D_\delta h=P(\delta)\). The strong trace theorem gives \(U_\delta:H\to V\) bounded and compact as a map into \(H\). The exact ODE gives
\[
D_\delta=e^{-\mu\delta}I+K_\delta,\qquad
K_\delta h=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y[h](r)dr. \tag{11}
\]
The Bochner integral is bounded into \(H^2\cap H^1_0\), so \(K_\delta:H\to H\) is compact. Thus \(D_\delta\) is Fredholm of index zero, has finite-dimensional kernel, and is not compact on the infinite-dimensional \(H\). The joint map \(h\mapsto(U_\delta h,D_\delta h)\) is a compact perturbation of \(h\mapsto(0,e^{-\mu\delta}h)\), so its kernel is finite-dimensional and its range in \(H\times H\) is closed. Neither fact proves this kernel zero or gives boundary observability of the reachable graph.

A concrete **additional** sufficient condition is obtained from \(Y(0)=0\) and \(\|Y_t\|_{L^2(0,\delta;H)}\le C_E\|h\|\):
\[
\|K_\delta\|\le\frac23|\gamma|C_E\delta^{3/2},\qquad
\frac23|\gamma|C_E\delta^{3/2}<e^{-\mu\delta}\ \Longrightarrow\ D_\delta^{-1}\text{ exists}. \tag{12}
\]
The proof is \(\|Y(t)\|\le\sqrt t\|Y_t\|_{L^2(0,\delta;H)}\), followed by the Neumann series. This is a sufficient criterion, not known for the actual parameters. It says a hypothetical full \(P(\delta)\) snapshot would identify \(h\); the measured scalar flux does not supply that snapshot. The exact factorization is \(\mathcal T=\mathcal O_\delta\mathcal S_\delta\) on the actual reachable graph, not a claim that \(\mathcal O_\delta\) is Fredholm. No conclusion says the delay fundamentally destroys information; whether it changes injectivity is open.

## 5. Actual modal equations and a stronger high-frequency theorem

For \(Y=\sum y_n\phi_n\), \(P=\sum p_n\phi_n\), define, for a.e. \(t\),
\[
M_{mn}=(M\phi_n,\phi_m),\quad B_{mn}=(B\phi_n,\phi_m),\quad S_{mn}=(S\phi_n,\phi_m).
\]
The weak exact system is
\[
(MY_t,\phi_m)+\kappa q_m^2y_m=(BY+SP,\phi_m),\qquad
p_m'+\mu p_m=\gamma y_m,\quad y_m(0)=0,\ p_m(0)=h_m. \tag{13}
\]
When expanded, the first term contains \(\sum_nM_{mn}y'_n\); multiplication by nonconstant even \(M,B,S\) couples odd sine modes. Equation (13) is a weak identity; infinite-matrix rearrangements require their own convergence proof. The actual boundary trace is defined through \(L^2_tH^2_x\), not by arbitrary termwise differentiation of an \(L^2\) sine series. There is no established common generator, independent exponential family, triangular matrix, or mode-by-mode decoupling. The exact infinite synthesis \(\mathcal Th=\sum h_nk_n\) converges in \(Z\) by the Hilbert–Schmidt bound; zero synthesis does not imply each coefficient is zero.

**Theorem 1 (actual remainder tail and approximation numbers).** Under the inherited expansion (5), for every \(0<\eta<1/2\), with \(P_N\) the odd sine projector,
\[
\|\mathcal R(I-P_N)\|_{H\to Z}\le C_\eta' N^{-1+\eta},\qquad
s_{N+2}(\mathcal T)\le C_\eta' N^{-1+\eta}. \tag{14}
\]
Here \(s_j\) are approximation numbers/singular values, ordered nonincreasingly with zeros if finite rank. **Proof.** By Cauchy–Schwarz,
\[
\|\mathcal R(I-P_N)h\|_Z\le\|h\|_H\Big(\sum_{n>N}\|\rho_n\|_Z^2\Big)^{1/2}
\le C_\eta'\|h\|_H N^{-1+\eta}.
\]
The rank of \(a_J\Lambda+\mathcal RP_N\) is at most \(N+1\), and its approximation error is the first bound, proving the second. On \(H_0\), \(\mathcal T=\mathcal R\), and the same tail bound holds. This strengthens the unseparated \(O(N^{-1/2})\) tail only **after retaining the rank-one lift**. It is an upper bound on singular values, not a lower bound or an injectivity result.

The near-collinearity also blocks a routine diagonal perturbation. For neighboring modes choose
\[
z_n=\phi_n-\frac{q_{n+1}}{q_n}\phi_{n+1},\quad \Lambda z_n=0,\quad
\|\mathcal Tz_n\|\le C_\eta q_n^{-3/2+\eta}. \tag{15}
\]
After normalizing, \(z_n\rightharpoonup0\) and \(\|z_n\|=1\). These are actual approximate invisible states, never an exact kernel. A uniform diagonal lower bound on high-mode blocks would contradict (15); any perturbation argument must account quantitatively for this deterioration. The finite-section least singular value has an upper bound of this order, not a positive lower bound.

## 6. Rigorous structural obstruction and exact counterexample search

**Theorem 2 (finite-data/absolute-perturbation obstruction).** Fix any \(N\), and let \(v_N\) be the normalized vector from (15) with \(n=N+1\). Define the rank-one modified operator on the *same Hilbert spaces*
\[
\widetilde{\mathcal T}_N h=\mathcal Th-\mathcal T v_N\,(h,v_N)_H. \tag{16}
\]
Then \(v_N\in H_0\cap H^2\), \(v_N\ne0\), \(\widetilde{\mathcal T}_Nv_N=0\), and \(\widetilde{\mathcal T}_N\phi_j=\mathcal T\phi_j\) for every \(j\le N\). Furthermore
\[
\|\widetilde{\mathcal T}_N-\mathcal T\|_{H\to Z}=\|\mathcal T v_N\|_Z
\le C_\eta N^{-3/2+\eta}\to0. \tag{17}
\]
For each fixed \(N\), only columns \(N+1,N+2\) change; thus (5)'s leading profile and asymptotic exponent also hold for \(\widetilde{\mathcal T}_N\), with a possibly different constant. **Proof.** Orthogonality of sine modes gives \((\phi_j,v_N)=0\) for \(j\le N\), \((v_N,v_N)=1\), and (15) gives (17). The rank-one norm is exactly \(\|\mathcal T v_N\|\).

This is an **abstract comparison operator**, not a realization of (1), not a modification of the experiment, and not a physical counterexample. It rigorously shows why any proposed proof based solely on a fixed finite numerical matrix plus an absolute operator-norm error, or solely on the high-frequency upper asymptotic, cannot establish actual injectivity. The constructed exact kernel belongs to the abstract \(\widetilde{\mathcal T}_N\), never to the actual \(\mathcal T\). It does not show that actual material coefficients can generate this rank-one perturbation.

**Physical counterexample attempts.** (i) Reflection maps an odd \(h\) to \(-h\), but the odd output also changes sign; equality requires \(\mathcal Th=0\) already. (ii) A single separable pair \(Y=\eta(t)\phi_n\), \(P=p(t)\phi_n\) has \(p'+\mu p=\gamma\eta\), \(\eta(0)=0,p(0)=1\), and requires the pointwise active-coefficient constraint
\[
M(t,x)\eta'(t)+\kappa q_n^2\eta(t)=B(t,x)\eta(t)+S(t,x)p(t) \tag{18}
\]
where \(\phi_n\ne0\). The active spatially variable coefficients do not automatically supply this scalar identity. Nevertheless, under (4), one can exclude this entire separable-kernel ansatz rigorously: zero flux implies \(\eta=0\) on \(J\), hence \(\eta\prime=0\) there and (18) forces \(p=0\) there because \(S\) is bounded away from zero. By Fubini choose a fixed \(x\) with \(\phi_n(x)\ne0\), \(M(t,x)\ge m_0\) a.e., and \(B(\cdot,x)\in L^2(0,T)\). At this \(x\), (18) and \(p\prime+\mu p=\gamma\eta\) form a homogeneous linear two-dimensional ODE with integrable coefficients; backward uniqueness of this finite-dimensional ODE makes \((\eta,p)\equiv(0,0)\), contradicting \(p(0)=1\). This excludes only exactly separable single-mode solutions in the symbolic regime, not general superpositions or an actual kernel. Without (4) no such conclusion is asserted. (iii) A finite or infinite modal cancellation is precisely \(\sum h_nk_n=0\); neither (5) nor finite Gram matrices give a solution. (iv) The pre-delay map (11) could have a finite-dimensional kernel, but no nonzero joint delayed state kernel was found. (v) The adjoint construction would require an explicit \(h\perp\operatorname{ran}\mathcal T^*\), not merely approximate orthogonality; none is known. There is no exact physical invisible initial state or pair of nonlinear admissible states in this report.

## 7. A constructive infinite-moment route with a quantitative threshold

This section uses the actual \(k_n\) and (14) rather than merely restating adjoint density. Define the augmented synthesis \(K_N:\mathbb R^{N+1}\to Z\) by
\[
K_N(c_1,\dots,c_N,c_*)=\sum_{j=1}^Nc_jk_j+c_*a_J,\qquad G_N=K_N^*K_N. \tag{19}
\]
Suppose for all sufficiently large \(N\), \(G_N\) is invertible. For fixed \(n\le N\), define the **actual** control
\[
f_{n,N}=K_NG_N^{-1}e_n\in L^2(J), \tag{20}
\]
where \(e_n\) has 1 in the \(n\)-th column and zero in all other \(N+1\) slots. Then
\[
(k_j,f_{n,N})=\delta_{jn}\ (j\le N),\qquad (a_J,f_{n,N})=0,\qquad
\|f_{n,N}\|_Z^2=(G_N^{-1})_{nn}. \tag{21}
\]
Because \(k_j=a_J/q_j+\rho_j\), the residual tail satisfies
\[
\|(I-P_N)\mathcal T^* f_{n,N}\|_H
=\left(\sum_{j>N}|(\rho_j,f_{n,N})|^2\right)^{1/2}
\le C_\eta' N^{-1+\eta}\sqrt{(G_N^{-1})_{nn}}. \tag{22}
\]

**Theorem 3 (sufficient moment-control criterion).** Under the actual hypotheses and expansion (5), if for every fixed \(n\) there is a sequence of integers \(N\to\infty\) such that \(G_N\) is invertible and
\[
C_\eta' N^{-1+\eta}\sqrt{(G_N^{-1})_{nn}}\longrightarrow0, \tag{23}
\]
then \(\mathcal T:H\to Z\) is injective. **Proof.** The first \(N\) coordinates of \(\mathcal T^*f_{n,N}\) equal those of \(\phi_n\); (22) and (23) imply \(\mathcal T^*f_{n,N}\to\phi_n\) in \(H\). Hence the actual adjoint range has closure containing every basis vector, and (3) is injective by duality. Equivalently, if \(\mathcal Th=0\), pairing with the controls and passing to the limit yields every \(h_n=0\). All controls are genuine \(L^2(J)\) functions, not delta distributions.

This is a **sufficient** quantitative theorem, not verified for the active experiment, not claimed minimal, and not a parameter-regime proof. \(G_N\) may be singular, e.g. if \(a_J=0\) or lies in the span of the columns; the criterion can fail even when \(\mathcal T\) is injective. The inverse Gram norm may grow faster than the displayed polynomial threshold because of near-collinearity. No calculated finite Gram, numerical rank or constructive sequence satisfying (23) is claimed. Certified Gram lower bounds and a certified expansion constant would be required; finite computation alone cannot establish the limiting condition. Proving or refuting (23), or developing a less restrictive actual moment construction, is a concrete route. If it holds, both the restricted-kernel and exact-range conditions follow automatically; without it neither is decided.

For the alternative exact-range strategy, with \(A=\mathcal T|_{H_0}\), \(u=q_1\phi_1\), \(b_*=\mathcal Tu\), the audited ratio is
\[
\sup_{f\in Z}\frac{|(b_*,f)|}{\|A^*f\|}=\infty\iff b_*\notin\operatorname{ran}A. \tag{24}
\]
No actual sequence with divergent ratio was constructed, and no exact \(v\in H_0\) with \(Av=b_*\) was found. A bound for the ratio of a finite number of discrete controls cannot settle (24).

## 8. Computation: explicit nonperformance and reproducibility requirements

The repository provides no numerical values for \(a,k,b,c,\kappa,\lambda,L,A_0,\theta_*,g_*\), no verified loading-smallness constants, and no computed active-base coefficient data. Consequently the requested two independent numerical implementations, singular-value tables, convergence plots, and numerical range-ratio investigation were **not performed**. Inventing a parameter set or substituting an equilibrium would violate the fixed-experiment requirement. No untested solver code or simulated data are supplied, and no numerical result is implied.

Once actual inputs are available, a reproducible protocol is: solve (1) first with compatible initial and boundary data, preserving the nonlocal \(Q\) term and nonzero sinusoid; independently solve (3) using sine Galerkin (matrix \(M_N(t)\dot y+\kappa Q_N^2y=B_Ny+S_Np\), \(\dot p=-\mu p+\gamma y\)) and an implicit finite-difference/finite-element solver (pointwise memory ODE and the same coefficients). Compute the left flux in each discretization, sample with time quadrature on the **actual** \(J\), and apply consistent quadrature weights before SVD. Refine base grid, linearized mesh, time step and ODE/linear-solver tolerance independently; compare both implementations and verify parity. For \(H_0\), use an orthonormal basis for the discrete nullspace of \((1/q_1,\ldots,1/q_N)\); compare the lifted direction \(u\), the restricted singular values, and regularized approximations to (24). Also compare \(q_n k_n\) to \(a_J\) and track weak/strong convergence of candidate right singular vectors after proper interpolation. Explicitly report coefficient, spatial, temporal, trace and quadrature errors. This protocol is **not** an executed implementation or numerical evidence; validated tails and an infinite limiting argument remain essential.

## 9. Primary-source comparison

Only theorem passages and the indicated proofs were inspected. The search is targeted, not exhaustive; no priority or novelty follows. Sources not fully transferred are not asserted to solve (3).

| Primary source | Exact theorem used | Hypotheses | Applicability | Missing step |
|---|---|---|---|---|
| Halanay–Pandolfi, [arXiv:1404.2745](https://arxiv.org/html/1404.2745) | Theorem 2, scalar approximate controllability | \(C^1\) temporal convolution on Laplacian; admissible boundary control | Different scalar Coleman–Gurtin state/control map | Unknown initial nondiffusive memory and variable lower-order active coupling. |
| Jha–George, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221) | Theorem 3.10 and Lemma 3.13 | Moving interior control; short-time closure; assumed adjoint UC and compactness–uniqueness | Coupled memory techniques are relevant in form | Their assumptions and geometry do not yield one delayed endpoint separation. |
| Apraiz–Lecaros–Zamorano, [arXiv:2610.26157](https://arxiv.org/html/2610.26157) | Lemma 2.2 proof, Theorem 2.3 | Centered weights and interior observation; weighted center snapshot | Shows why Volterra absorption can retain an unknown snapshot | Our single flux does not provide that snapshot or their interior data. |
| Kian–Sambou–Soccorsi, [arXiv:1612.07942](https://arxiv.org/html/1612.07942) | Theorem 1.2 and §1.1 | Scalar heat; separated \(\sigma(t)\beta(x)\); regularity, nondegeneracy, partial waveguide data | Illustrates structured-source recovery and general-source obstruction | \(S(t,x)h\) and coupled feedback do not satisfy their separated-source setup. |
| [*Boundary controllability for a coupled system of degenerate/singular parabolic equations*, arXiv:2104.00610](https://arxiv.org/html/2104.00610) | Theorem 1.1 exponential biorthogonality | Sector, gap, summability; autonomous diffusive systems | Useful moment template | Actual \(k_n\) are not proved to be an exponential family or to meet gaps. |
| Olive, [arXiv:2609.09982](https://arxiv.org/html/2609.09982) | Theorem 1.1 and appendix proof | Autonomous semigroup, spectral projections, complete adjoint root vectors | Root-vector strategy for other parabolic systems | Time-dependent active PDE–ODE and nondiffusive component lack its established assumptions. |
| Clason, [arXiv:2001.00617](https://arxiv.org/html/2001.00617) | Theorem 3.10 and proof | Compact Hilbert operator, singular system | Exact Picard range test applies abstractly to actual \(A\) | Actual singular data and convergence of the Picard sum are unknown. |

The original papers' cited dependencies were not independently verified. No paper in the inspected set proves or disproves the fixed active problem.

## 10. Final scientific decision

1. **Actual boundary-only injectivity:** unresolved under stated hypotheses; no exact counterexample.
2. **Shortest injectivity proof / weakest hypotheses:** unavailable. The sufficient condition (23) gives a concrete possible proof, not a verified weakest condition. A coupled continuation theorem is another possible route, not shown necessary.
3. **Exact invisible initial state:** none constructed for the actual experiment. The vector in (16) is invisible only for the explicitly labeled abstract comparison operator.
4. **Parameter dependence:** (4) is a nontrivial nonzero-load symbolic regime proving fixed sign and high single-mode detectability; it does not prove or disprove full injectivity. Actual numerical parameters are not known.
5. **Delay:** it causes an unobserved reachable state and is not shown to destroy injectivity; it also cannot yet be shown to be only a stability issue.
6. **One endpoint:** it carries an infinite-dimensional time signal and might suffice, but sufficiency is unproved. The second endpoint is redundant only in the odd channel.
7. **Stability:** no bounded inverse in the infinite-dimensional \(L^2\) norm; (14) and (15) quantify stronger high-mode ill-conditioning. A qualitative modulus modulo the unknown kernel on bounded \(H^2\) sets survives; a full modulus requires independent restricted injectivity. No explicit reconstruction rate is proved.
8. **Research significance:** a correct actual-system injectivity or exact counterexample could be mathematically substantive; publication suitability and priority cannot be judged without a fuller literature review and verification. This report is not a manuscript.
9. **Continuum principle:** none demonstrated. This is an inverse-identification question for the fixed existing constitutive model.
10. **Single next theorem:** prove a quantitative actual-system version of (23)—including a strictly positive augmented finite Gram and a certified inverse-Gram growth estimate relative to the \(N^{-1+\eta}\) tail—or find an explicit fixed-experiment \(h\ne0\) with zero trace. The proposed criterion is sufficient, not claimed necessary; a failure of (23) is not a counterexample.

**Decision: STRUCTURAL OBSTRUCTION IDENTIFIED**, precisely in the scoped sense of Theorem 2, together with the actual high-frequency Theorem 1 and conditional moment Theorem 3. The central physical identification question remains open; the required numerical diagnostics are outstanding pending actual parameter and base data.
