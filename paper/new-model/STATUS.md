# Phase status, drift checks and restart plan

1. **Literature map — partial.** Original sources are identified; most available evidence is metadata or publisher abstracts, not full papers. Overlap is substantial; the requested literature-supported novelty gap is unproved. See LITERATURE.md.
   **DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; novelty unverified.
2. **Model and thermodynamics — partial.** A periodic global linearized inequality and energy identity are derived, with sufficient parameter conditions and equation-level limiting cases. The local nonlocal interpoint flux, general GL and exact time-shift DPL are missing; source equivalence remains unverified. See MANUSCRIPT.md.
   **DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; newness is unverified.
3. **Analysis — partial.** Classical uniqueness and energy nonincrease, Fourier dispersion and limited propagation conclusions are derived; no existence, exponential stability, general coupled wave-speed classification or boundary-domain theorem. The semi-analytic manufactured periodic series is implemented and tested.
   **DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; newness is unverified.
4. **Benchmarks — partial.** Six automated tests and a spectral convergence illustration passed. A published numerical benchmark was not reproduced; reduced analytic checks are not publication replication. See RESULTS.md.
   **DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; benchmark acceptance criterion remains unmet.
5. **Manuscript — draft only.** Manuscript and author/affiliation included in MANUSCRIPT.md. No independent review, physical validation, TeX compilation or PDF. Publication readiness and originality are not established.
   **DRIFT CHECK: “Is this still a new thermoelasticity model paper?”** Yes in subject; novelty remains an open question.

## Scope-checked possible destinations, not recommendations to submit now
[Journal of Thermal Stresses](https://www.tandfonline.com/journals/uths20/about-this-journal) expressly covers thermoelasticity and mathematical and practical thermal stresses; [Journal of Elasticity](https://link.springer.com/journal/10659/aims-and-scope) covers mechanics of solids including coupling to thermal transport, and stresses significant original contributions. Publisher scope pages checked 2026-11-02. Scope fit is not an assessment of originality, acceptance probability, rank, or readiness. No quartile is claimed.

## Ordered restart
1. Acquire the complete original GL, LS, GN and Tzou texts and the overlapping nonlocal papers; compare constitutive variables, dimension, kernels, thermodynamics and theorems in a line-by-line table. Identify any defensible distinct contribution or discontinue the novelty claim.
2. If exact GL and time-shift DPL are still required, develop a separate extended constitutive model with the correct stress/entropy relaxation and a justified delay/history framework, then independently establish its admissibility; do not relabel this candidate as satisfying them.
3. Derive a local interpoint energy/entropy flux or make the nonlocal thermodynamic axiom precise; establish existence and boundary conditions in a well-defined solution space. Check rigorous coupled dispersion and propagation.
4. Select a published GN/LS/Eringen numerical benchmark with complete accessible data; implement and compare before considering new numerical claims. GL requires an actual GL model.
5. Obtain an independent expert review and author approval before any submission. Same-agent checks cannot replace these.
