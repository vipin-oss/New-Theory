# Independent mathematical audit of the positive-time regularity upgrade

**Date:** 1 November 2026

**Verdict: AUDIT PASSED WITH CORRECTIONS.** The central positive-time estimate and its stated downstream consequences follow from the frozen solution class. There is one algebraic transcription error in the explanatory sentence immediately after equation (4) of the audited report: its *undivided* product difference is missing a factor of \(h\). The actual difference-quotient equation (4), including the sign of the nonlocal term, is correct. We also make explicit the increment restriction needed for a nonempty interval \([a,T-h]\), and the limiting and representative arguments. These corrections do not change the regularity conclusions.

This is an independent recalculation by Arena in this task, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. No external research theorem is invoked: the proof uses the elementary Sobolev, interpolation, Young, Gronwall, and Hilbert-space compactness facts explicitly described below. No new Carleman search or continuation, channel-injectivity, or theory claim is made.

## 1. Claim-by-claim decision and frozen assumptions

| Audited claim | Decision | Qualification |
|---|---|---|
| Difference equations (report (4)) and uniform source bound | PASS WITH CORRECTION | Equations are correct; the explanatory undivided identity after (4) lacks a factor \(h\); §2. |
| Weighted nonlocal energy identity | PASS | The local time-weight term has a plus sign on the left; the projection term is exactly \(\frac d2\partial_t\|Qz_h\|_2^2\); §3. |
| Admissibility and integrability of the test | PASS WITH CLARIFICATION | Bounds for each fixed increment, not uniform high-regularity bounds, justify the chain rule and integration by parts; §3. |
| Uniform Gronwall and limiting estimate | PASS WITH CLARIFICATION | Use \(h<\min(a/4,T-a)\), choose an a.e. starting point, then exhaust \(T\); §4. |
| \(L^6\), \(L^\infty H^2\), and parabolic-metric Lipschitz bounds | PASS | The elliptic equation and 1-D inequalities are essential; the \(H^2\) bound alone does not give time regularity; §5. |
| Regularity at initial corners or joint boundedness of \(y_t\) | NOT ESTABLISHED | Neither is needed for the proof; no obstruction to their possible truth is asserted; §6. |

