# Independent mathematical audit of adjoint criteria and interior recovery

**Date:** 1 November 2026. **Decision: REFORMULATE.** The adjoint-density and exact-range ratio criteria are mathematically correct. The transposition equations and the interior-recovery formula are correct under the explicit inherited base and forced-forward assumptions below; those assumptions and the experimental small-load condition are not numerically verified. These statements do **not** establish either separation condition for the prescribed boundary-only experiment. This report is an independent recalculation by Arena, not certification by an independent human. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. No new foundational continuum theory or novelty is claimed.

## 1. Exact problem, assumptions, and decomposition

Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), and let the fixed displacement be \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\). The actual even base has
\[
D=a_{\rm mat}+k,\quad r=k/D,\quad \alpha=a_{\rm mat}/D,\quad \beta=b_{\rm mat}/D,\quad
\gamma=\lambda\beta,\quad \mu=\lambda\alpha,\quad d=b_{\rm mat}^2/D,\quad Qv=v-\bar v,
\]
\[
M=c+d\theta_b,\quad S=\lambda\alpha(b_{\rm mat}r\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-b_{\rm mat}E_b-b_{\rm mat}r\gamma\theta_b+2k\gamma w_b.
\]
The material constant \(b_{\rm mat}\ne0\) is distinguished from the output vector \(b_*\) below. The exact odd-channel system is
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\ P(\cdot,0)=h,\quad Y(0,t)=Y(L,t)=0,
\quad \mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{1}
\]
There is no spatial endpoint condition on \(P\) or \(h\). Let \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), \(X=H^2(I)\cap H\), and \(Z=L^2(J)\). Oddness is reflection about \(L/2\).

**Explicit inherited assumptions.** We use the actual nonzero-loaded base, not frozen or prescribed substitute coefficients. Assume the inherited solution exists, the coefficients are even, \(0<m_0\le M\le m_1\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\), and
\[
S\in C([0,T];H^1(I))\cap H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)). \tag{2}
\]
Assume also the full-space, zero-initial forced solution map is linear and bounded from \(L^2_{t,x}\times L^2_{t,x}\) to
\[
\mathcal E\times H^1_tL^2_x,\qquad
\mathcal E=H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_0(I)), \tag{3}
\]
with uniqueness and parity preservation when the data are odd. The analogous strong homogeneous-input estimate and the independently audited high-frequency bound (7) below are also inherited. These hypotheses are sufficient for this audit; no independent existence theorem or physical parameter validation is claimed. \(\mathcal E\hookrightarrow C([0,T];H^1_0(I))\) in the usual parabolic trace sense.

With \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(\{\phi_n\}\) is an orthonormal basis for \(H\). Write \(\ell(x)=1-2x/L\); direct integration gives
\[
(\ell,\phi_n)=\frac{2\sqrt{2/L}}{q_n},\quad
 g:=\sum_{n\ge1}\frac{\phi_n}{q_n}=\frac{\ell}{2\sqrt{2/L}},\quad
\|g\|_2^2=\sum_nq_n^{-2}=\frac{L^2}{24}. \tag{4}
\]
The series converges in \(H\). Thus \(\Lambda h=(h,g)=\sum_nh_n/q_n\) is bounded with \(\|\Lambda\|=L/\sqrt{24}\), \(H_0=\ker\Lambda=g^\perp\) is closed, and \(u=q_1\phi_1\) satisfies \(\Lambda u=1\).

