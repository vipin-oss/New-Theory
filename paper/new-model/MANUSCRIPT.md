# A periodic nonlocal thermoelastic model with thermal displacement and a relaxing heat flux: a candidate formulation

**Vipin Gupta**
Department of Mathematics, Gurugram University

## Abstract
We formulate a linear one-dimensional periodic thermoelastic candidate combining a mixed local–Helmholtz elastic operator with thermal displacement, Fourier conduction and a relaxing flux. A global linearized thermodynamic inequality and an energy identity are derived for positive coefficients; classical-solution uniqueness follows. The model specializes to standard one-dimensional Fourier, nondissipative thermal-displacement, combined thermal-displacement/Fourier, and Cattaneo forms, and a restricted first-order dual-phase-lag equation. A Fourier dispersion relation and a reproducible matrix-exponential illustration are given. These are normalized equation-level identifications, not verified equivalences to all original theories. General Green–Lindsay and exact-delay dual-phase-lag models are not recovered. Closely related nonlocal theories exist, and originality, physical validation, and reproduction of a published numerical benchmark remain open.

## 1. Background and status
See LITERATURE.md for primary-source mapping, access limitations and extensive overlap. The construction below is a research candidate, not a demonstrated new theory. All results are for a periodic one-dimensional linearization around a uniform stress-free state at absolute temperature T0>0. The mathematical model is self-contained, but original-source equation matching and a local thermodynamic formulation remain incomplete.

## 2. Variables, assumptions, and balance laws
On Ω=[0,L] with periodic fields, let u be displacement, ε=u_x, θ the temperature increment, v=u_t, α thermal displacement (α_t=θ), and r an internal heat-flux component. Denote q total heat flux, σ stress. No body forces or heat sources are imposed. Let ρ,C,c,kr,τ>0, h,κ≥0, β real, ℓ≥0 and 0<η≤1. Define the self-adjoint positive operator A=ηI+(1−η)(I−ℓ²∂xx)^−1 on periodic fields, with Fourier multiplier a(k)=η+(1−η)/(1+ℓ²k²), k=2πn/L. Thus η≤a≤1.

The equations and constitutive choices are

    σ = C A ε − β θ,                ρ u_tt = σ_x,
    c θ_t + T0 β ε_t = −q_x,       α_t = θ,
    q = −h α_x − κ θ_x + r,        τ r_t + r = −kr θ_x.             (1)

The heat balance is the linearized entropy/internal-energy balance about T0. In SI: [u]=m, [ε]=1, [θ]=K, [α]=K s, [σ]=Pa, [q]=[r]=W m⁻², [ρ]=kg m⁻³, [C]=Pa, [β]=Pa K⁻¹, [c]=J m⁻³ K⁻¹, [κ]=[kr]=W m⁻¹ K⁻¹, [h]=W m⁻¹ K⁻¹ s⁻¹, [τ]=s, and [ℓ]=m. The positivity of absolute temperature is a small-perturbation assumption; the quadratic linearized free energy is not asserted to be a globally valid finite-temperature potential.

### Global linearized thermodynamic inequality
Define the total free-energy functional and entropy increment by

    F = ∫Ω [C ε Aε/2 − β εθ − c θ²/(2T0)
             + h α_x²/(2T0) + τ r²/(2 kr T0)] dx,
    s = β ε + c θ/T0.                                                 (2)

Aε is nonlocal, so the first term is an energy density representation of a *functional*, not a proof of an ordinary pointwise local inequality. Self-adjointness gives d∫ε Aε/dt=2∫ε_t Aε. The linearized integrated free-energy dissipation, assuming periodicity, is

    D = ∫σ ε_t dx − dF/dt − ∫s θ_t dx − ∫q θ_x/T0 dx
      = (1/T0)∫[κ θ_x² + r²/kr] dx ≥ 0.                            (3)

Indeed −hα_xθ_x/T0 cancels the α part of −qθ_x/T0, and −(τ/kr)rr_t−rθ_x=r²/kr by (1). D has units energy per time per cross-sectional area. The corresponding linearized global entropy production is D/T0. Equation (3) assumes the standard linearized global free-energy inequality and entropy flux q/T0; it does not derive the missing interpoint energy flux or establish local Clausius–Duhem admissibility. The stated coefficient conditions are sufficient, not claimed necessary. When kr=0 or τ=0 the r-storage formula is singular or degenerates; use a separately reduced system, not (2) divided by zero.

### Limiting systems
Eliminating r at kr,τ>0 gives

    τ q_t + q = −h α_x − (κ+kr+τh) θ_x − τκ θ_xt.                   (4)

In the local elastic limit η=1 or ℓ=0: (i) τ=0 in the reduced constitutive system gives r=−krθ_x; h=0 then yields classical coupled Fourier thermoelasticity, commonly identified with GN I; h>0 yields the normalized GN III form; with κ=kr=0 and r absent it is GN II. (ii) h=κ=0 gives the standard Cattaneo/LS-form flux law. (iii) h=0 yields differential first-order DPL with K=κ+kr, τq=τ and τT=τκ/K. Thus 0≤τT<τq when kr>0; equality is a degenerate limit. These identifications refer to the displayed linear PDEs and not full verification against the original sources. The full Tzou time-shift equation is not identical to its first-order truncation. (iv) β=0 and η→0 yields a periodic Helmholtz-kernel Eringen-type elastic stress, one particular kernel rather than all nonlocal thermoelasticity. Coercivity is not uniform as η→0.

