# Independent mathematical audit and sharp observability analysis

**Date:** 1 November 2026. **Overall decision: REFORMULATE.** The active inverse problem is meaningful, but neither full odd injectivity nor an exact physical invisible profile is established. This audit confirms the preceding high-frequency bound and Schur reduction under the stated *conditional* base hypotheses; it strengthens the \(H^2\) tail analysis and the short-time memory estimate. It also gives an explicit abstract counterexample proving that the high-frequency estimate, positive every-order finite Gram matrix, and even a stronger smoothing estimate cannot by themselves establish infinite-dimensional injectivity. The counterexample is **not** a physical system or a counterexample to the active model. No mathematical priority or new foundational continuum theory is claimed.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is an independent recalculation by Arena of the previous report's mathematics, **not** independent human certification. Direction 1 remains rejected; this report concerns the fixed Direction-2 inverse boundary problem, not a new constitutive theory.

## 1. Exact setting and audit scope

The immediately preceding report, the active-base regularity audit, existence and admissible-topology reports, the coupled-boundary, delayed-adjoint and compact-quotient investigations were inspected. Take \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\). The displacement is the fixed active \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\); all original material constants and signs are retained. Put
\[
D=a+k,\quad r=k/D,\quad \alpha=a/D,\quad\beta=b/D,\quad
\gamma=\lambda\beta,\quad\mu=\lambda\alpha,\quad d=b^2/D,\quad Qv=v-\bar v.
\]
The active symmetric base gives the actual even coefficients
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{1}
\]
Let \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), \(X=H^2(I)\cap H\), where oddness is reflection about \(L/2\). The odd input has no imposed endpoint values. For \(h\in H\),
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad Y(0)=0,\ P(0)=h,\quad Y(t,0)=Y(t,L)=0,\quad
\mathcal Th=2A_0\kappa Y_x(\cdot,0)|_J. \tag{2}
\]
Initial-time and spatial-boundary conditions are different; no Dirichlet condition is imposed on \(P\). The physical class is \(X\), whereas extension to \(H\) is a linear analytic device. The available sufficient condition \(0<|g_*|/L<s_*\) is not numerically verified for the fixed amplitude; every forward assertion here assumes the inherited base/solution hypotheses rather than asserting unconditional existence or positivity.

Specifically, the base audit and forward theory give
\[
0<m_0\le M\le m_1,\ M,S\in L^\infty,\ M_x\in L^\infty_tL^2_x,\ B\in L^2_{t,x},\quad
\|Y\|_{\mathcal E}+\|P\|_{H^1_tL^2_x}\le C_E\|h\|_2, \tag{3}
\]
\(\mathcal E=H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\). The constant \(C_E\) is finite but not numerically certified. From \(p_{b,t}+\mu p_b=\gamma Qy_b\), \(p_b(0)=0\), \(w_b=m-v_b-\alpha p_b+\beta Qy_b\), and \(y_b\in C_tH^1_0\), one obtains \(w_b\in L^\infty_tH^1_x\) and hence
\[
C:=S/M\in L^\infty_tH^1_x,\quad A:=\kappa/M,\quad A_x\in L^\infty_tL^2_x,\quad 0<a_0:=\kappa/m_1\le A. \tag{4}
\]
There is no global assumption \(B\in L^\infty_tL^2_x\), \(A_t\in L^\infty\), or analyticity. Norm constants depend on the fixed units and parameters and cannot be assigned numerical values without the missing data. We write \(\|\cdot\|\) for \(L^2(I)\) unless specified, and \(\|v\|_V=\|v_x\|\).

## 2. Re-derivation of Theorem A

### 2.1 Multipliers and parity

