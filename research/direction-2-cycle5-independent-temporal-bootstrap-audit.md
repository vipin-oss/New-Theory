# Cycle 5: independent temporal-bootstrap recalculation

**Decision: CONDITIONALLY PROVED**, conditional on the cited base existence, positivity, solution class and bounds, and the extra coercivity inequality below. This is an Arena re-derivation, not an independent human certification. The full load history and projection remain unchanged.

## Inputs and mass

Work first in one fixed common-coupling unit system. Let \(Q u=u-L^{-1}\int_Iu\), \(\theta=\theta_*+y\), and \(\mathcal M_\theta=cI+d\theta Q\). We assume the actual fixed-point base \(y\in H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\cap C_tH^1_0\), \(p(0)=y(0)=v(0)=0\), \(\|y\|_{\mathcal E}\le2C_Bq\), and positive bounded \(\theta\), all from the cited base theorem. All constants in this document are finite and independent of quotient increment.

For real \(u\), orthogonality of \(Q\) gives
\[(\mathcal M_\theta u,u)=c\|u\|_2^2+d\theta_*\|Qu\|_2^2+d\int y(Qu)u
\ge(c-d\|y\|_\infty)\|u\|_2^2.\]
The adjoint is \(cI+dQ(\theta\cdot)\), not \(\mathcal M_\theta\) in general. The mean component has no positive \(d\theta_*\) contribution, so it cannot be dropped. \(\|y\|_\infty\le\sqrt L\sup_t\|y_x\|_2\le2\sqrt L C_Bq\), and \(q<c/(4d\sqrt L C_B)\) gives \(\mathcal M_\theta\ge c/2\) as a quadratic form. Same holds at shifted time. These quantities must share units: the exact dimensionless convention and combined interval are given in `direction-2-cycle5-combined-threshold-and-status.md`. No empirical values are claimed.

## Initial energy

