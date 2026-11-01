# Sharp stability, independent proof audit, and nonlinear identifiability

**Final label: STRONGER SCHATTEN RESULT PROVED.** Under exactly the inherited actual-base and strong-forced-forward hypotheses stated below, the previously established two-level error bounds imply, by a one-dimensional multiplicative trace estimate,
\[
\|\rho_n\|_{L^2(J)}\le Cq_n^{-3/2},\qquad
s_n(\mathcal T)\le Cn^{-3/2}. \tag{1}
\]
In particular \(\mathcal T\in\mathcal S_{2/3,\infty}\), the weak endpoint class, and \(\mathcal T\in\mathcal S_p\) for all \(p>2/3\). This removes the previous \(\varepsilon\)-loss, without asserting \(\mathcal T\in\mathcal S_{2/3}\), a lower asymptotic, or a sharp result for the actual PDE. The latter three questions remain open. Section 3 gives the complete proof, including a dyadic singular-value argument and an endpoint counterexample **only for the abstract column assumptions**.

For the linearized map, the excluded \(H^2\) Hölder exponents remain precisely those \(>4/7\) that this argument can exclude; the endpoint is not disproved. Section 4 proves the general \(H^s\) result and identifies exactly what stronger estimate would exclude the endpoint. Section 6 proves several **conditional nonlinear** obstruction theorems, with different exponents depending on the remainder norm. The nonlinear assumptions and admissibility neighborhood are not established for the prescribed experiment, so no unconditional nonlinear transfer is claimed. Manufactured computations validate aspects of two numerical discretizations, not the physical experiment.

**Scope and governance.** The active nonzero \(\sin^2\) loading, model, physical constants, delay, initial topology and solution class are unchanged. All preceding reports are preserved. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is Arena's independent recalculation, not certification by an independent human. Direction 1 remains rejected as a foundational theory; Direction 2 remains **REFORMULATE**. No new foundational theory, novelty, manuscript, or publication priority is claimed.

## 1. Fixed system and hypotheses

Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), and \(Z=L^2(J)\). Odd/even refer to reflection about \(L/2\). The prescribed displacement is \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\). Define
\[
D=a_{\rm mat}+k,\ r=k/D,\ \alpha=a_{\rm mat}/D,\ \beta=b/D,\quad
\gamma=\lambda\beta,\ \mu=\lambda\alpha,\ d=b^2/D,\ Qv=v-\bar v.
\]
The active base is the actual solution, not an externally prescribed coefficient field. Its coefficients are
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b.
\]
For initial odd memory \(h\),
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\ P(\cdot,0)=h,\quad Y|_{x=0,L}=0,\quad
\mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{2}
\]
These are **not** endpoint conditions on \(h\) or \(P\). Linearized output equals the flux-difference channel with the frozen normalization; no nonlinear conclusion follows from it alone.

All actual theorems below assume the inherited base exists and stays positive, coefficients are even, \(0<m_0\le M\le m_1\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\),
\[
S\in C_tH^1_x\cap H^1_tL^2_x\cap L^2_tH^2_x, \tag{3}
\]
and the audited zero/inhomogeneous initial-data strong solution and forced estimates hold in \(H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_0)\) for temperature and \(H^1_tL^2_x\) for memory. Parity, uniqueness and trace maps are included. These conditions are inherited assumptions; their validity for the unspecified experimental parameters, positivity, and nonempty nonlinear admissible class are not established here.

Set \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin q_nx\), \(k_n=\mathcal T\phi_n\), \(a_J=2A_0\sqrt{2/L}e^{-\mu t}S(t,0)\), \(\Lambda h=\sum(h,\phi_n)/q_n\). The earlier audit defines \(Y_n^a=e^{-\mu t}S\phi_n/(\kappa q_n^2)\) and proves for \(e_n=Y_n-Y_n^a\)
\[
\|e_n\|_{L^2(0,T;H^1)}\le Cq_n^{-2},\qquad
\|e_n\|_{L^2(0,T;H^2)}\le Cq_n^{-1}. \tag{4}
\]
The constants are uniform in \(n\), including both the nonzero initial-temperature mismatch and memory source. We independently check their residual and norms in §3.1. Define \(\rho_n=2A_0\kappa e_{n,x}(0,\cdot)|_J\); then \(k_n=a_J/q_n+\rho_n\). All actual constants depend on the fixed base and material data, not on \(n\).

## 2. Independent audit of the previous theorem and examples

The four specified reports and both original Python files were inspected; no previous file was overwritten. Classifications are for the statements actually made, not their strengthened versions below.

