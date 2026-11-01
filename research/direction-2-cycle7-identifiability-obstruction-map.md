# Cycle 7: where information may be lost

**Decision: CONTINUE with a restricted finite-prior inverse problem; full odd-state injectivity remains OPEN.** All existing model and Cycle 5–6 classifications remain unchanged. This is Arena's analysis, not independent human certification.

For the actual active base, use \(H_o=L^2_o(I)\), \(V_o=H^1_0\cap H_o\), \(J=(\delta,T)\). The exact chain is
\[h\in H_o\xrightarrow{\text{full evolution }[0,\delta]}(A_\delta h,D_\delta h)=(Gp,p)\xrightarrow{\text{coupled }[\delta,T]}(Y,P)\xrightarrow{2A_0\kappa Y_x(0)}\mathcal T h\in L^2(J),\quad p=D_\delta h.\]
Under the separately stated dimensionless small-load threshold, \(D_\delta\) is an isomorphism, so the first arrow loses **no** mathematical information about \(h\). Its graph restriction is additional structure, not evidence of loss. The identity \(\mathcal T=O D_\delta\), \(O=\mathcal R_\delta(G,I)\), gives \(\ker\mathcal T=D_\delta^{-1}\ker O\). In reverse, transposition gives \(\mathcal T^*f=D_\delta^*(G^*,I)\mathcal R_\delta^*f\), with backward PDE–ODE propagation and terminal/boundary data in the weak formulation; \(\ker O=0\iff\overline{\operatorname{ran}O^*}=H_o\). Neither density nor exact adjoint range is established.

| Suspected mechanism | What is actually proved / unknown |
|---|---|
| Boundary information | On odd inputs two heat powers are opposites and force is zero; there is exactly one independent heat history. This does not prove that one history is insufficient for uniqueness. |
| Loading | A single prescribed active loading gives one actual operator; differing loadings need not change the kernel. Repeatability of the same physical \(h\) is unverified. |
| Delay | Restriction to \(J\) may remove information but no nonzero hidden state is known; reference injectivity survives every nonempty delayed interval. |
| Nonautonomy | Mode mixing and only finite Sobolev regularity invalidate the reference residue separation; this is a proof obstruction, not an established kernel. |
| Graph | Isomorphism retains the state and constrains reachable pairs; discarding it enlarges the problem improperly. |
| Distributed \(SP\) | Zero boundary Cauchy data do not eliminate this graph-dependent interior source or the initial ODE term. |
| Spectral smoothing | The conditional actual endpoint implies weighted singular-value summability and excludes \(H^{-s}\) lower estimates for \(s\le3/2\). The reference has super-polynomial decay; that rate is **not** transferred to actual coefficients. Ill-conditioning is not non-identifiability. |

The obstacles are a combination of graph-linked distributed memory, nonautonomous signed mode mixing and severe smoothing. No single factor has been proved to be the cause of an actual nontrivial kernel. The credible theorem below chooses a fixed finite prior rather than claiming full-state recovery.
