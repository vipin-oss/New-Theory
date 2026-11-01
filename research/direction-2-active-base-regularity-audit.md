# Active-base regularity for future boundary Carleman estimates

**Date:** 1 November 2026

**Verdict: REGULARITY UPGRADE PROVED.** For every \(a\in(0,T)\), the actual active base satisfies
\[
(y_b)_t\in L^\infty(a,T;L^2(I))\cap L^2(a,T;H^1_0(I))\cap L^6((a,T)\times I),
\quad y_b\in L^\infty(a,T;H^2(I)),\quad B\in L^6((a,T)\times I).
\]
Consequently \(M_b\) and \(\kappa/M_b\) are Lipschitz in the **parabolic metric** on \([a,T]\times\bar I\): spatially Lipschitz and temporally at least \(1/2\)-Hölder. This is an improvement under the existing sufficient condition, with no further smallness assumption. It does **not** establish \(W^{1,\infty}\) in space-time, \(B\in L^\infty\), or all hypotheses of either boundary Carleman theorem compared below. It does not prove any boundary continuation property or control the independent memory source.

This is a single-agent Arena investigation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. No new constitutive theory or novelty is claimed.

## 1. Actual base and known estimates

Write \(I=(0,L)\), \(Qf=f-\bar f\),
\[
D=a_0+k,\quad r=k/D,\quad\alpha=a_0/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D,
\]
where \(a_0\) denotes the frozen material constant called \(a\) in the previous reports; this avoids confusion with the positive time cutoff \(a\). All physical constants and signs are unchanged. The load is \(m(t)=g_*L^{-1}\sin^2(\pi t/T)\), \(T=10/\lambda\), \(g_*\ne0\). With zero initial memory and \(\theta=\theta_*+y\), the actual base obeys
\[
\begin{gathered}
p_t=-\mu p+\lambda\beta Qy,\quad v_t=\lambda(m-v),\quad
w=m-v-\alpha p+\beta Qy,\quad E=m'+rp_t,\\
(cI+d\theta Q)y_t-\kappa y_{xx}=F:=-b\theta E+k\lambda w^2,\\
y(\cdot,0)=0,\quad y(0,t)=y(L,t)=0,\quad p(\cdot,0)=0,\quad v(0)=0.
\end{gathered}\tag{1}
\]
The variable \(v\) is the spatial mean of the frozen memory. The system is not replaced by an equilibrium. The sufficient fixed-unit hypothesis \(0<q=|g_*|/L<s_*\) gives the unique positive base of the existence report; no numerical verification of that hypothesis is available. It yields
\[
y\in H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x})\cap C_tH^1_{0,x},\quad
\theta_*/2\le\theta\le3\theta_*/2,\quad p,w,E\in L^\infty_{t,x}.\tag{2}
\]
In 1-D \(C_tH^1_x\hookrightarrow C_{t,x}\). Also \(p_t=-\mu p+\lambda\beta Qy\in L^\infty_{t,x}\), and \(F\in L^\infty_{t,x}\). All constants below may depend on the fixed base, parameters, \(T,L\), and cutoff; they do not depend on the difference quotient increment. The previously established \(L^2_{t,x}\) bound on \(y_t\) is crucial. No derivative estimate is inferred merely by embedding (2).

The coefficients in the odd temperature equation are
\[
M_b=c+d\theta,\quad
B=-dQy_t-bE-br\lambda\beta\theta+2k\lambda\beta w,\quad
S=\lambda\alpha(br\theta-2kw).\tag{3}
\]
All appearances of \(Q\) below are retained, including the nonlocal mass term.

## 2. Positive-time difference-quotient estimate

### 2.1 Exact equations for the quotients

