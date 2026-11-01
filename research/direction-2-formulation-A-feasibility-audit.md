# Formulation A: mathematical feasibility and prior-art audit

**Date:** 1 November 2026
**Decision: REFORMULATE**

## 1. Executive decision and scope

The frozen equations have a coherent formal thermodynamic structure, and their quasistatic mechanical constraint can be eliminated exactly. However, the inverse map is not yet a rigorously defined nontrivial map on the stated admissible class: the previous specification explicitly *assumed* forward existence, uniqueness, regularity and \(\theta\ge\theta_*/2\), without proving a nontrivial admissible class for the active experiment. If classical regularity is intended at the initial boundary corners, generic \(H^2\) data violate additional compatibility conditions derived below. If weaker solutions are intended, their existence, positive-temperature bounds and delayed heat-flux traces have not been established. This is a correctable specification weakness, not an inconsistency in the balance laws and not a proof that the experiment has no solutions.

**Injectivity remains unresolved.** No pair of distinct admissible initial states giving identical three traces for the frozen positive-parameter, nonzero-loading problem has been constructed, and no uniqueness or stability theorem is proved. A genuine sign-ambiguity example exists in a *different*, explicitly identified limiting problem, but it is not a counterexample to Formulation A. Reflection exchanges the two labeled calorimeters rather than automatically preserving the observation vector. The most important unresolved obstacle is to establish a nonempty forward solution class with usable observation traces and then determine whether the linearized and nonlinear memory-to-flux map has a nullspace. The nearest literature has not been checked exhaustively and some priority sources remain inaccessible, so neither an existing complete solution nor novelty is established.

The prior record was read in full: README and all six listed research reports (the directive enumerates seven files including README). Direction 1 remains rejected as a foundational continuum theory; Direction 2 remains reformulated. This is Arena's independent re-derivation of the equations, not a certification by a separately operating auditor. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. No independent review by ChatGPT is implied.

## 2. Frozen problem, conventions and units

Let \(x\in(0,L)\), \(A_0>0\), \(a,k,\lambda,c,\kappa,\theta_*>0\), and \(b\ne0\) be fixed and known; the sign of \(b\) is not prescribed. Let

\[
\begin{gathered}
\sigma_x=0,\qquad \varepsilon=u_x,\qquad
\sigma=(a+k)\varepsilon-b(\theta-\theta_*)-kz,\\
z_t=\lambda(\varepsilon-z),\qquad
c\theta_t=\kappa\theta_{xx}-b\theta\varepsilon_t+k\lambda(\varepsilon-z)^2.
\end{gathered}\tag{1}
\]

The imposed data are exactly \(u(0,t)=0\), \(u(L,t)=g(t)=g_*\sin^2(\pi t/T)\) with fixed small nonzero \(g_*\); \(\theta(0,t)=\theta(L,t)=\theta_*\), \(\theta(x,0)=\theta_*\), \(z(x,0)=z_0(x)\), \(T=10/\lambda\), \(\delta=T/100\). The stated bound is the full \(H^2\) norm \(\|z_0\|_{H^2}\le M\); if the directive's vertical bars meant only a seminorm, it would not supply the same compactness or amplitude bound. Denote the input-output map correctly by

\[
F_A:z_0\longmapsto \left(A_0\sigma(t),\ A_0\kappa\theta_x(0,t),\ -A_0\kappa\theta_x(L,t)\right)\big|_{(\delta,T)}. \tag{2}
\]

The directive's displayed arrow \(F_A\mapsto(F_m,Q_0,Q_L)\) is a notation slip, not a change to the experiment. \(Q_0,Q_L\) are **outward** heat powers; the thermal supply into the bar is \(-Q_0-Q_L\). Exact continuous-time data are idealized. The result below concerns the class described in the specification: initial \(H^2\) data for which a unique sufficiently regular positive-temperature solution exists and \(\theta\ge\theta_*/2\). That class is defined conditionally, not shown to equal the full ball or to be closed in \(L^2\).

