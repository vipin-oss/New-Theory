# Cycle 5 adversarial audit and decisions

This is an Arena mathematical re-derivation, not independent human certification. The Principal Researcher and final decision-maker is Dr. Vipin Gupta; the designated Scientific Supervisor and Auditor is ChatGPT. No novelty or foundational-theory conclusion is made.

| Attack | Finding |
|---|---|
| Nonsymmetric nonlocal mass | The quadratic estimate retains the mean projection and is valid, but only the additional small-load bound gives the uniform coercivity used in the second test. Positive \(\theta\) alone is not substituted. |
| Time-zero quotient | Strong heat energy plus the actual smooth \(\sin^2\) load yields \(X=O(t^3)\); the proof starts Gronwall at zero. No classical initial \(y_t\) or higher corner compatibility is assumed. |
| Product and chain rules | Fixed increments have strong regularity; the weighted quotient test, shift products and \(h\)-uniform integrability are explicitly checked. The second test uses the *first* result \(y_t\in L^\infty L^2\), avoiding circularity. |
| Coefficient transfer | Memory convolution gives \(p\in C H^2\) first, then \(p_t\in L^\infty H^1\); elliptic recovery gives \(y\in L^2H^3\), then \(p\in H^1H^3\). All \(Q\)'s remain. |
| Approximation | The isotropic cost includes every order-three derivative; fixed simultaneous extension, parity averaging, and time smoothing yield an explicit summable dyadic rate. No spatial endpoint derivative is assumed for the original \(S\). |
| Corrector constants | Full weak \(V'\) energy and trial mismatch are reconstructed; smooth endpoint traces and \(B H_f\) are controlled by isotropic \(H^3\). \(C\) depends on actual coefficients, fixed delay and forcing estimates, not on \(n,j,f_j\). Both cutoff commutators and full feedback are kept. |
| Startup and restart | Early \(A\phi_n,K\phi_n\) estimates and the coupled heat-to-flux cutoff use the entire actual history. Bare memory is \(e^{-\mu t}\phi_n\) after restart, not a smoothed surrogate. |
| Unit normalization | Common-coupling nondimensionalization is fixed in the combined-threshold report. The previous linear audit's differently normalized \(C_D\) must be recomputed/converted, not copied. This is a clarification of the combined use, not a numerical physical bound. |
| Claims | Bootstrap and endpoint survive **conditionally** on the actual strong-solution and forcing framework. They are not claimed for larger loads; graph UC, adjoint density, physical past and nonlinear uniqueness remain **OPEN**. |
| Literature | Primary passages checked: Volkov Thm 1.1 (kernel \(H^1\) implies weighted singular sum); Meyries–Schnaubelt Prop. 3.2 context (mixed derivatives under its operator assumptions); arXiv:2609.09982 Thm 1.1 (autonomous semigroup, compact resolvent, complete roots and relatively bounded observation); arXiv:2610.26157 eqs. (13)–(14) and Thm 2.3 (interior observation and a retained ODE time slice); arXiv:2506.22221 Assumptions 3.1/3.3 (moving interior geometry, delay-compatible weight and short-time remainder). None supplies this graph's one-endpoint UC. |

## Strongest result and missing step

Under the explicit nondimensional strict interval and inherited forward well-posedness/trace estimates, the actual base bootstrap and actual endpoint square-function estimate are conditionally proved; the latter yields the conditional weighted singular-value sum. No theorem was downgraded in this re-derivation; the unit-convention clarification above is required for combining previously differently normalized constants. No actual materials or amplitudes were supplied, so experimental applicability remains unverified. Standard difference quotients, interpolation and Tikhonov regularization are not claimed novel.

The most important missing step is a graph-specific qualitative boundary estimate eliminating the unknown distributed \(B_tY+S_tP\) and the graph-linked memory slice \(S(\delta)p\). A negative-norm inequality is one sufficient form, but no such inequality, physical counterexample or nonlinear injectivity proof is obtained. Direction 1 remains rejected as a foundational theory; Direction 2 remains **REFORMULATE**.

## Verification record

Eight test files ran with `/tmp/cycle4-env/bin/python` and bytecode writing disabled: **29 tests passed**, including three new algebra-only checks of the explicit oscillatory corrector cancellation, restart exponential and dyadic minimization. The other 26 are earlier algebra, moment, manufactured-solver and critical-asymptotic diagnostics. None is a physical run or certifies the PDE proofs. `git diff --check` passed. Starting local and remote branch head were both `754a4fb30292609a4c1d548469806576317d60e9`; the six deliverables were re-read before staging.
