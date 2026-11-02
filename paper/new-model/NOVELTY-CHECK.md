# Novelty check only: nonlocal thermoelastic candidate

Search date: 2026-11-02. This is a targeted search, not a priority certificate or an exhaustive search. No model has been changed. Equations transcribed from sources are distinguished from reductions and comparison polynomials calculated here. The primary equations of Das–De–Sarkar (2023) and Tiwari–Kumar (2021) were inspected in the author-uploaded full text; the full articles' proofs were not audited. Access status of every other source is given below. In particular, absence of a full-text match is **not** evidence of novelty.

## Reference equations and normalization

Our existing one-dimensional model has α_t=θ, σ=C A u_x−βθ, A=ηI+(1−η)(I−ℓ²∂xx)⁻¹, and

    q = −h α_x − κ θ_x + r,            τ r_t+r=−kr θ_x.             (O1)

Here a(k)=η+(1−η)/(1+ℓ²k²), and the Fourier ansatz is exp(st+ikx). Set B=β²T0 and D=1+τs. The existing polynomial is

    P_O=(ρs²+Ck²a) [c s²D+k²(h+(κ+kr+τh)s+τκs²)]
         + B k²s²D.                                                   (O2)

The flux equation obtained by eliminating r is **exact** within this differential model:

    D(∂t)q=−h α_x−(κ+kr+τh)θ_x−τκ θ_xt.                          (O3)

No Taylor approximation is used to derive O3 from O1. Conversely, initial r is fixed by initial q, α and θ; equality of eliminated laws also requires corresponding initial-state compatibility. The dispersion relations below concern nonzero Fourier modes and homogeneous equations, not boundary-value or entropy equivalence.

## 1. Closest match: nonlocal thermoelasticity with three-phase-lag heat conduction

