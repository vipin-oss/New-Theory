# Direction 1: focused prior-art audit

**Date:** 1 November 2026. **Status:** preliminary focused investigation; no new equations or new theory are proposed. This supplement preserves the existing discovery report. The auditor's assessment of Section E is acknowledged as an independent algebraic check, not scientific novelty validation.

## Decision

The Section E mediator model is **not a new foundational theory**. The undamped full coupled model is an exact coefficient specialization of the one-dimensional Mindlin-type system displayed by Berezovski and Ván. The proposed general realization question also encounters substantial prior work in conservative extensions of passive dispersive systems. **No precise mathematical result has yet been established as both new and non-routine.** A narrowly specified question for further screening appears below; it is not asserted to be open or publishable.

This is not the requested complete audit: the original 1964 Mindlin paper and the full 2022 Lazar–Agiasofitou paper were not independently inspected in full, and the full passive-realization and inverse-problem literature was not exhaustively searched. In particular, the exact equivalence below uses the accessible Berezovski–Ván version's explicit attribution to Mindlin, not a verified quotation from the 1964 original. Database-wide Scholar/Scopus/Web of Science/Crossref searches have not been completed. A negative search is not proof of novelty.

## 1. Evidence reviewed and search record

- **Full accessible text:** Berezovski–Ván, arXiv version [BV], especially §§2.4 and 3, equations (35)–(42), (51)–(64), and appendix. Publisher metadata confirms online 25 June 2015, volume 28, 1027–1037 (2016), DOI [10.1007/s00161-015-0453-2](https://doi.org/10.1007/s00161-015-0453-2). The earlier audit's [29] said DOI was unverified; this supplement corrects the bibliographic record without rewriting the original.
- **Full accessible text:** Agiasofitou–Lazar 2023 [AL23], §§2–4, equations (1)–(24); infinite-domain scalar kernel and dispersion are directly checked.
- **Primary paper, abstract and accessible snippets:** Lazar–Agiasofitou 2022 [LA22] identifies retarded Klein–Gordon Green functions, dispersion and band gaps. Detailed mathematical and thermodynamic comparison with the entire 2022 paper remains outstanding.
- **Primary-text evidence about Mindlin:** [BV] explicitly presents its equations (51)–(54) as a 1-D reduction following Mindlin, and (63)–(64) as the rewritten coupled equations. The original [M64] was not read in full; claims specific to its three-dimensional boundary conditions and equation numbering remain unverified here.
- **Accessible primary text:** Figotin–Schenker [FS07], abstract and construction, including its discussion of operator-valued susceptibilities, auxiliary-field Hamiltonian extensions, and the distinction between spatially local examples and spatially dispersive extensions. [FSS] is a related string example. Do not infer that these works automatically establish finite physical-space propagation for every spatial kernel.
- **Accessible preprint:** Neff et al. [N13] describes classical and relaxed micromorphic models and dynamic/static well-posedness under appropriate assumptions; published version and specific theorem hypotheses need checking.

Search phrases used included `"Microinertia and internal variables" "0453-2"`, `micromorphic continuum passive realization constitutive wave equation frequency wavenumber effective modulus`, `passive dispersive media conservative extension Hamiltonian realization Figotin Schenker`, `"nonlocal elasticity of Klein-Gordon type" Lazar Agiasofitou wave dispersion`, and `inverse viscoelastic wave equation wavenumber frequency identifiability`. Results and references are selective, not an exhaustive citation network.

## 2. Exact comparison: Berezovski–Ván and the baseline

For clarity, distinguish the discovery report's constants with subscripts `C0, b0, d0, m0, gamma0`, and let `e=u_x`. The baseline is

```
W = (C0/2)e² + (b0/2)(e-z)² + (d0/2)z_x²,
rho u_tt = [(C0+b0)e-b0 z]_x,
m0 z_tt + gamma0 z_t = d0 z_xx + b0 e - b0 z.
```

The corresponding equation of motion, stress and energy are reproduced **only to compare existing formulations**, not proposed as new equations.

### Mindlin-type reduction as presented in [BV]

[BV] equation (51) uses `epsilon=u_x`, microdeformation `psi`, relative strain `gamma_BV=epsilon-psi`, and

```
W_BV = (rho c²/2) epsilon² + g epsilon gamma_BV
       + (b_BV/2) gamma_BV² + (a/2) psi_x².
```

Its equations (63)–(64) give

```
rho u_tt = (rho c²+b_BV+2g)u_xx - (g+b_BV)psi_x,
I psi_tt = a psi_xx + (g+b_BV)u_x - b_BV psi,
I = rho' d_cell²/3.
```

Set `g=0`, `rho c²=C0`, `b_BV=b0`, `a=d0`, `I=m0`, `psi=z`, and `gamma0=0`. Then **both energies and both coupled field equations coincide term by term**. This is stronger than a resemblance or the prior report's comparison of the microbalance alone. Boundary and initial conditions must also match before solutions of a specific initial-boundary-value problem are identified; [BV] discusses the conceptual role of micro-boundary conditions, not a proof that all boundary-value problems coincide.

### Dual-variable representation in [BV]

[BV] equations (55)–(62) use `alpha, beta` and energy

```
Wbar = (rho c²/2) u_x² + A alpha u_x + (B/2)alpha²
       + (C_BV/2)alpha_x² + (D/2)beta².
```

For its nondissipative choice, `I=1/(L12² D)` and

```
rho u_tt = rho c² u_xx + A alpha_x,
I alpha_tt = C_BV alpha_xx - A u_x - B alpha.
```

Set `alpha=z`, `rho c²=C0+b0`, `A=-b0`, `B=b0`, `C_BV=d0`, `I=m0`. The elastic terms and macro/microbalances match exactly. The term `D beta²/2` becomes `I alpha_t²/2` after using [BV] equation (58), so this part corresponds to baseline **microkinetic** energy, not to its elastic `W`. Positivity of the resulting strain–microdeformation quadratic form follows for `C0,b0>0`: determinant `C0*b0>0`; `d0,m0>0` supply gradient and inertia positivity. The symbol `c` is a parametrization of the instantaneous coefficient, not automatically the relaxed macroscopic wave speed.

[BV] §§2.1–2.4 starts from internal-energy and entropy balances, a generalized entropy flux and a positive-semidefinite dissipative matrix; its explicit §3 specialization sets dissipative coefficients to zero. The baseline's `gamma0 z_t` is absent from that particular displayed nondissipative comparison. It is a standard Rayleigh-type damping addition, and the article's broader dissipative internal-variable discussion is significant prior art; **an exact coefficient mapping to the whole dissipative baseline has not been verified here**. A formal energy inequality for that addition is not equivalent to a complete non-isothermal entropy analysis.

## 3. Comparison with Agiasofitou–Lazar 2023

[AL23] equation (2) formulates a causal space–time integral mapping strain to stress. For an infinite homogeneous medium it factorizes the tensor kernel into elastic moduli and a scalar kernel (5)–(8); equations (9)–(13) use a Green operator

```
L = 1 - ell² Delta + tau² partial_t²,
L t_ij = C_ijkl e_kl.
```

It derives the displacement equation (16)–(18) and dispersion polynomial (23). Its parameter condition `ell/tau > c_L > c_T > 0` is used for real branches and stated band-gap behavior, not a general thermodynamic passivity theorem.

The baseline's mediator denominator, normalized by `b0`, is of the same *operator type*, `1 - (d0/b0) partial_x² + (m0/b0) partial_t² + (gamma0/b0) partial_t`. Nevertheless, the **full stress transfer is not the same**: the baseline is an instantaneous stiffness minus a mediator Green response, whereas [AL23] applies the Green response directly to the classical elastic stress. Its momentum-plus-constitutive dispersion equation therefore cannot be identified with the baseline determinant merely by matching the denominator. The 2023 paper studies a three-dimensional isotropic, unbounded, undamped case, not the same finite-body thermodynamic initial-boundary-value problem; matching branch plots would not prove operator or boundary equivalence.

**Evidence limits:** [AL23] §2 imposes temporal causality and §4 analyzes real frequencies; no complete entropy inequality or positive storage for its full 3-D system was identified in the inspected parts. That is a statement of this inspection, not a proof that no such analysis exists elsewhere. Real dispersion and a retarded kernel do not alone establish a global passive realization or finite propagation of the full coupled boundary problem. The retarded Green kernel and related work are already explicitly present in [LA22].

## 4. Mindlin and micromorphic context

[M64] is a foundational 1964 paper on linear elastic microstructure. [BV] provides the explicit 1-D Mindlin-attributed reduction and coefficient mapping above. [N13] separately describes a family of classical/relaxed micromorphic media, including independent microdistortion and inertia; its abstract reports dynamic and static well-posedness using coercive inequalities. Different kinematic spaces and boundary conditions matter: a 1-D scalar specialization does not establish equality of all 3-D theories, objectivity conditions, or dissipative/thermal constitutive classes. No direct claim about a specific equation or limit in [M64] is made without examining that original paper.

One limiting case that is exactly verified through the displayed specialization is `gamma0=0`. Decoupling the baseline by `b0=0` gives a classical elastic macroequation plus an independent mediator, although that parameter lies on the boundary of the strict positivity assumptions. `d0=0` removes spatial mediator stiffness; `m0=0` is a singular change of evolution class. Neither limit should be presented as an original constitutive contribution or a fully proved convergence theorem.

## 5. Passive realizations and potential theorem: critical screening

[FS07] constructs Hamiltonian extensions of dispersive and dissipative dynamical systems, describes a conservative auxiliary-field realization, and treats operator-valued susceptibility. [FSS] develops a damped string with hidden strings and explicitly notes possible spatial dispersion in the broader methods. These are serious prior art against the claim that a passive system can be represented by energy-carrying auxiliary fields as a new general idea. They do **not**, from the passages reviewed, automatically settle the narrower question of locality and finite propagation in the *physical* spatial coordinate under specified observation and boundary constraints.

**Precisely scoped screening question, not a claimed new theorem:** For a fixed bounded one-dimensional interval with specified mechanical and microboundary ports, which operator-valued, causal, passive strain-to-stress responses can be realized by a finite number of local second-order mediator fields having positive local storage and a specified uniform finite propagation speed? Require the characterization to include boundary response and admissible initial hidden states, not merely an infinite-domain Fourier multiplier. Determine if there is a necessary-and-sufficient criterion, or give a specific passive response demonstrably not realizable within the stated finite-dimensional, local class.

This question is narrower than general passive dilation but is not shown to be new. It might be an application of known positive-real realization, hyperbolic systems and operator theory; the finite-number restriction itself imposes rationality in the Laplace variable, and this elementary obstruction is not a publishable discovery. No criterion, impossibility theorem, proof, novel theory, or experimentally testable invariant has been produced here. A literature search yielding no exact wording would not suffice. Before further formulation, search full texts on distributed parameter systems, positive-real/operator-valued functions, boundary control, hyperbolic transfer functions, spatially dispersive conservative extensions, minimality and realization equivalence.

### Evidence and novelty matrix

| Item | Verified prior overlap | Meaning for Direction 1 |
|---|---|---|
| Coupled scalar macro/micro fields and positive quadratic energy | [BV] (51), (63)–(64): exact undamped specialization | Reject as novel model |
| Dual internal state and microinertia | [BV] (55)–(62) | Reject dual-state relabeling as novelty |
| Hyperbolic spatiotemporal Green operator | [AL23] (9)–(16), [LA22] abstract | Reject space–time denominator alone as novelty; full transfer differs |
| Passive conservative extension and hidden fields | [FS07], [FSS] | Generic extension/realization is prior art; physical-space local finite-speed constraints require separate search |
| Well-posedness of micromorphic systems | [N13] abstract; exact theorem not compared | A model-specific existence proof is not automatically novel |
| Boundary-sensitive measurement and identifiability | [INV] | Not a new theme; a theorem requires comparison of precise inputs/outputs and assumptions |

## 6. Bibliography and access status

- **[BV]** Berezovski, A.; Ván, P. “Microinertia and internal variables.” *Continuum Mechanics and Thermodynamics* 28, 1027–1037 (2016), online 2015. [Publisher DOI](https://doi.org/10.1007/s00161-015-0453-2); [accessible author preprint](https://arxiv.org/abs/1504.03485). Full relevant 1-D equations inspected.
- **[M64]** Mindlin, R.D. “Micro-structure in linear elasticity.” *Archive for Rational Mechanics and Analysis* 16, 51–78 (1964). [10.1007/BF00248490](https://doi.org/10.1007/BF00248490). Full original not inspected; [BV] provides an explicitly attributed reduction.
- **[AL23]** Agiasofitou, E.; Lazar, M. “Nonlocal elasticity of Klein-Gordon type with internal length and time scales: Constitutive modelling and dispersion relations.” *PAMM* 23, e202300065 (2023). [10.1002/pamm.202300065](https://doi.org/10.1002/pamm.202300065); [accessible text](https://publikationen.bibliothek.kit.edu/1000165899/151898056). Constitutive operator and dispersion sections inspected.
- **[LA22]** Lazar, M.; Agiasofitou, E. “Nonlocal elasticity of Klein–Gordon type: Fundamentals and wave propagation.” *Wave Motion* 114, 103038 (2022). [10.1016/j.wavemoti.2022.103038](https://doi.org/10.1016/j.wavemoti.2022.103038). Publisher abstract/snippets inspected; full text not reviewed.
- **[FS07]** Figotin, A.; Schenker, J.H. “Hamiltonian Structure for Dispersive and Dissipative Dynamical Systems.” *Journal of Statistical Physics* (2007). [10.1007/s10955-007-9321-1](https://doi.org/10.1007/s10955-007-9321-1); [author-hosted text](https://users.math.msu.edu/users/schenke6/reprints/jsp2007.pdf). Abstract and key construction inspected; complete theorem hypotheses and implications for physical-space cones remain to audit.
- **[FSS]** Figotin, A.; Schenker, J.H. “Hamiltonian extension and eigenfunctions for a time dispersive dissipative string.” *CRM Proceedings and Lecture Notes* 42 (2007). [Author preprint](https://arxiv.org/abs/math-ph/0604001). Abstract and footnote on spatial dispersion inspected; publisher DOI not verified.
- **[N13]** Neff, P.; Ghiba, I.-D.; Madeo, A.; Placidi, L.; Rosi, G. “A unifying perspective: the relaxed linear micromorphic continuum.” [arXiv:1308.3219](https://arxiv.org/abs/1308.3219), 2013 preprint version. Abstract and selected constitutive/model passages inspected; publication details not verified.
- **[INV]** “A Class of Algorithms for Recovery of Continuous Relaxation Spectrum from Stress Relaxation Test Data Using Orthonormal Functions.” *Polymers* (2023). [10.3390/polym15040958](https://doi.org/10.3390/polym15040958). Abstract reports ill-posed inversion and regularization; author details and full comparison remain to verify.

**Next gate:** obtain and inspect the original Mindlin and the complete related realization/thermodynamic literature, then produce an equation- and theorem-numbered comparison with explicit boundary assumptions. If the narrowly scoped question is already covered or only routinely follows, stop rather than present it as a foundational theory.

---

# Completion supplement: equations, propagation and realization

**Purpose and status.** This supplement adds the evidence and deductions obtained in response to the subsequent Direction 1 directive; the preceding investigation is preserved. It is a documented completion of the available-source audit, **not an exhaustive literature search or a novelty certification**. The original Mindlin paper remains subscription-restricted. The proposed original model is rejected as a new theory; no non-routine new theorem has been demonstrated. The general realization question is retained only as a narrowly scoped mathematical possibility, without claiming an open problem or originality.

## 7. Expanded primary-source inventory and exact evidence

| Reference / access | Verified evidence | Scope and limitation |
|---|---|---|
| Mindlin 1964 [M64], [Springer publisher record](https://link.springer.com/article/10.1007/BF00248490) | Publisher identifies R. D. Mindlin, 16, 51–78, DOI 10.1007/BF00248490; page states subscription/purchase required. | Original full text inaccessible. No original equation numbers, thermodynamic results or boundary conditions are asserted. The 1-D equations attributed to Mindlin are those explicitly reproduced by [BV]. |
| Berezovski–Ván [BV], [full author preprint](https://arxiv.org/html/1504.03485) | Eqs. (51)–(54), (57)–(64) give energies, state equations and both 1-D dynamics; §§2.1–2.4 and appendix discuss energy, entropy flux and dissipation. Publisher date/volume verified. | Original paper uses nondissipative specialization in its §3 comparison; finite-temperature closure, dissipation and particular boundary realization are not automatically identical to the audit baseline. The equations quoted here are from the preprint; possible version differences require checking against the publisher copy. |
| Berezovski et al. 2013 [BE13], [full author manuscript](https://commons.erau.edu/cgi/viewcontent.cgi?article=2024&context=publication) | Eqs. (1)–(4) give quadratic macro/micro energy and coupled dynamics, including `rho0 u_tt=rho0 c² u_xx+A phi_x`, `I phi_tt=C phi_xx-A u_x-B phi`. §§2 and 5 develop internal-variable equivalents and dispersion/initial- and boundary-value waves. | An earlier direct primary antecedent for the same coupled equations and their dispersion, not merely an analogy. Parameters and boundaries still need matching case by case. |
| Agiasofitou–Lazar [AL23], [full text](https://publikationen.bibliothek.kit.edu/1000165899/151898056) | Eqs. (1)–(3) balance and space–time integral, (5)–(10) factorized kernel/Green inverse, (13) `L=1-ell² Delta+tau² partial_t²`, (16)–(18) displacement dynamics, (23)–(24) dispersion and sufficient parameter constraint. | Infinite homogeneous 3-D domain, undamped scalar kernel; this is not identical to the baseline transfer. Its frequency constraint is not by itself a general entropy or passivity theorem. |
| Lazar–Agiasofitou 2022 [LA22], [publisher](https://doi.org/10.1016/j.wavemoti.2022.103038) | Publisher abstract explicitly identifies retarded Klein–Gordon Green functions and acoustic/optic dispersion. | Full text not obtained; equation-by-equation and entropy/boundary comparisons for this article remain incomplete. |
| Figotin–Schenker 2007 [FS07], [full preprint](https://arxiv.org/html/math-ph/0608003v2) | Eqs. (1.10b′), (1.13)–(1.14) and Theorem 1.1 give an operator-valued susceptibility, symmetry/power-dissipation condition and a quadratic Hamiltonian extension subject to §5 regularity. Its §3 footnote explicitly says the general construction accommodates spatial dispersion, but the extended Lagrangian is nonlocal in that case. | General conservative extension is not a theorem guaranteeing local physical-space fields, finitely many internal fields, or finite front speed. A minimal Hamiltonian extension's uniqueness is up to the article's specified isomorphisms, not uniqueness of microscopic physics. |
| Horsley–Philbin 2014 [HP14], [full publisher text](https://iopscience.iop.org/article/10.1088/1367-2630/16/1/013030) | Eqs. (12)–(18), especially (15), give an action with a reservoir field and a **spatially nonlocal** electromagnetic–reservoir coupling; the authors derive a spatially dispersive response. | Primary evidence from electromagnetic media, not a demonstrated equivalence to a mechanical micromorphic solid or a local finite-speed realization. |
| van der Schaft–Maschke 2002 [SM02], [publisher preview](https://doi.org/10.1016/S0393-0440(01)00083-3) | A distributed Hamiltonian formulation explicitly includes boundary energy ports; telegrapher, Maxwell and vibrating-string examples. | Full paper is paywalled in the publisher preview. The abstract establishes prior art for the general boundary-port concept, not a detailed equivalence to this model. |
| Jacob–Zwart 2012 [JZ12], [publisher metadata](https://doi.org/10.1007/978-3-0348-0399-1); Jacob–Zwart 2023 [JZ23], [full preprint](https://arxiv.org/html/2308.01822) | [JZ23] §2, eqs. (1)–(2), derives a transmission-line PDE and boundary power balance; §3 gives a first-order spatial port-Hamiltonian class. [JZ12] provides semigroup, boundary-control, transfer and well-posedness chapters. | [JZ23] is an introduction, not primary proof of a new realization for the mediator; [JZ12] full book was not inspected. |
| Bott–Duffin 1949 [BD49], [publisher DOI](https://doi.org/10.1063/1.1698532) | Bibliographic record and historical passive network synthesis verified; finite-dimensional real-rational positive-real synthesis is reviewed in [JZ23] bibliography context and [PR19]. | Original one-page article not inspected in full. Its lumped-network theorem is not a finite-speed spatially distributed realization theorem. |
| Lewkowicz 2019 [PR19], [full preprint](https://arxiv.org/html/1912.08249) | §1 states the finite-dimensional LTI rational positive-real setting and cites Bott–Duffin; investigates realization structure. | An arXiv preprint, not a substitute for a full audit of operator-valued/nonrational and distributed transfer functions. |

This list is the complete inventory for this focused supplement, not all potentially relevant literature. Do not infer absence of earlier work from it. All URLs above are references or source locations; papers were not copied into the repository.

## 8. Exact scope of equivalence and pre-existing dispersion

The preceding §2 gives the explicit invertible identification `psi=z`, `rho c²=C0`, `b_BV=b0`, `a=d0`, `I=m0`, `g=0`; it makes [BV] (51), (63), (64) match the undamped potential and **both** baseline balance equations. The alternative mapping of [BV] (57), (60), (62) has `A=-b0`, `B=b0`, `C_BV=d0`, and `rho c²=C0+b0`; the dual-variable quadratic term maps to microkinetic energy by [BV] (58). Under matching initial states and compatible micro- and macro-boundary data the corresponding PDE initial-boundary-value problems coincide. This mapping is a direct algebraic deduction from the primary equations; it does not rely on assuming arbitrary 3-D equivalence.

[BE13] independently has exactly the same generalized pair in its eqs. (1)–(4), predating [BV], and explicitly treats dispersion. Substituting the mapped constants and the `exp(st+ikx)` ansatz gives the determinant already derived in the original audit:

```
[rho s²+(C0+b0)k²] [m0 s²+gamma0 s+b0+d0 k²] - b0² k² = 0.
```

The `gamma0=0` equation is therefore the dispersion determinant of an already published coupled system; [BE13] analyzes its dispersion. The determinant is reproduced by algebra from that pair; the above formula is not claimed to be a verbatim numbered equation in [BE13]. The damped case is a standard extension; its exact equivalence to a particular dissipative coefficient set in [BV] has not been proved. Similarly, the energy identity is the familiar balance of the same quadratic continuum system. No claim is made that the exact formula with the present symbols or the proof below was first published in any particular source.

**Thermodynamic comparison.** [BV] starts with thermodynamic entropy and internal energy, generalized entropy flux and conjugate forces; its §3 explicit microelastic identification is nondissipative. Our energy calculation shows a nonnegative mechanical dissipation for `gamma0>=0` only. A full temperature-dependent body requires a separately specified heat/entropy balance and boundary power, not simply a verbal identification of lost mechanical energy as heat. [FS07] is a conservative extension of a linear passive response, not automatically the same as a local Clausius–Duhem formulation or a physical temperature model.

## 9. Positivity, boundary power, and finite propagation

**Assumptions for the following deductions:** the 1-D baseline on the whole real line; constant `rho,m0,C0,b0,d0>0` and `gamma0>=0`; no external force; smooth finite-energy solutions with enough decay/integrability to justify integration. Define `v=u_t`, `p=z_t`, `q=z_x`, `e=u_x`, and

```
h = (rho v²+m0 p²+C0 e²+b0(e-z)²+d0 q²)/2,
F = sigma v+d0 q p,   sigma=(C0+b0)e-b0 z.
```

**Energy and passivity (derived):** completing squares gives `h>=0`, with strict positivity in `(v,p,e,z,q)` for the stated coefficients. The balance is `h_t=F_x-gamma0 p²`. On `[a,b]`, `d/dt integral(h) = [F]_a^b - integral(gamma0 p²)`. Thus the natural outward mechanical port power is `n F`, with effort/flow pairs `(n sigma,v)` and `(n d0 q,p)`. E.g., `v=p=0` or `sigma=q=0` at both endpoints makes the boundary power zero; periodic boundaries also cancel it. This is a power balance, not a proof that every conceivable boundary relation is admissible or generates a semigroup. The generalized boundary-port framework already exists [SM02, JZ23].

**Finite propagation for this baseline (derived, not a novelty claim):** write `c1=sqrt((C0+b0)/rho)`, `c2=sqrt(d0/m0)`, `c*=max(c1,c2)`. Weighted Cauchy–Schwarz gives

```
sigma²/(C0+b0) <= C0 e² + b0(e-z)²,
|F| <= c* h.
```

For a right-moving endpoint `R+c*t`, where `c>=c*`, set `E_R(t)=integral_{R+ct}^infinity h(x,t) dx`. Differentiation and the local balance give

```
E_R'(t) = -F(R+ct,t) - c h(R+ct,t)
          - integral_{R+ct}^infinity gamma0 p² dx <= 0.
```

An analogous left-moving half-line estimate holds. If the initial energy density is supported in `[L,R]`, it remains zero outside `[L-c*t,R+c*t]`. The result concerns the **energy-bearing variables**; displacement itself is defined up to rigid translations and needs initial normalization if its support is to be asserted. These estimates prove a finite upper bound on propagation for smooth whole-line solutions. They do not prove that `c*` is the optimal front speed, establish bounded-domain boundary well-posedness, or prove a complete nonlinear/3-D result. The argument extends to finite-energy weak solutions only after constructing them and justifying approximation; that extension is not proved here.

**Well-posedness status:** positivity plus this a priori estimate gives uniqueness and continuous dependence within an appropriately constructed energy-solution class, but does not alone prove existence. For the constant-coefficient whole-line system, standard symmetric-hyperbolic/semigroup construction is a plausible route using first-order fields `(e,z,q,v,p)` and the constraints `q=z_x`, `e=u_x`; its domain, preservation of constraints and solution space must be established explicitly. For bounded intervals, an energy estimate is necessary but not sufficient: use boundary conditions satisfying an appropriate maximal-dissipativity/range condition, as emphasized by the port-Hamiltonian literature [JZ12, JZ23]. No exponential stability is inferred.

## 10. An explicit obstruction: passive does not imply finite-speed local realization

This is a simple **negative example**, not a claimed novel theorem. It treats a constitutive input–output operator, not necessarily a complete bounded-body elastodynamic model. Let `ell>0` and `G_ell(x)=exp(-|x|/ell)/(2 ell)`, and take real smooth strain inputs `e(x,t)` of compact spatial support, zero before time 0. Define the causal instantaneous nonlocal stress `sigma=G_ell * e`, with convolution in `x`. Its global storage and power satisfy

```
S(t) = (1/2) integral e(x,t) (G_ell*e)(x,t) dx >= 0,
dS/dt = integral sigma(x,t) e_t(x,t) dx.
```

Indeed the Fourier multiplier is `1/(1+ell² k²)>0`, and the kernel is real and symmetric. The system is therefore lossless/passive for the global strain-rate/stress power pairing with zero initial storage. Add any separately passive causal local-in-space hereditary contribution if a genuinely time-hereditary response is desired: the instantaneous nonlocal term still causes the same obstruction.

Choose `e(x,t)=f(t) g(x)`, with nonzero nonnegative compactly supported `g` and `f` switched on after 0. At **every** point outside the support of `g`, `G_ell*g` is positive, so the output there is nonzero immediately whenever `f(t)` is nonzero. A finite-speed spatially local input–output realization with zero initial hidden state, local input/output ports, and propagation bound `c<infinity` cannot reproduce this operator for all such inputs: a point at positive distance from the input support must receive no response before distance/c, whereas this operator responds immediately. The same argument applies on a bounded connected interval if one chooses a positive self-adjoint inverse elliptic kernel and separated internal input/output regions; no particular boundary kernel is asserted here.

**Interpretation:** temporal causality and global passivity do not imply a physical-space cone of dependence. The example does not rule out passive **nonlocal** Hamiltonian extensions, and does not say every passive hereditary kernel violates finite-speed locality. It is a standard support obstruction, not a discovery. An admissible input class restricted by compatibility, measurement geometry or nonzero hidden initial states would need its own formulation; equality of observed transfer operators must include such choices.

For finite-dimensional **lumped** state equations with finitely many time states, the transfer matrix is rational in the Laplace variable; thus a nonrational passive temporal response cannot have such a realization. This elementary observation does **not** imply that a PDE on a bounded spatial interval has a rational boundary transfer function: a finite number of fields still has infinitely many spatial modes, so that stronger claim would be false. Positive-real synthesis for rational lumped transfer functions [BD49, PR19] likewise does not by itself provide a local, finite-speed continuum realization.

## 11. Final novelty assessment and unresolved work

- **Reject** the displayed mediator system, its undamped energy, its coupling and its two-branch dispersion as a new theory: [BV] and [BE13] contain the same coupled structure, with explicit parameter maps above.
- **Reject** generic passive Hamiltonian extension, hidden energy storage, spatially dispersive realization and boundary-port language as novel principles: see [FS07], [HP14] and [SM02]. Their hypotheses, spaces and locality requirements differ, and should not be conflated.
- **Established here under explicit assumptions:** exact undamped coefficient equivalence; the baseline's energy flux bound and smooth-solution finite-speed upper bound; the passive nonlocal counterexample to the blanket realization claim. These are direct, routine deductions from established mathematics and are not asserted to be original or to have been peer reviewed.
- **Not established:** a new necessary-and-sufficient characterization of finite-speed realizability; an invariant unique to continuum mechanics; or a new foundational continuum theory. The finite-speed realization screening question in §5 remains a question only. Existence of many related positive-real, operator-valued, realization and hyperbolic boundary-control results means its novelty is unknown.
- **Remaining access and verification:** obtain [M64] and [LA22] in full; examine original equation numbers, 3-D assumptions, boundary conditions and entropy derivations; inspect [SM02], [BD49] and [JZ12] beyond previews; complete citation-network searches for distributed positive-real realizations, wave-equation boundary ports, nonlocal admissibility and finite-support transfer operators. Search mathematics and control databases and patents where appropriate. No final novelty claim can be based on the current search.

**Recommendation:** **Reject Direction 1 as a proposed new continuum theory.** A separately supervised, narrowly defined realization/finite-propagation mathematics study could be considered only after the outstanding audit; it is not approval to draft a theory or begin a new direction.

## 12. Additional verified bibliographic details

- **[BE13]** A. Berezovski, J. Engelbrecht, A. Salupere, K. Tamm, T. Peets and M. Berezovski, “Dispersive waves in microstructured solids,” *International Journal of Solids and Structures* 50 (2013), 1981–1990. [10.1016/j.ijsolstr.2013.02.018](https://doi.org/10.1016/j.ijsolstr.2013.02.018); [author manuscript](https://commons.erau.edu/cgi/viewcontent.cgi?article=2024&context=publication).
- **[FS07]** A. Figotin and J. H. Schenker, “Hamiltonian Structure for Dispersive and Dissipative Dynamical Systems,” *Journal of Statistical Physics* 128 (2007), 969–1056. [10.1007/s10955-007-9321-1](https://doi.org/10.1007/s10955-007-9321-1); [preprint](https://arxiv.org/html/math-ph/0608003v2).
- **[HP14]** S. A. R. Horsley and T. G. Philbin, “Canonical quantization of electromagnetism in spatially dispersive media,” *New Journal of Physics* 16 (2014), 013030. [10.1088/1367-2630/16/1/013030](https://doi.org/10.1088/1367-2630/16/1/013030).
- **[SM02]** A. J. van der Schaft and B. M. Maschke, “Hamiltonian formulation of distributed-parameter systems with boundary energy flow,” *Journal of Geometry and Physics* 42 (2002), 166–194. [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3). Publisher preview only.
- **[JZ12]** B. Jacob and H. J. Zwart, *Linear Port-Hamiltonian Systems on Infinite-dimensional Spaces*, Operator Theory: Advances and Applications 223, Birkhäuser (2012). [10.1007/978-3-0348-0399-1](https://doi.org/10.1007/978-3-0348-0399-1). Publisher metadata and contents, not full book.
- **[JZ23]** B. Jacob and H. Zwart, “Infinite-dimensional linear port-Hamiltonian systems on a one-dimensional spatial domain: An Introduction,” 2023 preprint. [10.48550/arXiv.2308.01822](https://doi.org/10.48550/arXiv.2308.01822). This is an arXiv identifier, not an asserted journal-publication DOI.
- **[BD49]** R. Bott and R. J. Duffin, “Impedance Synthesis without Use of Transformers,” *Journal of Applied Physics* 20 (1949), 816. [10.1063/1.1698532](https://doi.org/10.1063/1.1698532). Full original not inspected.
- **[PR19]** I. Lewkowicz, “Passive Linear Continuous-time Systems: Characterization through Structure,” 2019 preprint. [10.48550/arXiv.1912.08249](https://doi.org/10.48550/arXiv.1912.08249). arXiv identifier; journal status not verified.
