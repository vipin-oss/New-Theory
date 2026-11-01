# Graph-adjoint density and regularized controls

**Classification: OPEN.** The statement below independently verifies the Tikhonov identities, but not density.

Let \(H=H_o\), \(Z=L^2(J)\), \(O=\mathcal R_\delta(G,I):H\to Z\) under the pre-delay isomorphism. The bounded restart-to-flux map and the actual forward transposition construction yield \(O^*f=G^*\xi_f+\eta_f\), \((\xi_f,\eta_f)=\mathcal R_\delta^*f\). Distributionally the adjoint contains \(-\partial_t(Mz)\); its boundary data are transposition data, not an assumed classical adjoint trace.

For \(\alpha>0\), \(f_{n,\alpha}=(OO^*+\alpha I)^{-1}O\phi_n\). The resolvent intertwining identity, obtained by multiplying \((OO^*+\alpha I)O=O(O^*O+\alpha I)\) by both inverses, yields
\[O^*f_{n,\alpha}-\phi_n=-\alpha(O^*O+\alpha I)^{-1}\phi_n.\tag{1}\]
For the positive self-adjoint \(A=O^*O\), spectral calculus gives
\[\|O^*f_{n,\alpha}-\phi_n\|^2=\int_{[0,\|O\|^2]}\frac{\alpha^2}{(\lambda+\alpha)^2}\,d\|E_\lambda\phi_n\|^2
\longrightarrow\|E_{\{0\}}\phi_n\|^2=\|\Pi_{\ker O}\phi_n\|^2.\tag{2}\]
Dominated convergence applies; \(\ker A=\ker O\). The control bound \(\|f_{n,\alpha}\|\le(2\sqrt\alpha)^{-1}\) follows by maximizing \(s/(s^2+\alpha)\), using \(\|\phi_n\|=1\). Costs may diverge and no bounded control family is assumed.

Density \(\overline{\operatorname{ran}O^*}=H\) is equivalent to \(\Pi_{\ker O}=0\), equivalent to the limit in (2) vanishing for **every** sine. A valid graph-linked UC theorem would imply \(\ker O=0\), and then the regularized controls construct density via (2). Conversely these control limits would prove the graph theorem by completeness. The actual coefficient and boundary improvements in `direction-2-graph-linked-scalar-unique-continuation.md` do not yet bound these projections.

A reference-model control sequence fails to transfer automatically: the error is bounded by its reference error plus \(\|O-O_0\|\|f\|\), and approximation costs can diverge. Likewise the endpoint square-function theorem gives regularity of an integral kernel, not its synthesis injectivity. The exact next task is a coefficient-specific bound on the spectral measures near zero sufficient to show (2) vanishes, or a coupled boundary UC proof including \(p\) and the graph.
