# Independent mathematical audit: active parity decomposition

**Date:** 1 November 2026
**Overall conclusion: PASS WITH CORRECTIONS.** The exact parity decomposition and the stated interior-vanishing implication are valid under the prior explicit small-data hypothesis, provided the functional-analytic details below are supplied. No algebraic error was found in the active linearized equations or modal equations. Two statements need qualification: parity alone does not prove that the odd flux-difference operator detects even one nonzero input, and the zero force channel fixes a **sum**, not a product. The active three-channel kernel itself remains unresolved.

This is an independent recalculation by Arena, not certification by an independent human or by a separate model. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is the Research Scholar / Builder / Literature Investigator. This audit does not attempt a new kernel construction or prove injectivity.

## 1. Verdict inventory

The following classifications refer to `direction-2-active-linearized-kernel-analysis.md`, hereafter **the analyzed report**, and assume the explicit hypotheses in §2 below.

| Requested result | Verdict | Audited conclusion |
|---|---|---|
| 1. Force-kernel condition | **PASS** | \(b\bar Y+k e^{-\lambda t}\bar h=0\) a.e. on \(J\), not \(\bar Y=0\) for a general even input. |
| 2. Reflection transformation | **PASS** | The transformation preserves the original system and all data in their specified trace senses. |
| 3. Active base is symmetric | **PASS** | Reflection maps the base to a solution in the same weak class; full-class uniqueness gives equality. |
| 4. Even/odd subsystems | **PASS** | Equations (12)–(13) of the analyzed report include all active terms and the correct projections and mean-memory contribution. |
| 5. Direct-sum kernel | **PASS** | Equation (9) follows from parity-preserving linear well-posedness and invertible sum/difference of the labeled flux traces; it characterizes but does not determine the two kernels. |
| 6. Interior-vanishing implication | **PASS** | The stated additional assumption \(Y=0\) on the *entire* cylinder plus zero force implies \(h=0\); uniform nonvanishing near \(t=0\) follows from the indicated regularity. |
| 7. Modal equations | **PASS WITH CORRECTION** | Equation (18) is algebraically correct; convergence is clarified in §7. The report's phrase “L²-convergent expansions” must not be read as convergence of all coefficient functions uniformly in time, nor as a pointwise-in-time boundary series. |
| 8. Full active linearized kernel unresolved | **PASS** | The calculations do not prove triviality or construct a nonzero kernel element. The actual truth of either possibility is **NOT ESTABLISHED**. |

**Additional correction — sensor interpretation.** The analyzed report says the flux difference “can detect an odd direction,” followed by the caveat that it has not been shown to detect every odd direction. The parity calculation alone proves only that the difference **depends exclusively on** the odd input; it does not by itself prove this operator is nonzero for any actual odd direction on the delayed interval. The safe statement is: *the difference is the only labeled-flux combination carrying odd information, if any; whether it detects a particular or every nonzero odd input is not established by parity.* This correction is about the stated consequence, not the kernel splitting proof. Also, its §2 says the interval fixes a “product” \(b\bar Y+kV\); this is a **linear combination**, and zero force fixes that sum to zero.

## 2. Exact conditional setting and linearization

Let \(I=(0,L)\), \(J=(\delta,T)\), \(T=10/\lambda\), \(\delta=T/100\), \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\). Use the frozen parameters \(a,k,\lambda,c,\kappa,L,A_0,\theta_*>0\), \(b\ne0\), and \(M>0\). No sign of \(b\) is assumed. Put

\[
D=a+k,\ r=k/D,\ \alpha=a/D,\ \beta=b/D,\ \mu=\lambda\alpha,\ d=b^2/D,\quad
m=g/L,\quad Qf=f-\bar f.
\]

