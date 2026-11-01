# Boundary-flux uniqueness, constitutive sign, and delayed smoothing

**Date:** 1 November 2026

**Final verdict: NEW BOUNDARY-FLUX REPRESENTATION OR UNIQUENESS REDUCTION PROVED.** For the unchanged loaded base, the constitutive coupling \(S\gamma\) is uniformly positive on a quantitatively specified initial interval. On that interval, a sign-controlled odd input gives a one-sided, nonnegative boundary derivative by a proved cooperative comparison argument. A rigorous causal operator representation of the actual flux and a delayed-memory no-smoothing result are also given. The initial positive interval has **not** been shown to meet the fixed observation interval, and the sign theorem is not an injectivity theorem. Neither the exact kernel nor a nonzero element is determined.

This is an independent single-agent Arena recalculation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. No constitutive model, loading, material coefficient, or observation interval is changed. No novelty, nonlinear inverse theorem, numerical rank, or new foundational continuum theory is claimed.

## 1. Frozen system and independent audit

The complete `direction-2-odd-compact-quotient-injectivity-investigation.md` was read. The actual symmetric base starts from zero memory and is driven by \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\), \(T=10/\lambda\), on \(I=(0,L)\); the observation is \(J=(\delta,T)\), \(\delta=T/100\). Write
\[
D=a+k,\quad r=k/D,\quad \alpha=a/D,\quad\beta=b/D,\quad
\gamma=\lambda\beta,\quad\mu=\lambda\alpha,\quad d=b^2/D,\quad Qv=v-\bar v.
\]
All prescribed material signs are retained, including \(b\ne0\). For \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), and \(X=H^2(I)\cap H\), the actual input space is \(X\); the bounded linear extension to \(H\) does not imply nonlinear admissibility. With \(\theta_b=\theta_*+y_b\),
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\\
Y(0)=0,\quad P(0)=h,\quad Y(t,0)=Y(t,L)=0,
\end{cases}\quad
\mathcal T h=2A_0\kappa Y_x(\cdot,0)|_J,\tag{1}
\]
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b.\tag{2}
\]
The sufficient hypothesis \(0<q=|g_*|/L<s_*\) is assumed but not verified numerically. It gives a unique loaded base, \(0<m_0\le M_b\le m_1\), \(M_b,S\in L^\infty\), \(M_b\in C_tH^1_x\), and \(B\in L^2((0,T)\times I)\). On \(J\), \(M_b,\kappa/M_b\) are spatially Lipschitz and temporally \(3/4\)-Hölder in the separate uniform senses; \(B\in L^6_{t,x}\cap L^\infty_tL^2_x\cap L^2_tL^\infty_x\). The earlier results give continuous \(S\) on the closed cylinder. These do not imply \(B\in L^\infty_{t,x}\), time analyticity, or a time derivative of \(M_b\) bounded jointly in space-time.

### 1.1 Audit of the compression and adjoint

Use the previous definitions \(D_\delta h=P[h](\delta)\), \(U h=Y[h](\delta)\), \(E=\ker D_\delta\), \(H_1=E^{\perp_H}\), \(P_*=\operatorname{ran}D_\delta\), \(D_1=D_\delta|_{H_1}:H_1\to P_*\), \(F_*=U(E)\), \(N=E\cap\ker U\), \(F_0=\ker(\mathcal R(\cdot,0)|_{F_*})\), \(O_*=\mathcal T(E)\), \(Q_O\) the \(L^2(J)\)-orthogonal projection onto \(O_*^\perp\).

