# Cycle 5: graph-linked uniqueness and the exact next estimate

**Graph uniqueness and adjoint density remain OPEN.** Let \(p=P(\delta)\), \(G=A_\delta D_\delta^{-1}\) in the dimensionless combined threshold and put \(O=\mathcal R_\delta(G,I)\). The graph is \(Y(\delta)=Gp\), \(P(\delta)=p\). For \(F=SP=MY_t-\kappa Y_{xx}-BY\), the actual Volterra formula is
\[P(t)=e^{-\mu(t-\delta)}p+\gamma\int_\delta^te^{-\mu(t-s)}Y(s)\,ds,\quad
F(t)=S(t)e^{-\mu(t-\delta)}p+\gamma S(t)\int_\delta^te^{-\mu(t-s)}Y(s)ds.\tag{1}\]
Since \(S_t\in L^\infty\) and \(P,P_t\in L^\infty_tL^2_x\), \(F\in H^1_tL^2_x\) and \(F_t+\mu F=S_tP+\gamma SY\). If \(|S|\ge |S_0|/2\), then \((\partial_t+\mu-S_t/S)F=\gamma SY\) in \(L^2\), with \(F(\delta)=S(\delta)p\). This is an interior equality; arbitrary \(p\in L^2\) does not provide a boundary trace for \(P\) or \(F\).

The upgraded coefficient bounds and positive-time quotient calculation in the latest graph report yield \(Y_x(0,\cdot)\in H^1(a,T)\) for each \(a>0\). Thus if the observation vanishes on \(J\), both \(Y_x(0,\cdot)\) and the well-defined \((Y_t)_x(0,\cdot)\) vanish a.e. there. Let \(Z=Y_t\), \(W=P_t\); quotient passage gives
\[MZ_t-\kappa Z_{xx}=(B-M_t)Z+SW+B_tY+S_tP,\quad W_t+\mu W=\gamma Z.\tag{2}\]
The differentiated system still has interior source \(B_tY+S_tP\), and its initial values depend on the graph, not independent zero data. A boundary Carleman estimate for a homogeneous scalar equation cannot discard these terms. A centered-time ODE weight can reduce the Volterra integral, but (1) retains the weighted initial \(p\) term; graph compactness \(G:H_o\to H^1_0\) gives no lower bound. We have not derived an absorption inequality tying that term to the single observed boundary trace.

A precise sufficient target is: for some \(s>0,C<\infty\), prove for all \(p\in H_o\) and the **actual** graph solution
\[\|p\|_{H^{-s}(I)}\le C\|O p\|_{L^2(J)}.\tag{3}\]
Alternatively a weaker qualitative implication \(Op=0\Rightarrow p=0\) would suffice, so (3) is not asserted necessary. In a weighted Carleman derivation an intermediate target is an inequality that bounds the weighted initial term \(\|e^{s\varphi(\delta,\cdot)}S(\delta)p\|\) and the distributed term \(B_tY+S_tP\) by the *same* boundary observation plus genuinely absorbable weighted solution terms; neither has been proved. An operator-norm perturbation from a reference dense range is insufficient without control of the blow-up of reference controls.

For \(f_{n,\alpha}=(OO^*+\alpha I)^{-1}O\phi_n\), the exact resolvent identity gives \(O^*f_{n,\alpha}-\phi_n=-\alpha(O^*O+\alpha I)^{-1}\phi_n\). Spectral dominated convergence yields \(\|O^*f_{n,\alpha}-\phi_n\|\to\|\Pi_{\ker O}\phi_n\|\). A proof that every such projection vanishes is exactly density; no such bound is available. \(H_o\), \(X_o=H^2\cap H_o\), and coupled admissible pasts are distinct, and no actual physical invisible trajectory is constructed. Nonlinear uniqueness remains open even if the derivative is injective.
