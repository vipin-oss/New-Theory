# Direction 2: three boundary-identification problem specifications

**Research-planning document — 1 November 2026**

## 1. Binding scope and recommendation

Direction 1 remains **REJECTED** as a new foundational continuum theory. Direction 2 remains **REFORMULATE**. No theory, novelty, theorem or publication claim is made. The three alternatives below are inverse problems for standard thermoviscoelastic constitutive ingredients, not new continuum theories. This document builds on `direction-2-focused-prior-art-audit.md`; its access caveats remain in force.

**Recommendation for possible future investigation: formulation A**, subject to Dr. Vipin Gupta's decision and a further primary-literature check. It has a fixed one-dimensional body, a single unknown memory-state field and explicit boundary sensors. Even here, injectivity, a non-uniqueness example, and stability are all currently **unproved**. A boundary restriction or new combination of known equations is not evidence of a gap. The final choice belongs to Dr. Gupta. No derivation programme, simulation or manuscript is authorized by this recommendation.

Research roles: Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This planning document is not an independent audit.

## 2. Common physical constitutive model and its thermodynamics

All alternatives use the following conventional small-strain, thermoviscoelastic model with Fourier heat conduction. The internal variables are a finite-dimensional-in-memory realization of exponential relaxation; there is **no thermal memory kernel**. Quantities are per unit reference volume, and changes of geometry and cross-section are neglected. Let \(\Omega\) be the body, \(v=u_t\), \(E=\operatorname{sym}\nabla u\), and \(\theta>0\). In one dimension, \(E=u_x\), \(u\), stress and internal variables are scalars and \(I=1\). In three dimensions they are symmetric tensors, \(I\) is the identity, and the known elasticity tensor \(\mathbb C\) is symmetric and positive definite on symmetric tensors.

Choose known constants \(c,\kappa,\rho,\theta_*,k_j,\lambda_j>0\), and a known nonzero thermal coupling \(b\). Use the Helmholtz free-energy density and laws

\[
\begin{aligned}
\psi(E,\theta,Z)&=\tfrac12 E:\mathbb C E-b(\theta-\theta_*)\operatorname{tr}E
+c[\theta-\theta_*-\theta\ln(\theta/\theta_*)]
+\sum_{j=1}^m\tfrac{k_j}{2}|E-Z_j|^2,\\
\sigma&=\mathbb C E-b(\theta-\theta_*)I+\sum_j k_j(E-Z_j),\\
\eta&=-\partial_\theta\psi=b\operatorname{tr}E+c\ln(\theta/\theta_*),\\
\partial_t Z_j&=\lambda_j(E-Z_j),\qquad q=-\kappa\nabla\theta.
\end{aligned}
\]

The prescribed physical internal-energy density, with the above reference normalization, is

\[
e=\psi+\theta\eta
=\tfrac12E:\mathbb C E+\sum_j\tfrac{k_j}{2}|E-Z_j|^2
+b\theta_*\operatorname{tr}E+c(\theta-\theta_*).
\]

This \(e\) is not \(\psi\), and neither is asserted to equal minimum available storage. Substituting the laws into the local first law \(e_t=\sigma:E_t-\nabla\!\cdot q\), with no body heat source, gives the exact thermal equation

\[
c\theta_t=\kappa\Delta\theta-b\theta\operatorname{tr}E_t
+\sum_j k_j\lambda_j |E-Z_j|^2. \tag{1}
\]

The last term converts mechanical relaxation dissipation to heat; the thermoelastic term is reversible coupling and is not entropy production. The local entropy balance follows directly:

\[
\eta_t+\nabla\!\cdot(q/\theta)=
\frac{\sum_j k_j\lambda_j|E-Z_j|^2}{\theta}
+\frac{\kappa|\nabla\theta|^2}{\theta^2}\ge0. \tag{2}
\]

Consequently (1) and (2) give a route to the first and second laws for each alternative, **conditional on sufficiently regular solutions with positive temperature**. No general existence, positivity, or inverse theorem is claimed. Since \(Z_j(t)=e^{-\lambda_j t}Z_j(0)+\lambda_j\int_0^t e^{-\lambda_j(t-s)}E(s)ds\), the unknown \(Z_j(0)\) is a compressed initial memory state, not the entire history; \(k_j,\lambda_j\) and the relaxation kernel are known. Distinct pasts can share this state.

