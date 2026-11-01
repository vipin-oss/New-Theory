# Graph-sensitive uniqueness: control, elimination, and remaining gap

**Graph-sensitive boundary uniqueness: OPEN.** The following exact identities and conditional regularity gains do not prove a zero kernel. Assume the active-base and pre-delay hypotheses in the companion audits; \(H=H_o\), \(V=H^1_0\cap H_o\).

## 1. Constructive density test with an exact error formula

Set \(O=\mathcal R_\delta(G,I):H\to Z=L^2(J)\). The adjoint, with \((\xi_f,\eta_f)=\mathcal R_\delta^*f\in V'\times H\), is rigorously
\[O^*f=G^*\xi_f+\eta_f,\quad G^*=(D_\delta^{-1})^*A_\delta^*.\]
The backward pair is defined by the bounded forward transposition map; its distributional mass term is \(-\partial_t(Mz)\). It includes the exact propagation back to \(0\), not independent \(P(\delta)\) data.

For every target \(\phi_n\) and \(\alpha>0\), the explicit Tikhonov control
\[f_{n,\alpha}=(OO^*+\alpha I_Z)^{-1}O\phi_n\in Z\]
satisfies, by the bounded-operator spectral theorem,
\[O^*f_{n,\alpha}-\phi_n=-\alpha(O^*O+\alpha I_H)^{-1}\phi_n,\quad
\|f_{n,\alpha}\|_Z\le(2\sqrt\alpha)^{-1},\tag{1}\]
\[\lim_{\alpha\downarrow0}\|O^*f_{n,\alpha}-\phi_n\|_H
=\|\Pi_{\ker O}\phi_n\|_H.\tag{2}\]
Thus unbounded control costs are allowed, and this is a constructive regularization, but (2) makes the unsolved step explicit: prove the right-hand side vanishes for every \(n\). The compactness and Schatten estimates for \(G\) do not imply it.

A different comparison attempt uses controls for the injective constant reference operator. If \(f_{n,\varepsilon}^0\) approximates \(\phi_n\) through the reference adjoint with error \(\varepsilon\), then
\[\|O^*f_{n,\varepsilon}^0-\phi_n\|\le\varepsilon+\|O-O_0\|\,\|f_{n,\varepsilon}^0\|.\tag{3}\]
Even when a small-load comparison bound on \(\|O-O_0\|\) is established, it is fixed while the control norms can grow; (3) gives no vanishing bound. The existing abstract rank-one barrier makes this a real logical obstruction, not a physical counterexample. Nothing here assumes reference controls have a uniform cost.

## 2. Boundary-to-memory elimination, correctly interpreted

Let \(F=MY_t-\kappa Y_{xx}-BY=SP\). For every \(\varepsilon>0\), the actual regularity \(S_t\in L^2(\varepsilon,T;H^1_x)\hookrightarrow L^2_tL^\infty_x\), \(P\in C_tL^2_x\), and \(P_t=\gamma Y-\mu P\in L^2_tL^2_x\) imply
\[F\in H^1(\varepsilon,T;L^2_x),\qquad F_t+\mu F=S_tP+\gamma SY.\tag{4}\]
This is an equality in \(L^2((\varepsilon,T)\times I)\), proved by product approximation, and is useful additional time regularity **of the combined residual**, not separate regularity of \(MY_t\), \(Y_{xx}\), or \(BY\).

If the extra symbolic small-load condition \(q<|S_0|/(2D_S)\) is imposed in a consistent nondimensionalization, the inherited \(\|S-S_0\|_\infty\le D_Sq\), \(S_0\ne0\), gives \(|S|\ge|S_0|/2\). On positive-time cylinders one may then eliminate \(P\) as \(P=F/S\) and obtain in \(L^2\)
\[\bigl(\partial_t+\mu-S_t/S\bigr)\bigl(MY_t-\kappa Y_{xx}-BY\bigr)=\gamma SY.\tag{5}\]
The time derivative is the derivative of the **combined** \(L^2\) residual; treating the expanded terms as individually \(L^2\), or using \(B_t\), would be unjustified. At the delayed slice, \(F(\delta)=S(\delta)p\) in \(L^2\), \(Y(\delta)=Gp\); this follows from \(S\in C_tH^1_x\), \(P\in C_tL^2_x\), not a trace of \(Y_{xx}(\delta)\). The boundary data remain \(Y=0\), observed \(Y_x=0\). No time derivative of \(Y_x\) or boundary trace of \(F\) follows. A unique-continuation theorem for (5) would need exactly these graph-linked initial traces, rough \(S_t/S\), distributional principal terms, and this boundary geometry. None has been verified. The extra nonvanishing threshold is not numerically checked and is unnecessary for (4).

The alternative Volterra elimination
\[MY_t-\kappa Y_{xx}=BY+Se^{-\mu(t-\delta)}p+\gamma S\int_\delta^te^{-\mu(t-s)}Y(s)ds,\quad Y(\delta)=Gp\]
keeps an independent-looking forcing only as a shorthand: \(p\) is the graph coordinate, not an arbitrary external source. Scalar homogeneous UC cannot absorb the \(p\)-term. The control problem (1) and this eliminated equation describe the same obstruction in different spaces.

## 3. Signed synthesis, history, and nonlinear consequences

For every \(h=\sum h_n\phi_n\in H\), \(\sum h_n k_n\) converges in \(Z\) since the operator is bounded (indeed Hilbert–Schmidt). The actual expansion gives \(\sum h_n/q_n\) as a single scalar and a residual series; cancellation among mixed signs is not excluded. The positive-cone separator and finite Gram proofs do not establish arbitrary signed independence. We found no exact nonzero admissible physical invisible state; abstract perturbations and near-null vectors are not such states.

The weaker \(H^2\cap H\) question remains open separately: it is \((H^2\cap H)\cap\ker\mathcal T=\{0\}\). The graph inverse preserves that class by (5) of the structure report. A full past must additionally satisfy strain equilibrium, temperature and memory laws and their prescribed history; ODE-compatible memory alone is insufficient. **Physical past admissibility: OPEN.**

In the actual small-data \(H^2\) neighborhood the inherited solution/observation map is \(C^2\); its derivative on odd inputs is the compact \(\mathcal T\), and the full force/two-flux derivative is a fixed finite vector multiple of that scalar channel. The derivative kernel is unproved and its inverse is not bounded on infinite-dimensional \(H_o\): a compact operator cannot be bounded below there. Moreover, a local Lipschitz inverse at the base measured in either \(H_o\) or \(H^2\) on an open odd \(H^2\) neighborhood would, by differentiating along every \(H^2\) direction, give a lower bound for the derivative. The \(H_o\) lower bound extends by density and contradicts compactness; the \(H^2\) lower bound contradicts compactness of the derivative as an operator on \(H^2\). This is a conditional **stability obstruction**, not a noninjectivity proof. A continuous injective map on a compact prior may instead have only a qualitative modulus. **Nonlinear infinite-dimensional uniqueness: OPEN.**

**Exact next target:** establish \(\lim_{\alpha\downarrow0}\alpha\|(O^*O+\alpha I)^{-1}\phi_n\|=0\) for each \(n\), by a graph-specific Carleman/Volterra or constructive-control argument that includes (4)–(5) and justifies all boundary traces; alternatively exhibit a genuine nonzero \(h\) and its complete actual trajectory with identically zero delayed flux.