Let \(a_J(t)=2A_0\sqrt{2/L}\,e^{-\mu t}S(t,0)\). Its trace is in \(C([0,T])\), hence in \(Z\). For the actual columns \(k_n=\mathcal T\phi_n\), the inherited expansion is
\[
k_n=\frac{a_J}{q_n}+\rho_n,\qquad
\|\rho_n\|_Z\le C_\eta q_n^{-3/2+\eta},\quad 0<\eta<1/2. \tag{5}
\]
Choosing one such \(\eta\) gives \(\sum_n\|\rho_n\|_Z^2<\infty\). For \(h=\sum h_n\phi_n\), the series \(\mathcal Rh=\sum h_n\rho_n\) converges unconditionally in \(Z\); \(\mathcal R\) is Hilbert–Schmidt. On finite sums (5) gives \(\mathcal T=a_J\Lambda+\mathcal R\), and continuity extends the identity to all \(H\). Therefore \(\mathcal R=\mathcal T-a_J\Lambda\) is the **actual** remainder operator. The factors \(q_n^{-1}\) carry a length; \(g\) carries the matching input-space units, and \(a_J\Lambda h\) has output-flux units. \(\Lambda h=(h,\ell)/(2\sqrt{2/L})\) is a spatial integral, not \(h(0)\).

Let \(A=\mathcal R|_{H_0}=\mathcal T|_{H_0}\), \(b_*=\mathcal Tu\). The unique decomposition is
\[
h=v+cu,\quad c=\Lambda h,\quad v=h-(\Lambda h)u\in H_0,\quad
\mathcal Th=Av+cb_*. \tag{6}
\]
Then \(\ker\mathcal T=\{0\}\) iff \(\ker A=\{0\}\) and \(b_*\notin\operatorname{ran}A\): if \(b_*=Av\), \(u-v\ne0\) lies in the kernel; conversely a kernel vector with \(c\ne0\) implies \(b_*=A(-v/c)\), while \(c=0\) lies in \(\ker A\). This proof does not assume closed range.

## 2. Full transposition construction and signs

For arbitrary full-space \(F,G\in L^2((0,T)\times I)\), use the zero-initial solution of
\[
F=My_t-\kappa y_{xx}-By-Sp,\qquad G=p_t+\mu p-\gamma y. \tag{7}
\]
Since \(y\in L^2_tH^2_x\), the one-dimensional trace theorem yields
\[
\|y_x(0,\cdot)\|_{L^2(0,T)}\le C_I\|y\|_{L^2_tH^2_x}
\le C\bigl(\|F\|_{L^2_{t,x}}+\|G\|_{L^2_{t,x}}\bigr). \tag{8}
\]
Thus for each \(f\in Z\), the functional \(2A_0\kappa\int_J f(t)y_x(0,t)dt\) is bounded on the full forcing space. Riesz representation, using real Hilbert inner products, produces unique \((z_f,w_f)\in L^2_{t,x}^2\) with
\[
\iint(Fz_f+Gw_f)=2A_0\kappa\int_J f(t)y_x(0,t)dt,\quad
\|z_f\|_2+\|w_f\|_2\le C\|f\|_Z. \tag{9}
\]
The full-space estimate for arbitrary source pairs is an essential inherited hypothesis. Alternatively, an odd-space construction is possible, but it has the paired odd boundary normalization discussed below.

For compactly supported smooth \(y,p\), construct \(F,G\) by (7); uniqueness makes them the corresponding forward solutions, and the boundary functional vanishes. Testing \(y\) and \(p\) separately yields
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\qquad
-w_{f,t}+\mu w_f-Sz_f=0 \tag{10}
\]
in distributions. The \(-Bz_f\), \(-\gamma w_f\) and \(-Sz_f\) signs follow directly from (7). \(Mz_f\in L^2\) and \(Bz_f\in L^1\), so the first distribution is well-defined; no classical \(M_tz_f\) or boundary trace of \(z_f\) is needed.

Choose \(y=0\) and \(p\in H^1_tL^2_x\) with \(p(0)=0\), taking \(F=-Sp\), \(G=p_t+\mu p\). The resulting identity says
\[
\iint[p_t w_f+p(\mu w_f-Sz_f)]=0. \tag{11}
\]
With compact time tests this gives \(w_{f,t}=\mu w_f-Sz_f\in L^2_{t,x}\); hence \(w_f\in H^1_tL^2_x\). Integrating (11) by parts for arbitrary \(p(T)\in L^2\) gives \(w_f(T)=0\) in \(L^2(I)\). The terminal-value ODE has the unique Bochner solution
\[
w_f(t)=\int_t^T e^{-\mu(r-t)}S(r)z_f(r)\,dr. \tag{12}
\]
Here \(S\in L^\infty\), \(z_f\in L^2_{t,x}\), so the integrand is Bochner integrable in \(L^2_x\); (12) is in \(H^1_tL^2_x\) and has well-defined \(w_f(0)\).

