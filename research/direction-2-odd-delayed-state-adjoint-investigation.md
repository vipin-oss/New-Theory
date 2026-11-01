# Delayed-state factorization, Fredholm structure and adjoint completeness

**Date:** 1 November 2026

**Final verdict: ADJOINT-DENSITY REDUCTION PROVED, DENSITY OPEN.** The exact delayed-state factorization holds in a specified strong-temperature state space and on the odd \(L^2\) extension. The delayed state map has closed range and finite-dimensional kernel; its memory component is Fredholm of index zero. A rigorous transposition construction identifies the actual adjoint observation map with the initial memory component of a backward coupled system. The remaining reachable-state intersection / adjoint density has not been proved trivial. In particular, we do **not** prove that the whole observation kernel is finite-dimensional.

This is an Arena single-agent recalculation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. No general Carleman or literature survey, simulation, change to the experiment, novelty claim, or nonlinear inverse conclusion is made.

## 1. Frozen model and prior audit

We read in full `direction-2-odd-exact-kernel-investigation.md`, `direction-2-odd-channel-updated-uc-independent-audit.md`, `direction-2-active-base-regularity-independent-audit.md`, and `direction-2-odd-channel-independent-audit.md`. Keep the actual nonzero-loading active base, \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\), \(T=10/\lambda\), \(\delta=T/100\), \(I=(0,L)\), \(J=(\delta,T)\), and all active couplings. Put
\[
D=a+k,\ r=k/D,\ \alpha=a/D,\ \beta=b/D,\ \mu=\lambda\alpha,\ \gamma=\lambda\beta,\ d=b^2/D,\ Qv=v-\bar v.
\]
All material signs are as in the previous report: \(a,k,c,\kappa,\lambda,L,A_0,\theta_*,M>0\), \(b\ne0\). For the active symmetric base,
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b.\tag{1}
\]
Use the existing sufficient but numerically unverified hypothesis \(0<q=|g_*|/L<s_*\). It supplies \(m_0\le M_b\le m_1\), \(M_b,S\in L^\infty\), and \(B\in L^2((0,T)\times I)\). On \(J\), the audited upgrade gives \(B\in L^6_{t,x}\cap L^\infty_tL^2_x\cap L^2_tL^\infty_x\); \(M_b,\kappa/M_b\) are uniformly spatially Lipschitz and temporally \(3/4\)-Hölder. The continuous representative of \(S\) comes from the base construction. No \(C^1\) or time-Lipschitz principal coefficient is assumed.

For \(X_o=\{h\in H^2(I):h(L-x)=-h(x)\}\), put \(H_o=L^2_o(I)\). The exact system and observation are
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\\
Y(0,\cdot)=0,\ P(0,\cdot)=h,\quad Y(t,0)=Y(t,L)=0,
\end{cases}\qquad
\mathcal T_oh=2A_0\kappa Y_x(\cdot,0)|_J.\tag{2}
\]
Time is written first when ambiguity is possible. The established linear bound, initially for \(X_o\) and then by density for \(H_o\), is
\[
\|Y\|_{\mathcal E(0,T)}+\|P\|_{H^1(0,T;L^2)}\le C_E\|h\|_2,
\quad \mathcal E(a,b)=H^1(a,b;L^2)\cap L^2(a,b;H^2\cap H^1_0),\tag{3}
\]
with \(Y\in C_tH^1_0\), \(P\in C_tL^2\). The extension is linear analytic, not a nonlinear admissibility claim.

### 1.1 Independent check of the previous exact-kernel report

