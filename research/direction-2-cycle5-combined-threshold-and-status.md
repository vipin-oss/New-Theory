# Cycle 5: compatible thresholds and distinct conclusions

**Dimensionless convention.** Set \(\xi=x/L\), \(\tau=t/T\), \(\Theta=\theta/\theta_*\), \(U=u/L\), \(Z=z\), and \(D=a+k\). Multiply the dimensionless heat equation by \(c\theta_*/D\), so the common-coupling constants are
\[a'=a/D,\quad k'=k/D,\quad b'=b\theta_*/D,\quad c'=c\theta_*/D,\quad \kappa'=\kappa\theta_*T/(DL^2),\quad \lambda'=\lambda T,\quad L'=T'=\theta_*'=1.\]
Then \(d'=(b')^2/(a'+k')\), \(q=|g_*|/L\), \(\delta'=1/100\), and **all** constants \(s_*',C_B',C_D',D_S',\mu',S_0'\) are recomputed in this same normalization. \(S_0'\) is the constant zero-load reference for the dimensionless odd equation, using the same source-amplitude convention as \(D_S'\). The prior isomorphism audit writes its linear heat equation with a different scalar normalization; before insertion convert its \(S_0,D_S,C_D\) coherently, or recompute them using the common-coupling forced energy. Ratios \(|S_0'|/D_S'\) and the resulting perturbation inequality are invariant under a common nonzero scaling of the linear heat equation; \(C_D'\) must be recomputed, not numerically copied.

A sufficient simultaneous interval is
\[0<q<q_{\rm all}:=\min\left\{\frac{s_*'}2,\ \frac{c'}{4d'C_B'},\ \frac{e^{-\mu'\delta'}}{2C_D'},\ \frac{|S_0'|}{2D_S'}\right\}.\tag{1}\]
The factor \(\sqrt{L'}=1\). If a perturbation constant vanishes, its associated ratio is \(+\infty\). Here \(\|y\|_{\mathcal E}\le2C_B'q\), \(\|D_\delta-D^0_\delta\|\le C_D'q\), and \(\|S-S_0'\|_\infty\le D_S'q\), uniformly for \(q<s_*'/2\). For frozen nonzero couplings, finite constants and \(S_0'\ne0\), (1) is nonempty. It does **not** verify that an unknown prescribed experimental amplitude belongs to it. The endpoint proof does not actually require the last two terms; they are included to put the endpoint and graph descriptions in one regime.

Assume additionally the exact active-base existence/positive-temperature/weak-initial theorem, the full-history odd forced well-posedness and strong trace estimate, and fixed finite \(T\), \(\delta>0\). Under these hypotheses the cycle-5 independent reconstruction establishes:

1. \(y_{tt}\in L^2L^2\), \(y_t\in L^\infty H^1_0\cap L^2H^2\), and \(S\in L^2H^3\cap H^1H^1\cap H^2L^2\).
2. For actual \(\mathcal T\phi_n=a/q_n+\rho_n\), \(\sum_nq_n^2\|\rho_n\|_{L^2(J)}^2<\infty\), with actual feedback and complete pre-delay history. This is conditional, not proved for the wider prior load regime.
3. The odd residual kernel is in \(L^2(J;H^1_0)\); since the leading profile is in \(H^1\), the full odd kernel lies in \(L^2(J;H^1)\). Volkov's inspected Theorem 1.1 yields \(\sum_m m^2s_m(\mathcal T)^2<\infty\): extend the operator by zero to the even input subspace. This is an upper compactness conclusion, not a lower estimate.

| Question | Status |
|---|---|
| Base bootstrap | CONDITIONALLY PROVED as above |
| Actual endpoint square function | CONDITIONALLY PROVED as above |
| Weighted singular-value sum | CONDITIONALLY PROVED consequence; not an injectivity statement |
| Graph UC / actual signed injectivity | OPEN |
| Adjoint density | OPEN; projection onto the unknown kernel remains |
| Physical coupled past | OPEN; distinct from analytical \(H_o\) or \(X_o\) |
| Nonlinear infinite-dimensional uniqueness | OPEN; compactness rules out a local Lipschitz inverse in the stated open-prior setting, not injectivity |

Graph isomorphism describes \(D_\delta\), not the observation operator. No foundational continuum theory or demonstrated scientific novelty is inferred.
