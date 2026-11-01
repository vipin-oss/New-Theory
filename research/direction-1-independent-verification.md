# Direction 1: independent mathematical verification

**Reviewed:** `research/direction-1-prior-art-audit.md`, commit `884e92247e83b9fb9fc4568b7d2638b42a5ce9ee`, especially §§2, 8–10. **Date:** 1 November 2026. The calculations below were re-derived from the displayed field equations and checked against accessible original-source texts. This is a fresh mathematical check by the same research agent, **not** certification by a separate human or an independently operated scientific auditor. It is not an exhaustive literature search and makes no originality claim.

## 1. Executive verdict

The three principal claims withstand the checks **with conditions**: the undamped differential expressions and energy are an exact specialization of the 1-D equations reproduced by Berezovski–Ván and independently already present in Berezovski et al. (2013); the energy method gives a finite propagation **upper bound** for smooth, whole-line energy variables; and the nonlocal constitutive operator is globally passive yet violates a finite-speed local input–output cone. None establishes a new theory.

One correction is needed in the earlier audit: in its §9, `nF` is **power supplied to the body** by boundary tractions, not outward energy flux. The associated outward energy flux is `-nF`. The computed balance itself has the correct sign. A second qualification: in §10, a merely positive self-adjoint inverse elliptic operator does not by itself ensure a pointwise positive kernel; positivity preservation or another nonzero off-diagonal condition is required for the asserted bounded-interval analogue.

## 2. Claim-by-claim verdict

| Claim | Verdict | Exact scope |
|---|---|---|
| Undamped baseline versus the 1-D equations of Berezovski–Ván | **VERIFIED WITH CONDITIONS** | Exact energy and two differential expressions with specified coefficient/variable maps. Equality of complete problems needs matching domains, data and boundary operators; original Mindlin paper itself is inaccessible. |
| Dual internal-variable representation | **VERIFIED WITH CONDITIONS** | Requires nonzero antisymmetric coefficient and positive dual stiffness, correct state map `beta=-z_t/(L12 D)`, and transformed initial/boundary data. Damping and full thermal equations are not matched. |
| Local energy identity and passivity | **VERIFIED WITH CONDITIONS** | Smooth fields, positive coefficients, `gamma>=0`, and specified boundary power convention. It is a mechanical storage inequality, not a full thermodynamic entropy proof. |
| `nF` called outward mechanical power in prior audit | **INCORRECT** | `nF` is boundary power into the body with this definition of `F`; the outward energy flux is `-nF`. Boundary balance and zero-power examples remain correct. |
| Finite propagation | **VERIFIED WITH CONDITIONS** | Upper bound for smooth finite-energy whole-line solutions; decay/traces and Leibniz rules assumed. No proved optimal speed or bounded-domain/weak-solution theorem. |
| Passive spatially nonlocal counterexample | **VERIFIED WITH CONDITIONS** | Global stress–strain-rate port, arbitrary prescribed local strain inputs, zero hidden state and local port maps. It is an input–output statement, not a full thermoelastic body model or a no-go theorem for nonlocal ports. |
| General bounded-interval extension from positivity/self-adjointness alone | **PARTIALLY VERIFIED** | Existence of appropriate positive Green kernels is plausible and can be shown for particular boundary conditions; the properties stated in §10 alone do not imply pointwise kernel positivity. |
| Full original Mindlin equations and boundary conditions | **NOT VERIFIABLE** | Publisher gives subscription preview only; use the later authors' explicit attribution, not a claim to have read the original. |

## 3. Independent equivalence calculation

### 3.1 Baseline and direct energy

Let `u` be 1-D displacement, `e=u_x`, `z` a scalar dimensionless microdeformation, and use constants `rho,m,C,b,d>0`, `gamma>=0`:

```
W=(C/2)e²+(b/2)(e-z)²+(d/2)z_x²,
K=(rho/2)u_t²+(m/2)z_t²,
sigma=(C+b)e-bz,
rho u_tt=(C+b)u_xx-b z_x,
m z_tt=d z_xx+b u_x-b z-gamma z_t.
```

