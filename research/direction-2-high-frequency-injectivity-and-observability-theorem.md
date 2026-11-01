# High-frequency injectivity and observability: an active-system audit

**1 November 2026 — decision: REFORMULATE.** This report obtains an algebraic high-frequency **upper bound for the actual nonautonomous operator**, an exact finite-dimensional Schur-complement test for the **delayed-memory map**, and a certified conditional infinite-dimensional observability theorem. It does **not** prove the needed lower singular-value estimates, the kernel of the delayed observation, a coupled Carleman inequality, or an exact invisible profile. No novelty or publication priority is claimed. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This document is one agent's analysis, not independent human certification. Direction 1 remains rejected as a foundational continuum theory; Direction 2 is an observation/state problem, not a new continuum theory.

The reports on exact injectivity, coupled boundary observability, active-base regularity, delayed-state adjoint, reachable graph, compact quotient, and rigorous boundary positivity were inspected, as were the forward-existence and topology reports. Their hypotheses are carried forward, not replaced by a new experiment.

## 1. Fixed model, inherited bounds, and notation

Set \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), and \(X=H^2(I)\cap H\). The fixed nonzero loading is \(g_*\sin^2(\pi t/T)\). The sufficient small-load assumption \(0<|g_*|/L<s_*\) remains **numerically unverified**; all actual-system statements below are conditional on the inherited existence/regularity hypotheses, not a claim that a supplied numerical experiment satisfies them. All positive parameters and \(b\ne0\) remain as prescribed. With \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(d=b^2/D\), \(Qv=v-\bar v\), the actual base produces
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{1}
\]
The odd perturbation is
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(0,\cdot)=0,\ P(0,\cdot)=h,\ Y(t,0)=Y(t,L)=0,\quad
\mathcal Th=2A_0\kappa Y_x(\cdot,0)|_J. \tag{2}
\]
There is no spatial Dirichlet condition on \(P\). The physical class \(X\) may have nonzero endpoint values; \(H\) is the linear analytic extension. Inherited estimates are
\[
0<m_0\le M\le m_1,\quad M,S\in L^\infty,\quad M_x\in L^\infty_tL^2_x,\quad B\in L^2_{t,x},\tag{3}
\]
\[
\|Y\|_{H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)}+\|P\|_{H^1_tL^2_x}\le C_E\|h\|_2. \tag{4}
\]
On positive-time strips, \(B\in L^\infty_tL^2_x\cap L^2_tL^\infty_x\cap L^6_{t,x}\); no global \(L^\infty_tL^2_x\) bound on \(B\) is assumed. The base formula \(w_b=m-v_b-\alpha p_b+\beta Qy_b\), the ODE representation of \(p_b\), and \(y_b\in C_tH^1_0\) imply \(w_b\in L^\infty_tH^1_x\). Hence, in addition to (3),
\[
S\in L^\infty(0,T;H^1(I)),\qquad C:=S/M\in L^\infty(0,T;H^1(I)),\quad A:=\kappa/M,\quad A_x\in L^\infty_tL^2_x. \tag{5}
\]
These are multiplier bounds, not \(W^{1,\infty}\) regularity of \(S\) at the initial corner. The constants below depend on the actual fixed coefficients and their displayed norms, material units, \(L,T\) and the ellipticity lower bound. They are not evaluated numerically.

## 2. Actual high-frequency upper estimates

Let \(\phi_n=\sqrt{2/L}\sin(2\pi nx/L)\), \(q_n=2\pi n/L\), \(P_N\) be the orthogonal projection onto the first \(N\) odd Dirichlet sines, and \(k_n=\mathcal T\phi_n\). Let \(V'\) be the dual of \(V\), with norm defined using \(\|v_x\|_2\). For odd \(h\), \(\|h\|_{V'}^2=\sum_{n\ge1}|h_n|^2/q_n^2\).

### Theorem A — quantitative active-system upper bound

