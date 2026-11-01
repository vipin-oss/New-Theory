# Independent mathematical and prior-art audit: Formulation A existence

**Date:** 1 November 2026
**Publication-gate verdict: MATHEMATICALLY CORRECT BUT ROUTINE**

## 1. Executive conclusion and limits of independence

The local and conditional fixed-horizon existence/uniqueness claims survive the independent calculations below, **when the inequalities and norms are read as numerical quantities in a fixed system of units**, as in the investigated report. No algebraic error, invalid Galerkin limit, circular use of positivity, or counterexample to the claimed theorem was found. The explicit constants are sufficient, not sharp. A dimensional clarification and several proof details should be supplied before using the threshold as a physical engineering specification (§§4, 6, 10); these do not invalidate the numerical-unit mathematical assertion. This audit does not prove that the fixed, unspecified amplitude satisfies the threshold, that all data continue to \(T\), or that the classical admissible set is nonempty.

The result is useful as a **model-specific forward prerequisite**. Its construction uses a standard constant-reference parabolic estimate, a Lipschitz perturbation, a contraction on a small ball, and a weighted energy estimate. The searched literature establishes closely related strong/weak thermomechanical existence results and the same general techniques. No checked primary source is shown to contain the **exact** rank-one operator and all of this problem's boundary, loading and solution-class hypotheses. Therefore “routine” is an assessment of the demonstrated mathematical contribution, **not** a claim that an exact identical theorem has been located or that the literature search is exhaustive. A new verification for a particular system is not automatically a new general theorem or a publishable advance. No publication is recommended; novelty and scientific-importance gates are not met.

This is a fresh derivation and literature check by Arena, conducted in the same research environment, not a second human referee or an independent certification by the designated supervisor ChatGPT. The source report is left unchanged. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. Direction 1 remains rejected as a foundational continuum theory. There is no inverse analysis, simulation, manuscript, or change of physical assumptions.

## 2. Audit setup: frozen equations, notation, and classification

The original formulation is

\[
\sigma_x=0,\quad \sigma=(a+k)\varepsilon-b(\theta-\theta_*)-kz,\quad
z_t=\lambda(\varepsilon-z),\quad
c\theta_t=\kappa\theta_{xx}-b\theta\varepsilon_t+k\lambda(\varepsilon-z)^2,
\tag{A}
\]

\(\varepsilon=u_x\), \(u(0,t)=0\), \(u(L,t)=g(t)\), \(g(t)=g_*\sin^2(\pi t/T)\), \(T=10/\lambda\); \(\theta(0,t)=\theta(L,t)=\theta_*\), \(\theta(x,0)=\theta_*\), \(z(x,0)=z_0(x)\in H^2(0,L)\). Parameters have exactly the frozen signs and \(b,g_*\ne0\). The weak-initial class is exactly §5.1 of `direction-2-formulation-A-admissible-topology.md`, including \(\theta\ge\theta_*/2\), bounded \(\theta,p,w\), and the stated strong-temperature regularity. We do not redefine its topology.

Use \(\langle f\rangle=L^{-1}\int_0^L f\), \(Qf=f-\langle f\rangle\), \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\mu=\lambda\alpha\), \(d=b^2/D\), \(m=g/L\), \(y=\theta-\theta_*\), \(p=Qz\), \(v=\langle z\rangle\), \(w=\varepsilon-z\). The average is an orthogonal projection in \(L^2\); \(\|Q\|_{2\to2}=1\) and \(\|Q\|_{\infty\to\infty}\le2\).

| Source-report item | Audit finding |
|---|---|
| Reduction, mass/inverse and weighted bounds (2.1)–(2.8) | Correct under positive bounded \(\theta\); (2.8) is not a general nonautonomous maximal-regularity theorem. |
| (3.4), Galerkin and explicit (3.5) | Correct with the projected mass kept intact; explicit verification below. |
| (4.1), local (4.2), Banach ball | Correct; local inhomogeneous ball is nonempty and self-mapping, with contraction constant uniform for small time. |
| (5.1)–(5.5), (6.1), (6.3) | Correct as numerical-unit inequalities. Smallness is sufficient and not verified for the fixed experiment. The cited \(S_L\) can be made explicit; a dimensionless rewrite is advisable. |
| (7.1)–(7.3), full-class uniqueness | Correct for the stated class, including the weighted test and integrability; rigorous chain-rule justification is given below. |
| Original equations, observation traces | Reconstructed equations hold a.e.; boundary conditions and initial values hold in their specified traces, not as unproved corner-classical derivatives. |
| Original proof presentation | Several justifications are terse. They are completed below; no material change to the theorem or its solution class is needed. |