Differentiating `W` at fixed `z,z_x` gives `sigma`, and differentiating with respect to `z` and `z_x` gives `-b(e-z)` and `d z_x`. Thus the last equation follows from the variational microforce `-W_z+(W_{z_x})_x` with viscous drag. All comparisons below set **gamma=0**.

### 3.2 Berezovski–Ván Mindlin-type representation

In the accessible Berezovski–Ván preprint [1], eqs. (51)–(54) define macrostrain `epsilon`, microdeformation `psi`, relative strain `r=epsilon-psi`, and

```
W_BV=(rho c_BV²/2) epsilon² + g epsilon r
     +(b_BV/2) r²+(a_BV/2)psi_x²,
tau=rho c_BV² epsilon + g r,
s_BV=g epsilon+b_BV r,       mu=a_BV psi_x,
rho u_tt=(tau+s_BV)_x,
I psi_tt=mu_x+s_BV,   I=rho' d_cell²/3.
```

These expressions yield the authors' (63)–(64):

```
rho u_tt=(rho c_BV²+b_BV+2g)u_xx-(g+b_BV)psi_x,
I psi_tt=a_BV psi_xx+(g+b_BV)u_x-b_BV psi.
```

Set `epsilon=e`, `psi=z`, `g=0`, `rho c_BV²=C`, `b_BV=b`, `a_BV=d`, and `I=m` (choosing positive `rho'`, `d_cell` satisfying `rho' d_cell²/3=m`). Then `W_BV=W`, `tau+s_BV=Ce+b(e-z)=sigma`, and `mu=d z_x`. Substitution reproduces both undamped field equations, including all signs. The prior audit's direct mapping is correct. Independently, [2] eqs. (1)–(4) give `rho u_tt=rho c² u_xx+A phi_x` and `I phi_tt=C_micro phi_xx-A u_x-B phi`: set `rho c²=C+b`, `A=-b`, `B=b`, `C_micro=d`, `I=m`, and `phi=z`. Its quadratic energy becomes the same `W`. The baseline is a **special case**, not equivalent to every member of the broader BV family.

### 3.3 Dual-variable representation

For [1] eqs. (55)–(62), distinguish their coefficients by hats:

```
Wbar=(rho c_hat²/2)e²+A alpha e+(B/2)alpha²
     +(C_hat/2)alpha_x²+(D/2)beta²,
alpha_t=-L12 D beta,
beta_t=-L12(C_hat alpha_xx-Ae-B alpha),
I=1/(L12² D).
```

With `alpha=z`, `rho c_hat²=C+b`, `A=-b`, `B=b`, `C_hat=d`, and `I=m`, the energy's first four terms expand to exactly `W`, and [1] eqs. (60) and (62) give exactly the two undamped balances. Take `D>0` and `L12!=0` with `L12² D=1/m`; the state transformation is `beta=-z_t/(L12 D)`. Therefore

```
(D/2)beta² = z_t²/(2 L12² D) = (m/2)z_t².
```

Macrokinetic energy `rho u_t²/2` remains separate from `Wbar`; treating all of `Wbar` as purely elastic energy would double count the internal kinetic term. This reparameterization of `c_hat` does not require BV's separate special choice `b_BV+2g=0`, which keeps the same symbol `c` in their particular comparison; here the coefficient `rho c_hat²` is chosen anew. It also does not claim a match to all BV models or arbitrary thermodynamic interpretations.

### 3.4 Units and complete-problem qualifications

Use SI **energy per reference volume** `P=Pa`; equivalently, for a unit-area bar, the same numbers represent energy per reference length. Then `[u]=L`, `[e]=[z]=1`, `[rho]=M/L³`, `[C]=[b]=P`, `[d]=P L²`, `[m]=P T²=rho L²`, `[gamma]=P T`. Thus `d z_xx`, `b(e-z)` and `m z_tt` all have units `P`; `sigma_x` and `rho u_tt` both have units `P/L`; and both characteristic speeds below have units `L/T`. `F` has units `P L/T`, i.e. energy flux per area. The source coefficient `rho' d_cell²/3` has the same units as `m` when `rho'` has mass-density units. If a genuine bar model instead uses energy per length and line density, all stiffness, inertia, and traction coefficients must be scaled by cross-sectional area consistently.

