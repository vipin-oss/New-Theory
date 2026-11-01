# Actual-system separation and boundary-control analysis

**Date:** 1 November 2026. **Decision: REFORMULATE.** Three rigorous advances are obtained under the inherited, numerically unverified active-base hypotheses: (i) an actual-coefficient quasi-static high-frequency construction improves the individual sine-column bound to \(\|\mathcal T\phi_n\|=O(n^{-1})\), with a fully specified remainder of the *same* order; and (ii) the observation is Hilbert–Schmidt, so boundary impulses yield an actual \(H\)-valued response family; (iii) no bounded boundary-control pairing can separately extract the endpoint trace while annihilating all zero-endpoint inputs. None of these results proves full injectivity or constructs a physical invisible state. The exact missing statement is separation of the reachable memory projections in §4, or an equivalent actual coupled boundary theorem. No priority or new foundational continuum theory is claimed.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is an Arena recalculation, not an independent human certification. Direction 1 remains rejected as a foundational continuum theory; Direction 2 is an inverse observation/state problem.

## 1. Fixed problem and inherited regularity

The starting report and relevant active-base regularity, forward existence, admissible topology, delayed-adjoint, compact-quotient and high-frequency reports were inspected. Take \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\); the fixed displacement is \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\). With
\[
D=a+k,\ r=k/D,\ \alpha=a/D,\ \beta=b/D,\ \gamma=\lambda\beta,\ \mu=\lambda\alpha,\ d=b^2/D,\ Qv=v-\bar v,
\]
the actual even coefficients are
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{1}
\]
Let \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), \(X=H^2(I)\cap H\), where oddness means reflection about \(L/2\). For \(h\in H\), the actual linearized odd system and measured difference are
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(0)=0,\ P(0)=h,\ Y(t,0)=Y(t,L)=0,\quad
\mathcal Th=2A_0\kappa Y_x(\cdot,0)|_J. \tag{2}
\]
No spatial boundary condition is imposed on \(P\), and \(X\) permits nonzero endpoint values. The extension to \(H\) is a linear analysis device, not a claim of nonlinear physical admissibility. All material couplings and signs remain fixed; no coefficient is frozen or chosen independently.

The inherited sufficient small-load hypothesis \(0<|g_*|/L<s_*\) is **not numerically verified** for the prescribed experiment. Conditional on the base existence/regularity and strong linear forward theory, use
\[
0<m_0\le M\le m_1,\quad M,S\in L^\infty,\quad M_x\in L^\infty_tL^2_x,\quad B\in L^2((0,T)\times I),\tag{3}
\]
\[
Y\in\mathcal E:=H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0),\qquad P\in H^1_tL^2_x,
\qquad \|Y\|_{\mathcal E}+\|P\|_{H^1_tL^2_x}\le C_E\|h\|_2. \tag{4}
\]
The same estimate holds with initial temperature in \(H^1_0\), initial memory in \(L^2\), and arbitrary \(L^2_{t,x}\) sources; parity can be retained. The trace \(Y_x(0,\cdot)\in L^2(0,T)\) is genuine because \(Y\in L^2_tH^2_x\). On each positive-time strip, the audited base also yields \(B\in L^\infty_tL^2_x\cap L^2_tL^\infty_x\cap L^6_{t,x}\), and \(M,\kappa/M\) are spatially Lipschitz and time-Hölder in the previously specified senses. No global \(B\in L^\infty_tL^2_x\) or time analyticity is assumed.

