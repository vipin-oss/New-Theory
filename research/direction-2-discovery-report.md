# Direction 2 discovery: constitutive state, observation and thermodynamic information

**Research date:** 1 November 2026
**Principal Researcher and final decision-maker:** Dr. Vipin Gupta
**Research Scholar / Builder / Literature Investigator:** Arena
**Independent Scientific Supervisor and Auditor:** ChatGPT

## Executive decision

**Direction 1 is REJECTED AS A NEW FOUNDATIONAL CONTINUUM THEORY.** Its three reports remain part of the research record and are unchanged. No variant of its mediator model is proposed here.

**Direction 2 decision: INVESTIGATE FURTHER, but do not advance a candidate theory.** The most useful question uncovered is whether a *specified set of mechanical and calorimetric observations* determines enough of a material's state to determine a thermodynamic storage and an initial-boundary evolution. This is a question about the relationship between observation, state and thermodynamics, not a new constitutive law. Existing work on material equivalence classes, minimum and maximum free energies, multidomain/multifield memory and dissipative systems already covers substantial parts of it [1–8]. A distinct, defensible gap has **not** yet been established. In particular, merely quotienting histories, adding observables, or using recoverable work is not original on this evidence.

No proposed mathematical structure here meets the threshold for a new foundational continuum theory. The simple calculation in §5 is an **independently checked illustration of an established observability limitation**, not a candidate or a novelty claim. No simulation or manuscript is warranted. An independent scientific auditor has not reviewed this report; the stated research roles do not imply such review occurred.

## 1. Question, motivation and disciplined gap statement

A continuum model needs a state that is sufficient for future response, balances, boundary conditions and thermodynamics. Experimental measurements commonly give only selected stresses, strains, temperatures or boundary fluxes; they do not automatically reveal all initial microscopic or internal conditions. The research question is:

> For a specified class of admissible load and thermal protocols, observation ports and initial states, when do indistinguishable material preparations determine the same future work, calorimetric output and thermodynamic storage? Under what additional assumptions does a well-defined reduced state support an admissible continuum initial-boundary problem?

This is motivated by an actual *information mismatch*: matching one input–output experiment need not establish equality of physical energy, dissipation or hidden initial state. But a generic mismatch is **not a new discovery**. The existing literature already constructs stress-response states [2,3], families and extrema of free energies [3,4], work-based constructions [5,6], and extensions to structured bodies and nonlinear/electromagnetic materials [7,8]. The genuine gap, if any, would be a sharply defined, nontrivial result not already implied by that literature, involving an explicitly bounded experimental protocol class and complete mechanical/thermal continuum boundary-value setting. Its existence and importance are **unresolved**, not asserted.

The issue is different from Direction 1's local mediator and finite-speed realization question: it concerns identification and reduction of state under different observation protocols. It does not require a spatial kernel, microinertial field, a new wave model or a combination of established constitutive ingredients.

## 2. Territories screened and decisions

| Territory / potential structure | Closest comparison and obstacle | Screening decision |
|---|---|---|
| Observable constitutive states and thermodynamic information | Del Piero–Deseri, Deseri–Fabrizio–Golden, Golden and Mariano–Paoletti [2–4,7] already treat equivalent histories, free-energy extrema and state spaces. Willems [5,6] treats supply, storage and realizations. Giorgi–Golden [8] includes nonlinear and electrical settings. | **Investigate as a question only.** No new structure or theorem identified. |
| Geometric incompatibility, topology and defect conservation | Kröner and the geometric-defect literature already give incompatible elastic distortion and defect geometry; Sun [11] explicitly compares geometric compatibility and dislocation density with earlier theory. Nontrivial topology or a curl of distortion is not itself new. | **Reject as a standalone novelty claim.** Dynamic defect evolution, singular cores and boundary topology would each require an independent literature review. |
| Reversible/irreversible geometric evolution and energy conversion | GENERIC [9] and metriplectic constructions [10] already couple conservative and dissipative dynamics and encode energy and entropy constraints. An extra bracket or coupled field is insufficient. | **Reject as a standalone structure.** No specific limitation or new principle established. |
| Nonlinear/multiphysics hereditary state | [7,8] explicitly examine complex bodies, nonlinear memory and electrical conductors; extending a scalar memory state to another field alone does not establish novelty. | **Reject as a combination.** No exact new physical prediction shown. |

