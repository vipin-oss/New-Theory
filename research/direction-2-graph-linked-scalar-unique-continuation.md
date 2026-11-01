# Graph-linked scalar residual and boundary uniqueness

**Classification: OPEN.** The conditional temporal bootstrap improves the coefficient and boundary-trace analysis below, but no graph-linked unique-continuation theorem or actual invisible state is proved. All statements invoke the actual base and strong forward estimates, the additional coercivity/load condition in `direction-2-active-base-temporal-bootstrap.md`, and, for the graph, the pre-delay isomorphism threshold. Assume also \(q<|S_0|/(2D_S)\) in the same nondimensional convention when dividing by \(S\); this additional positive symbolic threshold is not verified experimentally.

## 1. Better actual coefficients and forward time traces

The new base bounds give \(M_t=dy_{b,t}\in L^\infty_tH^1_x\subset L^\infty(Q)\), \(B\in L^\infty_tH^1_x\subset L^\infty(Q)\), \(B_t\in L^2(Q)\), and \(S_t\in L^\infty_tH^1_x\subset L^\infty(Q)\). For example \(B_t=-dQy_{b,tt}-bE_{b,t}-br\gamma y_{b,t}+2k\gamma w_{b,t}\); every term is \(L^2\), and \(Q\) is retained. The source bound gives \(|S|\ge|S_0|/2\), so \(S_t/S\in L^\infty(Q)\).

For any \(h\in H_o\), the actual forward solution additionally satisfies, for every \(a>0\),
\[Y_t\in H^1(a,T;L^2)\cap L^2(a,T;H^2\cap H^1_0),\qquad Y_x(0,\cdot)\in H^1(a,T).\tag{1}\]
Proof: for \(h_t>0\) denote forward time quotients by \(Z_h=\Delta_{h_t}Y\), \(W_h=\Delta_{h_t}P\), and a superscript \(+\) means time shift. The exact quotient equations are
\[M^+(Z_h)_t-\kappa(Z_h)_{xx}=B^+Z_h+S^+W_h+(\Delta B)Y+(\Delta S)P-(\Delta M)Y_t,\quad (W_h)_t+\mu W_h=\gamma Z_h.\tag{2}\]
The strong original solution gives \(Y\in L^\infty_tH^1_0\subset L^\infty(Q)\), \(P\in C_tL^2\), \(P_t\in L^\infty_tL^2\). Consequently \(W_h\) is uniformly \(L^\infty_tL^2\); \(\Delta B\) is uniformly \(L^2(Q)\), while \(\Delta M,\Delta S\) are uniformly \(L^\infty(Q)\). Thus the last three terms in (2) are uniformly \(L^2\). Jensen gives a uniform \(L^2_tL^2_x\) bound for \(Z_h\).

Test (2) by \(Z_h\). The identity \((M^+(Z_h)_t,Z_h)=\frac12\partial_t\int M^+Z_h^2-\frac12\int M_t^+Z_h^2\) is valid for fixed \(h_t\), and \(M_t^+\) is bounded. Choose a starting time in \((a/4,a/2)\) by averaging the Jensen bound and apply Gronwall. This gives a uniform \(L^\infty(a/2,T-h_t;L^2)\cap L^2(a/2,T-h_t;H^1_0)\) bound on \(Z_h\). Choose a second starting time in \((a/2,a)\) by averaging its \(H^1\) norm; now test (2) by \((Z_h)_t\). Since \(M^+\ge m_0>0\), the right side is uniformly \(L^2\), giving \((Z_h)_t\in L^2\), \(Z_h\in L^\infty H^1_0\), uniformly on \((a,T-h_t)\). The equation bounds \((Z_h)_{xx}\) in \(L^2\). Translation convergence and weak compactness, with exhaustion of \(T\), prove (1). A fixed increment has the required strong spaces, so no formal test is used.

The trace conclusion follows because \(Y\in H^1(a,T;H^2)\) and the map \(H^2(I)\to\mathbb R\), \(u\mapsto u_x(0)\), is bounded. Thus zero observed flux implies \((Y_t)_x(0,t)=0\) a.e. on \(J\), and zero Dirichlet trace gives \(Y_t=0\) at the endpoints in Sobolev trace sense. This does **not** imply a boundary trace of \(P\) or \(F\): \(P=e^{-\mu t}h+\gamma\int_0^te^{-\mu(t-s)}Y(s)ds\) contains arbitrary \(h\in L^2\).

## 2. Exact scalar equation and graph slices

Define \(F=MY_t-\kappa Y_{xx}-BY=SP\). Since \(S_t\in L^\infty(Q)\), \(P\in C_tL^2\), \(P_t\in L^\infty_tL^2\), we have \(F\in H^1_tL^2\) and
\[F_t+\mu F=S_tP+\gamma SY.\tag{3}\]
Thus \((\partial_t+\mu-S_t/S)F=\gamma SY\) in \(L^2\); the combined residual is differentiated as a whole. The graph slice is exactly \(Y(\delta)=Gp\), \(F(\delta)=S(\delta)p\) in \(V_o\times H_o\). The positive-time forward gain also permits the coupled differentiated equations
\[M(Y_t)_t-\kappa(Y_t)_{xx}=(B-M_t)Y_t+S P_t+B_tY+S_tP,\quad (P_t)_t+\mu P_t=\gamma Y_t.\tag{4}\]
Here \(B_tY\in L^2\), \(S_tP\in L^2\), and the remaining terms are \(L^2\); (4) follows from quotients, not unjustified expansion. The new boundary derivative trace is valid, but (4) still contains the unknown distributed terms \(B_tY+S_tP\).

Zero flux on \(J\) plus homogeneous Dirichlet traces supplies Cauchy data for \(Y\), and now for \(Y_t\); neither makes \(F\) zero. The residual equation has second time order and mixed \(\partial_t\partial_{xx}\), not an independently established fourth-order spatial elliptic operator. A Carleman proof must control \(F\) (or \(P\)) and its initial graph slice without assuming \(F|_{\partial I}\), and handle the bounded but nonanalytic nonautonomous coefficients. The time-slice term \(S(\delta)p\) survives Volterra elimination. No inspected primary theorem establishes this implication for the single endpoint flux and this constrained graph. Thus no homogeneous scalar UC theorem is applied.

A sufficient exact missing lemma is: if (3), the heat equation and graph slice hold in the strong/transposition class, and \(Y_x(0,\cdot)=0\) on \(J\), then \(p=0\). An observability inequality in a negative norm would suffice but is not necessary. The new \(Y_t\) trace lets one attempt a source-specific Carleman estimate with differentiated boundary data; its unclosed term is the interior \(S_tP+B_tY\), together with the graph-linked unknown \(p\). Smallness or boundedness of this source does not make it zero or yield a full-space coercive bound for a compact observation.

## 3. Signed synthesis and counterexample status

The series \(\sum_n h_nk_n\) converges in \(L^2(J)\) for all \(h\in H_o\). Even the now conditionally proved endpoint \(\sum q_n^2\|\rho_n\|^2<\infty\) does not prove signed independence; the rank-one abstract example in `direction-2-graph-and-square-function-interaction.md` already has this regularity and a mixed-sign kernel. It is not an actual PDE counterexample. No nonzero \(p\) with a verified actual complete trajectory and identically zero flux has been found.
