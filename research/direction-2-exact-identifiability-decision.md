# Exact initial-memory identifiability: decision

## Selected decision

**RESTRICTED-CLASS IDENTIFIABILITY PROVED**

This verdict is deliberately narrow. Under the explicit, nonempty strengthened small-load regime (1) of `direction-2-boundary-unique-continuation-and-moment-problem.md`, for each sufficiently high but fixed odd sine mode \(\phi_n\), its unknown scalar amplitude is uniquely determined by the actual delayed linearized flux-difference signal. The continuous-time two-endpoint and full linearized vectors also identify that amplitude. A separate scalar inverse-function argument gives local injectivity of the actual nonlinear full observation **on that same fixed one-dimensional line**. The required high-mode cutoff depends on the actual base and is not numerically specified.

**The central all-input question remains open:** no proof that \(\ker(\mathcal T:L^2_o\to L^2(J))=\{0\}\), no proof even for every odd \(H^2\) input, and no actual nonzero invisible initial memory have been obtained. The one-mode result is not a solution for unknown mode number, an arbitrary finite-sine combination, or an infinite-dimensional prior. The exact adjoint and reachable-state reductions are rigorous but do not themselves prove density. No priority or novelty claim follows.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder. This is Arena's analysis, not independent human certification. The frozen constitutive equations, sine-squared nonzero load, actual active base, fixed delay and observation geometry remain unchanged. Direction 1 is not revived.

## Claim–evidence table

| Question | Evidence | Conclusion |
|---|---|---|
| Exact delayed flux-difference injectivity, arbitrary odd \(L^2\) or \(H^2\) memory | Actual adjoint identity \(\mathcal T^*f=\Pi_ow_f(0)\), with \((z_f,w_f)\) defined by transposition on the whole interval; exact reachable-graph factorization. | **Open.** Neither adjoint density nor a nonzero physical kernel vector is proved. \(H^2\)-restricted injectivity is weaker than full \(L^2\) injectivity. |
| Labeled two-endpoint flux vector, odd linearized input | Odd \(Y\) implies \(Y_x(L,t)=Y_x(0,t)\); outward powers are opposite and difference equals twice one. | **Same kernel as \(\mathcal T\)** on the odd linearized space; no added independent channel there. Not a statement for general even-plus-odd inputs. |
| Full force-plus-two-flux linearized vector, odd input | The first variation of reaction force is zero for odd input and the fluxes are opposite. | **Same kernel as \(\mathcal T\)** on this odd linearized space; all-input full-vector injectivity remains open. |
| Density of actual adjoint initial-memory range | \(\ker\mathcal T=(\operatorname{ran}\mathcal T^*)^\perp\). The admissible family is exactly \(\{\Pi_ow_f(0): f\in L^2(J)\}\). | Equivalent to odd \(L^2\) injectivity, **not established**. No arbitrary smooth adjoint states substituted. |
| Exact prior-restricted recovery | Explicit \(S\) sign bound throughout the cylinder, actual high-frequency leading term, and (5) in the companion report. | **Proved** on each individual prescribed high-mode line \(\mathbb R\phi_n\), \(n\ge N_*\). The mode and sign/load assumptions must be known; \(N_*\) is existential and base dependent. |
| Approximate invisibility and instability | Existing neighbor-mode cancellation and singular-value upper bounds. | Established under the inherited hypotheses; **not** exact nonuniqueness, a finite-dimensional rank proof, or a physical kernel construction. |
| Full nonlinear local injectivity | \(C^2\) full-output map plus nonzero scalar derivative on each prescribed high-mode line. | **Proved only on a small segment of that line.** Full nonlinear open-neighborhood injectivity is unresolved; linearized behavior alone does not settle it. |
| Physical exact invisible state | Explicit Volterra and infinite synthesis equations were examined; no nonzero admissible solution with zero trace for all \(t\in J\) constructed. | **Not constructed.** No claim that the observation geometry is insufficient. |

## Why the sign and the restricted theorem are genuine, but limited

The actual fixed-point estimates give \(\|y_b\|_\infty\le 2KC_Bq\), \(\|w_b\|_\infty\le(W_s+2C_BW_R)q\), with \(q=|g_*|/L\). The explicit additional inequality in the companion report makes
\[
\operatorname{sgn}(b)S\ge\tfrac12\lambda\alpha|br|\theta_*>0
\]
on the **entire** space-time cylinder. Thus the leading time profile of the actual high-mode response is nonzero on \(J\). The proved little-o remainder then guarantees each sufficiently high individual \(k_n\) is nonzero, and linearity recovers its scalar coefficient exactly. This is not an appeal to positivity of a coupled maximum principle, and nonzero generators do not imply injectivity on their span. Neither a physical parameter set nor an experimental validation of the smallness inequality was provided.

For the nonlinear line result, evaluate the full observation along \(c\phi_n\) and pair its flux difference with the fixed actual \(k_n\). The resulting real scalar function is \(C^1\) with strictly positive derivative at \(c=0\), so it is strictly monotone on some smaller interval. The size of this interval is not quantified and does not extend to a neighborhood containing arbitrary directions.

## The single most important next mathematical step

Prove or refute the following **reachable-graph boundary uniqueness statement** for the exact active \(M,B,S\), signs and solution class:

> If an odd solution of the coupled PDE–ODE is generated from \((Y(0),P(0))=(0,h)\), \(h\in L^2_o(I)\), with the full pre-delay history, and \(Y_x(0,t)=0\) for a.e. \(t\in(\delta,T)\), then \(h=0\).

This is equivalent to the central question, but the proof must attack a specified mechanism: construct approximate controls \(f_{n,j}\) whose actual transposition states \(\Pi_ow_{f_{n,j}}(0)\) converge to each odd sine, **or** prove both the delayed reachable-state intersection and pre-delay injectivity in adjoint report (11). A useful boundary Carleman theorem would need to absorb the nondiffusive memory component without assuming away its unknown \(P(\delta)\); any remaining time-slice term must be controlled using the actual pre-delay graph. Alternatively, an explicit nonzero \(h\) solving the infinite synthesis relation would refute the statement. No chosen route is guaranteed to succeed, and a scalar homogeneous heat UC theorem does not suffice.

## Verification and source limitations

The forward estimate, weak/strong trace properties, explicit nonlinear-base threshold and little-o response bound are inherited from the named committed reports and were algebraically rechecked; the new adjoint report reconstructs the genuine weak transposition proof and identifies its boundary normalization. The companion report includes focused primary sources and distinguishes accessible proof passages from abstract-only material. The literature search is not exhaustive. No source inspected was shown to settle this exact nonautonomous reachable-graph question.

No implementation was changed, so no tests were required or run for this assignment. No physical parameters, base arrays, artificial forcing or numerical rank conclusions were introduced as evidence about the experiment. The three reports are the only intended repository changes.