This screen is selective; rejected standalone proposals are not statements that these active areas are mathematically complete. Searches included variants of `minimal state viscoelasticity equivalent histories free energy`, `observable hidden states thermodynamic storage realization`, `GENERIC metriplectic degeneracy`, and `incompatible deformation dislocation geometry`; source references and alternate terminology were followed. It is not an exhaustive database or patent search.

## 3. History of the strongest question and exact prior-art comparison

1. **Memory as constitutive state.** Coleman [1] investigated thermodynamics of materials with memory in 1964. Del Piero and Deseri [2] explicitly studied state and free energy in linear viscoelasticity. Their publisher records confirm the historical and bibliographic facts; their complete assumptions and proofs were not accessible in this search.
2. **Minimal states.** Deseri, Fabrizio and Golden [3] state in their abstract that stress-response states, minimum/maximum free energies and an initial-boundary evolution are developed, including an appropriate contraction semigroup and energy decay under the paper's assumptions. Those assumptions and the theorem are not independently verified from the full paper; the abstract cannot justify universal decay. Golden [4] describes equivalence of histories in the Noll sense and energy extrema for a particular model. Thus “different pasts give the same future stress” is already central prior art, not a new principle.
3. **Systems and energy.** Willems [5] introduces available storage and required supply and bounds admissible storage functions, while [6] treats finite-dimensional linear systems and includes viscoelastic applications. The publisher abstracts identify these results; full theorem hypotheses were not inspected. Consequently “work-accessible energy depends on the allowed processes” is not an unexplored principle.
4. **Beyond a simple isothermal mechanical body.** Mariano and Paoletti [7], §5.2 Definition 1 and Proposition 1, use equivalence of histories under all prolongations, a quotient pseudometric and fading memory for a linearized multifield body; §5.6 Theorem 7 discusses free energies and dissipation, and §6 treats structured interfaces. Their assumptions are specific and cannot be extended automatically. Giorgi and Golden [8], §§2–4, discuss nonlinear memory, minimal states, mechanical/electrical applications and free energies. Simply appending electrical, thermal, surface or geometric fields to a state-equivalence construction is therefore a poor originality strategy.
5. **Geometric formalism.** The GENERIC original [9] describes a general reversible–irreversible coupling; [10] explicitly writes the Onsager flux relation in eq. (1), an alternative energy-gradient flux in eq. (2), and describes a metriplectic construction for continuum systems. A new coordinate system or geometric representation would require a substantive result beyond these frameworks, not a new name.

**Exact inclusion comparison.** If the proposed observational state is defined by equality of every future stress under every admissible continuation, with current state components fixed, it is the same *kind* of stress-response equivalence described in [3,4], not an independently new state concept. If equality of all generalized forces is demanded, [7] already includes macrostress, microstress and self-action under continuations. Adding heat/work observations refines an equivalence relation, but refinement alone has not been shown to be a new principle; heat-conduction and non-isothermal histories already appear in the literature and must be traced carefully before any claim.

## 4. Precise investigative formulation — not an asserted model

Let `X` be a set of admissible preparations on a fixed reference body and `U_T(x)` the set of loading/thermal protocols compatible with state `x` over `[0,T]`. Let `Y_P(x;u)` be the resulting trajectory observed through a specified port set `P`, **assuming an already existing, well-defined deterministic solution theory**. For two preparations having the same admissible protocol set, define

```
x ~_P x'  iff  Y_P(x;u) = Y_P(x';u)
                 for every T>0 and every u in U_T(x)=U_T(x').
```

This is a bookkeeping definition of operational indistinguishability, not a claim of novelty. Protocols must respect compatibility, initial traces, admissible controls, geometry and temperature positivity. Equality of protocol sets avoids comparing states for which one experiment is impossible. If protocol sets differ, an alternative equivalence must explicitly include accessibility; comparing only their intersection can be misleading. If uniqueness fails, observations must instead be sets or probability laws of trajectories and the definition changed accordingly.

