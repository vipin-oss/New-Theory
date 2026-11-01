# Direction 2: infinite-dimensional injectivity and square-sum investigation

**Decision: OPEN** for the actual full odd \(L^2\) flux operator. All assertions below are conditional on inherited actual-base and strong-solution hypotheses; no physical exact invisible initial state has been found. The user-requested full \(L^2\) space needs the full nonlocal system, not the odd reduction; see the operator reconstruction.

## Stronger exact delayed-graph reduction

In the additional actual nonzero small-load regime of `direction-2-small-load-predelay-memory-injectivity.md`, let \(D h=P(\delta)\) and \(A h=Y(\delta)\). \(D:H_o\to H_o\) is boundedly invertible and \(A:H_o\to V_o=H^1_0\cap H_o\) is bounded by the inherited energy estimate. Define the exact graph map \(G=AD^{-1}:H_o\to V_o\), bounded and compact as a map to \(H_o\) by Rellich. The delayed-state range of the analytical \(L^2\) extension is exactly \((Gp,p)\), \(p\in H_o\), not an arbitrary independent state pair. Physical \(H^2\)-admissible inputs generate only the corresponding subgraph with \(p\in D(H^2\cap H_o)\).

Let \(\mathcal R_\delta\) be the actual future observation map from \(V_o\times H_o\), and let \(O p=\mathcal R_\delta(Gp,p)\). Then \(\mathcal T=OD\). Since \(D\) is a bounded isomorphism,
\[\ker\mathcal T=0\iff\ker O=0\iff\overline{\operatorname{ran}(G^*,I)\mathcal R_\delta^*}=H_o.\tag{1}\]
Here \(G^*:V_o'\to H_o\), \(\mathcal R_\delta^*:L^2(J)\to V_o'\times H_o\). The second equivalence is Hilbert/Banach duality with the graph embedding; the control range need only be dense, not onto. This is an exact new characterization conditional on the earlier \(D\)-inverse proof; it does not prove the missing density. Compactness of \(G\) does not make \(O\) Fredholm.

## Routes B1–B3 and obstruction

**Boundary UC:** zero flux and zero Dirichlet data supply only Cauchy data for \(Y\), whose equation has the unknown source \(SP\). Neither \(Y=0\) inside nor \(P(\delta)=0\) follows from scalar homogeneous UC. Even a coupled Carleman estimate must retain the unknown graph state and the low regularity \(M_x\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\); a theorem requiring bounded coefficients, interior measurements, or a time-slice observation is not automatic.

**Adjoint:** (1) converts the target to the exact range of \((G^*,I)\mathcal R_\delta^*\), whose density is equivalent to density of the earlier \(\Pi_ow_f(0)\) range because \(\mathcal T^*=D^*O^*\); the two ranges are related by \(D^*\), not generally equal. We did not construct controls approximating a complete spatial basis, nor prove an annihilator is zero. Divergent control norms are compatible with density.

**Volterra/moments:** the exact forward substitution is in the reconstruction note. Its source \(S(t,x)e^{-\mu t}h(x)\) is not a separated known time factor times a static spatial coefficient, and the feedback involves the unknown \(Y\). Its causal invertibility on an interior function space does not imply invertibility after applying one boundary trace. Finite-mode Gram positivity does not extend uniformly as \(N\to\infty\).

## Route B4: independent square-sum decision

The leading input kernel is \(a(t)\ell(x)\), \(\ell=\sqrt{2/L}(L/4-x/2)\), and the residual has columns \(\rho_n\). Since \(\ell\) has nonzero endpoint values, use the residual rather than artificially imposing zero endpoint conditions on the full kernel. Under the inherited fractional regularity and zero trace of the residual,
\[R\in L^2(J;H^1(I))\iff\sum_nq_n^2\|\rho_n\|^2<\infty.\]
The inherited individual bound \(\rho_n=o(q_n^{-3/2})\) gives only \(\sum_{n\le N}q_n^2\|\rho_n\|^2=o(\log N)\). The fixed-feedback dyadic approximation criterion in `direction-2-observation-kernel-regularity-audit.md` §3 suffices, but has not been established for the actual \(S\). The series is **OPEN**: neither convergence nor failure is proved. An abstract diagonal sequence with an extra logarithm refutes the inference from the column bound alone, not the physical endpoint condition.

## Single next theorem target

Prove (or refute with an admissible state) the following **graph-sensitive boundary uniqueness lemma**: for the actual coefficients in the inherited regime and the specific \(G\) above, a future solution with initial \((Gp,p)\) and zero flux on \(J\) must have \(p=0\). Unlike a universal arbitrary-state boundary UC statement, this retains the full pre-delay graph; no quantitative \(L^2\) observability lower bound is postulated, since compactness rules it out. Establish an adjoint approximation or an exact infinite synthesis equation with justified convergence; do not infer the lemma from the compactness of \(G\).