| Claim | Recalculation and result |
|---|---|
| Weak boundary identity | **Correct.** \(\langle Y_{xx},\psi\rangle=[Y_x\psi]_0^L+\langle Y,\psi''\rangle\), because \(Y\) has zero Dirichlet traces. Thus the boundary terms in (4) below have the reported signs. All terms are \(L^2_t\); no time trace of \(Y_t\) at the spatial boundary is used. |
| Product limits and endpoint memory | **Correct with scope.** The essential cross-section estimate (5) and \(P\in C_tH^2_x\) for \(h\in X_o\) follow as shown below. The product \(SP\) can have a nonzero boundary value; its trace does not imply a trace of either \(Y_t\) or \(Y_{xx}\). For general extended \(H_o\) inputs, \(P\) need not be in \(H^2\). |
| Sine moments and output | **Correct.** Odd sines have eigenvalues \((2n\pi/L)^2\). Matrix terms and the derivative trace converge in the stated norms; zero output gives a zero **sum**, not coefficientwise zero. |
| Delayed memory Fredholm property | **Correct.** Its compact remainder has range in \(H^2\), so the scalar nonzero multiple of the identity plus it is index zero. The joint state kernel is finite-dimensional, but that does not imply the observation kernel is. |
| Adjoint equivalences and input span | **Correct.** Density in \(H_o\) is stronger than the restricted \(X_o\) criterion; sine sums are dense in \(H_o\) but not in all \(X_o\) in the \(H^2\) norm. |

One typographical error is corrected here without editing the earlier file: in the last paragraph of its §6, the intended convergence \(\|\mathcal T_o^*f_{n,j}-\phi_n\|_2\to0\) contains a tab instead of the LaTeX command \(\backslash\mathrm{to}\). The mathematical statement was clear from context; the correct formula is given in §6 below.

For fixed \(\psi\in H^2(I)\), testing (2) gives in \(L^2(J)\)
\[
\langle M_bY_t,\psi\rangle-\kappa\langle Y,\psi''\rangle
+\kappa Y_x(t,0)\psi(0)-\kappa Y_x(t,L)\psi(L)
=\langle BY+SP,\psi\rangle.\tag{4}
\]
With \(\psi=1-x/L\) it explicitly represents the measured derivative; all other fixed \(H^2\) tests recover the same PDE and the two boundary traces. Time-dependent tests can be integrated to yield useful duality identities, as in §5; without a suitable adjoint solution they do not add an independent observation. The observation and oddness give \(Y_x(t,0)=Y_x(t,L)=0\) a.e. on \(J\), not interior zero.

For a.e. \(x\), using \(|Y(t,x)|\le\sqrt{x}\|Y_x(t)\|_2\),
\[
\|B(\cdot,x)Y(\cdot,x)\|_{L^2(J)}\le
\sqrt{x}\|Y_x\|_{L^\infty(J;L^2)}\|B\|_{L^2(J;L^\infty)}.\tag{5}
\]
This is an essential \(x\downarrow0\) cross-section limit, not necessarily a classical trace of \(B\). The formula
\[
P(t)=e^{-\mu t}h+\gamma\int_0^t e^{-\mu(t-r)}Y(r)\,dr\tag{6}
\]
is a continuous \(H^2\)-valued identity for \(h\in X_o\), since \(Y\in L^1_tH^2_x\). Since \(Y(r)\in H^1_0\) a.e., \(P(t,0)=e^{-\mu t}h(0)\); oddness gives \(P(t,L)=-P(t,0)\). As \(S\) is continuous, \(SP\) has its corresponding endpoint value, possibly nonzero. The individual \(M_bY_t\) and \(Y_{xx}\) have only interior \(L^2\) regularity; equation (2) may not be evaluated termwise at an endpoint. Time differentiation of the zero flux is valid only as a distributional derivative of the trace, not as an identified trace of \(Y_{xt}\).

## 2. A forward estimate and the delayed observation operator

Set \(V_o=H^1_0(I)\cap H_o\), \(Z=H_o\times H_o\), and the natural strong-temperature restart space \(Z_1=V_o\times H_o\). Equip \(Z_1\) with the product Hilbert norm. For \((y_0,p_0)\in Z_1\), define \(\mathcal R_\delta(y_0,p_0)=2A_0\kappa y_x(\cdot,0)\) on \(J\), where \((y,p)\) solves (2) from \(t=\delta\) with that prescribed pair. This pair is a mathematical state, not an assertion that every such state is reachable from the physical initial memory.