**Rakhi Tiwari and Ravi Kumar**, “Analysis of plane wave propagation under the purview of three phase lag theory of thermoelasticity with non-local effect,” *European Journal of Mechanics – A/Solids* **88** (2021), 104235, [doi:10.1016/j.euromechsol.2021.104235](https://doi.org/10.1016/j.euromechsol.2021.104235). **Primary governing equations inspected** in the [author-uploaded article, section 2](https://www.researchgate.net/publication/349427933_Analysis_of_plane_wave_propagation_under_the_purview_of_three_phase_lag_theory_of_thermoelasticity_with_non-local_effect); article is plane strain in a half-space, not the periodic rod. With their ε the nonlocal length, their τν the thermal-displacement lag, and e=div u, equations (1)–(3) are

    (1−ε²∇²) t_ij=2μ e_ij+(λe−γθ)δ_ij,
    μ∇²u+(λ+μ)∇e−γ∇θ=ρ(1−ε²∇²)u_tt,
    K(1+τT∂t)∇²θ_t + K*(1+τν∂t)∇²θ
        = (1+τq∂t+τq²∂tt/2)(ρCE θ_tt+γT0 e_tt).              (T1)

They retain **second order in the flux lag** τq, but first order in the gradient lags; this is not the same differential law as O3. Their own stated thermodynamic inequalities and their geometry need separate verification for any proposed specialization.

For a one-dimensional longitudinal plane wave, write G=1+ε²k², C=λ+2μ, c=ρCE, β=γ and D2=1+τq s+τq²s²/2. Direct elimination from T1 gives the comparison polynomial (our derivation, not a quotation of their spatial-frequency expression):

    P_T=(ρs²+Ck²/G) [c s²D2+k²(K s(1+τT s)+K*(1+τν s))]
         +(B/G) k² s²D2.                                             (T2)

The source instead solves for a complex spatial wavenumber at real frequency, while O2 uses temporal s and real k. The mechanical model filters the **entire** local thermoelastic stress by G⁻¹: its coupling term is B/G; ours filters strain only and retains local −βθ, so its coupling term is B. Ours also permits η>0 rather than their pure Helmholtz response G⁻¹. Therefore T1/T2 are **not** the same as our full model. In addition, T2 has the extra τq²s²/2 factor. Dropping it is a different, first-order truncation, not an exact nonzero-τq specialization of T1.

### Exact identification of our eliminated law with a published *first-order* three-phase-lag form

The exact time-shifted three-phase-lag equation is reported in the primary paper [“Some solutions for a family of exact phase-lag heat conduction problems”](https://www.sciencedirect.com/science/article/abs/pii/S0093641311000747), DOI and authors verified below. Its equation is

    q(t+τq)=−K ∇θ(t+τT)−K*∇α(t+τν),  α_t=θ.                  (T3)

First-order Taylor expansion of T3 gives

    (1+τq∂t)q=−K* α_x−(K+K*τν)θ_x−KτT θ_xt.                    (T4)

T4 is exactly O3 as a **differential constitutive equation**, with

    τq=τ, K*=h, τν=0, K=κ+kr+τh, τT=τκ/K.                      (T5)

K>0 under the candidate's kr>0. Thus our relaxing-channel representation is a restricted parameterization of an already published first-order TPL heat-flux family; it is not a new heat law simply because r is explicit. O3 is not the exact delayed T3. The separately stated Tiwari–Kumar law T1 includes a second-order flux term and cannot be equated with T4 at τ>0. No claim is made here that T5 satisfies every admissibility condition in every TPL formulation.

## 2. Nonlocal MGT and the exact MGT subcase

**Narayan Das, Soumen De and Nantu Sarkar**, “Plane waves in Moore–Gibson–Thompson thermoelasticity considering nonlocal elasticity effect,” *Mathematics and Mechanics of Solids* **28**(9) (2023), 1978–1998, [doi:10.1177/10812865221145737](https://doi.org/10.1177/10812865221145737). **Primary governing equations inspected** in [author-uploaded full text, section 2](https://www.researchgate.net/publication/367327743_Plane_waves_in_Moore-Gibson-Thompson_thermoelasticity_considering_nonlocal_elasticity_effect). Their equations (1)–(3), in their notation, are

    (1−ε²∇²)t_ij=2μ e_ij+(λe−γθ)δ_ij,
    μ∇²u+(λ+μ)∇e−γ∇θ=ρ(1−ε²∇²)u_tt,
    (K*+Kt∂t)∇²θ=(∂t+τq∂tt)(ρCE θ_t+γT0 e_t).           (M1)

With the same longitudinal normalization as T2 and D=1+τq s, direct elimination gives

    P_M=(ρs²+Ck²/G)[c s²D+k²(K*+Kt s)]
         +(B/G)k²s²D.                                                (M2)

Our thermal factor becomes **exactly** that of M1/M2 when κ=0, identifying τq=τ, K*=h and Kt=kr+τh. The corresponding familiar MGT total-flux law is (1+τ∂t)q=−hα_x−(kr+τh)θ_x; it equals O3 at κ=0. For κ>0, O3 contains the extra −τκ θ_xt and O2 the extra τκk²s² term relative to this standard MGT law. This can still be represented by the first-order TPL law T4; it is not evidence of a new family. At η→0 and equal kernel lengths, mechanical stiffness matches M2, but the coupling term remains B rather than B/G because of the different placement of thermal stress. At ℓ=0, G=a=1, and κ=0, O2 and M2 coincide, provided coefficients and compatible initial data are matched. Their paper's dispersion is spatial-frequency based and includes shear waves and half-space boundary conditions; our polynomial comparison is the 1D longitudinal bulk reduction, not full equivalence of the boundary problems.

The MGT theory itself is due to **Ramón Quintanilla**, “Moore–Gibson–Thompson thermoelasticity,” *Mathematics and Mechanics of Solids* **24** (2019), 4020–4031, [doi:10.1177/1081286519862007](https://doi.org/10.1177/1081286519862007). **Original full text unverified**; M1 is explicitly presented by Das et al. as their equation based on Quintanilla. An independently accessible subsequent primary article, [Abouelregal et al., *Axioms* 12 (2023), 659](https://doi.org/10.3390/axioms12070659), states the exact standard MGT heat-flux equation q+τ0 q_t=−K∇θ−K*∇α; its additional electromagnetic geometry is different.

## 3. Two-phase local/nonlocal elasticity

**Pei Zhang and Hai Qing**, “Thermoelastic analysis of nanobar based on nonlocal integral elasticity and nonlocal integral heat conduction,” *Journal of Thermal Stresses* **44** (2021), 1244–1261, [doi:10.1080/01495739.2021.1967240](https://doi.org/10.1080/01495739.2021.1967240). **Abstract only; full equations unverified.** The abstract explicitly combines strain- and stress-driven two-phase local/nonlocal elastic integral models with two-phase nonlocal heat-conduction models. It is an existing thermoelastic mixture, but its kernel, dynamic evolution, thermal-displacement/relaxation law and dispersion cannot be identified from the abstract. No exact P comparison or claim of equivalence is justified.

**L. Meng, D. Zou, H. Lai et al.**, “Semi-analytic solution of Eringen’s two-phase local/nonlocal model for Euler-Bernoulli beam with axial force,” *Applied Mathematics and Mechanics* **39** (2018), 1805–1824, [doi:10.1007/s10483-018-2395-9](https://doi.org/10.1007/s10483-018-2395-9). **Abstract only; full equations unverified.** The abstract confirms Eringen two-phase local/nonlocal elasticity in a beam, not a thermal-flux model. Our operator is explicitly the usual local/nonlocal mixture of identity and periodic Helmholtz inverse; we have not verified whether its exact thermomechanical stress split, geometry and kernel match either article. Two-phase elasticity should not be confused with *two phase lags* in heat conduction.

## 4. Yu–Tian–Liu and follow-ups

There is a citation ambiguity worth correcting:

* **Y. Jun Yu, Xiao-Geng Tian and Xin-Rang Liu**, “Size-dependent generalized thermoelasticity using Eringen’s nonlocal model,” *European Journal of Mechanics – A/Solids* **51** (2015), 96–106, [doi:10.1016/j.euromechsol.2014.12.005](https://doi.org/10.1016/j.euromechsol.2014.12.005). **Publisher abstract and selected equation snippet only; full model unverified.** The abstract states differential Eringen elasticity plus fractional or memory-dependent heat transfer. Its displayed *local* constitutive snippet is σij=λεkkδij+2μεij−γθδij, ρη=γεkk+ρcEθ/T0. This snippet is not by itself the full nonlocal law; neither a heat-flux equation nor a dispersion match can be established from it. It does not verify the parallel flux, GN III, or two-phase mixture.
* **Y. Jun Yu, Xiao-Geng Tian and Q. L. Xiong**, “Nonlocal thermoelasticity based on nonlocal heat conduction and nonlocal elasticity,” *European Journal of Mechanics – A/Solids* **60** (2016), 238–253, [doi:10.1016/j.euromechsol.2016.08.004](https://doi.org/10.1016/j.euromechsol.2016.08.004). **Full text unverified**; citations disagree about the third author: the [publisher bibliography in the Abbas et al. 2022 primary paper](https://www.mdpi.com/2227-7390/10/13/2168) identifies Xiong, as do multiple independent publisher reference lists, while some later papers list Liu. Confirm against the 2016 title page before relying on authorship. The title and secondary citations identify both nonlocal heat conduction and elasticity, unlike our spatially local heat channel; full equations and P comparison unverified.
* **Ibrahim Abbas, Aatef Hobiny, Sorin Vlase and Marin Marin**, “Generalized Thermoelastic Interaction in a Half-Space under a Nonlocal Thermoelastic Model,” *Mathematics* **10** (2022), 2168, [doi:10.3390/math10132168](https://doi.org/10.3390/math10132168). **Publisher abstract inspected; complete equations unverified** because the accessible page extraction omitted mathematical expressions. The abstract states Eringen nonlocality plus LS relaxation; four local/nonlocal mechanical/thermal configurations are discussed. It is strong family-level overlap, but no honest exact flux or polynomial comparison is possible from the readable extract.

## 5. Exact citation for the three-phase-lag source

**Ramón Quintanilla**, “Some solutions for a family of exact phase-lag heat conduction problems,” *Mechanics Research Communications* **38**(5) (2011), 355–360, [doi:10.1016/j.mechrescom.2011.04.008](https://doi.org/10.1016/j.mechrescom.2011.04.008). **Publisher abstract and introduction inspected; full article unverified.** The source explicitly reports T3 and attributes it to Roy Choudhuri. The original source is **S. K. Roy Choudhuri**, “On a thermoelastic three-phase-lag model,” *Journal of Thermal Stresses* **30** (2007), 231–238, [doi:10.1080/01495730601130919](https://doi.org/10.1080/01495730601130919): **original full text unverified**. Equation T3 is transcribed from the accessible 2011 primary publisher abstract, not claimed to have been inspected in the 2007 original.

## Comparison summary

| Source | Primary access and exact evidence | Same as our law / P | Difference / unresolved |
|---|---|---|---|
| Tiwari–Kumar 2021 | Full governing equations T1 inspected | GN-type displacement, thermal-gradient lag, Eringen elasticity; T2 compares directly | Second-order flux lag; pure Helmholtz filters thermal stress; not mixed a(k); P_T≠P_O. First-order truncation is not their exact τq>0 model. |
| Three-phase-lag exact source; Roy Choudhuri 2007 | Publisher abstract equation T3; original 2007 unverified | First-order expansion T4 equals O3 exactly under T5, with compatible initial state | Exact delays are not O3; thermal equation correspondence does not prove thermomechanical or thermodynamic equivalence. |
| Das–De–Sarkar 2023 | Full governing equations M1 inspected | Nonlocal MGT, GN III/LS; O3 is MGT at κ=0; P agrees locally at κ=0 | Full nonlocal coupling is filtered by 1/G, unlike ours; mixed phase and κθ_xt term differ. |
| Zhang–Qing 2021 | Abstract only, full equations unverified | Two-phase elastic mixture in a thermoelastic model | Kernel/flux/dispersion not verified. |
| Meng et al. 2018 | Abstract only, full equations unverified | Eringen two-phase elastic mixture | Beam and mechanical-only comparison; no thermal equation or P checked. |
| Yu–Tian–Liu 2015 | Abstract and local constitutive snippet only; full model unverified | Eringen generalized thermoelasticity | Fractional/time-dependent heat treatment; no exact r or P comparison possible. |
| Yu–Tian–Xiong 2016 | Full text unverified | Nonlocal generalized thermoelasticity and heat conduction | Original equations and exact author list not independently read from title page; no P comparison. |
| Abbas et al. 2022 | Abstract inspected; math extraction incomplete | Eringen/LS relaxation and thermal nonlocality | Exact equation and P comparisons unverified. |

**Verdict: (b) a minor variant.** The eliminated thermal law is exactly a restricted first-order three-phase-lag law, and the κ=0 subcase is standard MGT; nonlocal MGT and nonlocal TPL thermoelastic wave models already exist. Our mixed elastic kernel, unfiltered thermal-stress coupling, explicit internal-flux storage and periodic energy calculation are identifiable formulation differences, but this search has not established their novelty, significance, or equivalence to all earlier models. No single inspected paper has been shown to reproduce every coefficient, constitutive state and boundary assumption of the full model, so this verdict does not assert exact identity of the complete model.