For actual initial memory \(h\in H\), set \(p=P-e^{-\mu t}h\), \(y=Y\). Then \(y(0)=p(0)=0\), \(F=e^{-\mu t}Sh\), \(G=0\). Applying (9), (12), and Fubini gives
\[
(\mathcal Th,f)_Z=\int_0^T e^{-\mu t}(h,S(t)z_f(t))_{L^2(I)}dt
=(h,\Pi_o w_f(0))_H,\qquad \mathcal T^*f=\Pi_o w_f(0). \tag{13}
\]
The middle inner product is the full \(L^2(I)\) pairing; only the odd part is seen by \(h\). The integral is finite by \(S\in L^\infty\) and \(z_f\in L^2_{t,x}\). It runs over **all** \((0,T)\): although \(f\) is supported in \(J\), the backward adjoint can extend into the pre-delay interval.

For smooth fields only, Green's formula contains
\[
[\langle My,z\rangle+\langle p,w\rangle]_0^T+
\kappa\int_0^T[y_x(0)z(0)-y_x(L)z(L)]dt, \tag{14}
\]
plus the two residual-adjoint products. Thus the formal full-space choices \(z(0)=2A_0 1_J f\), \(z(L)=0\), \(Mz(T)=0\) give (9); after odd projection the formal boundary values are \(A_0 1_Jf\) and \(-A_0 1_Jf\). Because \(y_x(L)=y_x(0)\) for odd \(y\), both terms add to \(2A_0\kappa\int_Jfy_x(0)\). These are normalization checks, **not** a claim that \(z_f\in L^2\) has classical boundary or terminal traces. Equation (9) is the rigorous boundary/terminal specification.

## 3. The density criterion is an equivalence, not density

Let \(\Pi_0h=h-(h,g)g/\|g\|_2^2\). For \(v\in H_0\), \(Av=\mathcal Tv\). Using (13),
\[
(v,A^*f)_{H_0}=(Av,f)_Z=(v,\mathcal T^*f)_H,
\qquad A^*f=\Pi_0\Pi_o w_f(0). \tag{15}
\]
Both projections are bounded; \(H_0\) carries the inherited \(L^2\) norm. For any bounded Hilbert operator,
\[
(\operatorname{ran}A^*)^\perp=\ker A,
\quad\text{so}\quad
\ker A=\{0\}\iff\overline{\operatorname{ran}A^*}^{\,H_0}=H_0. \tag{16}
\]
Indeed \(v\perp\operatorname{ran}A^*\) iff \((Av,f)=0\) for all \(f\in Z\), iff \(Av=0\). Combining with (13), (16) is equivalent to
\[
\forall v\in H_0\setminus\{0\}\quad\exists f\in L^2(J):
\int_0^T e^{-\mu t}(v,S(t)z_f(t))_{L^2(I)}dt\ne0. \tag{17}
\]
This applies to **every** \(v\in H_0\), with no approximation argument or unjustified smoothness. Its validity as an equivalence does not establish that the right-hand statement holds. A finite family of tests, nonzero columns, or injectivity on a dense subspace does not prove it.

## 4. Exact range: ratio, separators, and singular system