## 3. Independent reduction and reconstruction

Mechanical equilibrium makes \(\sigma\) spatially constant. Integrating the stress relation and using \(\langle\varepsilon\rangle=m\) gives

\[
\sigma=Dm-b\langle y\rangle-kv,\qquad
\varepsilon=m+r p+\beta Qy.\tag{3.1}
\]

Hence

\[
w=m-v-\alpha p+\beta Qy,\quad
v_t=\lambda(m-v),\quad p_t=-\mu p+\lambda\beta Qy.\tag{3.2}
\]

The corresponding ODE solutions are

\[
v(t)=e^{-\lambda t}v_0+\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds,\quad
p(t)=e^{-\mu t}p_0+\lambda\beta\int_0^t e^{-\mu(t-s)}Qy(s)ds.
\tag{3.3}
\]

Differentiation of (3.1) in \(L^2\) gives \(\varepsilon_t=m'+rp_t+\beta Qy_t\). Substitute this in (A) and set \(E=m'+rp_t\):

\[
(cI+d\theta Q)y_t=\kappa y_{xx}-b\theta E+k\lambda w^2.\tag{3.4}
\]

The coefficient of \(Qy_t\) is \(b\beta\theta=d\theta\); its sign in (3.4) is positive after moving it to the left. Conversely, from \(y,p,v\) solve (3.3), let \(z=v+p\) and define \(u(x,t)=\int_0^x\varepsilon(\xi,t)d\xi\). Because \(p_0=Qz_0\) and \(Qy\) has zero mean, \(\langle p\rangle=0\) for all \(t\), and \(\langle\varepsilon\rangle=m\). Thus \(u(0,t)=0\), \(u(L,t)=Lm=g(t)\); (3.1) satisfies the original constitutive stress with \(\sigma_x=0\); (3.2) yields \(z_t=\lambda w\); and (3.4) yields the original heat equation. At \(t=0\), \(z=z_0\), \(y=0\), and \(u_0(x)=r\int_0^xQz_0\). The equalities hold in the stated \(L^2\)-Sobolev/trace senses; no corner derivative is asserted.

## 4. Mass inverse, coercivity, and dimensions

For \(M_\theta h=ch+d\theta Qh\), let \(C(x)=c+d\theta(x)\). Solving \(M_\theta h=F\) first gives \(h=F/C+(d\theta/C)\langle h\rangle\). Averaging this identity yields

\[
\langle h\rangle=\frac{\langle F/C\rangle}{\langle c/C\rangle},\qquad
M_\theta^{-1}F=F/C+(d\theta/C)\frac{\langle F/C\rangle}{\langle c/C\rangle}.\tag{4.1}
\]

When \(0<\ell\le\theta\le u<\infty\), \(c/(c+du)\le\langle c/C\rangle\le c/(c+d\ell)\). Thus the denominator is strictly positive. This is an invertible multiplication operator plus a rank-one correction; it is **not** correct to drop the nonlocal term from the spatial principal operator.

In \(H_\theta=L^2(I,dx/\theta)\), direct polarization gives, for real \(h,j\),

\[
(M_\theta h,j)_{H_\theta}=c\int hj/\theta+d\bigl(\int hj-L\langle h\rangle\langle j\rangle\bigr),
\]

which is symmetric and satisfies

\[
c\|h\|_{H_\theta}^2\le(M_\theta h,h)_{H_\theta}
\le(c+du)\|h\|_{H_\theta}^2.
\tag{4.2}
\]

For example, the upper bound uses \(\|Qh\|_2\le\|h\|_2\le\sqrt u\|h\|_{H_\theta}\). The spectral bound for this positive self-adjoint bounded operator gives

\[
(M_\theta^{-1}F,F)_{H_\theta}\ge(c+du)^{-1}\|F\|_{H_\theta}^2.
\tag{4.3}
\]

With \(A=-\partial_{xx}\) on \(H^2\cap H^1_0\), \(\mathcal P_\theta=-\kappa M_\theta^{-1}A\), so \((-\mathcal P_\theta h,Ah)_{H_\theta}\ge\kappa(c+du)^{-1}\|Ah\|_{H_\theta}^2\). This is exactly the report's (2.6)–(2.8). It is a coercive pairing with \(Ah\), **not** an assertion of a pointwise maximum principle or a complete time-dependent maximal-regularity theorem. The weighted Hilbert norm is equivalent to ordinary \(L^2\) with constants involving \(\ell,u\).