For equality of *complete* initial-boundary-value problems one must use the same spatial interval or whole line and map `u(0),u_t(0),z(0),z_t(0)` to `u(0),u_t(0),alpha(0),beta(0)` with the formula above. The macro and micro boundary conditions and their time traces, forcing, solution spaces and regularity must agree after transformation. `z_t=0` at a boundary maps to `beta=0`; for the common constant-coefficient energy, microtraction `d z_x` maps directly. The existence of an equation mapping does not by itself prove a source paper uses the same boundary conditions. BV's §3 explicitly uses the nondissipative case; its broader entropy framework is not a term-by-term proof for this `gamma z_t` model at nonconstant temperature.

## 4. Energy, positivity and boundary power

Let `v=u_t`, `p=z_t`, `q=z_x`, and `h=K+W`. Differentiating and substituting the equations gives

```
h_t = rho v v_t + sigma e_t - b(e-z)p + d q q_t + m p p_t
    = v sigma_x + sigma v_x + d(p q_x + q p_x) - gamma p²
    = (sigma v+d q p)_x - gamma p².
```

Here `e_t=v_x`, `q_t=p_x`. Put `F=sigma v+d q p` and `j=-F`; then `h_t+j_x=-gamma p²`. `h` is strictly positive definite in the independent tuple `(v,p,e,z,q)`: its vanishing implies successively `v=p=e=e-z=q=0`, hence `z=0`. Equivalently the `(e,z)` stiffness matrix has determinant `C b>0` and positive leading entry `C+b`. Positive energy does not control a constant displacement `u` on an unbounded domain.

For an interval `[a,b]`, with `[F]_a^b=F(b)-F(a)`,

```
d/dt integral_a^b h dx = [F]_a^b - integral_a^b gamma p² dx.
```

At a boundary the outward unit normal is `n=-1` at `a`, `n=+1` at `b`. The traction and microtraction efforts `(n sigma,n d q)` paired with flows `(v,p)` give **supplied/inward mechanical power** `nF`; summed over both endpoints this is `[F]_a^b`. The outward flux of stored energy is `n j=-nF`. Different port conventions may exchange a sign, but the power identity must remain fixed. `v=p=0` or `sigma=q=0` at both endpoints, or periodic matching of the two endpoint fluxes, produces zero net boundary work. With a nonnegative boundary **supply** the energy need not decrease; passivity is `E(t)-E(0)<=integral boundary_supply`.

The identity assumes sufficient spatial/time smoothness for the chain rule, endpoint traces and integration by parts; a finite interval avoids a flux-at-infinity assumption. For the whole line one needs finite energy and vanishing flux at infinity in the sense required by the integration, or a cutoff argument. For `gamma>=0` the bulk loss is nonnegative. A heat bath receiving this loss and an entropy balance require independent specification; no full Clausius–Duhem result follows from this calculation alone.

## 5. Finite-propagation check

### 5.1 Flux estimate

Set `c_u=sqrt((C+b)/rho)`, `c_z=sqrt(d/m)` and `c*=max(c_u,c_z)`. Weighted Cauchy–Schwarz gives

```
sigma² = [C e+b(e-z)]²
        <= (C+b)[C e²+b(e-z)²].
```

By `2|ab|<=a²+b²`,

```
|sigma v| <= (c_u/2)[rho v²+sigma²/(C+b)],
|d q p|   <= (c_z/2)[m p²+d q²].
```

Consequently `|F|<=c* h`. This is an upper bound obtained from the chosen positive energy. The undamped principal symbol has high-frequency wave speeds `c_u,c_z`, but the inequality alone does **not** prove sharp propagation speed, observable front excitation, or a statement for a different boundary realization.

