# Cycle 7: two feasible formulations, with sharp scope

## A. Fixed finite prior and finite time-integrated measurements

**Previously established theorem, not a new discovery.** Take the frozen nonzero sinusoidal loading, \(0<\delta<T=10/\lambda\), fixed calibrated positive parameters and \(b,g_*\ne0\), and the inherited base existence/positivity, strong odd trace and \(C^2\) nonlinear forward-map assumptions. Use a fixed consistent unit convention or nondimensionalization. Let \(V_N=\operatorname{span}\{\phi_1,\dots,\phi_N\}\), \(\phi_n=\sqrt{2/L}\sin(2\pi nx/L)\), and \(\mathcal F\) the actual nonlinear flux-difference history on \(J\). The reference finite Gram has minimum singular value \(\sigma_N>0\). The independent-proof-audit report proves, under
\[0<q=|g_*|/L<\min\{q_0,\sigma_N/(2C_{\rm tr}H_N)\},\quad \|\mathcal T v\|_{L^2(J)}\ge c_N\|v\|_2,\quad c_N=\sigma_N/2,\quad v\in V_N.\tag{1}\]
Here the constants and hypotheses are exactly as in `direction-2-finite-prior-independent-proof-audit.md`; no numerical threshold is asserted for an unspecified specimen. The companion `direction-2-finite-prior-nonlinear-identifiability.md` already gives a sufficiently small \(H^2\)-ball in \(V_N\) with two-point lower bound \(c_N/2=\sigma_N/4\). These are conditional inherited results, not a general infinite-dimensional inverse theorem or an independent human certification.

**Finite-measurement corollary (elementary reformulation).** Let \(W_N=\mathcal T V_N\subset L^2(J)\) and choose an orthonormal basis \(e_i\) of \(W_N\). The \(N\) measurements
\[z_i(h)=\int_J[\mathcal F(h)-\mathcal F(0)]e_i(t)\,dt\]
are fixed by the independently calibrated base and known prior, not by the unknown \(h\). If a radius \(\rho>0\) is chosen such that on the ball \(B_\rho\subset V_N\), the derivative satisfies \(\|D\mathcal F(v)|_{V_N}-\mathcal T|_{V_N}\|_{L^2\to L^2(J)}\le c_N/2\), then
\[\|z(h_1)-z(h_2)\|_{\mathbb R^N}\ge(c_N/2)\|h_1-h_2\|_2,\qquad h_1,h_2\in B_\rho.\tag{2}\]
Proof: \(P_{W_N}\mathcal T v=\mathcal T v\). The fundamental theorem of calculus along the segment between \(h_1,h_2\) bounds the derivative remainder by \((c_N/2)\|h_1-h_2\|_2\); projection is a contraction, so (1) gives (2). In finite dimension, inherited \(C^2\) regularity and norm equivalence give such a radius, possibly very small and dependent on \(N\). The measurement vector is exactly the coordinate vector of \(P_{W_N}(\mathcal F(h)-\mathcal F(0))\); this is an ideal continuous-time weighted integration, not a claim about finitely many point samples.

If \(z^\eta=z(h)+e\), \(\|e\|\le\eta\), any exact solution \(\widehat h\in B_\rho\) of \(z(\widehat h)=z^\eta\) obeys \(\|\widehat h-h\|_2\le2\eta/c_N\). A constrained least-squares solution (when it exists on a chosen closed sub-ball containing \(h\)) has residual at most \(\eta\), hence error at most \(4\eta/c_N\). For a linear true state \(h=v+r\), \(v\in V_N\), model mismatch adds at most \(\|\mathcal T r\|\le\|\mathcal T\|\|r\|_2\) to the data error. For nonlinear out-of-prior states the mismatch is \(\|P_{W_N}(\mathcal F(h)-\mathcal F(v))\|\), only bounded by \(\|r\|\) under an independently justified derivative bound in the appropriate strong topology. The constants may deteriorate severely as \(N\) increases; (2) is not uniform in \(N\). The physical preparation must separately justify the finite prior and coupled-past compatibility.

## B. Finite moments of an unrestricted odd state: exact criterion, not a solved model theorem

Let \(H=H_o\), \(Z=L^2(J)\), \(T=\mathcal T\), and \(M:H\to\mathbb R^k\), \((Mh)_i=\langle h,\psi_i\rangle\). Then exact determination of the moments from noiseless data is equivalent to
\[\ker T\subseteq\ker M\quad\Longleftrightarrow\quad \psi_i\in\overline{\operatorname{ran}T^*}\;\text{ for each }i.\tag{3}\]
Proof: the first condition is exactly that all states with equal data have equal moments; Hilbert space orthogonality gives \((\ker T)^\perp=\overline{\operatorname{ran}T^*}\).

Stable linear moment recovery, \(\|Mh\|\le C\|Th\|\), holds **iff** every \(\psi_i\in\operatorname{ran}T^*\). If \(\psi_i=T^*f_i\), \((Mh)_i=\langle Th,f_i\rangle\) and \(C\le(\sum_i\|f_i\|^2)^{1/2}\). Conversely the inequality defines each coordinate as a bounded linear functional on \(\operatorname{ran}T\); extend it to \(Z\) and apply Riesz, giving \(\psi_i=T^*f_i\). For noisy data with \(\|e\|\le\eta\), this reconstruction has error at most \(\eta(\sum_i\|f_i\|^2)^{1/2}\).

The distinction between closure and exact range is essential: exact identifiability need not have a stable noise bound. Neither membership in (3) nor the existence of \(f_i\) is verified for any prescribed nonzero physical moment of the actual system. Taking \(\psi=T^*f\) manufactures a recoverable functional but does not establish its independent physical relevance. This criterion is standard operator theory, not a new continuum theory.