Fix a cutoff \(a\in(0,T)\). For \(h>0\), \(h<a/4\), and \(0<t<T-h\), put
\[
z_h(t)=\frac{y(t+h)-y(t)}h,\quad
\pi_h(t)=\frac{p(t+h)-p(t)}h,\quad
\nu_h(t)=\frac{v(t+h)-v(t)}h,\quad \theta_h(t)=\theta(t+h).
\]
Use analogous notation \(m_h,m'_h,E_h,w_h,F_h\). Time differences of (1), with no formal differentiation of \(y_t\), give
\[
\begin{aligned}
&(cI+d\theta_h Q)(z_h)_t-\kappa(z_h)_{xx}
= -d z_h Qy_t(t)+F_h,\\
&(\pi_h)_t=-\mu\pi_h+\lambda\beta Qz_h,\qquad
(\nu_h)_t=\lambda(m_h-\nu_h),\\
&E_h=m'_h+r[-\mu\pi_h+\lambda\beta Qz_h],\qquad
w_h=m_h-\nu_h-\alpha\pi_h+\beta Qz_h,\\
&F_h=-b\{z_h E(t+h)+\theta(t)E_h\}+k\lambda\{w(t+h)+w(t)\}w_h.
\end{aligned}\tag{4}
\]
For example, \(\theta(t+h)Qy_t(t+h)-\theta(t)Qy_t(t)=\theta_h Q(z_h)_t+z_hQy_t(t)\). The mean operator commutes with the time difference. The smooth prescribed \(m\) gives uniformly bounded \(m_h,m'_h\); \(\nu_h\) is uniformly bounded because \(v_t\) is bounded. Since \(\theta,E,w\) are bounded, for a.e. \(t\)
\[
\|F_h(t)\|_2\le C\{1+\|z_h(t)\|_2+\|\pi_h(t)\|_2\}.\tag{5}
\]
The original \(y\in\mathcal E_T\) ensures each fixed \(z_h\in H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x})\) on its domain, so \(z_h/\theta_h\) is a valid spatial \(H^1_0\) test and the time-chain rule below is justified by approximation, as in the frozen existence audit. No bound on \(z_h\) beyond the original difference-quotient bounds is assumed.

### 2.2 Nonlocal energy and uniform inequality

Test the first equation in (4) by \(z_h/\theta_h\). Since \(Q\) is the orthogonal mean-zero projection,
\[
\int_I (cI+d\theta_hQ)(z_h)_t\,{z_h\over\theta_h}dx
=\frac12\frac d{dt}\left(c\int_I\frac{z_h^2}{\theta_h}dx+d\|Qz_h\|_2^2\right)
+\frac c2\int_I\frac{(\theta_h)_t z_h^2}{\theta_h^2}dx.\tag{6}
\]
This is the **exact** rank-one contribution, not a scalar-mass approximation. The energy in parentheses is uniformly equivalent to \(\|z_h\|_2^2\) by positivity and boundedness of \(\theta\). Integrating the diffusion term by parts gives its coercive part \(\kappa\int |(z_h)_x|^2/\theta_h\), plus a cross term involving \((\theta_h)_x\). The boundary term vanishes because \(z_h\) has zero Dirichlet trace.

For \(u\in H^1_0(I)\), the one-dimensional estimates used are
\[
\|u\|_4^2\le C\|u\|_2^{3/2}\|u_x\|_2^{1/2},\qquad
\|u\|_\infty\le C\|u\|_2^{1/2}\|u_x\|_2^{1/2}.\tag{7}
\]
Hölder and Young therefore imply, for any fixed \(\varepsilon>0\),
\[
\begin{aligned}
\|f\|_2\|z_h\|_4^2
&\le\varepsilon\|(z_h)_x\|_2^2+C_\varepsilon\|f\|_2^{4/3}\|z_h\|_2^2,\\
\|\theta_x(t+h)\|_2\|z_h\|_\infty\|(z_h)_x\|_2
&\le\varepsilon\|(z_h)_x\|_2^2+C_\varepsilon\|\theta_x(t+h)\|_2^4\|z_h\|_2^2.
\end{aligned}\tag{8}
\]
The first line controls **both** the \((\theta_h)_t z_h^2\) term in (6) and the exact \(z_hQy_t(t)\) term in (4), taking \(f=y_t(t+h)\) and \(f=Qy_t(t)\), respectively. The second controls the spatial cross term. Estimate (5), Cauchy–Schwarz and Young control \(F_h\). Testing the \(\pi_h\) equation by \(\pi_h\), adding it to the heat energy, and choosing \(\varepsilon\) small gives, for some \(c_0>0\),
\[
\mathcal H_h'(t)+c_0\|(z_h)_x(t)\|_2^2
\le C\{1+K_h(t)\}\mathcal H_h(t)+C,\tag{9}
\]
where
\[
\mathcal H_h=c\int_I\frac{z_h^2}{\theta_h}dx+d\|Qz_h\|_2^2+\|\pi_h\|_2^2,
\quad K_h=\|y_t(t)\|_2^{4/3}+\|y_t(t+h)\|_2^{4/3}
+\|\theta_x(t+h)\|_2^4.
\]
The integrals of \(K_h\) are bounded uniformly in \(h\): \(y_t\in L^2_tL^2_x\), \(4/3<2\), and \(\theta_x\in L^\infty_tL^2_x\). No small coefficient or uncontrolled \(L^\infty\) norm of \(y_t\) is used. The same calculation is justified for the Sobolev solutions by the chain rule and spatial integration-by-parts arguments of the frozen existence audit; \(z_h/\theta_h\in L^2_tH^1_0\), and all displayed products are integrable using (7).