**Units.** With reference-volume energy \(J/m^3=\mathrm{Pa}\), \(x,L,u,g\) have units m, \(\varepsilon,z\) are dimensionless, \(\theta,\theta_*\) are K, \(\sigma,a,k\) are Pa, \(b,c\) are Pa/K, \(\lambda\) is s⁻¹, and \(\kappa\) is W/(m K). The free energy and internal energy are Pa; entropy density is Pa/K; heat flux \(q=-\kappa\theta_x\) is W/m². In (1), \(c\theta_t\), \(\kappa\theta_{xx}\), \(b\theta\varepsilon_t\), and \(k\lambda(\varepsilon-z)^2\) are all Pa/s. Each local entropy-balance term has units Pa/(K s). \(F_m\) is N and \(Q_0,Q_L\) are W. \(A_0\int e\,dx\) is J; \(F_m g'\) and \(Q_i\) are W. These are small-strain, reference-area conventions, not a finite-deformation result.

## 3. Independent thermodynamic check

For \(\theta>0\), the specified Helmholtz free energy per reference volume is

\[
\psi=\frac a2\varepsilon^2-b(\theta-\theta_*)\varepsilon
+c[\theta-\theta_*-\theta\ln(\theta/\theta_*)]
+\frac k2(\varepsilon-z)^2.\tag{3}
\]

Direct differentiation gives

\[
\sigma=\psi_\varepsilon=a\varepsilon-b(\theta-\theta_*)+k(\varepsilon-z),\qquad
\eta=-\psi_\theta=b\varepsilon+c\ln(\theta/\theta_*),
\]

and \(\psi_z=-k(\varepsilon-z)\). The physical internal energy \(e=\psi+\theta\eta\) is

\[
e=\frac a2\varepsilon^2+\frac k2(\varepsilon-z)^2+b\theta_*\varepsilon+c(\theta-\theta_*).\tag{4}
\]

Write \(w=\varepsilon-z\). Since \(z_t=\lambda w\),

\[
e_t=(a\varepsilon+kw+b\theta_*)\varepsilon_t-k\lambda w^2+c\theta_t
=\sigma\varepsilon_t+b\theta\varepsilon_t-k\lambda w^2+c\theta_t.
\]

Substituting the thermal balance yields \(e_t=\sigma\varepsilon_t+\kappa\theta_{xx}=\sigma\varepsilon_t-q_x\), the local first law, with \(q=-\kappa\theta_x\). Conversely this first law plus (3) and the constitutive laws yields the thermal equation in (1). Using \(\eta_t=b\varepsilon_t+c\theta_t/\theta\),

\[
\eta_t+(q/\theta)_x=\frac{k\lambda w^2}{\theta}+\frac{\kappa\theta_x^2}{\theta^2}\ge0.\tag{5}
\]

Thus the production is nonnegative for smooth positive-temperature solutions. Heat supply, entropy flux, internal energy, Helmholtz energy and minimum available storage are distinct. No unique minimum-storage statement is implied by (3)–(5).

Integrate \(e_t=\sigma u_{xt}-q_x\) over the bar. As \(\sigma_x=0\), \(u_t(0,t)=0\) and \(u_t(L,t)=g'(t)\),

\[
\frac{d}{dt}\left[A_0\int_0^L e\,dx\right]
=A_0\sigma g'+A_0[q(0)-q(L)]
=F_m g'-Q_0-Q_L.\tag{6}
\]

Thus \(F_m g'\) is mechanical power **supplied to** the body; outward heat powers are \(Q_0=A_0q(0)(-1)\) and \(Q_L=A_0q(L)\). The integral of (5) contains entropy supply \(-Q_0/\theta_*-Q_L/\theta_*\), not entropy production. These identities are formal for sufficiently regular solutions and do not prove forward existence or positivity.

## 4. Exact reduction of the forward and inverse maps

Set \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(m(t)=g(t)/L\); denote spatial averages by an overbar. Integration of \(u_x\) gives \(\bar\varepsilon=m\). Spatially uniform stress, integrated over the bar, gives

\[
\sigma=Dm-b(\bar\theta-\theta_*)-k\bar z,\qquad
\varepsilon=m+r(z-\bar z)+\beta(\theta-\bar\theta).\tag{7}
\]

This uniquely determines \(\varepsilon\) from \(z,\theta,g\) because \(D>0\), and then \(u(x,t)=\int_0^x\varepsilon(y,t)dy\) satisfies both displacement boundary conditions. No additional mechanical initial condition is needed.

Averaging \(z_t=\lambda(\varepsilon-z)\) gives

\[
\bar z_t=\lambda(m-\bar z),\quad
\bar z(t)=e^{-\lambda t}\bar z_0+\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds.\tag{8}
\]

For \(p=z-\bar z\), \(v=\theta-\bar\theta\), \(\mu=\lambda\alpha\),

\[
p_t=-\mu p+\lambda\beta v,\qquad
p(x,t)=e^{-\mu t}p_0(x)+\lambda\beta\int_0^t e^{-\mu(t-s)}v(x,s)ds,\quad p_0=z_0-\bar z_0.\tag{9}
\]

This is equivalent to the original integrating factor formula \(z=e^{-\lambda t}z_0+\lambda\int_0^t e^{-\lambda(t-s)}\varepsilon(s)ds\). The local mismatch and strain rate become

\[
w=\varepsilon-z=m-\bar z-\alpha p+\beta v,\qquad
\varepsilon_t=m'+r(-\mu p+\lambda\beta v)+\beta(\theta_t-\overline{\theta_t}).\tag{10}
\]

Consequently the thermal equation, exactly, is

\[
(c+d\theta)\theta_t-d\theta\overline{\theta_t}
=\kappa\theta_{xx}-b\theta[m'+r(-\mu p+\lambda\beta v)]
+k\lambda[m-\bar z-\alpha p+\beta v]^2=:H,\quad d=b^2/D.\tag{11}
\]

The initial and boundary temperatures are unchanged, and \(p,\bar z\) are given by (8)–(9). This is a nonlinear parabolic–Volterra equation with spatial means, a quadratic dissipative source, multiplication by temperature, and a rank-one nonlocal term in \(\theta_t\). For positive \(\theta\), \(C(x,t)=c+d\theta>0\), and (11) can also be explicitly solved for the mean time derivative:

\[
\overline{\theta_t}=\frac{\overline{H/C}}{1-\overline{d\theta/C}}
=\frac{\overline{H/C}}{\overline{c/C}},\qquad
\theta_t=\frac{H+d\theta\,\overline{\theta_t}}{C}.\tag{12}
\]

The denominator is strictly positive for positive bounded \(\theta\). This algebraic inversion does not prove parabolic well-posedness or justify traces. Once the reduced solution \(\theta[z_0]\) exists, (7)–(9) give explicit **solution-dependent functionals**:

\[
F_m=A_0\{Dm-b(\bar\theta[z_0]-\theta_*)-k\bar z[z_0]\},\quad
Q_0=A_0\kappa\partial_x\theta[z_0](0,t),\quad
Q_L=-A_0\kappa\partial_x\theta[z_0](L,t).\tag{13}
\]

These do not furnish a closed formula in \(z_0\) without solving (11), and do not imply injectivity.

## 5. Initial equilibrium, compatibility, positivity and existence

At \(t=0\), \(m(0)=m'(0)=0\), \(\theta=\theta_*\), and (7) yields

\[
\sigma(0)=-k\bar z_0,\qquad
\varepsilon_0=r(z_0-\bar z_0),\qquad
u_0(x)=r\int_0^x(z_0(y)-\bar z_0)dy.\tag{14}
\]

Both displacement values are zero. Every \(H^2\) initial \(z_0\) therefore has a unique compatible initial quasistatic strain/displacement, and its possible nonzero strain is not a contradiction. The uniformly prescribed initial temperature matches both bath values. This does **not** establish higher-order compatibility or reachability by an actual preparation history.

If, in addition, \(\theta_t,\theta_{xx}\) extend continuously to the initial corners and the PDE holds there, the fixed boundary temperatures require \(\theta_t(0,0)=\theta_t(L,0)=0\). Since the initial temperature is constant, \(\theta_{xx}(x,0)=0\), \(v(x,0)=0\). Put \(p_0=z_0-\bar z_0\), \(w_0=-\bar z_0-\alpha p_0\), and \(C_*=c+d\theta_*\). From (11),

\[
c\overline{\theta_t}(0)=k\lambda\overline{w_0^2},\qquad
C_*\theta_t(x,0)=b\theta_*r\mu p_0(x)+k\lambda w_0(x)^2+d\theta_*\overline{\theta_t}(0).\tag{15}
\]

Thus the right-hand side must vanish at **both endpoints** for that classical solution class. For a nonzero constant \(z_0=s\), \(p_0=0\) and \(\overline{\theta_t}=k\lambda s^2/c\), so the endpoint right-hand side is \(k\lambda s^2(1+d\theta_*/c)>0\). Such an \(H^2\) datum violates the stated corner regularity, although it may admit an initial-layer/weak solution; this is not proof it is physically impossible. The positive observation delay avoids measuring at the corners but does not itself establish existence or \(L^2\) flux traces.

The corner conditions are not formally limited to zero data. To see this, let \(z_0=p_0=s\sin(2\pi x/L)+h\cos(2\pi x/L)\), which has mean zero and the same endpoint value \(h\). Equation (15) reduces at both ends to

\[
G(s,h)=b\theta_*r\mu h+k\lambda\alpha^2\left[h^2+\frac{d\theta_*}{2c}(s^2+h^2)\right]=0.\tag{16}
\]

Here \(G(0,0)=0\) and \(\partial_hG(0,0)=b\theta_*r\mu\ne0\). The elementary implicit-function theorem gives a smooth \(h(s)=O(s^2)\) for sufficiently small \(s\), yielding nonzero \(H^2\) fields satisfying this **first** corner condition and any prescribed positive norm bound by taking \(s\) small. This establishes nontrivial formal compatibility only, not existence, higher compatibility, temperature bound or a nonempty solution-defined admissible class for the active experiment.

For a given classical solution with bounded \(\varepsilon_t\), the thermal equation is

\[
\theta_t-(\kappa/c)\theta_{xx}+(b/c)\varepsilon_t\theta=(k\lambda/c)w^2\ge0.\tag{17}
\]

A standard maximum-principle comparison with \(\theta_*e^{-Bt}\), \(B=\|b\varepsilon_t/c\|_{L^\infty}\), shows \(\theta\ge\theta_*e^{-Bt}>0\) on the cylinder, provided the needed smoothness and bounded coefficient hold. This bound does **not** guarantee \(\theta\ge\theta_*/2\) on \([0,T]\) unless \(BT\le\ln2\), and does not itself bound \(\varepsilon_t\) or prove the coupled solution exists. In particular, relaxation heating alone does not remove the need to control the reversible coupling.

Forward existence/uniqueness in a specified function space, data-to-solution continuity, positivity through the finite horizon, admissible preparation, and the endpoint flux trace in \(L^2(\delta,T)\) remain **unproved**. The earlier planning report carefully made these assumptions; its phrase that an equilibrium state is included for *zero actuation* does not prove nonemptiness for the frozen nonzero \(g_*\). A later choice between classical compatible data and a rigorously defined weak/mild setting would be a clarification, not a silent change to the frozen physics.

## 6. Injectivity and obstruction tests

### 6.1 What the data provably contain

Equations (8) and (13) show that mechanical equilibrium discards spatial information directly: the force depends only on \(\bar z_0\) and \(\bar\theta(t)\), not directly on \(p_0(x)\). This is **not** an automatic nullspace of the full map, because both heat fluxes and \(\bar\theta\) can depend on \(p_0\) through (9)–(11). Likewise each calorimeter observes a boundary derivative of a solution with an interior source; two time traces can encode infinitely many modes. The spatial averaging alone does not prove non-uniqueness.

The force relation determines \(b(\bar\theta-\theta_*)+k\bar z\), not its two components separately, from force alone. Integrating the heat equation gives a relation involving \(Q_0+Q_L\), but the unknown internal work/temperature terms do not turn it into direct local state measurement. The delay \(\delta>0\) removes the earliest data and may aggravate stability; without an analyticity or backward-uniqueness result it cannot be assumed either to preserve or destroy injectivity. Differences of nonlinear solutions do not obey a closed scalar homogeneous heat equation, so standard scalar Cauchy uniqueness cannot be applied blindly.

### 6.2 Sign and reflection: conditions rather than invented counterexamples

The quadratic heat term by itself does not determine the sign of \(w\); nevertheless the full equation also includes \(-b\theta\varepsilon_t\), the imposed \(m(t)\), and the heat/strain feedback. A sign flip of \(z_0\) generally changes these terms, the force and/or the labeled fluxes. It is a **possible** ambiguity mechanism, not a counterexample for the frozen experiment.

Reflection \(R f(x)=f(L-x)\) preserves the reduced equations and the imposed temperatures and end displacement. If the forward problem is unique, reflection maps the data as

\[
F_A(Rz_0)=(F_m(z_0),Q_L(z_0),Q_0(z_0)).\tag{18}
\]

Proof: spatial means and \(m\) are unchanged, \(\theta^R=R\theta\), \(z^R=Rz\), and derivatives acquire a minus sign. Reflecting strain and integrating from the left gives the same end values for \(u\). Hence reflection is an **exact transformation**, but provides identical labeled data only when \(Q_0=Q_L\). No nonsymmetric admissible initial profile satisfying that equality over the whole observation interval has been established. Relabeling or summing sensors would be a different experiment and is not used here.

A further necessary-condition check illustrates the coupling. Suppose two solutions have the same **entire temperature field**, not merely boundary data, and the same mean \(z_0\). Then \(\Delta p=e^{-\mu t}\Delta p_0\). Subtracting (11) gives pointwise

\[
0=\alpha\lambda\Delta p\,[b r\theta-k(w+\widetilde w)].\tag{19}
\]

For nonzero \(\Delta p\), one must have \(w+\widetilde w=\beta\theta\). In particular, at \(t=0\), for such points, \(-2\bar z_0-\alpha(p_0+\widetilde p_0)=\beta\theta_*\). Equation (19) is necessary only under the stronger same-temperature assumption; it neither proves nor disproves equality of boundary observations. It shows why flipping a quadratic term in isolation is insufficient.

### 6.3 Rigorous counterexample only in an excluded limiting experiment

The following calculation is a diagnostic **outside** the frozen hypotheses: set \(b=0\) and also set \(g_*=0\), both changes explicitly forbidden in the main problem. Let \(h\in H^2(0,L)\) be nonzero with zero spatial mean, and take \(z_0^{\pm}=\pm h\). Assuming the linear heat problem is solved in a suitable weak class, (7)–(9) give \(\sigma^\pm=0\), \(z^\pm=\pm e^{-\mu t}h\), \(\varepsilon^\pm=\pm r e^{-\mu t}h\), \(w^\pm=\mp\alpha e^{-\mu t}h\). Both temperatures solve exactly the same Dirichlet heat problem with initial \(\theta_*\) and source \(k\lambda\alpha^2e^{-2\mu t}h^2\), so their force and both heat fluxes coincide while \(z_0^+\ne z_0^-\). Standard linear heat uniqueness applies in its chosen weak class. This does not prove a counterexample for nonzero \(b\) and nonzero \(g_*\); nor does it establish that the stricter classical-corner admissibility condition holds for arbitrary \(h\). Degenerate \(k=0\), \(a=0\), or \(\lambda=0\) would likewise leave the frozen class and are not used to defeat it.

**Current conclusion:** no rigorous non-uniqueness result or proof of injectivity has been established for (1)–(2). The particular positive parameters, \(g_*\), \(M\), and admissible regularity affect the answer. A limiting counterexample does not settle them.

## 7. Conditional stability

No Lipschitz, Hölder, logarithmic or other modulus has been established for (2). Thermal diffusion and loss of pre-\(\delta\) observations motivate concern about high spatial frequencies; the state \(p\) itself retains the unsmoothed term \(e^{-\mu t}p_0\), so one cannot simply declare that the *complete* nonlinear map is the heat semigroup or is compact. The quadratic source and multiplication by a nonuniform base state may mix frequencies; whether this preserves, weakens or destroys high-frequency information requires a proof. Failure of a Lipschitz estimate, if proved, would not by itself prove non-injectivity.

A useful **conditional topological fact** is available. Let \(K\) be a genuinely compact subset of \(L^2(0,L)\), and let \(F_A:K\to L^2(\delta,T)^3\) be continuous and injective. Define

\[
\omega(r)=\sup\{\|z-\widetilde z\|_{L^2}:z,\widetilde z\in K,\ \|F_A(z)-F_A(\widetilde z)\|_{L^2}\le r\}.
\]

Then \(\omega(r)\to0\) as \(r\downarrow0\). Indeed, otherwise there are pairs with output differences tending to zero and state differences at least some \(\epsilon>0\); compactness yields subsequences converging in \(L^2\), continuity gives equal limiting outputs, and injectivity makes the limiting states equal, a contradiction. Thus a uniform conditional modulus exists *under those assumptions*, without giving a rate. A closed bounded \(H^2\) ball is relatively compact in \(L^2\); but the specification's subset defined through existence and the \(\theta_*/2\) bound is **not shown closed in \(L^2\)**, and continuity and injectivity of \(F_A\) are not proved. One cannot apply the fact to the actual class without these missing steps. Even compactness plus injectivity alone gives no justified Lipschitz, Hölder or logarithmic rate.

A credible conditional route is to linearize (8)–(13) about an actually existing smooth positive base solution, keeping the fixed nonzero loading and both flux traces, and analyze the resulting nonlocal parabolic–ODE observation operator. Its nullspace is a necessary diagnostic: a nontrivial derivative nullspace alone would not prove nonlinear non-injectivity, and injectivity of the derivative alone would not prove global nonlinear injectivity. A smoothing/compactness estimate for that operator on specified spaces could test Lipschitz stability; neither such estimate nor its required forward differentiability is established here.

## 8. Focused prior-art and source-access ledger

Targeted renewed searches addressed *initial* relaxation/internal-variable recovery, nonlinear parabolic source recovery from fluxes, and full-text access to the specifically requested papers. This is a citation/reference follow-up, not an exhaustive search. Table fields marked **unavailable** are not inferred from abstracts.

| Primary source and access | Equations, unknowns, conditions, measurement and time actually checked | Result / relevance to A |
|---|---|---|
| Deseri, Fabrizio & Golden (2006), [minimal state](https://link.springer.com/article/10.1007/s00205-005-0406-1). Direct publisher PDF request returned subscription preview; alternate focused search did not yield a verified full text. | Abstract identifies linear viscoelasticity, stress-response minimal state and an IBVP. Exact PDE, initial/boundary assumptions, measurements and time interval **unavailable**. | Abstract reports free-energy and evolution results, but exact uniqueness/stability hypotheses cannot be audited. It does not verify or rule out A's boundary inverse map. |
| Amendola–Fabrizio–Golden (2012), [book](https://link.springer.com/book/10.1007/978-1-4614-1692-0), [chapter 19](https://link.springer.com/chapter/10.1007/978-1-4614-1692-0_19). Publisher book and chapter previews only. | Chapter 19 is “Controllability of Thermoelastic Systems with Memory,” pp. 419–437; book overview also lists inverse problems. Exact equations, unknowns, data, time and theorem conditions **unavailable**. | Direct overlap remains unresolved; controllability is not automatically A's observability. Publisher full chapter is subscription-restricted. |
| Fabrizio–Gentili–Golden (2004), [nonisothermal free energies](https://www.sciencedirect.com/science/article/pii/S089571770490009X). Full publisher PDF §§2–3 inspected; source identifier discrepancy remains as documented in the focused audit. | Material-point current deformation/coldness and histories; generalized response includes weighted stress and internal energy; work integral over all admissible process continuations, closed under restriction/concatenation. Not an endpoint-sensor IBVP; no fixed A-type observation interval. | Proposition 3.1 gives response/work equivalence with equal present fields; Theorem 3.2 gives minimum scaled free energy under the paper's strong dissipation/zero-state assumptions, citing an earlier proof. Does not establish A injectivity or stability. |
| Carillo (2005), [heat conduction and viscoelasticity](https://www.atlantis-press.com/article/488.pdf), full PDF selected §§1–3. | Rigid conductor with \(e=\alpha_0(\theta-\theta_0)\), heat flux from a temperature-gradient-history convolution, with \(k\in L^1\), \(k'\in L^1\cap L^2\); current temperature and integrated history represent the state. All admissible process continuations, rather than boundary calorimeter traces over A's time interval. | The paper states response/work equivalence in its model; it compares isothermal viscoelasticity. It does not prove A's finite-time inverse result. Some PDF formula rendering is imperfect. |
| Green, Liu & Mitkovski (2019), [boundary observability](https://www.math.wustl.edu/~awgreen/files/papers/visco-control-siamjco-2020.pdf), full primary PDF §1 inspected. | \(w_{tt}-\Delta w=\int_0^t M(t-s)\Delta w(s)ds\), \(M\in H^2(0,T)\); \(w_0\in H^1_0\), \(w_1\in L^2\), zero Dirichlet boundary; normal derivative on a geometric boundary part during \((0,T)\). Unknown initial wave displacement/velocity, not a separate arbitrary prehistory field. | Establishes a boundary observability inequality under its stated geometric/time conditions. Does not directly settle quasistatic thermoelastic A or its nonlinear heat traces. Full proof not independently checked. |
| Bellassoued & Yamamoto (2011), [thermoelastic inverse source](https://iopscience.iop.org/article/10.1088/0266-5611/27/1/015006), subscription abstract only; alternate full-text search unsuccessful. | Abstract identifies a bounded isotropic linear Lamé–heat system, zero surface displacement, unknown heat source and a stated displacement/traction-related observation in a subdomain over sufficiently large time. Publisher abstract is ambiguous about precise measurement wording. Exact PDE, initial data, observation operator and threshold time **unavailable**. | Abstract reports Hölder stability; no exact theorem or assumptions inferred. A's unknown is initial mechanical memory, not a prescribed heat source. |
| Wu & Liu (2012), [thermoelastic inverse source with memory](https://iopscience.iop.org/article/10.1088/0266-5611/28/9/095012), publisher abstract only; full access unavailable. | Abstract: spatially varying source known near boundary; coupled hyperbolic thermoelastic system with memory; displacement measured in an interior subdomain for sufficiently long time. Exact PDE, initial and boundary conditions, observation norms and threshold **unavailable**. | Abstract reports Hölder stability and uniqueness for that source, not A's initial field. No original theorem statement inferred. |
| Slodička (2014), [nonlinear inverse sources](https://www.tandfonline.com/doi/pdf/10.1080/17415977.2013.823418), accessible full PDF, introduction and Theorem 2.1 inspected. | \(u_t+Lu=f(x)+h(x,t)+\int_0^t g(u(x,s))ds\), prescribed Dirichlet and known initial value, with unknown spatial source \(f\); measurement is the **whole interior final field** \(u(\cdot,T)\), \(T>0\). Theorem 2.1 uses uniformly elliptic time-independent symmetric \(L\), stated data spaces and \(g'\ge0\). | At most one spatial source under those conditions; no stated boundary-flux result or A-specific stability. Demonstrates strong prior work on nonlinear parabolic memory/source inversion but does not settle A. |
| Lin, Z. Zhang & Z. Zhang, [linear parabolic sparse flux inverse source](https://arxiv.org/html/2111.02285), arXiv:2111.02285v1, model and Theorem 1 inspected. | \((\partial_t+\mathcal A)u=\sum p_k(x)\mathbf1_{[t_{k-1},t_k)}\), homogeneous initial and Dirichlet data, symmetric uniformly elliptic \(\mathcal A\); flux on an open boundary subset for \((0,\infty)\). Source changes and nonzero coefficients satisfy Assumption 1.1, plus additional source regularity Assumption 2.4. | Theorem 1 states uniqueness within this semi-discrete source class and those assumptions. It is linear, uses infinite-time observations and does not supply A's nonlinear finite-time memory-state theorem. Exact stability not independently audited. |
| Fabrizio, Giorgi & Pata, [A new approach to equations with memory](https://arxiv.org/html/0901.4063), 2009 preprint, abstract and introduction inspected; found by following citations to Deseri et al. | Abstract viscoelastic equation \(u_{tt}-\Delta[G(0)u+\int_0^\infty G'(s)u(t-s)ds]=0\) for nonincreasing convex \(G\); history is given for negative times; discusses trajectories for all positive times. Exact boundary observation setting is not A. | Minimal-state and initial-history distinguishability have extensive direct prior art. Introduction does not prove finite-port injectivity in A; detailed theorems not independently audited. |
| Egger, Engl & Klibanov, [nonlinear parabolic source](https://iopscience.iop.org/article/10.1088/0266-5611/21/1/017), publisher abstract only, identified from nearby inverse-source citations. | Semilinear parabolic equation with known initial and Dirichlet data, unknown scalar nonlinearity \(q(\cdot)\) known on the initial-data range, Neumann data. Exact PDE, time interval and full assumptions unavailable in the abstract rendering. | Abstract reports uniqueness and Hölder stability under its own conditions; not initial-memory recovery and not verified as an A theorem. |

No inspected source has been shown to settle precisely (1)–(2). This is an access-limited finding, not evidence the question is new or unsolved. The detailed Deseri 2006 paper, relevant 2012 book chapters, and both thermoelastic inverse-source papers are the most consequential unavailable sources. Other records and searches do not substitute for their original equations and theorem hypotheses.

## 9. Remaining obstacles and final recommendation

1. Specify the actual forward regularity and prove existence, uniqueness, positive-temperature and delayed flux traces for a nonempty class under the **unchanged** active experiment. Resolve corner compatibility versus initial layers; check whether \(\theta\ge\theta_*/2\) follows from explicit data bounds.
2. Determine how admissible preparations relate to the assumed memory state, rather than asserting an arbitrary history is physically realizable.
3. With that class fixed, investigate the nonlinear observation operator and its derivative, including labeled reflection, nonlinear sign effects, finite observation delay and rank-one spatial coupling. An exact counterexample or an injectivity proof must use the strictly positive parameters and nonzero loading.
4. If injectivity is obtained, determine the topology and compactness of the *actual* admissible class, continuity of the map and, separately, any quantitative stability. Noise and finite sensor bandwidth are absent from ideal exact data.
5. Obtain missing full texts and follow their references and citations for boundary observability of initial memory and related inverse heat sources before claiming a new result.

**Recommendation to Dr. Vipin Gupta: REFORMULATE the mathematical admissibility/forward-solution specification before considering further inverse analysis.** The equations and sensors need not be changed to make that clarification. The present audit neither proves the problem impossible nor authorizes a research programme, new continuum theory, simulation or manuscript. Final decision rests with Dr. Gupta.