The necessary bounded well-posedness can be checked directly, without a general nonautonomous maximal-regularity theorem. On any \((a,b)\subseteq(0,T)\), also allow sources \(F,G\in L^2((a,b)\times I)\):
\[
M_by_t-\kappa y_{xx}=By+Sp+F,\quad p_t+\mu p=\gamma y+G,\quad y|_{\partial I}=0.\tag{7}
\]
Use a Dirichlet sine Galerkin approximation for \(y\), and an \(L^2\) orthonormal basis for \(p\), preserving parity for odd data. The finite mass matrix is uniformly positive. Test the heat equation by \(y_t\), the ODE by \(p\), and set \(E(t)=\kappa\|y_x(t)\|_2^2+\|p(t)\|_2^2\). The 1-D embedding \(\|y\|_\infty\le\sqrt L\|y_x\|_2\), Young's inequality, bounded \(S\), and Poincaré yield for constants depending on the frozen parameters and \(m_0\),
\[
E'(t)+m_0\|y_t\|_2^2
\le C\bigl(1+\|B(t)\|_2^2\bigr)E(t)+C(\|F(t)\|_2^2+\|G(t)\|_2^2).\tag{8}
\]
Here \(\|By\|_2\le\|B(t)\|_2\sqrt L\|y_x\|_2\); no bound on \(M_{b,t}\) is used. Gronwall gives a uniform \(C_tH^1_0\), \(H^1_tL^2\) and \(C_tL^2\) bound. The Galerkin heat equation, projected in \(L^2\), gives the \(L^2_tH^2\) bound because \(M_by_t,By,Sp,F\in L^2\); the ODE gives \(p_t\in L^2\). Weak compactness, strong compactness of \(y\) in \(L^2_tH^s_x\), \(s\in(1/2,1)\), and boundedness of multiplication by \(B\) on the appropriate products allow passage to (7); alternatively the linear products can be identified weakly against bounded tests. The same estimate applied to differences yields uniqueness. The standard Hilbert time-trace argument gives \(y\in C_tH^1_0\), \(p\in C_tL^2\). In particular,
\[
\|y\|_{\mathcal E(a,b)}+\|p\|_{H^1(a,b;L^2)}
\le C_{a,b}(\|y_0\|_{H^1_0}+\|p_0\|_2+\|F\|_2+\|G\|_2).\tag{9}
\]
The constants are finite because \(\int\|B(t)\|_2^2dt<\infty\). The endpoint derivative trace is continuous \(L^2_tH^2_x\to L^2_t\); hence \(\mathcal R_\delta:Z_1\to L^2(J)\) is bounded. No claim is made here that an arbitrary \(L^2\) initial *temperature* produces an \(L^2(J)\) endpoint flux; its initial-time singularity needs a different state/output space.

## 3. Exact factorization and operator geometry

Define on \(H_o\)
\[
U_\delta h=Y[h](\delta)\in V_o,\quad D_\delta h=P[h](\delta)\in H_o,\quad
\mathcal S_\delta h=(U_\delta h,D_\delta h)\in Z_1.\tag{10}
\]
The solution estimate and time traces give boundedness \(\mathcal S_\delta:H_o\to Z_1\). Restricting the unique full trajectory to \(J\) and using uniqueness in (9) gives the **exact identity**
\[
\mathcal T_o=\mathcal R_\delta\mathcal S_\delta\quad\text{on }H_o,\ \text{hence also on }X_o.\tag{11}
\]
This is factorization through the correlated reachable pair, not independent delayed memory and temperature data.

The temperature map \(U_\delta:H_o\to H_o\) is compact: it is bounded into \(V_o\Subset H_o\). This argument does **not** establish compactness as a map into \(V_o\). Equation (6) gives
\[
D_\delta=e^{-\mu\delta}I+K_\delta,\quad
K_\delta h=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y[h](r)\,dr.\tag{12}
\]
By (3), \(K_\delta:H_o\to H^2(I)\) is bounded, and its inclusion into \(H_o\) is compact. Therefore \(D_\delta:H_o\to H_o\) is Fredholm, index zero, with finite-dimensional kernel and cokernel and closed range. These are statements about \(H_o\), not Fredholmness in the \(H^2\) input norm.