Let \(I=(0,L)\), \(Qf=f-\bar f\), and write the material constant originally denoted \(a\) as \(a_0\), reserving \(a\in(0,T)\) for the time cutoff. Set
\[
D=a_0+k,\quad r=k/D,\quad\alpha=a_0/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D.
\]
All frozen signs and nonzero material couplings are retained. The loading is \(m=g_*L^{-1}\sin^2(\pi t/T)\), \(g_*\ne0\), \(T=10/\lambda\). With \(\theta=\theta_*+y\), the actual nonzero-loading base and zero initial memory solve
\[
\begin{gathered}
p_t=-\mu p+\lambda\beta Qy,\qquad v_t=\lambda(m-v),\\
w=m-v-\alpha p+\beta Qy,\qquad E=m'+rp_t,\\
(cI+d\theta Q)y_t-\kappa y_{xx}=F:=-b\theta E+k\lambda w^2,\\
y(\cdot,0)=0,\quad y(0,t)=y(L,t)=0,\quad p(\cdot,0)=0,\quad v(0)=0.
\end{gathered}\tag{1}
\]
The existing sufficient condition \(0<q=|g_*|/L<s_*\) is assumed, not numerically verified. The only temperature regularity initially used is
\[
y\in H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)\cap H^1_0(I))\cap C([0,T];H^1_0(I)).\tag{2}
\]
We also use the established positive bounds \(0<\underline\theta\le\theta\le\overline\theta\) and bounded \(p,w,E\). In 1-D, (2) gives \(y\in C([0,T]\times\bar I)\) and \(\theta_x\in L^\infty_tL^2_x\). The ODE gives \(p_t\in L^\infty_{t,x}\) and \(v_t\in L^\infty_t\); the smooth load gives \(m,m',m''\in L^\infty\). Hence \(F\in L^\infty_{t,x}\). None of these statements assumes the upgrade.

## 2. Recalculation of every time quotient

For \(h>0\), let \(\Delta_h f(t)=(f(t+h)-f(t))/h\), \(0<t<T-h\). Put
\[
z=\Delta_hy,\quad \pi=\Delta_hp,\quad \nu=\Delta_hv,
\quad \Theta=\theta(t+h),\quad f^+=f(t+h).
\]
We suppress \(h\) in \(z,\pi,\nu,\Theta\) below. Since \(Q\) is bounded linear and independent of time,
\[
\Delta_h(\theta Qy_t)=\Theta Qz_t+zQy_t(t).\tag{3}
\]
Here \(z_t=\Delta_h y_t\) in \(L^2\), for each fixed \(h\). Equivalently, the **undivided** identity is
\[
\theta^+Qy_t^+-\theta Qy_t
=h\{\Theta Qz_t+zQy_t\}.\tag{4}
\]
The audited report states (4) without the factor \(h\) in its explanatory sentence. This is a transcription error, not an error in its displayed quotient equation: substituting the correctly divided (3) gives
\[
(cI+d\Theta Q)z_t-\kappa z_{xx}=F_h-dzQy_t(t),\qquad F_h=\Delta_hF.\tag{5}
\]
The negative sign is forced by moving \(+dzQy_t(t)\) from the left to the right. Subtraction of the ODEs yields exactly
\[
\begin{aligned}
\pi_t&=-\mu\pi+\lambda\beta Qz,&\quad \nu_t&=\lambda(m_h-\nu),\\
E_h&=m'_h+r(-\mu\pi+\lambda\beta Qz),&
 w_h&=m_h-\nu-\alpha\pi+\beta Qz.
\end{aligned}\tag{6}
\]
For the thermal source,
\[
F_h=-b(zE^++\theta E_h)+k\lambda(w^++w)w_h.\tag{7}
\]
Thus the time arguments in the audited equation are correct: \(E^+\) multiplies \(z\), while \(\theta\) without the shift multiplies \(E_h\). The alternative decomposition with \(E\) and \(\Theta\) would also be valid but is not the one used here.

The mean-value/Jensen bound gives \(\|m_h\|_\infty\le\|m'\|_\infty\), \(\|m'_h\|_\infty\le\|m''\|_\infty\), and \(\|\nu\|_\infty\le\|v_t\|_\infty\), uniformly in \(h\). The bound \(\|Qz\|_2\le\|z\|_2\), boundedness of \(\theta,E,w\), and (6)–(7) imply, a.e. in time,
\[
\|F_h(t)\|_2\le C\{1+\|z(t)\|_2+\|\pi(t)\|_2\}.\tag{8}
\]
The constant is independent of \(h\); it includes \(\sqrt L\). Every term in (5) is in \(L^2\) for each fixed \(h\): \(z\in C_tH^1_0\subset L^\infty_{t,x}\), \(Qy_t\in L^2\), and (8) applies. This fixed-increment bound is not a uniform \(L^\infty\) estimate on \(z\).

## 3. Energy, signs, tests, and exponents

For each fixed \(h\), (2) gives
\[
z\in H^1(0,T-h;L^2)\cap L^2(0,T-h;H^2\cap H^1_0)\cap C([0,T-h];H^1_0).
\]
Also \(\Theta\in C_tH^1_x\cap H^1_tL^2_x\), \(\underline\theta\le\Theta\le\overline\theta\), and \(\pi\in H^1_tL^2_x\). In particular \(z,\Theta,1/\Theta\) are bounded for each fixed \(h\), and
\[
\partial_x(z/\Theta)=z_x/\Theta-z\Theta_x/\Theta^2\in L^2_{t,x},\qquad z/\Theta\in L^2_tH^1_0.
\]
Thus \(z/\Theta\) is a valid \(L^2\) multiplier of the a.e. equation and a spatial \(H^1_0\) test. The following chain rule is justified directly by approximation or difference quotients: \(z,\Theta\) are bounded, their time derivatives are in \(L^2\), and the reciprocal is smooth on the compact positive temperature range. Each product in
\[
\frac d{dt}\int_I\frac{z^2}{\Theta}dx
=2\int_I\frac{zz_t}{\Theta}dx-\int_I\frac{z^2\Theta_t}{\Theta^2}dx
\]
is in \(L^1\). The first integral is \(L^1\) by \(z\) bounded and \(z_t\in L^2\); the second by bounded \(z\) and \(\Theta_t\in L^2\). Hence the energy has an absolutely continuous representative. Since \(Q\) is self-adjoint and idempotent on \(L^2(I)\),
\[
\begin{aligned}
\int_I(cI+d\Theta Q)z_t\,\frac z\Theta dx
&=c\int_I\frac{zz_t}{\Theta}dx+d(Qz_t,z)_2\\
&=\frac12\frac d{dt}\left(c\int_I\frac{z^2}{\Theta}dx+d\|Qz\|_2^2\right)
+\frac c2\int_I\frac{\Theta_tz^2}{\Theta^2}dx.\tag{9}
\end{aligned}
\]
The plus sign in the final term is correct. The full \(Q\) contribution is retained; it is not \(\|z\|_2^2\) and it does not require \(\bar z=0\).

Integration by parts in space is legal because \(z\in H^2\) and \(z/\Theta\in H^1_0\) for a.e. \(t\). The precise diffusion term is
\[
-\kappa\int_Iz_{xx}\frac z\Theta dx
=\kappa\int_I\frac{|z_x|^2}{\Theta}dx
-\kappa\int_I\frac{z_xz\Theta_x}{\Theta^2}dx.\tag{10}
\]
The endpoint term vanishes by the Sobolev Dirichlet trace of \(z\); no pointwise trace of \(z_t\), \(y_t\), or \(\Theta_x\) is used.

For \(u\in H^1_0(I)\), the elementary 1-D Sobolev estimate \(\|u\|_\infty^2\le C\|u\|_2\|u_x\|_2\), together with \(\int |u|^4\le\|u\|_\infty^2\|u\|_2^2\), yields
\[
\|u\|_4^2\le C\|u\|_2^{3/2}\|u_x\|_2^{1/2},\qquad
\|u\|_\infty\le C\|u\|_2^{1/2}\|u_x\|_2^{1/2}.\tag{11}
\]
For \(f\in L^2(I)\), Young with exponents \(4\) and \(4/3\), respectively \(4/3\) and \(4\), gives
\[
\begin{aligned}
\int_I|f|z^2dx&\le \|f\|_2\|z\|_4^2
\le\varepsilon\|z_x\|_2^2+C_\varepsilon\|f\|_2^{4/3}\|z\|_2^2,\\
\int_I|\Theta_xzz_x|dx&\le\|\Theta_x\|_2\|z\|_\infty\|z_x\|_2
\le\varepsilon\|z_x\|_2^2+C_\varepsilon\|\Theta_x\|_2^4\|z\|_2^2.\tag{12}
\end{aligned}
\]
The first line applies to \(f=\Theta_t=y_t(t+h)\) in (9), and to \(f=Qy_t(t)\) in (5), after multiplication by bounded reciprocal temperatures. The projection has \(\|Qy_t\|_2\le\|y_t\|_2\). The second line handles the cross term in (10). In particular, no bound on \(y_t\) in a stronger space is assumed. These products are integrable even before the uniform estimate, because for fixed \(h\), \(z\in L^\infty_tH^1_0\), while \(\Theta_t,Qy_t\in L^2_{t,x}\).

## 4. Uniform energy, starting time, and limit at \(T\)

Define
\[
H_h(t)=c\int_I\frac{z^2}{\Theta}dx+d\|Qz\|_2^2+\|\pi\|_2^2.\tag{13}
\]
It is absolutely continuous and uniformly equivalent to \(\|z\|_2^2+\|\pi\|_2^2\), since \(c>0\) and \(\underline\theta\le\Theta\le\overline\theta\). Test (5) by \(z/\Theta\), test \(\pi_t=-\mu\pi+\lambda\beta Qz\) by \(\pi\), multiply the resulting half-energy identities by 2, and add. From (8),
\[
\left|\int_I F_h z/\Theta\,dx\right|+|\lambda\beta(\pi,Qz)_2|
\le C\{1+\|z\|_2^2+\|\pi\|_2^2\}.
\]
Using (9)–(12), absorbing a fixed fraction of \(\kappa\overline\theta^{-1}\|z_x\|_2^2\), and dropping the favorable \(-\mu\|\pi\|_2^2\) term, yields for a.e. \(t\in(0,T-h)\)
\[
H_h'(t)+c_0\|z_x(t)\|_2^2\le C(1+K_h(t))H_h(t)+C,\tag{14}
\]
\[
K_h(t)=\|y_t(t)\|_2^{4/3}+\|y_t(t+h)\|_2^{4/3}+\|\theta_x(t+h)\|_2^4.
\]
Here \(c_0,C\) are independent of \(h\). Hölder in time gives
\[
\int_0^{T-h}\|y_t(t+h)\|_2^{4/3}dt
\le T^{1/3}\left(\int_0^T\|y_t\|_2^2dt\right)^{2/3},
\]
and the unshifted term has the same bound; the last term is bounded by \(T\|\theta_x\|_{L^\infty_tL^2_x}^4\). Hence \(\int K_h\le C\) uniformly.

The Bochner fundamental theorem of calculus and Jensen yield
\[
\int_0^{T-h}\|z(t)\|_2^2dt\le\int_0^T\|y_t(t)\|_2^2dt,\quad
\int_0^{T-h}\|\pi(t)\|_2^2dt\le\int_0^T\|p_t(t)\|_2^2dt.\tag{15}
\]
Fix \(a\in(0,T)\), then restrict to \(0<h<\min(a/4,T-a)\). This additional explicit restriction ensures \(a<T-h\); it does not change any \(h\downarrow0\) conclusion. By averaging (15) over \((a/4,a/2)\), there is an \(h\)-dependent \(t_h\) in that interval, chosen in the full-measure set where (14) holds, such that \(H_h(t_h)\le C_a\). The interval is inside \((0,T-h)\) and the energy has an absolutely continuous representative. Gronwall from \(t_h\) gives
\[
\sup_{t\in[a,T-h]}H_h(t)+\int_a^{T-h}\|z_x(t)\|_2^2dt\le C_a,\tag{16}
\]
with \(C_a\) independent of \(h\); the integral estimate follows by integrating (14) after the energy bound. Dependence on \(a\), the solution norms, and the fixed parameters is allowed, and no uniformity as \(a\downarrow0\) is claimed.

For each fixed \(T'<T\), the difference quotients converge strongly to \(y_t\) in \(L^2((a,T')\times I)\). This follows directly by writing \(z(t)=h^{-1}\int_t^{t+h}y_t(s)ds\) and using continuity of translations in \(L^2\). Bound (16), weak compactness in \(L^2(a,T';H^1_0)\), and weak-* compactness in \(L^\infty(a,T';L^2)\) identify the limit as \(y_t\). The same \(C_a\) works for every \(T'<T\); exhausting \(T\) and monotone convergence of the spatial-gradient integral give
\[
y_t\in L^\infty(a,T;L^2(I))\cap L^2(a,T;H^1_0(I)),\tag{17}
\]
with the stated bound on the open time interval. No separate trace of \(y_t\) at \(T\) is implied. A positive cutoff is fixed before the limit; no \(t=0\) trace enters.

## 5. Independent verification of downstream implications

**Sixth power and \(B\).** For \(u\in H^1_0(I)\), \(\|u\|_6^6\le\|u\|_\infty^4\|u\|_2^2\le C\|u\|_2^4\|u_x\|_2^2\). Integrating and using (17),
\[
\|y_t\|_{L^6((a,T)\times I)}^6
\le C\|y_t\|_{L^\infty(a,T;L^2)}^4\|\partial_x y_t\|_{L^2((a,T)\times I)}^2.
\tag{18}
\]
Also \(H^1_0(I)\hookrightarrow L^\infty(I)\) gives \(y_t\in L^2(a,T;L^\infty)\). The projection \(Q=I-\bar{\cdot}\) is bounded on \(L^6(I)\), \(L^2(I)\), and \(L^\infty(I)\). The other terms in
\[
B=-dQy_t-bE-br\lambda\beta\theta+2k\lambda\beta w
\]
are bounded on the finite cylinder. Therefore \(B\in L^6_{t,x}\cap L^\infty_tL^2_x\cap L^2_tL^\infty_x\) on \((a,T)\times I\). These statements do not give \(B\in L^\infty_{t,x}\).

**Spatial \(H^2\) and principal derivative.** Equation (1), including its nonlocal part, reads
\[
\kappa y_{xx}=cy_t+d\theta Qy_t-F.\tag{19}
\]
The bounded multipliers, (17), and \(F\in L^\infty_{t,x}\) give \(y_{xx}\in L^\infty(a,T;L^2)\). Together with the Dirichlet condition and the 1-D estimate \(\|u\|_{H^2}\le C\|u_{xx}\|_2\) for \(u\in H^2\cap H^1_0\), this yields \(y\in L^\infty(a,T;H^2)\). This implication uses (19) and the bounded source; \(y_t\in L^\infty L^2\) **alone** for an arbitrary function does not imply \(H^2\) spatial regularity. By \(H^1(I)\hookrightarrow L^\infty(I)\) applied to \(y_x\), \(y_x\in L^\infty((a,T)\times I)\) and \((M_b)_x=d y_x\in L^\infty\).

**Representatives and time interpolation.** By (17), the \(L^2\)-valued absolutely continuous representative of \(y\) satisfies
\[\|y(t)-y(s)\|_2\le C_a|t-s|\quad(s,t\in[a,T]).\tag{20}\]
The known \(C([0,T];H^1_0)\) representative is the same one. Although (19) gives \(H^2\) only for a.e. time, the uniform bound extends to every \(t\in[a,T]\): choose good times \(t_n\to t\), extract a weakly convergent bounded \(H^2\) subsequence, and identify its limit with \(y(t)\) by strong \(H^1\) continuity. Lower semicontinuity preserves the bound. This also covers \(t=a,T\).

For \(f\in H^2(I)\cap H^1_0(I)\), the 1-D interpolation inequality
\[
\|f\|_\infty\le C\|f\|_2^{3/4}\|f\|_{H^2}^{1/4}\tag{21}
\]
follows, for instance, by extending \(f\) to the line and applying the one-dimensional Gagliardo–Nirenberg inequality; the constant depends on \(I\). Apply it to \(f=y(t)-y(s)\) and use (20) and the uniform \(H^2\) bound:
\[
\|y(t)-y(s)\|_\infty\le C_a|t-s|^{3/4}\qquad(s,t\in[a,T]).\tag{22}
\]
The time Hölder estimate thus uses **both** (17) and the equation-derived \(H^2\) bound, not \(L^\infty H^2\) alone. The spatial \(W^{1,\infty}\) bound gives the jointly continuous representative
\[
|M_b(t,x)-M_b(s,x')|\le C_a\{|x-x'|+|t-s|^{3/4}\},
\quad M_b=c+d\theta.\tag{23}
\]
Since \(M_b\) is uniformly positive, the same holds for \(\kappa/M_b\). On a finite time interval, \(|t-s|^{3/4}\le C_T|t-s|^{1/2}\); this is Lipschitz in the parabolic metric \(|x-x'|+|t-s|^{1/2}\). It is **not** a proof of \(W^{1,\infty}\) in space-time: \(M_{b,t}=dy_t\) and the reciprocal's time derivative are only known in the mixed spaces in (17)–(18), not jointly bounded. Nor does (23) establish classical \(C^1\) coefficients.

## 6. Initial time, spatial boundary, and delayed interval

The proof establishes (17)–(23) on every \([a,T]\) with \(a>0\), with constants depending on \(a\). It does not control their behavior as \(a\downarrow0\) and does not establish \(y_t(0)\), \(y_t(0,0)\), \(y_{xx}(0,0)\), or higher-order corner compatibility. Initial and bath values are compatible at order zero. Formal vanishing of \(m(0),m'(0),p(0),v(0),y(0)\) does not produce a classical derivative trace.

The \(H^1_0(I)\) membership in (17) is a statement about the spatial Sobolev trace of \(y_t(t,\cdot)\) for a.e. positive time. It follows from the zero-trace quotients and weak closedness, not from differentiating the endpoint condition pointwise. The \(H^2\) and Lipschitz-in-space bounds include the closed spatial interval via representatives; they do not assert continuity of \(y_t\) or \(y_{xx}\) at either endpoint. Taking any \(a<\delta\) gives the asserted bounds uniformly on the delayed interval \(J=(\delta,T)\), including times arbitrarily near \(T\) in the essential-norm sense and coefficients continuously extended to \(T\).

## 7. Final verdict

**AUDIT PASSED WITH CORRECTIONS.** The omitted factor \(h\) in the explanatory product identity is a genuine algebraic typo, but the normalized quotient equation, subsequent energy inequality, positive-time estimate, \(B\in L^6\), \(L^\infty H^2\), and parabolic-metric Lipschitz conclusions survive. The additional restriction on \(h\) and the compactness/representative details above close minor presentation gaps. Nothing here establishes initial-corner regularity, \(B\in L^\infty\), a fully applicable boundary Carleman estimate, or any continuation or injectivity property.
