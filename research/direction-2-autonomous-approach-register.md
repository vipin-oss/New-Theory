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

## Next cycle: verification, transfer, and prior-art gate

- **Finite-prior linear audit:** VERIFIED AS WRITTEN conditional on the cited actual-base and odd strong-solution results. All coefficient/Gram/energy/trace constants are recalculated in `direction-2-finite-prior-independent-proof-audit.md`; no independent human certification. The active load remains nonzero and the reference is only a comparison.
- **Finite-prior nonlinear transfer:** PROVED conditionally in `direction-2-finite-prior-nonlinear-identifiability.md` using the actual derivative range and a two-point \(C^2\) bound; \(\sigma_N/4\) local stability and an existential, \(N\)-dependent radius. No infinite-dimensional implication.
- **Adversarial review:** see `direction-2-finite-prior-adversarial-audit.md`. No fatal flaw found; \(H^2\) fixed-unit and inherited active-base assumptions are essential.
- **Literature gate:** Eller–Rieder Appendix C, Lemma C.1(a), provides the general finite-dimensional nonlinear Lipschitz transfer. The exact model-specific finite Gram calculation is not shown to be contained in that theorem, but it is a standard perturbation argument; no demonstrated publication-level novelty. The expanded primary comparisons are in `autonomous-primary-literature-audit.md`.
- **Next:** investigate and pursue distinct alternatives beyond finite-dimensional stability. Infinite-dimensional Direction 2 exact injectivity and actual endpoint square function remain unresolved.
- **Alternative escalation:** five distinct candidate problems and primary comparisons were screened in `autonomous-five-candidate-discovery-audit.md`. Candidate 1 was pursued: an exact invisible signed distributed-memory state is constructed for a different model, but is proved not reachable through a specified common finite-energy prehistory. Its physical applicability and novelty remain unproved. Candidates 2–5 are not at final stopping points; next pursue the gradient-interface partial-boundary Runge identity and literature overlap.

**Checkpoint remains incomplete:** no breakthrough or final report is claimed. Verify the alternative construction's singular-integral identity and exact history space independently, then work on candidate 2 and the other unresolved candidates; broaden the primary minimal-state literature search. Fixed parent for this cycle is `b1ec3395b01f1d9ef3d90f70ba0cbcf5612be568`; the present commit is obtained from `git log -1 --format=%H` after checkpointing.
- **Next distinct alternative actually pursued:** candidate 2 now has a variational partial-control interface-trace density lemma with proof in the discovery audit §8. It does not establish disjoint-observation shape uniqueness; its closeness to standard Runge theory must be checked before claiming novelty. More routes remain open.

**Exact restart sequence:** (1) verify the alternative Hilbert-transform construction and the reachability exclusion under the intended history topology; (2) inspect the full proof of the primary interface paper's Runge lemma and partial-data results, then investigate disjoint observation rather than treating interface density as shape uniqueness; (3) examine primary minimal-state/history-range theory and pursue candidates 3–5 with explicit proofs or counterexamples; (4) revisit the infinite-dimensional actual-system kernel problem. The complete original formulation-A dependency chain has not been independently re-audited line-by-line this cycle; its fixed-point and odd strong-solution assertions remain explicitly inherited. No final research stopping point is claimed.

## Cycle 4 partial checkpoint and exact restart

Started from `cb904502bea00fb10e280e4c117575023b29bff4`, verified local and remote branch HEAD and clean tree, and inspected the complete preceding commit diff. Candidate 1's principal value calculation is checked in `candidate-1-invisible-state-independent-proof-audit.md`; `candidate-1-physical-history-reachability-theorem.md` gives exact vector-Hardy range, dense nonclosed closure, a correction that the spatially tensored map is not compact, and exclusion of the entire separated ansatz under analytic conditions. A general reachable invisible state or general injectivity is not obtained. Candidate 2 density is rechecked in `candidate-2-interface-density-independent-audit.md`; `candidate-2-partial-data-shape-identifiability.md` proves a conditional partial-to-full DtN reduction by a different route, without inferring a shape derivative or novelty. No independent human certification is claimed.

Restart: (1) inspect and verify all of these new proofs, in particular endpoint logarithms, the vector Hardy normalization, the analytic divided difference, and the collar UCP/conormal trace; (2) derive the actual surface-energy shape derivative and kernel, and verify every hypothesis of the full-data theorem and at least three close primary papers per candidate; (3) pursue candidates 3–5 with explicit equations and theorems/obstructions and their literature; (4) return to the frozen actual nonautonomous Direction 2 adjoint range, reachable graph, and source-kernel endpoint square sum by materially distinct methods. The complete formulation/dependency chain and all designated reports have not been read in full in this cycle, so inherited conclusions remain conditional. This is not a systematic stopping point or completed research cycle.