### 5.2 Both moving half-lines

Assume a smooth solution on `R x [0,T]`, spatially integrable `h` and `p²`, and sufficient decay of `F` to justify truncation and the limit. Let `c>=c*`. For the right exterior `x>R+ct`, Leibniz and integration give

```
E_R'(t)=-F(R+ct,t)-c h(R+ct,t)
        -integral_(R+ct)^infinity gamma p² dx <=0.
```

For the left exterior `x<L-ct`, the corresponding computation is

```
E_L'(t)= F(L-ct,t)-c h(L-ct,t)
        -integral_(-infinity)^(L-ct) gamma p² dx <=0.
```

Both boundary terms are nonpositive because `|F|<=ch`. If the initial energy vanishes outside `[L,R]`, the nonnegative exterior energies remain zero. Thus `v,p,e,z,q` vanish almost everywhere outside the enlarged interval; for smooth fields the statement is pointwise. This is finite propagation of energy-bearing fields, not necessarily compact support of `u`: outside the cone `u_x=u_t=0`, so `u` is a time-independent spatial constant on each exterior component. Normalizing those constants, or directly imposing suitable initial displacement support, is necessary to infer displacement support.

This is a conditional a priori estimate. By applying it to differences, one obtains uniqueness/continuous dependence in classes where the same integration and zero external power are justified. No existence proof, weak-solution approximation or trace theorem is supplied here; a weak-solution extension requires a well-posed energy-space construction and convergence of approximants. For a bounded interval, characteristic boundary conditions, reflected waves and the operator domain must be specified. Dissipative boundary power alone is not a proof of maximal dissipativity or existence. No exponential decay follows.

## 6. Passive nonlocal example: attempts to falsify it

Let `ell>0`, `G(x)=exp(-|x|/ell)/(2 ell)` and `sigma=G*e` on `R`. For a Fourier convention with `hat f(k)=integral exp(-ikx)f(x) dx`, direct integration yields `Ghat(k)=1/(1+ell² k²)>0`. For real `e in L²`, Plancherel gives

```
S(e)=1/2 <e,G*e>
    =(1/(4 pi)) integral |e_hat(k)|²/(1+ell² k²) dk >=0.
```

It is strictly positive for nonzero `e in L²`, though not uniformly coercive in the `L²` norm because the multiplier tends to zero at high wave number. `G*` is a bounded self-adjoint operator on `L²`. For `e in C¹([0,T];L²)`, differentiating the bounded quadratic form yields `S'(t)=<sigma,e_t>`. Hence with input `e_t`, output `sigma`, and zero initial strain, the global port is lossless and passive. This is not pointwise local stored-energy density, nor a thermal entropy balance.

Choose `g>=0`, nonzero and smooth with compact support in `[a,b]`, and `e(x,t)=f(t)g(x)`, where `f` is smooth, zero for `t<=0`, and positive for arbitrarily small `t>0` (e.g. `exp(-1/t)` for `t>0`). Since `G>0`, `(G*g)(x)>0` for every `x`; at any point a distance `r>0` from `[a,b]`, stress is nonzero for arbitrarily small positive `t`, whereas a zero-state, locally actuated and locally observed realization having the assumed domain-of-dependence bound `c` must give zero before `r/c`. Therefore exact input–output equality for this input class is impossible. This is a direct support contradiction under a stipulated cone property, not a claim that all passive Hamiltonian realizations possess local ports.

**Compatibility challenge:** a nonnegative nonzero `g` is a legitimate prescribed strain, but cannot be `u_x` for a compactly supported displacement on the whole line because its integral is positive. The argument can be strengthened within compatible compact displacements: take any nonnegative nonzero `h in C_c^infinity((a,b))`, let `g=h'`, and prescribe `u(x,t)=f(t)h(x)`. For `x>b`, integration by parts gives

```
(G*g)(x) = - exp(-x/ell)/(2 ell²) integral_a^b exp(y/ell) h(y) dy !=0.
```