The Volterra formula and \(Q\)-contraction give \(\|p_t\|_2\le\mu\|p\|_2+|\gamma|\|y\|_2\), \(\|w\|_2\le\sqrt L(|m|+|v|)+|\alpha|\|p\|_2+|\beta|\|y\|_2\). From the given class, \(\theta,w\) are bounded in space-time; hence
\[\|H\|_2\le C[|m'|+|m|+|v|+\|p\|_2+\|y_x\|_2].\tag{1}\]
Specifically, \(\|w^2\|_2\le\|w\|_\infty\|w\|_2\); Poincaré controls \(y\). Pair heat with \(y_t\), and the ODE with \(p\). The time chain rules are valid because \(y\in H^1_tL^2\cap L^2_tH^2\) and \(p\in H^1_tL^2\):
\[\tfrac12(\kappa\|y_x\|_2^2)' +(\mathcal M_\theta y_t,y_t)=(H,y_t),\quad \tfrac12(\|p\|_2^2)'=-\mu\|p\|_2^2+\gamma(Qy,p).\]
Young and Poincaré yield \(X'+c_1\|y_t\|^2\le CX+C(|m'|^2+|m|^2+|v|^2)\) for \(X=\kappa\|y_x\|^2+\|p\|^2\). Since \(m=q\operatorname{sgn}(g_*)\sin^2(\pi t/T)\), \(|m|\le Ct^2\), \(|m'|\le Ct\), and \(v=\lambda\int_0^te^{-\lambda(t-s)}m(s)ds=O(t^3)\). Gronwall from \(X(0)=0\) gives \(X(t)\le Ct^3\), and continuity of \(y\) in \(H^1_0\) and of \(p\) in \(L^2\) gives \(\|y(h)/h\|_{H^1_0}+\|p(h)/h\|_2\le C h^{1/2}\). No classical \(y_t(0)\) is invoked.

## Difference quotients: first energy

For \(0<h<T\), put \(z=\Delta_hy,\pi=\Delta_hp,\nu=\Delta_hv,\Theta=\theta(t+h)\). In \(L^2\),
\[\Delta_h(\theta Qy_t)=\Theta Qz_t+zQy_t,\quad \mathcal M_\Theta z_t-\kappa z_{xx}=H_h-dzQy_t,\quad \pi_t+\mu\pi=\gamma Qz.\tag{2}\]
The undivided product difference contains a factor \(h\). Moreover
\[H_h=-b(zE^++\theta[m_h'+r(-\mu\pi+\gamma Qz)])+k\lambda(w^++w)(m_h-\nu-\alpha\pi+\beta Qz).\]
Thus \(\|H_h(t)\|_2\le C(1+\|z\|_2+\|\pi\|_2)\), using \(m',m'',v_t,\theta,E,w\in L^\infty\). Here \(E,w\in L^\infty\) follows from \(y\in C_tH^1\) and the ODE, before any bootstrap.

For fixed \(h\), \(z\in H^1_tL^2\cap L^2_tH^2\cap C_tH^1_0\), so \(z/\Theta\in L^2_tH^1_0\) and is a valid multiplier. Because \(z,\Theta,1/\Theta\) are bounded and \(z_t,\Theta_t\in L^2\), the chain rule gives
\[(\mathcal M_\Theta z_t,z/\Theta)=\tfrac12\partial_t(c\!\int z^2/\Theta+d\|Qz\|_2^2)+\tfrac c2\int\Theta_tz^2/\Theta^2.\tag{3}\]
Integration by parts has no boundary term because \(z\) has zero Dirichlet trace:
\[-\kappa(z_{xx},z/\Theta)=\kappa\int |z_x|^2/\Theta-\kappa\int z_xz\Theta_x/\Theta^2.\]
For \(u\in H^1_0\), \(f,g\in L^2\), the one-dimensional Gagliardo–Nirenberg and Young inequalities yield
\[\int |f|u^2\le\epsilon\|u_x\|_2^2+C_\epsilon\|f\|_2^{4/3}\|u\|_2^2,\quad
\int |g u u_x|\le\epsilon\|u_x\|_2^2+C_\epsilon\|g\|_2^4\|u\|_2^2.\tag{4}\]
Use \(f=\Theta_t,Qy_t\), \(g=\Theta_x\), and pair the ODE with \(\pi\). For \(\mathcal H=c\int z^2/\Theta+d\|Qz\|^2+\|\pi\|^2\), uniform equivalence with \(\|z\|^2+\|\pi\|^2\) follows from \(0<\theta_{\min}\le\Theta\le\theta_{\max}\); we obtain
\[\mathcal H'+c_0\|z_x\|^2\le C(1+K_h)\mathcal H+C,\quad K_h=\|y_t(t+h)\|_2^{4/3}+\|Qy_t(t)\|_2^{4/3}+\|\theta_x(t+h)\|_2^4.\tag{5}\]
The integral of \(K_h\) is uniformly bounded by the original \(y_t\in L^2_tL^2\), \(\theta_x\in L^\infty_tL^2\), Hölder, and translation. The initial energy is uniformly bounded (indeed \(O(h)\)) by startup. Hence Gronwall starts at **zero**; an averaging start is not required in this stronger global argument. Independently, for any \(a>0\), Jensen gives a uniform \(L^2(0,a/2;L^2)\) quotient bound, so a start \(s_h\in(a/4,a/2)\) with bounded \(\mathcal H(s_h)\) gives the alternative positive-time result; one must choose \(h<a/4\). Weak compactness on \((0,T-\varepsilon)\), translation convergence in \(L^2\), and exhaustion then yield
\[y_t\in L^\infty(0,T;L^2)\cap L^2(0,T;H^1_0).\tag{6}\]
The weak-* limit on the full interval can be obtained by restriction to \((0,T-h)\) and zero extension, whose endpoint jump is immaterial for these bounds.

## Second energy and coefficient transfer

By (6), \(\|zQy_t\|_{L^2_{t,x}}\le C\|z\|_{L^2_tH^1}\|y_t\|_{L^\infty_tL^2}\); by (5), \(H_h\) is uniformly \(L^2\). Testing (2) by \(z_t\), using the nonsymmetric quadratic-form lower bound at \(\Theta\), yields
\[\tfrac{c}{4}\|z_t\|_2^2+\tfrac\kappa2(\|z_x\|_2^2)'\le C\|H_h-dzQy_t\|_2^2.\]
The startup \(\|z_x(0)\|=O(h^{1/2})\) closes the uniform bound. The equation gives \(z_{xx}=\kappa^{-1}(\mathcal M_\Theta z_t-H_h+dzQy_t)\), bounded in \(L^2\). Weak limits and strong translation convergence identify \(y_{tt}\in L^2L^2\), \(y_t\in L^\infty H^1_0\cap L^2H^2\). Consequently, with \(z=y_t\), the differentiated equation is valid in \(L^2\):
\[(cI+d\theta Q)z_t-\kappa z_{xx}=-d zQz-b(zE+\theta E_t)+2k\lambda ww_t,\quad E_t=m''+r(-\mu p_t+\gamma Qz),\quad w_t=m'-v_t-\alpha p_t+\beta Qz.\]
In particular the projection in \(Qz_t=z_t-\overline{z_t}\) is retained; the product \(zQz\in L^2\) follows from (6).

For \(p=\gamma\int_0^te^{-\mu(t-s)}Qy(s)ds\), \(Q:H^k\to H^k\) for \(k=1,2,3\); \(y\in L^2H^2\) implies \(p\in H^1H^2\subset C H^2\). Since \(y\in C H^1\), \(p_t=-\mu p+\gamma Qy\in L^\infty H^1\); hence \(\theta,E,w\in L^\infty H^1\), and \(H\in L^\infty H^1\) by the one-dimensional product algebra. Thus the exact base equation gives \(y_{xx}\in L^2H^1\), i.e. \(y\in L^2H^3\). Reapply the Volterra equation to get \(p\in H^1H^3\). Finally \(S=\mu(br\theta-2kw)\) has \(L^2H^3\cap H^1H^1\), and
\[p_{tt}=-\mu p_t+\gamma Qy_t,\quad w_{tt}=m''-v''-\alpha p_{tt}+\beta Qy_{tt},\quad S_{tt}=\mu(br y_{tt}-2kw_{tt})\in L^2L^2.\]
No extra classical boundary or initial trace is used. This confirms \(S\in L^2H^3\cap H^1H^1\cap H^2L^2\) under the stated inputs, not time analyticity.