Let `P_m` denote mechanical observations and let `P_mt` include mechanical and specified thermal observations, with a common protocol family. If `P_m` is a projection of `P_mt`, then directly from the definition

```
x ~_P_mt x'  implies  x ~_P_m x'.
```

The reverse need not hold. A quantity `A:X->R` is well-defined on the mechanical quotient precisely when it is constant on each `~_P_m` class. That is a definition-level factorization criterion, not a substantial theorem. Different choices of measured output, times, controllability and state restrictions produce different equivalence classes. Storage is not generally uniquely fixed even when it is a state function: compare [3–6]. A quantity could fail to descend simply because it includes an energy reservoir neither measured nor coupled to the allowed ports.

**Only a research target, not a formulated candidate:** characterize a meaningful class of *coupled, observable, thermomechanical* continua for which a restricted-port quotient admits a physically calibrated storage, while proving or disproving well-posedness of its induced dynamics. The burden is to identify explicit nontrivial assumptions and show that any result is not contained in [2–8] or existing inverse/control and thermoviscoelastic literature. The decoupled counterexample below is a baseline that such a result must handle or explicitly exclude; it does not solve that target.

## 5. Independently checked test: identical mechanical outputs do not fix total storage

This deliberately elementary, established-type example is used to falsify an overstrong inference, not to propose a new theory. Consider an isothermal material point in a small-strain one-dimensional bar, with imposed strain `e(t)` and an unobserved dimensionless internal preparation `w(t)`. Let

```
sigma = C e,                  w_t = -a w,
psi(e,w) = (C/2)e² + (H/2)w²,
```

where `C,H>0` have units of stress (energy per reference volume), and `a>0` has units `1/time`. `e,w` are dimensionless. For any differentiable imposed strain,

```
psi_t = C e e_t + H w w_t
      = sigma e_t - a H w²,
D := sigma e_t - psi_t = a H w² >= 0.
```

Thus the *isothermal mechanical free-energy inequality* is satisfied for every `e(t)` and `w(0)`, and `psi` is positive definite in `(e,w)`. For two initial conditions with the same initial strain but `w_1(0)^2 != w_2(0)^2`, both yield exactly `sigma(t)=C e(t)` under every common strain continuation, but `psi_1(0) != psi_2(0)` and the dissipated powers differ. The mechanical port alone cannot identify this total storage on this unrestricted preparation class. If `w(0)=0` is imposed, the discrepancy disappears; it also disappears from the mechanical state if one explicitly discards the hidden reservoir and uses the lower storage `C e²/2`. Such a reduced storage does **not** equal the full stored energy for all hidden preparations.

For a standard quasistatic or dynamic bar, one may pair this constitutive response with `e=u_x`, `rho u_tt=sigma_x+f` and compatible displacement/traction initial-boundary data; the mechanical equation is independent of `w`, so its response is the same given the same `u,u_t` and forcing, provided the corresponding mechanical problem is well posed. The example does not rely on or assert an independent existence theorem. Mechanical energy density `rho u_t²/2+psi` satisfies, for smooth fields,

```
partial_t (rho u_t²/2 + psi)
  = partial_x(sigma u_t) + f u_t - a H w².
```

Boundary power is `n sigma u_t` **into** the bar. With no body force, zero boundary supply and sufficient regularity, total mechanical free energy is nonincreasing. `w` evolves pointwise; prescribe `w(x,0)` and no spatial boundary condition for it. This is an energy estimate, not a proof of coupled-system well-posedness.

### Thermodynamic interpretation and limitations

At a fixed bath temperature `theta0>0`, the calculated `D` is compatible with an isothermal free-energy balance, with `D/theta0` an entropy-production density **only after** a suitable heat-bath/energy accounting is supplied. If all dissipated energy is assumed to leave immediately as heat, a calorimeter resolving that outflow can distinguish preparations with different `w²`, so the result is not a mechanical-plus-calorimetric indistinguishability claim. In a full thermomechanical body, temperature, heat flux, thermal energy and entropy constitutive laws, heat capacity, boundary heat exchange and the local first and second laws must be defined and checked; they are not defined here. The sign of `w` remains indistinguishable by the illustrated quadratic heat output as well. We make no claim about a unique full physical energy based on mechanical measurements.