For outward normal \(n\), traction \(\sigma n\), and heat flux \(q\), the mechanical boundary power and inward thermal power are respectively

\[
P_m=\int_{\partial\Omega}(\sigma n)\cdot v\,dS,\qquad
P_h=-\int_{\partial\Omega}q\cdot n\,dS.
\]

With \(\rho v_t=\nabla\cdot\sigma\), integration gives \(d\int_\Omega(e+\rho|v|^2/2)/dt=P_m+P_h\). With quasistatic \(\nabla\cdot\sigma=0\), the same identity holds without kinetic energy. The entropy boundary supply is \(-\int_{\partial\Omega}q\cdot n/\theta\,dS\), not \(P_h\) and not the right-hand production in (2). A calorimeter measures heat transfer, not local stored energy or entropy production automatically. Fixed-temperature baths and force/heat-flux sensors below are idealized, measurable boundary devices; sensors are passive, and accuracy, finite bandwidth and bath losses must be addressed experimentally.

## 3. Common mathematical conventions and limits

For each formulation, set a concrete \(T=10/\lambda_1\), \(\delta=T/100\), and assume boundary instruments return exact continuous-time traces only on \((\delta,T)\). This idealization is needed for the mathematical uniqueness question; in reality measurements are sampled and noisy. The nonzero delay avoids requiring that potentially incompatible initial boundary traces be measured at \(t=0\). A single fixed experiment is specified, not an assumed family of infinitely repeatable preparations. Outputs include measured reactions/heat transfer, not merely prescribed inputs.

For each candidate initial state in the defined admissible class, **assume** a unique solution on \([0,T]\), sufficiently regular for the stated traces and identities, and satisfying \(\theta\ge\theta_*/2\). The inverse question is conditional on proving this forward assumption for a useful nontrivial class. The admissible class is explicitly the set of initial data with stated regularity/bounds for which such a solution exists; it includes the equilibrium solution for zero actuation. In the active experiments below existence and a nontrivial admissible class are not established. No a priori bound on all possible solutions is claimed. A rigorous extension to weak solutions and sensor traces is a separate prerequisite.

For the target field \(z\) in a formulation, write \(F(z)\) for its complete specified measurement vector. The uniqueness question is the exact injectivity statement \(F(z)=F(\tilde z)\) almost everywhere on \((\delta,T)\) implies \(z=\tilde z\) almost everywhere in the body, **within that admissible class**. Equal outputs on one fixed experiment do not mean equality for all conceivable controls. A possible conditional stability question is

\[
\|z-\tilde z\|_{L^2(\Omega)}\le C\,\omega\bigl(\|F(z)-F(\tilde z)\|_{L^2(\delta,T)}\bigr), \tag{3}
\]

where \(C\) can depend on the known experiment and an a priori \(H^2\) bound, and \(\omega(r)\to0\) as \(r\to0\). For vector/tensor outputs use the product \(L^2\) norm. Whether any modulus exists, or is Lipschitz, Hölder or logarithmic, is unknown; (3) is a question, not a claimed estimate. Infinite-dimensional recovery from noisy finite-resolution sensors is expected to be delicate and may be unstable even if exact traces are injective.

All three alternatives **know** the constitutive coefficients and normalized functions \(e,\psi\). They do not identify kernels, parameters, physical energy functions or Helmholtz free-energy functions. Nor do they identify minimum available storage: that would first require a specified supply, admissible controls and normalization. If the target state is recovered, the known \(e\) and \(\psi\) can be evaluated at that state; that is not independent measurement or functional identification. If the entire initial state and later inputs are known and the forward problem is well posed, future fields are predictable in that assumed model; the inverse problem is not itself identification of an unknown future law. Observation of full physical microstate or past history is not implied.

## 4. Formulation A — quasistatic one-dimensional bar, unknown initial memory state

**Body and model.** A homogeneous straight bar \(0<x<L\) of known uniform area \(A_0\); all equations are per unit area. Take \(m=1\), \(\mathbb C=a>0\), \(k_1=k>0\), \(\lambda_1=\lambda>0\). With \(\varepsilon=u_x\) and \(z=Z_1\), the governing balances and constitutive law are

\[
\partial_x\sigma=0,\quad
\sigma=a\varepsilon-b(\theta-\theta_*)+k(\varepsilon-z),\quad
z_t=\lambda(\varepsilon-z),\quad
c\theta_t=\kappa\theta_{xx}-b\theta\varepsilon_t+k\lambda(\varepsilon-z)^2.
\]