| Audited result | Decision | Independent check |
|---|---|---|
| \(\widehat\Gamma=Q_O\mathcal T|_{H_1}D_1^{-1}\) | **Correct as written.** | \(D_1^{-1}p\) has delayed pair \((A_*p,p)\); identify the quotient isometrically with \(O_*^\perp\). |
| \(\ker\widehat\Gamma=D_1(\Pi_{H_1}\ker\mathcal T)\) | **Correct as written.** | If the output of \(h_1\) belongs to \(\mathcal T(E)\), choose \(e\in E\) to cancel it; conversely decompose an invisible \(h=h_1+e\). |
| Quotients and \(\dim\ker\mathcal T=\dim N+\dim F_0+\dim\ker\Gamma\) | **Correct as written.** | The first quotient has kernel \(E\cap\ker\mathcal T\); the map \(e\mapsto Ue\) has kernel \(N\) and maps that space onto \(F_0\). Finite summands and possibly infinite \(\ker\Gamma\) are allowed. |
| Graph Volterra formulas (7)–(10) | **Correct as written.** | The ODE integral starts at \(\delta\), retains \(P(\delta)\), and the heat forcing multiplies the convolution by \(S(t,x)\). The bounded inverse of \(I-\mathcal V\) follows from the separately proved coupled restart estimate, not from an assumed Neumann-series contraction. |
| \(\widehat\Gamma^*f=(D_1^{-1})^*\Pi_{H_1}\Pi_ow_f(0)\), \(f\perp O_*\) | **Correct as written.** | \(\mathcal T^*f=\Pi_ow_f(0)\); \((D_1^{-1})^*:H_1\to P_*\), and \(f\perp O_*\iff\mathcal T^*f\perp E\). |
| \(F_0\) Gram criterion | **Correct with stated basis qualification.** | For a \(V\)-orthonormal basis \(v_i\) of \(F_*\), \(G_{ij}=\langle\mathcal R(v_i,0),\mathcal R(v_j,0)\rangle_{L^2(J)}\), and \(F_0=0\) iff \(G\) is positive definite. For a basis of \(E\), the analogous Gram matrix instead tests \(E\cap\ker\mathcal T=0\), including \(N\); see §7. |
| \(S(0)\gamma>0\) and abstract example | **Correct as written.** | At \(t=0\), \(y_b=w_b=0\), so \(S(0)\gamma=\lambda^2\alpha r\theta_*b^2/(a+k)>0\). The abstract example has \(S\gamma<0\) and is not the active constitutive system. |

All orthogonal complements above use the \(H\) or \(L^2(J)\) inner product as indicated. In the factorization \(\mathcal R^*:L^2(J)\to V\times H\), the displayed components and \(A_*^*\) depend on the chosen equivalent Hilbert inner product on \(V\) and the product; the adjoint is always taken consistently with that choice. The quotient isomorphism via \(Q_O\) uses the fixed \(L^2(J)\) inner product. Changing equivalent state norms changes Riesz representatives and Gram coordinates, not kernels, finite dimensions, or the truth of positive definiteness.

## 2. Constitutive sign: an explicit initial interval

