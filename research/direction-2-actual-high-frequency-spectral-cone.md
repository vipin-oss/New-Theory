# Actual Direction 2: high-frequency spectral-cone separation

**CONDITIONALLY PROVED**, assuming the inherited actual nonzero-load base, its odd strong solution and the established refined column expansion. This is a restricted infinite-dimensional **separation** result, not injectivity on all inputs, and is Arena's analysis pending independent human audit. No positivity or Hopf lemma is used.

## Theorem

Let \(H_o=L^2_o(0,L)\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(q_n=2\pi n/L\), and \(\mathcal T\phi_n=a/q_n+\rho_n\) on \(J=(\delta,T)\). Suppose \(a\in L^2(J)\), \(\|a\|>0\), and \(q_n\|\rho_n\|\to0\). For the actual active coefficients the stronger inherited estimate \(\|\rho_n\|=o(q_n^{-3/2})\) supplies the last hypothesis. The explicit small-load sign regime in `direction-2-exact-identifiability-decision.md` ensures \(\|a\|>0\), with \(a(t)=2A_0\sqrt{2/L}e^{-\mu t}S(t,0)\); the numerical regime has not been verified for an experiment.

There exists a finite, base-dependent \(N\) such that, for every real \(h=\sum_{n\ge N}h_n\phi_n\in H_o\) whose coefficients are all nonnegative,
\[\langle\mathcal Th, a/\|a\|\rangle_{L^2(J)}\ge\frac{\|a\|}{2}\sum_{n\ge N}\frac{h_n}{q_n}.\tag{1}\]
The right-hand side is finite, and is strictly positive unless \(h=0\). For all nonpositive coefficients, the reverse-sign inequality holds. Consequently, whenever two odd initial states differ by such a nonzero high-frequency one-sign coefficient sequence (or its negative), their actual delayed **linearized** fluxes differ.

## Proof

Choose \(N\) so that \(\|\rho_n\|\le\|a\|/(2q_n)\) for every \(n\ge N\); this is possible by the limit. With \(f=a/\|a\|\), \(\|f\|=1\), Cauchy–Schwarz gives
\[\langle\mathcal T\phi_n,f\rangle=\|a\|/q_n+\langle\rho_n,f\rangle\ge\|a\|/(2q_n).\]
For finite partial sums with \(h_n\ge0\), multiply by \(h_n\) and sum. For general \(\ell^2\) coefficients, \(\sum |h_n|/q_n<\infty\) by Cauchy–Schwarz and \(\sum q_n^{-2}<\infty\); boundedness of \(\mathcal T\) gives convergence of the outputs in \(L^2(J)\). Passing to the limit proves (1). The negative-coefficient case follows by linearity. □

## Adversarial qualifications

The proof controls the **whole infinite positive series**, not just nonvanishing of individual columns. It says nothing about cancellation for mixed-sign coefficient sequences. A pair of distinct points in the positive cone need not have a positive-cone difference, so (1) does **not** imply injectivity on that cone for arbitrary pairs, or on its linear span. The lower bound is a weak weighted \(\ell^1\) functional, not \(\|h\|_2\); for \(h=\phi_n\) it tends to zero, consistent with compactness. The fixed control \(f\) depends on the actual base and \(N\) is not numerically determined. The result is not a nonlinear theorem, does not resolve physical past admissibility, and has no established novelty.