This is mechanically quasistatic and thermally transient; the derived laws (1)–(2) apply, with bath heat flux at both ends and force \(A_0\sigma\). The quasistatic assumption is appropriate only for sufficiently slow loading compared with elastic wave travel time and is part of the model, not a consequence of the inverse data.

**Unknown and known initial quantities.** The target is \(z_0\in H^2(0,L)\), with \(\|z_0\|_{H^2}\le M\), for a fixed known \(M>0\). The initial temperature is known and spatially uniform: \(\theta(x,0)=\theta_*\). The initial displacement is not an independent unknown: it is the solution of initial quasistatic equilibrium with the fixed end positions. Its reference is fixed by \(u(0,0)=0\). Thus the initial material state \((\varepsilon_0,\theta_*,z_0)\) is determined by \(z_0\) in the model; no arbitrary initial velocity exists in this quasistatic formulation. The unknown memory history leading to \(z_0\) is not the target.

**Actuation and measurement.** For the single prescribed experiment, fix \(u(0,t)=0\), \(u(L,t)=g(t)=g_*\sin^2(\pi t/T)\), with known small nonzero \(g_*\); impose \(\theta(0,t)=\theta(L,t)=\theta_*\) using thermostatic baths. A load cell at \(x=L\) records \(F_m(t)=A_0\sigma(L,t)\). Calorimeters record the outward heat powers \(Q_0(t)=A_0\kappa\theta_x(0,t)\) and \(Q_L(t)=-A_0\kappa\theta_x(L,t)\); these follow from \(q\cdot n\) at the left and right ends. The data are \(F_A(z_0)=(F_m,Q_0,Q_L)|_{(\delta,T)}\). Both ends are assumed thermally and mechanically instrumented without altering the ideal boundary conditions; lateral surface is insulated.

**Question.** Is \(F_A\) injective on the admissible \(H^2\)-bounded class? Is any conditional estimate of type (3) valid? The measured force and heat powers are observable by construction; pointwise \(z_0\), local initial energy and past history are **not shown** observable. An injective answer, if obtained, would recover this model's full initial material state because the other fields are known or constrained, but not the past itself. An ideal time trace contains infinitely many data; it is not equivalent to practical finite sampling.

**Main difficulties and prior-art risk.** Initial memory enters the stress as a spatial field, while quasistatic equilibrium makes the reaction spatially uniform and couples strain nonlocally. Heat contains a quadratic relaxation source, nonlinear thermoelastic coupling and potentially sign ambiguities; limited bath flux may average information away. Positive-temperature forward well-posedness, boundary trace regularity and admissible initial preparation must be proved first. This is closely related to existing 1-D memory observability and heat-source inverse problems; a direct reduction could make it routine or already covered. FGG's non-isothermal material-point equivalence includes internal energy as generalized response, but is not a theorem about this particular fixed finite-time boundary experiment. Carillo treats thermal work equivalence in a different rigid heat-memory model. Their differences do **not** establish novelty.

## 5. Formulation B — dynamic one-dimensional bar, unknown initial memory state

**Body and model.** Use the same bar, one branch and exact constitutive laws as A, but retain inertia: \(\rho u_{tt}=\sigma_x\), with the same \(z_t\) and thermal equation. Kinetic energy and mechanical boundary power enter the integrated first law as in §2. This is a dynamic wave–heat–relaxation problem, not the quasistatic experiment A.

**Initial quantities.** Prescribe \(u(x,0)=0\), \(u_t(x,0)=0\), and \(\theta(x,0)=\theta_*\), all known. The sole target is the unknown \(z_0\in H^2(0,L)\), \(\|z_0\|_{H^2}\le M\), restricted to states producing the specified regular positive-temperature solution. No initial equilibrium is required: the hidden branch stress can generate initial acceleration. Known coefficients are \(a,b,k,\lambda,c,\kappa,\rho,\theta_*,L,A_0\).

