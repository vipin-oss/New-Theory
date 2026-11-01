# Alternative-candidate discovery audit — in progress

The Direction 2 finite-prior result passes a conditional proof gate but, in light of the general prior nonlinear theorem and routine perturbation method, does not pass a demonstrated breakthrough/novelty gate. The following are **alternative research problems**, not changes to the frozen Direction 2 experiment, and are not a new foundational continuum theory. These are screening comparisons, not exhaustive literature clearance. Arena is the builder; this is not independent human certification. Five genuinely different candidates are evaluated, and candidate 1 is actually pursued in §6. No publication recommendation or invented experimental data are provided.

## 1. Hidden distributed relaxation states: exact boundary nonuniqueness

**Equations/unknown.** On \(I=(0,L)\), rates \(r\in[a,b]\), \(0<a<b\), study
\[u_t-\kappa u_{xx}=\int_a^bp(t,x,r)\,dr,\quad p_t=-rp+\gamma u,\quad u|_{x=0,L}=0,\quad u(0,x)=0,\ p(0,x,r)=h(x,r),\]
with \(\kappa>0\), \(\gamma\ne0\), and \(h\in L^2(I\times[a,b])\). Observe both \(u_x(0,\cdot),u_x(L,\cdot)\) on any open \((\delta,T)\). The unknown is the fully distributed signed internal state, not the material kernel. Objective: construct an exact invisible nonzero \(h\), including its pre-delay response, and decide if it is compatible with a chosen realizable history class.

