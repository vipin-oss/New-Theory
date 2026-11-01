# Formulation A: forward-existence investigation

**Date:** 1 November 2026
**Outcome B — CONDITIONAL EXISTENCE**

## 1. Decision and exact scope

For the unchanged equations and nonzero sinusoidal loading, a direct fixed-point construction below gives:

1. **Local existence** in the previously specified strong-temperature/weak-initial class for every \(z_0\in H^2(0,L)\), including every \(z_0\in C_M\), with a positive lifetime depending on the data. The constructed temperature is at least \(\theta_*/2\) on that local interval. The construction does not require first-order corner compatibility and does not assert a corner-classical solution.
2. **Finite-horizon conditional existence** through the prescribed \(T=10/\lambda\), with \(\theta\ge\theta_*/2\), if the explicit data-only smallness inequalities in §6 hold. The same argument supplies a nonzero compatible initial field in \(\mathcal A_T^{\rm w}\) if the **fixed**, nonzero loading amplitude satisfies the stated threshold. The threshold is a sufficient mathematical condition, not a change to the experiment or a claimed necessity.
3. **Uniqueness in the full specified weak-initial class**, not merely in the fixed-point ball, follows by the energy argument in §7. The boundary observations are then well-defined in the required \(L^2\) space.

The previous documents specify \(g_*\) only as small and nonzero, without numerical values or an inequality matching §6. Therefore the data actually supplied do **not** establish that the fixed experiment satisfies the sufficient threshold. No unconditional nonemptiness assertion for its fixed amplitude is justified. General continuation to \(T\), a maximal existence interval for arbitrary data, and corner-classical existence remain **UNPROVED**. This is a mathematical conditional theorem, not a new constitutive theory or a novelty claim.

The five named prior reports were read and their definitions retained. Direction 1 remains rejected as a foundational continuum theory. Dr. Vipin Gupta is Principal Researcher and final decision-maker; Arena is Research Scholar / Mathematical Analyst. This is a single-agent mathematical verification, not a claim of independent certification. There is no inverse-injectivity analysis, simulation or manuscript.

## 2. Fixed system and exact principal operator

Put \(I=(0,L)\), \(P f=\bar f=L^{-1}\int_I f\), \(Q=I-P\), and

\[
D=a+k,\ r=k/D,\ \alpha=a/D,\ \beta=b/D,\ \mu=\lambda\alpha,\ d=b^2/D,\quad
m(t)=\frac{g_*}{L}\sin^2(\pi t/T),\quad T=10/\lambda.
\]

All parameters retain their prescribed signs, including \(b\ne0\), \(g_*\ne0\). Let \(p_0=z_0-\bar z_0\). The prescribed initial and bath temperatures are \(\theta_*\), so with \(y=\theta-\theta_*\), \(y(0)=0\) and \(y|_{\partial I}=0\). The exact memory representations are

\[
\bar z(t)=e^{-\lambda t}\bar z_0+\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds,\quad
p(t)=e^{-\mu t}p_0+\lambda\beta\int_0^t e^{-\mu(t-s)}Qy(s)ds.\tag{2.1}
\]