Assume \(0<q=|g_*|/L<s_*\), with \(s_*\) exactly (6.3) of `direction-2-formulation-A-existence-investigation.md`; the numerical inequalities are interpreted in its fixed unit convention. The frozen experimental parameters are unspecified, so this is a **sufficient conditional hypothesis**, not a verified fact. The independent existence audit's dimensional clarification remains relevant: an engineering test needs consistently nondimensionalized or fixed-unit constants.

Write \(y_b=\theta_b-\theta_*\), \(p_b=Qz_b\), \(v_b=\bar z_b\), \(w_b=m-v_b-\alpha p_b+\beta Qy_b\), \(E_b=m'+r(p_b)_t\). The actual driven trajectory has \(y_b=p_b=v_b=0\) initially, but is not replaced by a static zero-load equilibrium. Differentiating the reduced system independently gives

\[
\begin{aligned}
V&=e^{-\lambda t}\bar h,& P_t&=-\mu P+\lambda\beta QY,&P(0)&=Qh,\\
W&=-V-\alpha P+\beta QY,&Y(0)&=0,&Y|_{\partial I}&=0,\\
(cI+d\theta_bQ)Y_t-\kappa Y_{xx}
&=-dYQ(y_b)_t-bYE_b-br\theta_bP_t+2k\lambda w_bW.
\end{aligned}\tag{2.1}
\]

For the derivative, \(Y\in\mathcal E_T=\{Y\in H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x}):Y(0)=0\}\); \(P\in H^1_tL^2_x\). The fourth line is obtained from the \(\theta\)-dependent mass, \(-b\theta E\), and \(k\lambda w^2\):

\[
D[(cI+d\theta Q)y_t]= (cI+d\theta_bQ)Y_t+dYQ(y_b)_t,\quad DE=rP_t,\quad D(w^2)=2w_bW.
\]

Thus the apparently easy-to-miss term \(-dYQ(y_b)_t\), the active \(-bYE_b\), the full \(-br\theta_bP_t\), and the active heating variation all have the correct signs and factors.

## 3. Force observation — PASS

Equilibrium and the displacement constraint yield

\[
\sigma=Dm-b\bar y-kv,\qquad
D\sigma[h]=-b\bar Y-ke^{-\lambda t}\bar h.
\]

Since \(A_0>0\), zero force in \(L^2(J)\) is exactly

\[
b\bar Y+ke^{-\lambda t}\bar h=0\quad\text{a.e. on }J.\tag{3.1}
\]

The complete derivative also has heat powers \(A_0\kappa Y_x(0,\cdot)\) and \(-A_0\kappa Y_x(L,\cdot)\). The force equation does not imply \(\bar Y=0\) unless \(\bar h=0\), and within the force kernel the two zero-mean conditions are equivalent because \(b,k\ne0\). An odd input does satisfy both by symmetry; a general even input need not. The analyzed parity theorem correctly keeps (3.1) in its even condition (10). Its output equalities are a.e. in \(J\); \(\bar Y\in H^1(0,T)\), so the mean-force equality has a continuous representative on \(J\).

## 4. Reflection: original equations, initial and boundary data — PASS

For an original solution define

\[
u^R(x,t)=g(t)-u(L-x,t),\quad
\theta^R(x,t)=\theta(L-x,t),\quad z^R(x,t)=z(L-x,t).
\]

Reflection is an isometry on \(L^2,H^1,H^2\). For a.e. \((x,t)\),

\[
\varepsilon^R=(u^R)_x=\varepsilon(L-x,t),\quad
\varepsilon^R_t=\varepsilon_t(L-x,t),\quad
\theta^R_t=\theta_t(L-x,t),\quad
\theta^R_{xx}=\theta_{xx}(L-x,t).
\]

Consequently \(\sigma^R=a\varepsilon^R-b(\theta^R-\theta_*)+k(\varepsilon^R-z^R)=\sigma(L-x,t)\), so \((\sigma^R)_x=0\). Likewise \((z^R)_t=\lambda(\varepsilon^R-z^R)\), and each term in the heat equation is the reflected original term. In particular the quadratic heat source is invariant; no sign is lost from the reflection of \(u\).

