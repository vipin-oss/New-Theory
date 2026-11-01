# Temporal bootstrap for the actual active base

**Classification: CONDITIONALLY PROVED.** In addition to the inherited positive small-load base theorem and its weak-initial solution class, assume in the same fixed consistent units (or after the nondimensionalization of `direction-2-independent-audit-pre-delay-isomorphism.md`)
\[0<q=|g_*|/L<\min\{s_*/2,\ c/(4d\sqrt L C_B)\}.\tag{1}\]
Here \(d=b^2/(a+k)>0\), and \(C_B,s_*\) are the base-theorem constants recomputed in those units. This is a positive symbolic range, not an experimentally verified amplitude. It implies \(d\|y\|_\infty\le2d\sqrt L C_Bq<c/2\). The conclusion is stronger than positive-time regularity: in the Sobolev sense on the whole fixed interval,
\[y_{tt}\in L^2(0,T;L^2),\quad y_t\in L^\infty(0,T;H^1_0)\cap L^2(0,T;H^2),\quad
S_{tt}\in L^2(0,T;L^2).\tag{2}\]
Also \(S\in L^2H^3\cap H^1H^1\cap H^2L^2\); consequently \(S_t\in H^1(0,T;L^2)\), including \([\delta/2,T]\). No classical initial-corner derivative or analyticity is asserted. Arena's calculation is not independent human certification.

## 1. Exact equation and coercivity