General GL requires additional temperature-rate constitutive structure: σ here has no θ_t term. No general GL, exact time-shift DPL, three-phase-lag or MGT recovery is claimed. No Klein–Gordon restoring term follows: neither a local u² nor α² potential was assumed. Adding one without a material mechanism would change the model.

## 3. Energy, uniqueness and dispersion
For smooth periodic solutions multiply the momentum equation by u_t and the heat equation by θ/T0, integrate, and use α_t=θ and the r equation. All boundary terms vanish and β terms cancel. The result is

    E = 1/2 ∫[ρu_t²+C ε Aε+(c/T0)θ²
                 +(h/T0)α_x²+(τ/(kr T0))r²]dx,
    dE/dt = −(1/T0)∫[κθ_x²+r²/kr]dx ≤ 0.                            (5)

For two classical solutions with identical initial data, the difference has E(0)=0. Since A≥ηI and the positive terms control u_t, ε, θ and r, these vanish; u_t=0 and the initial displacement fix u, while α_t=θ and its initial value fix α even when h=0. This is uniqueness of sufficiently smooth periodic solutions, not an existence theorem. Energy is nonincreasing; no strict, uniform or exponential decay follows, especially for zero modes and conservative limits. If h>0, α_x is also controlled. For η→0 the estimate loses uniform strain coercivity; pure nonlocal uniqueness is not asserted here.

For k≠0, Fourier modes exp(st+ikx) have polynomial

    P(s,k) = (ρs²+Ck²a(k)) [(cs²+κk²s+hk²)(1+τs)+kr k²s]
             + β²T0 k²s²(1+τs) = 0.                                 (6)

The code checks this against the full five-state determinant. For h>0, each nonzero mode has a positive energy metric and (5) gives Re(s)≤0. Write s=−γ−iω: temporal attenuation γ=−Re(s), phase speed ω/k, and, on a differentiable simple branch, group speed dω/dk=Im(P_k/P_s). Branch tracking is required; these need not describe a sharply localized pulse in dissipative media. Degenerate cases can have auxiliary or gauge roots; check the eigenvectors and reduced equations rather than counting every polynomial factor as a wave. This is temporal attenuation, not a spatial attenuation coefficient from real-frequency complex-k analysis.

In decoupled local Fourier conduction the heat equation is parabolic and has infinite propagation speed on the line. The decoupled local GN II thermal field has speed √(h/c), and the decoupled local LS thermal field has characteristic speed √(kr/(τc)); these do not establish speeds for all coupled modes. Spatial nonlocality itself destroys general compact-support propagation: on the line, with 0≤η<1 and ℓ>0, the inverse Helmholtz kernel is exp(−|x|/ℓ)/(2ℓ). For generic compactly supported initial u, u_t=θ=α=r=0, u_tt at t=0 contains ∂xx(K*u) and has nonzero tails outside the support, so arbitrarily early motion occurs there. The periodic problem has no exterior region, and speed claims on it require a separate definition.

## 4. Analytical checks and numerical illustration
For β=0 the reduced Fourier scalar mode is θk(t)=θk(0)exp[−Kk²t/c]. The reduced GN II mode satisfies θ̈k+(h/c)k²θk=0. The Cattaneo thermal mode has τc s²+cs+kr k²=0, and the uncoupled elastic mode has ω²=Ck²a(k)/ρ. These analytical checks are verified by the supplied code, not reproductions of specific published numerical results. For a fully coupled mode y=(u,u_t,θ,α,r), y(t)=exp(tM(k))y(0). The implementation uses SciPy's matrix exponential; it does not discretize time.

RESULTS.md lists actual dimensionless coefficients, sampled spectral convergence, test tolerances and runtime. Each mode obeys (5); Fourier orthogonality implies that truncation error in the energy seminorm is bounded by the initial high-frequency energy tail for finite-energy initial data, for the periodic linear system and the positive-energy assumptions above. Sampled θ errors are a separate numerical diagnostic, not a uniform analytical bound. The example is manufactured and is neither a material measurement nor an experimental validation. No parameter fitting or published benchmark reproduction was performed.

## 5. Discussion and limitations
The global thermodynamic and energy structures supply a tractable illustrative benchmark, but a full local balance with nonlocal interpoint flux, existence, boundary-value extensions, source-by-source equivalence, general GL and exact-delay DPL, physical parameter calibration and published benchmark replication remain to be established. Prior abstracts already demonstrate overlapping families; novelty cannot yet be assessed responsibly. All analysis and checks are same-agent work, not independent review or certification. The author makes the final research and submission decisions.

References and detailed source access: LITERATURE.md. Reproduction instructions: README.md.
