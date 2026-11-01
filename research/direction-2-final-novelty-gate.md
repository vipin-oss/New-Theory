# Direction 2 — final novelty gate

## Decision

**NOVELTY NOT ESTABLISHED**

The established small-load model theorem is mathematically meaningful and the companion report gives a fixed-finite-memory, nonsymmetric two-endpoint extension plus a conditional quantitative rate. Neither the extension nor its stronger regularity assumption presently establishes a genuinely differentiated theorem over the literature. The strongest nearby general singular-value theorem has an unverified kernel regularity hypothesis, and a directly relevant boundary-initial-data article has not been inspected beyond its abstract. This is not proof that prior work subsumes the result, nor proof that it does not. There is no genuinely promising *demonstrated* new theory on this evidence.

Retain the work as supporting mathematical analysis, diagnostic software and a scoped result for the frozen experiment. Do **not** proceed with a standalone novelty-driven paper on the present evidence; close that proposal unless new evidence below changes the gate. This is an assessment for Dr. Vipin Gupta, Principal Researcher and final decision-maker. ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This report is not an independent human certification. Direction 1 remains rejected as a new foundational continuum theory. This is not a manuscript or journal recommendation.

## Claim–evidence table

| Claim | Evidence and limits | Gate status |
|---|---|---|
| Actual nonlinear base exists | Positive weak-initial solution and full-class uniqueness are inherited from the formulation-A existence chain; explicit positive \(s_*\) and nonzero sine-squared regime are reproduced in the exact-overlap report. Its proof was rechecked at the level of the provided contraction and dependencies. | Supported in the stated mathematical regime; no experimental load or parameters were supplied. |
| Original odd derivative and delayed output | Actual even base gives \(M\ge c+3d\theta_*/4\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2\), \(S\in H^1_tL^2_x\cap L^2_tH^2_x\); the coupled ODE and nonautonomous mass are retained. | Supported under that regime; not a frozen-coefficient proxy. |
| Critical high-frequency columns | \(\mathcal T\phi_n=a/q_n+o(q_n^{-3/2})\) in \(L^2(J)\), with source approximation, full history and delayed cutoff. No nonzero leading coefficient is assumed. | Supported; a little-o upper bound, not a sharp asymptotic equivalence. |
| Singular values | \(s_n=o(n^{-3/2})\); Volkov's source-kernel Sobolev theorem is a strong possible generic explanation if its stronger hypothesis can be proved. An abstract counterexample shows column little-o alone does not imply that hypothesis. | Supported; exact literature subsumption unresolved. Not strong \(\mathcal S_{2/3}\). |
| Linear and nonlinear obstructions | The neighboring-mode cancellation excludes \(\xi\ge4/7\) for the linear full-state estimate. An explicit small-data nonlinear neighborhood and quadratic remainder yield the distinct \(\xi\ge11/14\) obstruction for force and two fluxes together. | Supported as upper-limit obstructions, not optimal rates; nonlinear \(4/7\) is not established. |
| Finite memory / sensor generalization | Companion report gives explicit \(N\)-branch energy and history estimates, corrected trial, endpoint vector, same-parity cancellation and aggregate bounds for uniform constants. | A derived fixed-\(N\) mathematical extension; likely generic mechanism, not evidence of independent novelty. No uniformity as \(N\to\infty\) without stated aggregate and approximation bounds. |
| Quantitative remainder | Companion report derives \(O(q^{-3/2-\eta/2})\) under additional isotropic \(H^{2+\eta}\) regularity, explicitly including higher time derivatives and controlled smoothing cost. | Conditional mathematical strengthening; actual base has not been shown to satisfy the stronger condition. Not a lower bound or sharpness claim. |
| Exact initial-memory identification | Exact reachable graph and adjoint-range / synthesis questions remain unresolved. Approximate invisibility and compactness do not determine injectivity. | Open; no physical exact kernel, all-input injectivity, adjoint density or minimal additional measurement proved. |
| Novelty | Inspected Volkov, Delgado–Ruzhansky, Li–Li–Zhou, PDE–ODE/memory and instability sources; Birman–Solomyak and Hào–Oanh boundary proof are not fully mapped. | Not established. Neither subsumption of the full package nor its absence is proved. |

## Independent numerical/forcing audit

