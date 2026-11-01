# Adversarial proof audit (same-agent, not independent human review)

| Obligation | Verification | Status |
|---|---|---|
| Boundary term and normalization | Both odd endpoint terms have same sign; \(C_n=2\kappa c_Lq_n/M\) | PASS |
| Root ordering and product | Characteristic polynomial at \(-\mu\) negative and physical product positive; \(\delta b=d>0\) | PASS |
| Time reversal | \(t=-s\), zero initial state gives \(e^{tD}\), \(F(z)=\int e^{zt}f(t)dt\) | PASS |
| Watson expansion | Split near 0, Taylor with remainder; far part is exponentially small | PASS |
| Analytic jet identity | The difference of finite Taylor polynomials is \(O(w^N)\) along infinitely many \(w=\delta_n\to0\); any first nonzero coefficient contradicts this. Variable change is analytic near 0. | PASS |
| Radius and bound | J has only possible singularity at \(1/\mu\); use any smaller circle, not a bound at the boundary | PASS |
| Analytic uniqueness extension | Entire jet g equals f on the **whole** interval only by real-analytic identity. No such equality is valid for smooth f | PASS |
| Tail contradiction | For nonzero entire g the first nonzero derivative at T exists; global exponential bound controls distant tail. Real or complex sign cannot cancel the leading term for all large x | PASS |
| Memory exclusion | Both moment equations for infinitely many n give infinitely many zeros of the same entire F at distinct accumulating slow roots | PASS |
| Power-law memory tail | \(p_n=C_n\gamma F_+/b_n\), first jet j gives \(F_+\sim-f^{(j)}\delta^{j-1}/d^j\); use \(b\sim\kappa q^2/M\) | PASS |
| Cost obstruction | Memory operator is Hilbert–Schmidt on no-gap \(L^2\); test each temperature mode by weak convergence. Gap density is an inherited dependency, not re-proved here | CONDITIONAL for density; PASS for bounded-norm obstruction |
| Actual system and physics | Linear odd realization only; nonlinear and even physical preparation are not covered | INCOMPLETE |

Attempted counterexamples: nonflat sine-basis controls satisfy finitely many equations with tiny residual; 60-digit validation detects nonzero withheld modes, and higher truncations are ill-conditioned. A smooth flat basis also fits a finite system but is ruled out as an exact solution by the prior flat theorem. A polynomial analytic candidate cannot satisfy the complete equations by the analytic theorem. None disproves the smooth nonanalytic possibility. The proof has not been checked by an independent expert; source-priority checks remain incomplete.

## Jet-sufficiency counterexample audit

The construction in §10 uses the weighted space \(L^2(s\,ds)\): H is symmetric and its power series is positive definite, giving a nonnegative compact self-adjoint operator, so \(I+\mathsf T\) has a bounded inverse. The Borel/Laplace identity follows from \(\int_0^\infty e^{-xt}e^{\mu t}t^{k+1}dt=(k+1)!/(x-\mu)^{k+2}\). Nonzero h cannot map to zero f, the two endpoint/integral constraints leave an infinite-dimensional kernel, and vanishing of all moments against polynomials implies v=0 in the weighted space. This proves only sufficiency failure for the jet hierarchy: no claim is made that the constructed inputs solve the exact discrete moments. This was reconstructed by the same agent, not an independent reviewer.

A dimensional coefficient cross-check corrected the tail constant before delivery: \(F_+\sim-f^{(j)}\delta^{j-1}/d^j\) and \(\delta\sim dM/(\kappa q^2)\) cancel \(d^{j-1}\), giving the factor \((M/\kappa)^{j-1}/d\), not \((dM/\kappa)^{j-1}/d\). The power of q is unchanged. This illustrates why the tail is not inferred from numerical data.