Set \(w=m-\bar z-\alpha p+\beta Qy\), \(E=m'+r(-\mu p+\lambda\beta Qy)\). The exact heat equation is

\[
M_\theta y_t=\kappa y_{xx}-b\theta E+k\lambda w^2,\qquad
M_\theta f=(c+d\theta)f-d\theta\bar f.\tag{2.2}
\]

Writing \(C(x)=c+d\theta(x)\), its inverse for positive bounded \(\theta\) is

\[
M_\theta^{-1}F=\frac{F}{C}+\frac{d\theta}{C}\,
\frac{\overline{F/C}}{\overline{c/C}}.\tag{2.3}
\]

Indeed \(1-\overline{d\theta/C}=\overline{c/C}\). Thus the exact principal spatial part on \(H^2\cap H^1_0\) is

\[
\mathcal P_\theta y=\kappa\left[\frac{y_{xx}}{C}+
\frac{d\theta}{C}\frac{\overline{y_{xx}/C}}{\overline{c/C}}\right].\tag{2.4}
\]

The second term is rank one **after** the second derivative, not a bounded operator on \(L^2\) itself. Under \(0<\theta_{\min}\le\theta\le\theta_{\max}<\infty\),

\[
\frac{c}{c+d\theta_{\max}}\le\overline{c/C}\le\frac{c}{c+d\theta_{\min}}\le1.\tag{2.5}
\]

### Weighted coercivity and meaning of parabolicity

For \(f\in L^2(I)\), use \((f,g)_{\theta^{-1}}=\int_I fg/\theta\,dx\). Then \(M_\theta\) is bounded and self-adjoint in this weighted Hilbert space and

\[
(M_\theta f,f)_{\theta^{-1}}
=c\int_I\frac{f^2}{\theta}dx+d\int_I(f-\bar f)^2dx
\ge c\|f\|_{\theta^{-1}}^2.\tag{2.6}
\]

Also \((M_\theta f,f)_{\theta^{-1}}\le(c+d\theta_{\max})\|f\|_{\theta^{-1}}^2\). Thus the inverse is positive and bounded with

\[
(M_\theta^{-1}F,F)_{\theta^{-1}}\ge
\frac{1}{c+d\theta_{\max}}\|F\|_{\theta^{-1}}^2.\tag{2.7}
\]

For the positive Dirichlet Laplacian \(L_D=-\partial_{xx}\), (2.7) implies

\[
(-\mathcal P_\theta y,L_Dy)_{\theta^{-1}}
\ge\frac{\kappa}{c+d\theta_{\max}}\|L_Dy\|_{\theta^{-1}}^2.\tag{2.8}
\]

These are uniform **generalized mass/principal-operator coercivity estimates** on a fixed positive bounded temperature range, including the nonlocal correction. The constants depend on \(c,d,\theta_{\max}\), and \(\kappa\); equivalence to the usual \(L^2\) norm also uses \(\theta_{\min}\), while \(L\) enters the average and boundary inequalities. They do not by themselves prove maximal regularity for an arbitrary time-dependent \(\theta\), nor that (2.4) is a local divergence-form uniformly elliptic operator. The proof below instead establishes a constant-reference linear problem and controls the exact nonlinear remainder.

Units agree: \([c]=\mathrm{Pa/K}\), \([d]=\mathrm{Pa/K^2}\), \([M_\theta]=\mathrm{Pa/K}\), so \(M_\theta y_t\) and the right side of (2.2) are Pa/s. \(Qy\) is K, \(\beta Qy\), \(p\), \(w\), \(m\) are dimensionless, and \(\kappa y_{xx}\) is Pa/s.

## 3. Linear problem: hypotheses and explicit estimate

All norms are taken in fixed, consistently chosen units. Define for \(0<\tau\le T\)

\[
\|y\|_{\mathcal E_\tau}=\|y_t\|_{L^2((0,\tau)\times I)}+
\|y_{xx}\|_{L^2((0,\tau)\times I)}+
\sup_{t\in[0,\tau]}\|y(t)\|_{H^1(I)},\tag{3.1}
\]

on \(\mathcal E_\tau=H^1(0,\tau;L^2)\cap L^2(0,\tau;H^2\cap H^1_0)\), \(y(0)=0\). This is complete; the standard Hilbert-space time trace gives \(y\in C([0,\tau];H^1_0)\). For \(K_x=\sqrt L\), \(\|y\|_{L^\infty((0,\tau)\times I)}\le K_x\|y\|_{\mathcal E_\tau}\) by \(|y(x)|\le\sqrt L\|y_x\|_2\).

Let \(C_*=c+d\theta_*\), \(M_*=cI+d\theta_*Q\), and consider, for \(f\in L^2((0,\tau)\times I)\), \(p_0\in L^2(I)\),

\[
M_*y_t-\kappa y_{xx}=f+Bp-CQy,\quad
p_t=-\mu p+\lambda\beta Qy,\quad y(0)=0,\ p(0)=p_0,\tag{3.2}
\]

where \(B=b\theta_*r\mu\), \(C=b\theta_*r\lambda\beta=\theta_*r\lambda d\). \(M_*\) is self-adjoint in ordinary \(L^2\), \((M_*v,v)\ge c\|v\|_2^2\), and \(\|M_*\|\le C_*\).

**Linear lemma.** Under precisely these hypotheses, (3.2) has a unique solution \(y\in\mathcal E_\tau\), \(p\in H^1(0,\tau;L^2)\). There is an explicit finite constant \(C_L\), depending only on the displayed coefficients, \(L,T\), with

\[
\|y\|_{\mathcal E_\tau}\le C_L(\|f\|_{L^2((0,\tau)\times I)}+\|p_0\|_2),\quad 0<\tau\le T.\tag{3.3}
\]

**Verification.** Let \(H=L/\pi\), \(q_B=|B|\), \(q_C=|C|\), and

\[
K_0=\max\left\{\frac{3q_B^2}{c}+|\lambda\beta|H,\ \frac{3q_C^2H^2/c+|\lambda\beta|H}{\kappa}\right\}.
\]

Testing the heat equation by \(y_t\), the memory equation by \(p\), and using \(\|Qy\|_2\le\|y\|_2\le H\|y_x\|_2\), gives for \(\Xi=\kappa\|y_x\|_2^2+\|p\|_2^2\)

\[
\Xi'(t)+c\|y_t\|_2^2\le(3/c)\|f\|_2^2+K_0\Xi(t).\tag{3.4}
\]

No boundary term survives because \(y_t\) has zero Dirichlet trace in the Galerkin calculation. Gronwall gives \(\sup\Xi^{1/2}\le J(\|f\|_2+\|p_0\|_2)\), with \(J=e^{K_0T/2}\max\{1,\sqrt{3/c}\}\). Integrating (3.4) yields \(\|y_t\|_2\le U(\|f\|_2+\|p_0\|_2)\), where \(U=\sqrt{(1+3/c+K_0TJ^2)/c}\). Equation (3.2) and Poincaré give an \(L^2\) bound for \(y_{xx}\). One usable explicit choice is

\[
C_L=U+\frac{C_*U+1+(q_B\sqrt T+q_CH\sqrt{T/\kappa})J}{\kappa}
+\frac{\sqrt{1+H^2}J}{\sqrt\kappa}.\tag{3.5}
\]

Here and below a space-time \(L^2\) norm is abbreviated \(\|\cdot\|_2\) when no ambiguity arises. A Galerkin proof uses Dirichlet sine functions for both unknowns: the finite-dimensional mass matrix is positive definite; (3.4) is uniform; the projected heat equation gives the uniform \(y_{xx}\) bound, and the memory equation bounds \(p_t\) in \(L^2\). Weak compactness gives a solution, and the equations and initial traces pass to the limit; the same energy estimate with zero data proves uniqueness. The time-continuity in \(H^1_0\) follows from the standard \(H^1_tL^2_x\cap L^2_tH^2_x\) trace/energy argument. This establishes the needed linear result directly; no nonlocal quasilinear theorem is imported.

## 4. Exact fixed point and local existence

For an input \(y\in\mathcal E_\tau\), define \(p[y]\) and \(\bar z\) by (2.1), and put

\[
E[y]=m'+r(-\mu p[y]+\lambda\beta Qy),\quad
w[y]=m-\bar z-\alpha p[y]+\beta Qy.
\]

The linear part (3.2) incorporates exactly \(-b\theta_*r(-\mu p+\lambda\beta Qy)\). Define the nonlinear forcing

\[
N[y]=-d\,y\,Qy_t-b\,y\,E[y]+k\lambda w[y]^2.\tag{4.1}
\]

Let \(\Phi(y)\) be the heat component of the unique linear solution (3.2) with \(f=-b\theta_*m'+N[y]\) and the prescribed \(p_0\). A fixed point solves (2.2) exactly: \(M_*=cI+d\theta_*Q\), and moving \(-d yQy_t\) to the left gives \(M_{\theta_*+y}y_t\). No term is dropped.

**Local theorem.** For every \(z_0\in H^2(I)\), including \(z_0\in C_M\), and the prescribed fixed nonzero \(g_*\), there is \(0<\tau\le T\) and a solution \(y\in\mathcal E_\tau\), \(z\in H^1(0,\tau;L^2)\), satisfying the unchanged reduced and reconstructed equations, initial/boundary data, bounded \(\theta,p,w\), and \(\theta\ge\theta_*/2\). It is unique among solutions in the weak-initial class of §7 on that interval.

**Fixed-point verification.** Let \(y_L\) solve (3.2) with \(f=-b\theta_*m'\). By (3.3) it exists on the full fixed \([0,T]\). Because \(y_L(0)=0\), its restriction satisfies \(\|y_L\|_{\mathcal E_\tau}\to0\) as \(\tau\downarrow0\). The function \(w[0]=m-\bar z-\alpha e^{-\mu t}p_0\) is bounded because \(z_0\in H^2\); hence \(\|w[0]^2\|_{L^2((0,\tau)\times I)}\to0\). For fixed data, (2.1), \(\|Qy\|_\infty\le2K_x\|y\|_{\mathcal E_\tau}\), and \(\|Qy_t\|_2\le\|y_t\|_2\) show that for inputs in an \(\mathcal E_\tau\)-ball of radius \(R\),

\[
\|N[y]-N[\tilde y]\|_2\le [2dK_xR+\sqrt\tau\,C_{\rm data,T}(1+R)]\,\|y-\tilde y\|_{\mathcal E_\tau},\tag{4.2}
\]

for finite \(C_{\rm data,T}\); its terms arise respectively from \(yQy_t\), \(yE\), and \(w^2\). Set \(R_\tau=2(\|y_L\|_{\mathcal E_\tau}+C_L k\lambda\|w[0]^2\|_2)\). Then \(R_\tau\to0\), and for sufficiently small \(\tau\), \(K_xR_\tau\le\theta_*/2\) and \(C_L[2dK_xR_\tau+\sqrt\tau C_{\rm data,T}(1+R_\tau)]\le1/2\). Equation (3.3) and (4.2) then make \(\Phi\) a contraction mapping that ball into itself. Banach's fixed-point theorem applies because the ball is closed in the complete \(\mathcal E_\tau\). Positivity follows directly from \(|y|\le K_xR_\tau\); it is not assumed in the construction. The uniqueness in the full weak class is proved separately in §7. This theorem establishes local existence without requiring \(z_0\) to satisfy classical corner conditions, but it does not establish continuous corner derivatives.

## 5. Bounds used for the finite horizon

Let \(S_L\) be any fixed explicit Sobolev-embedding constant satisfying \(\|f\|_\infty\le S_L\|f\|_{H^2(I)}\), e.g. any valid interval Sobolev constant; it is independent of data. Write

\[
\eta=\|z_0\|_{H^2},\quad q=|g_*|/L,\quad s=\eta+q,\quad Z=K_x\|y\|_{\mathcal E_T}.
\]

From (2.1), \(|m|\le q\), \(|m'|\le\pi q/T\), \(|\bar z|\le S_L\eta+q\), \(\|p_0\|_\infty\le2S_L\eta\), and

\[
\|p[y]\|_\infty\le2S_L\eta+2\lambda|\beta|TZ.\tag{5.1}
\]

It follows that

\[
\|E[y]\|_\infty\le A_s s+A_R\|y\|_{\mathcal E_T},\quad
\|w[y]\|_\infty\le W_s s+W_R\|y\|_{\mathcal E_T},\tag{5.2}
\]

where the explicitly computable constants are

\[
\begin{aligned}
A_s&=\pi/T+2r\mu S_L,&A_R&=2r\lambda|\beta|(1+\mu T)K_x,\\
W_s&=2+(1+2\alpha)S_L,&W_R&=2|\beta|(1+\alpha\lambda T)K_x.
\end{aligned}\tag{5.3}
\]

In (5.2) the time-dependent forcing \(m'\), the mean \(\bar z\), memory and the relaxation heating are all retained. For inputs in a ball \(\|y\|_{\mathcal E_T}\le R\), (5.2) and the corresponding difference bounds yield

\[
\|N[y]\|_2\le C_N(s+R)^2,\qquad
\|N[y]-N[\tilde y]\|_2\le C_N'(s+R)\|y-\tilde y\|_{\mathcal E_T},\tag{5.4}
\]

where one sufficient choice is

\[
\begin{aligned}
C_N={}&dK_x+|b|K_x\sqrt{LT}\max\{A_s,A_R\}
+k\lambda\sqrt{LT}\max\{W_s,W_R\}^2,\\
C_N'={}&2dK_x+|b|K_x\sqrt{LT}(A_s+2A_R)
+2k\lambda\sqrt{LT}\,W_R(W_s+W_R).
\end{aligned}\tag{5.5}
\]

For instance, \(\|yQy_t-\tilde yQ\tilde y_t\|_2\le2K_xR\|y-\tilde y\|_{\mathcal E_T}\), and the \(w^2\) difference is \((w+\tilde w)(w-\tilde w)\). The mean projection \(Q\) has \(L^2\) norm one and \(L^\infty\) norm at most two. No estimate treats a quadratic heat source as automatically bounded without (5.1)–(5.2).

## 6. Finite-horizon small-data theorem and positivity

Define

\[
C_B=C_L\left(|b|\theta_*\frac{\pi\sqrt{LT}}{T}+2\sqrt L\,S_L\right)>0,\qquad R=2C_Bs.
\]

For the prescribed fixed \(T\), suppose the **data-only inequalities**

\[
\begin{aligned}
&C_LC_N(1+2C_B)^2s\le C_B,\\
&C_LC_N'(1+2C_B)s\le\tfrac12,\\
&2K_xC_Bs\le\tfrac12\theta_*
\end{aligned}\tag{6.1}
\]

hold. Every constant in (6.1) is fixed by the given material parameters, \(L,T\), and the chosen interval Sobolev constant, through (3.5) and (5.3)–(5.5). The inequalities are explicit, although generally conservative; they use fixed units because the full \(H^2\) norm combines derivatives of different dimensions. They are not inferred from the word “small.”

**Theorem.** Under (6.1), \(z_0\in H^2(I)\), and the frozen sinusoidal \(g_*\ne0\), the original problem has a solution on the entire specified \([0,T]\) in the weak-initial class (5.1) of the topology audit. Its temperature satisfies

\[
\theta_*/2\le\theta(x,t)\le3\theta_*/2\quad\text{on }[0,L]\times[0,T].\tag{6.2}
\]

It is the unique solution in that full class by §7. Force and both labeled endpoint heat-flux traces belong to \(L^2(\delta,T)\).

**Proof.** From (3.3), the linear solution with forcing \(-b\theta_*m'\) and initial \(p_0\) has \(\|y_L\|_{\mathcal E_T}\le C_Bs\). In the closed ball of radius \(R\), (3.3) and (5.4) give

\[
\|\Phi(y)\|_{\mathcal E_T}\le C_Bs+C_LC_N(s+R)^2\le2C_Bs=R.
\]

The second inequality in (6.1) gives \(\|\Phi(y)-\Phi(\tilde y)\|_{\mathcal E_T}\le\tfrac12\|y-\tilde y\|_{\mathcal E_T}\). Banach's theorem yields a unique fixed point **in that ball**. The third inequality implies \(\|y\|_\infty\le K_xR\le\theta_*/2\), proving (6.2) from data alone. In particular, the positivity estimate does not depend on an assumed solution norm: the norm bound has just been obtained by contraction. Representation (2.1) makes \(p,w,\theta\) bounded, and yields \(z\in H^1_tL^2_x\). The exact reduced equations imply the original stress, strain, memory and thermal laws after reconstruction. The endpoints \(u(0)=0\), \(u(L)=g\) hold because \(\bar\varepsilon=m\), and \(y\in L^2_t(H^2\cap H^1_0)\) gives both bath traces. The \(H^2\) spatial trace theorem gives \(y_x(0,\cdot),y_x(L,\cdot)\in L^2(0,T)\); the stress formula gives the force trace. This establishes all claims except full-class uniqueness, which §7 proves.

**Nonzero compatible state.** Define the positive threshold

\[
s_*:=\min\left\{\frac{C_B}{C_LC_N(1+2C_B)^2},\
\frac{1}{2C_LC_N'(1+2C_B)},\
\frac{\theta_*}{4K_xC_B}\right\}.\tag{6.3}
\]

The constants are positive for the frozen nonzero coupling. If the **given** loading obeys \(0<|g_*|/L<s_*\), choose a sufficiently small nonzero member \(z_\xi=\xi\sin(2\pi x/L)+h(\xi)\cos(2\pi x/L)\) of the earlier compatibility family so that \(\|z_\xi\|_{H^2}\le M\) and \(\|z_\xi\|_{H^2}+|g_*|/L<s_*\). The earlier implicit-function calculation proves \(z_\xi\in C_M\) and \(\|z_\xi\|_{H^2}\to0\). Then (6.1) holds and §7 makes this state a member of \(\mathcal A_T^{\rm w}\). Thus **conditional on that explicit bound on the already fixed amplitude**, \(\mathcal A_T^{\rm w}\) contains nonzero compatible data. A zero initial memory field is also covered when the bound holds, but its solution is driven by nonzero loading and is not an equilibrium. The supplied record gives no numerical \(g_*\) or constants, so the condition is not verified for the actual unspecified fixed amplitude.

## 7. Uniqueness in the specified weak-initial class

This step is needed because contraction on a ball alone would not rule out another large solution in the class used to define \(\mathcal A_T^{\rm w}\). Let two solutions in that class have identical data. Write \(V=\theta_1-\theta_2\), \(P=p_1-p_2\), and \(W=w_1-w_2\). Their \(\bar z\) agree and

\[
P_t=-\mu P+\lambda\beta QV,\qquad W=-\alpha P+\beta QV,\quad P(0)=V(0)=0.
\]

As in the prior audit, subtraction gives

\[
M_{\theta_1}V_t-\kappa V_{xx}=-bV\varepsilon_{2t}-b\theta_1rP_t+k\lambda(w_1+w_2)W.\tag{7.1}
\]

The class has \(\theta_i,p_i,w_i\in L^\infty\), \(\theta_i\ge\theta_*/2\), \(\theta_{it},\varepsilon_{it}\in L^2\), \(\theta_i\in C([0,T];H^1)\), and \(V\in L^2_tH^2_x\cap H^1_tL^2_x\). Test (7.1) by \(V/\theta_1\), which belongs to \(H^1_0\) for a.e. time. Define

\[
\mathscr E(t)=\frac c2\int_I\frac{V^2}{\theta_1}dx+\frac d2\|QV\|_2^2+\frac12\|P\|_2^2.\tag{7.2}
\]

Since \(\theta_1\) is positive and bounded, \(\mathscr E\) controls \(\|V\|_2^2+\|P\|_2^2\). The weighted mass term is \(\mathscr E'\) plus \((c/2)\int V^2\theta_{1t}/\theta_1^2\), after adding the \(P\)-equation. Integration by parts produces the nonnegative term \(\kappa\int V_x^2/\theta_1\) and the cross term \(-\kappa\int V_xV\theta_{1x}/\theta_1^2\). There is no boundary contribution because \(V=0\) at both endpoints.

In one dimension, \(\|V\|_4^2\le C\|V\|_2^{3/2}\|V_x\|_2^{1/2}\) and \(\|V\|_\infty\le C\|V\|_2^{1/2}\|V_x\|_2^{1/2}\). Young's inequality therefore bounds the terms containing \(\theta_{1t}\) and \(\varepsilon_{2t}\) by an arbitrarily small multiple of \(\|V_x\|_2^2\) plus \(C(\|\theta_{1t}\|_2^{4/3}+\|\varepsilon_{2t}\|_2^{4/3})\|V\|_2^2\). The gradient cross term is bounded similarly by a small multiple of \(\|V_x\|_2^2\) plus \(C\|\theta_{1x}\|_2^4\|V\|_2^2\). Bounded \(w_1+w_2\), the ODE for \(P\), and \(W=-\alpha P+\beta QV\) bound the remaining terms by \(C(\|V\|_2^2+\|P\|_2^2)\). Consequently

\[
\mathscr E'(t)+c_0\|V_x\|_2^2\le A(t)\mathscr E(t),\quad
A(t)=C\{1+\|\theta_{1x}(t)\|_2^4+\|\theta_{1t}(t)\|_2^{4/3}+\|\varepsilon_{2t}(t)\|_2^{4/3}\}\in L^1(0,T).
\tag{7.3}
\]

The coefficient is integrable because \(\theta_1\in C_tH^1_x\) and the time derivatives are in \(L^2\). The chain rule for (7.2) and the test follow by smooth approximation: \(V,\theta_1\) are bounded, \(\theta_1\) is bounded below, and their time derivatives are in \(L^2\). Gronwall and \(\mathscr E(0)=0\) give \(V=P=0\); the reconstructed \(z,u,\sigma\) then agree. This proves uniqueness **within the weak-initial class**, not among arbitrary distributional solutions.

## 8. Continuation, a priori limits and unresolved claims

The local theorem supplies an interval \([0,\tau]\); the conditional theorem solves directly on the full fixed \([0,T]\), rather than assuming local solutions continue. Estimates (5.1)–(5.2) control memory, heating and the mean term on the fixed-point ball, while (6.2) supplies both upper and lower temperature bounds there. The \(\mathcal E_T\) bound controls \(L^\infty_tH^1_x\) and \(L^2_tH^2_x\), not \(L^\infty_tH^2_x\). The strictly positive lower bound is obtained without the earlier solution-dependent exponential comparison.

For data not satisfying (6.1), **continuation to \(T\) is unproved**. The local fixed-point construction around the initial constant temperature does not by itself establish restart theory at arbitrary positive-time states, an actual maximal lifetime, or an exact blow-up alternative. Plausible obstacles include loss of a positive lower temperature bound, unbounded temperature/gradient/memory norms, or failure of the relevant nonlocal maximal-regularity estimates; these are not claimed to be a proved exhaustive continuation criterion. A formal total-energy identity does not provide the missing uniform \(\mathcal E_T\) estimate. No general corner-classical existence or nonempty \(\mathcal A_T^{\rm cl}\) has been proved even for \(C_M\); the weak solution's existence does not prove the required continuity of \(\theta_t,\theta_{xx}\) through the corners.

The actual values of \(g_*\), \(L\), \(a,k,\lambda,c,\kappa,b,\theta_*\) and \(M\) are not numerically specified in the record. Thus (6.3) is a quantitative sufficient threshold but its validity for the fixed experiment is **unverified**. This prevents promotion of outcome B to unconditional outcome A.

## 9. Sources and theorem-hypothesis verification

| Result / source | Hypotheses checked and actual use |
|---|---|
| Banach fixed-point theorem | A contraction on a nonempty closed ball of a complete metric space has one fixed point in that ball. \(\mathcal E_\tau\) is Banach and the ball is closed; (4.2) or (6.1) verifies contraction and self-mapping. This theorem does not itself establish uniqueness outside the ball; §7 addresses that separately. |
| Interval Poincaré, Sobolev, trace, and time-trace inequalities | \(I\) is bounded; \(H^1_0\) provides Poincaré and \(\|y\|_\infty\le\sqrt L\|y_x\|_2\); \(H^2\) provides endpoint gradient traces. The time-space Hilbert trace is used with \(H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\). These standard results are applied only with the stated spaces. |
| Gronwall and Galerkin compactness | Finite positive \(c,\kappa\), bounded coefficients and \(f\in L^2\) yield (3.4); the explicit energy estimate and projected equation justify weak compactness and passage to the exact constant-mass linear problem. Uniqueness follows from the zero-data estimate. No claim is made that a general nonautonomous result automatically applies. |
| N. Lindemulder, [*Maximal Regularity with Weights for Parabolic Problems with Inhomogeneous Boundary Conditions*](https://arxiv.org/html/1702.02803), arXiv:1702.02803v2, introduction and theorem overview inspected | Addresses linear differential boundary problems under ellipticity, boundary-complementing and weighted-space hypotheses. The nonlocal mass inverse and memory here are not verified as that theorem's hypotheses. **Not invoked for the proof**; it is context for trace/maximal-regularity issues. |
| V. Colao and L. Muglia, [*Solutions to nonlocal evolution equations governed by non-autonomous forms and demicontinuous nonlinearities*](https://arxiv.org/html/2110.03565), arXiv:2110.03565v3, introduction and Theorem 1.1 inspected | Quotes Lions' weak-form theorem for a bounded coercive form, yielding \(L^2_tV\cap H^1_tV'\); the paper's stronger results impose additional regularity hypotheses. That conclusion alone does not supply the \(L^2_tH^2_x\) endpoint-flux traces here. **Not invoked as a theorem for (2.2).** |
| S. Bechtel, C. Mooney and M. Veraar, [*Counterexamples to maximal regularity for operators in divergence form*](https://link.springer.com/article/10.1007/s00013-024-02014-9), *Arch. Math.* 123 (2024), 199–209, DOI 10.1007/s00013-024-02014-9; abstract inspected | Shows that coercivity alone does not imply every desired \(L^2\) maximal-regularity property for time-dependent divergence-form operators. This is a caution, not a counterexample to (2.2); the proof above uses a separately established constant-mass linear lemma. |

The linear and nonlinear estimates are deductions here, not asserted novel. The earlier audit's inaccessible thermoelastic sources remain inaccessible; their exact theorems are not attributed or used. The search is not exhaustive.

## 10. Final recommendation

**Outcome B — CONDITIONAL EXISTENCE.** Local existence for the exact active system is established in the specified strong-temperature/weak-initial setting. A full-horizon, positive-temperature, unique solution and a nonzero compatible member of \(\mathcal A_T^{\rm w}\) follow under the explicit fixed-amplitude/data threshold (6.3). The frozen experiment's actual parameters have not been shown to meet it, so nonemptiness for the unspecified fixed amplitude and unconditional continuation remain unresolved. \(\mathcal A_T^{\rm cl}\) is not shown nonempty.

The next decision belongs to Dr. Vipin Gupta. No inverse injectivity, inverse stability, simulation, manuscript, or new constitutive theory is pursued here.
