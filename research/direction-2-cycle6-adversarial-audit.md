# Cycle 6 adversarial audit and decision

**Actual graph-linked injectivity: OPEN. Research direction: REFORMULATE.** Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is Scientific Supervisor and Auditor; this is Arena's mathematical investigation, not independent human certification.

| Challenge | Disposition |
|---|---|
| Infinite signed cancellation | Constant reference injectivity was rederived for every \(\ell^2\) signed sequence using absolute/local uniform convergence, holomorphy, Laplace transform, a connected continuation domain and residues. This result was already present in `direction-2-infinite-mode-reference-and-perturbation-barrier.md`; it is not new evidence for the actual system. |
| Spectral accumulation | Slow roots converge to \(-\mu\); standard ordered-to-infinity Dirichlet-series arguments cannot be applied wholesale. The accumulation is excluded from the reference continuation domain and does not coalesce its isolated fast poles. |
| Polynomial observability | Under the conditional actual endpoint, factorization through \(O\) excludes all negative Sobolev estimates for \(s\le3/2\). For the reference a direct Taylor/fast-tail rank construction excludes every finite \(s\). Neither shows actual noninjectivity; \(s>3/2\) is not decided for the actual system. |
| Time and coefficients | The actual base is nonautonomous, with proven finite Sobolev—not analytic—regularity. The comparison resolvent has no justified actual analogue. Small-norm perturbations alone cannot preserve compact-operator injectivity. |
| Boundary and graph | The weighted identity records all spatial and temporal boundary terms; \(P\) has no assumed boundary trace. The graph term and the distributed source \(B_tY+S_tP\) remain uncontrolled. The exhibited weight is a test identity, not a completed Carleman estimate. |
| Full memory | \(P(t)=e^{-\mu(t-\delta)}p+\gamma\int_\delta^t e^{-\mu(t-r)}Y(r)dr\); the first term is not eliminated by Volterra smallness. \(p=D_\delta h\), \(Y(\delta)=Gp\). |
| Adjoint | The exact Tikhonov limit is the norm of the unknown kernel projection; even dense reference adjoint range supplies no uniform transfer because control costs can diverge. Exact factorization into injective maps is only a conditional sufficient hypothesis, not established for the actual coefficients. |
| Counterexample | None found. Reference behavior, abstract rank-one perturbations and finite-mode near-null vectors cannot serve as an active physical invisible trajectory. |
| Input and nonlinear classes | \(H_o\), \(H^2\cap H_o\), and fully coupled pasts are distinct; linear injectivity would not prove nonlinear uniqueness. |
| Scientific claim | An inverse theorem for the frozen constitutive equations is not a foundational continuum theory. Prior internal-variable and hereditary thermoviscoelastic structure exists; no new physical principle or experimentally distinguishable prediction has been demonstrated. |

**Most important missing step:** establish a coefficient- and graph-specific qualitative mechanism eliminating \(p\) from zero flux, despite the retained initial memory and distributed feedback, or construct and verify an actual nonzero invisible trajectory. A negative-Sobolev inequality is not required and is likely too strong for comparison with the reference. No fixed change to the experiment is proposed.

## Diagnostic record

All nine discovered test files passed using `/tmp/cycle4-env/bin/python` with bytecode disabled: **32 tests**, including three new abstract/comparison checks of the two root branches, Taylor remainder bound and a discretized sign check for the weighted heat identity. The first attempt at the new check encountered a NumPy API incompatibility (`trapz`); it was corrected to `trapezoid`, and the complete suite was rerun successfully. These tests are diagnostics, not proofs or physical simulations. `git diff --check` passed. Starting local and remote heads were both `a69426d6f9d3819b87fc8320cecb807c51a38bf7`.