For geometry use also the continuous embedding \(i:Z_1\to Z\) and let \(\widetilde S=i\mathcal S_\delta:H_o\to Z\). Write
\[
\widetilde S h=(0,e^{-\mu\delta}h)+(U_\delta h,K_\delta h)=Jh+Ch,\tag{13}
\]
where \(C:H_o\to Z\) is compact and \(J\) is bounded below. Consequently there is \(c>0\) such that
\[
\|\widetilde S h\|_Z\ge c\,\operatorname{dist}(h,\ker\widetilde S).\tag{14}
\]
Proof: if (14) failed, choose unit \(h_n\perp\ker\widetilde S\) with \(\widetilde S h_n\to0\). Compactness gives a convergent subsequence of \(Ch_n\); since \(J\) is bounded below, \(h_n\) is then strongly convergent. Its limit has norm one and lies both in the kernel and its orthogonal complement, contradiction. The same compactness argument makes the unit ball of the kernel compact, hence the kernel is finite-dimensional; (14) gives closed range in \(Z\). In particular \(\ker\widetilde S\subseteq\ker D_\delta\). The map is not compact: for an orthonormal weakly null sequence, the second component is \(e^{-\mu\delta}h_n+o(1)\).

\(\widetilde S:H_o\to Z\) is **not Fredholm** in the usual two-sided sense: \(J\) has infinite-dimensional cokernel \(H_o\times\{0\}\), and a compact perturbation of a Fredholm operator is Fredholm iff the original is. Equivalently, it is upper semi-Fredholm (closed range, finite kernel) with infinite-dimensional cokernel. Whether \(\widetilde S\), or \(\mathcal S_\delta\), is injective remains open. Closedness of the range in \(Z\) implies closedness of \(\operatorname{ran}\mathcal S_\delta\) in the stronger space \(Z_1\), because a \(Z_1\)-convergent reachable sequence also converges in \(Z\), and the resulting state lies in \(Z_1\). In \(Z_1\), the cokernel is also infinite-dimensional: the map \(v\mapsto[(v,0)]\) embeds \(V_o/U_\delta(\ker D_\delta)\) into \(Z_1/\operatorname{ran}\mathcal S_\delta\), and the denominator is finite-dimensional. Hence \(\mathcal S_\delta:H_o\to Z_1\) is upper semi-Fredholm but not Fredholm, and is not compact because its memory component is not compact.

Let
\[
N=\ker\mathcal S_\delta,\qquad W=\ker\mathcal R_\delta\cap\operatorname{ran}\mathcal S_\delta\subset Z_1.\tag{15}
\]
Both are closed in their indicated spaces, \(\dim N<\infty\), and \(\mathcal S_\delta\) induces the exact sequence
\[
0\longrightarrow N\longrightarrow\ker\mathcal T_o
\xrightarrow{\ \mathcal S_\delta\ } W\longrightarrow0.\tag{16}
\]
By (14), its restriction to \(N^\perp\) has a bounded inverse on its range even when the range is given the \(Z_1\) norm. Thus, as Hilbert spaces,
\[
\ker(\mathcal T_o:H_o\to L^2(J))\cong N\oplus W.\tag{17}
\]
This is a genuine decomposition into a finite-dimensional pre-delay loss and a separately characterized reachable delayed-observation kernel. **It does not establish \(\dim W<\infty\)**, so it does not prove the observation kernel finite-dimensional. On the frozen domain, the exact algebraic sequence uses \(N\cap X_o\) and \(W_X=\ker\mathcal R_\delta\cap\mathcal S_\delta(X_o)\); \(W_X\) need not be closed. Restricted injectivity is equivalent to
\[
N\cap X_o=\{0\}\quad\text{and}\quad W_X=\{0\}.\tag{18}
\]
For the full \(H_o\) extension, replace these by \(N=\{0\}\) and \(W=\{0\}\). The intersection condition by itself is insufficient if \(N\ne0\). Equations (15)–(18) are exact structural reductions, but the identity of \(W_X\) is a reformulation until a separate reachable-state observability theorem is supplied.

## 4. Can the finite-dimensional part be settled?

The ODE integrates to (12), so \(D_\delta h=0\) means
\[
h=-\gamma e^{\mu\delta}\int_0^\delta e^{-\mu(\delta-r)}Y[h](r)dr.\tag{19}
\]
This is an eigenvalue equation for a compact operator, not a triangular Volterra equation in the unknown initial field \(h\). Its finite-dimensional solution space may be zero, but neither the sign of \(b\) nor the energy estimate (8) rules out a finite-dimensional cancellation. The PDE energy is forward and does not yield a lower bound on \(P(\delta)\). No proved backward uniqueness for the coupled active system is available. A joint-zero input must satisfy (19) **and** \(Y[h](\delta)=0\); hence it is an explicitly characterized subspace of \(\ker D_\delta\), but neither is shown trivial.

