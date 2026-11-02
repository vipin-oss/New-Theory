# Reproducibility and results — phases 3 and 4

## Phase 3: analytical and numerical results
MANUSCRIPT.md contains the conditional classical uniqueness proof, global energy identity, dispersion polynomial, simple-root speed formulas, and explicit propagation caveats. All numerical coefficients here are **dimensionless and manufactured**, not estimates for an actual material. L=2π, ρ=2, C=3, β=0.4, T0=1.5, c=2.2, κ=0.3, h=0.7, kr=0.8, τ=0.6, ℓ=0.4, η=0.35. In dimensionless variables these are numerical values; mapping to SI requires an explicit nondimensionalization. The convergence example initializes θ(x,0)=2∑_{n≥1}exp(−n)cos(nx), all other state fields zero. It evaluates t=0.5 on 513 periodic sample points. The N=32 result is an internal reference, not exact truth. Observed max sampled |θ_N−θ_32|:

| N | Error |
|---:|---:|
| 4 | 5.326835816926e-03 |
| 8 | 5.901497669436e-06 |
| 16 | 1.336277200004e-09 |
| 24 | 7.260858581049e-14 |

A separate k=1 mode with unit initial temperature has energy 0.733333333333 at t=0 and 0.614994410297 at t=0.5 in the complex-mode normalization in model.py. This is illustration, not a stability proof or calibrated prediction. Matrix exponential roundoff and finite sampled points limit accuracy; no independent algorithm or mesh is used.

**DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; novelty remains to be established.

## Phase 4: tests and published-benchmark status
On 2026-11-02 the following were run in this workspace: Python 3.11.2, NumPy 2.4.6, SciPy 1.17.1, SymPy 1.14.0. The last unittest run passed **6 tests in 0.690 s** (test runner time). It checked a symbolic 5×5 determinant, symbolic constitutive elimination and selected factor limits; the Fourier energy matrix identity at k=1,2.5,9 to absolute and relative 2e−13; energy monotonicity for selected states; and analytic Fourier, GN II, Cattaneo and Helmholtz-elastic mode solutions to 1e−12 absolute and relative tolerance. The convergence example was also run; its output is above. These checks do not verify original-source normalization, all parameter ranges, a discretized boundary problem, or independently prove the analysis. Algebraic degenerate-mode factors must be filtered.

**Required published numerical benchmark: NOT DONE.** No published GN, GL, LS or Eringen numerical table, graph, boundary-value setup, parameter set and numerical tolerance has been reproduced. The analytical limiting checks above must not be represented as such reproduction. Next: obtain a full accessible original or later published benchmark, transcribe geometry, loading, units, material values and initial/boundary data, implement independently, and quantify error against the published data. A general GL implementation is absent, so its benchmark is also unavailable.

**DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; no verified novelty or published benchmark replication yet.