The scalar one-dimensional example is small-strain and does not establish finite-deformation frame indifference. A 3-D objective extension would require objective strain and a specified transformation law/material symmetry for the internal quantity; choosing one is a separate modeling assumption. A displacement-dependent actual observer transformation cannot be resolved by relabeling the scalar. Dispersion, front speed and physical prediction are not relevant to this decoupled illustration. It is not a new continuum formulation and cannot justify advancing Direction 2.

## 6. Scientific status and possible next tests

| Status | Item |
|---|---|
| Established by source | Stress-response minimal state, memory free energies and continuum evolution already studied [2–4,7,8]; storage bounds and input–output dissipativity studied [5,6]. |
| Independently verified here | Logical refinement of a fixed-protocol equivalence relation; the explicit inequality and mechanical indistinguishability in §5. |
| Plausible but unproven research question | Whether physically meaningful *restricted* combined thermal/mechanical observations define a well-posed reduced continuum state while retaining a specified energy observable. This is not asserted to be new or unsolved. |
| Potentially original proposition | **None identified.** A candidate proposition requires exact hypotheses, a genuinely nontrivial statement, a search of equivalent notions, and a proof or explicit conjecture status. |
| Demonstrated novelty | **None.** No proof of priority, unexplained prediction, or parameter-invariant difference from existing theories. |

If Dr. Gupta authorizes further inquiry, first (1) obtain full texts of [2,3,5,6] and the relevant non-isothermal/heat-conduction minimal-state papers; (2) map work-equivalence versus force-response-equivalence and precise available/required storage hypotheses; (3) fix the class of observations, preparation accessibility, temperature boundary protocols and calorimetric resolution; (4) compare against nonlinear system observability, minimal realization, inverse problems and existing thermomechanical PDE results; and only then (5) formulate an example with genuinely coupled observable thermal dynamics and a precise mathematical claim. A decisive negative result from (1)–(4) would close the question. No numerical exploration before a defensible candidate and admissible model exist.

## 7. Source audit: bibliographic facts, access and evidential limits