**Prior comparison.** [arXiv:0806.0965](https://arxiv.org/html/0806.0965), equations (1.1) and initial conditions, develops a history-space formulation for a *plate* with distinct hereditary terms and shows history can affect stability. [arXiv:2506.22221](https://arxiv.org/html/2506.22221), §§1,3, studies observability/controllability of a different spatial-memory/delay model. [arXiv:2604.11464](https://arxiv.org/html/2604.11464), §§2,4, explicitly represents passive relaxation spectra, but not this boundary initial-state inverse question. General hidden-state and realization nonuniqueness are established themes. Exact overlap with a distributed-state boundary nullspace has **not** been excluded.

**Proof strategy/obstruction.** Construct a compactly supported spatial field and use a continuous superposition of exponentials whose spectral density is selected by the PDE and ODE. A nontrivial cancellation is necessary because ODE feedback generates additional spectral density; one cannot just prescribe \(p=e^{-rt}h\) when \(\gamma\ne0\). §6 provides an exact construction. \(h\in L^2\) is not automatically the reachable state of a specified prehistory; this is the key physical limitation.

**Significance / feasibility / gate.** Infinite-dimensional hidden internal-state ambiguity would be relevant to inverse memory measurements, but prior art and the admissible prehistory constraint are decisive. A mathematical construction is feasible; publication-level novelty and physical realizability remain **UNRESOLVED**.

## 2. Gradient-interface elasticity with partial-access shape data

**Equations/unknown.** In a bounded elastic body with inclusion \(D\), use antiplane equilibrium \(\nabla\cdot(\mu\nabla u)=0\) in each phase, continuity of \(u\), and the interface jump determined variationally by \(\int_{\partial D}[\mu_s|\nabla_su|^2+\ell_s^2\mu_s|\nabla_s^2u|^2]/2\). Prescribe exterior displacement on an open boundary patch and measure exterior traction on a (possibly disjoint) patch. Unknown: \(D\) and interface parameters. Objective: a precise partial-data uniqueness or counterexample theorem for the variational interface operator, with a clearly stated geometry and regularity.

**Prior.** [arXiv:2509.15171](https://arxiv.org/html/2509.15171), §§1,4–5, derives a higher-order interface energy and proves parameter and shape recovery from the full exterior Dirichlet-to-Neumann map. Extending merely to an added coefficient is not enough. A genuine gap would have to be proved for partial-access geometry, not inferred from the full-data statement.

**Strategy/obstruction.** Runge approximation for the transmission operator and a partial-data factorization method; higher-order surface nullspace and patch-to-interface density are the obstacles. Feasibility moderate-to-low without a primary UC theorem adapted to the surface transmission problem. Importance: interfacial characterization. Novelty **UNVERIFIED**; no claim of a positive theorem. Potential requires a genuinely new partial-data result.

## 3. Semiconductor inverse doping with disjoint contacts

**Equations/unknown.** Use the stationary drift–diffusion–Poisson system in [arXiv:2011.12200](https://arxiv.org/html/2011.12200), equation (1): \(\lambda_D^2\Delta V=\delta_D^2(e^Vu-e^{-V}v)-C(x)\), \(\operatorname{div}J_n=\delta_D^4Q(V,u,v,x)(uv-1)\), \(\operatorname{div}J_p=-\delta_D^4Q(V,u,v,x)(uv-1)\), with their contact and insulation boundary conditions. Unknown \(C(x)\); prescribe voltage on one contact and observe current on a disjoint one. Target: prove exact nonuniqueness or uniqueness for an explicitly defined infinite-dimensional admissible class, not finite numerical rank.

**Prior.** The cited primary work §3 explicitly discusses the identification obstacle for disjoint sub-boundaries and maps related cases to conductivity; [arXiv:2401.04834](https://arxiv.org/html/2401.04834) treats a different kinetic Vlasov–Poisson, incoming/outgoing measurement problem. A source's stated open problem does not guarantee it is still open today.

**Strategy/obstruction.** First analyze the exact linearized voltage-current map and reachable products; any linear kernel is insufficient for nonlinear nonuniqueness. Global uniqueness with one scalar contact current is delicate, and nonlinear continuation/analyticity may fail. High physical relevance, feasibility currently low, exact novelty **UNVERIFIED**, potential only after a new exact theorem and broader prior-art search.

## 4. Thermoviscoelastic plate with inherited histories and singular limits

**Equations/unknown.** The coupled plate and thermal equations and full past histories are precisely (1.1) of [arXiv:0806.0965](https://arxiv.org/html/0806.0965); kernels act on \(\Delta^2u\), temperature and thermal conduction. Seek a theorem characterizing when a memory-kernel singular limit is uniform over a specified bounded history-energy ball, or exhibit an exact family obstructing uniform convergence. Unlike a zero-history approximation, the data include arbitrary initial histories.

**Prior.** The primary paper's §3 derives exponential stability under its thermal-power-memory hypotheses; §4 proves semigroup closeness as kernels fade, with stated assumptions and initial layers. Any proposed rate must be compared line by line to those theorems. A mere restatement of an initial layer is **SUBSUMED**.

**Strategy/obstruction.** Resolvent/spectral lower bounds and concentration of normalized histories on fast memory scales; the natural state spaces themselves vary with the small parameter, so identification maps between them must be fixed before an operator norm claim. Physical relevance is real; feasibility moderate; novelty and precise functional setting **UNRESOLVED**.

## 5. Matrix-valued passive memory with noncommuting couplings

**Equations/unknown.** For \(z(t)\in\mathbb R^m\), \(z=\int_0^tK(t-s)\dot e(s)ds\), and an elastic/thermal system driven by \(z\), let \(K(t)=\int_0^\infty e^{-rt}\,d\boldsymbol\Sigma(r)\) with a finite positive semidefinite matrix-valued measure. Seek an exact characterization of minimal internal-state realizations and their unobservable history subspaces from a restricted boundary port, including noncommuting matrix residues.

**Prior.** [arXiv:2604.11464](https://arxiv.org/html/2604.11464), §§2 and 4, gives scalar Stieltjes/passive realizations and rational approximations. Matrix positive-real realization and operator-valued Bernstein theory are mature: a construction obtained simply by adding matrix coefficients is not a novelty gap. Relevant matrix-valued primary realization theorems still require full-text inspection.

**Strategy/obstruction.** Describe the state space as a direct integral, formulate reachable/observable subspaces and test whether noncommutation obstructs spectral reconstruction; a positive storage identity alone proves neither minimality nor identification. Physical relevance: anisotropic relaxation. Feasibility moderate, novelty **UNVERIFIED**, publication potential depends on an exact unproved characterization rather than model decoration.

## 6. Pursuit of candidate 1: exact invisible state in the alternative model

This is a rigorous construction for the **alternative** two-coordinate state space above, not for the frozen single-internal-variable Direction 2 system. It assumes arbitrary signed \(L^2\) internal initial states, not a demonstrated reachable prehistory.

Choose nonzero \(\rho\in C_c^\infty((a,b))\) with \(\int_a^b\rho(s)ds=0\), and nonzero \(\psi\in C_c^\infty((0,L))\). Set
\[f(t)=\int_a^b e^{-rt}\rho(r)dr,\qquad u(t,x)=\psi(x)f(t).\]
Then \(f(0)=0\), \(u_x(0,t)=u_x(L,t)=0\), and \(f\not\equiv0\) by injectivity of the compact-support Laplace transform. Define for \(r\in(a,b)\)
\[
K_\rho(r)=\operatorname{p.v.}\int_a^b\frac{\rho(r)+\rho(s)}{s-r}ds
=\rho(r)\log\frac{b-r}{r-a}+\operatorname{p.v.}\int_a^b\frac{\rho(s)}{s-r}ds.
\]
\(K_\rho\in L^2(a,b)\): the second term is a finite-interval Hilbert transform of a compactly supported smooth function, and the logarithmic term is bounded on the support of \(\rho\). Define
\[
h(x,r)=-r\rho(r)\psi(x)-\kappa\rho(r)\psi''(x)-\gamma\psi(x)K_\rho(r),\quad
p(t,x,r)=e^{-rt}h(x,r)+\gamma\psi(x)\int_0^te^{-r(t-s)}f(s)ds. \tag{1}
\]
Then \(h\in L^2(I\times[a,b])\), \(p\) solves its ODE with initial value \(h\), and the heat equation is satisfied **exactly**. To verify it, use the identity
\[
\int_a^b\!\int_0^t e^{-r(t-s)}f(s)ds\,dr=\int_a^be^{-rt}K_\rho(r)dr. \tag{2}
\]
Derivation: substitute the Laplace representation of \(f\), integrate in time to obtain \((e^{-st}-e^{-rt})/(r-s)\), remove the diagonal strip \(|r-s|<\varepsilon\), and exchange the finite integrations. Coefficients of \(e^{-rt}\) give the displayed principal value. The original difference quotient is continuous on the diagonal, so the removed-strip error tends to zero. The truncated Hilbert transforms converge in \(L^2\), justifying the limit on the right. From (1)–(2),
\[
\int_a^bp(t,x,r)dr=\int_a^be^{-rt}[-r\rho(r)\psi(x)-\kappa\rho(r)\psi''(x)]dr=u_t-\kappa u_{xx}.
\]
The state \(h\) is nonzero. Indeed if \(h=0\), uniqueness for the homogeneous coupled initial-value problem (standard energy/Gronwall on \(L^2(I)\times L^2(I\times[a,b])\)) would imply \(u=0\), contradicting \(\psi\ne0\) and injectivity of the Laplace transform. Alternatively, at any \(r\) with \(\rho(r)\ne0\), \(h(\cdot,r)=0\) would force the compactly supported nonzero \(\psi\) to solve a constant-coefficient second-order ODE globally, impossible by uniqueness.

Thus this alternative has a nonzero exact invisible distributed state even for both endpoint fluxes and the full time interval. It uses nonzero \(\gamma\), no numerical approximation, and the complete pre-delay evolution. **It does not prove physical nonuniqueness of the frozen Direction 2 system**: the extra rate coordinate and arbitrary signed state are different assumptions. It is also not shown historically novel.

## 7. Selection and next mathematical route

Candidate 1 was selected for its explicit infinite-dimensional state and concrete obstruction; §6 is an actual proof attempt, not just a list. The central unresolved test is whether its \(h\) belongs to the closure or range of a physically specified past-history map such as \(h(x,r)=\gamma\int_{-\infty}^0 e^{rs}v(x,s)ds\) with one common driving history, finite energy, and applicable mechanical/thermal compatibility. Arbitrary \(L^2\) spectral states need not be reachable in that way. Next: derive the exact range and seek either a reachable nonzero invisible state or a proof that this construction is excluded; then inspect primary full-text minimal-state and history-representation literature before any novelty or research-value claim. Candidates 2–5 remain screening-level and require further primary theorem/proof comparison and genuine attempts; they have not reached definitive stopping points.

### Reachability attack on the explicit example

The construction above is **not** reachable from the common finite-energy prehistory \(v\in L^2(({-\infty},0);L^2(I))\) through
\[h_v(x,r)=\gamma\int_{-\infty}^0 e^{rs}v(x,s)ds,\quad r\in[a,b].\]
Indeed \(r\mapsto h_v(\cdot,r)\) is \(L^2(I)\)-valued holomorphic for \(\operatorname{Re}r>0\), by Cauchy–Schwarz and differentiation under the integral (the extra powers of \(|s|\) remain exponentially integrable on compact subsets of that half-plane). Because nonzero compactly supported \(\psi\) and \(\psi''\) are linearly independent in \(L^2(I)\), choose a bounded real linear functional \(\ell\) with \(\ell(\psi)=0\) and \(\ell(\psi'')\ne0\). For the constructed state, \(\ell(h(\cdot,r))=-\kappa\ell(\psi'')\rho(r)\). A holomorphic function on the right half-plane agreeing almost everywhere with a nonzero compactly supported smooth \(\rho\) on \((a,b)\) would vanish on an open subinterval and hence everywhere, contradiction. Thus the example is **REFUTED as a reachable-common-history counterexample** in this particular finite-energy prehistory class. It remains valid for arbitrary distributed initial \(L^2\) state. Other physical prehistory classes must be analyzed separately; this exclusion is not a general identification theorem.

The next materially different approach is candidate 2: derive the partial-boundary Runge identity for the actual gradient-interface variational operator, and either prove the needed density or locate a precise UC barrier. Candidate 1's abstract theorem does not by itself clear the research-value gate.

## 8. Candidate 2 pursued: partial-access interface Runge lemma

The following is a **conditional mathematical lemma for a new alternative model**, not the frozen Direction 2 model and not a claim of novel shape recovery. Let \(\Omega\subset\mathbb R^2\) be bounded connected with smooth boundary, \(D\Subset\Omega\) a smooth simply connected inclusion with \(\Omega\setminus\overline D\) connected, \(\Gamma=\partial D\), and \(\Gamma_c\subset\partial\Omega\) nonempty and relatively open. Take piecewise constant \(\mu_\pm>0\) and constants \(\alpha\ge0,\beta>0\). Work in
\[V=\{v\in H^1(\Omega):v|_\Gamma\in H^2(\Gamma)\},\quad V_0=\{v\in V:v|_{\partial\Omega}=0\},\]
\[a(u,v)=\int_{\Omega\setminus\overline D}\!\mu_+\nabla u\cdot\nabla v+\int_D\!\mu_-\nabla u\cdot\nabla v+\int_\Gamma[\alpha\partial_su\partial_sv+\beta\partial_s^2u\partial_s^2v].\]
The trace from either side agrees because \(u\in H^1(\Omega)\). The surface terms are the variation of the candidate energy; the transmission law is understood weakly, not as an assumed classical fourth-order interface identity. \(a\) is continuous and coercive on \(V_0\): the bulk gradient and exterior Dirichlet Poincaré control \(H^1(\Omega)\), the interface trace controls \(L^2(\Gamma)\), and on the closed smooth curve \(\|g\|_{H^2}\le C(\|g\|_{L^2}+\|\partial_s^2g\|_{L^2})\). For each smooth \(f\) supported in \(\Gamma_c\), choose an extension \(Ef\in V\) supported away from \(\Gamma\) and let \(u_f-Ef\in V_0\) solve \(a(u_f,v)=0\) for all \(v\in V_0\). Lax–Milgram gives a unique solution.

**Lemma.** \(\{u_f|_\Gamma:f\in C_c^\infty(\Gamma_c)\}\) is dense in \(H^2(\Gamma)\).

**Proof.** Suppose \(\ell\in(H^2(\Gamma))'\) annihilates all these traces. By Lax–Milgram, a unique \(w\in V_0\) satisfies \(a(v,w)=\ell(v|_\Gamma)\) for all \(v\in V_0\). For \(f\) as above,
\[\ell(u_f|_\Gamma)=a(u_f-Ef,w)=a(u_f,w)-a(Ef,w)=-a(Ef,w).\]
Here \(w\in V_0\), so \(a(u_f,w)=0\), and \(Ef|_\Gamma=0\). Thus \(\ell(u_f|_\Gamma)=0\) for all such \(f\) gives vanishing exterior weak conormal derivative of \(w\) on \(\Gamma_c\). Testing the adjoint with compactly supported functions in \(\Omega\setminus\bar D\) shows \(\Delta w=0\) there, while \(w=0\) on the exterior boundary. Zero Cauchy data on \(\Gamma_c\), the standard local boundary uniqueness for the Laplacian (zero extension across a smooth boundary patch followed by interior harmonic unique continuation), and connectedness imply \(w=0\) in \(\Omega\setminus\bar D\). The \(H^1\) transmission trace then gives \(w|_\Gamma=0\). Testing inside \(D\) gives \(\Delta w=0\) in \(D\); uniqueness for zero Dirichlet data gives \(w=0\) there. Hence \(\ell(v|_\Gamma)=0\) for every \(v\in V_0\). The trace map \(V_0\to H^2(\Gamma)\) is onto: extend an arbitrary \(H^2\) function in a smooth tubular neighborhood of \(\Gamma\) with a normal cutoff supported inside \(\Omega\). Consequently \(\ell=0\), and Hahn–Banach proves density. □

**Audit and stopping point.** This lemma assumes a smooth known interface, constant bulk coefficients and complete freedom to prescribe localized boundary functions. It gives neither shape recovery, nor recovery from a single scalar flux, nor nonlinear stability; the measurable patch for the adjoint is the *control patch*, not automatically a disjoint observation patch. It is likely a standard partial-boundary adaptation of the full-data Runge argument in [arXiv:2509.15171](https://arxiv.org/html/2509.15171) §4, so novelty is **not established**. A nontrivial next step would require a partial-data factorization or exact obstruction, rigorously mapping both disjoint patches and the surface nullspace, plus a complete full-text primary comparison. The lemma cannot be promoted to that stronger conclusion.

## 9. Abstract singular-integral diagnostic (not proof)

The following standalone Python 3 midpoint calculation checks the sign in (2) for the abstract smooth mean-zero rate density \(\rho(r)=(r-2)(r-1)^2(3-r)^2\), \([a,b]=[1,3]\). It is **not** a physical parameter run or an injectivity test. The diagonal difference quotient is replaced by its continuous value; the two integrals have different discretization errors. At \(n=800\), absolute differences were approximately \(2.70\times10^{-5}\) at \(t=0.4\) and \(5.44\times10^{-5}\) at \(t=1.1\). The analytic proof above, not this diagnostic, supplies the identity.

```python
import math
a,b=1.,3.; n=800; dr=(b-a)/n
x=[a+(i+.5)*dr for i in range(n)]
v=[(r-2)*((r-a)*(b-r))**2 for r in x]
for t in (0.4,1.1):
    left=sum(v[j]*((math.exp(-x[j]*t)-math.exp(-r*t))/(r-x[j])
              if i!=j else t*math.exp(-r*t))*dr*dr
             for i,r in enumerate(x) for j in range(n))
    k=[2*v[i]*math.log((b-r)/(r-a))+
       sum((v[j]-v[i])/(s-r)*dr for j,s in enumerate(x) if i!=j)
       for i,r in enumerate(x)]
    right=sum(math.exp(-r*t)*k[i]*dr for i,r in enumerate(x))
    print(t,left,right,abs(left-right))
```