The previous estimate is correct: from \(Y(0)=0\) and Cauchy–Schwarz,
\[
\|Y(r)\|_2\le\sqrt r\,\|Y_t\|_{L^2(0,\delta;L^2)}\le C_E\sqrt r\|h\|_2,
\quad \|K_\delta\|\le\frac23|\gamma|C_E\delta^{3/2}.\tag{20}
\]
If \((2/3)|\gamma|C_E\delta^{3/2}<e^{-\mu\delta}\), then (12) is invertible by a Neumann series, so \(N=0\). This sufficient inequality is **additional and unverified** and says nothing by itself about \(W\).

The constant need not depend circularly on the unknown linearized solution. The original existence report's explicit reference-solver constant \(C_L\), common fixed-point derivative bound \(\|D_y\Phi\|\le1/2\), and bounds \(\|y_b\|_\infty\le2K_xC_Bq\), \(\|w_b\|_\infty\le C_wq\), \(C_w=W_s+2C_BW_R\), give a valid **temperature** bound
\[
C_{Y}\ :=2C_L\left[1+\sqrt T\,q\{2|br\mu|K_xC_B+2k\lambda\alpha C_w\}\right],
\qquad \|Y_t\|_{L^2(0,T;L^2)}\le C_Y\|h\|_2.\tag{21}
\]
Indeed, the reference solver receives the initial memory \(h\) and the additional forcing \((br\mu y_b-2k\lambda\alpha w_b)e^{-\mu t}h\); its norm is bounded by the displayed bracket, and the inverse fixed-point derivative has norm at most two. The constants \(C_L,K_x,C_B,W_s,W_R\) are data-only constants of that fixed-unit construction. Formula (20) can use \(C_Y\) in place of \(C_E\); this does not require bounding the memory part of the full \(C_E\). It is generally conservative and supplies no verification of the numerical Neumann condition without the actual material/load values. Nothing changes the prescribed \(\delta\).

## 5. Actual coupled adjoint by transposition

### 5.1 Construction on the whole frozen interval

For this section temporarily allow general (not necessarily odd) source functions in (7), with zero initial data on \((0,T)\). The coefficients in (1) are even in space, and the same energy proof works for the displayed local system on full \(L^2(I)\). This auxiliary source problem is a mathematical duality device; it does not change the physical odd input or observation. Let \((y[F,G],p[F,G])\) be its solution. By (9) and the endpoint trace theorem, for \(f\in L^2(J)\)
\[
\Lambda_f(F,G)=2A_0\kappa\int_J f(t)y[F,G]_x(t,0)dt
\]
is a bounded functional on \(L^2((0,T)\times I)^2\). Riesz representation gives a unique pair
\[
(z_f,w_f)\in L^2((0,T)\times I)^2,\qquad
\iint(Fz_f+Gw_f)=\Lambda_f(F,G).\tag{22}
\]
This is a **constructed**, not assumed, transposition solution. Its norm is bounded by \(C\|f\|_{L^2(J)}\).

Taking smooth compactly supported \((u,v)\), setting
\[
F=M_bu_t-\kappa u_{xx}-Bu-Sv,\qquad G=v_t+\mu v-\gamma u,
\]
and noting the corresponding forward solution is exactly \((u,v)\), (22) implies in distributions
\[
-\partial_t(M_bz_f)-\kappa(z_f)_{xx}-Bz_f-\gamma w_f=0,\qquad
-(w_f)_t+\mu w_f-Sz_f=0.\tag{23}
\]
The mass is **inside** the time derivative. These signs follow directly from the forward residuals; expanding \(-\partial_t(M_bz_f)\) requires additional product regularity and is unnecessary. Since \(S\in L^\infty\), the second equation gives \(w_f\in H^1(0,T;L^2(I))\). Testing (22) with \(u=0\) and \(v\) smooth, \(v(0)=0\) but arbitrary \(v(T)\), yields the terminal trace
\[
w_f(T)=0,\qquad
w_f(t)=\int_t^T e^{-\mu(s-t)}S(s)z_f(s)ds\quad\text{in }L^2(I).\tag{24}
\]
In particular \(w_f(0)\) is a genuine \(L^2\) state.