Use \(Q=I-\mathrm{mean}\), \(z=y_t\), \(p_t=-\mu p+\gamma Qy\), \(v_t=\lambda(m-v)\),
\[\mathsf M_\theta z-\kappa y_{xx}=H:=-b\theta E+k\lambda w^2,\quad \mathsf M_\theta=cI+d\theta Q,\quad E=m'+rp_t,\quad w=m-v-\alpha p+\beta Qy.\]
The mass is not generally self-adjoint in unweighted \(L^2\). Under (1), for every real \(u\in L^2\),
\[(\mathsf M_\theta u,u)=c\|u\|^2+d\theta_*\|Qu\|^2+d(yQu,u)\ge(c-d\|y\|_\infty)\|u\|^2\ge(c/2)\|u\|^2.\tag{3}\]
The extra threshold is used exactly here, both at \(t\) and at shifted times. It is not inferred merely from \(\theta>0\). The mean mode remains in \(Q\).

Formally differentiating gives the precise equation
\[\mathsf M_\theta z_t-\kappa z_{xx}=-d zQz-b(zE+\theta E_t)+2k\lambda w w_t,\tag{4}\]
\[p_{tt}=-\mu p_t+\gamma Qz,\quad E_t=m''+r(-\mu p_t+\gamma Qz),\quad w_t=m'-v_t-\alpha p_t+\beta Qz.\tag{5}\]
Thus the derivative of the mean is \(Qz_t=z_t-\overline{z_t}\), and \(\partial_t(\theta Qz)=zQz+\theta Qz_t\). We do not differentiate the mass inverse. Equation (4) is justified only after the quotient limit below; it is not used as a starting regularity assumption.

## 2. A startup estimate without a classical corner trace

The base strong solution has \(y(0)=p(0)=v(0)=0\); \(m(0)=m'(0)=0\), and the prescribed smooth load satisfies \(|m'(t)|\le Ct\), \(|m(t)|\le Ct^2\), \(|v(t)|\le Ct^3\). Using the already established bounded \(\theta,w\), the actual ODEs, and \(\|y\|_2\le C\|y_x\|_2\),
\[\|H(t)\|_2\le C(|m'(t)|+|m(t)|+|v(t)|+\|p(t)\|_2+\|y_x(t)\|_2).\tag{6}\]
Test the strong heat equation by \(y_t\), the \(p\)-ODE by \(p\), and use (3), Young and Poincaré. For \(X=\kappa\|y_x\|_2^2+\|p\|_2^2\),
\[X'(t)+c_1\|y_t(t)\|_2^2\le C X(t)+C(|m'|^2+|m|^2+|v|^2),\quad X(0)=0.\tag{7}\]
The tests are legitimate for \(y\in H^1_tL^2\cap L^2_tH^2\cap C_tH^1_0\), \(p\in H^1_tL^2\); no \(y_t(0)\) is needed. Gronwall yields \(X(t)\le Ct^3\) for \(t\in[0,T]\), after enlarging \(C\) if necessary. In particular the difference-quotient initial data satisfy
\[\|[y(h)-y(0)]/h\|_{H^1_0}+\|[p(h)-p(0)]/h\|_2\le C h^{1/2}.\tag{8}\]
This is a Sobolev estimate at the initial time, not corner-classical compatibility.

## 3. First quotient energy globally

For \(h>0\), set \(z_h=\Delta_hy\), \(\pi_h=\Delta_hp\), \(\nu_h=\Delta_hv\), \(\Theta=\theta(t+h)\). Difference the actual strong equations in \(L^2\):
\[\mathsf M_\Theta(z_h)_t-\kappa(z_h)_{xx}=\Delta_hH-dz_hQy_t(t),\quad (\pi_h)_t=-\mu\pi_h+\gamma Qz_h.\tag{9}\]
Also
\[\Delta_hE=\Delta_hm'+r(-\mu\pi_h+\gamma Qz_h),\quad
\Delta_hw=\Delta_hm-\nu_h-\alpha\pi_h+\beta Qz_h,\]
\[\Delta_hH=-b(z_hE(t+h)+\theta(t)\Delta_hE)+k\lambda(w(t+h)+w(t))\Delta_hw.\tag{10}\]
Smooth \(m\), bounded \(v_t,\theta,E,w\) imply \(\|\Delta_hH(t)\|_2\le C(1+\|z_h(t)\|_2+\|\pi_h(t)\|_2)\), uniformly in \(h\).

Use the rigorous weighted test \(z_h/\Theta\) and the \(\pi_h\) test described in `direction-2-active-base-regularity-independent-audit.md` §§2–4. It gives
\[\mathcal H_h'+c_0\|(z_h)_x\|_2^2\le C(1+K_h)\mathcal H_h+C,\quad
\mathcal H_h=c\int z_h^2/\Theta+d\|Qz_h\|_2^2+\|\pi_h\|_2^2,\tag{11}\]
where \(\int_0^{T-h}K_h\le C\) uniformly, since \(y_t\in L^2(Q)\) and \(\theta_x\in L^\infty_tL^2_x\). The quotient has the needed strong regularity for each fixed \(h\), so the weighted chain rule is valid. Unlike the earlier positive-time averaging argument, (8) gives uniformly bounded initial \(\mathcal H_h(0)\). Gronwall from zero and integration yield
\[\sup_{t\le T-h}(\|z_h(t)\|_2+\|\pi_h(t)\|_2)+\|(z_h)_x\|_{L^2((0,T-h)\times I)}\le C.\tag{12}\]
Translation convergence \(z_h\to y_t\) in \(L^2\) and weak compactness imply \(y_t\in L^\infty_tL^2\cap L^2_tH^1_0\) globally. The proof uses the original nonlocal weighted energy, not a claim that \(Qy_t=y_t\).

## 4. Second energy, passage, and source amplitude

With the just-proved \(y_t\in L^\infty_tL^2\), (12) and 1D \(H^1_0\hookrightarrow L^\infty\) give
\[\|z_hQy_t\|_{L^2((0,T-h)\times I)}\le C\|y_t\|_{L^\infty_tL^2_x}\|z_h\|_{L^2_tH^1_x}\le C.\tag{13}\]
By (10), \(\Delta_hH\) is uniformly \(L^2\). Test (9) by \((z_h)_t\), now legitimate for each fixed \(h\); use (3) for \(\Theta\), Young, and the initial \(H^1\) estimate (8):
\[\sup_{t\le T-h}\|(z_h)_x(t)\|_2^2+\|(z_h)_t\|_{L^2}^2\le C.\tag{14}\]
Rearrange (9), using bounded mass, (13), and \(\Delta_hH\), to get \(\|(z_h)_{xx}\|_{L^2}\le C\). Exhausting \((0,T)\), weak compactness and translation convergence identify \((z_h)_t\rightharpoonup y_{tt}\) and \((z_h)_{xx}\rightharpoonup(y_t)_{xx}\), proving (2) for \(y\). The limit equation (4) holds in \(L^2\): \(zQz\in L^2\) by \(z\in L^\infty L^2\cap L^2H^1\); all remaining terms are \(L^2\). The mean derivative in (5) is valid as \(Q\) is bounded on \(L^2\).

To transfer to \(S\), first \(p\in C_tH^2\) by its Volterra formula and \(y\in L^2H^2\). Since \(y\in C_tH^1\), \(p_t\in L^\infty_tH^1\); hence \(E,w,\theta\in L^\infty_tH^1\), and \(H\in L^\infty_tH^1\) by the 1D algebra property. From the base equation, \(y_{xx}=(cy_t+d\theta Qy_t-H)/\kappa\in L^2_tH^1\), so \(y\in L^2_tH^3\). The memory convolution then gives \(p\in H^1_tH^3\), and \(S=\mu(br\theta-2kw)\in L^2H^3\cap H^1H^1\). Equations (5) and \(y_{tt}\in L^2L^2\) yield \(S_{tt}=\mu[br y_{tt}-2k(m''-v''-\alpha p_{tt}+\beta Qy_{tt})]\in L^2L^2\). The fixed smooth loading and scalar ODE give bounded \(m'',v''\).

## 5. Analyticity assessment

The algebraic mass inverse and polynomial nonlinearities are analytic on a positive-temperature Banach neighborhood, and the load is analytic. However analytic time smoothing would additionally require a sectorial/maximal-regularity theorem for the full nonlocal mass and ODE in a specified boundary-compatible scale and analytic dependence of that solution operator. Those hypotheses are not established here. Equations (2) are sufficient for the endpoint route and do not imply analyticity or Gevrey bounds. Without the additional coercivity inequality in (1), step (14) cannot use the unweighted test as written; no assertion of failure of the actual solution is made.
