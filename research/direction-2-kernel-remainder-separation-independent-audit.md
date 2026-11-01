# Independent audit: boundary asymptotics and actual kernel remainder separation

**Date:** 1 November 2026. **Decision: REFORMULATE.** The sharper expansion and kernel traces survive the calculations below **under the explicit inherited active-base and strong-forward assumptions**, which have not been verified for the prescribed experiment. They do not prove injectivity. The principal new observation here is an exact two-part separation criterion: injectivity of the remainder on a codimension-one subspace is necessary but is not enough; a specific additional range-exclusion condition is also necessary. Neither condition is established for the actual coefficients. This is a research audit by Arena, not certification by a separate human auditor. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. Direction 1 remains rejected; no new foundational continuum theory or demonstrated novelty is claimed.

## 1. Fixed problem and conditional hypotheses

On \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), retain the actual even active base with prescribed nonzero loading \(g_*\sin^2(\pi t/T)\), not an equilibrium or independently chosen coefficients. Set
\[
D=a_{\rm mat}+k,\quad r=k/D,\quad \alpha=a_{\rm mat}/D,\quad \beta=b/D,\quad
\gamma=\lambda\beta,\quad \mu=\lambda\alpha,\quad d=b^2/D,\quad Qv=v-\bar v,
\]
where \(a_{\rm mat}\) is the material parameter called \(a\) in the preceding report. The actual coefficients are
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b.
\]
For reflection-odd \(h\in H=L^2_o(I)\), with \(V=H^1_0(I)\cap H\), the exact linearized system is
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\ P(\cdot,0)=h,\ Y(0,t)=Y(L,t)=0,
\quad \mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{1}
\]
No endpoint condition is imposed on \(h\) or \(P\). We assume \(M,B,S\) real and even, constants \(m_0,m_1>0\), and
\[
m_0\le M\le m_1,\quad M_x\in L^\infty(0,T;L^2),\quad B\in L^2((0,T)\times I),\quad
S\in C_tH^1_x\cap H^1_tL^2_x\cap L^2_tH^2_x. \tag{2}
\]
The resulting \(S\in L^\infty_tH^1_x\subset L^\infty_{t,x}\), \(A=\kappa/M\), \(A_x\in L^\infty_tL^2_x\), and \(M^{-1},S/M\in L^\infty_tH^1_x\). Also assume the inherited forced strong-forward theorem: for \(F,G\in L^2_{t,x}\), \(y_0\in V\), \(p_0\in H\), the odd solution of the forced version of (1) is unique and
\[
\|y\|_{H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_0)}+\|p\|_{H^1_tL^2_x}
\le C_E(\|y_0\|_{H^1}+\|p_0\|_2+\|F\|_2+\|G\|_2). \tag{3}
\]
These are sufficient hypotheses for this audit, not asserted minimal or verified experimentally. Their base derivation uses the inherited active-base class, not a proof of global existence, positivity, or nonempty admissibility. The sufficient small-load condition has not been numerically checked. Constants may depend on this fixed base and physical quantities; none is fitted here.

## 2. Oscillation and full residual, including parity