| Ref. | Source and primary evidence checked | Access / limits |
|---|---|---|
| [1] | B. D. Coleman, “Thermodynamics of materials with memory,” *Archive for Rational Mechanics and Analysis* **17**, 1–46 (1964), [10.1007/BF00283864](https://doi.org/10.1007/BF00283864). Publisher record confirms metadata. | Subscription record; original equations and proof not inspected. |
| [2] | G. Del Piero and L. Deseri, “On the Concepts of State and Free Energy in Linear Viscoelasticity,” *Archive for Rational Mechanics and Analysis* **138**, 1–35 (1997), [10.1007/s002050050035](https://doi.org/10.1007/s002050050035). | Publisher metadata/preview, not full proof or equation numbers. |
| [3] | L. Deseri, M. Fabrizio and J. M. Golden, “The Concept of a Minimal State in Viscoelasticity: New Free Energies and Applications to PDEs,” *Archive for Rational Mechanics and Analysis* **181**, 43–96 (2006), [10.1007/s00205-005-0406-1](https://doi.org/10.1007/s00205-005-0406-1). | Publisher abstract and bibliography; full text subscription-only. Reported semigroup and decay are the abstract's claims under the paper's own assumptions, not independently verified theorems here. |
| [4] | J. M. Golden, “Minimal states and maximum free energies of materials with memory,” *Computers & Structures* **84**, 1115–1124 (2006), [10.1016/j.compstruc.2006.01.007](https://doi.org/10.1016/j.compstruc.2006.01.007). | [Publisher abstract and introduction](https://www.sciencedirect.com/science/article/abs/pii/S0045794906000782); full article not accessible. Specific singularity claims are not generalized here. |
| [5] | J. C. Willems, “Dissipative dynamical systems part I: General theory,” *Archive for Rational Mechanics and Analysis* **45**, 321–351 (1972), [10.1007/BF00276493](https://doi.org/10.1007/BF00276493). | Publisher abstract and metadata; complete original theorem statements and conditions not checked. |
| [6] | J. C. Willems, “Dissipative dynamical systems Part II: Linear systems with quadratic supply rates,” *Archive for Rational Mechanics and Analysis* **45**, 352–393 (1972), [10.1007/BF00276494](https://doi.org/10.1007/BF00276494). | Publisher abstract; finite-dimensional linear results must not be imported wholesale to continuum PDEs. |
| [7] | P. M. Mariano and P. Paoletti, “Complex bodies with memory: linearized setting,” [arXiv:0805.4307v1](https://arxiv.org/html/0805.4307) (2008), [10.48550/arXiv.0805.4307](https://doi.org/10.48550/arXiv.0805.4307). | Accessible full preprint, selected §§1, 5.2–5.3, 5.6 and 6; Definition 1, Proposition 1, Theorem 7 and surface Definition 12 checked as printed, not independently reproved in full. Preprint DOI is not an assertion of a journal DOI. |
| [8] | C. Giorgi and J. M. Golden, “Viscoelastic and Electromagnetic Materials with Nonlinear Memory,” *Materials* **15**, 6804 (2022), [10.3390/ma15196804](https://doi.org/10.3390/ma15196804). | [Open full article](https://www.mdpi.com/1996-1944/15/19/6804), introduction and §§2–4 examined; it explicitly studies nonlinear and electrical cases. Not an exhaustive check of each mathematical proof. |
| [9] | M. Grmela and H. C. Öttinger, “Dynamics and thermodynamics of complex fluids. I. Development of a general formalism,” *Physical Review E* **56**, 6620–6632 (1997), [10.1103/PhysRevE.56.6620](https://doi.org/10.1103/PhysRevE.56.6620). | Publisher abstract and metadata; original full equations and theorem numbers not inspected. |
| [10] | A. Zaidni and P. J. Morrison, “Metriplectic 4-bracket algorithm for constructing thermodynamically consistent dynamical systems,” [arXiv:2501.00159v2](https://arxiv.org/html/2501.00159v2), dated 23 January 2025 on the arXiv record, [10.48550/arXiv.2501.00159](https://doi.org/10.48550/arXiv.2501.00159). | Full preprint accessible; introduction, eqs. (1)–(2) and construction overview examined. Not a full independent proof audit; no journal publication asserted. |
| [11] | B. Sun, “Incompatible deformation field and Riemann curvature tensor,” *Applied Mathematics and Mechanics (English Edition)* **38**, 311–332 (2017), [10.1007/s10483-017-2176-8](https://doi.org/10.1007/s10483-017-2176-8). | [Open article](https://www.amm.shu.edu.cn/fileup/0253-4827/HTML/20170301.htm), abstract and introduction inspected, including comparison with Kröner; much mathematical notation in fetched rendering is in images. Original Kröner full text and equation-level attribution were not independently verified. |
| [12] | G. Amendola, M. Fabrizio and J. M. Golden, *Thermodynamics of Materials with Memory: Theory and Applications*, Springer (2012), [10.1007/978-1-4614-1692-0](https://doi.org/10.1007/978-1-4614-1692-0). | Publisher book overview and contents only; not full-text verification. Shows wider context including inverse problems and memory PDEs. |

The above evidence does not exclude earlier, equivalent or later literature. Some key primary sources are inaccessible and mathematical physics/control and coupled thermo-electro-mechanics need further tracing. No reliance on inaccessible equations or an exhaustive novelty search is claimed.

## 8. Final recommendation

**Do not advance a Direction 2 theory.** Keep the bounded-observation/state question as an **unapproved research lead** only. Its generic statement is substantially anticipated by existing theories; its proposed narrower coupled thermomechanical setting has neither a proved gap nor a complete candidate. Direction 1 remains closed, and no alternative foundational theory has been demonstrated in this investigation. Final scientific and programme decisions rest with Dr. Vipin Gupta, with independent audit still required.