A further regularity consequence, used below, follows from the *actual* base equations, not a new assumption. Since \(y_b\in\mathcal E\cap C_tH^1_0\) and
\[
p_b(t)=\gamma\int_0^t e^{-\mu(t-r)}Qy_b(r)dr,\qquad
w_b=m-v_b-\alpha p_b+\beta Qy_b, \tag{5}
\]
with the prescribed smooth scalar \(m,v_b\), we have \(p_b\in C_tH^1\cap L^\infty_tH^2\), \(p_{b,t}\in L^2_tL^2\), and therefore
\[
S\in C_tH^1_x\cap H^1_tL^2_x\cap L^2_tH^2_x,\qquad S,S_x\in L^\infty_tL^2_x,\quad S\in L^\infty_{t,x}. \tag{6}
\]
For \(p_b\), the \(H^2\) bound follows from Cauchy–Schwarz in time applied to \(Qy_b\in L^2_tH^2_x\); the equality holds in the corresponding Bochner space. \(S(0)\in H^1\) is a legitimate time trace. Constants below are dimensional and depend on the fixed coefficients, \(L,T,m_0,\kappa\), and their stated norms; no numerical values are supplied.

## 2. Transposition and all boundary terms

Let a general strong forward pair have \(y(0)=y_0\in H^1_0(I)\), \(p(0)=p_0\in L^2(I)\), \(y|_{\partial I}=0\), and
\[
F=My_t-\kappa y_{xx}-By-Sp,\qquad G=p_t+\mu p-\gamma y. \tag{7}
\]
For temporarily smooth \(y,p,z,w,M\), spatial integration by parts twice and time integration once give the **full** identity
\[
\begin{aligned}
\iint(Fz+Gw)={}&\big[\langle My,z\rangle+\langle p,w\rangle\big]_{0}^{T}
+\int_0^T\{-\kappa y_x(t,L)z(t,L)+\kappa y_x(t,0)z(t,0)\}dt\\
&+\iint y[-\partial_t(Mz)-\kappa z_{xx}-Bz-\gamma w]
+\iint p[-w_t+\mu w-Sz].
\end{aligned} \tag{8}
\]
Terms \(\kappa[y z_x]_0^L\) vanish because of the forward Dirichlet conditions. The sign \(-\gamma w\) comes from \(-\gamma y\) in \(G\), and \(-Sz\) from \(-Sp\) in \(F\). Formal terminal conditions \(Mz(T)=0\), \(w(T)=0\), and boundary values \(z(t,0)=2A_0\mathbf1_J f(t)\), \(z(t,L)=0\), reduce (8) to
\[
\iint(Fz+Gw)=2A_0\kappa\int_J f(t)y_x(t,0)dt
-\langle M(0)y_0,z(0)\rangle-\langle p_0,w(0)\rangle. \tag{9}
\]
Equation (9) is only a formal Green formula until the boundary/terminal traces are justified. We do **not** assume classical \(z\) traces or a separately defined \(z(0)\).

For the rigorous construction, take the full-space zero-initial forced problem with arbitrary \((F,G)\in L^2_{t,x}\times L^2_{t,x}\), not only odd sources. Estimate (4) for forced pairs and the endpoint trace make
\[
\Lambda_f(F,G)=2A_0\kappa\int_J f y_x(0)dt
\]
a bounded functional. Riesz gives unique \((z_f,w_f)\in L^2_{t,x}^2\) such that
\[
\iint(Fz_f+Gw_f)=\Lambda_f(F,G) \quad\text{for all zero-initial forced pairs}. \tag{10}
\]
Testing (10) with compactly supported smooth \(y,p\) yields in distributions
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\qquad
-w_{f,t}+\mu w_f-Sz_f=0. \tag{11}
\]
All products are meaningful: \(Bz_f\in L^1_{t,x}\), \(M,S\) are bounded. Taking \(y=0\), \(p\in H^1_tL^2_x\) with \(p(0)=0\) in (10) yields
\[
w_f\in H^1(0,T;L^2(I)),\quad w_f(T)=0,\quad
w_f(t)=\int_t^T e^{-\mu(r-t)}S(r)z_f(r)dr,\quad
\|w_f\|_{H^1_tL^2_x}\le C\|f\|_{L^2(J)}. \tag{12}
\]
Thus \(w_f(0)\) exists in \(L^2\). Formula (10), rather than unproved classical traces, encodes the boundary and temperature terminal conditions of (9); for general nonzero \(y_0\), the initial temperature term is an appropriate dual functional, not an asserted \(L^2\) point trace of \(z\). For (2) put \(p=P-e^{-\mu t}h\): its zero-initial sources are \(F=Se^{-\mu t}h\), \(G=0\). From (10)–(12),
\[
\langle\mathcal Th,f\rangle_{L^2(J)}=\langle h,w_f(0)\rangle_{L^2(I)},\qquad
\boxed{\mathcal T^*f=\Pi_o w_f(0)}. \tag{13}
\]
No trace of \(z\) was used in the proof. Consequently \(\overline{\operatorname{ran}\mathcal T^*}=H\) iff \(\ker\mathcal T=\{0\}\).

