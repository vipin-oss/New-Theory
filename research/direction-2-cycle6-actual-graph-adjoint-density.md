# Cycle 6: graph-adjoint density, comparison controls and a structured sufficient condition

**Actual density: OPEN.** Let \(O=\mathcal R_\delta(G,I):H_o\to Z\), \(G=A_\delta D_\delta^{-1}\). For \(f\in Z\) the bounded restart transposition gives \((\xi_f,\eta_f)=\mathcal R_\delta^*f\in V_o'\times H_o\), and
\[O^*f=G^*\xi_f+\eta_f.\tag{1}\]
The adjoint distribution contains \(-\partial_t(Mz)\), not merely \(-Mz_t\); terminal and boundary values are encoded in the weak/transposition construction in `direction-2-exact-adjoint-and-observability.md`. Equation (1) incorporates the actual pre-delay graph; it is not a claim that \(\eta_f\) alone is controllable.

For \(f_{n,\alpha}=(OO^*+\alpha I)^{-1}O\phi_n\), the resolvent identity yields \(O^*f_{n,\alpha}-\phi_n=-\alpha(O^*O+\alpha I)^{-1}\phi_n\), so spectral dominated convergence gives
\[\lim_{\alpha\downarrow0}\|O^*f_{n,\alpha}-\phi_n\|=\|\Pi_{\ker O}\phi_n\|.\tag{2}\]
All projections must vanish to establish density. Tikhonov controls identify the missing projection; they do not show it vanishes, or provide exact range or bounded costs.

The independently rechecked \(O_0\) is injective on the reference graph, so \(\operatorname{ran}O_0^*\) is dense. For any reference control \(f\),
\[\|O^*f-\phi_n\|\le\|O_0^*f-\phi_n\|+\|(O-O_0)^*f\|.\tag{3}\]
The first term can tend to zero, but the norm \(\|f\|\) may diverge; this is especially material because the reference singular values decay faster than any power. No fixed small operator-norm perturbation controls the second term. The explicit compact-operator construction in `direction-2-infinite-mode-reference-and-perturbation-barrier.md` confirms this logical failure, not physical noninjectivity.

A **conditional structured theorem** pinpoints a possible transfer: if the actual coefficient evolution were shown to factor exactly as \(O=L O_0 R\), with bounded injective \(L:Z\to Z\) and bounded injective \(R:H_o\to H_o\), then \(Op=0\Rightarrow O_0Rp=0\Rightarrow p=0\), and (2) vanishes. This statement is a taut but complete operator theorem, not an asserted representation of the actual PDE; no such \(L,R\) have been constructed. A weaker sufficient concrete task is for every \(n\) to find actual controls \(f_{n,k}\) with \(\|O_0^*f_{n,k}-\phi_n\|\to0\) **and** \(\|(O-O_0)^*f_{n,k}\|\to0\); the latter is the missing coefficient-specific estimate. Equation (3), compactness, endpoint \(H^1\)-kernel regularity, and individual nonzero columns do not prove it.

Analytic-in-time nonautonomous evolution could support a different constructive continuation of adjoint controls, but requires the unverified sectorial/common-domain and trace conditions in the coupled-boundary report, and even then the graph cancellation must be excluded. No full-range or nonlinear uniqueness conclusion follows.