Let \(A:H_0\to Z\) be any bounded real Hilbert-space operator and let \(b_*=\mathcal Tu\). Define
\[
\mathcal C=\sup_{f\in Z}\frac{|(b_*,f)_Z|}{\|A^*f\|_{H_0}}, \tag{18}
\]
using \(+\infty\) if the denominator is zero and the numerator nonzero, and zero for \(0/0\). This convention includes \(f=0\). Then
\[
\boxed{b_*\in\operatorname{ran}A\iff\mathcal C<\infty,\qquad
b_*\notin\operatorname{ran}A\iff\mathcal C=\infty.} \tag{19}
\]
**Proof.** If \(b_*=Av\), then \(|(b_*,f)|=|(v,A^*f)|\le\|v\|\|A^*f\|\), even when \(A^*f=0\). Conversely, if \(\mathcal C<\infty\), then \(A^*f=0\) implies \((b_*,f)=0\); hence \(L(A^*f)=(b_*,f)\) is independent of the representing \(f\). It is linear and bounded on \(\operatorname{ran}A^*\), with \(|L(A^*f)|\le\mathcal C\|A^*f\|\). It extends uniquely by continuity to \(\overline{\operatorname{ran}A^*}\). Riesz supplies \(v\) in that closed subspace of \(H_0\) such that \(L(A^*f)=(v,A^*f)=(Av,f)\) for all \(f\); hence \(b_*=Av\), an **exact** preimage. This covers \(\ker A^*\ne0\) and does not use compactness or closed range. If a preimage exists, its minimum-norm representative is this Riesz vector and \(\mathcal C\) equals its norm.

The separate cases are:

* If \(b_*\notin\overline{\operatorname{ran}A}\), orthogonal projection gives \(f\in\ker A^*\) with \((b_*,f)\ne0\); the ratio is infinite with zero denominator. This is bounded separation.
* If \(b_*\in\overline{\operatorname{ran}A}\setminus\operatorname{ran}A\), every \(f\in\ker A^*\) has \((b_*,f)=0\), so no bounded orthogonal separator exists, but (19) still forces the supremum to be infinite over nonzero denominators. Equivalently a sequence can be chosen with \(A^*f_j\ne0\) and ratios tending to infinity.
* If \(b_*\in\operatorname{ran}A\), the supremum is finite; in particular all numerator values vanish on \(\ker A^*\).

If \(b_*\notin\operatorname{ran}A\), the map \(L(Av+cb_*)=c\) is algebraically well-defined on \(\operatorname{ran}A+\operatorname{span}\{b_*\}\). It is bounded exactly when \(b_*\notin\overline{\operatorname{ran}A}\); in the closure-but-not-range case it is unbounded. This is conditional on already knowing nonmembership, not a method that proves it.

Under (5), \(A\) is compact. For its nonzero singular system \(Av_j=\sigma_jz_j\), \(A^*z_j=\sigma_jv_j\), \(\sigma_j>0\), finite or countable,
\[
b_*\in\operatorname{ran}A\iff b_*\perp\ker A^*,\quad
\sum_j\frac{|(b_*,z_j)_Z|^2}{\sigma_j^2}<\infty. \tag{20}
\]
Necessity uses Bessel on a preimage. Conversely the sum gives \(v=\sum_j (b_*,z_j)\sigma_j^{-1}v_j\in H_0\), and orthogonality to \(\ker A^*=(\overline{\operatorname{ran}A})^\perp\) implies \(Av=b_*\). Equation (20) is the standard compact-operator Picard criterion; (19) is a general bounded-operator fact. Neither evaluates the actual coefficients or singular data, and neither establishes that the actual ratio is infinite.

## 5. Actual-base full-interior recovery

The active base has initial equilibrium \(y_b(0)=0\), \(p_b(0)=0\), with \(\theta_b=\theta_*+y_b\). Its prescribed scalar mean strain \(m(t)=g_*L^{-1}\sin^2(\pi t/T)\) and mean memory \(v_b(t)=\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds\) satisfy \(m(0)=v_b(0)=0\). Since
\[
w_b=m-v_b-\alpha p_b+\beta Qy_b,\quad w_b(0)=0,
\]
the exact coupling at \(t=0\) is
\[
S(0,x)=\lambda\alpha b_{\rm mat}r\theta_*, \tag{21}
\]
constant in \(x\), nonzero for the frozen signs \(a_{\rm mat},k,\lambda,\theta_*>0\), \(b_{\rm mat}\ne0\). Its sign is \(\operatorname{sgn}b_{\rm mat}\), not necessarily positive. By (2) and the one-dimensional embedding \(H^1\hookrightarrow C^0\), \(S\in C_tC_x\). Thus for some \(\varepsilon\in(0,T]\) and \(s_0>0\), \(|S(t,x)|\ge s_0\) uniformly on \([0,\varepsilon]\times\bar I\). This is a qualitative consequence of the assumed base and its initial data, not numerical verification of its admissibility.