The odd projection can be eliminated by solving the transposition problem on odd test pairs: \(z_o=\Pi_o z_f\), \(w_o=\Pi_o w_f\). Since the actual coefficients are even, (11) is preserved, and (13) becomes \(\mathcal T^*f=w_o(0)\). In the **formal** full-interval odd representation the boundary controls are \(z_o(t,0)=A_0\mathbf1_J f\), \(z_o(t,L)=-A_0\mathbf1_J f\). On the half interval \((0,L/2)\), they are \(z_o(0)=A_0\mathbf1_J f\), \(z_o(L/2)=0\); the factor 2 in full-interval odd inner products restores (13). These boundary values again denote transposition data, not independently established classical traces.

## 3. Active high-frequency quasi-static ansatz with a rigorous error

Let \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), and \((Y_n,P_n)\) solve (2) with \(h=\phi_n\). Define the **actual-coefficient** trial fields
\[
P_n^a(t,x)=e^{-\mu t}\phi_n(x),\qquad
Y_n^a(t,x)=\frac{e^{-\mu t}}{\kappa q_n^2}S(t,x)\phi_n(x). \tag{14}
\]
They are not a frozen half-line model: \(S(t,x)\) is the prescribed nonautonomous active-base coefficient, and \(M,B,\gamma\) remain in the residual. The dominant formal balance is \(-\kappa\partial_{xx}Y_n^a\approx SP_n^a\). The ansatz is in \(\mathcal E\), has zero spatial Dirichlet trace, and \(P_n^a\in H^1_tL^2\), by (6). It does **not** satisfy \(Y_n^a(0)=0\).