The equations themselves have consistent physical units: \([b]=\mathrm{Pa/K}\), \([d]=\mathrm{Pa/K^2}\), \([c]=\mathrm{Pa/K}\), \([\kappa]=\mathrm{Pa\,m^2/(K\,s)}\), \([m,p,w]=1\). However, the report's full \(H^2\) norm, \(\mathcal E\)-norm, and constants combine derivatives and quantities of different dimensions. A fixed numerical unit convention makes these perfectly well-defined real inequalities, but their symbols are **not unit-invariant physical sums**. To communicate (6.1) as a physical threshold, first fix positive reference length, time, temperature and pressure scales, express every quantity and every norm in the resulting dimensionless variables, and rederive the numerical constants in those variables. Merely switching meters to millimeters without transforming all coefficients and norm definitions can change the numerical test. This is a precision issue, not a demonstrated counterexample to the fixed-unit theorem.

## 5. Constant-reference problem and its actual Galerkin bound

Put \(M_0=cI+d\theta_*Q\), \(B=b\theta_*r\mu\), \(C=b\theta_*r\lambda\beta\), \(H=L/\pi\). Given \(f\in L^2((0,\tau)\times I)\), \(p_0\in L^2(I)\), consider

\[
M_0 y_t-\kappa y_{xx}=f+Bp-CQy,\qquad p_t=-\mu p+\lambda\beta Qy,\quad y(0)=0,\ p(0)=p_0.\tag{5.1}
\]

Let \(\Pi_n\) project on the first \(n\) Dirichlet eigenfunctions, and impose both equations after projection with initial \(\Pi_np_0\). The heat mass matrix is \(\Pi_nM_0|_{\Pi_nL^2}\), positive definite since \((M_0h,h)\ge c\|h\|_2^2\). **It is not assumed that \(Q\) preserves the sine subspace.** The projected ODE system therefore exists and is unique.

Test the heat equation by \(2y_{n,t}\) and the memory equation by \(2p_n\). Three Young inequalities absorb exactly \(c\|y_{n,t}\|^2\) from the \(2c\|y_{n,t}\|^2\) mass term, while

\[
2|\lambda\beta|\,\|p_n\|_2\|Qy_n\|_2
\le |\lambda\beta|H(\|p_n\|_2^2+\|y_{n,x}\|_2^2),\qquad
\|Qy_n\|_2\le H\|y_{n,x}\|_2.
\]

Discarding \(-2\mu\|p_n\|_2^2\) gives, with \(X_n=\kappa\|y_{n,x}\|_2^2+\|p_n\|_2^2\),

\[
X_n'+c\|y_{n,t}\|_2^2\le\frac3c\|f\|_2^2+K_0 X_n,
\quad K_0=\max\!\left\{\frac{3B^2}{c}+|\lambda\beta|H,\frac{3C^2H^2/c+|\lambda\beta|H}{\kappa}\right\}.\tag{5.2}
\]

This is exactly (3.4). The Galerkin space consists of Dirichlet Laplacian eigenfunctions, so \(y_{n,xx}\) also lies in it. The projected equation gives

\[
\kappa\|y_{n,xx}\|_2\le(c+d\theta_*)\|y_{n,t}\|_2+\|f\|_2+|B|\|p_n\|_2+|C|\|Qy_n\|_2.\tag{5.3}
\]

Thus (5.2) genuinely provides \(y_{n,t}\) and \(y_{n,xx}\) uniformly in \(L^2_{t,x}\), plus \(p_n\) in \(L^\infty_tL^2_x\), and the projected memory equation provides \(p_{n,t}\in L^2_{t,x}\). Extract weak/weak-* subsequences, using (5.3) and the interval elliptic estimate to obtain \(y\in L^2_t(H^2\cap H^1_0)\), \(y_t\in L^2_{t,x}\); \(p\in H^1_tL^2_x\). Since \(\Pi_n\phi\to\phi\) strongly, all linear terms pass to the limit without asserting that \(Q\) and \(\Pi_n\) commute. The continuous time traces supply the prescribed initial data. Repeating (5.2) for a zero-data difference proves uniqueness.

For the explicit report constant let \(A_D=\|f\|_{L^2_{t,x}}+\|p_0\|_2\),

\[
J=e^{K_0T/2}\max\{1,\sqrt{3/c}\},\quad
U=\sqrt{(1+3/c+K_0TJ^2)/c},\quad C_0=c+d\theta_*.
\]

Gronwall gives \(\sup_tX^{1/2}\le JA_D\). Integration of (5.2) gives \(\|y_t\|_2\le UA_D\). By (5.3),

\[
\|y_{xx}\|_2\le\kappa^{-1}[C_0U+1+(|B|\sqrt T+|C|H\sqrt{T/\kappa})J]A_D,
\quad \sup_t\|y(t)\|_{H^1}\le\sqrt{(1+H^2)/\kappa}\,J A_D.
\]