For every \(0<\eta<1/2\), under (3)–(5), there is a finite \(C_\eta\), depending only on the indicated coefficient/forward bounds, such that for all \(h\in H\)
\[
\boxed{\|\mathcal Th\|_{L^2(J)}\le C_\eta\|h\|_{V'}^{1/2-\eta}\|h\|_2^{1/2+\eta},\qquad
\|k_n\|_{L^2(J)}\le C_\eta q_n^{-1/2+\eta},\quad
 e_N\le C_\eta q_{N+1}^{-1/2+\eta}.} \tag{6}
\]
The bound applies equally on \((0,T)\), so the fixed delay need not be used to prove it. It retains the time-varying principal coefficient, the rough \(B\), and the memory feedback. It is an **upper** estimate, not an asymptotic equivalent, lower bound, or injectivity theorem.

**Proof.** Multiplication by any \(a\in H^1(I)\) sends \(H^1_0(I)\) to itself with norm \(\le C_L\|a\|_{H^1}\); by duality it acts on \(V'\) with the same type of bound. All base coefficients are even, so the odd test space is preserved. Divide the heat equation by \(M\), test by \(Y\), and integrate by parts:
\[
\tfrac12\frac{d}{dt}\|Y\|_2^2+\int A|Y_x|^2
=-\int A_xY_xY+\int (B/M)Y^2+\langle P,CY\rangle_{V',V}. \tag{7}
\]
The actual positive \(A\) is bounded below. The first term is controlled by
\(C\|A_x\|_2\|Y_x\|_2^{3/2}\|Y\|_2^{1/2}\), and the potential by \(C\|B(t)\|_2\|Y\|_2^{3/2}\|Y_x\|_2^{1/2}\), using the one-dimensional Gagliardo–Nirenberg inequalities and Poincaré. Young's inequality bounds these by an absorbable multiple of \(\|Y_x\|_2^2\) plus
\(C(1+\|A_x\|_2^4+\|B(t)\|_2^{4/3})\|Y\|_2^2\). The last term is at most \(C\|P\|_{V'}\|Y_x\|_2\) and is similarly absorbed. The coefficient of \(\|Y\|_2^2\) is integrable: **only** \(B\in L^2_{t,x}\) is needed.

The exact ODE in \(V'\) gives
\(\|P(t)\|_{V'}\le e^{-\mu t}\|h\|_{V'}+|\gamma|\int_0^t e^{-\mu(t-r)}\|Y(r)\|_{V'}dr\).
Apply a coupled Gronwall estimate, or differentiate \(\|P\|_{V'}^2\) using the Hilbert \(V'\) inner product, to get
\[
\|Y\|_{L^\infty_tL^2_x}+\|Y\|_{L^2_tH^1_x}+\|P\|_{L^\infty_tV'}\le C\|h\|_{V'}. \tag{8}
\]
For \(h\in H\), all manipulations can be made with the strong solution: \(P\in L^2\), \(CY\in V\), and the spatial integration by parts is valid for a.e. time; standard approximation justifies the energy chain rule. No derivative of \(M\) in time is used.

Choose \(s=3/2+\eta\in(3/2,2)\). Interpolation of (8) with (4) gives
\[
\|Y\|_{L^2_tH^s_x}\le C_\eta\|h\|_{V'}^{2-s}\|h\|_2^{s-1}.
\]
The one-dimensional trace \(v\mapsto v_x(0)\) is continuous on \(H^s(I)\), yielding the first inequality in (6). Since \(\|\phi_n\|_{V'}=q_n^{-1}\) and \(\|(I-P_N)h\|_{V'}\le q_{N+1}^{-1}\|h\|_2\), the remaining inequalities follow. □

**What this tells us.** The delayed observation of any high-frequency sine, and every unit-norm superposition in the high-frequency tail, tends to zero at at least the displayed algebraic rate. It does not say two modes have distinguishable outputs, nor that cancellation occurs exactly. The bulk weak-energy estimate also gives \(\|Y_n\|_{L^2_tH^1}=O(n^{-1})\), whereas (4) only gives a uniform \(L^2_tH^2\) bound. A boundary trace loses spatial regularity; the estimate above does not identify a boundary layer or prove its thickness. The heat diffusion heuristic suggests \(q_n^{-1}\) spatial and \(q_n^{-2}\) temporal scales, but for variable coefficients and distributed ODE memory these are **not derived asymptotics**. The endpoint values of \(\phi_n\) vanish, yet their normal derivatives grow like \(q_n\); neither \(S(0)\), \(M(0)\), nor a spatial average is proved to control the actual leading delayed response. We obtain no lower bound, temporal exponential/nonharmonic family, or true-system remainder relative to a proposed leading term. Establishing one would require a boundary-parametrix or equivalent estimate uniform in \(n\), including mode coupling, the rough \(B\), memory feedback, and the positive-time boundary traces. Theorem A is the available rigorous remainder-free upper estimate, not a frozen half-line substitute.

## 3. Finite sections, optimal tails, and an actual conditional theorem

Define \(\sigma_N=\inf_{v\in P_NH,\|v\|=1}\|\mathcal Tv\|\) and \(e_N=\|\mathcal T(I-P_N)\|\). If \(\sigma_N>0\), then for \(r_N(h)=\|(I-P_N)h\|\),
\[
\|h\|_2\le \frac{\|\mathcal Th\|}{\sigma_N}+\left(1+\frac{e_N}{\sigma_N}\right)r_N(h). \tag{9}
\]
Indeed, \(\sigma_N\|P_Nh\|\le\|\mathcal Th\|+e_Nr_N(h)\), followed by the triangle inequality. For \(h\in H^1\), integration by parts gives \(|h_n|\le C_Ln^{-1}\|h\|_{H^1}\), including the endpoint contribution, so \(r_N(h)\le C_LN^{-1/2}\|h\|_{H^1}\).

More generally, for **every** \(s>1/2\),
\[
r_N(h)\le C_{s,L}N^{-1/2}\|h\|_{H^s(I)},\qquad h\in H^s(I)\cap H. \tag{10}
\]
For \(1/2<s<1\), subtract the linear odd endpoint interpolant \(\ell_h(x)=h(0)(1-2x/L)\). Its coefficients are \(O(h(0)/n)\). The remainder has zero endpoint traces, belongs to \(H^s_0(I)\), and the Dirichlet sine spectral norm gives a tail \(O(N^{-s}\|h-\ell_h\|_{H^s})\). For \(s\ge1\), use the \(H^1\) integration-by-parts estimate. Trace continuity controls \(|h(0)|\). This \(N^{-1/2}\) exponent is **optimal on the unrestricted class**, even for smooth \(h\): for \(h(x)=1-2x/L\), its odd sine coefficients are nonzero constants times \(1/n\), so the tail is comparable to \(N^{-1/2}\). If the endpoint values are known to vanish, stronger rates hold in compatible Dirichlet spectral spaces; for \(1/2<s\le1\), \(h\in H^s\) with zero trace gives \(r_N\le C N^{-s}\|h\|_{H^s}\). At higher \(s\), further boundary compatibility/critical-index qualifications are required; unrestricted \(H^s\) alone does not improve (10).

**Conditional observability theorem.** Let \(s>1/2\), \(R>0\), and suppose certified \(\sigma_{N_j}\ge a_j>0\), \(e_{N_j}\le b_j\), along \(N_j\to\infty\), with
\[
C_{s,L}R\,(1+b_j/a_j)N_j^{-1/2}\longrightarrow0. \tag{11}
\]
Then on \(\{h\in H^s\cap H:\|h\|_{H^s}\le R\}\),
\[
\|h\|_2\le \omega_R(\|\mathcal Th\|),\quad
\omega_R(\varepsilon)=\inf_j\left[\varepsilon/a_j+C_{s,L}R(1+b_j/a_j)N_j^{-1/2}\right]\to0. \tag{12}
\]
The limit follows by first selecting a sufficiently large fixed \(j\), then taking \(\varepsilon\downarrow0\). Consequently \(\mathcal T\) is injective on \(H^s\cap H\), by scaling any input into a fixed ball. This proves a **genuine conditional infinite-dimensional separation result**, but (11) has not been verified for the actual system. The bound (6) can provide \(b_j=C_\eta q_{N_j+1}^{-1/2+\eta}\). The missing result is a rigorous lower estimate for the *entire* smallest singular value, not individual column norms. In particular \(\sigma_N\le\|k_N\|\le C_\eta q_N^{-1/2+\eta}\), an **upper**, not lower, bound. Positivity of every \(\sigma_N\) alone does not establish (11); no actual \(N_j\) is known. If available validated numbers \(a_j,b_j\) are substituted, (12) is an explicit computable upper modulus; without them it is a theorem with unverified premises, not a computed rate.

A principal-coefficient-adapted basis would depend on time because \(M\) does; it also couples the memory variable and changes the projection-tail problem. A fixed weighted Sturm–Liouville basis may improve constants for a frozen time, but no proven improvement to \(e_N/\sigma_N\) follows. Singular-vector bases diagonalize a compact operator abstractly, but require prior knowledge of its unknown nullspace; ordering only nonzero singular vectors cannot rule out invisible components. A truly effective basis would have to supply a certified smooth-class tail *and* an independent singular-value lower bound.

## 4. Two-time ODE weights and snapshot control attempt

For \(a<t_c<b\) in \(J\), with \(W_s=e^{s\psi(x)-sa_w(t-t_c)^2}\), the exact two-sided representation is
\[
P(t)=e^{-\mu(t-t_c)}P(t_c)+\gamma\int_{t_c}^t e^{-\mu(t-r)}Y(r)dr. \tag{13}
\]
The centered Schur estimate, valid on both sides, gives
\[
\|W_sP\|_2^2\le C s^{-1}|\gamma|^2\|W_sY\|_2^2+C s^{-1/2}\|e^{s\psi}P(t_c)\|_2^2. \tag{14}
\]
Here constants depend on the interval, \(\mu\), \(a_w\), not \(s\). Two observations centered at \(t_1<t_2\) do eliminate the snapshot algebraically in their **difference**:
\[
e^{\mu t_2}P(t_2)-e^{\mu t_1}P(t_1)=\gamma\int_{t_1}^{t_2}e^{\mu r}Y(r)dr. \tag{15}
\]
But this eliminates the common unknown rather than estimating it. Taking \(Y=0\), \(P(t)=e^{-\mu t}p\) for the ODE alone makes every such difference zero while an arbitrary snapshot remains. This is an ODE obstruction illustration, **not** a solution of the coupled physical PDE. Two weights therefore do not automatically give coercivity; the parabolic coupling must independently measure the missing homogeneous ODE component.

The exact reachable snapshot equation is
\[
P(t_c)=e^{-\mu t_c}h+\gamma\int_0^{t_c}e^{-\mu(t_c-r)}Y(r)dr. \tag{16}
\]
Replacing the snapshot by (16) introduces an unknown \(h\); the compact perturbation of the identity derived below does not control \(h\) by the observed flux. Weighting both equations simultaneously leads to the same homogeneous-memory direction unless an independent estimate couples \(P(t_c)\) to a parabolic quantity. A sufficient, explicitly unverified, **snapshot absorption premise** would be: for the same weights and all actual solutions, \(s^{-1/2}\|e^{s\psi}P(t_c)\|_2^2\le \varepsilon_s\mathcal I_s(Y)+C_s\|Y_x(0,\cdot)\|_{L^2(J)}^2\), with \(\varepsilon_s\) small enough to absorb in a separately established scalar parabolic Carleman inequality. If that inequality has positive left side controlling \(Y\), treats \((B/M)Y\) and time-cutoffs, and has no uncontrolled boundary terms, combining it with (14) yields a **conditional** coupled estimate. This premise is almost the desired separation and is not advertised as minimal or proved.

Boundary bookkeeping: \(Y=0\) at both endpoints and \(Y_x(L,t)=Y_x(0,t)\) by oddness; a spatial integration-by-parts Carleman proof produces signed weighted normal-derivative terms at both ends, which must be computed for the chosen weight, not discarded. The ODE has no spatial boundary integration. Temporal cutoffs create bulk commutators and possibly endpoint terms. A classical calculation would require, for example, bounded time and spatial derivatives of \(A\), smooth weights and sufficient solution regularity; the actual global assumptions give \(A_x\in L^\infty_tL^2_x\), not \(A_t\in L^\infty\). On positive strips the earlier better Sobolev bounds still do not by themselves certify a particular boundary Carleman theorem. No spatial weight is shown to absorb an arbitrary snapshot without an extra coercive estimate. Thus no coupled Carleman or snapshot control is proved.

## 5. Delayed memory: a finite Schur certificate, not an observation theorem

From the exact ODE,
\[
D_\delta=e^{-\mu\delta}I+K,\quad Kh=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y[h](r)dr. \tag{17}
\]
By (4), \(K:H\to H^2\cap H^1_0\) is bounded and hence compact into \(H\); \(D_\delta\) is Fredholm of index zero. By the new weak estimate (8),
\[
\|Kh\|_{H^1_0}\le C_K\|h\|_{V'},\qquad
\|K(I-P_N)\|_{H\to H}\le C_K/q_{N+1}. \tag{18}
\]
The first inequality follows by Cauchy–Schwarz in time; the constant includes \(|\gamma|\), \(\delta\) and the embedding constant. This is a concrete high-frequency near-identity property of the **memory map**, not a flux lower bound.

### Theorem B — exact finite Schur-complement criterion

Put \(Q_N=I-P_N\), \(d_0=e^{-\mu\delta}>0\). Whenever a verified \(C_K/q_{N+1}<d_0\), the tail block
\[
D_{QQ}=Q_ND_\delta Q_N|_{Q_NH}=d_0I+Q_NKQ_N
\]
is invertible by a Neumann series and \(\|D_{QQ}^{-1}\|\le(d_0-C_K/q_{N+1})^{-1}\). Define on \(P_NH\)
\[
F_N=P_ND_\delta P_N-P_ND_\delta Q_ND_{QQ}^{-1}Q_ND_\delta P_N. \tag{19}
\]
Then
\[
\boxed{\ker D_\delta=\{v-D_{QQ}^{-1}Q_ND_\delta v:v\in\ker F_N\},\quad
D_\delta\text{ invertible}\iff F_N\text{ invertible}.} \tag{20}
\]
Proof: solve the tail row of \(D_\delta(v+w)=0\) for \(w\in Q_NH\), and substitute in the finite row. The same block elimination solves arbitrary right-hand sides when \(F_N\) is invertible. This is an exact criterion for the actual map, including all tail feedback via \(D_{QQ}^{-1}\). It is not the determinant of the raw \(N\times N\) truncation, and no determinant is evaluated. A validated implementation would need a certified \(C_K\), certified tail inverse and interval enclosure of \(F_N\); the condition holds abstractly for sufficiently large \(N\), but no usable numerical \(N\) is specified. Even a proof that \(D_\delta\) is invertible would not imply \(\mathcal T\) injective.

The exact identity
\[
\langle D_\delta h,h\rangle=d_0\|h\|_2^2+\gamma\int_0^\delta e^{-\mu(\delta-r)}\langle Y[h](r),h\rangle dr \tag{21}
\]
has an uncontrolled signed cross term. Testing the heat equation by \(Y_t\) and the ODE by \(P\) supplies forward upper energy estimates, not a positive lower bound for (21); variable \(M,S,B\) obstruct a constant symmetrizer without further conditions. Even \(S\gamma\ge0\) throughout \((0,\delta)\) is only a cooperative cone statement and does not prove signed quadratic positivity. A sufficient (not verified) condition \(\|K\|<d_0\) gives coercivity in real part and invertibility. In general \(E=\ker D_\delta\) is finite-dimensional and \(E\subset H^2\cap H^1_0\cap H\), because \(h=-d_0^{-1}Kh\); (20) characterizes its elements without claiming a concrete eigenvector.

Let \(U h=Y[h](\delta)\), \(N=E\cap\ker U\), \(F_*=U(E)\). For an orthonormal basis \(v_i\) of \(F_*\), choose \(e_i\in E\) with \(Ue_i=v_i\), and set \(G_{ij}=\langle\mathcal Te_i,\mathcal Te_j\rangle_{L^2(J)}\). Since \(D_\delta e_i=0\), \(G\)'s nullspace is exactly the coefficient representation of \(F_0=\{v\in F_*:\mathcal R_\delta(v,0)=0\}\). The full \(\ker(\mathcal T|_E)\) has dimension \(\dim N+\dim F_0\); positive \(G\) eliminates \(F_0\) only, not \(N\). No Gram entries or signs are known. On \(H_1=E^\perp\), \(D_1:D_1H_1=\operatorname{ran}D_\delta\) is a bounded isomorphism; the graph temperature is \(A_*=UD_1^{-1}\). With \(O_*=\mathcal T(E)\), the graph quotient is
\[
\widehat\Gamma=(I-P_{O_*})\mathcal T|_{H_1}D_1^{-1}. \tag{22}
\]
It is compact and its kernel may be infinite-dimensional. Exact decomposition \(\dim\ker\mathcal T=\dim N+\dim F_0+\dim\ker\widehat\Gamma\) does not bound the last term. Zero observation never implies \(P(\delta)=0\). No energy, sign or graph unique-continuation proof closes (22).

## 6. Dual separation without strict Hopf

For any \(f\in L^2(J)\), solve the forward zero-initial forced pair for \(F,G\in L^2_{t,x}\). The bounded functional
\[
\Lambda_f(F,G)=2A_0\kappa\int_J f(t)y_x(t,0)dt
=\iint(Fz_f+Gw_f) \tag{23}
\]
defines unique \(z_f,w_f\in L^2_{t,x}\). Distributional testing yields
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\quad
-w_{f,t}+\mu w_f-Sz_f=0,\quad
w_f(T)=0,\quad w_f\in H^1_tL^2_x, \tag{24}
\]
and
\[
 w_f(0)=\int_0^T e^{-\mu t}S(t)z_f(t)dt,\quad
\mathcal T^*f=\Pi_o w_f(0). \tag{25}
\]
The formal boundary conditions are \(z_f(0,t)=2A_0\mathbf1_J f(t)\), \(z_f(L,t)=0\), and \(M(T)z_f(T)=0\), encoded by (23), not claimed classical traces. Full-space forced tests are used in (23); odd projection is applied only in (25).

A concrete characterization that does not merely rename \(\ker\mathcal T\) is
\[
\mathscr R^\perp=\left\{h\in H:\int_0^T e^{-\mu t}\langle S(t)h,z_f(t)\rangle_{L^2_x}dt=0\quad\forall f\in L^2(J)\right\}. \tag{26}
\]
It is equivalent to the kernel by duality but explicitly displays the actual adjoint family and time-weighted spatial pairings. In moment form, \(\langle\mathcal T^*f,\phi_n\rangle=\langle f,k_n\rangle\). A dual proof of density requires, for every nonzero \(h\in H\), a control \(f\) whose *whole* series \(\sum h_n\langle f,k_n\rangle\) is nonzero. Separating each basis vector individually is insufficient. Orthogonality to all controls yields the weighted identity (26), but no closed scalar adjoint equation or time-analytic continuation that separates \(h\) is available.

A second test family or sign-changing controls cannot be asserted to remove cancellations merely from the non-strict cone: the latter requires \(C_+=\operatorname{sgn}\gamma S\ge0\) from time zero through some \(t_1>\delta\) and does not prove positive response for all signed inputs. One-end actuation plus parity correctly doubles the flux but supplies no verified spectral completeness in this nonautonomous coupled problem. An adjoint backward-UC theorem for \((z,w)\) would also need to respect its distributional boundary data and the nonsmoothing ODE; scalar homogeneous backward UC is insufficient. The range \(\mathscr R\) is not shown dense, nor has a nonzero element of (26) been constructed. A nonzero element there would be a state not separated by reachable memory projections, not a constructed actual physical invisible \(H^2\) profile unless it also lies in \(X\).

## 7. Exact-candidate search and nonlinear interpretation

* Endpoint-compatible odd \(h\), and even \(h\) vanishing near endpoints with nonzero interior, still generate the actual distributed source \(SP\); boundary compatibility or zero finite jets do not give zero delayed flux.
* A computed eigenvector of \(D_\delta\) with eigenvalue zero would have \(P(\delta)=0\), but may have nonzero \(U h\) and output. Schur test (20) gives a rigorous route to find or exclude this finite-dimensional possibility, but has not been evaluated. Generalized eigenvectors need not lie in \(E\).
* Multiple exact modal terms may cancel, but no convergent nonzero \(\ell^2\) coefficient sequence satisfying the entire coupled time-series identity has been exhibited. A zero finite set of temporal samples or a tiny singular value is not such a sequence.
* The adjoint orthogonality (26) is necessary and sufficient for linearized invisibility; it does not exhibit a state. Parabolic smoothing gives approximate high-frequency invisibility by (6), not an exact zero. Setting a coupling or the active load to zero, or selecting independent \(M,B,S\), would change the prescribed problem. The criterion \(|b|r\theta_*-|b|r\|y_b(t)\|_\infty-2k\|w_b(t)\|_\infty>0\) is a sufficient actual sign test, not a special parameter relation proving signed injectivity; it has not been verified on \(J\).

No exact nonzero physical invisible state is constructed. For a nonlinear map, let \(\mathcal U\subset X\) be an **open** neighborhood of the base in which every initial state yields a unique solution of the frozen nonlinear problem through \(T\), with positive temperature and an \(L^2(J)\) boundary-flux trace. Define \(\mathcal F:\mathcal U\to L^2(J)\) by the actual odd boundary-difference flux. The existing sufficient small-data theorem does not by itself establish all these uniform neighborhood, trace and differentiability properties in the constrained admissible topology. A valid differentiability proof must bound the nonlinear remainder after subtracting the active-base solution and the solution of (2), in the strong-temperature norm, and show it is \(o(\|h\|_X)\); then \(D\mathcal F(0)=\mathcal T|_X\). This identification is **conditional**, not asserted established here.

Even an injective compact derivative does not in general imply local nonlinear injectivity. A classical Banach inverse theorem requires an isomorphism between specified Banach spaces; a compact derivative on an infinite-dimensional full input space cannot be bounded below in \(L^2\). Restricted smoothness classes can still have nonlinear identification if one proves a separate uniform two-point estimate, e.g. \(\|h_1-h_2\|_H\le\Omega(\|\mathcal F(h_1)-\mathcal F(h_2)\|)\), or a remainder estimate small relative to a verified linear modulus on all differences. Neither is established. A finite-dimensional parameter manifold may admit an inverse if its restricted derivative has a verified positive smallest singular value and the necessary regularity holds; that changes the input class, not the physical experiment.

## 8. Targeted primary-source check

This targeted search is not a comprehensive priority search. Statements/proofs inspected are distinguished from their cited external dependencies.

1. Yavar Kian, Diomba Sambou, Eric Soccorsi, *Logarithmic stability inequality in an inverse source problem for the heat equation on a waveguide*, [arXiv:1612.07942v1](https://arxiv.org/html/1612.07942), 2016. The paper's source is the separated \(\sigma(t)\beta(x)\) for a scalar constant-principal heat equation in an infinite waveguide; Theorem 1.2 also imposes spatial a priori conditions and specific measurements. Its proof proceeds through a Carleman observability inequality and a heat-semigroup argument. The actual source \(SP\) is coupled to the solution and coefficients vary in space and time, so neither its stability nor its boundary asymptotics transfer. Selected statement/argument passages were inspected; the full dependency chain was not independently certified.
2. Jone Apraiz, Rodrigo Lecaros, Sebastián Zamorano, *A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations*, [arXiv:2610.26157v1](https://arxiv.org/html/2610.26157), 2026. Lemma 2.2 and its Schur proof give a centered-weight ODE estimate with an explicit center-time state term; Theorem 2.3 uses interior observation and a snapshot in a different Kelvin–Voigt system. The actual endpoint-only data do not supply that term; (14) is independently rederived in the predecessor. No transfer is claimed.
3. Dev Prakash Jha and Raju K. George, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), 2026. Lemma 3.5 assumes zero initial ODE auxiliary memory, special delay-compatible weights and a moving interior observation. Its proof invokes a prior moving-control estimate rather than proving that dependency in full. The actual delayed \(P\) is unknown and endpoint data are different.
4. Andrei Halanay and Luciano Pandolfi, *Approximate controllability and lack of controllability to zero of the heat equation with memory*, [arXiv:1404.2745v1](https://arxiv.org/html/1404.2745), 2014. Theorems 1–2 and their Volterra-transformation argument concern a scalar Coleman–Gurtin equation, \(C^1\) time-convolution kernel multiplying the Laplacian, bounded \(C^2\) domain and admissibility of boundary controls. Its reachable temperature is not the initial-memory projection in (25). The theorem and proof portions were inspected; it does not prove density here.
5. Guillaume Olive, *Boundary approximate controllability of some linear parabolic systems*, [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), 2026. Theorem 1.1 and appendix use an autonomous generator, compact resolvent, complete adjoint root vectors and an appropriate observation operator. The appendix uses spectral projections and complex resolvent analyticity. These hypotheses are not established for the active time-dependent PDE–ODE; the ODE component also prevents assuming compact resolvent. No infinite moment theorem transfers.
6. Christian Clason, *Regularization of inverse problems*, [arXiv:2001.00617](https://arxiv.org/abs/2001.00617), lecture notes. Compact-operator singular-system theory and regularization are relevant background, not an exact finite-section certificate for (2); the theorem/proof were inspected in the accessible PDF extract, not an exhaustive finite-section literature review. Theorems A–B above are independently derived here and priority is not established.

Other targeted searches included nonautonomous memory Carleman and high-frequency boundary work. The primary statement and proof of a theorem specifically yielding the variable-coefficient active boundary leading term or the required \(\sigma_N\) bound were **not located/verified**. Inaccessible or abstract-only papers are not used as evidence of applicability or novelty.

## 9. Reproducible diagnostic and certification plan

Required inputs: the actual dimensional \(a,k,b,c,\kappa,\lambda,\theta_*,L,A_0,g_*\), all prescribed initial/bath data, units, \(T,\delta\), and the numerical values/constants needed to verify the sufficient base hypothesis. Do not substitute equilibrium for the active base. Use compatible discretizations for the nonlinear base and the full \(M,B,S\), with odd symmetry checked rather than imposed on non-symmetric coefficients by fiat. The quantities \(C_E,C_K,C_\eta\) require certified ellipticity, coefficient and multiplier norms with unit-consistent conversion; observed numerical convergence alone is not a rigorous bound.

```text
read frozen parameters, units and active loading; verify sufficient hypotheses
compute active base on mesh dx,dt; form M,B,S including Q(y_b)_t and history
for each refinement of base, dx, dt, boundary quadrature:
    for n=1,...,N solve coupled linearized PDE–ODE with P(0)=phi_n
    retain complete memory integral, original signs, and Y Dirichlet endpoints
    record flux k_n on J and assemble Gram G_N via convergent time quadrature
    solve transposition adjoint with test controls supported in J
    check <f,k_n> = <Pi_odd w_f(0),phi_n> independently
    estimate flux and Gram errors by refinement AND validated residual bounds
    bound sigma_N below by sqrt(max(0,lambda_min(Ghat_N)-||G_N-Ghat_N||))
    bound e_N by independently certified C_eta*q_(N+1)^(-1/2+eta)
    insert only positive lower bounds and tail bounds into (12)
    optionally certify C_K/q_(N+1)<exp(-mu*delta), enclose tail resolvent,
      and compute interval enclosure of exact Schur complement (19)
separate measurement noise, base discretization, PDE/ODE residual,
  flux quadrature, Gram perturbation and infinite tail in the error budget
```
For physical \(H^2_o\) studies include boundary-lifting functions such as \(1-2x/L\), plus boundary-compatible basis functions; Dirichlet sines alone need not approximate nonzero endpoint data in \(H^2\). Finite-section checks based on sines still approximate every input in \(L^2\), with tail (10). Repeat for increasing \(N\) and independent spatial/time meshes; report actual errors and units. A small singular value could reflect approximate invisibility, resolution/noise or finite-dimensional cancellation; a rigorous **exact zero** requires an analytically verified nonzero \(h\in X\) satisfying the actual equations and zero output a.e. on all of \(J\). Conversely, positive finite Grams and numerical convergence cannot prove no infinite cancellation. A certified positive \(a_j\) and a certified infinite-tail bound meeting (11), not ordinary numerical rank, would prove the stated restricted-class separation.

## 10. Final theorem map

| Question | Verdict | Justification |
|---|---|---|
| High-frequency asymptotic of \(k_n\) | **NOT ESTABLISHED** | Actual algebraic upper bound (6), but no leading term or lower remainder. |
| Lower bound for \(\sigma_N\) | **NOT ESTABLISHED** | Individual-column upper bounds cannot control smallest singular values. |
| Upper bound for \(e_N\) | **PROVED** | (6), under the inherited active-base hypotheses. |
| Finite-section injectivity criterion | **CONDITIONAL** | (11)–(12) prove smooth-class separation if actual bounds are certified. |
| Coupled Carleman estimate | **NOT ESTABLISHED** | Snapshot, coefficient and boundary terms remain uncontrolled. |
| Memory snapshot control | **NOT ESTABLISHED** | Two-time difference removes rather than bounds homogeneous memory. |
| Delayed-state injectivity | **NOT ESTABLISHED** | Exact Schur test (20), no verified finite determinant. |
| Reachable-graph injectivity | **NOT ESTABLISHED** | Compact quotient (22) remains unresolved. |
| Adjoint range density | **NOT ESTABLISHED** | Explicit orthogonal characterization (26), no separating controls. |
| Exact invisible input | **NOT CONSTRUCTED** | No actual nonzero \(H^2_o\) solution with zero delayed flux. |
| Full odd-channel injectivity | **NOT ESTABLISHED** | Neither (11) nor an independent continuation theorem verified. |
| Nonlinear local identification | **NOT ESTABLISHED** | Neighborhood, differentiability and nonlinear two-point estimate missing. |
| New mathematical theorem | **NOT ESTABLISHED** | Theorems A–B and conditional criterion are proved here under stated hypotheses, but mathematical novelty/priority is unverified. |
| New foundational continuum theory | **REFORMULATE** | No new foundational principle is demonstrated. |

The constructive next targets are a certified smallest-singular-value/tail relation sufficient for (11), or an independent graph separation theorem controlling the homogeneous ODE snapshot. Neither is inferred from finite matrices, positivity on a cone, smooth coefficients alone, or compactness. Final decision belongs to Dr. Gupta.