Direct distributional differentiation, justified by (6), gives
\[
\begin{aligned}
R_n&:=MY^a_{n,t}-\kappa Y^a_{n,xx}-BY_n^a-SP_n^a\\
&=\frac{e^{-\mu t}}{\kappa q_n^2}
\left[(M(S_t-\mu S)-BS-\kappa S_{xx})\phi_n-2\kappa S_x\phi_n'\right].
\end{aligned} \tag{15}
\]
Since \(\|\phi_n\|_\infty=\sqrt{2/L}\), \(\|\phi_n'\|_\infty=\sqrt{2/L}\,q_n\),
\[
\|R_n\|_{L^2_{t,x}}\le C\left(q_n^{-1}+q_n^{-2}\right),\qquad
\|Y_n^a\|_{L^2_{t,x}}\le Cq_n^{-2},\quad
\|Y_n^a(0)\|_{H^1_0}\le C(q_n^{-1}+q_n^{-2}). \tag{16}
\]
The \(BS\) term uses only \(B\in L^2_{t,x}\) and bounded \(S\); the \(S_x\) term is the leading \(O(q_n^{-1})\) residual. All products and traces are legitimate in the inherited spaces. The estimate is uniform in \(n\); finitely many small \(n\) are absorbed into the constant.

Set \(e_n=Y_n-Y_n^a\), \(r_n=P_n-P_n^a\). They satisfy the **exact coupled error system**
\[
Me_{n,t}-\kappa e_{n,xx}=Be_n+Sr_n-R_n,\qquad
r_{n,t}+\mu r_n=\gamma e_n+\gamma Y_n^a, \tag{17}
\]
with \(e_n(0)=-Y_n^a(0)\), \(r_n(0)=0\), \(e_n|_{\partial I}=0\). The established forced forward estimate yields
\[
\|e_n\|_{\mathcal E}+\|r_n\|_{H^1_tL^2_x}\le Cq_n^{-1}. \tag{18}
\]
The boundary derivative of the trial field exists in \(L^2_t\), and \(\phi_n(0)=0\), \(\phi_n'(0)=\sqrt{2/L}\,q_n\), so
\[
\boxed{\ k_n(t)=\mathcal T\phi_n(t)=\frac{2A_0\sqrt{2/L}}{q_n}e^{-\mu t}S(t,0)+\mathfrak r_n(t),\qquad
\|\mathfrak r_n\|_{L^2(J)}\le Cq_n^{-1}.\ } \tag{19}
\]
Thus **for the actual active system**, \(\|k_n\|_{L^2(J)}\le Cq_n^{-1}\), a stronger individual-column upper bound than the preceding \(q_n^{-1/2+\eta}\). This result remains conditional on (3)–(6) and the inherited forced estimate, not on an unverified numerical threshold. Importantly, the error is **the same order** as the displayed trial boundary term. Equation (19) is a controlled decomposition, not a proved leading asymptotic or a lower bound: cancellation with \(\mathfrak r_n\) is possible. The initial mismatch and the \(S_x\phi_n'\) residual are the explicit obstacles. The positive delay might suppress the former, but a uniform variable-coefficient delayed boundary smoothing estimate is not supplied here. The trial term depends on the boundary value of the *active* \(S(t,0)\) and on \(\phi'_n(0)\), while the true leading term is unknown; \(M\) enters the remainder and may contribute at leading order. No claim of an actual boundary-layer profile, triangular matrix, or exact individual nonvanishing follows. The ordinary continuous \(L^2\) endpoint trace of \(S\) follows from \(S\in C_tH^1\), not a pointwise evaluation of the heat equation.

### 3.1 Hilbert–Schmidt kernel and actual vector impulse response

The uniform bound on **each** column in (19) has a stronger consequence than compactness. Since \(\sum_n q_n^{-2}<\infty\),
\[
\sum_{n=1}^\infty\|\mathcal T\phi_n\|_{L^2(J)}^2<\infty. \tag{19a}
\]
Thus \(\mathcal T:H\to L^2(J)\) is Hilbert–Schmidt. In particular,
\[
\|\mathcal T(I-P_N)\|\le\left(\sum_{n>N}\|k_n\|_{L^2(J)}^2\right)^{1/2}\le C_L N^{-1/2}. \tag{19b}
\]
This is an operator-tail bound, independent of any finite rank computation; it improves the previously proved \(N^{-1/2+\eta}\), though it still gives no singular-value lower bound. Define
\[
K(t,x)=\sum_{n\ge1}k_n(t)\phi_n(x)\quad\text{in }L^2(J\times I),\qquad
\mathcal Th(t)=\int_I K(t,x)h(x)dx\quad\text{a.e. }t. \tag{19c}
\]
The equality follows first for finite sine sums and then for all \(h\in H\) by Hilbert–Schmidt convergence. For a.e. \(t\), \(K(t,\cdot)\in H\), and
\(\mathcal T^*f=\int_J f(t)K(t,\cdot)dt\) as an \(H\)-valued Bochner integral. Thus the actual delay-restricted adjoint memory reachable space is
\[
\overline{\operatorname{ran}\mathcal T^*}=\overline{\operatorname{span}}\{K(t,\cdot):t\in J\text{ outside a fixed null set}\}. \tag{19d}
\]
For example take the null set to exclude non-Lebesgue points of the \(H\)-valued \(K\). The forward inclusion follows from Bochner integration, while normalized interval controls give every such \(K(t)\) as a strong \(H\) limit of reachable states. Density is **still unproved**: (19d) identifies a concrete family whose completeness is the remaining question, rather than claiming its completeness. The kernel and impulse response are defined almost everywhere, not pointwise classically, and no time analyticity follows.

## 4. Controls, impulses, and a Gramian obstruction

For arbitrary nonzero \(h\in H\) and \(f\in L^2(J)\),
\[
\langle h,\mathcal T^*f\rangle=\int_J f(t)k_h(t)dt
=\int_0^T e^{-\mu t}\langle h,S(t)z_f(t)\rangle dt,\quad k_h=\mathcal Th. \tag{20}
\]
If \(k_h\ne0\), choosing \(f=k_h\) gives a strictly positive pairing; the missing statement is precisely that every nonzero \(h\) has \(k_h\ne0\). At an \(H\)-valued Lebesgue point \(t_0\) of the kernel \(K\) from (19c), normalized interval controls \(f_\varepsilon=\varepsilon^{-1}\mathbf1_{(t_0,t_0+\varepsilon)}\), with intervals contained in \(J\), satisfy \(\mathcal T^*f_\varepsilon\to K(t_0,\cdot)\) strongly in \(H\). However \(\|f_\varepsilon\|_2=\varepsilon^{-1/2}\to\infty\); these are approximate impulses, not uniformly bounded controls, and their existence does not prove completeness of the family.

The boundary-control Gramian is the bounded positive compact operator
\[
W=\mathcal T^*\mathcal T:H\to H,\quad
\langle Wh,h\rangle=\|\mathcal Th\|_{L^2(J)}^2,\quad
\ker W=\ker\mathcal T. \tag{21}
\]
Similarly \(\mathcal T\mathcal T^*\) acts on controls. If \(W\) were coercive in the \(H\)-norm on a dense linear subspace, continuity would extend the lower bound to all \(H\), contradicting compactness on infinite-dimensional \(H\). The same contradiction holds on any infinite-dimensional closed finite-codimensional subspace. Individual finite-dimensional subspaces may have positive constants, but none has been shown for actual coefficients. A weaker negative-Sobolev estimate or a smooth-class modulus is not ruled out, but has not been proved. The concrete missing adjoint theorem is:
\[
\forall\,0\ne h\in H\quad\exists f\in L^2(J):\quad
\int_0^T e^{-\mu t}\langle h,S(t)z_f(t)\rangle dt\ne0, \tag{22}
\]
where \(z_f\) is defined by (10). This is a full-time, equation-specific separation condition, not a claim that arbitrary boundary impulses are dense. Proving it only for \(h\in X\) would settle physical-class linear injectivity but not density in all \(H\).

## 5. Memory, moments, time dependence, and reconstruction

The exact ODE identity for every \(h\in H\) is
\[
P(t)=e^{-\mu t}h+\gamma\int_0^t e^{-\mu(t-r)}Y(r)dr. \tag{23}
\]
Thus the nonsmoothing component \(e^{-\mu t}h\) survives explicitly; it is coupled to an interior response. From (14), (18), \(P_n=e^{-\mu t}\phi_n+O_{H^1_tL^2_x}(q_n^{-1})\). In fact the earlier \(V'\)-energy estimate gives \(\|Y_n\|_{L^2_tL^2_x}\le Cq_n^{-1}\); the convolution in (23) then improves the memory correction to \(O_{H^1_tL^2_x}(q_n^{-1})\), still not an output separation theorem. From **known interior temperature** \(Y\), one can calculate the feedback term but not the unknown \(h\) from (23) unless \(P\) is also known. If additionally \(|S|\ge s_0>0\) on a strip and the interior \(Y_t,Y_{xx},Y\) and coefficients are known, the PDE gives \(P=(MY_t-\kappa Y_{xx}-BY)/S\) a.e.; then (23) recovers \(h\). Neither interior data nor such a global nonvanishing bound follows from endpoint flux alone, and the division is not valid where \(S\) vanishes.

For \(y_m(t)=\langle Y(t),\phi_m\rangle\), \(p_m=\langle P,\phi_m\rangle\), the exact modal system is
\[
\sum_m M_{nm}(t)\dot y_m+\kappa q_n^2y_n=\sum_m B_{nm}(t)y_m+\sum_m S_{nm}(t)p_m,\qquad
\dot p_n+\mu p_n=\gamma y_n,\quad p_n(0)=h_n. \tag{24}
\]
Here \(M_{nm}=\langle M\phi_m,\phi_n\rangle\), and similarly for \(B,S\); sums are understood through the actual strong-solution products, not as independently diagonal ODEs. Fourier truncations of \(Y\) converge in \(L^2_tH^s_x\), \(s<2\), and hence their boundary derivative sums converge in \(L^2(J)\) for \(s>3/2\). The slow ODE response is explicit but all off-diagonal coefficients remain. Dividing by \(M\) yields \(Y_t=(\kappa/M)Y_{xx}+(B/M)Y+(S/M)P\), not a diagonal equation in the sine basis. No time-dependent diagonalizing transformation with bounded invertibility, controlled derivative terms and output trace is proved.

The load is smooth, but the inherited coefficients only give \(S\) as in (6), \(B\in L^2_{t,x}\), and positive-time Sobolev improvements. No theorem here proves \(M,B,S\), the coupled state, or \(\mathcal Th\) analytic in time on \(J\); the \(L^2(J)\) flux is the established temporal space. Smooth loading alone does not establish base analyticity, and differentiation of the boundary trace is not licensed. The exact temporal family \(\{k_n\}\) is Bessel and tends to zero, but no independence, output completeness or \(\ell^2\)-synthesis injectivity is shown. Nonharmonic Fourier/Müntz theorems require an actual exponential family and applicable separation/completeness hypotheses; variable matrices and the memory feedback do not supply them. In (19) the candidate trial functions all share the same time profile, and the error is of the same order, so that expression is inadequate for proving distinguishability or non-distinguishability.

## 6. Endpoint lifting: a rigorous obstruction to bounded separation

For \(\ell(x)=1-2x/L\), \(h\in X\), \(h=h(0)\ell+g\) with \(g\in X_0:=H^2\cap H^1_0\cap H\), linearity gives the exact decomposition
\[
\mathcal Th=h(0)\mathcal T\ell+\mathcal Tg. \tag{25}
\]
Neither \(\mathcal T\ell\ne0\) nor injectivity of \(\mathcal T|_{X_0}\) has been verified on \(J\). An initial-time sign argument does not extend to delayed times without an additional theorem.

**Endpoint nonseparation theorem.** There is no bounded linear functional \(F\) on \(L^2(J)\) satisfying \(F(\mathcal Tg)=0\) for every \(g\in X_0\) but \(F(\mathcal T\ell)\ne0\). In particular no control \(f\in L^2(J)\) can produce a pairing \(\langle\mathcal Th,f\rangle=h(0)\) for every \(h\in X\).

**Proof.** Finite odd Dirichlet sine sums belong to \(X_0\) and are dense in \(H\). Since \(\mathcal T:H\to L^2(J)\) is bounded, \(\mathcal T(P_N\ell)\to\mathcal T\ell\) in \(L^2(J)\). Continuity of \(F\) gives the first statement; the second is the special case \(F(v)=\langle v,f\rangle\). □

Quantitatively, \(\ell_n=\sqrt{2L}/(\pi n)\); using the Hilbert–Schmidt tail bound (19b) and \(\|(I-P_N)\ell\|=O(N^{-1/2})\) gives
\[
\|\mathcal T\ell-\mathcal T(P_N\ell)\|_{L^2(J)}\le C N^{-1}. \tag{26}
\]
The approximants have zero endpoints and \(\|P_N\ell\|_{H^2}\) grows like \(N^{3/2}\). Thus this result does **not** say the two outputs are exactly equal, or that endpoint identification is impossible on an \(H^2\)-bounded class with a nonlinear/discontinuous or regularized procedure. It rules out the natural single bounded-control annihilator route on unrestricted \(X_0\). It also shows \(\mathcal T\ell\in\overline{\mathcal T(X_0)}\), whether or not \(\mathcal T\ell\) itself vanishes.

The sharper input tail \(\|(I-P_N)g\|\le q_{N+1}^{-2}\|g''\|\) is valid for \(g\in X_0\), but no actual lower singular-value estimate is known, so it cannot establish restricted injectivity. The original weak-initial physical class does not impose endpoint zero. Corner-classical conditions in the topology audit are nonlinear necessary compatibility relations for full initial states, not a proof that odd perturbations have zero endpoints or that their differences remain in a linear subspace. No extra endpoint condition is imposed here.

## 7. Exact kernel, nonlinear scope, and numerical protocol

Endpoint-compatible, interior-supported, or finite sine-combination inputs do not force \(SP=0\). For a finite combination, zero full-time output is equivalent to an exactly singular actual Gram, whose rank is unknown. A candidate in \(E=\ker D_\delta\) has zero delayed memory but may have nonzero delayed temperature and output. A joint zero restart state would be invisible, yet no nonzero such state is constructed. The abstract counterexample in the predecessor is not a physical trajectory. No nonzero \(h\in X\) satisfying (2) and zero flux on all \(J\) has been found, and no mathematical argument excludes one.

For nonlinear identification, one must first specify a genuine admissible \(H^2\) neighborhood or manifold, prove existence/uniqueness and positivity through \(T\), continuous delayed flux, and a Fréchet remainder estimate showing derivative \(\mathcal T\) in the chosen topology. Even if \(\mathcal T\) is injective, compactness makes the usual full-space bounded inverse theorem inapplicable, and injective derivative alone does not imply nonlinear local injectivity. A verified nonlinear two-point modulus on the admissible class, or a finite-dimensional chart with \(C^1\) map and injective restricted derivative, would be sufficient under the appropriate hypotheses; neither is established for the actual experiment.

No physical constants or numerical data were supplied, so **no numerical experiment or rank is claimed**. A reproducible diagnostic, with all units fixed, is:

```text
INPUT actual a,k,b,c,kappa,lambda,theta_*,L,A_0,g_* and initial/bath data
verify forward sufficient bounds or label the run conditional; T=10/lambda
solve the full nonlinear active base and its memory/mean equations
form M,B,S, including Q(y_b)_t, and quantify coefficient residuals
for each space/time mesh and independent output quadrature refinement:
    solve (2) for ell and for N odd sine inputs, with actual memory history
    compute full L2(delta,T) flux traces and Gram matrix G_N
    compute singular values of trace synthesis, not just point samples
    independently solve backward transposition discretization for test f
    compare integral_J f*(2 A_0 kappa Y_x(0)) with <h,Pi_o w(0)>
    compare ell output with zero-endpoint approximants P_N ell
    estimate base, PDE and ODE residuals, flux trace and quadrature errors
    report noise, discretization and infinite-tail uncertainty separately
```
Use meshes resolving wavelengths \(2\pi/q_n\) and parabolic times \(q_n^{-2}\), with independent refinement; do not infer exact rank from an SVD. For a rigorous finite \(N\) lower bound, enclose the exact continuous Gram in operator norm, e.g. \(\|G_N-\widehat G_N\|\le\varepsilon_G\) from validated residual/trace/coefficient and quadrature estimates, and then certify \(\lambda_{\min}(G_N)\ge\lambda_{\min}(\widehat G_N)-\varepsilon_G>0\). This proves only finite-section separation. Infinite-dimensional identification needs an independent certified tail/singular-value relation or the actual adjoint separation theorem (22); (19)'s single-column estimate and (26) do not supply either.

## 8. Primary-source theorem checks

The search was targeted, not exhaustive; absence of a directly transferable theorem is not a novelty proof.

* **Michel Duprez**, *Controllability of a 2×2 parabolic system by one force with space-dependent coupling term of order one*, [arXiv:1701.05315v1](https://arxiv.org/html/1701.05315v1), 2017, §§1, 2 and 5. The statement uses two diffusive equations on an interval, time-independent spatial couplings with Sobolev bounds and boundary or distributed control; the moment/Fattorini proof uses autonomous spectral structure. The actual second equation is an ODE and coefficients depend on time; its spectral theorem does not apply. Selected statement and proof steps were inspected, not every cited dependency.
* **Guillaume Olive**, *Boundary approximate controllability of some linear parabolic systems*, [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), 2026, Theorem 1.1 and appendix. The autonomous generator/compact-resolvent, complete-adjoint-root-vector and observation hypotheses support the root-space projection proof. They are not established for (11); the nondiffusive ODE component also makes compact resolvent nonautomatic. No time-analytic propagation is imported.
* **Dev Prakash Jha and Raju K. George**, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), 2026, Lemma 3.5: zero auxiliary initial memory, specified weights and moving interior control. The proof invokes an earlier ODE Carleman result; that dependency was not independently verified. It does not control our arbitrary memory from one boundary.
* **Yavar Kian, Diomba Sambou, Eric Soccorsi**, *Logarithmic stability inequality in an inverse source problem for the heat equation on a waveguide*, [arXiv:1612.07942v1](https://arxiv.org/html/1612.07942), 2016, Theorem 1.2 and §§4.1–4.2. The proof time-differentiates a scalar separated-source heat equation and uses homogeneous heat observability; data include an \(H^1_t\) Neumann norm. Here \(SP\) depends on the unknown coupled state, and only \(L^2_t\) flux is justified. The theorem cannot be transferred.

No primary theorem inspected establishes (22), an \(o(q_n^{-1})\) boundary remainder for the actual active coefficients, or injectivity of the physical memory map from the delayed trace. Inaccessible papers and uninspected proofs are not used as evidence.

## 9. Final decision map

| Question | Result | Proof or missing lemma | Consequence |
|---|---|---|---|
| Adjoint identity | **PROVED under inherited hypotheses** | (8)–(13), transposition with \(w(0)\in L^2\) | Exact projected memory control, with constants and parity. |
| Adjoint range density | **NOT ESTABLISHED** | Prove (22) for all nonzero \(h\in H\) | Full odd injectivity remains open. |
| Boundary-control Gramian | **CONSTRUCTED; trace class, no full coercivity** | (19a), (21), compactness and density argument | Impulse-response family exists; no \(H\)-norm lower bound on dense or finite-codimensional subspace. |
| PDE–ODE memory reconstruction | **CONDITIONAL** | (23); interior PDE division needs \(|S|\ge s_0\) and interior derivatives | Endpoint flux alone does not supply these data. |
| Temporal completeness | **NOT ESTABLISHED** | Need actual time regularity and coupled synthesis separation | Smooth load is not time analyticity of the base. |
| High-frequency leading term | **NOT ESTABLISHED; improved upper bound proved** | Actual ansatz (14)–(19), remainder only \(O(q_n^{-1})\) | Cannot derive lower bounds or mode separation from the trial term. |
| Endpoint/interior separation | **BOUNDED LINEAR SEPARATION IMPOSSIBLE** | Density and (26); no bounded control annihilates all \(X_0\) outputs while selecting \(\ell\) | Does not preclude nonlinear recovery on bounded smoothness classes. |
| Restricted \(H^2\) injectivity | **NOT ESTABLISHED** | Need (22) for \(X\), or a verified lower-bound/tail condition | Faster \(X_0\) tail alone is insufficient. |
| Exact physical invisible state | **NOT CONSTRUCTED** | Must satisfy actual coefficients and zero full trace | Approximate invisibility is not a counterexample. |
| Full odd-channel injectivity | **NOT ESTABLISHED** | Equation-specific boundary separation needed | Compactness alone decides neither way. |
| Nonlinear local identification | **NOT ESTABLISHED** | Domain, differentiability, and nonlinear two-point stability | Linearized injectivity would not suffice. |

**Final decision: REFORMULATE.** The immediate mathematically defensible route is either a delayed-strip estimate improving the actual boundary error in (19) to \(o(q_n^{-1})\) **together with a separate infinite-synthesis argument**, or a proof of the transposition separation statement (22) on the actual reachable graph. Neither an improved column bound nor a non-strict cone result solves that missing step. Dr. Gupta is the final decision-maker.