### 5.2 Boundary input, terminal condition and rigorous pairing

For smooth coefficients and adjoint fields, integrating the residuals gives the heat boundary term
\[
\kappa\int_0^T\bigl[y_x(t,0)z_f(t,0)-y_x(t,L)z_f(t,L)\bigr]dt,
\]
plus terminal \(\langle M_b(T)y(T),z_f(T)\rangle+\langle p(T),w_f(T)\rangle\) and minus the corresponding initial terms. Thus the formal boundary/terminal data corresponding to (22) are
\[
z_f(t,0)=2A_0\,\mathbf1_J(t)f(t),\quad z_f(t,L)=0,\quad
M_b(T)z_f(T)=0,\quad w_f(T)=0.\tag{25}
\]
For merely \(L^2\) boundary input, (22) is the rigorous **definition** of (25) in transposition; \(z_f\) is only known in \(L^2_{t,x}\), so no classical boundary trace or pointwise terminal value is asserted. The exact weak statement is: for every strong pair \((u,v)\) with zero initial data, homogeneous Dirichlet \(u\), and residuals \(F,G\in L^2\),
\[
\iint\{(M_bu_t-\kappa u_{xx}-Bu-Sv)z_f+(v_t+\mu v-\gamma u)w_f\}
=2A_0\kappa\int_J f(t)u_x(t,0)dt.\tag{26}
\]
This incorporates the terminal and boundary terms and follows directly from uniqueness of the forward source problem, not from an unjustified classical integration by parts.

For an actual input \(h\in H_o\), let \((Y,P)\) solve (2) and define \(v=P-e^{-\mu t}h\). Then \((Y,v)\) has zero initial data and solves the source problem with
\[
F=S e^{-\mu t}h,\qquad G=0.
\]
Both are in \(L^2\). Apply (22), then (24):
\[
\begin{aligned}
\langle\mathcal T_oh,f\rangle_{L^2(J)}
&=\iint S(t,x)e^{-\mu t}h(x)z_f(t,x)\,dxdt\\
&=\langle h,w_f(0)\rangle_{L^2(I)}
=\langle h,\Pi_o w_f(0)\rangle_{H_o}.
\end{aligned}\tag{27}
\]
Here \(\Pi_o\) is reflection-odd projection. Consequently
\[
\boxed{\mathcal T_o^*f=\Pi_o w_f(0)\quad\text{in }H_o.}\tag{28}
\]
This is the actual adjoint map, not only a formal PDE. The full adjoint temperature need not be odd because the auxiliary boundary input is imposed at one endpoint; projecting the initial memory is the correct restriction. Equivalently one may use odd boundary data \(z(0)=A_0f\), \(z(L)=-A_0f\), but that equivalence is not needed for (28).

### 5.3 Density criterion

Let \(\mathscr A=\{\Pi_o w_f(0):f\in L^2(J)\}\subset H_o\). Equations (27)–(28) give
\[
\ker(\mathcal T_o|_{X_o})=X_o\cap\mathscr A^\perp,\qquad
\ker(\mathcal T_o|_{H_o})=\mathscr A^\perp.\tag{29}
\]
Thus \(\overline{\mathscr A}^{H_o}=H_o\) is equivalent to injectivity of the \(H_o\) extension and sufficient, but not necessary, for the frozen \(X_o\) question. Exact restricted injectivity needs only \(X_o\cap\mathscr A^\perp=\{0\}\). Full density could be proved by constructing, for every \(n\), controls \(f_{n,j}\in L^2(J)\) such that
\[
\|\Pi_o w_{f_{n,j}}(0)-\phi_n\|_{H_o}\longrightarrow0.\tag{30}
\]
Because \(\mathcal T_o\) is compact, its adjoint is compact; approximate controls may need unbounded norms, and no strong observability estimate follows. We have not constructed the controls or proved (30) or the weaker condition (29). Boundary support only on \(J\), the evolution back through \((0,\delta)\), and the variable couplings in (23) are all retained. This density route is mathematically precise and potentially useful, but not yet a proof of injectivity or a claim of a new theorem.

