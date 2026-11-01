# Cycle 8: acquisition from finite time bins, and the point-sampling gap

## What is actually known

For the nonlinear forward solution \(y\), the existing space is \(\mathcal E=H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x})\). Consequently the nonlinear labeled outward heat-power difference \(\mathcal F(h)=A_0\kappa[y_x(0,\cdot)+y_x(L,\cdot)]\) is in \(L^2(J)\), and the forward map is \(C^2\) into this space. The two individual traces are \(L^2\) as well. These facts do **not** provide a continuous representative in time or justify \(\mathcal F(h)(t_k)\); an \(L^2\) equivalence class can be changed at each finite sample point without affecting the known data. We do not claim pointwise evaluation is impossible under further PDE regularity, only that it has not been proved by these estimates. Likewise the actual basis \(e_i\in L^2(J)\) has no justified point values.

## A rigorous finite-bin theorem under existing hypotheses

This is a new **model-specific corollary**, not a new general sampling theorem. Use the dimensionless convention and constants in the dependency audit. Let \(J=(\delta,T)\), and let \(I_j\), \(j=1,\ldots,K\), partition \(J\) into intervals of positive lengths \(\ell_j\), with \(\Delta=\max\ell_j\). Define finite integrated observations
\[b_j(h)=\ell_j^{-1/2}\int_{I_j}[\mathcal F(h)(t)-\mathcal F(0)(t)]dt,\qquad b(h)=(b_1,\ldots,b_K).\]
Every integral is well defined for \(L^2\) data. These are time-window **averages/integrals**, not instantaneous samples. Set \(P_K\) to the orthogonal projection onto functions constant on the intervals; \(\|b(h_1)-b(h_2)\|_{\ell^2}=\|P_K[\mathcal F(h_1)-\mathcal F(h_2)]\|_{L^2(J)}\).

Let \(k_n^0=\mathcal T_0\phi_n\), whose explicit two-exponential formula is in the finite-prior proof audit. Define the finite, known reference quantity
\[C_{N,J}=\left(\sum_{n=1}^N\|(k_n^0)'\|_{L^2(J)}^2\right)^{1/2}.\]
Let \(e_q=C_{\rm tr}qH_N<\sigma_N/2\), and \(r=K_2r_NK_N\le\sigma_N/4\) on the same convex \(H^2\) prior ball. If
\[a_K:=\sigma_N-e_q-\frac{\Delta}{\pi}C_{N,J}-r>0,\tag{1}\]
then for every two states in this ball,
\[\boxed{\quad\|b(h_1)-b(h_2)\|_{\ell^2}\ge a_K\|h_1-h_2\|_{L^2(I)}.\quad}\tag{2}\]
In particular, the sufficient condition \(\Delta C_{N,J}/\pi<\sigma_N/4\) makes \(a_K>0\). This requires no time derivative of the **actual** flux.

**Proof.** For each interval, the sharp mean-zero Poincaré inequality gives \(\|f-f_{I_j}\|_{L^2(I_j)}\le(\ell_j/\pi)\|f'\|_{L^2(I_j)}\). For \(v=\sum v_n\phi_n\), Cauchy–Schwarz and orthonormality give
\[\|(I-P_K)\mathcal T_0v\|\le(\Delta/\pi)\|(\mathcal T_0v)'\|\le(\Delta/\pi)C_{N,J}\|v\|_2.\]
Thus \(\|P_K\mathcal T_0v\|\ge(\sigma_N-\Delta C_{N,J}/\pi)\|v\|_2\). The actual/reference operator difference has norm at most \(e_q\); projection is a contraction. The nonlinear two-point derivative remainder has norm at most \(r\|h_1-h_2\|_2\), again unchanged by projection. The reverse triangle inequality proves (2). Because \(C_{N,J}<\infty\) and \(\sigma_N>0\), some finite partition satisfies (1). Its \(K\times N\) matrix \(B_{jn}=\ell_j^{-1/2}\int_{I_j}\mathcal T\phi_n\) consequently has \(s_{\min}(B)\ge\sigma_N-e_q-\Delta C_{N,J}/\pi>0\), hence \(K\ge N\); no numerical rank calculation is being substituted for proof. If a proposed coarse partition has \(K<N\), the displayed sufficient condition cannot hold.

This explicit mesh condition uses the analytic **reference** derivative, the actual perturbation bound and actual nonlinear remainder; it does not infer temporal smoothness of the active coefficients. The constants, including \(K_2\), may be extremely conservative and are not experimentally calibrated. The construction provides a finite acquisition model, but actual instrumentation must measure integrated heat power over those windows with quantified error.

## Point samples and quadrature

The requested \(z_i^{(K)}=\sum_k w_k[\mathcal F(h)(t_k)-\mathcal F(0)(t_k)]e_i(t_k)\) is **not yet a well-defined theorem**. For it, prove time-continuous representatives for both the actual response and weights, and a uniform two-point quadrature bound
\[\|(z^{(K)}-z)(h_1)-(z^{(K)}-z)(h_2)\|_{\ell^2}\le\varepsilon_K\|h_1-h_2\|_2,\qquad\varepsilon_K<c_N/2.\tag{3}\]
Then Cycle 7 gives lower bound \(c_N/2-\varepsilon_K\). A uniform **absolute** error over the ball alone is not enough for this two-point Lipschitz conclusion. One sufficient route, not verified for the actual PDE, is a uniform bound for \(D\mathcal F(h)|_{V_N}:L^2\to H^s(J)\), \(s>1/2\), plus \(e_i\in H^s(J)\), together with an explicitly bounded quadrature rule on products; use the segment integral to get (3). Pointwise smoothness of the reference cannot be transferred to actual coefficients by an \(L^2\) operator perturbation. Numerical quadrature for an \(L^2\) flux from finitely many point values is not generally well defined.

Alternatively, replace each physical bin integral by a point-sampling approximation only after proving a **pairwise** error estimate \(\|b^{\rm sample}(h_1)-b^{\rm sample}(h_2)-[b(h_1)-b(h_2)]\|\le\varepsilon_K\|h_1-h_2\|_2<a_K\|h_1-h_2\|_2\); the lower bound becomes \(a_K-\varepsilon_K\). An absolute acquisition error bound gives reconstruction error, but not this injectivity statement.

## Error bookkeeping

For a closed prior sub-ball, exact bin model and a least-squares minimizer, a data error \(\eta_{\rm tot}\) gives \(\|\hat h-v\|_2\le2\eta_{\rm tot}/a_K\) relative to any feasible prior approximation \(v\). Separate and bound in the **same normalized \(\ell^2\) coordinates**: sensor error, finite quadrature or sensor-window approximation, parameter uncertainty, forward-solver error, base subtraction error, and preparation/prior mismatch. Their norms can be added only after each is independently estimated. Unknown preparation \(h-v\) additionally enters the desired true-state error. No sensor bandwidth, mesh size, material value or numerical solver certification is supplied.
