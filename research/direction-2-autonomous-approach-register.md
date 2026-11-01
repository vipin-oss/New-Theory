# Autonomous approach register

Starting state: branch `arena/5b089bbe-new-theory`, clean at `207a07715ec9e35cc0a848e38284b7a3ddcf3d8b`; remote matched. The complete previous commit three-file diff was inspected in two consecutive chunks. Fifty existing Direction 2 reports were inventoried; the active-base, critical-asymptotics, adjoint, positivity, kernel and novelty dependencies were inspected in detail. Inventorying summaries is not a claim of line-by-line independent re-verification of all fifty reports. Earlier files remain unchanged. This is Arena's work, not independent human certification.

## Live findings

### A. Endpoint-preserving approximation
- Objective: test the suspected \(S(t,0)-f(t,0)\) error.
- Method/assumptions: auxiliary source with actual feedback fixed, \(f,S\in\mathcal A\); subtract the leading term belonging to each source before comparing.
- Attempt and result: **PROVED** algebraically; the endpoint difference exists in the raw flux, but cancels exactly in the remainder difference. See `direction-2-autonomous-endpoint-and-finite-prior-proof.md` §1. The prior error estimate is not refuted by that objection.
- Separate failure: an everywhere smooth \(f\) matching an arbitrary \(\mathcal A\) endpoint for all time need not exist; an explicit even \(H^1_tL^2_x\cap L^2_tH^2_x\) source with a nonsmooth temporal endpoint is given there. This abstract example is not an actual base.
- Literature overlap: approximation/corrector machinery is standard; the earlier targeted comparison is in the primary-literature audit.
- Verification: independent algebra and regularity check in proof file §1. Next: B, simultaneous frequency control.

### B. Direct source-variable square function
- Objective: \(\sum q_n^2\|\rho_n\|^2<\infty\) for the actual base.
- Attempt: combine weak \(H^{-1}\) and strong \(L^2\) column estimates, retain cutoff history, and sum dyadic blocks. The modewise trace bound only gives a harmonic series; no valid orthogonality of boundary traces or time-dependent multiplication was found.
- Required missing theorem: a genuinely vector-valued estimate for the nonautonomous boundary trace after rank-one subtraction. \(M,B,S\) have the inherited rough regularity; the nondiffusive initial memory is not smoothed by positive time alone.
- Status: **UNRESOLVED** for actual coefficients; no counterexample. Verification: the abstract diagonal example shows why modewise little-o does not suffice, not a physical failure. Next: C.

### C. Operator ideals / Volkov
- Objective: recover endpoint singular-value decay without \(H^1\) source regularity.
- Attempt: apply source fractional factorization to each \(s<1\), and compare Volkov Theorem 1.1 and Delgado–Ruzhansky Theorem 2.2(iii), primary proof passages.
- Result: **SUBSUMED BY EXISTING LITERATURE** for the fractional operator-ideal component; it yields a weaker exponent than the inherited critical little-o. Volkov requires the still-unproved source \(H^1\) condition. No finite-\(s\) limit yields endpoint with uniform constants.
- Verification: `direction-2-volkov-theorem-hypothesis-mapping.md`; primary locations in the new literature audit. Next: D, exact identifiability.

### D. Actual transposition-adjoint density
- Objective: \(\overline{\operatorname{ran}\mathcal T^*}=H_o\).
- Attempt: derive \(\mathcal T^*f=\Pi_o\int_0^T e^{-\mu t}S(t)z_f(t)dt\) with boundary data supported on \(J\), and factor through the actual delayed reachable graph. Existing duality is exact; no construction of controls approximating every odd sine was obtained.
- Status: **UNRESOLVED**; a scalar UC theorem cannot discard the unknown coupled source or pre-delay graph. No unsupported analyticity imported. Next: E.

