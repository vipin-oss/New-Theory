# Adversarial reconstruction

Same-agent reconstruction is not independent scientific certification.

| Claim | Required assumptions | Location | Audit status | Remaining gap |
|---|---|---|---|---|
| Nonlinear mass inverse | bounded positive temperature | 02 (1) | PASS | Does not prove solution existence |
| Odd flat no-gap obstruction | smooth initial-compatible flat input, linear odd system, nonzero couplings | 05 | PASS | Human review and literature priority search |
| Exact finite sine exclusion | same control class, zero initial state | 05 | PASS | Not nonlinear; nonflat class unaddressed |
| Gap \(L^2\) density | reference signed synthesis and bounded gap map | Cycle 6/10 | CONDITIONAL | Relies on previous same-agent proof |
| Full odd/even nonlinear preparation | positivity, exact terminal field, strong well-posedness | 07–09 | INCOMPLETE | Controlled existence and endpoint feasibility |
| No-gap nonflat impossibility | all moment constraints | 05 | INCOMPLETE | Endpoint-jet compatibility does not determine global transform |
| Physical inverse transfer | prepared \(H^2\) family, full tail derivative | 10 | INCOMPLETE | Physical family not known |

Adversarial alternatives: a bump nonzero arbitrarily near 0 shows flatness alone does not force zero; the proof needs all moments. A nonflat control \(f(t)=t\chi(t)\) produces a finite nonzero limiting fast contribution, so the flat proof cannot be extended by deleting a hypothesis. Even controls cannot cancel odd first variation but may affect even memory or nonlinear cross terms. Finite truncations produce tiny residuals in double precision and are not counterexamples to an infinite moment theorem. No exact nonzero no-gap counterexample, nonlinear branch, or bounded-control counterexample was found. Numerical rank deficiency was observed but cannot be isolated from conditioning and discretization. No independent high-precision numerical or human proof review was completed.

The one-sign no-gap theorem was checked separately: both branch weights \(\delta_1,b_1\) are strictly positive and the first temperature kernel is strictly positive, so an attempted nonnegative no-gap control cannot even cancel its first mode. This does not use maximum principles for the coupled PDE and does not extend to sign-changing controls, nonlinear mode mixing, or physical measures. Negative coupling \(b\) does not alter the conclusion because \(S\gamma>0\) still holds.

Joint density reconstruction: the \(\eta\)-fast coefficients grow like \(q_n\), so the adjoint series is not uniformly summable at \(t=0\); the proof uses local uniform convergence only on positive times, and an extra \(q_n^{-2}\) from Laplace integration for absolute convergence. Slow poles accumulate but every individual pole is isolated and has a residue; both branches are needed to force both adjoint components to zero. The proof relies on the fixed positive control gap for bounded endpoint maps, and no exact or nonlinear range claim is made. The argument should receive independent expert review.