**Inputs and outputs.** Hold both bar ends fixed, \(u(0,t)=u(L,t)=0\); this is a passive clamp experiment, not a claim that additional excitations have been applied. Hold both end temperatures at \(\theta_*\). A load cell at the right end measures \(A_0\sigma(L,t)\); two calorimeters measure the outward heat powers \(A_0\kappa\theta_x(0,t)\) and \(-A_0\kappa\theta_x(L,t)\). The measured vector \(F_B(z_0)\) is their restriction to \((\delta,T)\). The mechanical boundary power is zero because the clamps have zero velocity, although the reaction is measurable; thermal energy may leave or enter the baths.

**Question and stability.** Is the map \(F_B\) injective, and if so can an estimate (3) hold on the admissible class? All mechanical displacement/velocity and initial temperature fields are fixed, so recovery of \(z_0\) gives the initial state for this model. Force and boundary heat are measured; the branch field, its past and local energy are not directly measured, and their identifiability remains open. The known kernels and physical energy functions are not estimated. A fixed-time horizon need not satisfy a wave observability geometric/time condition, and no such condition is assumed to hold merely because \(T=10/\lambda\).

**Analytical difficulties and closest work.** The inverse source generated by initial branch stress interacts with wave propagation, heat smoothing, quadratic dissipation and unbounded boundary traces. The known \(u_0,v_0,\theta_0\) make this materially different from recovering arbitrary initial wave/heat data. Green, Liu and Mitkovski's 2019 [boundary observability for the viscoelastic wave equation](https://www.math.wustl.edu/~awgreen/files/papers/visco-control-siamjco-2020.pdf), full PDF introduction inspected, treats a known kernel \(M\in H^2(0,T)\), zero lower limit prehistory, and recovery of \((w_0,w_1)\) by partial-boundary normal-derivative data under a geometric condition. It does not directly establish recovery of an independent nonzero \(z_0\) coupled to heat. Its exact observability framework may nevertheless cover or strongly constrain a reduction. Bellassoued–Yamamoto and Wu–Liu (§7) address related thermoelastic inverse sources; obtaining their full assumptions and searching further for initial-memory observability is essential. Risk of routine duplication is high.

## 6. Formulation C — three-dimensional dynamic body with two known relaxation times

**Body and model.** Let \(\Omega\) be the unit ball in \(\mathbb R^3\), with known smooth homogeneous positive-definite isotropic \(\mathbb C\). Set \(m=2\), with known \(k_1,k_2>0\) and distinct known \(\lambda_1,\lambda_2>0\). The state equations are \(\rho u_{tt}=\nabla\cdot\sigma\), equation (1), and \((Z_j)_t=\lambda_j(E-Z_j)\), with the tensor laws in §2. Two branches represent a fixed two-exponential spectrum, not an arbitrary kernel or an extra physical field introduced solely for complexity. This choice increases scope and prior-art risk; it does not demonstrate an advantage.

**Initial quantities and data.** Set known \(u(x,0)=u_t(x,0)=0\), \(\theta(x,0)=\theta_*\), and known \(Z_2(x,0)=0\). The only unknown is symmetric \(Z_1(x,0)\in H^2(\Omega;\mathrm{Sym}(3))\), bounded by \(M\). This avoids pretending two unrestricted tensor fields can be identified by a few sensors and retains a genuinely three-dimensional memory-state target. Physical preparation of \(Z_2=0\) while \(Z_1\) is unknown is a strong experimental assumption, not a known procedure. Prior histories are not determined. All coefficients, including the two rates, conductivity and heat capacity, are known.

**Controls and finite-port observations.** Fix \(u=0\) and \(\theta=\theta_*\) on all of \(\partial\Omega\) during the one experiment. Let the fixed disjoint surface patches be the six spherical caps
\(\Gamma_{\pm i}=\{x\in\partial\Omega: \pm x_i>0.9\}\), \(i=1,2,3\). At each cap measure the three components of the integrated reaction \(R_{\pm i}(t)=\int_{\Gamma_{\pm i}}\sigma n\,dS\) and the integrated outward heat power \(H_{\pm i}(t)=\int_{\Gamma_{\pm i}}q\cdot n\,dS\). This gives 24 scalar time traces \(F_C(Z_{1,0})\) on \((\delta,T)\), not full spatially resolved boundary data. The rest of the boundary remains clamped and thermostated but unmeasured. Realization requires segmented force and heat-flux sensors with known spatial integration and bath losses. With the clamped boundary the mechanical input power is zero; total thermal supply in the first law includes **all** the boundary, not just the six measured patches.

