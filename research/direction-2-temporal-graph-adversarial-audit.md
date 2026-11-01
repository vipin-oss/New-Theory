# Adversarial audit: temporal bootstrap, endpoint, graph

Arena's self-audit only, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Auditor; Arena is Research Scholar / Builder.

| Challenge | Disposition |
|---|---|
| Mass and mean | \(\partial_t(\theta Qy_t)=y_tQy_t+\theta Qy_{tt}\), not a local scalar mass. The proof uses difference quotients, and a separate small-load condition makes the nonsymmetric unweighted mass coercive; positivity of \(\theta\) alone is not substituted for that bound. |
| Startup | The prescribed \(m(0)=m'(0)=0\), zero base memory and data imply \(X(t)=O(t^3)\) by a strong-solution energy; hence quotient initial \(H^1\) norms are \(O(h^{1/2})\). This is an \(L^2\)/Sobolev statement, not an asserted corner-classical \(y_{tt}\). |
| Second quotient | The product \(z_h Qy_t\) is bounded in \(L^2\) only *after* the first quotient step gives \(y_t\in L^\infty L^2\) globally; then \(z_h\in L^2H^1\) and 1D embedding close it. The second test is performed on fixed increments before passage. |
| Threshold and units | Require \(q<\min\{s_*/2,c/(4d\sqrt L C_B)\}\), with constants in fixed consistent units or recomputed dimensionless variables. Graph isomorphism and \(S\)-nonvanishing require their own further thresholds. None has been checked on physical parameter values. |
| Approximation cost | \(H^3(Q)\) is isotropic; the bound includes \(f_{ttt},f_{ttx},f_{txx},f_{xxx}\). The new \(S_{tt}\in L^2\) controls the first, and \(S\in H^{1/2}_tH^2_x\) controls the third. One fixed feedback is retained. The resulting block sequence is summable. |
| Early history | The restart identity separates actual early heat, accumulated early memory and the persistent bare memory. The first two have \(O(2^{-j})\) weighted blocks; the last has the late direct source plus its actual feedback. Both cutoff forcing terms are included. No memory is erased. |
| Positive-time boundary | Conditional coefficient gains allow a quotient proof of \(Y_x(0,\cdot)\in H^1(a,T)\); derivative of zero flux is justified. \(P,F\) need not possess spatial traces for arbitrary \(h\in L^2\), so no equation is evaluated at the boundary. |
| Division by \(S\) | Performed only under the additional \(q<|S_0|/(2D_S)\) bound. The differentiated residual is an equality for \(F=SP\); no unsupported separate \(B_tY_t\) or \(Y_{xxt}\) trace is introduced. |
| Mixed signs and compactness | Endpoint kernel regularity does not rule out mixed-sign cancellation; an approximate null vector is not an exact physical kernel. The reference operator's density does not transfer by small norm without controlling diverging control norms. |
| Dense versus exact range | Tikhonov's limit equals projection onto \(\ker O\), not automatically zero. Density, exact adjoint range, and stability are distinct. |
| Actual past and nonlinear map | \(H_o\), \(H^2\) and coupled-past states are different. No complete physical counterexample or nonlinear uniqueness theorem is claimed; compactness obstructs a Lipschitz inverse but does not prove noninjectivity. |
| Prior sources | The fixed-point/forced-solution/corrector estimates remain explicitly inherited; several primary literature theorems concern different equations, geometry or data. No independent human audit or novelty certification. |

## Classifications

| Question | Decision |
|---|---|
| Active-base temporal bootstrap | **CONDITIONALLY PROVED**, with the additional symbolic coercivity load bound and inherited base theory. |
| Endpoint square function | **CONDITIONALLY PROVED**, with the same extra bound and inherited fixed-feedback corrector; open for the previously broader regime. |
| Graph-linked unique continuation | **OPEN**, even under the extra thresholds. |
| Graph adjoint density | **OPEN**. |
| Physical past admissibility | **OPEN**. |
| Nonlinear infinite-dimensional uniqueness | **OPEN**. |

The first unclosed graph estimate is control of the unknown interior \(S_tP+B_tY\) and graph-linked \(S(\delta)p\) by the single boundary Cauchy data. Next investigate a source-specific coupled Carleman/Volterra estimate in the upgraded spaces, or an actual complete invisible trajectory. Separately seek the endpoint without the extra unweighted mass-coercivity bound. No demonstrated novel foundational theory follows.

## Diagnostic record

Using `/tmp/cycle4-env/bin/python`, all seven test files passed: four new finite-dimensional checks (nonlocal quotient, nonsymmetric mass coercivity lower bound, Tikhonov projection, dyadic exponent bookkeeping), three next-cycle checks, three graph/square-function checks, two cycle-4 checks, five moment checks, six manufactured-solver checks, and three critical-asymptotics checks: **26 tests total**. These are algebraic or manufactured diagnostics, not a proof of the PDE estimates, a physical simulation or experimental parameter validation. `git diff --check` also passed.