Thus the counterexample survives compact-displacement compatibility. The prescribed `u` is a constitutive test input, not necessarily a free solution of the coupled momentum equation; external forcing/constraints would have to be modeled for a full mechanical experiment. The input must be independently realizable within the specified local-port system. Exact equivalence on only a restricted boundary-to-boundary observation set, or with nonzero preloaded/nonlocally prepared hidden state, is not ruled out. An instantaneous direct *local* feedthrough is allowed but cannot transmit to separated points; a nonlocal feedthrough evades the premise. A passive local hereditary term can be added without eliminating the instantaneous remote signal if the term is local and has zero initial state.

For a bounded interval, self-adjoint positive **operator** means a nonnegative quadratic form, not pointwise positivity of its kernel. A particular inverse such as a strictly positive Green function for `1-ell² d²/dx²` with appropriate homogeneous Dirichlet conditions supplies a bounded-domain version, but it must be explicitly specified and verified. The broad assertion in the earlier report should not be read as a theorem from self-adjoint positivity alone.

## 7. Primary-source verification table

The equation numbers below refer to the cited accessible versions; reviewing selected relevant sections is not equivalent to checking every page or a comprehensive search.

| Source / verified bibliography | Access and evidence checked | Limitation |
|---|---|---|
| [1] A. Berezovski and P. Ván, “Microinertia and internal variables,” *Continuum Mechanics and Thermodynamics* **28** (2016), 1027–1037; published online 2015. [10.1007/s00161-015-0453-2](https://doi.org/10.1007/s00161-015-0453-2). | [Full author preprint](https://arxiv.org/html/1504.03485), §3 eqs. (51)–(64), specifically state, energy and dual evolution. | Preprint checked, not publisher typeset full text; non-isothermal damping and all boundary conditions not independently matched. |
| [2] A. Berezovski, J. Engelbrecht, A. Salupere, K. Tamm, T. Peets and M. Berezovski, “Dispersive waves in microstructured solids,” *International Journal of Solids and Structures* **50** (2013), 1981–1990. [10.1016/j.ijsolstr.2013.02.018](https://doi.org/10.1016/j.ijsolstr.2013.02.018). | [Full author manuscript](https://commons.erau.edu/cgi/viewcontent.cgi?article=2024&context=publication), §2 eqs. (1)–(5), (6)–(10), (14)–(20). Potential and kinetic energies and nondissipative coupled dynamics predate the proposed model. | Eq. numbers refer to the manuscript; no claim that every possible damped or boundary formulation is identical. |
| [3] R. D. Mindlin, “Micro-structure in linear elasticity,” *Archive for Rational Mechanics and Analysis* **16** (1964), 51–78. [10.1007/BF00248490](https://doi.org/10.1007/BF00248490). | [Publisher record](https://link.springer.com/article/10.1007/BF00248490), author, title and bibliographic metadata. | Subscription preview only. Original equation numbers and original full assumptions **not verified**; attribution of the 1-D reduction is as given in [1]. |
| [4] E. Agiasofitou and M. Lazar, “Nonlocal elasticity of Klein-Gordon type with internal length and time scales: Constitutive modelling and dispersion relations,” *PAMM* **23** (2023), e202300065. [10.1002/pamm.202300065](https://doi.org/10.1002/pamm.202300065). | [Full article](https://publikationen.bibliothek.kit.edu/1000165899/151898056), eqs. (2), (5)–(13), (16)–(18) and (23)–(24). `L t=sigma_classical`, `L=1-ell² Delta+tau² partial_t²`. | Same mediator operator type does not give identical full constitutive transfer or boundary conditions. No full thermodynamic equivalence is inferred. |
| [5] A. Figotin and J. H. Schenker, “Hamiltonian structure for dispersive and dissipative dynamical systems,” *Journal of Statistical Physics* **128** (2007), 969–1056. [10.1007/s10955-007-9321-1](https://doi.org/10.1007/s10955-007-9321-1). | [Author preprint](https://arxiv.org/html/math-ph/0608003v2), eqs. (1.11), (1.13)–(1.15), Theorem 1.1 and §5. The theorem states an iff quadratic Hamiltonian extension under its symmetry, power-dissipation and regularity hypotheses. | The theorem's abstract Hilbert-space extension does not assert a finite physical-space propagation cone or local boundary ports. |
| [6] S. A. R. Horsley and T. G. Philbin, “Canonical quantization of electromagnetism in spatially dispersive media,” *New Journal of Physics* **16** (2014), 013030. [10.1088/1367-2630/16/1/013030](https://doi.org/10.1088/1367-2630/16/1/013030). | [Full article](https://iopscience.iop.org/article/10.1088/1367-2630/16/1/013030), §3 eqs. (12)–(18), especially (15): a spatially nonlocal coupling to reservoir fields. | Electromagnetic action, not a proof of equivalence to the mechanical example or of finite physical-space speed. The fetched rendering displays equations as images: surrounding prose and equation references were inspected, not independently transcribed formula-by-formula. |
| [7] A. J. van der Schaft and B. M. Maschke, “Hamiltonian formulation of distributed-parameter systems with boundary energy flow,” *Journal of Geometry and Physics* **42** (2002), 166–194. [10.1016/S0393-0440(01)00083-3](https://doi.org/10.1016/S0393-0440(01)00083-3). | [Publisher preview](https://doi.org/10.1016/S0393-0440(01)00083-3) and abstract describe boundary energy flow, Dirac structure and vibrating-string example. | Full article unavailable through publisher preview; exact equation/theorem numbers not checked. |
| [8] B. Jacob and H. J. Zwart, *Linear Port-Hamiltonian Systems on Infinite-dimensional Spaces*, Birkhäuser (2012). [10.1007/978-3-0348-0399-1](https://doi.org/10.1007/978-3-0348-0399-1). | Publisher metadata and chapter list checked. Related [2023 introductory preprint](https://arxiv.org/html/2308.01822), DOI [10.48550/arXiv.2308.01822](https://doi.org/10.48550/arXiv.2308.01822), eqs. (1)–(2) explicitly show transmission-line boundary power and §3 the 1-D port-Hamiltonian form. | Book full text not inspected; preprint is a separate source, not a book theorem citation. |

## 8. Corrections required in the earlier audit

1. **§9 boundary sign terminology:** replace “outward mechanical port power `nF`” with “mechanical power supplied to the body `nF`”; outward energy flux is `-nF`. No change to `[F]_a^b` or the energy estimate is required.
2. **§10 bounded-domain statement:** specify a positivity-preserving Green operator or otherwise prove the relevant off-diagonal kernel is nonzero; positivity and self-adjointness alone only establish nonnegative quadratic storage.
3. **§10 input class:** explicitly state that prescribed strains are constitutive inputs; if compactly supported displacement compatibility is demanded, use `g=h'` as above rather than nonnegative `g`.
4. **§9 finite-speed result:** retain the limitations on smooth whole-line solutions, admissible traces/decay and the distinction between energy fields and displacement. An optimal front speed, weak-solution extension and boundary well-posedness are not established.
5. **§§2 and 8 equivalence:** retain the distinction between a coefficient specialization and all members of the source theory; specify dual initial-state mapping and do not assert direct verification of Mindlin's original article.

These corrections are recorded here without altering the prior report.

## 9. Remaining uncertainties and final recommendation

The original Mindlin paper, the full van der Schaft–Maschke paper and the Jacob–Zwart book were not available for full examination. The Berezovski–Ván and Berezovski et al. comparisons use accessible author versions; publisher-version differences have not been exhaustively checked. The literature investigation is selective. A general characterization of local finite-speed realizability is not proved, nor is it claimed to be novel.

**Recommendation:** maintain rejection of the existing Direction 1 mediator as a new foundational continuum theory. The verified conditional calculations support that negative finding; they do not establish scientific originality, empirical validity, full thermodynamics or a general existence theorem.