### E. Volterra elimination and resolvent
- Objective: infer initial memory from delayed boundary trace.
- Attempt: use \(MY_t-\kappa Y_{xx}-BY-\gamma S(t)\int_0^t e^{-\mu(t-s)}Y(s)ds=S(t)e^{-\mu t}h\). The forward Volterra problem is causal, but inversion in time is not inversion of its boundary trace; \(S,M,B\) are nonautonomous.
- Status: **PARTIALLY PROVED** as an exact reduction, not as injectivity. Next: F.

### F. Boundary jets
- Objective: turn zero trace and flux into interior vanishing and memory vanishing.
- Attempt: source term \(SP\) prevents homogeneous scalar boundary UC; \(Y_t,Y_{xx}\) are only known in interior \(L^2\), with no justified boundary traces, and no \(S_{xx}(0,t)\) or \(M_t(0,t)\) trace follows.
- Status: **FAILED** under the actual regularity; no classical corner conditions imposed. Next: G.

### G. Exact invisible state
- Objective: construct nonzero actual odd \(H^2\) input with zero whole \(J\)-trace.
- Attempt: look for invariant sines, a reachability-loss vector, and an infinite synthesis relation. Active variable coefficients couple sine modes; compact Fredholm memory does not itself produce a kernel; approximate null vectors need not converge strongly.
- Status: **UNRESOLVED**, no physical counterexample. Next: H, finite-dimensional subspaces.

### H. Fixed finite odd-sine prior, actual nonzero load
- Objective: identify **all combinations** in any fixed finite set of odd sine modes, not just individual modes.
- Method: calculate a constant-coefficient reference response solely as a mathematical comparison; prove its finite Gram positive by distinct real exponential rates; estimate the true active coefficients and all evolution differences uniformly in the real nonzero load; choose an explicit positive sufficient load threshold. No physical experiment is replaced by equilibrium and no coupling is set to zero.
- Status: **PROVISIONAL CONDITIONAL PROOF**, subject to further audit and the proof and adversarial check in `direction-2-autonomous-endpoint-and-finite-prior-proof.md` §§2–4. This gives a concrete finite-dimensional linearized identifiability/stability theorem for the active system. It says nothing uniform as the number of modes grows and nothing about arbitrary odd states.
- Prior art: finite-dimensional perturbation/Gram principles and separated-source uniqueness are established; exact PDE/observation mapping and access limits are recorded in `autonomous-primary-literature-audit.md`. This is a model-specific conditional application, not a demonstrated new continuum theory or proven chronological novelty.
- Next triggered by limited scope: test nonlinear restricted map and global-infinite question; test whether a finite-dimensional projection inverse argument yields a local nonlinear result on the same fixed subspace, with a potentially smaller neighborhood. General all-input exact identification remains open.

## Restart point — programme not complete

The above restricted-prior proof is promising but its standard mechanism and finite-dimensional scope do not yet justify classifying it as the requested strong breakthrough. The nonlinear multi-mode extension, broader primary-literature overlap check, and full re-reading of all fifty previous reports are unfinished. The alternative-candidate escalation has **not** been carried out; no five-candidate comparison or selection is claimed. No final breakthrough report has been created.

Next deterministic actions: (1) independently re-check every constant in (1)–(4) of the finite-prior proof against the cited base fixed-point bounds, and verify the exact prior \(C^2\) differentiability theorem; (2) derive or refute a local nonlinear injectivity theorem on \(V_N\) using a finite-dimensional inverse function theorem with the actual observation projection, identifying the neighborhood and preserving physical admissibility; (3) inspect primary full texts specifically for finite-mode parabolic–ODE initial-memory boundary identification and perturbation arguments; (4) if this still fails the strong-result/novelty gate, investigate at least five materially distinct continuum/memory candidates with complete equation/objective/literature/feasibility comparisons and pursue the strongest rather than treating a candidate list as a result; (5) resume B–G whenever new insight changes their stopping points. Only after the specified completion condition is met should the final report be written.

Execution checkpoint: the parent commit is `207a07715ec9e35cc0a848e38284b7a3ddcf3d8b`; the commit containing this checkpoint is identified by `git log -1 --format=%H` when resuming. The current work is an incomplete research programme, not a final decision or independent certification.