For any \(v\in H\), the memory ODE gives
\[
P(t)=e^{-\mu t}v+\gamma\int_0^t e^{-\mu(t-r)}Y(r)dr.
\]
Therefore
\[
D_Y:=MY_t-\kappa Y_{xx}-BY-\gamma S(t)\int_0^t e^{-\mu(t-r)}Y(r)dr
=e^{-\mu t}S(t,x)v(x) \tag{22}
\]
in \(L^2((0,T)\times I)\). Indeed \(M,S\in L^\infty\), \(Y_t,Y_{xx}\in L^2\), and \(BY\in L^2\) because \(B\in L^2\) and \(Y\in C_tH^1_x\hookrightarrow L^\infty_{t,x}\). The Volterra term is \(L^2\) by Young's inequality in time and boundedness of \(S\).

Let \(w(x)=\int_0^T e^{-2\mu t}|S(t,x)|^2dt\). Then
\[
w(x)\ge s_0^2\int_0^\varepsilon e^{-2\mu t}dt=:w_0>0,\quad
v(x)=\frac{\int_0^T e^{-\mu t}S(t,x)D_Y(t,x)dt}{w(x)}\quad\text{for a.e. }x. \tag{23}
\]
Fubini applies to the \(L^2\) equality (22) and the product in the numerator is \(L^1\) in time for a.e. \(x\). Cauchy–Schwarz gives
\[
\|v\|_{L^2(I)}\le w_0^{-1/2}\|D_Y\|_{L^2((0,T)\times I)}. \tag{24}
\]
Since \(\|D_Y\|_2\le C\|Y\|_{\mathcal E}\) for the fixed coefficients, (24) also gives strong-topology interior-data stability, not stability from noisy \(L^2\)-only temperature or boundary data.

**Clarification to the previous report:** full time \((0,T)\) is sufficient, not necessary. For any \(0<\tau\le\varepsilon\), the same formula and proof use integrals only over \((0,\tau)\), with \(w_\tau\ge s_0^2\int_0^\tau e^{-2\mu t}dt\); this still requires the complete spatial temperature field and its derivatives in the strong sense. More generally an interval \((t_1,t_2)\) suffices only if the weight there is bounded below **and** the earlier history \(Y|_{(0,t_1)}\) or the equivalent memory contribution is known; otherwise \(D_Y\) is unavailable. No overlap of the initial nonzero interval with delayed \(J\) has been shown. One boundary flux supplies neither the interior field nor its pre-delay history; (23) therefore proves no boundary-only injectivity.

## 6. Audit of the formal higher-order correction