The two software packages are diagnostic, not physical data. `code/direction-2-moment-analysis/manufactured.py` chooses artificial \(M=1\), \(B=0.3\), \(S=1+0.2\cos(2\pi x)\), dimensionless constants, and
\[
Y=e^{-t}[t\sin(2\pi x)+0.15t^2\sin(4\pi x)],\quad
P=e^{-t}[(1+t)\sin(2\pi x)+0.2\sin(4\pi x)].
\]
Direct differentiation gives the implemented \(Y_t,Y_{xx},P_t\) and \(F=Y_t-\kappa Y_{xx}-0.3Y-SP\), \(G=P_t+\mu P-\gamma Y\). Thus these fields exactly solve the **forced manufactured** system, with \(Y(0)=0\) and sine initial memory. The independently implemented centered-space, midpoint-Crank–Nicolson `finite_difference.py` evolves both components with the signs \(M^{-1}(\kappa\Delta+B)Y+M^{-1}SP\), \(\gamma Y-\mu P\), uses a second-order one-sided boundary derivative and interpolates the delayed trace. It requires initial memory to vanish at endpoints because it stores only interior values. That is a diagnostic restriction, **not** an original-model requirement for general \(H^2\) memory. A separate BDF spectral reference and grid/time refinement provide code cross-checks; their agreement is not an infinite-dimensional theorem. Fixed-grid time errors can be nonmonotone when spatial/time errors cancel, so temporal self-convergence is the relevant separate check.

`code/direction-2-critical-asymptotics/manufactured_high_frequency.py` uses artificial \(M=1,B=0,\kappa=1\), \(S=s(x)\), \(P=e^{-\mu t}\phi_n\), and
\[
Y=e^{-\mu t}(1-e^{-q_n^2t})(s\phi_n/q_n^2+\phi_n/q_n^3).
\]
The displayed implemented \(Y_t\) and \(Y_{xx}\) follow from the product rule; \(F=Y_t-\kappa Y_{xx}-sP\), \(G=P_t+\mu P-\gamma Y=-\gamma Y\). Hence forcing is essential: the chosen memory does **not** satisfy the unforced physical ODE. Its exact flux is the derivative of the manufactured field; its scaled remainder, neighboring cancellation, two boundary stencils and observation quadrature check software/algebra. The chosen rough \(s\sim|x-1/2|^{1.6}\) has square-integrable second derivative, with the point singularity assigned a harmless numerical value for sampling. None of these artificial fields verifies the active-base coefficient regularity, existence, exact injectivity, or (8) for the actual experiment.

Current verification, in an isolated temporary environment: `python -m unittest discover -s code/direction-2-moment-analysis -v` — **11 passed**; `python -m unittest discover -s code/direction-2-critical-asymptotics -v` — **3 passed**. No new fabricated physical experiment or filler test was performed. The suites test code properties and artificial examples; they do not independently prove the analytic theorem.

## Evidence that would change the decision

1. Obtain the full Hào–Oanh boundary-observation article and original Birman–Solomyak paper, inspect actual statements and proofs, follow relevant direct predecessors, and map each hypothesis to the complete PDE–ODE output. A directly applicable earlier result would warrant an **existing-theory-subsumes** or model-application classification; continued nonidentification is not a priority proof.
2. Establish or refute the actual rank-one-subtracted observation kernel's source-variable \(H^1\) regularity. If established, apply Volkov exactly and separate its generic consequence from model-specific coefficient and trace analysis. If it fails, supply a rigorous failure for the actual system, not an unrelated diagonal example.
3. Produce an exact theorem with a mathematically consequential hypothesis/conclusion absent from the nearest primary proofs—for example, a complete reachable-graph transposition/density theorem or a constructed nonzero physical initial memory in the exact kernel, with the active coefficients and nonzero load. Either requires a proof, not numerical rank or a sufficient abstract criterion.
4. Validate any claimed stronger rate against an independently checked active-base regularity theorem, or prove sharp lower behavior on the actual base. The added isotropic \(H^{2+\eta}\) assumption alone does not demonstrate that the frozen experiment has it.
5. Obtain user-supplied active-base arrays and error-certified solver inputs before numerical diagnostics. Separate base-solver, coefficient, PDE discretization, time observation and roundoff errors; no exact conclusions from finite truncations.

Only such evidence, accompanied by a fresh primary-source overlap audit, justifies revisiting the standalone gate. No journal choice or manuscript is proposed.