| Item | Classification | Independent check / exact qualification |
|---|---|---|
| \(R=B_sD_s\) | CORRECT | For \(0<s<1\), choose \(\eta<1-s\). Then \(\sum q_n^{2s}\|\rho_n\|^2\le C\sum n^{2s-3+2\eta}<\infty\); \(B_s\phi_n=q_n^s\rho_n\) is Hilbert–Schmidt, and \(D_s\phi_n=q_n^{-s}\phi_n\). Equality holds first on finite sums and extends by continuity on \(H\). At \(s=1\) that argument fails; this is not a proof \(B_1\) exists. |
| Schatten product | CORRECT | \(D_s\in\mathcal S_r\) iff \(sr>1\), and Schatten Hölder gives \(1/p=1/2+1/r\). Letting \(s\uparrow1\), \(r\downarrow1/s\) reaches every \(p>2/3\); include larger \(p\) by nesting. Quasi-Schatten product inequalities remain valid for \(p<1\). Rank one lies in all \(\mathcal S_p\). |
| \(s_n=O(n^{-3/2+\varepsilon})\) | CORRECT | \(s_{2j-1}(B_sD_s)\le s_j(B_s)s_j(D_s)\le Cj^{-1/2-s}\); the rank-one perturbation shifts index by at most one. The constant depends on \(s,\eta\) and may diverge as \(s\uparrow1\); passing to the endpoint was not justified. New §3 supplies an independent endpoint proof. |
| Abstract threshold sharpness | CORRECT | The diagonal \(d_n=n^{-3/2}/\log(n+1)\) satisfies every \(n^{-3/2+\eta}\) column bound. Yet \(\sum d_n^{2/3}=\sum n^{-1}/\log(n+1)^{2/3}=\infty\). Add an arbitrary rank-one leading operator: if the sum belonged to \(\mathcal S_{2/3}\), subtraction of the rank-one operator would force the diagonal to belong too. Not a physical example. |
| Neighboring cancellation | CORRECT UNDER ADDITIONAL HYPOTHESES | \(z_n=\phi_n-(q_{n+1}/q_n)\phi_{n+1}\) has \(\Lambda z_n=0\), norm bounded above/below, and \(\|z_n\|_{H^s}\asymp q_n^s\) for fixed \(s>0\); the previous \(O(q_n^{-3/2+\eta})\) follows from the column bounds. It assumes (2)–(4). |
| \(4/7\) obstruction | CORRECT UNDER ADDITIONAL HYPOTHESES | \(h_n=cq_n^{-2}z_n\) has \(\|h_n\|_2\asymp q_n^{-2}\), output \(O(q_n^{-7/2+\eta})\), and bounded \(H^2\)-norm. For every \(\alpha>4/7\) take \(\eta>0\) with \(\alpha(7/2-\eta)>2\). This is a linearized full-state estimate on a ball containing zero, not nonlinear admissibility. |
| Modulo-kernel versus full-state | CORRECT | \(N=\ker\mathcal T\) is closed in \(H\). An \(H^2\)-bounded sequence has a weakly \(H^2\), strongly \(L^2\) convergent subsequence; bounded \(\mathcal T\) gives a qualitative modulus for \(\operatorname{dist}_H(h,N)\). For \(\|h\|_2\) instead, one additionally needs \(N\cap H^2=\{0\}\). The full kernel is not interchangeable with \(N\cap H^2\); no explicit modulus follows from compactness alone. |
| Abstract injective and noninjective examples | CORRECT | \(T_+=a\Lambda+D\) has \(D e_n=n^{-2}e_n\), hence is injective and has finite augmented distance \(n^{-2}\). For \(T_-=a\Lambda+D(I-v\otimes v)\), with unit infinite-support \(v\in\ker\Lambda\), \(\ker T_-=\operatorname{span}\{v\}\), and all finite augmented blocks are independent: a finite vector parallel to \(v\) is zero. With \(v_n\sim n^{-2}\), \(\sum_{j>N}v_j\rho_j=Dv_{>N}-(\sum_{j>N}v_j^2)Dv=O(N^{-3})\); the distance for fixed \(n\) is at most \(C_nN^{-3}\). These are abstract constructions. |

No fatal error in the eight main results was found. One presentation correction in the prior report: the sentence “The latter illustrates that normal equations lose precision” follows the newly added matrix-exponential test; it should refer to the **Schur/inverse comparison**, not the matrix-exponential test. The comparison alone is illustrative, not a quantified numerical error analysis. The prior use of strict \(H^{3/2+\eta}\) trace is valid but not optimal; the endpoint improvement below does not claim that derivative evaluation is bounded on \(H^{3/2}\).

## 3. Actual endpoint estimate and weak Schatten theorem

### 3.1 Independent residual and two-level inputs