**Question and stability.** Does equality of the 24 traces imply equality of the six independent components of \(Z_{1,0}\) almost everywhere? If yes, does any a priori bounded conditional estimate of form (3) exist? Pointwise displacement, temperature, entropy and memory are not directly observed. No general injectivity or non-injectivity is asserted. Finite spatial ports can have unobservable modes, and the ball/patch symmetries and tensor nature make that risk acute; continuous time does not make their recovery automatic. Known energy functions permit evaluation only if enough state is recovered; initial-energy functional and storage are not targets.

**Main analytical difficulties and closest work.** Three-dimensional vector elasticity, tensor-valued memory, finite patch integration, spectral multiplicities, parabolic smoothing and nonlinear heat generation make rigorous uniqueness or a robust counterexample much harder. Green–Liu–Mitkovski provide spatially resolved normal-derivative wave observability on a geometric boundary set, not these 24 integrated ports or an independent memory state. Grasselli, Muñoz Rivera and Squassina's [thermoviscoelastic plate with memory](https://arxiv.org/html/0806.0965) is a coupled PDE with initial histories and semigroup/decay analysis, not this tensor inverse problem. The 2012 Amendola–Fabrizio–Golden book advertises thermoelastic memory controllability and inverse problems, but its relevant chapters remain uninspected. Those omissions, and the broad prior literature on hyperbolic–parabolic observability, make any novelty claim particularly premature.

## 7. Prior-art challenge and source-access ledger

The most relevant published primary work and what it does **not** settle are listed below; access levels are as actually inspected. No literature search is exhaustive.