## 6. Coupled moments, weighted tests and what remains

Let \(\phi_n=\sqrt{2/L}\sin(2n\pi x/L)\), \(\rho_n=(2n\pi/L)^2\), \(u_n=\langle Y,\phi_n\rangle\), \(p_n=\langle P,\phi_n\rangle\). The exact system is
\[
\sum_m\langle M_b\phi_m,\phi_n\rangle u'_m+\kappa\rho_nu_n
=\langle BY,\phi_n\rangle+\sum_m\langle S\phi_m,\phi_n\rangle p_m,\quad
p'_n+\mu p_n=\gamma u_n,\quad p_n(0)=h_n.\tag{31}
\]
\(u(0)=0\). The mass and \(S\) sums converge by Parseval; \(BY\in L^2\); \(u\in H^1_t\ell^2\) and \(\sum\rho_n^2|u_n|^2\in L^1_t\). Strong spectral convergence of \(Y\) in \(L^2_tH^s_x\), \(3/2<s<2\), gives
\[
Y_x(\cdot,0)=\lim_{N\to\infty}\sum_{n=1}^N\phi_n'(0)u_n\quad\text{in }L^2(J).\tag{32}
\]
For every \(f\in L^2(J)\), zero observation implies the exact weighted identity
\[
0=\lim_{N\to\infty}\sum_{n=1}^N\phi'_n(0)\int_J f(t)u_n(t)dt
=\langle h,\Pi_ow_f(0)\rangle.\tag{33}
\]
No interchange of an infinite sum outside its established limit is used. The adjoint identity is a justified dual test sequence; taking increasingly many \(f\)'s yields exactly the annihilator condition in (29), not individual \(h_n=0\) without density.

Define \(\psi_n=\mathcal T_o\phi_n\). For \(h=\sum h_n\phi_n\) in \(H_o\), boundedness gives \(\sum_{n\le N}h_n\psi_n\to\mathcal T_oh\) in \(L^2(J)\), and
\[
\langle\Pi_ow_f(0),\phi_n\rangle=\langle f,\psi_n\rangle_{L^2(J)}.\tag{34}
\]
These are exact weighted moment identities including pre-delay history. The missing completeness result is: the only \(h\in X_o\) whose output series has zero \(L^2(J)\) limit is \(0\), equivalently the restricted annihilator in (29) is zero. A stronger sufficient result is the explicit approximate controllability (30). The spatial multipliers \(M_b,B,S\) can couple modes; no actual off-diagonal entry is asserted nonzero, and no valid general triangularization has been found. Distributional time derivatives of the zero output yield no new independent condition; identifying termwise derivatives of (32) is not justified by its \(L^2\) convergence. Finite truncations cannot establish the needed infinite-family independence.

## 7. Diagnostic numerics and synthesis

The repository supplies no verified numerical material-parameter set or computed nonzero-loading active-base coefficient data for this experiment. A meaningful numerical diagnostic would need \(a,k,b,c,\kappa,\lambda,L,A_0,\theta_*,g_*\), the established-threshold constants and a converged representation of the actual \(M_b,B,S\) on the full interval, including pre-delay evolution. None is invented here; no numerical simulation is performed. Even with such data, singular values of truncated maps would diagnose approximate invisibility, not prove an exact kernel or injectivity.

**Proved here:** the forward restart bound, exact factorization, closed-range/finite-kernel state geometry, decomposition (16)–(17), and the transposition adjoint (22)–(28). **Independently verified:** the previous boundary, trace, moment, and Fredholm calculations, with the explicit typo correction in §1. **Reduced but open:** whether \(N\cap X_o\) is zero, whether \(W_X\) is zero, and equivalently whether the adjoint initial-memory range separates \(X_o\). \(N\) is finite-dimensional; \(W\) has not been shown finite-dimensional. The conditional Neumann test in §4 is not verified and would settle only the pre-delay part. No exact nonzero invisible input is constructed.

**Final verdict: ADJOINT-DENSITY REDUCTION PROVED, DENSITY OPEN.**