Let \(A_n=e^{-\mu t}S\phi_n/(\kappa q_n^2)\), \(P_n^a=e^{-\mu t}\phi_n\). Direct differentiation gives the exact first-equation residual
\[
F_n^a=\frac{e^{-\mu t}}{\kappa q_n^2}\left(\left[M(S_t-\mu S)-BS-\kappa S_{xx}\right]\phi_n-2\kappa S_x\phi_n'\right). \tag{5}
\]
The leading oscillatory term is \(-2\sqrt{2/L}\,e^{-\mu t}S_x\cos(q_nx)/q_n\). Because \(S_x\in L^2_tH^1_x\), integration by parts against \(v\in H^1_0\) yields
\[
\|S_x\cos(q_n\cdot)\|_{L^2_tH^{-1}_x}\le Cq_n^{-1}\|S_x\|_{L^2_tH^1_x}. \tag{6}
\]
There is no boundary term: \(v\) vanishes at both endpoints. The other terms of (5) are \(L^2\), using \(S\in L^\infty\), \(B,S_t,S_{xx}\in L^2\). Hence \(\|F_n^a\|_{L^2_tL^2_x}\le Cq_n^{-1}\), \(\|F_n^a\|_{L^2_tH^{-1}_x}\le Cq_n^{-2}\). The ODE error forcing is \(\gamma A_n\), and the temperature initial mismatch \(-A_n(0)\) satisfies \(L^2\)-norm \(O(q_n^{-2})\), \(H^1\)-norm \(O(q_n^{-1})\). The audited weak-energy estimate and assumed strong forced estimate respectively yield exactly (4). We do not infer extra time regularity, bounded \(B_x\), a classical second-derivative trace, or delayed exponential decay.

### 3.2 Multiplicative trace: no \(\varepsilon\) needed

For every \(v\in H^1(0,L)\), averaging \(v(0)^2=v(x)^2-2\int_0^xv v'\) over \(x\) gives
\[
|v(0)|^2\le L^{-1}\|v\|_2^2+2\|v\|_2\|v'\|_2. \tag{7}
\]
Apply this for a.e. \(t\) to \(v=e_{n,x}(t,\cdot)\). Integrate in time and apply Cauchy–Schwarz:
\[
\|e_{n,x}(0,\cdot)\|_{L^2(0,T)}^2
\le C\|e_n\|_{L^2H^1}^2+C\|e_n\|_{L^2H^1}\|e_n\|_{L^2H^2}
\le C(q_n^{-4}+q_n^{-3}). \tag{8}
\]
Thus \(\|\rho_n\|_Z\le Cq_n^{-3/2}\). No critical \(H^{3/2}\to\mathbb R\) bounded trace is asserted: (7) is a **multiplicative estimate on functions already in \(H^2\)**, and integration uses both independent norm bounds. In particular, no estimate of how the old \(C_\eta\) behaves as \(\eta\downarrow0\) is needed. This improvement uses neither an \(S_{xx}(0)\) trace nor extra coefficient smoothness.

### 3.3 Weak endpoint singular values from column decay

**Theorem 1.** Suppose \(R:\ell^2\to Z\) has \(\|Re_n\|\le Cn^{-\beta}\), \(\beta>1/2\). Then \(s_n(R)\le C_\beta n^{-\beta}\); the same holds after adding finite rank. Applied to (8), \(\beta=3/2\), yielding (1) and \(\mathcal S_{2/3,\infty}\).

**Proof.** For integer \(N\), split off the first \(N\) columns (rank at most \(N\)). Let \(R_k\) contain columns with \(2^kN<n\le2^{k+1}N\). Then
\[
\|R_k\|_{\mathcal S_2}\le C(N2^k)^{1/2-\beta}. \tag{9}
\]
Choose \(0<\theta<2\beta-1\), \(m_k=\lfloor N2^{-\theta k}\rfloor\), for all \(k\le K\), where \(K\) is the largest index with \(N2^{-\theta K}\ge1\). Their sum is \(O(N)\), and \(s_{m_k+1}(R_k)\le\|R_k\|_{\mathcal S_2}/\sqrt{m_k+1}\le C N^{-\beta}2^{-k(\beta-1/2-\theta/2)}\). Approximate each block by a rank-\(m_k\) operator; the sum of their operator-norm errors is \(O(N^{-\beta})\). The remaining tail has Hilbert–Schmidt norm \(O((N2^K)^{1/2-\beta})\). Choose \(\theta\) sufficiently small that \((1+1/\theta)(\beta-1/2)\ge\beta\); then this tail is \(O(N^{-\beta})\). Combining the finite-rank approximants gives an approximant to \(R\) of rank \(O(N)\) and error \(O(N^{-\beta})\), proving the claimed rate. A finite-rank perturbation shifts indices. □

For the actual \(\beta=3/2\), the concrete choice \(\theta=1/2\) gives \(m_k\simeq N2^{-k/2}\), \(K\simeq2\log_2 N\), block errors \(CN^{-3/2}2^{-3k/4}\), and final tail \(O(N^{-3})\). Thus the earlier factorization's endpoint obstruction is overcome by block allocation, **not** by falsely claiming \(B_1\) is Hilbert–Schmidt. (For \(\mathcal S_{p,\infty}\), use the standard definition \(\sup_n n^{1/p}s_n<\infty\).)

### 3.4 What remains at the strong Schatten endpoint

Even the strengthened column bound does **not** imply \(\mathcal S_{2/3}\): take output \(Z=\ell^2(\{0,1,\ldots\})\), \(a=e_0\), \(\rho_n=n^{-3/2}e_n\), \(q_n=n\), and \(T=a\Lambda+R\). Then \(s_n(R)=n^{-3/2}\) and \(\sum s_n(R)^{2/3}=\sum1/n=\infty\); rank-one subtraction rules out \(T\in\mathcal S_{2/3}\). It also satisfies \(K_R\in L^2_tH^s_x\) in the sine-compatible scale for every \(s<1\), because \(\sum n^{2s-3}<\infty\). Thus this kernel regularity alone cannot settle the strong endpoint or improve the exponent. It is **not** a PDE coefficient or physical realization.

A sufficient extra condition is, for example, \(\sum_n\|\rho_n\|^{2/3}<\infty\), via the rank-one \(\mathcal S_p\) quasi-triangle inequality; \(\|\rho_n\|\le Cn^{-3/2}(\log(n+1))^{-\gamma}\) with \(\gamma>3/2\) suffices. Alternatively a kernel with \(L^2_tH^{1+\epsilon}_x\) regularity **in an appropriate spectral/trace setting** yields \(\mathcal S_{2/3}\) by factorization. None is derived from (3). More modest \(\rho_n=o(n^{-3/2})\) gives \(s_n=o(n^{-3/2})\) by the same block proof, but still need not yield strong endpoint summability. Actual \(s_n\) may decay faster; no actual lower bound or optimality follows from (1).

## 4. Stability exponent: three independent routes and sharpness limits

### 4.1 Adjacent cancellation and arbitrary \(H^s\)

For every \(s>0\), finite trigonometric sums obey \(\|z_n\|_{H^s}\asymp q_n^s\), by integer derivative estimates and Sobolev interpolation; lower bounds follow by duality/interpolation or localization of the two frequencies. No imposed endpoint condition is needed on the full \(H^s\) class. From (8),
\[
\Lambda z_n=0,\quad \|\mathcal Tz_n\|\le Cq_n^{-3/2},\quad
h_n=c_Rq_n^{-s}z_n,\quad \|h_n\|_2\asymp q_n^{-s},\quad
\|\mathcal Th_n\|\le C_Rq_n^{-(s+3/2)}. \tag{10}
\]
Thus on every nontrivial \(H^s\)-ball the full-state inequality \(\|h\|_2\le C\|\mathcal Th\|^\alpha\) fails for every
\[
\alpha>\frac{s}{s+3/2}. \tag{11}
\]
More generally, a cancellation bound \(\|Tz_n\|\le Cn^{-\beta}\) gives the threshold \(s/(s+\beta)\). If instead \(\|Tz_n\|=o(n^{-\beta})\), the **endpoint** \(\alpha=s/(s+\beta)\) also fails: the two sides have the same power but the right side has a vanishing factor. Likewise \(O(n^{-\beta}(\log n)^{-\gamma})\), any \(\gamma>0\), excludes the endpoint. The actual estimate (8) supplies only big-O; neither little-o nor the logarithm has been proved.

### 4.2 Modulus and logarithmic comparison

If a nondecreasing modulus \(\omega\) controls all inputs in the ball, choose \(n\asymp\varepsilon^{-1/(s+3/2)}\) large enough that \(\|\mathcal Th_n\|\le\varepsilon\). Then
\[
\omega(\varepsilon)\ge c_R\varepsilon^{s/(s+3/2)}\quad(\varepsilon\downarrow0). \tag{12}
\]
Consequently \(o(\varepsilon^{s/(s+3/2)})\) is impossible, and so are all higher Hölder exponents; equality in order is **not** excluded. A logarithmic modulus is much larger than this lower bound and is not ruled out, but neither is it justified. If \(\mathcal T\) has a nonzero smooth kernel vector, no full-state modulus vanishing at zero can hold. If \(\ker\mathcal T\cap H^s=\{0\}\), compactness of \(H^s\Subset L^2\) and closedness of its bounded ball under weak limits yield some full-state modulus; without this premise, one has the compactness modulus only for distance to the **full** \(L^2\) kernel. Our sequence has not been shown uniformly separated from that kernel, so (11) is not automatically a modulo-kernel obstruction.

### 4.3 Endpoint cannot be decided by column information alone

The abstract diagonal model \(T_+h=e_0\sum h_n/n+\sum n^{-3/2}h_ne_n\) satisfies the improved column estimate, is injective and has \(\|T_+h\|^2\ge\sum n^{-3}|h_n|^2\). On the spectral Sobolev ball \(\sum n^{2s}|h_n|^2\le R^2\), Hölder interpolation yields
\[
\|h\|_2\le R^{\frac{3/2}{s+3/2}}\|T_+h\|^{\frac{s}{s+3/2}}. \tag{13}
\]
Indeed write each \(|h_n|^2\) as \((n^{2s}|h_n|^2)^{\beta/(s+\beta)}(n^{-2\beta}|h_n|^2)^{s/(s+\beta)}\), \(\beta=3/2\), and apply Hölder. This establishes the endpoint on this **sine-compatible spectral subspace**, not on every physical \(H^s(I)\) function or the actual operator. Conversely \(T_-\) in §2 has the same (indeed faster) column bound but a nonzero \(\ell^2\) kernel; even when that vector is not \(H^2\), its existence shows that column bounds alone do not supply the needed lower estimate. The preceding theorem's \(4/7\) endpoint is consequently an open actual-system issue, not a proved sharp physical threshold.

An actual matching estimate would follow, on a spectral \(H^s\) class, from the missing **global lower bound**
\[
\|\mathcal Th\|_Z\ge c\left(\sum_n q_n^{-3}|h_n|^2\right)^{1/2}. \tag{14}
\]
This is much stronger than nonzero columns or finite-block rank and is not established. For full \(H^s(I)\), endpoint traces and the \(\ell(x)=1-2x/L\) component must be treated separately; one cannot identify the full Sobolev space with a Dirichlet spectral scale at critical indices.

## 5. General compact-observation theorem

**Theorem 2 (approximation-number obstruction).** Let \(X\hookrightarrow H\) be a compact embedding of Hilbert spaces, and \(T:H\to Z\) compact. Suppose for some \(s,\beta>0\) there are subspaces \(E_N\subset X\) of dimension at least \(2N\) with
\(\|h\|_X\le C N^s\|h\|_H\) on \(E_N\), and \(s_N(T)\le CN^{-\beta}\). Then on any nonzero \(X\)-ball every full-state modulus satisfies \(\omega(\varepsilon)\ge c\varepsilon^{s/(s+\beta)}\); hence no Hölder exponent above that ratio is possible. If \(s_N(T)=o(N^{-\beta})\), the endpoint Hölder estimate is impossible as well.

**Proof.** Let \(u_1,\ldots,u_N\) be right singular vectors corresponding to the largest singular values, padding the list arbitrarily if rank is smaller. There exists nonzero \(v_N\in E_N\cap\operatorname{span}\{u_1,\ldots,u_N\}^\perp\). Normalize \(\|v_N\|_H=1\). The min–max/SVD property gives \(\|Tv_N\|\le s_{N+1}(T)\), even if \(v_N\) has a kernel component. Put \(h_N=c_RN^{-s}v_N\): it belongs to the \(X\)-ball and has \(H\)-norm \(c_RN^{-s}\), while its output is \(O(N^{-(s+\beta)})\). Monotonicity of \(\omega\) and choosing \(N\asymp\varepsilon^{-1/(s+\beta)}\) proves the modulus bound; the little-o variant gives a contradiction at equality. □

For the actual problem, use \(X=H^s(I)\cap H\), \(E_N=\operatorname{span}\{\phi_1,\ldots,\phi_{2N}\}\); the inverse inequality follows for integer \(s\) from orthogonality of derivatives and for fractional \(s\) by interpolation. Theorem 1 supplies \(\beta=3/2\), giving (11) without using neighboring modes. The compact inclusion \(J_s:X\to H\) has \(s_n(J_s)=O(n^{-s})\) in one dimension, hence Fan's product inequality yields \(s_n(TJ_s)=O(n^{-(s+3/2)})\). This is an upper bound on compressed singular values, **not** a lower bound on \(\|Th\|\) for arbitrary constrained inputs; singular vectors of \(T\) need not align with the Sobolev scale. The dimension-intersection proof above is what relates the two spaces. Standard compact-operator instability arguments are compared in §9; the specialization is proved here rather than claimed novel.

## 6. Nonlinear map: rigorous implications and missing forward estimates

### 6.1 Exact form of the needed remainder

Let \(\mathcal F\) denote the actual nonlinear delayed boundary observation relative to the fixed active base, on an admissible local subset of \(H^2_o\); if both labeled fluxes or force are included, use the corresponding vector norm and verify the same differentiability/trace estimates for every component. Neither local existence on an open \(H^2\)-ball nor differentiability is established by the inherited linear forced theorem. A formal expansion cannot supply them.

For perturbations \(u=\theta-\theta_b\), \(p=p_{\rm base\ difference}\), let \(\Delta w=-\alpha p+\beta Qu\), \(\Delta E=rp_t\), with \(p_t+\mu p=\gamma Qu\) and the fixed mean strain unchanged. Subtracting the active base from its nonlinear equation produces the full-space linearization plus terms of the schematic exact quadratic form
\[
-d\,u\,Q u_t-b\,u\,\Delta E+k\lambda(\Delta w)^2, \tag{15}
\]
with signs depending on which side the residual is placed. Full-space \(Q\) is retained: nonlinear differences need not remain odd. The \(u_t\) term is quasilinear and cannot be discarded or replaced by a scalar potential. Assuming a **full-space** linearized forced estimate to the strong temperature/flux norm, plus a locally uniform nonlinear difference bound
\[
\|u\|_{\mathcal E}+\|p\|_{H^1_tH^1_x}\le C\|h\|_{H^2}, \tag{16}
\]
(15) is \(L^2_{t,x}\) with norm \(O(\|h\|_{H^2}^2)\): \(\mathcal E\hookrightarrow L^\infty_tH^1_x\hookrightarrow L^\infty_{t,x}\), \(u_t,p_t\in L^2\), and \(\Delta w\in L^\infty_{t,x}\). With zero initial remainder, the forced estimate and boundary trace give
\[
\|\mathcal F(h)-\mathcal F(0)-\mathcal Th\|_Z\le C\|h\|_{H^2}^2. \tag{17}
\]
This is a valid conditional derivation, not a claim that (16), the full-space forced estimate, or an open admissible ball have been proved. The nonlinear strong solution must also retain positivity and all original compatibility conditions; a priori formal compatibility is insufficient.

A potentially stronger tame result would be
\[
\|\mathcal N(h)\|_Z\le C\bigl(\|h\|_{L^2}^2+\|h\|_{L^4}^2\bigr). \tag{18}
\]
A sufficient route would be a uniform estimate \(\|u\|_{\mathcal E}\le C\|h\|_2\), \(\|p\|_{L^\infty_tL^4_x}\le C(\|h\|_4+\|h\|_2)\), \(\|p_t\|_{L^2_{t,x}}\le C\|h\|_2\), plus the full-space forced estimate; then the first two products in (15) are \(O(\|h\|_2^2)\) and the last is bounded by \(\|\Delta w\|_{L^\infty L^4}^2\). The memory formula \(p=e^{-\mu t}h+\gamma\int_0^te^{-\mu(t-r)}Qu(r)dr\) explains the \(L^4\) term and why an \(L^2\)-quadratic remainder is not automatic. The necessary nonlinear estimates, including uniform ellipticity/mass inversion, are not available from the present audit.

### 6.2 Differentiability alone: no local nonlinear Lipschitz inverse, conditionally

**Theorem 3.** Suppose \(\mathcal F\) is Fréchet differentiable at zero as a map from an open \(H^2_o\) neighborhood to \(Z\), with derivative \(\mathcal T|_{H^2_o}\), and all sufficiently small scalar multiples of each \(z_n\) are admissible. Then no local inequality \(\|h\|_2\le C\|\mathcal F(h)-\mathcal F(0)\|_Z\) can hold.

**Proof.** For each fixed \(z_n\), insert \(h=tz_n\), divide by \(|t|\), and let \(t\to0\). Differentiability gives \(\|z_n\|_2\le C\|\mathcal Tz_n\|_Z\), contradicting (10). This uses no uniform differentiability in \(n\). □

This conditional result covers a two-point Lipschitz estimate by choosing the base as one point. It does not prove nonlinear failure without the open-admissibility and differentiability hypotheses, and it does not imply noninjectivity.

### 6.3 Quadratic \(H^2\)-remainder scaling

Assume (17) and an admissible \(H^2\)-ball. Let \(h_n=q_n^{-2-r}z_n\), \(r>0\); then \(\|h_n\|_{H^2}=O(q_n^{-r})\to0\), \(\|h_n\|_2\asymp q_n^{-(2+r)}\), and
\[
\|\mathcal F(h_n)-\mathcal F(0)\|\le C\left(q_n^{-(r+7/2)}+q_n^{-2r}\right). \tag{19}
\]
To make the quadratic bound smaller than the linear upper bound choose \(r>7/2\); a Hölder estimate of exponent \(\alpha\) would then require \(\alpha\le(r+2)/(r+7/2)\). Letting \(r\downarrow7/2\) excludes every \(\alpha>11/14\). At \(r=7/2\), the bounds are of equal order and give the same strict threshold; the phrase “remainder smaller than the linear signal” means smaller than the **upper estimate**, not a lower bound on the unknown actual linear signal. If it cancels further, the contradiction only strengthens. Exponents \((4/7,11/14]\) and the endpoint are not ruled out by (17) alone.

If the tame estimate (18) also holds, take \(h_n=\varepsilon q_n^{-2}z_n\) with a fixed sufficiently small \(\varepsilon>0\). The sine functions have uniformly bounded \(L^4\) norms, so \(\|h_n\|_2+\|h_n\|_4=O(\varepsilon q_n^{-2})\), \(\|\mathcal N(h_n)\|=O(\varepsilon^2q_n^{-4})\), while \(\|\mathcal Th_n\|\le C\varepsilon q_n^{-7/2}\). Thus every nonlinear exponent \(>4/7\) is excluded under these **additional unverified** tame assumptions. The fixed sequence is small in \(H^2\) only because \(\varepsilon\) is chosen small; it need not converge to zero in \(H^2\). If convergence is required, take \(\varepsilon_n=q_n^{-r}\) with small \(r>0\) and optimize the strict exponent limit. No \(4/7\) endpoint claim follows.

An injective nonlinear map can have a noninjective, compact or nonsurjective derivative: \(F(x)=x^3\) is injective on \(\mathbb R\) but \(F'(0)=0\); \(F(x)_n=x_n/n\) on \(\ell^2\) is injective with compact, nonsurjective derivative. These are illustrations, not thermoviscoelastic models. Neither linearized kernel triviality nor its failure alone decides nonlinear local injectivity.

## 7. The spatial derivative \(S_x\), endpoints, and weak expansion

In the regularity class of (3), \(S_x\in L^2_tH^1_x\) has spatial endpoint traces for a.e. time. For the actual base, \(w_b=m-v_b-\alpha p_b+\beta Qy_b\), \(\theta_b=\theta_*+y_b\), hence weakly
\[
S_x=\lambda\alpha[-br\,(y_b)_x+2k\alpha(p_b)_x],\quad
(p_b)_x(t)=\gamma\int_0^te^{-\mu(t-r)}(y_b)_x(r)\,dr. \tag{20}
\]
We used \(k\beta=br\). The base regularity \(y_b\in\mathcal E\) gives the first identity in \(L^2_tH^1_x\) and the endpoint identity a.e. Reflection gives \(S_x(t,L)=-S_x(t,0)\), **not** \(S_x(t,0)=0\); the Dirichlet condition fixes temperature, not its normal derivative. The integral formula ties the endpoint derivative to past base heat flux. It supplies no global sign without a separate flux sign theorem.

If \(S_x\equiv0\), set \(f=(y_b)_x\). From (20), \(br f=2k\alpha\gamma\int_0^te^{-\mu(t-r)}f(r)dr\); since \(br\ne0\), Volterra uniqueness gives \(f=0\), so \(y_b=0\). Then \(p_b=0\), \(w_b=m-v_b\) is spatially constant, and the heat equation requires
\(-b\theta_*m'(t)+k\lambda(m(t)-v_b(t))^2=0\) a.e. For \(m(t)=g_*L^{-1}\sin^2(\pi t/T)\), near \(0\), \(m'(t)\sim 2(g_*/L)(\pi/T)^2t\) while \(m-v_b=O(t^2)\); the first term has a nonzero linear coefficient and the second is \(O(t^4)\). Thus \(S_x\not\equiv0\) on \((0,T)\times I\), conditional on the actual base and its equations. This does **not** prove nonvanishing on \(J\), a sign, or a lower bound for \(\rho_n\).

An explicit **abstract coefficient** example isolates the missing information: choose smooth even nonconstant \(g(x)\), a smooth nonzero \(\chi(t)\) supported in \((0,\delta/2)\), and \(S_{\mathrm{art}}(t,x)=S_0+\chi(t)g(x)\), with \(S_0
e0\). It has the stated regularity and a nonzero spatial derivative somewhere before the delay, but \((S_{\mathrm{art}})_x=0\) throughout \(J\). This example does not satisfy or purport to solve the active base equations, and does not show the physical coefficient has this form. It proves only that global nonvanishing plus the abstract regularity cannot by themselves supply a positive-time local lower bound.

A nonzero source does not imply a nonzero boundary trace of its solution: for any smooth compactly supported odd \(Y(t,x)\) in the interior, take the heat forcing \(F=MY_t-\kappa Y_{xx}-BY\) (and solve the forced memory equation if desired); \(F\) is nonzero while \(Y_x(0,t)=0\). This artificial construction is not a coefficient example or physical counterexample, but shows why norm nonvanishing alone cannot yield a boundary lower bound. In particular oscillatory residuals can be canceled by initial mismatch, feedback and opposite boundary contributions. Under extra \(S\in L^2H^3\), suitable temporal trace regularity and compatible initial data, the previous audit's corrected cosine trial is meaningful; under (3) its \(S_{xx}(0)\) term is not defined. A weak negative-norm version of (5) gives the proved endpoint upper bound (8) without any second endpoint derivative, but does **not** identify a next coefficient or an \(o(q_n^{-3/2})\) error. Establishing such an error, or directly \(\|\mathcal Tz_n\|=o(q_n^{-3/2})\), is the precise missing endpoint theorem.

## 8. Computational audit, independent solver, and reproducible results

### 8.1 Review and corrections

The original Galerkin state reshape places output initial modes in matrix columns and is consistent with \(Y(0)=0\), \(P(0)=I\). Odd sines have mean zero, so no \(Q\) is omitted from (2). The base scheme's \(Q_h=I-\mathbf1w^T\), interior mass \(cI+d\operatorname{diag}(\theta)Q_h\), pointwise \(p_t=-\mu p+\gamma Q_hy\), and reconstruction of \(M,B,S\) match the base equations under trapezoid quadrature. Endpoint values of base \(p\) are evolved and not set to zero. In the Galerkin scheme \(M_N\dot Y=B_NY+S_NP-\kappa\operatorname{diag}(q_n^2)Y\); stiffness is exact for an exactly integrated sine basis. The derivative trace uses \(q_n\sqrt{2/L}\) and the specified \(2A_0\kappa\) prefactor. Linear interpolation of coefficients and BDF error remain separate from coefficient/base error. The delayed time grid must contain \(\delta\) exactly; trapezoid weights are then applied. SVD projection is preferable to a normal-equation inverse, but near rank loss its residual/control and numerical rank are not certificates.

**Actual code error fixed:** for \(2N\) spatial cells, \(\sin(2\pi Nx/L)\) vanishes at every grid point, so the prior `len(x)>=2*N+1` guard accepted a singular/aliased highest mode. It now requires at least \(2N+1\) cells, still only an anti-alias lower limit. No previous physical result relied on this code: no actual physical data had been run. The base finite-difference solver's midpoint/temporal errors, origin of supplied data, physical admissibility, and convergence remain unverified.

`finite_difference.py` independently discretizes (2) with centered second differences and Crank–Nicolson, with second-order one-sided boundary flux; it accepts the same NPZ fields. It currently restricts **its trial inputs** to zero endpoint values (sine columns), not the physical input class. It interpolates coefficients at time midpoints, includes \(\delta\) in the delayed output by interpolation, and has no assumed state decoupling. `manufactured.py` adds a known artificial forcing to both equations and implements a separate BDF spectral comparison. `moment_diagnostics.py` reports SVD condition numbers, rank, finite moment residuals and leakage into available higher columns; the finite leakage is not the full infinite adjoint error. `time_resolution_demo.py` uses artificial time-series to expose output-grid quadrature sensitivity.

### 8.2 Manufactured forced example

All numbers in this section are **dimensionless manufactured software tests**, not material data or a physical active-base claim. Set \(L=T=A_0=1\), \(\kappa=0.6\), \(\gamma=0.4\), \(\mu=0.7\), \(M=1\), \(B=0.3\), \(S(x)=1+0.2\cos(2\pi x)\), \(\delta=0.1\), and
\[
Y=e^{-t}[t\sin(2\pi x)+0.15t^2\sin(4\pi x)],\quad
P=e^{-t}[(1+t)\sin(2\pi x)+0.2\sin(4\pi x)]. \tag{21}
\]
These satisfy zero endpoint temperature and initial \(Y=0\). Define \(F=MY_t-\kappa Y_{xx}-BY-SP\), \(G=P_t+\mu P-\gamma Y\); both are explicitly evaluated analytically in the script. The exact boundary signal is \(2A_0\kappa e^{-t}[2\pi t+0.6\pi t^2]\). This deliberately includes a nonzero manufactured ODE forcing \(G\) and is not the physical source-free ODE.

Executed with NumPy 2.4.6/SciPy 1.17.1, `python code/direction-2-moment-analysis/manufactured.py` inside the documented virtual environment. Spatial refinement with 2048 CN steps gave:

| Cells | \(Y(T)\) discrete \(L^2\) error | \(P(T)\) error | delayed flux \(L^2_t\) error | FD versus independent BDF spectral \(Y(T)\) |
|---:|---:|---:|---:|---:|
| 24 | 1.76621e-3 | 3.44580e-4 | 1.07064e-1 | 1.76621e-3 |
| 48 | 4.39534e-4 | 8.58463e-5 | 2.74482e-2 | 4.39534e-4 |
| 96 | 1.09764e-4 | 2.14419e-5 | 6.90525e-3 | 1.09764e-4 |
| 192 | 2.74388e-5 | 5.35811e-6 | 1.72913e-3 | 2.74388e-5 |

All errors fall by approximately four on halving \(\Delta x\); agreement follows because the 8-mode BDF spectral solution also matches the exact manufactured fields in the unit test. At 96 cells, combined final-state FD difference from the 2048-step reference for 16, 32, 64, 128, 256 steps was respectively \(1.37388\!\times10^{-4}\), \(3.43696\!\times10^{-5}\), \(8.58792\!\times10^{-6}\), \(2.14080\!\times10^{-6}\), \(5.28909\!\times10^{-7}\); the expected second-order temporal trend is observed before the reference floor. These comparisons are diagnostics, not rigorous enclosures.

### 8.3 Finite moment and output-resolution illustration

For the abstract infinite-kernel example, output truncation 2048 and 64 available columns produced the following for target \(1\) and moving target \(N\). Leakage uses only columns \(N+1,\ldots,64\):

| N | augmented condition | distance fixed | finite leakage fixed | distance moving | finite leakage moving |
|---:|---:|---:|---:|---:|---:|
| 4 | 218.4 | 1.3650e-2 | 3.5186 | 3.1033e-2 | 1.1167 |
| 8 | 2084 | 1.4381e-3 | 9.2084 | 1.0845e-2 | 0.7394 |
| 16 | 21695 | 1.3912e-4 | 25.011 | 3.2450e-3 | 0.5056 |

The fixed target constraint residual at \(N=16\) was \(4.54\times10^{-7}\), warning of finite-precision amplification. In the independent artificial time-series example, using 8 versus 256 output times changed the fixed-mode distance from 0.17039 to 0.13498, condition number from 51.22 to 57.06, and leakage to the two available extra columns from 0.0953 to 0.1405. These are neither physical data nor convergence proofs. Exact commands and source code appear in the package README.

### 8.4 Tests and reproducibility

Commands executed:

```text
python -m venv .venv
.venv/bin/pip -q install numpy scipy
.venv/bin/python -m unittest discover -s code/direction-2-moment-analysis -v
Ran 11 tests in 4.822s
OK
.venv/bin/python code/direction-2-moment-analysis/manufactured.py
.venv/bin/python code/direction-2-moment-analysis/moment_diagnostics.py --columns 64 --outputs 2048 --blocks 4 8 16
.venv/bin/python code/direction-2-moment-analysis/time_resolution_demo.py
```

Tests cover artificial manufactured spatial/boundary/memory convergence, temporal self-convergence, independent spectral/analytic agreement, alias-grid rejection, moment control, comparison of the original Galerkin implementation with the independent finite-difference solver on the same artificial source-free coefficient fields, and the five pre-existing tests. In that last comparison the delayed-flux discrepancies for 24, 48 and 96 cells were 0.0105254, 0.00268097 and 0.000682077, respectively (512 CN steps and 101 spectral output times). A physical run still requires actual parameters/base arrays, independent coefficient validation and separate error estimates; none were supplied.

## 9. Primary literature audit

This targeted search is not exhaustive, and publication novelty has not been verified. The theorem statements and indicated proof passages below were inspected in their primary texts; the theorems' cited dependencies were not independently audited. ArXiv version/date is given where a publication record was not independently established.

| Primary source | Exact theorem and assumptions | Relevance | Missing for the active model |
|---|---|---|---|
| Herbert Koch, Angkana Rüland, Mikko Salo, *On instability mechanisms for inverse problems*, Ars Inveniendi Analytica revised paper 1 (2025), [arXiv:2012.01855v4](https://arxiv.org/html/2012.01855), DOI 10.15781/kvf0-ds86 | Appendix A, esp. Propositions A.4/A.6 and A.4 comparison: singular values and assumptions on compact sets yield instability; aligned Hilbert scales can make the exponent sharp. | Establishes that these operator-instability ideas are standard, not a novelty claim. | The actual singular-vector/regularity alignment and lower bounds are unknown; the abstract framework does not establish PDE injectivity. |
| Darko Volkov, *Optimal decay rates in Sobolev norms for singular values of integral operators*, [arXiv:2309.00153v2](https://arxiv.org/html/2309.00153), 2023 | Theorem 1.1: for integer \(p\), bounded Lipschitz \(d\)-dimensional input and \(L^2\)-integrable \(H^p\) input-variable derivatives, \(s_n=o(n^{-p/d-1/2})\), with weighted \(\ell^2\) conclusion. Proof uses Neumann spectral regularity. | The input-kernel derivative route could be stronger if its **endpoint** hypotheses were established. | Only \(H^s\), \(s<1\), for the remainder is inherited; \(H^1\) is not established, and sine/physical endpoints must not be conflated. |
| Carlos Montalto, Plamen Stefanov, *Stability of Coupled-Physics Inverse Problems with internal measurements*, [arXiv:1306.1978v1](https://arxiv.org/html/1306.1978), 2013 | Theorem A.1 assumes an order-\(>1\) nonlinear remainder, a conditional stability estimate for the linearization, interpolation inequalities and derivative continuity between stated Banach spaces. | Shows why nonlinear transfer requires quantitative hypotheses. | Neither their linear lower bound nor all their Banach-space estimates are established for (2); their problem is an elliptic internal measurement. |
| Mourad Choulli, *Various stability estimates for the problem of determining an initial heat distribution from a single measurement*, [arXiv:1512.07421v1](https://arxiv.org/html/1512.07421), 2015 | Theorem 3.1 and preceding nondegenerate-point condition: scalar heat, a fixed sensor with a quantitative sine condition, positive-measure time set, and an \(H^2\) bound imply a logarithmic estimate from an \(L^\infty\)-time measurement. | Illustrates that logarithmic recovery can coexist with severe smoothing. | No analogous scalar heat semigroup, point nondegeneracy, or \(L^\infty\)-time observation has been proved for the coupled active model. |
| Ze Li, Zhiyuan Li, Zhi Zhou, *Inverse Heat Source Problems from Boundary Flux and Interior Observations on Sets of Low Hausdorff Dimension*, [arXiv:2609.10071v1](https://arxiv.org/html/2609.10071), 2026 | Theorem 1.3: scalar separated source \(g(t)f(x)\), holomorphic sector extension of \(g\), \(\sigma>d/4\), spectral prior and boundary-geometric condition yield double-log recovery from delayed \(\partial_t\partial_\nu u\). Proof uses spectral inequality and analytic continuation. | An especially close delayed-boundary stability comparison. | Active \(S(t,x)P\) is not separated; the model supplies neither analytic continuation nor the measured time derivative nor those spectral hypotheses. |

The 1977 Birman–Solomyak paper is foundational for singular-number estimates, but its full primary proof was not independently accessed here; the checked Volkov paper discusses it. These comparisons do not establish that the new endpoint consequence in §3 is original.

## 10. Final decision and exact next target

1. **Schatten:** \(p>2/3\) remains the strongest *strong* Schatten range proved; the improved weak endpoint \(\mathcal S_{2/3,\infty}\) and loss-free \(O(n^{-3/2})\) are now proved conditionally for the actual operator.
2. **Strong endpoint:** \(\mathcal S_{2/3}\) is not established; it does not follow from even the strengthened abstract column bound.
3. **Singular exponent:** \(3/2\) is optimal for the abstract class of column bounds, not proved sharp for the actual PDE.
4. **\(4/7\):** all exponents \(>4/7\) are excluded for linearized recovery on any nonzero \(H^2\) ball; no matching actual lower estimate is known.
5. **Endpoint \(4/7\):** not ruled out. An actual \(o(q_n^{-3/2})\) cancellation, or a positive logarithmic improvement, would rule it out.
6. **General \(H^s\):** exponents \(>s/(s+3/2)\) and moduli \(o(\varepsilon^{s/(s+3/2)})\) are excluded for full linearized recovery; weaker moduli remain possible. Modulo-kernel conclusions require a kernel-distance lower bound.
7. **Nonlinear transfer:** Fréchet differentiability plus an admissible neighborhood conditionally rules out local Lipschitz recovery. A verified \(H^2\)-quadratic remainder would also exclude exponents \(>11/14\); the stronger tame \(L^2/L^4\) remainder would transfer all \(>4/7\). None of these additional nonlinear assumptions has been proved for the actual experiment.
8. **Nonlinear injectivity:** may coexist with compact or noninjective derivative and with linear instability; it remains unknown here.
9. **\(S_x\):** its exact Volterra identity and nonvanishing somewhere in the full time-space cylinder follow conditionally from nonzero loading, but no sign, delayed nonvanishing, remainder lower bound, or next asymptotic is proved.
10. **Single next target:** prove the actual weak-asymptotic estimate \(\|\mathcal Tz_n\|_Z=o(q_n^{-3/2})\), with full pre-delay memory and inherited low-regularity coefficients. This would exclude the linearized \(4/7\) endpoint; a complete proof must handle the initial mismatch, time-dependent coupling and boundary trace, not infer it from nonzero \(S_x\). If it fails, construct an actual admissible counterexample or derive a different decisive lower estimate. Dr. Gupta makes the final decision.