| Source | Verified scope and access | Consequence for these specifications |
|---|---|---|
| Fabrizio, Gentili & Golden, 2004, [nonisothermal free energies](https://www.sciencedirect.com/science/article/pii/S089571770490009X) | Full PDF introduction and §§2–3 inspected. At a material point, present fields and all-process generalized responses (stress and internal energy) define equivalence; Proposition 3.1 relates response/work and Theorem 3.2 describes minimum scaled free energy under stated dissipation/normalization assumptions. | Strong prior art against a general observation/storage theory. Not an established result for A–C's spatial boundary traces. No inference that the latter are original. |
| Carillo, 2005, [heat conduction and viscoelasticity](https://www.atlantis-press.com/article/488.pdf) | PDF introduction and selected §§2–3; rigid heat-conduction memory and isothermal viscoelasticity, thermal work/response equivalence under the author's process assumptions. | Thermal minimal state and work are already studied. A–C instead use Fourier conduction and mechanical exponential memory, and do not infer a new heat-memory theory. |
| Deseri, Fabrizio & Golden, 2006, [minimal state in viscoelasticity](https://link.springer.com/article/10.1007/s00205-005-0406-1) | Abstract only; stress-based minimal states, free energies and viscoelastic IBVP. | Closest state/IBVP foundation; exact overlap and hypotheses require full text. |
| Willems, 1972, [general theory](https://link.springer.com/article/10.1007/BF00276493) and [linear systems](https://link.springer.com/article/10.1007/BF00276494) | Publisher abstracts only. Available storage, required supply and dissipativity precede any proposed storage identification. | No general equality of observed state, physical Helmholtz energy and all admissible storages. Exact PDE applicability and hypotheses are not verified. |
| Green, Liu & Mitkovski, 2019, [boundary observability](https://www.math.wustl.edu/~awgreen/files/papers/visco-control-siamjco-2020.pdf) | Full paper introduction inspected: known kernel, boundary normal derivative and initial displacement/velocity; no separate unknown prehistory in displayed equation. | Strong duplication risk for B/C; needs comparison against independent initial-memory forcing and thermal coupling. |
| Bellassoued & Yamamoto, 2011, [inverse heat source in thermoelasticity](https://iopscience.iop.org/article/10.1088/0266-5611/27/1/015006) | Publisher abstract only; coupled linear thermoelastic inverse heat source, Carleman estimate and Hölder stability. Publisher wording describes observation in a subdomain, not a finite set of boundary sensors. | An inverse source is not initial internal memory; its techniques and exact measurement setting need full-text verification. |
| Wu & Liu, 2012, [unknown source in thermoelasticity with memory](https://iopscience.iop.org/article/10.1088/0266-5611/28/9/095012) | Publisher-linked record and [abstract](https://www.osti.gov/etdeweb/biblio/22214592) only: spatial source, displacement measurement in a subdomain, source known near boundary, sufficiently long observation; stated Hölder stability. | Very close coupled memory/inverse-source prior art. It is not verified to answer A–C, and detailed assumptions are unavailable here. |
| Avdonin, Ivanov & Wang, [inverse problems for heat equation with memory](https://arxiv.org/html/1612.02129), arXiv:1612.02129v2 | Open preprint introduction and model inspected: 1-D Gurtin–Pipkin equation, zero initial temperature, Dirichlet-to-Neumann response operator and kernel recovery under conditions. | Kernel identification is different from recovering \(z_0\); nonetheless a serious warning against claiming boundary memory inversion is new. Pandolfi and Cavaterra–Guidetti in the focused audit similarly identify kernels under specified assumptions. |
| Charlès & Le Cam, 2020, [thermomechanical parameter identification](https://univ-rennes.hal.science/hal-02469675/document) | Open manuscript abstract/introduction: measured thermal and kinematic fields, known thermophysical coefficients and chosen hyperelastic model. | Practical heat-source reconstruction is established; A–C instead assume model parameters known and seek initial memory. Different target alone does not prove novelty. |
| Amendola, Fabrizio & Golden, 2012, [book](https://link.springer.com/book/10.1007/978-1-4614-1692-0) | Publisher overview only, including thermoelastic memory controllability and inverse problems; chapters not obtained. | Essential unresolved overlap. Full-text access and related citations are prerequisites to any originality assessment. |

The 2004 article's publisher/PDF DOI discrepancy is documented in the focused audit and is not resolved here. Existing theory already covers broad minimal-state, dissipation, thermal-memory and viscoelastic-observability concepts. **No inspected source has been verified to prove or disprove the exact finite-port nonlinear initial-state maps A, B or C**, but this is a statement about inspection, not evidence that these maps are unsolved. Boundary observations do not become original simply by differing from all-process material response.

## 8. Comparative assessment

| Criterion | A: quasistatic 1-D | B: dynamic 1-D | C: dynamic 3-D |
|---|---|---|---|
| Tractability | Highest of the three, but nonlinear heat and nonlocal equilibrium remain | Moderate/low: coupled wave–heat plus memory | Lowest: vector/tensor fields and finite patch integrals |
| Physical relevance | Slow tests on a thin, thermally controlled bar | Transient vibrations with clamped ends | Three-dimensional specimen; difficult preparation and instrumentation |
| Primary literature | Good open memory/work and inverse sources; important book and minimal-state details inaccessible | Strong open wave-observability source; closest thermoelastic inverse sources abstract-only | Open wave and plate papers; key coupled inverse/controllability literature incomplete |
| Uniqueness/non-uniqueness potential | A definite field-to-three-trace map can be tested analytically; neither outcome established | Wave visibility and heat may distinguish or conceal memory; neither outcome established | Symmetry and patch averaging suggest a possible obstruction, but none is demonstrated |
| Analytical proof feasibility | Relatively best; forward positive-temperature theory and nonlinear inverse analysis still significant | Harder due to wave geometry/time and trace regularity | Poorer: spectral multiplicities, tensor modes and partial measurements |
| Routine inverse-problem risk | High | High | High despite technical difficulty |
| Duplication of minimal-state/observability | High; FGG and Carillo are especially close conceptually | Very high; known viscoelastic wave and thermoelastic inverse-source results | Very high; 3-D observability and memory controllability literature |
| Potential scientific significance | Clear negative or positive answer could clarify a concrete controlled bar experiment, conditional on overlap check | Could clarify dynamic preparation, subject to strong assumptions | Could matter for realistic spatial sensing, but finite ports and preparation may render it inaccessible |

A is recommended **only as a possible future question**, not as a demonstrated research gap. Its advantage is focus: one unknown memory field, known thermal initial state, explicitly measured force and two heat fluxes, and a fully stated admissibility/uniqueness target. It remains possible that existing theorems settle it, that the measurement map has a simple symmetry obstruction, or that the forward admissible class is too restrictive. Prior to any investigation, obtain the inaccessible 2006 minimal-state paper, the relevant 2012 book chapters and the inverse-source papers; compare exact variables, initial histories, observation operators, horizon, geometry and norms. If these already settle A or its sensors cannot be realized, stop rather than force a theory. Dr. Gupta retains the final decision.