Summing these three bounds yields precisely the proposed \(C_L\) in (3.5). In particular the formula is a uniform bound for every \(0<\tau\le T\), not only for \(\tau=T\). Independently, \(M_0^{-1}=c^{-1}P+(c+d\theta_*)^{-1}Q\), where \(P=I-Q\); this verifies its invertibility and norm \(1/c\). The Galerkin proof does **not** need to treat \(M_0^{-1}\) as commuting with the Dirichlet Laplacian.

## 6. Functional space, fixed point, and nonlinear differences

Let \(\mathcal E_\tau=\{y\in H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0):y(0)=0\}\), with the report's sum of \(\|y_t\|_2\), \(\|y_{xx}\|_2\), and \(\sup_t\|y\|_{H^1}\). Dirichlet Poincaré and the one-dimensional elliptic estimate make this equivalent to the standard intersection norm on the zero-initial subspace; Hilbert-space trace theory gives \(y\in C_tH^1_0\), so the initial condition is closed. It is a Banach space. Also \(\|y\|_{L^\infty_{t,x}}\le K\|y\|_{\mathcal E_\tau}\), \(K=\sqrt L\).

For an input \(h\) let \(p[h]\) solve (3.3), \(v\) solve (3.3), and write \(E[h]=m'+rp[h]_t\), \(w[h]=m-v-\alpha p[h]+\beta Qh\). Expanding (3.4) about \(\theta_*\) shows that the output heat field solves (5.1), with the original \(p_0\), and forcing

\[
f_h=-b\theta_*m'+N[h],\qquad
N[h]=-d hQh_t-bhE[h]+k\lambda w[h]^2.\tag{6.1}
\]

The memory variable in the *output* is determined by (5.1); at a fixed point output and input coincide, so the input and output memory fields coincide by ODE uniqueness. This avoids a potential circularity in the definition of the map. For each input, \(h\) and \(p[h],w[h]\) are bounded in space-time, while \(h_t\in L^2\); hence \(N[h]\in L^2\) before solving the linear equation.

If \(\|h\|,\|\tilde h\|\le R\) in \(\mathcal E_\tau\), \(\Delta h=h-\tilde h\), then

\[
\|hQh_t-\tilde hQ\tilde h_t\|_2\le 2KR\|\Delta h\|_{\mathcal E_\tau}.\tag{6.2}
\]

For the other terms, \(\|p[h]-p[\tilde h]\|_\infty\le 2\lambda|\beta|TK\|\Delta h\|\); therefore, with finite constants depending only on the fixed data and \(T\),

\[
\|E[h]-E[\tilde h]\|_\infty+\|w[h]-w[\tilde h]\|_\infty\le C_1\|\Delta h\|,
\quad \|E[h]\|_\infty+\|w[h]\|_\infty\le C_2(1+R).
\]

Taking \(L^2\) norms over an interval of length \(\tau\) and using the space-time supremum yields

\[
\|N[h]-N[\tilde h]\|_2\le[2dKR+\sqrt\tau C_{\rm data,T}(1+R)]\|\Delta h\|,
\tag{6.3}
\]

with the factor \(\sqrt L\) included in \(C_{\rm data,T}\). This independently verifies (4.2).

Let \(Y_L\) be the linear output with forcing \(-b\theta_*m'\) on \([0,T]\). Its restricted \(\mathcal E_\tau\)-norm tends to zero, including the \(\sup H^1\) part, because \(Y_L\in C_tH^1_0\), \(Y_L(0)=0\), and its other two norms are absolutely continuous in time. \(w[0]\) is bounded since \(z_0\in H^2\), so \(\|w[0]^2\|_{L^2((0,\tau)\times I)}\to0\). Thus

\[
R_\tau=2\left(\|Y_L\|_{\mathcal E_\tau}+C_Lk\lambda\|w[0]^2\|_{L^2((0,\tau)\times I)}\right)\to0.
\]

The radius is nonnegative and the closed ball contains zero, even if it happens to be zero. For small \(\tau\), (6.3) times \(C_L\) is \(\le1/2\), and \(KR_\tau\le\theta_*/2\). The output is bounded by half the radius at input zero plus at most half the radius for the difference, hence the ball is mapped into itself. Banach's hypotheses are all met. At the fixed point, \(|y|\le KR_\tau\) establishes the lower temperature bound; no prior positivity of trial inputs or unknown solution is needed.

## 7. Finite-horizon constants and the stated threshold

Let \(\eta=\|z_0\|_{H^2}\), \(q=|g_*|/L\), \(s=\eta+q\), all evaluated in a fixed numerical convention. A usable explicit embedding constant is

\[
S_L=\sqrt{L^{-1}+L},\qquad \|h\|_\infty\le L^{-1/2}\|h\|_2+L^{1/2}\|h_x\|_2\le S_L\|h\|_{H^2}.
\]

From (3.3), for \(\|h\|_{\mathcal E_T}\le R\),

\[
|m|\le q,\quad |m'|\le\pi q/T,\quad |v|\le S_L\eta+q,\quad
\|p[h]\|_\infty\le2S_L\eta+2\lambda|\beta|TKR.
\tag{7.1}
\]

The bound for \(v\) is deliberately nonsharp: the exponential convolution has mass at most one. Combining (7.1) with \(\|Qh\|_\infty\le2KR\) gives the report's

\[
\|E[h]\|_\infty\le A_s s+A_RR,\quad \|w[h]\|_\infty\le W_s s+W_RR,
\]

\[
A_s=\pi/T+2r\mu S_L,\quad A_R=2r\lambda|\beta|(1+\mu T)K,\quad
W_s=2+(1+2\alpha)S_L,\quad W_R=2|\beta|(1+\alpha\lambda T)K.
\tag{7.2}
\]

The difference versions are \(\|\Delta E\|_\infty\le A_R\|\Delta h\|\), \(\|\Delta w\|_\infty\le W_R\|\Delta h\|\). Using them and (6.2), for \(Z=\sqrt{LT}\),

\[
\|N[h]\|_2\le[dKR^2+|b|KZR(A_ss+A_RR)+k\lambda Z(W_ss+W_RR)^2],\tag{7.3}
\]
\[
\|\Delta N\|_2\le[2dKR+|b|KZ(A_ss+2A_RR)+2k\lambda ZW_R(W_ss+W_RR)]\|\Delta h\|.\tag{7.4}
\]

Each right side is bounded by the respective expression in (5.4) with the report's \(C_N,C_N'\) in (5.5); for example \(A_ss+A_RR\le\max(A_s,A_R)(s+R)\). Thus all stated nonlinear constants are sufficient.

As \(\|p_0\|_2\le2\sqrt L S_L\eta\) and \(\|m'\|_2\le(\pi q/T)\sqrt{LT}\), the linear solution obeys \(\|Y_L\|\le C_Bs\) with the report's \(C_B\). With \(R=2C_Bs\), equations (7.3)–(7.4) make the closed ball invariant and make the map a contraction of factor at most \(1/2\) precisely under the first two inequalities of (6.1); the third gives \(\theta_*/2\le\theta\le3\theta_*/2\). The three entries in (6.3) are exactly the right sides obtained by solving these inequalities for \(s\); their minimum does imply all three. Constants are finite and positive under the frozen signs. If \(q<s_*\), the compatible family from the prior topology report approaches zero in \(H^2\), so sufficiently small nonzero members satisfy both the \(M\)-ball and \(\eta+q<s_*\). This is conditional on the fixed \(q\); it is not a proof that the given experiment satisfies the condition.

## 8. Full weak-class uniqueness: all terms and test regularity

Suppose two weak-initial solutions share the data, and set \(V=y_1-y_2\), \(P=p_1-p_2\), \(W=w_1-w_2\). Their mean memory is identical; \(P_t=-\mu P+\lambda\beta QV\), \(W=-\alpha P+\beta QV\). Subtracting the **original** heat equations before reduction, using \(\varepsilon_{1t}-\varepsilon_{2t}=rP_t+\beta QV_t\), yields

\[
M_{\theta_1}V_t-\kappa V_{xx}=-bV\varepsilon_{2t}-b\theta_1rP_t+k\lambda(w_1+w_2)W.\tag{8.1}
\]

Thus the source report's (7.1), including signs, is correct. \(V\in C_tH^1_0\cap L^2_tH^2\), \(V_t\in L^2\); the same temperature regularity gives \(\theta_1\in C_tH^1\subset C_{t,x}\). The a.e. positive lower bound extends to the continuous representative. \(V/\theta_1\in L^\infty_tH^1_0\): its derivative is \(V_x/\theta_1-V\theta_{1x}/\theta_1^2\). It is legitimate as an \(L^2\) multiplier of the a.e. equation and as a spatial \(H^1_0\) test after integration by parts.

Set

\[
\mathcal F=\frac c2\int V^2/\theta_1+\frac d2\|QV\|_2^2+\frac12\|P\|_2^2.
\]

The chain rule is justified directly in \(H^1_tL^2_x\): \(V,\theta_1\) are space-time bounded; the reciprocal is Lipschitz on the positive range; difference quotients converge in \(L^2\), and the products in the derivative are in \(L^1\). Thus \(t\mapsto\int V^2/\theta_1\) is absolutely continuous, with derivative \(\int(2VV_t/\theta_1-V^2\theta_{1t}/\theta_1^2)\). No time trace of \(V_t\) at the boundary is used. The \(Q\) term is \(\frac d2\frac d{dt}\|QV\|_2^2\).

After testing and adding \((P_t,P)\), the principal spatial term is

\[
\kappa\int \frac{|V_x|^2}{\theta_1}-\kappa\int\frac{V_xV\theta_{1x}}{\theta_1^2}.
\]

For \(V\in H^1_0(I)\), the one-dimensional Gagliardo–Nirenberg inequalities give

\[
\|V\|_4^2\le C\|V\|_2^{3/2}\|V_x\|_2^{1/2},\qquad
\|V\|_\infty\le C\|V\|_2^{1/2}\|V_x\|_2^{1/2}.
\]

For \(h=\theta_{1t}\) or \(\varepsilon_{2t}\),
\(\int |h|V^2\le C\|h\|_2\|V\|_2^{3/2}\|V_x\|_2^{1/2}\le\epsilon\|V_x\|_2^2+C_\epsilon\|h\|_2^{4/3}\|V\|_2^2\).
Likewise \(\int |\theta_{1x}VV_x|\le\epsilon\|V_x\|_2^2+C_\epsilon\|\theta_{1x}\|_2^4\|V\|_2^2\). The \(P_t\) term is controlled by the ODE, and the \(W\) term by bounded \(w_1+w_2\) and \(\|W\|_2\le\alpha\|P\|_2+|\beta|\|V\|_2\). Bounds on \(\theta_1\) above and below make \(\mathcal F\) equivalent to \(\|V\|_2^2+\|P\|_2^2\). Consequently

\[
\mathcal F'+c_0\|V_x\|_2^2\le C[1+\|\theta_{1x}\|_2^4+\|\theta_{1t}\|_2^{4/3}+\|\varepsilon_{2t}\|_2^{4/3}]\mathcal F.
\tag{8.2}
\]

The bracket is integrable on finite \([0,T]\): \(\theta_{1x}\in L^\infty_tL^2_x\), and both time derivatives are in \(L^2_{t,x}\). Gronwall yields \(V=P=0\) because \(\mathcal F(0)=0\). It follows that the mean memory, \(z\), \(\varepsilon\), \(u\), and \(\sigma\) also agree. This is uniqueness in **the whole stated class**, not all distributional solutions. The coefficients of (8.2) may depend on the two solutions; they need not satisfy the fixed-point-ball bound. No positivity is assumed for an unconstructed solution: positivity is part of the comparator class, and was separately proved for the constructed one.

## 9. Boundary traces, observations, and counterexamples to unsafe shortcuts

The temperature regularity implies \(y(t)\in H^2(I)\) for a.e. \(t\), and the bounded trace map gives

\[
\int_0^T(|y_x(0,t)|^2+|y_x(L,t)|^2)dt\le C\int_0^T\|y(t)\|_{H^2}^2dt<\infty.
\]

Both labeled heat powers are therefore in \(L^2(\delta,T)\). The reconstructed force \(A_0[Dm-b\langle y\rangle-kv]\) is continuous in time, hence also in \(L^2(\delta,T)\). For data satisfying the conditional threshold and \(\|z_0\|_{H^2}\le M\), existence plus §8 uniqueness makes the observation map well-defined on the stated actual weak-admissible set. Delay is not used as a substitute for the \(H^2\) trace estimate.

**Counterexample 1: the rank-one-after-differentiation correction is not generally bounded on \(L^2\).** Take constant positive \(\theta\), and \(h_n(x)=\sin((2n+1)\pi x/L)\). \(\|h_n\|_2=\sqrt{L/2}\), but \(|\langle h_{n,xx}\rangle|=2(2n+1)\pi/L^2\to\infty\). Thus the nonlocal correction in the principal operator, although rank one as a map applied to \(h_{xx}\), is unbounded as an operator of \(h\) on \(L^2\). This confirms rather than refutes the investigated report's warning.

**Counterexample 2: energy regularity alone does not supply endpoint flux.** For \(y(x,t)=t\,x^{3/4}(L-x)\), \(y\in H^1_tL^2_x\cap L^2_tH^1_0\), but \(y_x\sim (3/4)tLx^{-1/4}\) near \(0\), so the classical endpoint derivative is not finite and \(y\notin L^2_tH^2_x\). The example is not asserted to solve (A); it refutes the tempting inference of boundary-gradient traces from weaker energy spaces alone.

**Counterexample 3: contraction-ball uniqueness is not full-space uniqueness.** On \(\mathbb R\), \(F(x)=x^2\) is a contraction on \([-1/4,1/4]\) with fixed point zero, but it has another fixed point \(1\). This elementary example explains why §8, not Banach's theorem alone, is necessary for the actual admissibility predicate. No counterexample to the stated weak-class uniqueness was found.

## 10. Prior art and novelty audit

Searches covered rank-one/nonlocal parabolic mass, spatially nonlocal time derivatives, quasilinear thermoelasticity, memory/internal-state systems, nonautonomous maximal regularity, and fixed-point thermomechanics. Inspected primary statements and access limits are below. A nonlocal *initial condition*, a fractional time derivative, or an integral spatial diffusion is not automatically the same as this \(M_\theta y_t\).

1. **T. Cieślak, M. Galić, B. Muha**, *A model in one-dimensional thermoelasticity*, [arXiv:2003.03806v2](https://arxiv.org/html/2003.03806), 2020. **Full open preprint, Theorems 1–2 and model inspected.** For its dynamic wave–heat system with homogeneous displacement Dirichlet and temperature Neumann data, Theorem 1 takes \(u_0\in H^2\cap H^1_0\), \(u_1\in H^1_0\), \(\theta_0\in H^2\), \(\theta_0\ge0\), and proves local unique strong solutions; Theorem 2 gives global measure-valued solutions for lower initial regularity. The introduction identifies earlier small-data global theory and contraction arguments. Its inertia and Neumann thermal boundary, and absence of our independent exponential mechanical memory, make it **not** a theorem for (A). It establishes that one-dimensional coupled positive-temperature existence and regularity are not a new theme.

2. **M. Winkler**, *Rough Data in an Evolution System Generalizing 1D Thermoviscoelasticity with Temperature-Dependent Parameters*, *Applied Mathematics & Optimization* **91**, article 44 (2025), [DOI 10.1007/s00245-025-10243-9](https://doi.org/10.1007/s00245-025-10243-9). **Open article, displayed model, Proposition 1.3, Theorem 1.4 and their hypotheses inspected.** For its Neumann dynamic Kelvin–Voigt-type system, smooth coefficients with \(\gamma>0\), \(\Gamma\ge0\), \(F(0)=0\), and initial data in appropriate \(W^{1,p}\) spaces with \(p>n\), the paper proves local existence and uniqueness in its defined weak class and a maximal-time statement. Our quasistatic rank-one mass and prescribed Dirichlet baths are not its model; neither theorem implies the other. It is strong prior art on coupled weak existence and full-class uniqueness, not evidence of novelty for (A).

3. **F. Meyer**, *Large time existence in a thermoviscoelastic evolution problem with mildly temperature-dependent parameters*, *Journal of Elliptic and Parabolic Equations* (2026), [DOI 10.1007/s41808-026-00482-4](https://doi.org/10.1007/s41808-026-00482-4). **Open article, abstract and Theorem 1.1 inspected.** For a 1-D dynamic Kelvin–Voigt wave–heat system with mechanical Neumann and thermal Dirichlet data, smooth compatible initial data with a prescribed energy bound, bounded positive viscosity, growth assumptions, and sufficiently small \(\|\gamma'\|_\infty,\|f'\|_\infty\), the theorem extends a classical solution to an arbitrarily prescribed finite horizon. Its parameter-smallness and wave model differ from (6.1)'s data-smallness and quasistatic memory. It shows that conditional prescribed-horizon existence and quadratic heating obstacles are established research topics, not that this exact condition was already proved.

4. **P. Gwiazda, F. Z. Klawe, S. Owczarek**, *Thermo-visco-elasticity for Norton–Hoff-type models with homogeneous thermal expansion*, [arXiv:1611.05188v1](https://arxiv.org/html/1611.05188), 2016. **Open preprint, model and Theorem 1.1 inspected.** It studies a quasistatic three-dimensional equilibrium–heat–inelastic-strain system with a Norton–Hoff evolution law and linearized thermal expansion; under its stated constitutive/data assumptions Theorem 1.1 establishes a weak solution, using a two-level approximation. The thermal coupling and internal strain are materially related, but the nonlinear flow law, dimensions, linearization, spaces and boundary data differ from (A). It is prior art for PDE–internal-variable existence, not an exact-covering theorem.

5. **K. L. Kuttler, M. Shillor, J. R. Fernández**, *Existence for the thermoviscoelastic thermistor problem*, *Differential Equations and Dynamical Systems* **17**, 217–233 (2009), [DOI 10.1007/s12591-009-0017-7](https://doi.org/10.1007/s12591-009-0017-7). **Publisher abstract and references only; subscription full text unavailable.** The abstract reports existence of a weak solution to a dynamic thermoviscoelastic–heat–charge system with temperature-dependent electrical conductivity and quadratic Joule heating, via retarded approximations; it explicitly leaves uniqueness open. Exact assumptions and theorem cannot be independently checked from the preview. It is relevant coupled-heating background, not a source for (A)'s unique strong-temperature theorem.

6. **V. Colao, L. Muglia**, *Solutions to nonlocal evolution equations governed by non-autonomous forms and demicontinuous nonlinearities*, [arXiv:2110.03565v3](https://arxiv.org/html/2110.03565), 2022. **Open preprint introduction and Theorem 1.1 inspected.** It restates Lions' theorem for measurable bounded coercive forms, giving \(L^2_tV\cap H^1_tV'\) solutions; its subsequent stronger theory requires additional hypotheses including maximal regularity. Its nonlocality includes a nonlocal initial condition; it is not a direct theorem for the state-dependent rank-one mass. It does not justify importing \(L^2_tH^2_x\) for (A).

7. **S. Bechtel, C. Mooney, M. Veraar**, *Counterexamples to maximal regularity for operators in divergence form*, *Archiv der Mathematik* **123**, 199–209 (2024), [DOI 10.1007/s00013-024-02014-9](https://doi.org/10.1007/s00013-024-02014-9). **Open article abstract and introduction inspected.** For certain spatially and temporally dependent divergence-form coefficients, coercive weak-form theory does not automatically imply the stronger maximal \(L^2\)-regularity in \(L^2\). This does not refute (A); it independently supports the need for §5's explicit linear proof rather than an unsupported operator-theorem invocation.

8. **G. Amendola, M. Fabrizio, J. M. Golden**, *Thermodynamics of Materials with Memory: Theory and Applications*, first ed., Springer (2012), [DOI 10.1007/978-1-4614-1692-0](https://doi.org/10.1007/978-1-4614-1692-0). **Publisher book overview only; relevant full chapters unavailable.** The overview describes existence, uniqueness and stability for viscoelastic evolution equations and thermoelastic-memory controllability. Exact theorem statements and assumptions were not inspected; no claim is made that this book proves or does not prove (A). Its inaccessible chapters are a serious remaining exact-overlap risk.

**Comparison and novelty classification.** The independently checked derivation is a model-specific proof using standard tools. It may be an unrecorded theorem for the exact frozen system; the search does not establish that it is already published, nor does it establish a general theorem beyond existing operator classes. In particular, “new proof for one model,” “new theorem for an already studied operator class,” and “genuinely new mathematical insight” are different assertions. Here the first is a description of the repository work, not a claim of chronological priority; the latter two are **not demonstrated**. The exact inverse mass formula is a direct rank-one calculation, and weighted testing plus small-ball contraction are conventional. We did not identify a genuinely promising new theory or a differentiated mathematical advance meeting the requested gate.

## 11. Scientific importance and final decision

- **Obstacle resolved conditionally:** Eliminating equilibrium puts a spatial-average term on \(\theta_t\); the explicit reference-mass estimate handles it while the ODE memory feeds a quadratic heat term. The proof provides a positive local solution and a positive finite-horizon one under concrete numerical smallness conditions, including full-class uniqueness and heat-flux traces.
- **Why it matters to this thermomechanical model:** It verifies that, under checkable assumptions, the reduced equations and sensors correspond to at least one consistent active experiment rather than merely formal identities. This is a useful foundational check, not a new constitutive law or a broadly validated physical prediction.
- **Previously unavailable result?** It supplies that guarantee within this repository under an extra bound. No numerical frozen data establish the bound and no comprehensive prior-art search establishes that the guarantee was unavailable in the literature. The result does not cover unrestricted fixed loading or classical corners.
- **Use for later boundary-state questions:** It supplies a nonempty conditional weak domain and well-defined forward traces. It does not establish injectivity, stability, sensor sufficiency, or practical observability, and this audit does not investigate them.
- **Likely specialist editorial view:** The proof is a careful but standard small-data application to one rather restricted, one-dimensional quasistatic model. In the absence of a sharper general theorem, genuinely new technique, parameter-verified physical consequence, or a differentiated result against exact prior art, technical effort alone is not persuasive evidence of a meaningful standalone mathematical publication.

**Verdict: MATHEMATICALLY CORRECT BUT ROUTINE.** This is a judgment on the theorem as presently supported, not a claim that an exact published duplicate has been located. No publication recommendation is made. Dr. Gupta makes the final scientific decision.