The end conditions are \(u^R(0,t)=g-u(L,t)=0\), \(u^R(L,t)=g-u(0,t)=g\), and the two equal bath values exchange. At \(t=0\), \(g(0)=0\), \(\theta^R=\theta_*\), and \(z^R=Rz_0\). For a general initial memory the quasistatic initial displacement is **not** separately zero: \(u_0(x)=r\int_0^x Qz_0(s)\,ds\). Since \(\int_0^LQz_0=0\), the transformed initial displacement satisfies

\[
-u_0(L-x)=r\int_0^xQ(Rz_0)(s)\,ds,
\]

which is exactly the reconstructed quasistatic initial displacement for \(Rz_0\). For the actual base \(z_0=0\), \(u_0=0\) as well. Reflected fields satisfy all weak initial, spatial boundary, positivity, boundedness and \(L^2\)-trace requirements. The displacement time derivative has a \(g'\) term, but the equation involves \(\varepsilon_t\); differentiating the reflected strain gives the required expression above.

**Base symmetry — PASS.** At \(z_0=0\) the reflected solution has the same initial and boundary data as the active base. The existence theorem and its separately established uniqueness in the entire specified weak-initial class apply to both. Therefore \(Ry_b=y_b\), \(Rp_b=p_b\), and \(R\theta_b=\theta_b\), \(Rw_b=w_b\), \(RE_b=E_b\) a.e. This uses uniqueness beyond the contraction ball, not merely the fixed-point uniqueness. By (2.1), reflection also commutes with the linearized system about that symmetric base; the derivative's linear solution is unique by the invertibility established in §8.

## 5. Parity subsystems and observations — PASS

Set \(\Pi_e=(I+R)/2\), \(\Pi_o=(I-R)/2\), \(h_{e,o}=\Pi_{e,o}h\). These are bounded projections on \(H^2\), \(h=h_e+h_o\), and the ranges intersect only at zero. Reflection commutes with \(Q\); multiplication by each even base coefficient also commutes with reflection. By linear uniqueness \(Y=Y_e+Y_o\), \(P=P_e+P_o\), with corresponding parities. For an odd function, \(\bar h_o=\bar Y_o=\bar P_o=0\), and \(Q(Y_o)_t=(Y_o)_t\) in \(L^2_{t,x}\). For even inputs the mean-memory variation remains \(V_e=e^{-\lambda t}\bar h_e\).

For even input (2.1) reduces exactly to

\[
\begin{aligned}
(P_e)_t&=-\mu P_e+\lambda\beta QY_e,\quad P_e(0)=Qh_e,\\
W_e&=-e^{-\lambda t}\bar h_e-\alpha P_e+\beta QY_e,\\
(cI+d\theta_bQ)(Y_e)_t-\kappa(Y_e)_{xx}
&=-dY_eQ(y_b)_t-bY_eE_b-br\theta_b(P_e)_t+2k\lambda w_bW_e.
\end{aligned}\tag{5.1}
\]

For odd input it reduces exactly to

\[
\begin{aligned}
(P_o)_t&=-\mu P_o+\lambda\beta Y_o,\quad P_o(0)=h_o,\\
W_o&=-\alpha P_o+\beta Y_o,\\
(c+d\theta_b)(Y_o)_t-\kappa(Y_o)_{xx}
&=-dY_oQ(y_b)_t-bY_oE_b-br\theta_b(P_o)_t+2k\lambda w_bW_o.
\end{aligned}\tag{5.2}
\]

In particular, on the odd subspace the rank-one subtraction \(-d\theta_b\overline{(Y_o)_t}\) vanishes; it does **not** vanish for general even inputs. Neither equation replaces \(\theta_b\) by \(\theta_*\) or deletes \(E_b,w_b\).

For a.e. time, \(Y_{e,o}(t)\in H^2(I)\) and the equality to its reflected representative holds in \(H^2\). The one-dimensional \(H^2\) trace theorem therefore gives

\[
(Y_e)_x(L)=-(Y_e)_x(0),\qquad (Y_o)_x(L)=(Y_o)_x(0)\quad\text{in }L^2(0,T).
\]

With \(F,Q_0,Q_L\) denoting the three **variations** and with \(J\)-restriction implicit,

\[
F=-A_0(b\bar Y_e+ke^{-\lambda t}\bar h_e),\quad
Q_0+Q_L=2A_0\kappa(Y_e)_x(0),\quad
Q_0-Q_L=2A_0\kappa(Y_o)_x(0).\tag{5.3}
\]

The signs reflect the physical convention \(Q_L=-A_0\kappa Y_x(L)\), and agree with (14) in the analyzed report.

### Direct-sum kernel — PASS

Let \(K_e\subseteq H^2\cap\{Rh=h\}\) be defined by zero even force and \((Y_e)_x(0)=0\) on \(J\); let \(K_o\subseteq H^2\cap\{Rh=-h\}\) be defined by \((Y_o)_x(0)=0\) on \(J\). The map \((Q_0,Q_L)\mapsto(Q_0+Q_L,Q_0-Q_L)\) is invertible on \(L^2(J)^2\). Hence (5.3) proves both directions of

\[
\ker(D\mathcal O(0):H^2\to L^2(J)^3)=K_e\oplus K_o.\tag{5.4}
\]

The directness is inherited from the even/odd decomposition, not from any assumption that either \(K_e\) or \(K_o\) is trivial. No full-map injectivity or non-injectivity is implied.

## 6. Interior-vanishing result and delayed memory — PASS

Assume \(D\mathcal O(0)h=0\) and, independently, \(Y=0\) a.e. on **all** \((0,T)\times I\). Equation (3.1) gives \(\bar h=0\); the memory formula gives \(P=e^{-\mu t}h\), \(P_t=-\mu e^{-\mu t}h\), \(V=0\), and \(W=-\alpha e^{-\mu t}h\). Substitution in (2.1) gives the analyzed report's exact coefficient

\[
\lambda\alpha\left(br\theta_b-2kw_b\right)e^{-\mu t}h=0\quad\text{a.e. on }(0,T)\times I.\tag{6.1}
\]

This uses \(\mu=\lambda\alpha\); the two terms carry \(+br\mu\theta_b\) and \(-2k\lambda\alpha w_b\), respectively.

The usual maximal-regularity time-trace theorem yields \(y_b\in C([0,T];H^1_0(I))\), and the 1-D Sobolev embedding is continuous into \(C([0,L])\). Thus \(y_b\in C([0,T];C([0,L]))\). At \(z_0=0\), the ODE representation

\[
p_b(t)=\lambda\beta\int_0^t e^{-\mu(t-s)}Qy_b(s)\,ds
\]

is continuous into \(C([0,L])\); \(v_b\) and \(m\) are continuous. Hence \(w_b=m-v_b-\alpha p_b+\beta Qy_b\) is continuous on the compact cylinder, and at zero time \(\theta_b=\theta_*\), \(w_b=0\). Since \(br\theta_*\ne0\), there is \(\varepsilon>0\) for which

\[
|br\theta_b(t,x)-2kw_b(t,x)|\ge |br\theta_*|/2
\quad(0\le t\le\varepsilon,\ 0\le x\le L).
\]

No assumption \(b>0\) is required. Multiplying (6.1) by the reciprocal on this cylinder and applying Fubini gives \(h=0\) in \(L^2(I)\), hence in \(H^2(I)\). This proves the implication as stated; no corner value of \((y_b)_t\) is used. The premise is stronger than the measured boundary data, and zero force remains an explicit hypothesis.

If instead \(Y=0\) merely on \(J\), causality yields only

\[
P(t)=e^{-\mu(t-\delta)}P(\delta),\qquad
P(\delta)=e^{-\mu\delta}Qh+\lambda\beta\int_0^\delta e^{-\mu(\delta-s)}QY(s)\,ds.\tag{6.2}
\]

The integral may be nonzero; delayed vanishing alone does not permit its removal or backward continuation. Even \(Y=0\) on \(J\) is not derived from the boundary data. The report's caution on this point is correct.

## 7. Modal system and convergence — PASS WITH CORRECTION

Let \(\phi_j=\sqrt{2/L}\sin(j\pi x/L)\), \(\nu_j=(j\pi/L)^2\), \(a_j=(1,\phi_j)\), where \((\cdot,\cdot)\) denotes the real \(L^2(I)\) inner product. Put \(Y_j=(Y,\phi_j)\), \(P_j=(P,\phi_j)\), \(H_j=(h,\phi_j)\). Then

\[
\bar Y=L^{-1}\sum_j a_jY_j,\quad
\dot P_i=-\mu P_i+\lambda\beta(Y_i-a_i\bar Y),\quad
P_i(0)=H_i-a_i\bar h.\tag{7.1}
\]

These follow by testing the memory equation; in particular \((QY,\phi_i)=Y_i-a_i\bar Y\).

With row index \(i\) the test function and column index \(j\) the expanded factor, the analyzed report defines

\[
\begin{array}{ll}
B_{ij}=(\theta_bQ\phi_j,\phi_i),&H_{ij}=(\theta_b\phi_j,\phi_i),\\
C_{ij}=((dQ(y_b)_t+bE_b)\phi_j,\phi_i),&K_{ij}=(w_b\phi_j,\phi_i),\\
K^Q_{ij}=(w_bQ\phi_j,\phi_i),&w_i=(w_b,\phi_i).
\end{array}
\]

Testing (2.1) gives precisely

\[
\begin{aligned}
c\dot Y_i+d\sum_j B_{ij}\dot Y_j+\kappa\nu_iY_i
={}&-\sum_jC_{ij}Y_j-br\sum_jH_{ij}\dot P_j\\
&+2k\lambda\left[-e^{-\lambda t}\bar h\,w_i-\alpha\sum_jK_{ij}P_j+\beta\sum_jK^Q_{ij}Y_j\right].
\end{aligned}\tag{7.2}
\]

For example \(B_{ij}=H_{ij}-(\theta_b,\phi_i)\bar\phi_j\), with \(\bar\phi_j=a_j/L\); this exhibits the correct rank-one subtraction. Testing \(-\kappa Y_{xx}\) gives \(+\kappa\nu_iY_i\), using the Dirichlet trace. The \(P_t\) term uses \(H\), not \(B\), because it is \(\theta_bP_t\), although \(P_t\) has zero mean. The signs and factors in (7.1)–(7.2) agree with equation (18).

**Convergence clarification.** Let \(\Pi_N\) denote projection onto the first \(N\) Dirichlet eigenfunctions. \(\Pi_NY\to Y\) in \(L^2_t(H^2\cap H^1_0)\) and in \(H^1_tL^2\); the convergence in \(C_tH^1_0\) follows from the maximal-regularity embedding. Also \(\Pi_NP\to P\) in \(H^1_tL^2\). Multiplication by bounded \(\theta_b,w_b\) and application of \(Q\) preserve the relevant \(L^2\) convergence. For \(C\), \(dQ(y_b)_t+bE_b\in L^2_{t,x}\), while \(\Pi_NY-Y\to0\) in \(C_tH^1_x\hookrightarrow L^\infty_{t,x}\); thus the product converges in \(L^2_{t,x}\). Consequently each fixed-row equation holds in \(L^2(0,T)\), with a common a.e. representative for the countable rows. This supplies the precise sense of the sums; it does not assert uniform-in-time convergence of \(C_{ij}(t)\) or termwise endpoint-flux evaluation.

Moreover \(\Pi_NY\to Y\) in \(L^2_tH^2_x\), so the endpoint derivative traces of the finite partial sums converge in \(L^2(0,T)\), and on \(J\). This is a legitimate **trace-limit** interpretation, not an assertion of absolute or pointwise time convergence of the derivative series.

Since \(R\phi_j=(-1)^{j+1}\phi_j\), \(a_j=0\) for even \(j\). The symmetric coefficients \(\theta_b,w_b,E_b,Q(y_b)_t\) and \(Q\) commute with reflection; thus all displayed matrices vanish between opposite parity blocks for a.e. time. Within a block, multiplication by a spatially varying even coefficient can create off-diagonal entries. Also \(Q\phi_j=\phi_j-a_j/L\), so even when a coefficient is spatially constant, the rank-one correction couples odd-index (spatially even) sine modes in general. The odd-index/even-index split is established; simultaneous diagonalization, modal distinguishability, completeness of the observation moments and injectivity are **not** established.

## 8. Small-data neighborhood and differentiability — PASS, with proof details

Choose \(s_0\) satisfying \(q<s_0<s_*\), and choose \(\rho<\min\{M,s_0-q\}\). For every \(\|z_0\|_{H^2}<\rho\), put \(s=\|z_0\|_{H^2}+q<s_0\). All inequalities (6.1) of the existence investigation hold with uniform margin, using the common radius \(R_0=2C_Bs_0\) and a contraction constant at most \(1/2\). Its fixed-point construction gives a solution, positivity and endpoint traces; the separate weighted-energy argument gives uniqueness in the **whole actual weak class**. Therefore this open \(H^2\) ball is contained in \(\mathcal A_T^{\rm w}\), rather than merely a formal candidate. This relies on \(M>0\) and \(q<s_*\); no claim is made outside it.

For differentiability, regard the fixed-point map \(\Phi(y,z_0)\) on the open Banach product \(\mathcal E_T\times H^2(I)\), not just its restricted positive ball. The memory formulas are affine continuous in \((y,z_0)\): \(H^2(I)\hookrightarrow L^\infty(I)\), \(\mathcal E_T\hookrightarrow C_tH^1_x\hookrightarrow L^\infty_{t,x}\), and the time convolutions are bounded. The nonlinear forcing

\[
N(y,z_0)=-dyQy_t-byE(y,z_0)+k\lambda w(y,z_0)^2
\]

is a continuous polynomial map into \(L^2_{t,x}\): for example \(y\in L^\infty\) and \(Qy_t\in L^2\). Composing with the previous bounded linear heat–memory solver makes \(\Phi\) continuously Fréchet differentiable. Its uniform contraction bound implies \(\|D_y\Phi\|\le1/2\) at the base fixed point; \(I-D_y\Phi\) is invertible by a Neumann series. The Banach implicit-function theorem gives the unique \(C^1\) solution branch in a neighborhood of zero. Its restriction agrees with the actual forward map by full-class uniqueness. Differentiating the fixed-point equation gives (2.1), and bounded mean/endpoint trace maps give (4) of the analyzed report. This establishes the use of all \(H^2\) directions, without asserting differentiability on the entire admissible set.

## 9. Scope and final audit decision

The symmetry result is a correct mathematical reduction for the **nonzero-loading base**, not a resolution of the inverse problem. The full kernel remains unresolved: no complete moment theorem, missing boundary-to-interior implication, or nonzero invisible direction is established here. In particular, compactness does not imply a nonzero kernel, and a nontrivial derivative kernel would not automatically imply nonlinear non-injectivity; conversely nonlinear injectivity need not require a trivial derivative (a scalar cubic illustrates the logical distinction). The interior-vanishing theorem is conditional on an unmeasured interior premise and cannot be substituted for boundary unique continuation.

**Final mathematical verdict: PASS WITH CORRECTIONS** as detailed in §1. Preserve the exact force condition and all active terms, interpret modal sums via the proved function-space limits, and replace the unsupported sensor-detectability wording by the conditional statement given there. The specific active-kernel question remains **NOT ESTABLISHED**.