Let \(m(t)=g_*L^{-1}\sin^2(\pi t/T)\), and denote the base mean memory by \(v_b\) and base mean-zero memory by \(p_b\). The exact base formulas are
\[
v_b(t)=\lambda\int_0^t e^{-\lambda(t-r)}m(r)dr,\quad
p_b(t)=\gamma\int_0^t e^{-\mu(t-r)}Qy_b(r)dr,\quad
w_b=m-v_b-\alpha p_b+\beta Qy_b.\tag{3}
\]
The previous existence report gives \(\|y_b\|_{\mathcal E_T}\le R_b:=2C_Bq\), with \(\|y_{b,t}\|_{L^2_tL^2_x}\le R_b\) and \(\sup_t\|y_{b,x}(t)\|_2\le R_b\). Since \(y_b(0)=0\),
\[
\|y_b(t)\|_2\le R_b\sqrt t,\qquad
\|y_b(t)\|_\infty^2\le2\|y_b(t)\|_2\|y_{b,x}(t)\|_2
\le2R_b^2\sqrt t.\tag{4}
\]
The 1-D inequality follows by integrating \((y_b^2)'\) from a zero boundary value. Set
\[
Y_*(t)=\sqrt2 R_b t^{1/4},\qquad
W_*(t)=q\frac{\pi^2t^2}{T^2}\left(1+\frac{\lambda t}{3}\right)
+2\bigl(|\beta|+\alpha|\gamma|t\bigr)Y_*(t).\tag{5}
\]
Because \(|m(t)|\le q\pi^2t^2/T^2\), \(|v_b(t)|\le\lambda q\pi^2t^3/(3T^2)\), \(\|Qy_b\|_\infty\le2\|y_b\|_\infty\), and \(\|p_b(t)\|_\infty\le2|\gamma|tY_*(t)\), (3) yields
\[
\|y_b(t)\|_\infty\le Y_*(t),\qquad \|w_b(t)\|_\infty\le W_*(t).\tag{6}
\]
These are conservative bounds in the fixed units of the existence investigation, valid for \(0\le t\le T\); they do not require initial-corner derivative regularity.

Since \(\operatorname{sgn}\gamma=\operatorname{sgn}b\), (2) and (6) give the one-sided estimate
\[
S(t,x)\gamma\ge\lambda\alpha|\gamma|\left[|b|r\theta_*-|b|rY_*(t)-2kW_*(t)\right].\tag{7}
\]
The bracket tends to \(|b|r\theta_*>0\) as \(t\downarrow0\). Consequently **for every base satisfying the existing sufficient hypothesis**, there exists \(\tau_+\in(0,T]\) such that
\[
|b|rY_*(\tau_+)+2kW_*(\tau_+)\le\tfrac12|b|r\theta_*,
\qquad S\gamma\ge\tfrac12\lambda\alpha|\gamma||b|r\theta_*>0
\quad\text{on }[0,\tau_+]\times\bar I.\tag{8}
\]
The functions in (5) are nondecreasing, so the inequality at \(\tau_+\) suffices for the entire interval. This explicitly proves more than continuity at \(0\), but it does **not** prove \(\tau_+>\delta\); the conservative bound may expire before observation begins.

For the entire horizon, the separate sufficient, unverified condition \(q<q_{\rm nd}=|b|r\theta_*/(8kC_w)\), \(C_w=W_s+2C_BW_R\), gives \(\theta_b\ge\theta_*/2\), \(\|w_b\|_\infty\le C_wq\), and
\[
S\gamma>\lambda\alpha|\gamma||b|r\theta_*/4>0\quad\text{on }[0,T]\times I.\tag{9}
\]
This strengthens the earlier absolute-value bound to the **correct sign**, for either sign of \(b\). Without the additional bound, (7) is the strongest sign conclusion derived here; the term \(-2kw_b\) can offset \(br\theta_b\). We do not claim a sign change actually occurs or that (9) is necessary.

### 2.1 A proved one-sided boundary-flux sign

Let \(I_-=(0,L/2)\). For odd \(h\), assume \(\operatorname{sgn}(\gamma)h\ge0\) a.e. on \(I_-\). Define \(Z=\operatorname{sgn}(\gamma)P\) and \(C_+=\operatorname{sgn}(\gamma)S\). Because the active coefficients are even, oddness gives \(Y(t,L/2)=0\). On \((0,\tau_+)\times I_-\), (8) implies \(C_+\ge0\), and
\[
M_bY_t-\kappa Y_{xx}=BY+C_+Z,\qquad Z_t+\mu Z=|\gamma|Y,\quad
Y|_{x=0,L/2}=0,\quad Y(0)=0,\ Z(0)\ge0.\tag{10}
\]
No spatial boundary condition is imposed on the ODE state \(Z\).

**Theorem 1.** Under the frozen sufficient condition, (10) implies \(Y\ge0\), \(Z\ge0\) a.e. on \((0,\tau_+)\times I_-\), and
\[
Y_x(t,0)\ge0\quad\text{for a.e. }t\in(0,\tau_+).\tag{11}
\]
If the extra condition (9) holds, the same result holds for \(0<t<T\), including the actual observation window. Reversing the sign assumption on \(h\) reverses the inequalities by linearity.

**Proof.** Put \(Y_-:=\max(-Y,0)\), \(Z_-:=\max(-Z,0)\). Use \(-Y_-/M_b\) as a heat test and \(-Z_-\) as an ODE test. These are legitimate by Sobolev chain rules: \(M_b\) is uniformly positive, \(M_{b,x}\in L^\infty_tL^2_x\), \(Y\in C_tH^1_0\cap H^1_tL^2\cap L^2_tH^2\), and \(Z\in H^1_tL^2\). After integrating by parts on \(I_-\), the heat term contains \(\kappa\int |(Y_-)_x|^2/M_b\) and a cross term bounded by
\[
C\|M_{b,x}\|_2\|Y_-\|_\infty\|(Y_-)_x\|_2
\le\varepsilon\|(Y_-)_x\|_2^2+C_\varepsilon\|M_{b,x}\|_2^4\|Y_-\|_2^2.
\]
Here \(\|Y_-\|_\infty^2\le2\|Y_-\|_2\|(Y_-)_x\|_2\). Similarly,
\[
\int|B|Y_-^2\le\|B\|_2\|Y_-\|_\infty\|Y_-\|_2
\le\varepsilon\|(Y_-)_x\|_2^2+C_\varepsilon\|B\|_2^{4/3}\|Y_-\|_2^2.
\]
The cooperative signs give \(-C_+ZY_-/M_b\le C|Z_-|Y_-\), while the ODE test gives \(-|\gamma|YZ_-\le |\gamma|Y_-Z_-\). Young's inequality and absorption therefore yield
\[
\frac d{dt}(\|Y_-\|_2^2+\|Z_-\|_2^2)
\le C\bigl(1+\|M_{b,x}\|_2^4+\|B\|_2^{4/3}\bigr)
(\|Y_-\|_2^2+\|Z_-\|_2^2).
\tag{12}
\]
The coefficient is integrable on the finite interval, since \(M_{b,x}\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\). The negative parts vanish initially, so Gronwall gives \(Y_-=Z_-=0\). For a.e. time, \(Y(t)\in H^2(I_-)\) has a \(C^1\) representative, \(Y(t,0)=0\), and \(Y(t,x)\ge0\); hence its right derivative at zero is nonnegative. □

This is a cone comparison, not a general maximum principle assumed without proof. The only odd function nonnegative on all of \(I\) is zero; the meaningful cone is one-signed on the **half** interval and reflected oddly. The theorem does not prove strict positivity of the derivative, that \(\tau_+>\delta\), or uniqueness from zero flux. A Hopf-type strict result at these source/coefficient classes would need a separate proof.

## 3. Exact boundary-flux and Volterra representations

Solving the ODE in \(L^2(I)\) gives
\[
P(t)=e^{-\mu t}h+\gamma\int_0^t e^{-\mu(t-r)}Y(r)dr,\tag{13}
\]
so the actual integro-parabolic equation is
\[
M_bY_t-\kappa Y_{xx}-BY
=S(t)e^{-\mu t}h+\gamma S(t)\int_0^t e^{-\mu(t-r)}Y(r)dr,
\quad Y(0)=0,\quad Y|_{\partial I}=0.\tag{14}
\]
The source multiplier is at the **current** \((t,x)\). The first term contains all of the independent initial memory; the second is causal in time and local in space. The scalar exponential factor is positive, but \(S\), the odd input and \(Y\) need not be sign-definite on the full interval. Under (8) or (9), \(\gamma S\ge0\) on the relevant time interval, but that alone does not prove boundary unique continuation.

Let \(\mathcal H_0F\) be the unique strong-temperature solution of
\[
M_bu_t-\kappa u_{xx}-Bu=F,\quad u(0)=0,\quad u|_{\partial I}=0.
\]
The energy/Galerkin estimate in the preceding audit gives \(\mathcal H_0:L^2_{t,x}\to\mathcal E_T\) bounded, without assuming a Green function or a time-independent eigenbasis. Set
\[
F_h=S e^{-\mu t}h,\quad
(\mathcal V u)=\mathcal H_0\!\left(\gamma S(t)\int_0^t e^{-\mu(t-r)}u(r)dr\right),\quad
\mathcal B u=2A_0\kappa\,u_x(\cdot,0)|_J.
\]
Then the actual measured output has the rigorous operator representation
\[
\boxed{\mathcal T h=\mathcal B(I-\mathcal V)^{-1}\mathcal H_0F_h.}\tag{15}
\]
The inverse is bounded on the zero-initial-temperature subspace of \(\mathcal E_T\): for any \(g\) in that space, solve the established forced coupled problem with source \(M_bg_t-\kappa g_{xx}-Bg\) and zero initial state. Its temperature solves \((I-\mathcal V)Y=g\), and uniqueness plus the energy bound supplies the inverse. \(Bg\in L^2\) since \(B\in L^2_{t,x}\) and \(g\in L^\infty_{t,x}\). The trace map \(\mathcal B\) is bounded because \(u\in L^2_tH^2_x\). This is a valid operator representation, not an asserted pointwise boundary Poisson kernel or a proved Green-function formula. Construction and derivative estimates for a nonautonomous kernel at these coefficient classes are not supplied here.

For \(f\in L^2(J)\), the separately constructed coupled transposition adjoint gives the second exact representation
\[
\langle\mathcal T h,f\rangle_{L^2(J)}=\langle h,\Pi_ow_f(0)\rangle_H,\quad
-\partial_t(M_bz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\quad
-w_{f,t}+\mu w_f-Sz_f=0.
\tag{16}
\]
The heat boundary input \(2A_0\mathbf1_J f\) at \(0\), zero input at \(L\), and terminal heat condition are understood by transposition; \(z_f\in L^2\), \(w_f\in H^1_tL^2_x\), \(w_f(T)=0\). Completeness of \(\{\Pi_ow_f(0)\}\) or its separation of \(X\) has not been proved. The positivity of \(S\gamma\) on a short interval does not establish positivity or completeness of this adjoint family.

## 4. What the positive delay smooths—and what it does not

For every \(h\in H\), the established solution bound gives
\[
Y(\delta)\in V,\qquad P(\delta)=e^{-\mu\delta}h+K_\delta h,\qquad
K_\delta:H\to H^2(I)\cap H^1_0(I)\cap H\text{ bounded}.\tag{17}
\]
The second assertion follows by integrating \(Y\in L^2(0,\delta;H^2\cap H^1_0)\) in the Bochner sense. In particular \(K_\delta:H\to H\) is compact; \(Y(\delta)\) is bounded into \(V\), and its map into \(H\) is compact. An \(H^2\) trace for \(Y(\delta)\), or compactness of its map into \(V\), is not established.

Equation (17) also yields the exact **no extra Sobolev smoothing of the memory input** statement: for each \(0\le s\le2\),
\[
P(\delta)\in H^s(I)\quad\Longleftrightarrow\quad h\in H^s(I),\tag{18}
\]
for \(h\in H\). Indeed \(K_\delta h\in H^2\subset H^s\), and \(e^{-\mu\delta}\ne0\). In particular a general \(L^2\) memory direction is not made \(H^1\) by waiting until \(\delta\); smoothness of the correction cannot cancel a nonsmooth \(h\). For \(h\in X\), the same formula yields \(P(\delta)\in H^2\), and its endpoint traces are \(P(\delta,0)=e^{-\mu\delta}h(0)\), \(P(\delta,L)=e^{-\mu\delta}h(L)\).

The delayed memory map is Fredholm of index zero, so its range is closed of codimension \(\dim\ker D_\delta\). It is proper **only if** \(\ker D_\delta\ne0\), not automatically proper. The reachable pair additionally obeys the graph-plus-finite-fiber relation of the previous report; it is not an arbitrary element of \(V\times H\). These restrictions and (18) do not yet show that the full flux on \(J\) determines the reachable pair, even up to finite dimension: the compact graph-output quotient has not been proved to have finite-dimensional kernel.

## 5. Boundary continuation and weighted memory

For every fixed \(\psi\in H^2(I)\), the valid weak boundary identity is
\[
\langle M_bY_t,\psi\rangle-\kappa\langle Y,\psi''\rangle
+\kappa Y_x(t,0)\psi(0)-\kappa Y_x(t,L)\psi(L)
=\langle BY+SP,\psi\rangle\quad\text{in }L^2(J).\tag{19}
\]
Zero observation and odd symmetry give both endpoint derivative traces zero, but the unknown distributed \(SP\) remains. Neither \(Y_t\) nor \(Y_{xx}\) has an independently justified endpoint trace, so the PDE cannot be evaluated there termwise. The scalar reduction
\[
Y_t-A Y_{xx}=VY+CP,\quad A=\kappa/M_b,\ V=B/M_b,\ C=S/M_b,
\tag{20}
\]
has \(VY,CP\in L^2\); it is not a homogeneous scalar equation. In divergence form, \(Y_t-(AY_x)_x=VY+CP-A_xY_x\).

For a symmetric compact subinterval \(J_0=(t_-,t_+)\Subset J\), center \(t_c\), \(H_0=t_+-t_-\), and bounded exponential weight \(W_s\) nonincreasing away from \(t_c\), the exact ODE gives, by Cauchy–Schwarz and Fubini,
\[
\begin{aligned}
\iint_{J_0\times I}W_s^2|P|^2\le{}&2e^{2\mu H_0}H_0\int_I W_s(t_c)^2|P(t_c)|^2\\
&+2e^{2\mu H_0}|\gamma|^2H_0^2\iint_{J_0\times I}W_s^2|Y|^2.
\end{aligned}\tag{21}
\]
The backward half uses the oriented integral with a minus sign and the factor at most \(e^{\mu H_0}\); all weighted terms are finite for bounded standard negative singular weights. This is an ODE estimate, not a coupled boundary Carleman estimate. The unknown \(P(t_c)\) is correlated with the past by (13) but not known from zero flux. A different weight or coupled argument might control it. Even if \(S\gamma>0\), (21) does not absorb this distributed trace into endpoint observation, and a scalar residual estimate still contains \(CP\). The comparison theorem in §2.1 only covers one-sided inputs and cannot replace this missing estimate for arbitrary odd inputs. No interior or subregion vanishing, nor quantitative continuation, is proved.

## 6. Moments and positive-time asymptotics

Let \(\phi_n=\sqrt{2/L}\sin(2n\pi x/L)\), \(\rho_n=(2n\pi/L)^2\), \(u_n=\langle Y,\phi_n\rangle\), \(p_n=\langle P,\phi_n\rangle\), \(h_n=\langle h,\phi_n\rangle\). The exact coupled moments are
\[
\sum_m\langle M_b\phi_m,\phi_n\rangle u_m'+\kappa\rho_nu_n
=\langle BY,\phi_n\rangle+\sum_m\langle S\phi_m,\phi_n\rangle p_m,
\quad p_n'+\mu p_n=\gamma u_n,\quad p_n(0)=h_n.\tag{22}
\]
The series are understood through \(L^2\) projections; \(BY\in L^2\). Strong-temperature regularity gives \(Y_N=\sum_{n\le N}u_n\phi_n\to Y\) in \(L^2(J;H^s(I))\) for \(3/2<s<2\), so
\[
Y_x(\cdot,0)=\lim_{N\to\infty}\sum_{n\le N}\sqrt{2/L}\,(2n\pi/L)u_n(\cdot)
\quad\text{in }L^2(J).\tag{23}
\]
This is a convergent **trace expansion**, not a proved time-asymptotic expansion by distinct exponential decays. The actual spatial and time-dependent multipliers need not be diagonal and can couple modes; neither a nonzero particular off-diagonal entry nor a spectral gap/Riesz basis for the nonautonomous coupled evolution has been proved. Zero output gives only that the sum converges to zero, not that each summand or \(h_n\) vanishes.

One sufficient exact completeness condition would be: for every \(n\), there exist controls \(f_{n,j}\in L^2(J)\) such that \(\Pi_ow_{f_{n,j}}(0)\to\phi_n\) in \(H\). Then (16) gives \(h_n=0\) for all \(n\). This condition is stronger than needed for \(X\), and remains unproved. Compactness shows that any such controls need not have bounded norm; it does not contradict qualitative completeness.

## 7. Pre-delay and vertical components

The joint pre-delay kernel is \(N=\{h:Y(\delta)=P(\delta)=0\}\), and the delayed-memory kernel \(E=\ker D_\delta\) contains it. The known \(K_\delta:H\to H^2\cap H^1_0\) implies \(N\subset E\subset X\). The previous conditional bound
\[
\|K_\delta\|\le |\gamma|C_Y\left[\int_0^\delta\left(\frac{1-e^{-\mu u}}\mu\right)^2du\right]^{1/2}
\tag{24}
\]
would make \(D_\delta\) invertible if it were strictly below \(e^{-\mu\delta}\); \(C_Y\) is the data-only bound derived in the preceding report. That condition is not numerically verified. A forward upper energy bound cannot exclude a trajectory reaching zero: \(E(t)\le C E(0)\) is not a backward lower bound. The precise missing coupled backward property is
\[
Y(0)=0,\ P(0)=h,\ (Y(\delta),P(\delta))=(0,0)\quad\Longrightarrow\quad h=0,
\tag{25}
\]
for the actual coefficients and \(h\in H\); it is not established by sign alone.

For the vertical state fiber \(F_*=U(E)\), choose a \(V\)-orthonormal basis \(v_1,\ldots,v_m\), and select \(e_i\in E\) with \(Ue_i=v_i\). Since \(D_\delta e_i=0\), \(\mathcal T e_i=\mathcal R(v_i,0)\). Thus
\[
G_{ij}=\langle\mathcal T e_i,\mathcal T e_j\rangle_{L^2(J)},\qquad
F_0=0\iff G\text{ is positive definite}.\tag{26}
\]
Choosing instead a basis of **all** \(E\) produces a Gram matrix that has a null vector for any nonzero \(N\), even when \(F_0=0\); the distinction matters. The comparison result gives no positivity or linear independence of \(\mathcal T e_i\) for general signed \(e_i\); neither \(N\) nor \(F_0\) is proved zero, and no Gram rank is asserted. A sufficient additional result is linear independence of those \(m\) actual output functions in \(L^2(J)\); it must be proved, not inferred from finite dimension.

## 8. Narrow primary-theorem check

The search was restricted to the exact parabolic–ODE/Volterra or boundary-flux question. Primary texts and relevant displayed proofs were reopened; no result is inferred from an abstract.

1. **P. Gaitan**, *Inverse Conductivity Problem for a Parabolic Equation using a Carleman Estimate with One Observation*, [arXiv:0706.1422](https://arxiv.org/html/0706.1422), Theorem 2.2 and Assumption 2.1. On a smooth bounded domain, the displayed scalar operator is \(\partial_t-\nabla\cdot(c(x)\nabla)\) with smooth positive **time-independent** conductivity, zero lateral Dirichlet data, a spatial \(C^4\) noncritical weight with boundary sign condition, and displayed \(q\in H^1_tH^2_x\). Its right side contains a measured boundary normal derivative **and** the full scalar residual. There is no independent distributed ODE state. It is a weighted estimate, not our coupled uniqueness theorem: the actual \(A(x,t)\) and solution class are not the stated ones, and \(CP\) remains a residual. The text does not prove the needed coupled absorption.

2. **D. P. Jha and R. K. George**, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), Lemma 3.5, Lemma 3.7 and Proposition 3.8, including their displayed proofs. Their ODE realization uses \(q_t+\mu q=G\), \(q(0)=0\), moving interior observation and delay-compatible weights; their proposition has a constant principal Laplacian, a moving interior observation and a short-time remainder. It does not treat our fixed endpoint derivative and independently unknown correlated \(P(\delta)\). The lemma/proposition statements and proof text were inspected, not independently certified in full.

3. **J. Apraiz, R. Lecaros and S. Zamorano**, *A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations*, [arXiv:2610.26157v1](https://arxiv.org/html/2610.26157), Lemma 2.2 and Theorem 2.3. The centered ODE inequality controls a zero-order term by an ODE residual **plus a weighted center-time trace**; the Kelvin–Voigt theorem uses a constant-principal parabolic factor, an interior observation and that snapshot, in its \(N=2,3\) setup. It is not a one-dimensional endpoint-only theorem for (1). Its Schur proof was inspected but does not control our actual unknown trace from flux.

The previously used Albano–Tataru primary PDF could not be fetched in this current check; its earlier audit remains recorded separately, and no new claim about its proof is made here. No directly applicable theorem was found in this narrow search; this is not an exhaustive negative literature claim.

## 9. Final status

| Question | Status | Exact mathematical reason |
|---|---|---|
| Constitutive sign of \(S\gamma\) near \(t=0\) | **Proved** | Explicit bound (7)–(8), under the existing sufficient base assumption. |
| Sign of \(S\gamma\) on delayed interval | **Conditional; otherwise open** | (9) under additional unverified \(q<q_{\rm nd}\); \(\tau_+\) is not known to exceed \(\delta\). |
| Boundary-flux representation | **Proved** | Causal strong-solution operator (15) and transposition identity (16); no Green kernel claimed. |
| Delayed-state smoothing | **Partly proved** | \(Y(\delta)\in V\); \(P(\delta)=e^{-\mu\delta}h+H^2\) correction and equivalence (18). |
| Reachable-state boundary uniqueness | **Open** | Full flux could have an unresolved exact kernel on the reachable graph. |
| Coupled boundary unique continuation | **Not established** | Unknown distributed source and weighted memory trace in (19)–(21). |
| Moment completeness | **Open** | Only the \(L^2_t\) trace series is justified; no independence of its time outputs. |
| Injectivity of \(D_\delta\) | **Open** | Fredholm; sufficient condition (24) unverified. |
| Joint state injectivity \(N=0\) | **Open** | Coupled backward property (25) not proved. |
| Vertical component \(F_0=0\) | **Open** | Finite Gram criterion (26), no proved rank. |
| Quotient kernel \(\ker\Gamma=0\) | **Open** | No coupled separation/density theorem. |
| Injectivity on \(X_o\) | **Open** | No proof or exact counterexample. |
| Injectivity on \(H_o\) | **Open** | Full adjoint density not established. |
| Exact nonzero invisible input | **Not constructed** | The sign and compactness results do not produce one. |

The next mathematical target is a qualitative coupled boundary-to-interior or adjoint separation theorem for the actual variable coefficients that controls the delayed memory term without a forbidden uniform strong-state observability estimate. A proof of strict boundary response for sign-controlled inputs on an interval overlapping \(J\) would be a narrower possible step, but it would not by itself prove injectivity for sign-changing odd inputs.

**Final verdict: NEW BOUNDARY-FLUX REPRESENTATION OR UNIQUENESS REDUCTION PROVED.**