Give \(V\) norm \(\|v_x\|_2\), and \(V'\) its real Hilbert dual. For any \(a\in H^1(I)\), \(v\in H^1_0(I)\), and \(q_n=2\pi n/L\), the product \(av\in H^1_0(I)\), so weak integration by parts gives
\[
\int_I a\cos(q_nx)v\,dx=-q_n^{-1}\int_I\sin(q_nx)(a_xv+av_x)\,dx.
\]
One-dimensional embeddings and Poincaré imply
\[
\|a\cos(q_nx)\|_{H^{-1}(I)}
\le C_Lq_n^{-1}(\|a_x\|_2+\|a\|_{H^1})\le C_L' q_n^{-1}\|a\|_{H^1}. \tag{4}
\]
The bound is uniform in \(n\); it requires no trace of \(a\), because \(v\) vanishes at both endpoints. It remains true on restricting tests to \(V\). If \(a=S_x\), then \(S_x\) is reflection-odd and \(\cos(q_n(L-x))=\cos(q_nx)\), so \(S_x\cos(q_nx)\) is odd, as required. The same calculation applied for almost every \(t\), followed by integration, gives the identical uniform bound in \(L^2_tV'\) from \(S_x\in L^2_tH^1_x\).

For an even \(c\in H^1\), multiplication maps \(V\to V\) and \(V'\to V'\), by \(\|(cv)_x\|_2\le \|c\|_\infty\|v_x\|_2+\|c_x\|_2\|v\|_\infty\); dual multiplication is defined by \(\langle cF,v\rangle=\langle F,cv\rangle\). The uniform \(H^1\) bound for \(1/M\) follows from \((1/M)_x=-M_x/M^2\); no derivative of \(F\) or \(M_t\) is needed. In particular \(\|F/M\|_{V'}\le C\|F\|_{V'}\).

With \(\phi_n=\sqrt{2/L}\sin(q_nx)\), let
\[
P_n^a=e^{-\mu t}\phi_n,\qquad Y_n^a=e^{-\mu t}S\phi_n/(\kappa q_n^2).
\]
The product is in the strong temperature class; \(Y_n^a\) vanishes at both ends but generally not at \(t=0\). Its exact residual in the first equation is
\[
F_n^a={e^{-\mu t}\over\kappa q_n^2}
\{[M(S_t-\mu S)-BS-\kappa S_{xx}]\phi_n-2\kappa S_x\phi_n'\}. \tag{5}
\]
The bracket except the last term is \(L^2_{t,x}\), using only \(B\in L^2\) and \(S\in L^\infty\). The derivative term has an extra \(q_n\) in \(L^2\) but, by (4), not in \(V'\). Thus, after adjusting constants for finitely many modes,
\[
\|F_n^a\|_{L^2_tL^2_x}\le Cq_n^{-1},\quad
\|F_n^a\|_{L^2_tV'}\le Cq_n^{-2},\quad
\|Y_n^a\|_{L^2_{t,x}}+\|Y_n^a(0)\|_2\le Cq_n^{-2},\quad
\|Y_n^a(0)\|_V\le Cq_n^{-1}. \tag{6}
\]
Here \(S(0)\in H^1\) is essential for the initial mismatch. Multiplication by \(M^{-1}\) preserves (6)'s negative-norm rate. No \(B\in L^\infty_tL^2_x\), \(S_t\in L^\infty\), or derivative of \(B\) was used.

## 3. Independent two-level estimate

For odd strong solutions of
\[
My_t-\kappa y_{xx}=By+Sp+F,\qquad p_t+\mu p=\gamma y+G, \tag{7}
\]
write \(b_0=B/M\), \(c_0=S/M\). Divide in \(L^2\) by \(M\); since \(y\in L^2H^2\cap H^1L^2\), test by \(y\in V\). Integration by parts is legitimate for \(A\in H^1\), \(y\in H^2\):
\[
\tfrac12\frac d{dt}\|y\|_2^2+\int A|y_x|^2
=-\int A_xy_xy+\int b_0y^2+\langle p,c_0y\rangle+\langle F/M,y\rangle. \tag{8}
\]
All pairings are spatial at almost every time. In one dimension, \(\|y\|_\infty\le C\|y\|_2^{1/2}\|y_x\|_2^{1/2}\) and \(\|y\|_4^2\le C\|y\|_2^{3/2}\|y_x\|_2^{1/2}\). For arbitrary \(\varepsilon>0\), Young's inequality gives
\[
\begin{aligned}
|\int A_xy_xy|&\le\varepsilon\|y_x\|_2^2+C_\varepsilon\|A_x\|_2^4\|y\|_2^2,\\
|\int b_0y^2|&\le\varepsilon\|y_x\|_2^2+C_\varepsilon\|b_0\|_2^{4/3}\|y\|_2^2,\\
|\langle p,c_0y\rangle|&\le\varepsilon\|y_x\|_2^2+C_\varepsilon\|c_0\|_{H^1}^2\|p\|_{V'}^2,\\
|\langle F/M,y\rangle|&\le\varepsilon\|y_x\|_2^2+C_\varepsilon\|F\|_{V'}^2.
\end{aligned} \tag{9}
\]
The third estimate uses the multiplier property and Poincaré; it does not require \(p\in V\). Define \(\|p\|_{V'}^2=\langle p,(-\partial_{xx}|_V)^{-1}p\rangle\). Since \(p\in H^1_tL^2_x\hookrightarrow H^1_tV'\), the Hilbert chain rule gives
\[
\tfrac12\tfrac d{dt}\|p\|_{V'}^2+\mu\|p\|_{V'}^2
=\gamma(p,y)_{V'}+(p,G)_{V'}
\le C(\|p\|_{V'}^2+\|y\|_2^2+\|G\|_{V'}^2), \tag{10}
\]
with \(|\mu|\|p\|_{V'}^2\) moved to the right if needed. Combining (8)–(10), choosing \(\varepsilon\) against \(\inf A>0\), gives
\[
E'(t)+c\|y_x\|_2^2\le C(t)E(t)+C(\|F\|_{V'}^2+\|G\|_{V'}^2),\quad E=\|y\|_2^2+\|p\|_{V'}^2, \tag{11}
\]
where \(C(t)=C[1+\|A_x\|_2^4+\|B\|_2^{4/3}+\|S/M\|_{H^1}^2]\in L^1(0,T)\). Indeed \(A_x,c_0\) are uniformly bounded and \(\|B(t)\|_2\in L^2_t\); finite \(T\) gives its \(4/3\) power integrable. Gronwall and integration yield
\[
\|y\|_{L^\infty_tL^2_x}+\|y\|_{L^2_tV}+\|p\|_{L^\infty_tV'}
\le C(\|y_0\|_2+\|p_0\|_{V'}+\|F\|_{L^2_tV'}+\|G\|_{L^2_tV'}). \tag{12}
\]
This is an a priori estimate for the assumed strong solutions; it does not assert existence for arbitrary \(V'\)-sources. In (8) multiplication of the actual \(L^2\) source is ordinary multiplication, matching the dual extension.

For \(e_n=Y_n-Y_n^a\), \(z_n=P_n-P_n^a\), equation (7) has \(F=-F_n^a\), \(G=\gamma Y_n^a\), \(y_0=-Y_n^a(0)\), \(p_0=0\). These data satisfy (3), including the \(H^1_0\) initial requirement and both \(L^2\) sources. Estimates (6), (12), and (3) give
\[
\|e_n\|_{L^2_tH^1_x}\le Cq_n^{-2},\qquad \|e_n\|_{L^2_tH^2_x}\le Cq_n^{-1}. \tag{13}
\]
The initial mismatch-only problem has right sides \(O(q_n^{-2})\) in (12), \(O(q_n^{-1})\) in (3); the source-only problem has the same separate bounds by (6). Superposition is legitimate by assumed uniqueness. Neither bound proves delayed exponential decay.

## 4. Trace interpolation and expansion

Let \(s=3/2+\eta\), \(0<\eta<1/2\). Pointwise spatial interpolation followed by Hölder in time gives
\[
\|e_n\|_{L^2H^s}\le C_s\|e_n\|_{L^2H^1}^{2-s}\|e_n\|_{L^2H^2}^{s-1}
\le C_\eta q_n^{-3/2+\eta}. \tag{14}
\]
For \(s>3/2\), derivative evaluation is continuous \(H^s(I)\to\mathbb R\); the strict threshold is necessary for this standard theorem. Strong measurability and bounded linear trace imply \(e_{n,x}(0,\cdot)\in L^2(0,T)\) with (14)'s bound; it agrees almost everywhere with the trace coming from \(L^2H^2\).

Let \(k_n=\mathcal T\phi_n\), and use this section's temporal profile \(a_J(t)=2A_0\sqrt{2/L}\,e^{-\mu t}S(t,0)\). Since \(\phi_n'(0)=\sqrt{2/L}\,q_n\) and \(\phi_n(0)=0\),
\[
2A_0\kappa\partial_xY_n^a(t,0)=\frac{a_J(t)}{q_n},\qquad
k_n=\frac{a_J}{q_n}+\rho_n,\quad
\|\rho_n\|_{L^2(0,T)}\le C_\eta q_n^{-3/2+\eta}. \tag{15}
\]
Here \(k_n\) on \((0,T)\) denotes the analogous all-time observation; restriction produces the delayed columns. The sign is positive for the prescribed \(+Y_x(0)\) convention, not the outward-normal derivative (which is negative at \(0\)); \(\kappa\) cancels exactly. This flux has the model's prefactor \(2A_0\kappa\); the input-kernel trace below is a different object. If \(a_J=0\) on \(J\), the bound still holds but is not a nonzero leading asymptotic. Nonvanishing on the fixed delayed interval remains unverified.

## 5. Actual kernel, traces, and adjoint

\(\sum_n\|k_n\|_{L^2(J)}^2<\infty\), so \(\mathcal T\) is Hilbert–Schmidt and has kernel \(K=\sum_n k_n\phi_n\) in \(L^2(J\times I)\). Direct integration gives for \(\ell(x)=1-2x/L\)
\[
(\ell,\phi_n)=\sqrt{2/L}\int_0^L(1-2x/L)\sin(q_nx)dx
=2\sqrt{2/L}/q_n. \tag{16}
\]
Consequently, in \(L^2(J\times I)\),
\[
K(t,x)=A_0e^{-\mu t}S(t,0)\ell(x)+R(t,x),\qquad R=\sum_n\rho_n\phi_n. \tag{17}
\]
For any \(0\le s<1\), choose \(0<\eta<\min(1/2,1-s)\); then
\[
\sum_n(1+q_n^2)^s\|\rho_n\|_{L^2(J)}^2\le C\sum_n n^{2s-3+2\eta}<\infty. \tag{18}
\]
The spectral Dirichlet space embeds continuously into \(H^s(I)\); for \(1/2<s<1\) it consists of zero-trace \(H^s\) functions. At \(s=1/2\) it is a smaller critical spectral space, not all \(H^{1/2}_0\); no endpoint trace is asserted there. Tonelli and Hilbert-valued series convergence establish \(R\in L^2(J;H^s\cap H)\) for every \(s<1\), and zero endpoint traces for almost every \(t\) when \(s>1/2\). Thus
\[
K(t,0)=A_0e^{-\mu t}S(t,0),\qquad K(t,L)=-A_0e^{-\mu t}S(t,0) \quad\text{a.e. }t. \tag{19}
\]
The fixed \(s>1/2\) representative suffices; no common pointwise time representative, temporal continuity, or analyticity is inferred.

For \(f\in L^2(J)\), the Bochner integral gives \(\mathcal T^*f=\int_J f(t)K(t,\cdot)dt\in H^s\cap H\), with norm bounded by \(\|K\|_{L^2H^s}\|f\|_2\). Therefore
\[
(\mathcal T^*f)(0)=A_0\int_J e^{-\mu t}S(t,0)f(t)dt,\quad
(\mathcal T^*f)(L)=-(\mathcal T^*f)(0). \tag{20}
\]
Independently of the regularity formula, the inherited forced transposition identity defines \((z_f,w_f)\in L^2_{t,x}^2\) through all zero-initial forced solutions and gives, in distributions,
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\quad
-w_{f,t}+\mu w_f=Sz_f,\quad w_f(T)=0,\quad
\mathcal T^*f=\Pi_o w_f(0).
\]
The ODE yields \(w_f(t)=\int_t^T e^{-\mu(r-t)}S(r)z_f(r)dr\in H^1_tL^2_x\); boundary forcing is encoded in the full transposition identity, not an assumed classical trace of \(z_f\). Formula (20) concerns the spatial trace of this **particular adjoint output**. Formula (19) concerns the input-space kernel for almost every observation time. Neither is the endpoint \(h(0)\) of an arbitrary physical \(H^2\) input. For \(h\in L^2\), the latter is not even defined. No dimensional identification between these distinct traces is made.

## 6. The actual remainder separation problem

Let \(Z=L^2(J)\), \(h_n=(h,\phi_n)\), and define
\[
\Lambda h=\sum_{n\ge1}h_n/q_n,\qquad \mathcal Rh=\sum_{n\ge1}h_n\rho_n,\qquad
\mathcal Th=a_J\Lambda h+\mathcal Rh. \tag{21}
\]
The first series is absolutely convergent by Cauchy–Schwarz; \(\Lambda\) is bounded and nonzero on \(H\). The second converges unconditionally in \(Z\) because \(\sum\|\rho_n\|_Z^2<\infty\). For finite sums (21) follows from the actual PDE columns; by continuity it holds for every \(h\in H\). Equivalently \(\mathcal R\) is the Hilbert–Schmidt integral operator with the *actual* \(R\) in (17), not a merely formal subtraction. The units of \(\Lambda\) follow from \(1/q_n\); \(a_J\Lambda h\) and \(\mathcal Rh\) have exactly the physical output units.

Put \(H_0=\ker\Lambda\), choose \(u=q_1\phi_1\) so \(\Lambda u=1\), and set \(b_*=a_J+\mathcal Ru=\mathcal Tu\). Every \(h\in H\) is uniquely \(h=v+c u\), \(v\in H_0\), \(c=\Lambda h\), and
\[
\mathcal Th=\mathcal Rv+c b_*. \tag{22}
\]
**Exact separation criterion.** \(\ker\mathcal T=\{0\}\) if and only if both
\[
\ker(\mathcal R|_{H_0})=\{0\},\qquad b_*\notin\operatorname{ran}(\mathcal R|_{H_0}). \tag{23}
\]
Proof: injectivity of \(\mathcal T\) implies the first condition; if \(b_*=\mathcal Rv\), then \(\mathcal T(u-v)=0\) with \(\Lambda(u-v)=1\). Conversely (22) implies that a zero output with \(c\ne0\) puts \(b_*\) in the exact range, and with \(c=0\) violates the first condition. The **exact**, not closed, range is needed. If \(a_J=0\) this remains valid. In particular \(\mathcal R|_{H_0}\) injective alone is insufficient. Whether either condition holds for the actual system is unresolved; no nonzero physical kernel element is constructed.

The estimates alone cannot decide (23). As abstract Hilbert-space examples, take any fixed nonzero \(a_J\), an orthonormal family \(e_n\subset a_J^\perp\subset Z\), and weights \(d_n=q_n^{-2}\). The family \(\rho_n=0\) satisfies (15)'s norm bounds but gives \(H_0\) as a kernel. The family \(\rho_n=d_ne_n\) also satisfies the bounds and gives injective synthesis; \(a_J\Lambda+\mathcal R\) is then injective by projecting onto \(a_J\) and the \(e_n\). These are abstract operators, **not** realizations of (1), and do not settle the actual system. They show that even all the stated column norm estimates and the shared profile do not determine separation.

### What the equations add, and what is missing

The actual remainder columns satisfy the forced coupled error equations with the *specific* oscillatory residual (5), nonzero initial mismatch and memory forcing \(\gamma Y_n^a\). In particular their temporal shapes are not arbitrary: all are outputs of the same nonautonomous forced PDE–ODE. The exact memory elimination gives, for each \(h\),
\[
MY_t-\kappa Y_{xx}=BY+e^{-\mu t}S h+
\gamma S(t)\int_0^t e^{-\mu(t-r)}Y(r)dr,\quad Y(0)=0. \tag{24}
\]
For \(h\in H_0\), (21) says the physical boundary trace is exactly \(\mathcal Rh\). Thus zero remainder output means precisely \(Y_x(0,t)=0\) on \(J\), with (24)'s unknown distributed source and the whole pre-delay history retained. Dirichlet plus Neumann traces alone do not make this inhomogeneous equation homogeneous. Substituting (24) into a formal boundary equation would require a trace of \(Y_t,Y_{xx},Sh\), not justified by (2)–(3); no such equation is used as proof.

Projecting (1) onto \(\phi_m\) gives a rigorous almost-everywhere weak modal relation
\[
(MY_t,\phi_m)+\kappa q_m^2(Y,\phi_m)=(BY+SP,\phi_m),\qquad
(P_m)' +\mu P_m=\gamma Y_m. \tag{25}
\]
The multiplications by nonconstant \(M,B,S\) couple the sine modes; the first term is \((MY_t,\phi_m)\), not \(M_mY'_m\). Expanding into infinite matrices requires convergence in the relevant weak spaces and produces no established triangular recurrence, diagonal moment family, or closed recurrence for boundary columns. The Volterra history in (24) is exact but its invertibility as a time-evolution equation is not boundary observability. No applicable completeness theorem for this nonautonomous parabolic–nondiffusive ODE pair has been verified.

**Single next theorem (exact missing lemma):** for the fixed actual coefficients, show that the map \(v\mapsto\mathcal Rv\), \(v\in H_0\), has zero kernel and that \(\mathcal Tu\notin\mathcal R(H_0)\), where the outputs are defined by (1). These two clauses are together equivalent to full injectivity, so no stronger coercive inequality, time analyticity, sign, or assumed closed range is logically required. A proof may exploit (24), transposition, or another valid route; a counterexample must construct actual admissible coefficients and a physical state for this fixed experiment. No claim is made that the listed regularity alone suffices. For just \(H^2\) identification, replacing \(H\) by \(X\) gives a weaker target.

## 7. Restricted states, endpoint identification, stability

Let \(X=H^2(I)\cap H\), \(X_0=H^2\cap H^1_0\cap H\), and \(\mathcal B_R=\{h\in X:\|h\|_{H^2}\le R\}\). Oddness gives \(h(L)=-h(0)\), hence \(h=h(0)\ell+g\), \(g\in X_0\). For \(g_n=(g,\phi_n)\), two integrations by parts yield \(q_n^2g_n=-(g'',\phi_n)\); consequently
\[
\|(I-P_N)h\|_2\le |h(0)|\frac{\sqrt{2L}}{\pi\sqrt N}+q_{N+1}^{-2}\|h''\|_2. \tag{26}
\]
This is an upper bound, not a mechanism to extract \(h(0)\) from output. In fact \(\Lambda h=(h,\ell)/(2\sqrt{2/L})\): the leading profile measures a bounded **spatial integral**, not the endpoint. The common profile makes simple high-mode separation harder, but neither proves nor disproves endpoint identification.

Endpoint identification from noiseless linearized data on \(X\) holds exactly when \(\ker\mathcal T\cap X\subset\ker E\), \(E(h)=h(0)\). Full profile identification holds exactly when \(\ker\mathcal T\cap X=\{0\}\). Both are unverified. For any nontrivial \(H^2\) ball, the same conditions characterize uniqueness for pairs in the ball, by scaling a kernel vector; the difference belongs to \(\mathcal B_{2R}\).

Let \(N=\ker\mathcal T\subset H\). Compact embedding of \(\mathcal B_R\) in \(H\), weak compactness in \(H^2\), and continuity of \(\mathcal T\) prove the qualitative modulus
\[
\omega_R(\varepsilon)=\sup\{\operatorname{dist}_H(h,N):h\in\mathcal B_R,\ \|\mathcal Th\|_Z\le\varepsilon\}\to0. \tag{27}
\]
Indeed any violating sequence has a strongly \(H\)-convergent subsequence whose limit is in \(N\). This is distance to the **full** kernel, not necessarily to \(N\cap X\), and gives neither a rate nor uniqueness. If \(N\cap X=\{0\}\), the \(H^2\)-bounded limit is in \(X\) and zero; the same proof yields an \(H\)-norm modulus for pairs on \(\mathcal B_R\). If only \(N\cap X\subset\ker E\), compact embedding \(H^2\Subset C^0\) yields an endpoint modulus on \(\mathcal B_R\), again without an explicit rate. Neither premise follows from the new expansion.

There cannot be a bounded linear output functional \(F:Z\to\mathbb R\) satisfying \(F(\mathcal Th)=h(0)\) on all \(X\): \(X_0\) is dense in \(H\), so continuity of \(F\mathcal T\) forces it to vanish on all \(H\), but \(\ell(0)=1\). This does not rule out unbounded or nonlinear reconstruction on an a priori bounded set. A proposed constrained method is to minimize \(\|\mathcal Th-d\|_Z^2+\alpha\|h\|_{H^2}^2\) over \(X\), or minimize the residual over \(\mathcal B_R\); injectivity, rates, noise choice and physical nonlinear validity are not asserted by proposing it.

## 8. Targeted primary-source audit and limits

The following are primary text passages inspected for this assignment, not an exhaustive survey or a priority search. Cited dependencies were not independently checked.

* Halanay–Pandolfi, [*Approximate controllability and lack of controllability to zero of the heat equation with memory*](https://arxiv.org/html/1404.2745), Theorems 1–2 and boundary-control definitions: on a bounded \(C^2\) domain, a scalar Coleman–Gurtin equation with \(C^1\) convolution multiplying the Laplacian has approximate controllability under distributed or admissible boundary controls. The reachable terminal scalar temperature and its admissibility are not the initial nondiffusive memory component of (1), and the convolution here is not a nonautonomous lower-order PDE–ODE coupling. No transfer to (23).
* Avdonin–Ivanov–Wang, [*Inverse Problems for the Heat Equation with Memory*](https://arxiv.org/html/1612.02129), Theorem 4 and §3: a Gurtin–Pipkin problem identifies its time convolution kernel from equality of response operators under the paper's finite-speed setup. This is not recovery of arbitrary initial \(P\) from one delayed trace; the paper's finite-speed and data assumptions are not those of (1).
* Olive, [*Boundary approximate controllability of some linear parabolic systems*](https://arxiv.org/html/2609.09982), Theorem 1.1 and appendix proof: the autonomous semigroup/root-space characterization uses spectral projections and completeness of adjoint root vectors; the applications concern coupled **diffusive** heat equations. We do not have its autonomous generator, root completeness or compact-resolvent assumptions for the actual time-dependent heat–ODE system. It gives no synthesis separation here.
* Jha–George, [*Observability and Null Controllability for Parabolic Systems with Delay and Memory*](https://arxiv.org/html/2506.22221), Theorem 3.10 and Lemma 3.13: the former invokes a short-time energy-closure assumption, and the latter also assumes adjoint unique continuation and terminal compactness–uniqueness; the observation is associated with moving interior regions. These assumptions and data are not established for a single delayed endpoint output in (1); cited auxiliary results were not independently audited.
* Kian–Sambou–Soccorsi, [*Logarithmic stability inequality in an inverse source problem for the heat equation on a waveguide*](https://arxiv.org/html/1612.07942), Theorem 1.2 and §1.1: scalar heat, \(F=\sigma(t)\beta(x)\), \(\sigma\in C^1\), \(\sigma(0)\ne0\), \(H^1_0\)-bounded unknown, partial waveguide boundary data and further stated hypotheses. The paper explicitly notes that arbitrary inhomogeneous sources can have zero Cauchy trace. The actual source (24) includes feedback and variable \(S(t,x)\); the theorem does not prove (23).
* Choulli–Kian, [*Stability of the determination of a time-dependent coefficient in parabolic equations*](https://arxiv.org/html/1202.5392), Theorem 1: a scalar nonautonomous potential \(\sigma(t)f(x)\), smooth compatible data and a strictly nonzero boundary factor yield stability of \(\sigma\) from differentiated Neumann data. This is not a boundary unique-continuation theorem for our unknown memory; its smoothness, nondegeneracy and observation differ. No primary nonautonomous boundary-UC theorem with the actual coupled hypotheses has been verified here; its absence from this audit is not an impossibility or novelty claim.
* Clason, [*Regularization of Inverse Problems*](https://arxiv.org/html/2001.00617), Theorem 3.9 and Example 3.12: compact-operator singular systems and \(\overline{\operatorname{ran}K^*}=\ker(K)^\perp\). This supports the standard functional-analysis distinction, but not injectivity or a rate for our \(\mathcal T\). The modulus in (27) is proved directly above.

Output completeness \(\overline{\operatorname{span}}\{k_n\}=Z\) is dense **range** of \(\mathcal T\); it is not the injectivity of \(\ell^2\) synthesis \(h\mapsto\sum h_nk_n\). The latter is equivalent to density of \(\operatorname{ran}\mathcal T^*\) in \(H\), or to completeness of the input-space vectors \(K(t,\cdot)\) in the appropriate essential-span sense. Neither completeness statement is established for the actual system.

## 9. Corrections and verdict

The preceding report's main asymptotic, weighted summability and endpoint formulas are confirmed conditional on (2)–(3). No fatal error in those claims was found. Clarifications: (i) its phrase “normalized columns” for \(q_n k_n\) means **scaled**, not unit-norm columns; (ii) the remainder-separation target must include the exact range exclusion (23), not merely injectivity on \(H_0\); (iii) the critical \(s=1/2\) spectral space must not be casually identified with all of \(H^{1/2}_0\); (iv) the leading functional \(\Lambda\) is an interior integral, not endpoint evaluation; (v) labels “PROVED” in the preceding table remain conditional on its inherited, unverified hypotheses. No prior file was changed.

| Claim | Classification | Reason |
|---|---|---|
| Oscillatory dual estimate and multiplier | CORRECT BUT ROUTINE | Integration by parts and 1D Sobolev product, §2. |
| Two-level estimates and \(o(q_n^{-1})\) expansion | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | (2)–(3), (4)–(15); actual base and forced estimates not independently verified for the experiment. |
| Kernel \(H^s\), \(s<1\), and endpoint/adjoint traces | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | (16)–(20); almost-everywhere time traces only. |
| Abstract exact range criterion | PROVED | (22)–(23), conditional only on a bounded operator and nonzero \(\Lambda\). |
| \(H^2\) modulus modulo kernel | CORRECT BUT ROUTINE | Compact embedding and continuity, (27), conditional on existence of \(\mathcal T\). |
| Bounded linear output functional for \(h(0)\) on all \(X\) | FALSE | Dense zero-endpoint inputs; §7. |
| Actual \(\mathcal R|_{H_0}\) injectivity or nontrivial kernel | NOT ESTABLISHED | Exact equations (24)–(25) supply no separation theorem yet. |
| Full injectivity, endpoint/profile identification, nonzero physical invisible state | NOT ESTABLISHED | Missing (23), or weaker restricted-class analogue; no exact physical counterexample. |
| Novel theory or publication priority | NOT ESTABLISHED | Targeted literature review is incomplete; theorem analysis is not a new continuum theory. |

**Answers:** (1) Yes, conditional on the explicit inherited hypotheses. (2) Yes, under the same hypotheses and with the strict trace threshold. (3) No new injectivity result follows. (4) The exact criterion (23) and actual Volterra/transposition equations furnish a defensible route, but no proof or physical disproof yet. (5) Pursue the single actual-system two-clause separation lemma in §6; if it fails, exhibit an admissible fixed-experiment counterexample rather than relying on norm bounds or numerical rank.