For \(a\in H^1(I)\), \(v\in H^1_0(I)\), one-dimensional Sobolev embedding and Poincaré give
\[
\|(av)_x\|_2\le\|a\|_\infty\|v_x\|_2+\|a_x\|_2\|v\|_\infty
\le C_L\|a\|_{H^1}\|v_x\|_2. \tag{5}
\]
The trace of \(av\) is zero. In (2) \(C\) is even and \(v\) odd, so \(Cv\in V\); this parity is essential if \(V'\) denotes the dual of the odd space rather than of all \(H^1_0\). Thus \(\|CP\|_{V'}\le C_L\|C\|_{H^1}\|P\|_{V'}\) by duality, even when \(P\) has no endpoint trace. This verifies the multiplier assertion. The hypotheses actually needed for this part are evenness and \(C\in L^\infty_tH^1_x\), or any weaker multiplier assumption giving the same uniform norm.

### 2.2 Energy, with integrability visible

For a.e. \(t\), divide (2) by \(M\), multiply by \(Y\), and integrate. Since \(Y\in H^1_tL^2_x\cap L^2_tH^2_x\), \(A\in L^\infty\cap H^1_x\), and \(Y\in H^1_0\), integration by parts has no boundary term and gives
\[
\tfrac12(\|Y\|^2)' +\int A|Y_x|^2
=-\int A_xY_xY+\int (B/M)Y^2+\langle P,CY\rangle_{V',V}. \tag{6}
\]
For \(u\in H^1_0(I)\), \(\|u\|_\infty^2\le2\|u\|\|u_x\|\) and \(\|u\|_4^2\le C_L\|u\|^{3/2}\|u_x\|^{1/2}\). Thus for any \(\varepsilon>0\), with constants depending on \(\varepsilon,L,m_0\),
\[
\begin{aligned}
|\int A_xY_xY|&\le C\|A_x\|_2\|Y_x\|^{3/2}\|Y\|^{1/2}
 \le\varepsilon\|Y_x\|^2+C_\varepsilon\|A_x\|_2^4\|Y\|^2,\\
|\int (B/M)Y^2|&\le m_0^{-1}\|B\|_2\|Y\|_4^2
 \le\varepsilon\|Y_x\|^2+C_\varepsilon\|B\|_2^{4/3}\|Y\|^2,\\
|\langle P,CY\rangle|&\le C_L\|C\|_{H^1}\|P\|_{V'}\|Y_x\|
 \le\varepsilon\|Y_x\|^2+C_\varepsilon\|C\|_{H^1}^2\|P\|_{V'}^2.
\end{aligned} \tag{7}
\]
The exponents \(4\) and \(4/3\) are the Young-conjugate powers, not assumptions that \(B\) is uniformly bounded. A sufficient condition for the estimate is \(\|A_x\|_2^4,\|B\|_2^{4/3},\|C\|_{H^1}^2\in L^1(0,T)\). The actual bounds (3)–(4) imply these on the finite interval; no claim is made that they are mathematically necessary or optimal.

Let \(\mathcal A_V:V\to V'\) be the Riesz isomorphism induced by \(\int u_xv_x\). Since \(P\in H^1_tH\subset H^1_tV'\), testing the ODE in the Hilbert \(V'\) inner product gives
\[
\tfrac12(\|P\|_{V'}^2)' +\mu\|P\|_{V'}^2
=\gamma(Y,P)_{V'}\le\tfrac{|\gamma|}{2}(c_P^2\|Y\|^2+\|P\|_{V'}^2), \tag{8}
\]
where \(\|Y\|_{V'}\le c_P\|Y\|\), \(c_P=L/(2\pi)\) on odd functions. Adding (6)–(8) with \(3\varepsilon\le a_0/2\), and discarding favorable damping,
\[
E'(t)+a_0\|Y_x\|^2\le F(t)E(t),\quad E=\|Y\|^2+\|P\|_{V'}^2,\quad
F=C\{1+\|A_x\|_2^4+\|B\|_2^{4/3}+\|C\|_{H^1}^2\}\in L^1(0,T). \tag{9}
\]
Thus \(E(0)=\|h\|_{V'}^2\) and Gronwall yield
\[
\|Y\|_{L^\infty_tL^2_x}+\|Y\|_{L^2_tH^1_0}+\|P\|_{L^\infty_tV'}
\le C_-(a_0,L,\gamma,\int_0^T F)\|h\|_{V'}. \tag{10}
\]
For \(h\in H\) this is justified directly, not only formally: \(Y\in C_tH^1_0\), \(A_xY_xY\) and \(BY^2\) are integrable by the strong bounds and (7), and \(P\in H^1_tV'\). The Hilbert chain rule applies to \(Y\in H^1_tL^2\) and to \(P\). The weak spatial product rule follows by approximating \(A(t,\cdot)\) in \(H^1\) and \(Y(t,\cdot)\) in \(H^2\cap H^1_0\); the limits are dominated by the above norms. No \(M_t\) appears because the divided equation was tested. Extension to \(V'\) inputs would require an independent weak-solution construction; the bound is only asserted here for \(h\in H\).

### 2.3 Trace and interpolation

Let \(3/2<s<2\). For a.e. \(t\), Sobolev interpolation and Hölder in time give
\[
\|Y\|_{L^2_tH^s_x}\le C_{s,L}
\|Y\|_{L^2_tH^1_x}^{2-s}\|Y\|_{L^2_tH^2_x}^{s-1}
\le C_{s,L}C_-^{2-s}C_E^{s-1}\|h\|_{V'}^{2-s}\|h\|^{s-1}. \tag{11}
\]
The endpoint trace \(|u_x(0)|\le C_{s,L}\|u\|_{H^s}\) requires the **strict** inequality \(s>3/2\); it is not asserted at \(s=3/2\). Taking \(s=3/2+\eta\), \(0<\eta<1/2\), gives the predecessor's estimate
\[
\|\mathcal Th\|_{L^2(J)}\le C_\eta\|h\|_{V'}^{1/2-\eta}\|h\|^{1/2+\eta}. \tag{12}
\]
For \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(q_n=2\pi n/L\), and odd sine projection \(P_N\),
\(\|\phi_n\|_{V'}=q_n^{-1}\) and \(\|(I-P_N)h\|_{V'}\le q_{N+1}^{-1}\|h\|\), so
\[
\|\mathcal T\phi_n\|\le C_\eta q_n^{-1/2+\eta},\qquad
 e_N=\|\mathcal T(I-P_N)\|\le C_\eta q_{N+1}^{-1/2+\eta}. \tag{13}
\]
**Audit verdict:** mathematically valid under (3)–(4) and the inherited strong forward estimate. The original proof's phrase “multiplication by any \(a\in H^1\) acts on \(V'\)” needs the parity qualification in §2.1; arbitrary nonsymmetric multipliers need not preserve odd \(V\). It did immediately note even base coefficients, so this is a clarified domain qualification, not a failure of the actual estimate. No active leading term or lower bound follows.

## 3. Sharp endpoint and finite-section tails

### 3.1 The unrestricted claim is correct

For \(s>1/2\), the continuous endpoint trace and midpoint oddness imply \(h(L)=-h(0)\). Define
\[
\ell(x)=1-2x/L,\quad a=h(0),\quad g=h-a\ell. \tag{14}
\]
Then \(g\) is odd and has zero traces, and \(\|g\|_{H^s}+|a|\le C_{s,L}\|h\|_{H^s}\); the trace constant grows as the critical exponent \(s\downarrow1/2\), and depends on the chosen dimensional \(H^s\) norm and \(L\). Direct integration gives
\[
\ell_n=\langle\ell,\phi_n\rangle=\frac{2\sqrt{2/L}}{q_n}=\frac{\sqrt{2L}}{\pi n},\qquad
\|(I-P_N)\ell\|^2=\frac{2L}{\pi^2}\sum_{n>N}\frac1{n^2}. \tag{15}
\]
The integral comparison \((N+1)^{-1}\le\sum_{n>N}n^{-2}\le N^{-1}\) proves two-sided order \(N^{-1/2}\), for a smooth, endpoint-nonzero \(h\). Thus no better uniform exponent can hold on unrestricted \(H^s_o\), even for \(s>2\).

For \(1/2<s<1\), \(g\in H^s_0(I)\), the closure of \(C_c^\infty(I)\) in \(H^s\), equivalently the zero-trace subspace in this range. Its Dirichlet sine coefficients satisfy \(\sum q_n^{2s}|g_n|^2\le C_{s,L}\|g\|_{H^s}^2\), hence \(\|(I-P_N)g\|\le Cq_{N+1}^{-s}\|g\|_{H^s}\). At \(s=1\), Parseval gives \(\sum q_n^2|g_n|^2=\|g_x\|^2\); for \(s>1\), the \(H^1\) estimate suffices. Combining with (15) gives the predecessor's claimed \(C_{s,L}N^{-1/2}\) bound for **all** \(s>1/2\). The critical space at \(s=1/2\) is not covered; zero trace alone at that exponent is not a well-defined substitute for the Lions–Magenes weighted space. No extrapolation through higher Dirichlet fractional-domain critical indices is required for this proof.

### 3.2 Stronger result for the physical \(H^2\) topology

For every \(h\in X\), \(g=h-h(0)\ell\in H^2\cap H^1_0\cap H\). Integration by parts twice gives \(\langle g'',\phi_n\rangle=-q_n^2g_n\), so Parseval yields the exact estimate
\[
\boxed{\ \|(I-P_N)h\|\le |h(0)|\frac{\sqrt{2L}}{\pi\sqrt N}
+q_{N+1}^{-2}\|h''\|.\ } \tag{16}
\]
This refines the previous report for every actual physical-class input and shows exactly which boundary trace causes the slower rate. If \(h(0)=h(L)=0\), then \(\|(I-P_N)h\|\le q_{N+1}^{-2}\|h''\|\); this \(N^{-2}\) bound is uniform and sharp in operator norm on bounded \(H^2\cap H^1_0\) sets, tested by appropriately normalized \(\phi_{N+1}\). It is **not** a claim that the original physical weak-initial class has zero endpoint values. The topology audit imposes no such condition; its corner-classical compatibility is nonlinear and is not equivalent to this Dirichlet condition. No extra compatibility has been inferred.

The refined lifting can also be built into finite sections without pretending \(\ell\) is orthogonal to the sines. Let \(Z_N=\mathbb R\times P_NH\) have norm \((|a|^2+\|v\|^2)^{1/2}\), \(L_N(a,v)=a\ell+v\), and \(\tau_N=\inf_{\|(a,v)\|=1}\|\mathcal T L_N(a,v)\|\). Since \(\ell\) is not a finite sine sum, \(L_N\) is injective; however \(\tau_N\) may be zero and may become badly conditioned as sines approximate \(\ell\) in \(L^2\). When \(\tau_N>0\), writing \(g_N=P_Ng\), \(r_N=(I-P_N)g\), gives
\[
\|h\|\le \|L_N\|\tau_N^{-1}\|\mathcal Th\|+
\left(1+\|L_N\|e_N/\tau_N\right)q_{N+1}^{-2}\|h''\|. \tag{17}
\]
Indeed \(\tau_N\|(a,g_N)\|\le\|\mathcal Th\|+e_N\|r_N\|\). If actual certified \(\tau_{N_j}>0\) and \((1+\|L_{N_j}\|e_{N_j}/\tau_{N_j})q_{N_j+1}^{-2}\to0\), (17) proves separation of the full \(X\) class without artificially setting endpoint values to zero. No such certificates are known. \(\|L_N\|\le\sqrt{\|\ell\|^2+1}\) with the stated product norm (the scale of \(a\) must be chosen consistently in physical units).

## 4. A decisive impossibility result for the information-only strategy

The preceding finite-section inequality is correct, but its unverified condition cannot be deduced merely from compactness, the active-system upper estimates, and positivity of all finite Gram matrices. The following proof gives a concrete counterexample to that **inference**, not to (2).

Let \(v=\sqrt3\sum_{n\ge1}2^{-n}\phi_n\), so \(\|v\|=1\), \(v\in H^m\cap H^1_0\) for every \(m\), and \(v\notin P_NH\) for any \(N\). Let \(D\phi_n=q_n^{-1}\phi_n\), choose any isometry \(U:H\to L^2(J)\), and define the abstract compact operator
\[
T_{\rm abs}=UD(I-v\otimes v). \tag{18}
\]
Here \((v\otimes v)h=\langle h,v\rangle v\). Since \(D\) is injective and compact, \(\ker T_{\rm abs}=\operatorname{span}\{v\}\), containing a nonzero smooth odd, zero-endpoint function. Nevertheless, \(\ker T_{\rm abs}\cap P_NH=\{0\}\), so every finite Gram matrix is strictly positive definite. Moreover
\[
\|T_{\rm abs}h\|\le\|h\|_{V'}+\|v\|_V\|Dv\|\,\|h\|_{V'}\le C\|h\|_{V'}, \tag{19}
\]
which is **stronger** than (12), using \(\|h\|_{V'}\le c_P\|h\|\). For the tail, \(\|D Q_N\|=q_{N+1}^{-1}\) and \(\|Q_Nv\|=2^{-N}\), so
\[
e_N^{\rm abs}\le q_{N+1}^{-1}+\|Dv\|2^{-N}=O(N^{-1}),\qquad
 e_N^{\rm abs}\ge\|T_{\rm abs}\phi_{N+1}\|\ge q_{N+1}^{-1}-\sqrt3\,2^{-N-1}\|Dv\|. \tag{20}
\]
Thus \(e_N^{\rm abs}\asymp N^{-1}\) for large \(N\). Since \(T_{\rm abs}v=0\),
\[
\sigma_N^{\rm abs}\|P_Nv\|\le e_N^{\rm abs}\|Q_Nv\|=e_N^{\rm abs}2^{-N},\quad
\frac{e_N^{\rm abs}}{\sigma_N^{\rm abs}}\ge 2^N\|P_Nv\|. \tag{21}
\]
The predecessor's ratio times \(N^{-1/2}\) diverges; even an \(N^{-2}\) physical-tail factor cannot overcome this example. Every finite column is nonzero and every finite family independent, yet an exact smooth infinite combination vanishes. The operator is an abstract construction using an isometry, not the true \(\mathcal T\), and it neither proves nor disproves its kernel.

**Scientific consequence:** no proof depending only on (12), compactness, all-order finite rank and the Fourier-tail estimates can close actual injectivity. Some active-equation-specific input is indispensable. In particular, the *smallest missing lemma for the previous sufficient route* is a bound on actual \(\sigma_{N_j}\) relative to \(e_{N_j}\) and the admissible-class tails, e.g. the precise limit in its conditional criterion, not merely a pointwise nonvanishing estimate. For the lifted approach the corresponding quantity is \(\tau_N\) in (17).

## 5. Actual Gram, moment coupling, and the unresolved lower bound

For \(Y_n,P_n\) the actual solutions with \(h=\phi_n\), \(k_n=2A_0\kappa Y_{n,x}(0,\cdot)|_J\), the exact Gram is
\[
G_{mn}=4A_0^2\kappa^2\int_\delta^T Y_{m,x}(0,t)Y_{n,x}(0,t)dt,\qquad
\sigma_N^2=\lambda_{\min}(G_N). \tag{22}
\]
This is well-defined by the strong trace but no entries, sign of determinant, or \(\sigma_N>0\) are known. Projection of the actual PDE gives the exact matrix system
\[
\sum_m M_{nm}(t)\dot y_m+\kappa q_n^2y_n
=\sum_m B_{nm}(t)y_m+\sum_m S_{nm}(t)p_m,\quad
\dot p_n+\mu p_n=\gamma y_n, \tag{23}
\]
where all matrix elements are multiplication-operator pairings with \(\phi_n\). Time-dependent \(M_{nm}\) multiplies \(\dot y_m\); \(S_{nm}\), \(B_{nm}\) need not be diagonal, and \(B\) has only the global \(L^2\) control. The sine series of the solution and its endpoint derivative converge in the previously established trace topology, but vanishing of their sum does not imply vanishing of individual terms. Uniform \(H^1\) multipliers give some off-diagonal decay in coefficient-difference indices, but do not provide a diagonal temporal family, a comparison with the *smallest* singular value, or a sufficiently small relative remainder. For any \(N\), even nonzero individual columns would not prove their independence.

The exact adjoint formula \(\langle f,k_n\rangle=\langle\Pi_o w_f(0),\phi_n\rangle\) gives the same missing statement: for each nonzero \(h\), find \(f\in L^2(J)\) with \(\int e^{-\mu t}\langle S(t)h,z_f(t)\rangle dt\ne0\). There is no verified biorthogonal family, triangularity or relative off-diagonal error estimate for (23). A diagonal approximation alone would require \(\|R_N\|<\sigma_{\min}(D_N)\) uniformly in the manner needed for (11), including the infinite tail; neither side is bounded in this way. No actual finite-dimensional independence or lower estimate is asserted.

## 6. Delayed-memory Schur analysis, independently derived

With \(Y[h]\) from (2),
\[
D_\delta h=e^{-\mu\delta}h+Kh,\qquad
Kh=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y[h](r)dr. \tag{24}
\]
The Bochner integral lies in \(H^2\cap H^1_0\cap H\), because \(Y\in L^2_tH^2_x\); hence \(K:H\to H\) is compact. From (10),
\[
\|Kh\|_{H^1_0}\le |\gamma|\sqrt\delta\,C_-\|h\|_{V'},\qquad
\|KQ_N\|_{H\to H}\le C_K/q_{N+1}, \tag{25}
\]
where \(C_K\) includes the \(H^1_0\to L^2\) embedding factor and \(Q_N=I-P_N\). This independently verifies the claimed smoothing estimate and identifies dependencies. The constants can in principle be written in terms of the Gronwall integral (9), fixed embedding/trace constants, and the base norms, but a usable numerical value requires verified coefficient bounds and unit normalization. No numerical smallness follows from abstract existence.

Write \(d_0=e^{-\mu\delta}>0\). For \(C_K/q_{N+1}<d_0\), on \(Q_NH\)
\[
D_{QQ}=d_0I+Q_NKQ_N,\qquad \|D_{QQ}^{-1}\|\le(d_0-C_K/q_{N+1})^{-1}. \tag{26}
\]
This is the Neumann-series bound. Decompose \(h=v+w\), \(v\in P_NH\), \(w\in Q_NH\); the tail row of \(D_\delta h=0\) gives \(w=-D_{QQ}^{-1}Q_ND_\delta v\). The remaining row is
\[
F_Nv=0,\quad F_N=P_ND_\delta P_N-P_ND_\delta Q_ND_{QQ}^{-1}Q_ND_\delta P_N. \tag{27}
\]
Therefore \(v\mapsto v-D_{QQ}^{-1}Q_ND_\delta v\) is a bijection from \(\ker F_N\) onto \(\ker D_\delta\), and the same block solution with arbitrary right-hand side proves \(D_\delta\) invertible iff \(F_N\) is invertible. The inverse in (27) is infinite-dimensional and must itself be certified: \(P_ND_\delta P_N\) alone is **not** the exact test. Compact perturbation of a nonzero scalar identity yields Fredholm index zero, and if \(h\in\ker D_\delta\) then \(h=-d_0^{-1}Kh\in H^2\cap H^1_0\cap H\). These statements are valid.

### 6.1 Sharper short-time sufficient condition

Set \(M_P=\sup_{0\le t\le\delta}\|P[h](t)\|/\|h\|\le C_E\). Test the heat equation by \(Y_t\). Using \(M\ge m_0\), \(\|Y\|_\infty\le\sqrt L\|Y_x\|\), Young's inequality and \(Y(0)=0\),
\[
\frac\kappa2\frac d{dt}\|Y_x\|^2+\frac{m_0}{2}\|Y_t\|^2
\le \frac1{m_0}\big(L\|B(t)\|_2^2\|Y_x\|^2+\|S\|_\infty^2\|P\|^2\big). \tag{28}
\]
Gronwall and the integral of (28) imply, for \(0\le t\le\delta\),
\[
\int_0^t\|Y_t\|^2dr\le C_{\delta}\,t\|h\|^2,\qquad
\|Y(t)\|\le\sqrt t\left(\int_0^t\|Y_t\|^2dr\right)^{1/2}\le\sqrt{C_\delta}\,t\|h\|. \tag{29}
\]
One possible finite \(C_\delta\) is obtained from \(m_0,\kappa,L,\|S\|_\infty,C_E,\int_0^\delta\|B(r)\|_2^2dr\) by the displayed Gronwall steps; constants are nonnegative and dimensionful, and no coefficient is set to zero. Hence
\[
\boxed{\ \|K\|\le |\gamma|\sqrt{C_\delta}\int_0^\delta e^{-\mu(\delta-r)}r\,dr
\le |\gamma|\sqrt{C_\delta}\,\delta^2/2.\ } \tag{30}
\]
If the **actual** right-hand side is less than \(e^{-\mu\delta}\), then \(D_\delta\) is invertible and \(\operatorname{Re}\langle D_\delta h,h\rangle\ge(d_0-\|K\|)\|h\|^2\). This is a verifiable sufficient condition in principle, not verified from the unspecified fixed parameters; constants may be large and depend on \(\delta\). It does not change \(\delta\) or claim that its numerical smallness alone suffices. The exact identity
\(\langle D_\delta h,h\rangle=d_0\|h\|^2+\gamma\int e^{-\mu(\delta-r)}\langle Y(r),h\rangle dr\)
contains an uncontrolled signed cross term. A constant symmetrizer that cancels the heat–ODE coupling would have to handle time/space-dependent \(S/M\), its derivatives and the \(B\) term; no such coercive identity is verified. \(S\gamma\ge0\), even on the whole pre-delay interval, gives cone comparison, not a positive quadratic form on signed \(h\).

If \(D_\delta\) were invertible, the reachable delayed pair would be the graph \((UD_\delta^{-1}p,p)\). Boundary output would still be the compact graph map \(p\mapsto\mathcal R_\delta(UD_\delta^{-1}p,p)\), whose kernel is unproved; invertibility of the memory coordinate is not boundary observability.

## 7. Alternative exact routes and why they do not yet close

**Volterra elimination.** For \(h\in H\), the exact Bochner identity is
\[
P(t)=e^{-\mu t}h+\gamma\int_0^t e^{-\mu(t-r)}Y(r)dr,
\quad MY_t-\kappa Y_{xx}-BY-\gamma S\int_0^te^{-\mu(t-r)}Y(r)dr=Se^{-\mu t}h. \tag{31}
\]
With scalar zero-initial source solution \(\mathscr H:L^2_{t,x}\to\mathcal E_0\), define \(\mathscr VY=\mathscr H(\gamma S\int_0^te^{-\mu(t-r)}Y(r)dr)\). The preceding arbitrary-forcing argument gives bounded \((I-\mathscr V)^{-1}\) on \(\mathcal E_0\), and the exact observation \(\mathcal T=\mathscr B(I-\mathscr V)^{-1}\mathscr H(Se^{-\mu t}\cdot)\). This solves the forward problem but does not make \(\mathscr B\) injective on that source range; it does not diagonalize the active coefficients. It is not a scalar temporal Volterra equation for the endpoint flux.

**Restart and two-time identity.** For \(t\ge\delta\), \(P(t)=e^{-\mu(t-\delta)}D_\delta h+\gamma\int_\delta^te^{-\mu(t-r)}Y(r)dr\), while \(Y(\delta)=Uh\). For \(t_1<t_2\), \(e^{\mu t_2}P(t_2)-e^{\mu t_1}P(t_1)=\gamma\int_{t_1}^{t_2}e^{\mu r}Y(r)dr\). This controls only a difference *if the interior temperature is known*; neither interior temperature nor the snapshot is measured. The homogeneous ODE component cancels from the identity, so multiple intervals alone do not bound it.

**Transposition, whole delayed trace.** For forward zero-initial forced pairs with sources \(F,G\in L^2_{t,x}\), the functional \(2A_0\kappa\int_J f y_x(0)dt\), \(f\in L^2(J)\), gives \((z,w)\in L^2_{t,x}^2\) and
\[
-\partial_t(Mz)-\kappa z_{xx}-Bz-\gamma w=0,\qquad -w_t+\mu w-Sz=0,\quad w(T)=0,\quad
\mathcal T^*f=\Pi_o\int_0^T e^{-\mu t}S(t)z(t)dt. \tag{32}
\]
The boundary control is interpreted by the residual transposition identity, with formal \(z(0,t)=2A_0\mathbf1_Jf\), \(z(L,t)=0\); it is not a classical trace claim. Density of the projected memory range would prove injectivity, but no construction separates every nonzero \(h\) in (32). The full time trace is used, not finite samples. No strict Hopf or sign-cone assertion replaces density.

**Boundary weak identity.** For fixed \(\psi\in H^2(I)\), actual solutions satisfy a.e. in time
\[
\langle MY_t,\psi\rangle-\kappa\langle Y,\psi''\rangle
+\kappa Y_x(0)\psi(0)-\kappa Y_x(L)\psi(L)=\langle BY+SP,\psi\rangle. \tag{33}
\]
Odd symmetry makes the two derivatives equal. Zero flux does not remove the interior \(BY+SP\), so (33) is not scalar homogeneous unique continuation. No backward theorem with the required independent ODE source and actual coefficient regularity has been verified. The established Volterra representation, dual moment identity and entire-interval boundary data remain exact, but none controls \(h\) by flux without an additional equation-specific separation theorem.

## 8. Exact candidate search and nonlinear implications

An endpoint-compatible profile or a smooth odd profile supported strictly inside \((0,L)\) has no reason to make the distributed source \(SP\) vanish. A finite high-frequency combination has zero flux on all of \(J\) only if its actual Gram is singular; no such singularity is established. The abstract kernel vector in §4 is **not** a trajectory of (2). An element of the actual \(E=\ker D_\delta\) is smooth enough for \(X\) but may have nonzero delayed temperature \(Uh\) and flux. If both \(Uh=0\) and \(D_\delta h=0\), it is invisible, but no nonzero such state is found. A general state in \(\ker\mathcal T\) need not be in \(E\). The necessary and sufficient adjoint orthogonality \(\int e^{-\mu t}\langle S h,z_f\rangle dt=0\) for every \(f\) is an exact characterization, not an explicit solution. Cancellation of \(e^{-\mu t}h\) against the feedback term is possible algebraically but has not been shown to satisfy the actual coupled PDE and full delayed boundary trace. Approximate invisibility from (13) does not construct an exact invisible state.

To define nonlinear \(\mathcal F\), one needs an actual neighborhood (or a precisely specified admissible manifold/subset) of the base in physical \(H^2\), with unique active-load solutions through \(T\), positivity, uniform strong-temperature estimates and a continuous \(L^2(J)\) flux map. On an open \(H^2\) neighborhood, Fréchet differentiability at the base additionally requires a controlled nonlinear residual \(\|\mathcal F(h)-\mathcal F(0)-\mathcal Th\|_{L^2(J)}=o(\|h\|_{H^2})\), derivable only after bounding all nonlocal products and the difference of solutions uniformly. For a non-open corner-compatible set, ordinary Fréchet differentiability on an open space cannot simply be asserted; use a proved extension or manifold charts and tangent directions. The necessary facts are not established by the linear system alone.

An injective derivative, even a compact one, does not in general imply local nonlinear injectivity. A suitable sufficient hypothesis is a proved **two-point** bound \(\|h_1-h_2\|_H\le\Omega(\|\mathcal F(h_1)-\mathcal F(h_2)\|)\), \(\Omega(r)\to0\), on an actual admissible neighborhood or compact smoothness class. Alternatively, on a finite-dimensional admissible chart, \(C^1\) regularity and a verified injective restricted derivative give local separation (project the output to a suitable finite-dimensional image and apply the finite-dimensional inverse theorem). Neither is established for the unrestricted physical problem. Compactness prevents a full-space \(L^2\)-bounded inverse of the derivative, but does not itself exclude injectivity or a weaker nonlinear modulus.

## 9. Targeted primary-source inspection

Search and direct theorem/proof checks are limited and not a priority or exhaustive literature determination. No unavailable text is represented as verified.

* Y. Kian, D. Sambou, E. Soccorsi, *Logarithmic stability inequality in an inverse source problem for the heat equation on a waveguide*, [arXiv:1612.07942v1](https://arxiv.org/html/1612.07942), 2016, Theorem 1.2 and §§4.1–4.2: scalar \(\partial_t-\Delta\), a separated source, waveguide geometry, a priori spatial constraints, and \(H^1_t\) measured Neumann data. The proof differentiates in time and uses a homogeneous heat observability estimate. Our \(SP\) depends on the coupled state, and our output is only known in \(L^2(J)\); its coefficient/time-differentiability and initial nondegeneracy assumptions do not transfer.
* A. Halanay and L. Pandolfi, *Approximate controllability and lack of controllability to zero of the heat equation with memory*, [arXiv:1404.2745v1](https://arxiv.org/html/1404.2745), 2014, Theorem 2 and §3: a \(C^1\) convolution kernel multiplying the Laplacian, fixed scalar spatial operator, and admissibility of boundary controls. The proof transforms the controllability equation with an invertible scalar Volterra operator and checks endpoint reachability. The active source is lower-order PDE–ODE coupling with variable \(M,B,S\) and unknown initial memory; the observed quantity differs.
* G. Olive, *Boundary approximate controllability of some linear parabolic systems*, [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), 2026, Theorem 1.1 and appendix: autonomous generator, compact resolvent and complete adjoint root vectors; the proof uses spectral projections and resolvent analyticity. Nonautonomous active coefficients and an ODE state do not satisfy these hypotheses by assertion. No finite-time spectral density conclusion is imported.
* D. P. Jha and R. K. George, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), 2026, Lemma 3.5 and its cited proof: zero auxiliary initial memory, special moving interior control geometry and weight hypotheses. The proof relies on a cited earlier moving-control estimate whose proof was not audited. Our arbitrary unknown memory and one-endpoint observation do not meet the displayed setup.
* H. Lhachemi, C. Prieur, E. Trélat, *Boundary control of heat-heat cascades*, [arXiv:2506.10497v1](https://arxiv.org/html/2506.10497), 2025, §§2–3 and appendix: two autonomous heat components with constant coefficients and boundary coupling; explicit eigensystem and generalized-eigenvector calculations yield spectral-mode tests. We inspected the eigenvector proof and spectral reduction; the actual second component has no diffusion and the base is nonautonomous. Those formulas and Riesz-basis properties do not transfer.

These sources do not establish a high-frequency leading boundary term, finite-section lower bound or adjoint density for (2). No specifically matching primary theorem for the exact Schur certificate was located and checked; the block argument in §6 is elementary and is not claimed novel. Search results and abstract-only matches were not used to claim priority or applicability.

## 10. Decision table

| Mathematical question | Independent audit verdict | Corrected theorem or missing step | Scientific consequence |
|---|---|---|---|
| High-frequency bound | **VERIFIED, conditional on inherited base/forward hypotheses** | (5)–(13); multiplier must preserve parity, trace needs \(s>3/2\) | Actual tail upper rate, no lower rate or leading term. |
| Fractional Fourier tail | **VERIFIED** | \(s>1/2\); endpoint lifting and critical trace qualification | \(N^{-1/2}\) is sharp unrestricted. |
| Physical \(H^2\) tail | **STRENGTHENED** | Exact boundary-lift estimate (16), \(N^{-2}\) for zero endpoints | Faster remainder after retaining the endpoint degree of freedom; no extra physical condition assumed. |
| Finite sections imply injectivity | **FALSE AS A GENERAL INFERENCE** | Explicit abstract smoothing operator (18)–(21) has positive all-order Grams and smooth kernel | The actual proof must use more than upper estimates and finite ranks. |
| Conditional infinite-dimensional criterion | **CORRECT, PREMISE UNVERIFIED** | Actual relative singular-value/tail estimate, or lifted (17), remains missing | No actual identification theorem follows. |
| Memory smoothing / Schur theorem | **VERIFIED** | (25)–(27); tail inverse included, not raw finite matrix | Exact finite certificate in principle; values absent. |
| Delayed-memory invertibility | **NOT ESTABLISHED** | Sufficient bound (30) must be evaluated for fixed data | Fredholmness alone does not prove it. |
| Active boundary graph separation | **NOT ESTABLISHED** | Need a direct output separation lemma for (23), (31), or (32) | Even invertible memory map would not settle it. |
| Exact nonzero invisible physical input | **NOT CONSTRUCTED** | Must satisfy actual (2) and zero flux on all \(J\) | Abstract example is not a physical counterexample. |
| Full odd injectivity / adjoint density | **NOT ESTABLISHED** | Need a separating control or equivalent actual-system theorem | Open; compactness does not answer it. |
| Nonlinear local identification | **NOT ESTABLISHED** | Neighborhood, differentiability and nonlinear two-point estimate | Linearized injectivity alone is insufficient. |
| New foundational continuum theory | **REFORMULATE** | No new physical principle | Direction 2 remains an inverse problem. |

**Next research decision:** do not repeat finite-rank positivity, compactness, or the same snapshot estimate as a substitute for separation. Either (i) prove/certify a lower singular-value bound together with the exact tail ratio on the actual active equations, using the lifted \(H^2\) estimate where useful, or (ii) construct a nonautonomous boundary-control separation theorem for the actual reachable graph. Equation-specific estimates, certified constants and the actual nonzero load are essential. The choice and final scientific decision belong to Dr. Gupta.