### 2.3 Starting the estimate without initial-corner regularity

Jensen's inequality gives
\[
\int_0^{T-h}\|z_h(t)\|_2^2dt\le\int_0^T\|y_t(t)\|_2^2dt,\qquad
\int_0^{T-h}\|\pi_h(t)\|_2^2dt\le\int_0^T\|p_t(t)\|_2^2dt.\tag{10}
\]
Thus there exists a possibly \(h\)-dependent \(t_h\in(a/4,a/2)\) with \(\mathcal H_h(t_h)\le C_a\), using the uniform equivalence of energy and \(L^2\) norms. Apply Gronwall to (9) on \((t_h,T-h)\), then integrate (9). Since \(h<a/4\), this yields
\[
\sup_{t\in[a,T-h]}\|z_h(t)\|_2^2+
\int_a^{T-h}\|(z_h)_x(t)\|_2^2dt\le C_a.\tag{11}
\]
For any compact \((a,T')\), \(T'<T\), the time quotients converge strongly to \(y_t\) in \(L^2((a,T')\times I)\). Weak compactness in \(L^2H^1_0\) and weak-* compactness in \(L^\infty L^2\), followed by \(T'\uparrow T\), show
\[
y_t\in L^\infty(a,T;L^2(I))\cap L^2(a,T;H^1_0(I)).\tag{12}
\]
The test uses the actual zero Dirichlet values; hence this estimate reaches both spatial endpoints in the Sobolev sense, not merely the interior. No estimate uniform as \(a\downarrow0\) is asserted. Equation (10) avoids claiming \(y_t(0)\) exists as a strong trace.

## 3. Consequences for \(B\) and the principal coefficient

### 3.1 Lower order

From (12) and the 1-D embedding \(H^1_0(I)\hookrightarrow L^\infty(I)\),
\[
y_t\in L^2(a,T;L^\infty(I)).\tag{13}
\]
Moreover the 1-D Gagliardo–Nirenberg inequality gives
\[
\|u\|_6^6\le C\|u\|_2^4\|u_x\|_2^2\quad(u\in H^1_0(I)),
\qquad \|y_t\|_{L^6((a,T)\times I)}^6
\le C\|y_t\|_{L^\infty_tL^2_x}^4\|y_{tx}\|_{L^2_{t,x}}^2.\tag{14}
\]
Since the mean projection is bounded on \(L^6(I)\) and the remaining terms in (3) are bounded, \(B\in L^6((a,T)\times I)\); indeed \(B\in L^\infty(a,T;L^2(I))\cap L^2(a,T;L^\infty(I))\) as well. These are delayed-cylinder statements including both spatial boundaries. Neither (12) nor (14) implies \(y_t\) or \(B\) is bounded jointly in space and time. The estimate does not establish \(y_t\in L^p\) globally across \(t=0\) for any \(p>2\).

### 3.2 Principal mass and metric regularity

From (1), for almost every \(t\in(a,T)\),
\[
\kappa y_{xx}=c y_t+d\theta Qy_t-F.
\]
All multipliers are bounded, \(Q\) is bounded on \(L^2\), and (12) gives
\[
\|y_{xx}\|_{L^\infty(a,T;L^2)}\le C_a,
\quad \|y\|_{L^\infty(a,T;H^2)}\le C_a,\tag{15}
\]
using the Dirichlet one-dimensional elliptic estimate. Thus \(\|y_x\|_{L^\infty((a,T)\times I)}\le C_a\), by \(H^1(I)\hookrightarrow L^\infty(I)\). In particular \((M_b)_x=d y_x\in L^\infty\), while \((M_b)_t=d y_t\) is only in the spaces in (12)–(14).

For \(s,t\in[a,T]\), absolute continuity in \(L^2\) gives \(\|y(t)-y(s)\|_2\le C_a|t-s|\). The interpolation inequality
\[
\|f\|_\infty\le C\|f\|_2^{3/4}\|f\|_{H^2}^{1/4}\tag{16}
\]
for \(f\in H^2(I)\cap H^1_0(I)\), together with (15), gives \(\|y(t)-y(s)\|_\infty\le C_a|t-s|^{3/4}\). This holds for continuous representatives, first for a.e. \(s,t\), then for all by continuity. Therefore
\[
|M_b(t,x)-M_b(s,x')|+\left|\frac\kappa{M_b(t,x)}-\frac\kappa{M_b(s,x')}\right|
\le C_a\big(|x-x'|+|t-s|^{1/2}\big).\tag{17}
\]
The positive lower bound on \(M_b\) justifies the reciprocal. In fact the time exponent obtained is \(3/4\), and the finite interval allows the weaker \(1/2\) form. For \(A=\kappa/M_b\), \(A_x=-\kappa d y_x/M_b^2\in L^\infty\), while \(A_t=-\kappa d y_t/M_b^2\) has the mixed-norm regularity above but is not shown \(L^\infty\). Metric Lipschitz continuity does **not** prove \(W^{1,\infty}_{t,x}\) or classical \(C^1\) coefficients.

### 3.3 Parameter dependence

Only the existing \(0<q<s_*\) was used, through existence, positivity, and (2). No stronger threshold is introduced. The bounds \(C_a\) may blow up as \(a\downarrow0\); the proof gives no usable numerical certificate for the unspecified load. Applying with any \(a<\delta\) establishes all displayed bounds on \(J=(\delta,T)\) with a finite constant.

## 4. Boundary, corners, and scope of further bootstrap

The imposed initial and Dirichlet temperature are compatible at order zero. For zero initial memory, \(m(0)=m'(0)=0\), \(v(0)=p(0)=y(0)=0\), so \(w(0)=E(0)=0\) in the natural continuous/data sense; the *formal* initial heat forcing vanishes. These identities suggest, but do not by themselves establish, higher-order corner compatibility or a trace \(y_t(0,0)=0\): \(y_t\) and \(y_{xx}\) are originally only \(L^2\). The calculation in §2 deliberately starts at a positive time and provides Sobolev boundary regularity, not classical differentiability at \((0,0)\) or \((L,0)\). The fact that the data are smooth does not, alone, supply a global theorem for the nonlocal nonlinear mass.

A further attempt at bounded \(y_t\) would require an independently justified parabolic smoothing estimate for the time-difference system with the variable rank-one mass and coefficients containing \(Qy_t\), or a closed higher-energy estimate. Equation (4) is not a standard local scalar equation. Merely inserting \(F\in L^\infty\) into the mass inverse does not produce bounded \(y_t\), since the inverse also contains a rank-one term acting on \(y_{xx}\), known initially only in \(L^2\). Nor does (15) bound \(y_{xx}\) pointwise. No circular assumption \(y_t\in L^\infty\), differentiability of \(B\), or time analyticity is made.

## 5. Comparison with inspected boundary Carleman statements

The following are primary texts and actual theorem statements, not abstract-based claims. The comparisons concern a **scalar estimate with residual**, not the coupled memory problem. A time translation makes a theorem on an arbitrary positive-length time cylinder formally relevant to a delayed interval, subject to all its other hypotheses. “Not matched” means not justified from our results, not proof that the assumption fails.

1. **P. Gaitan, [Theorem 2.2](https://arxiv.org/html/0706.1422#S2.Thmtheorem2), *Inverse Conductivity Problem for a Parabolic Equation using a Carleman Estimate with One Observation*.** The displayed operator is \(\partial_t-\nabla\cdot(c(x)\nabla)\), with smooth positive **time-independent** conductivity in the paper's setup. On a bounded \(C^1\) domain with \(n\le3\), its weight has a \(C^4\) spatial function, nonvanishing gradient, and a boundary normal-sign condition outside the observed portion. For \(q\in H^1(t_0,T;H^2(\Omega))\) with zero lateral Dirichlet data, the theorem bounds weighted derivatives and \(q\) by a weighted normal derivative on the chosen boundary portion **plus** the weighted squared scalar PDE residual. A delayed interval is explicitly used in its setup. For our odd temperature, the interval domain and zero Dirichlet/one-endpoint trace are compatible with the 1-D geometry, and \(BY+SP\in L^2\), but \(A=\kappa/M_b\) is time dependent and not proved as the theorem's smooth \(c(x)\); the odd solution is only \(H^1_tL^2_x\cap L^2_tH^2_x\), not the displayed \(H^1_tH^2_x\). Treating \(B/M_b\) as part of the residual is legitimate in \(L^2\); absorbing it is an additional weighted estimate not supplied by the theorem. **NOT APPLICABLE DIRECTLY.**

2. **P. Albano and D. Tataru, [Theorem 3.1](https://ejde.math.txstate.edu/Volumes/2000/22/albano.pdf), *Carleman estimates and boundary observability for a coupled parabolic-hyperbolic system*.** Their scalar heat operator is \(\partial_t-\partial_i(b^{ij}\partial_j)+b^i\partial_i+b\) on a smooth bounded domain. H1 requires uniformly elliptic \(C^1\) principal coefficients and measurable bounded lower-order terms; the theorem uses a smooth weight with nonzero spatial gradient and a singular temporal factor. For the scalar Dirichlet problem with \(f\in L^2\) and initial datum \(H^1_0\), it estimates a weighted anisotropic order-two norm by \(\|e^{\tau\psi}f\|_2^2\) and a signed boundary normal-derivative integral. In 1-D, an appropriate monotone weight makes one endpoint the observed side; restriction/time translation permits a delayed cylinder. Writing \(Y_t-A Y_{xx}=\cdots\) in divergence form adds the drift \(A_xY_x\), now bounded by (15). However (17) and \(A_x\in L^\infty\) do not establish the theorem's \(C^1\) principal class; \(B/M_b\in L^6\), not established bounded. It can instead be included in the residual, but a weighted absorption proof would still be needed. The independent source \(SP/M_b\) also remains in \(f\). **NOT APPLICABLE DIRECTLY.**

A targeted search also found claims concerning rough-principal or unbounded lower-order coefficients, but no further boundary theorem was included without access to its full primary statement and precise hypotheses. In particular, parabolic-metric Lipschitz regularity in (17) is a potentially useful match for some rough-coefficient theories, but no inspected theorem here proves that it suffices for this endpoint global estimate with an \(L^6\) potential. No exhaustive literature claim is made.

## 6. Final classification and unresolved points

**REGULARITY UPGRADE PROVED.** The frozen active equations yield, for every positive cutoff, the improved temperature derivative and \(B\) classes and the parabolic-metric Lipschitz principal coefficient in §§2–3. The proof explicitly preserves the rank-one mean term and reaches the spatial boundary in Sobolev norms. The result is a coefficient upgrade, **not** a claim that the coefficient mismatch for a particular boundary theorem has been completely closed. Unresolved are joint boundedness of \(y_t\) and \(B\), \(W^{1,\infty}\) or \(C^1\) principal regularity, estimates through the initial corners, and a precise boundary Carleman theorem plus weighted absorption at these established classes. The independent memory source remains a separate issue; no unique-continuation conclusion is drawn.