The prior trial \(Y_n^a=e^{-\mu t}S\phi_n/(\kappa q_n^2)\), \(P_n^a=e^{-\mu t}\phi_n\), has first-equation residual
\[
F_n^a=\frac{e^{-\mu t}}{\kappa q_n^2}
\{[M(S_t-\mu S)-BS-\kappa S_{xx}]\phi_n-2\kappa S_x\phi_n'\}. \tag{25}
\]
Its leading oscillatory part is \(-2\sqrt{2/L}\,e^{-\mu t}S_x\cos(q_nx)/q_n\). Let formally
\[
Y_n^{(1)}=\frac{2\sqrt{2/L}e^{-\mu t}}{\kappa q_n^3}
\left[S_x(t,x)\cos(q_nx)-S_x(t,0)\ell(x)\right]. \tag{26}
\]
Since \(S\) is even about \(L/2\), \(S_x(L)=-S_x(0)\); since \(\cos(q_nL)=1\), \(\ell(0)=1\), \(\ell(L)=-1\), the bracket has zero traces at both endpoints whenever \(S_x(t)\in H^1\). Formally, differentiating twice yields a leading term \(-q_n^2 S_x\cos(q_nx)\), so \(-\kappa(Y_n^{(1)})_{xx}\) contributes \(+2\sqrt{2/L}e^{-\mu t}S_x\cos(q_nx)/q_n\), cancelling (25)'s leading cosine. The sign is correct.

To use the inherited **strong** forced estimate on (26), one sufficient route would assume \(S\in L^2_tH^3_x\), \(S_x\in H^1_tL^2_x\), and \(S_x(\cdot,0)\in H^1(0,T)\), with compatible initial trace. These are examples of sufficient conditions for the individual terms, not claimed necessary for every possible cancellation or weaker method. They are not consequences of (2). Formally
\[
\partial_xY_n^{(1)}(t,0)=\frac{2\sqrt{2/L}e^{-\mu t}}{\kappa q_n^3}
\left[S_{xx}(t,0)+\frac{2}{L}S_x(t,0)\right], \tag{27}
\]
but \(S_{xx}\in L^2_{t,x}\) has no general spatial endpoint trace. The latter failure is rigorous: pick a smooth \(\psi\) supported near zero with \(\psi''(0)\ne0\), and put \(s_\epsilon(x)=\epsilon^{3/2}[\psi(x/\epsilon)+\psi((L-x)/\epsilon)]\) for sufficiently small \(\epsilon\). These functions are smooth and even under reflection; \(\|s_\epsilon\|_{H^2}\) stays bounded while \(|s_\epsilon''(0)|=\epsilon^{-1/2}|\psi''(0)|\to\infty\). Thus second-derivative endpoint evaluation is not bounded on \(H^2\); this is not a physical counterexample.

The proposed formal spatial correction does not itself require differentiating \(B\) or \(M\). Further residual manipulations that differentiate \(BS\) would require information about \(B_x\). **Clarification:** while \(M_x\) alone does not control \(M_t\), the inherited base actually gives \(M_t=d(y_b)_t\in L^2_{t,x}\); this does not establish the stronger temporal or boundary regularity needed for arbitrary differentiated expansions. No \(B_x\) bound is asserted from \(B\in L^2\) alone. A higher-order theorem also needs to control the nonzero initial-temperature mismatch and memory forcing, and prove a boundary remainder smaller than the purported next term. The existing \(O(q_n^{-3/2+\eta})\) estimate does not do so. These observations block the stated strong-class correction under the available assumptions; they do **not** prove that every different second-order or delayed asymptotic is impossible.

## 7. Restricted \(H^2\) and stability audit

Set \(X_0^\Lambda=X\cap H_0\), \(A_X=A|_{X_0^\Lambda}\). As \(u=q_1\phi_1\in X\) and \(\Lambda u=1\), every \(h\in X\) has the unique (topological) direct-sum decomposition \(h=v+cu\) with \(v\in X_0^\Lambda\). Continuity of \(\Lambda\) on \(H^2\) makes the projection continuous. From (6), the same argument as in §1 proves
\[
\ker\mathcal T\cap X=\{0\}\iff
\ker A_X=\{0\}\quad\text{and}\quad b_*\notin A_X(X_0^\Lambda). \tag{28}
\]
This is weaker than \(L^2\)-injectivity: an \(H_0\) preimage of \(b_*\) need not belong to \(X\).

Let \(E(h)=h(0)\), a continuous functional on \(X\); note \(E(u)=0\). Endpoint identification on \(X\) is equivalent to \(\ker\mathcal T\cap X\subset\ker E\), which is exactly
\[
\ker A_X\subset\ker E,\qquad
\text{every }v\in X_0^\Lambda\text{ with }A_Xv=b_*\text{ has }E(v)=0. \tag{29}
\]
If the second solution set is empty, the second clause is vacuous. Necessity comes from testing \(v\) and \(u-v\); for sufficiency, if \(Av+cb_*=0\), use the first clause for \(c=0\), and otherwise put \(w=-v/c\), giving \(Aw=b_*\) and \(E(v+cu)=-cE(w)=0\).

For \(\mathcal B_R=\{h\in X:\|h\|_{H^2}\le R\}\), weak compactness of the \(H^2\) ball and compact embedding into \(L^2\) give a compact \(L^2\)-image of \(\mathcal B_R\), with every limit in \(X\). Boundedness of \(\mathcal T\) gives the qualitative modulus
\[
\sup\{\operatorname{dist}_{L^2}(h,\ker\mathcal T):h\in\mathcal B_R,\ \|\mathcal Th\|_Z\le\epsilon\}\to0. \tag{30}
\]
The distance is to the **full closed \(L^2\) kernel**, not necessarily to its intersection with \(X\). If \(\ker\mathcal T\cap X=\{0\}\), the same compactness argument gives \(\|h\|_2\to0\) on the constrained set. If only endpoint uniqueness holds, compact embedding \(H^2\Subset C^0\) and the same limiting argument give \(|E(h)|\to0\). For pairs in \(\mathcal B_R\), apply these statements to their difference in \(\mathcal B_{2R}\). No explicit rate, unbounded-class stability, or uniqueness follows without the respective premise.

## 8. Corrections, classifications, and verdict

No fatal error was found in the latest report's actual adjoint equations, density equivalence, ratio criterion, or interior formula under the explicitly stated inherited assumptions. Two precision corrections are recorded without modifying the frozen report: **(i)** its use of full-time interior data is sufficient but not necessary; arbitrarily short initial intervals work as in §5; **(ii)** the discussion of \(M_t\) should distinguish the absence of control from \(M_x\) alone from the actual inherited fact \(M_t=d(y_b)_t\in L^2\), which still does not supply the stronger traces needed in §6. The higher-order correction's separate regularity assumptions are a sufficient route, not a proof that all other methods fail.

| Central claim | Classification | Scope and gap |
|---|---|---|
| Fourier normalization, decomposition and two-part equivalence | CORRECT BUT ROUTINE | (4)–(6); actual column expansion conditional on inherited forward/base estimates. |
| Forced Riesz construction, signs, ODE terminal trace and \(\mathcal T^*\) | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | Full-space forced estimate, actual regularity and parity; (7)–(15). |
| Density criterion and equation-specific test | PROVED | Hilbert duality (16); the identification with (17) is conditional on the transposition construction. |
| Exact-range unbounded-ratio theorem | PROVED | General bounded Hilbert operator; no closed-range or injectivity assumption. |
| Compact singular-system criterion | CORRECT BUT ROUTINE | Picard criterion (20); no actual singular values are computed. |
| Initial coupling and interior recovery/stability | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | Actual base initial data and (2)–(3); full interior initial-time field, not boundary data. |
| Impossibility of evaluating \(S_{xx}(t,0)\) from stated \(H^2\) regularity | PROVED | Bump sequence in §6; not an impossibility theorem for every asymptotic method. |
| Restriction and endpoint criteria | PROVED | Algebraic equivalences (28)–(29), not their premises. |
| Qualitative bounded-class moduli | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | Compactness, bounded operator, and the separately stated uniqueness premise when needed. |
| Actual density, range exclusion, full injectivity or physical invisible input | NOT ESTABLISHED | Neither actual adjoint separation (17) nor unboundedness (18) has been proved. |
| Claim that the present estimates rule out every second-order asymptotic | FALSE | Only the proposed strong-class derivation is obstructed. |

**Explicit answers:** (1) Yes, conditionally, with boundary data encoded by transposition rather than unproved classical traces. (2) Yes; it is an equivalence, not a proof of density. (3) Yes: finite ratio is equivalent to membership in the **exact** range. (4) Yes, conditionally; a short initial interior interval suffices. (5) No. (6) The stated functional-space obstruction is valid for the proposed correction, with the \(M_t\) clarification above; it does not rule out all alternatives. (7) The missing theorem is an actual-system proof of (17) on all \(H_0\) and of divergence of (18) for \(b_*=\mathcal Tu\), or an exact fixed-experiment counterexample. The prescribed delayed endpoint trace has not been shown to determine the interior field or pre-delay memory. Dr. Gupta is the final decision-maker.
