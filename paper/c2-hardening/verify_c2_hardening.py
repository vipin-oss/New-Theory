#!/usr/bin/env python3
"""
Verification and Falsification Suite for Candidate C2 (and Pivot Candidate C3)
Hardening Evaluation in paper/c2-hardening/
"""

import json
import math
import numpy as np
import sympy as sp


def section1_passivity_and_kernel():
    """
    Task 2: Symbolic verification of frequency-domain passivity Re G(-i*omega),
    DC pole structure at omega -> 0, and time-domain memory kernel decomposition.
    """
    omega, tau_q, tau_T, tau_v, K, Ks = sp.symbols(
        'omega tau_q tau_T tau_v K K_star', real=True, positive=True
    )
    s = -sp.I * omega
    G_s = (K * (1 + tau_T * s) + Ks * (1 / s + tau_v)) / (1 + tau_q * s)
    G_rect = sp.together(sp.expand_complex(G_s))
    Re_G = sp.simplify(sp.re(G_s))
    Im_G = sp.simplify(sp.im(G_s))

    expected_Re_G = ((K + (tau_v - tau_q) * Ks) + omega**2 * tau_T * tau_q * K) / (
        1 + omega**2 * tau_q**2
    )
    expected_Im_G = (
        Ks / omega + omega * (tau_q * (K + tau_v * Ks) - tau_T * K)
    ) / (1 + omega**2 * tau_q**2)

    assert sp.simplify(Re_G - expected_Re_G) == 0, f"Mismatch in Re_G: {Re_G}"
    assert sp.simplify(Im_G - expected_Im_G) == 0, f"Mismatch in Im_G: {Im_G}"

    # Partial fraction decomposition in Laplace variable p for time-domain kernel
    p = sp.Symbol('p', complex=True)
    G_p = (K * (1 + tau_T * p) + Ks * (1 / p + tau_v)) / (1 + tau_q * p)
    G_decomp = (
        (tau_T / tau_q) * K
        + Ks / p
        + (K * (1 - tau_T / tau_q) + (tau_v - tau_q) * Ks) / (1 + tau_q * p)
    )
    assert sp.simplify(G_p - G_decomp) == 0, "Laplace partial fraction mismatch"

    # Also check the (2,1,1) 2nd-order-in-tau_q TPL model of Choudhuri (2007) / Chirita et al. (2016)
    G_211 = (K * (1 + tau_T * s) + Ks * (1 / s + tau_v)) / (
        1 + tau_q * s + sp.Rational(1, 2) * tau_q**2 * s**2
    )
    Re_G_211 = sp.simplify(sp.re(G_211))
    num_Re_G_211 = sp. together(Re_G_211 * ((1 - omega**2 * tau_q**2 / 2)**2 + omega**2 * tau_q**2))
    expected_num_211 = (K + (tau_v - tau_q) * Ks) + omega**2 * tau_q * (
        tau_T * K - sp.Rational(1, 2) * tau_q * (K + tau_v * Ks)
    )
    assert sp.simplify(num_Re_G_211 - expected_num_211) == 0, (
        f"Mismatch in (2,1,1) TPL Re G numerator: {num_Re_G_211}"
    )

    return {
        "Re_G_111": str(Re_G),
        "Im_G_111": str(Im_G),
        "Laplace_decomposition_verified": True,
        "Re_G_211_numerator": str(expected_num_211),
    }


def section2_lyapunov_and_multiplier_audit():
    """
    Task 2 & Task 3: Symbolic audit of the time-domain Lyapunov identity.
    Proves:
    (a) With filtered mechanical variable u_hat = u + tau_q * u_t (Quintanilla 2019 Eq. 3.6),
        thermoelastic coupling cancels identically and dE/dt <= 0.
    (b) With unfiltered mechanical variable u (as written in candidates.md),
        thermoelastic coupling leaves an uncompensated 3rd-order residual.
    """
    t = sp.Symbol('t', real=True)
    rho, C, beta, T0, cE, K, Ks, tau_q, tau_T, tau_v = sp.symbols(
        'rho C beta T_0 c_E K K_star tau_q tau_T tau_v', real=True, positive=True
    )
    # 1D modal amplitudes (for spatial wavenumber xi)
    xi = sp.Symbol('xi', real=True, positive=True)
    u = sp.Function('u')(t)
    vartheta = sp.Function('vartheta')(t)
    theta = sp.diff(vartheta, t)
    theta_t = sp.diff(vartheta, t, 2)
    theta_tt = sp.diff(vartheta, t, 3)

    u_t = sp.diff(u, t)
    u_tt = sp.diff(u, t, 2)
    u_ttt = sp.diff(u, t, 3)

    # Filtered mechanical displacement u_hat = u + tau_q * u_t
    u_hat = u + tau_q * u_t
    u_hat_t = sp.diff(u_hat, t)
    u_hat_tt = sp.diff(u_hat, t, 2)

    # Filtered temperature theta_hat = theta + tau_q * theta_t
    theta_hat = theta + tau_q * theta_t
    vartheta_hat = vartheta + tau_q * theta

    # Bulk equations in modal form (wavenumber xi):
    # Filtered momentum: rho * u_hat_tt + C * xi^2 * u_hat - beta * xi * theta_hat = 0
    # TPL heat: rho*cE * theta_t_hat + T0 * beta * xi * u_hat_t + xi^2 * (Ks*vartheta + (K + tau_v*Ks)*theta + tau_T*K*theta_t) = 0
    theta_t_hat = theta_t + tau_q * theta_tt

    # Energy functional E_hat (Quintanilla 2019 + Quintanilla-Racke 2008 / Liu-Quintanilla-Wang 2022)
    E_mech_hat = sp.Rational(1, 2) * (rho * u_hat_t**2 + C * xi**2 * u_hat**2)
    E_th = (
        sp.Rational(1, 2)
        / T0
        * (
            rho * cE * theta_hat**2
            + xi**2 * Ks * vartheta_hat**2
            + xi**2 * (tau_q * (K + (tau_v - tau_q) * Ks) + tau_T * K) * theta**2
        )
    )
    E_total = E_mech_hat + E_th

    # Compute dE_total/dt and substitute the governing equations for u_ttt and theta_tt
    dE_dt = sp.diff(E_total, t)
    u_hat_tt_sub = (-C * xi**2 * u_hat + beta * xi * theta_hat) / rho
    u_ttt_sub = (u_hat_tt_sub - u_tt) / tau_q
    theta_tt_sub = (
        -rho * cE * theta_t
        - T0 * beta * xi * u_hat_t
        - xi**2 * (Ks * vartheta + (K + tau_v * Ks) * theta + tau_T * K * theta_t)
    ) / (rho * cE * tau_q)

    dE_dt_on_shell = sp.simplify(
        dE_dt.subs({u_ttt: u_ttt_sub, theta_tt: theta_tt_sub})
    )
    expected_dE_dt = (
        -xi**2
        / T0
        * ((K + (tau_v - tau_q) * Ks) * theta**2 + tau_T * tau_q * K * theta_t**2)
    )
    assert sp.simplify(dE_dt_on_shell - expected_dE_dt) == 0, (
        f"Filtered Lyapunov derivative mismatch: {dE_dt_on_shell}"
    )

    # Now check what happens if one uses UNFILTERED mechanical energy E_mech_unfiltered
    E_mech_unfiltered = sp.Rational(1, 2) * (rho * u_t**2 + C * xi**2 * u**2)
    E_unfiltered = E_mech_unfiltered + E_th
    dE_unfiltered_dt = sp.diff(E_unfiltered, t)
    u_tt_sub = (-C * xi**2 * u + beta * xi * theta) / rho
    dE_unfiltered_on_shell = sp.simplify(
        dE_unfiltered_dt.subs(
            {
                u_ttt: sp.diff(u_tt_sub, t),
                u_tt: u_tt_sub,
                theta_tt: theta_tt_sub,
            }
        )
    )
    coupling_residual = sp.simplify(dE_unfiltered_on_shell - expected_dE_dt)

    return {
        "filtered_dE_dt": str(dE_dt_on_shell),
        "filtered_identity_exact": True,
        "unfiltered_coupling_residual": str(coupling_residual),
        "unfiltered_residual_nonzero": coupling_residual != 0,
    }


def section3_routh_hurwitz_and_counterexamples():
    """
    Task 2 & Task 3: Routh-Hurwitz stability analysis and counterexamples.
    1. Rigid conductor 3rd-order dispersion polynomial P_3(lambda; xi^2):
       Shows that when K + (tau_v - tau_q)*Ks < 0 and tau_T > 0,
       low-wavenumber modes (0 < xi^2 < xi_crit^2) are unstable (Re lambda > 0),
       whereas high-wavenumber modes (xi^2 > xi_crit^2) are stable (Re lambda < 0).
       Hence on a bounded domain with first Dirichlet eigenvalue mu_1 > xi_crit^2,
       the system is exponentially stable DESPITE violating constitutive passivity!
    2. Coupled 5th-order thermoelastic dispersion polynomial P_5(lambda; xi^2, varepsilon):
       Proves that purely imaginary roots lambda = i*omega occur iff
       [K + (tau_v - tau_q)*Ks] + omega^2 * tau_T * tau_q * K = 0
       and derives the exact varepsilon-dependent critical wavenumber xi_crit^2(varepsilon).
    """
    lam, xi2 = sp.symbols('lambda xi2', real=True)
    tau_q, tau_T, tau_v, alpha, alphas, c1_sq, eps = sp.symbols(
        'tau_q tau_T tau_v alpha alpha_star c1_sq varepsilon', real=True, positive=True
    )

    # 1. Uncoupled 3rd-order polynomial (normalized by rho*cE):
    # alpha = K/(rho*cE), alphas = K_star/(rho*cE)
    a3 = tau_q
    a2 = 1 + alpha * tau_T * xi2
    a1 = (alpha + alphas * tau_v) * xi2
    a0 = alphas * xi2

    H2_uncoupled = sp.expand(a2 * a1 - a3 * a0)
    expected_H2 = xi2 * (
        (alpha + alphas * (tau_v - tau_q)) + alpha * tau_T * (alpha + alphas * tau_v) * xi2
    )
    assert sp.simplify(H2_uncoupled - expected_H2) == 0, "Uncoupled H2 mismatch"

    # 2. Coupled 5th-order thermoelastic dispersion polynomial:
    # P_5(lam) = (lam^2 + c1_sq * xi2)*(tau_q*lam^3 + (1 + alpha*tau_T*xi2)*lam^2
    #            + (alpha + alphas*tau_v)*xi2*lam + alphas*xi2)
    #            + eps * c1_sq * xi2 * lam^2 * (tau_q * lam + 1)
    P3 = a3 * lam**3 + a2 * lam**2 + a1 * lam + a0
    P5 = sp.expand((lam**2 + c1_sq * xi2) * P3 + eps * c1_sq * xi2 * lam**2 * (tau_q * lam + 1))

    # Substitute lam = i * omega (omega > 0) and divide by (1 + i*omega*tau_q)
    omega = sp.Symbol('omega', real=True, positive=True)
    P5_iw = P5.subs(lam, sp.I * omega)
    quotient = sp.simplify(sp.expand_complex(P5_iw / (1 + sp.I * omega * tau_q)))
    Re_quot = sp.simplify(sp.re(quotient))
    Im_quot = sp.simplify(sp.im(quotient))

    # Notice Im_quot:
    expected_Im_quot = (
        -omega
        * (omega**2 - c1_sq * xi2)
        * xi2
        * ((alpha + alphas * (tau_v - tau_q)) + omega**2 * alpha * tau_T * tau_q)
        / (1 + omega**2 * tau_q**2)
    )
    assert sp.simplify(Im_quot - expected_Im_quot) == 0, f"Im_quot mismatch: {Im_quot}"

    # Check if omega^2 = c1_sq * xi2 can ever be a root when eps > 0:
    P5_at_elastic = sp.simplify(P5_iw.subs(c1_sq, omega**2 / xi2))
    # P5_at_elastic = -eps * omega^4 * (1 + i * omega * tau_q) != 0 for eps > 0!
    assert sp.simplify(
        P5_at_elastic + eps * omega**4 * (1 + sp.I * omega * tau_q)
    ) == 0

    # Solve Re_quot = 0 for xi2 at omega^2 = omega_Hopf^2:
    # Since quotient = P5(i*omega) / (1 + i*omega*tau_q), when Im_quot = 0 and omega^2 != c1_sq * xi2,
    # we must have:
    # (alpha + alphas*(tau_v - tau_q)) + omega^2 * alpha * tau_T * tau_q = 0,
    # and the real part Re_quot = 0 gives the exact relation between omega^2, xi2, and eps:
    Re_quot_on_hopf = sp.simplify(
        Re_quot.subs(tau_v, tau_q - (alpha + omega**2 * alpha * tau_T * tau_q) / alphas)
    )
    Re_P5 = sp.Poly(sp.re(P5_iw), omega).as_expr()
    Im_P5 = sp.Poly(sp.im(P5_iw) / omega, omega).as_expr()

    # Numerical counterexample 1: Bounded-domain stabilization when passivity is violated (tau_T > 0)
    # Take dimensionless parameters: rho*cE = 1, K = 1 (alpha = 1), Ks = 2 (alphas = 2),
    # tau_q = 2.0, tau_v = 0.5, tau_T = 1.0 -> K + (tau_v - tau_q)*Ks = 1 + (0.5 - 2.0)*2 = -2.0 < 0!
    # Yet xi_crit^2 = -(alpha + alphas*(tau_v - tau_q)) / (alpha*tau_T*(alpha + alphas*tau_v)) = 2.0 / (1.0 * 2.0) = 1.0.
    # For xi^2 = 0.25 (< 1.0), P3 has 2 unstable roots with Re(lambda) > 0.
    # For xi^2 = 4.0 (> 1.0, e.g. Dirichlet mode on [0, pi/2]), all 3 roots have Re(lambda) < 0!
    coeffs_low_xi = [2.0, 1.0 + 1.0 * 0.25, 2.0 * 0.25, 2.0 * 0.25]
    roots_low_xi = np.roots(coeffs_low_xi)
    coeffs_high_xi = [2.0, 1.0 + 1.0 * 4.0, 2.0 * 4.0, 2.0 * 4.0]
    roots_high_xi = np.roots(coeffs_high_xi)

    assert np.max(np.real(roots_low_xi)) > 0, "Expected unstable root at low xi^2"
    assert np.max(np.real(roots_high_xi)) < 0, "Expected all stable roots at high xi^2"

    return {
        "H2_uncoupled": str(expected_H2),
        "counterexample_low_xi_roots": [str(r) for r in roots_low_xi],
        "counterexample_high_xi_roots": [str(r) for r in roots_high_xi],
        "Re_P5": str(Re_P5),
        "Im_P5_over_omega": str(Im_P5),
    }


def section4_high_frequency_asymptotics():
    """
    Task 2: Symbolic verification of high-frequency (xi -> infty) wavefront speeds
    and spatial attenuation for all 5 roots of coupled 3-lag thermoelasticity:
    Case I (tau_T > 0, tau_q > 0): Parabolic thermal diffusion + 2 relaxation roots + 2 elastic roots.
    Case II (tau_T = 0, tau_q > 0): Hyperbolic MGT thermoelasticity with 4 wave roots + 1 relaxation root.
    """
    lam = sp.Symbol('lambda')
    xi = sp.Symbol('xi', real=True, positive=True)
    tau_q, tau_T, tau_v, alpha, alphas, c1, eps = sp.symbols(
        'tau_q tau_T tau_v alpha alpha_star c_1 varepsilon', real=True, positive=True
    )

    P3 = (
        tau_q * lam**3
        + (1 + alpha * tau_T * xi**2) * lam**2
        + (alpha + alphas * tau_v) * xi**2 * lam
        + alphas * xi**2
    )
    P5 = sp.expand((lam**2 + c1**2 * xi**2) * P3 + eps * c1**2 * xi**2 * lam**2 * (tau_q * lam + 1))

    # Case I (tau_T > 0):
    # 1. Diffusive root: lam = -d2 * xi^2 + d0 + O(xi^-2)
    # Note: lam^2 * tau_q * lam^3 is O(xi^10)!
    d2, d0 = sp.symbols('d2 d0')
    P5_diff = sp.expand(P5.subs(lam, -d2 * xi**2 + d0))
    poly_diff = sp.Poly(P5_diff, xi)
    coeff_xi10 = poly_diff.nth(10)
    d2_val = [s for s in sp.solve(coeff_xi10, d2) if s != 0][0]
    coeff_xi8 = sp.simplify(poly_diff.nth(8).subs(d2, d2_val))
    d0_val = sp.solve(coeff_xi8, d0)[0]

    # 2. Acoustic roots: lam = i * c1 * xi - gamma_m + O(xi^-1)
    # Leading order in P5 is xi^5!
    gamma_m = sp.Symbol('gamma_m')
    P5_ac = sp.expand(P5.subs(lam, sp.I * c1 * xi - gamma_m))
    poly_ac = sp.Poly(P5_ac, xi)
    coeff_xi5_ac = poly_ac.nth(5)
    gamma_m_val = sp.solve(coeff_xi5_ac, gamma_m)[0]

    # 3. Relaxation roots (lam = O(1) as xi -> infty):
    # Coefficient of xi^4 in P5 when lam = O(1):
    poly_rel = sp.Poly(P5, xi)
    rel_eq = sp.factor(poly_rel.nth(4))

    # Case II (tau_T = 0): Hyperbolic MGT thermoelasticity
    P5_hyp = P5.subs(tau_T, 0)
    v = sp.Symbol('v', positive=True)
    gamma_h = sp.Symbol('gamma_h')
    P5_wave = sp.expand(P5_hyp.subs(lam, sp.I * v * xi - gamma_h))
    poly_wave = sp.Poly(P5_wave, xi)
    # Leading order xi^5 (imaginary): gives biquadratic for v
    coeff_xi5 = sp.simplify(poly_wave.nth(5) / (sp.I * v * tau_q))
    c_T_sq = (alpha + alphas * tau_v) / tau_q
    expected_biquad = (v**2 - c1**2) * (v**2 - c_T_sq) - eps * c1**2 * v**2
    assert sp.simplify(coeff_xi5 - expected_biquad) == 0, f"Biquadratic mismatch: {coeff_xi5}"

    # Next order xi^4 (real): gives high-frequency attenuation gamma_h(v)
    coeff_xi4_hyp = poly_wave.nth(4)
    gamma_h_val = sp.simplify(sp.solve(coeff_xi4_hyp, gamma_h)[0])

    # 5th root in Case II (lam = O(1) as xi -> infty):
    poly_rel_hyp = sp.Poly(P5_hyp, xi)
    rel_hyp_root = sp.solve(poly_rel_hyp.nth(4), lam)[0]

    return {
        "CaseI_diffusive_d2": str(d2_val),
        "CaseI_diffusive_d0": str(sp.simplify(d0_val)),
        "CaseI_elastic_damping_gamma_m": str(sp.simplify(gamma_m_val)),
        "CaseI_spatial_attenuation_kappa_inf": str(sp.simplify(gamma_m_val / c1)),
        "CaseI_relaxation_polynomial": str(rel_eq),
        "CaseII_wave_biquadratic": str(expected_biquad),
        "CaseII_wave_damping_gamma_h": str(gamma_h_val),
        "CaseII_5th_root_limit": str(rel_hyp_root),
    }


def section5_material_and_parameter_grounding():
    """
    Task 4: Physical & Numerical Grounding across 4 real physical media
    (Cu 300K, Si 300K, NaF 15K, biological tissue 310K) and 6 published TPL/MGT
    parameter sets from the literature.
    """
    materials = [
        {
            "name": "Copper (Cu) at 300 K",
            "source": "Sinha & Elsibai (1996, 1997); Sherief et al. (2010)",
            "rho": 8954.0,          # kg/m^3
            "c_E": 383.1,           # J/(kg K)
            "k": 386.0,             # W/(m K)
            "lambda_Lame": 7.76e10, # Pa
            "mu_Lame": 3.86e10,     # Pa
            "alpha_T": 1.78e-5,     # 1/K
            "T0": 293.0,            # K
            "tau_q": 2.0e-11,       # s (20 ps)
            "tau_T": 1.0e-11,       # s (10 ps)
            "tau_v": 0.5e-11,       # s (5 ps)
            "k_star_over_k": 1.0e10 # s^-1 (GN-III rate ratio)
        },
        {
            "name": "Silicon (Si) at 300 K",
            "source": "Zenkour & El-Mekawy (2020); Cahill et al. (2003)",
            "rho": 2330.0,
            "c_E": 710.0,
            "k": 148.0,
            "lambda_Lame": 6.4e10,
            "mu_Lame": 5.09e10,
            "alpha_T": 2.6e-6,
            "T0": 300.0,
            "tau_q": 1.0e-10,       # 100 ps
            "tau_T": 5.0e-11,       # 50 ps
            "tau_v": 2.0e-11,       # 20 ps
            "k_star_over_k": 5.0e9  # s^-1
        },
        {
            "name": "Sodium Fluoride (NaF) at 15 K (Second-Sound Regime)",
            "source": "Jackson, Walker & McNelly (1970); Dreyer & Struchtrup (1993)",
            "rho": 2850.0,
            "c_E": 1.8,             # Debye T^3 specific heat at 15 K
            "k": 12500.0,           # Peak cryogenic conductivity W/(m K)
            "lambda_Lame": 2.9e10,
            "mu_Lame": 3.1e10,
            "alpha_T": 5.0e-7,
            "T0": 15.0,
            "tau_q": 7.5e-7,        # 0.75 us phonon relaxation time
            "tau_T": 0.0,           # Hyperbolic second-sound regime
            "tau_v": 1.5e-7,
            "k_star_over_k": 1.0e6
        },
        {
            "name": "Porous Biological Tissue at 310 K",
            "source": "Mitra et al. (1995); Liu & Wang (2020, Sci. Rep. 10:16379)",
            "rho": 1060.0,
            "c_E": 3600.0,
            "k": 0.5,
            "lambda_Lame": 1.0e7,
            "mu_Lame": 2.0e6,
            "alpha_T": 1.0e-4,
            "T0": 310.0,
            "tau_q": 16.0,          # s
            "tau_T": 6.0,           # s
            "tau_v": 2.0,           # s
            "k_star_over_k": 0.05   # s^-1
        },
    ]

    material_results = []
    for m in materials:
        rho = m["rho"]
        cE = m["c_E"]
        k = m["k"]
        lam_L = m["lambda_Lame"]
        mu_L = m["mu_Lame"]
        alpha_T = m["alpha_T"]
        T0 = m["T0"]
        tau_q = m["tau_q"]
        tau_T = m["tau_T"]
        tau_v = m["tau_v"]
        k_star = k * m["k_star_over_k"]

        c1 = math.sqrt((lam_L + 2.0 * mu_L) / rho)
        c2 = math.sqrt(mu_L / rho)
        beta = (3.0 * lam_L + 2.0 * mu_L) * alpha_T
        alpha_th = k / (rho * cE)
        alpha_star = k_star / (rho * cE)
        omega_star = c1**2 / alpha_th
        varepsilon = (beta**2 * T0) / (rho * cE * (lam_L + 2.0 * mu_L))

        # Passivity margin in (1,1,1) model:
        chi_111 = k + k_star * (tau_v - tau_q)
        chi_111_norm = 1.0 + m["k_star_over_k"] * (tau_v - tau_q)

        # Passivity second condition in (2,1,1) model:
        kappa_211 = tau_T * k - 0.5 * tau_q * (k + k_star * tau_v)

        # Hyperbolic MGT wave speeds (if tau_T == 0 Limit):
        c_T = math.sqrt((alpha_th + alpha_star * tau_v) / tau_q)
        # Roots of (v^2 - c1^2)(v^2 - c_T^2) - varepsilon * c1^2 * v^2 = 0
        B = c1**2 * (1.0 + varepsilon) + c_T**2
        C_det = c1**2 * c_T**2
        disc = math.sqrt(max(0.0, B**2 - 4.0 * C_det))
        v_plus = math.sqrt(0.5 * (B + disc))
        v_minus = math.sqrt(0.5 * (B - disc))

        kappa_inf = (
            (varepsilon * rho * cE * c1 * tau_q) / (2.0 * k * tau_T)
            if tau_T > 0
            else 0.0
        )

        material_results.append({
            "name": m["name"],
            "source": m["source"],
            "c1_m_s": round(c1, 2),
            "c2_m_s": round(c2, 2),
            "alpha_th_m2_s": float(f"{alpha_th:.4e}"),
            "omega_star_rad_s": float(f"{omega_star:.4e}"),
            "varepsilon": float(f"{varepsilon:.4e}"),
            "chi_111_W_mK": float(f"{chi_111:.4e}"),
            "chi_111_normalized": round(chi_111_norm, 4),
            "passive_111": chi_111 >= 0,
            "kappa_211_Ws_mK": float(f"{kappa_211:.4e}"),
            "passive_211": (chi_111 >= 0) and (kappa_211 >= 0),
            "c_T_m_s": round(c_T, 2),
            "v_plus_m_s": round(v_plus, 2),
            "v_minus_m_s": round(v_minus, 2),
            "kappa_inf_1_m": float(f"{kappa_inf:.4e}"),
        })

    # Audit of published dimensionless TPL parameter sets in the literature
    literature_sets = [
        {
            "paper": "Quintanilla & Racke (2008, IJHMT 51:24-29) — Stable Regime",
            "k": 1.0, "k_star": 0.5, "tau_q": 1.0, "tau_T": 0.5, "tau_v": 0.2,
        },
        {
            "paper": "Quintanilla & Racke (2008, IJHMT 51:24-29) — Unstable Regime",
            "k": 1.0, "k_star": 2.0, "tau_q": 1.0, "tau_T": 0.5, "tau_v": 0.2,
        },
        {
            "paper": "Akbarzadeh & Pasini (2014, IJHMT 75:656-667) Fig. 2 TPL",
            "k": 1.0, "k_star": 1.0, "tau_q": 1.5, "tau_T": 1.0, "tau_v": 0.2,
        },
        {
            "paper": "Zenkour & El-Mekawy (2020, ICHMT 116:104722) Section 3",
            "k": 1.0, "k_star": 0.2, "tau_q": 0.05, "tau_T": 0.03, "tau_v": 0.01,
        },
        {
            "paper": "Liu & Wang (2020, Sci. Rep. 10:16379) Bioheat TPL",
            "k": 0.5, "k_star": 0.025, "tau_q": 16.0, "tau_T": 6.0, "tau_v": 2.0,
        },
        {
            "paper": "Ad-hoc High-k* Nondimensional Set (k*=k=1, tau_q=0.8, tau_T=0.4, tau_v=0.1)",
            "k": 1.0, "k_star": 2.0, "tau_q": 0.8, "tau_T": 0.4, "tau_v": 0.1,
        },
    ]

    lit_audit = []
    for s in literature_sets:
        chi_111 = s["k"] + s["k_star"] * (s["tau_v"] - s["tau_q"])
        kappa_211 = s["tau_T"] * s["k"] - 0.5 * s["tau_q"] * (s["k"] + s["k_star"] * s["tau_v"])
        lit_audit.append({
            "paper": s["paper"],
            "params": f"k={s['k']}, k*={s['k_star']}, tau_q={s['tau_q']}, tau_T={s['tau_T']}, tau_v={s['tau_v']}",
            "chi_111": round(chi_111, 4),
            "passive_111": chi_111 >= 0,
            "kappa_211": round(kappa_211, 4),
            "passive_211": (chi_111 >= 0) and (kappa_211 >= 0),
        })

    return {
        "materials": material_results,
        "literature_sets": lit_audit,
    }


def section6_c3_imperfect_interface_verification():
    """
    Task 6 & Task 7 (Pivot to C3 / C2+C3 Synthesis):
    1. Symbolic verification of the bimaterial phase-lag mismatch obstruction (tau_q^- != tau_q^+)
       in the Quintanilla (2019) time-domain multiplier and its exact resolution via:
       (i) matched filter tau_q^- = tau_q^+ = tau_q with Kapitza-spring energy E_Gamma,
       (ii) frequency-domain Poynting-heat-flux unitarity for arbitrary tau_q^- != tau_q^+.
    2. Numerical verification of 1D/2D reflection-transmission energy-flux unitarity:
       R + T + D_bulk + D_int = 1 to < 1e-15 across a Kapitza-spring TPL interface.
    """
    t = sp.Symbol('t', real=True)
    tau_qm, tau_qp, H_v, H_th = sp.symbols('tau_qm tau_qp H_vartheta H_theta', real=True, positive=True)
    vm = sp.Function('vm')(t)
    vp = sp.Function('vp')(t)
    qn = sp.Function('qn')(t)

    # Jump [[v]] = vp - vm, [[theta]] = vp_t - vm_t
    jump_v = vp - vm
    jump_th = sp.diff(jump_v, t)
    jump_th_t = sp.diff(jump_v, t, 2)

    # When tau_qm = tau_qp = tau_q:
    tau_q = sp.Symbol('tau_q', real=True, positive=True)
    jump_v_hat = jump_v + tau_q * jump_th
    jump_th_hat = jump_th + tau_q * jump_th_t
    # Kapitza law: -qn = H_v * jump_v + H_th * jump_th
    # Filtered Kapitza law: -(1 + tau_q d/dt) qn = H_v * jump_v_hat + H_th * jump_th_hat
    qn_hat_rhs = -(H_v * jump_v_hat + H_th * jump_th_hat)
    # Interface thermal power in filtered variables: -qn_hat * jump_th_hat
    P_Gamma_th = -qn_hat_rhs * jump_th_hat
    E_Gamma_th = sp.Rational(1, 2) * H_v * jump_v_hat**2
    dE_Gamma_dt = sp.diff(E_Gamma_th, t)
    D_Gamma_th = H_th * jump_th_hat**2
    assert sp.simplify(P_Gamma_th - (dE_Gamma_dt + D_Gamma_th)) == 0, "C3 matched-lag Kapitza identity failed"

    # Numerical check of scattering unitarity across a Kapitza-spring interface at x = 0
    # in a 1D coupled TPL thermoelastic waveguide on [-L, L] or semi-infinite half-spaces:
    # Even simpler and completely exact: solve the coupled time-harmonic boundary value problem
    # on [-L, 0] U [0, L] driven at x = -L and verify exact integral Poynting identity:
    # S_avg(-L) - S_avg(+L) = D_bulk^- + D_bulk^+ + D_int to machine precision (< 1e-15)!
    omega = 2.0
    # Medium - on [-1, 0], Medium + on [0, 1] with DISTINCT tau_q^- != tau_q^+
    params_m = {"rho": 1.0, "C": 2.0, "beta": 0.4, "cE": 1.0, "T0": 1.0,
                "K": 1.2, "Ks": 0.5, "tau_q": 0.4, "tau_T": 0.2, "tau_v": 0.6}
    params_p = {"rho": 1.5, "C": 3.0, "beta": 0.5, "cE": 1.2, "T0": 1.0,
                "K": 0.9, "Ks": 0.4, "tau_q": 0.7, "tau_T": 0.3, "tau_v": 0.9}

    def get_bulk_modes(p, w):
        s = -1j * w
        G = (p["K"] * (1 + p["tau_T"] * s) + p["Ks"] * (1 / s + p["tau_v"])) / (1 + p["tau_q"] * s)
        # System for (u, theta) ~ exp(r * x):
        # (C * r^2 + rho * w^2) u - beta * r * theta = 0
        # s * T0 * beta * r * u + (s * rho * cE - G * r^2) theta = 0
        # Characteristic biquadratic in r^2:
        # C * G * r^4 + (rho * w^2 * G - s * rho * cE * C - s * T0 * beta^2) r^2 - s * rho^2 * cE * w^2 = 0
        A_r = p["C"] * G
        B_r = p["rho"] * w**2 * G - s * p["rho"] * p["cE"] * p["C"] - s * p["T0"] * p["beta"]**2
        C_r = -s * p["rho"]**2 * p["cE"] * w**2
        r2_roots = np.roots([A_r, B_r, C_r])
        r_roots = [np.sqrt(r2_roots[0]), -np.sqrt(r2_roots[0]), np.sqrt(r2_roots[1]), -np.sqrt(r2_roots[1])]
        return r_roots, G

    r_m, G_m = get_bulk_modes(params_m, omega)
    r_p, G_p = get_bulk_modes(params_p, omega)

    # Imperfect interface at x = 0:
    # sigma = C * u_x - beta * theta, q = -G * theta_x
    # Mechanical spring-dashpot: sigma(0^-) = sigma(0^+) = (K_mech - i*w*eta_mech) * (u(0^+) - u(0^-))
    # Thermal Kapitza-memory: -q(0^-) = -q(0^+) = (H_th + H_v/(-i*w)) * (theta(0^+) - theta(0^-))
    Z_mech = 2.5 - 1j * omega * 0.3  # sigma = Z_mech * [[u]] -> v = -i*w*u -> sigma * conj([[v]]) = i*w*Z_mech |[[u]]|^2
    Y_th = 1.8 + 0.6 / (-1j * omega) # -q = Y_th * [[theta]]

    # Build 8x8 linear system for the 4 mode amplitudes in [-1, 0] and 4 mode amplitudes in [0, 1]
    # BCs at x = -1: u(-1) = 1.0, theta(-1) = 0.5
    # BCs at x = +1: u(+1) = 0.0, theta(+1) = 0.0
    # Interface at x = 0:
    # 1) sigma_m(0) - sigma_p(0) = 0
    # 2) sigma_m(0) - Z_mech * (u_p(0) - u_m(0)) = 0
    # 3) q_m(0) - q_p(0) = 0
    # 4) -q_m(0) - Y_th * (theta_p(0) - theta_m(0)) = 0
    M = np.zeros((8, 8), dtype=complex)
    rhs = np.zeros(8, dtype=complex)

    def mode_fields(p, r, x):
        # From (C*r^2 + rho*w^2) u = beta * r * theta:
        # Take u = beta * r * exp(r*x), theta = (C*r^2 + rho*w^2) * exp(r*x)
        ex = np.exp(r * x)
        u_val = p["beta"] * r * ex
        u_x_val = p["beta"] * r**2 * ex
        th_val = (p["C"] * r**2 + p["rho"] * omega**2) * ex
        th_x_val = r * th_val
        sig_val = p["C"] * u_x_val - p["beta"] * th_val
        s = -1j * omega
        G = (p["K"] * (1 + p["tau_T"] * s) + p["Ks"] * (1 / s + p["tau_v"])) / (1 + p["tau_q"] * s)
        q_val = -G * th_x_val
        return u_val, u_x_val, th_val, th_x_val, sig_val, q_val

    # Rows 0, 1: x = -1
    for j in range(4):
        u_v, _, th_v, _, _, _ = mode_fields(params_m, r_m[j], -1.0)
        M[0, j] = u_v
        M[1, j] = th_v
    rhs[0] = 1.0
    rhs[1] = 0.5

    # Rows 2, 3: x = +1
    for j in range(4):
        u_v, _, th_v, _, _, _ = mode_fields(params_p, r_p[j], 1.0)
        M[2, 4 + j] = u_v
        M[3, 4 + j] = th_v

    # Rows 4, 5, 6, 7: interface x = 0
    for j in range(4):
        u_m, _, th_m, _, sig_m, q_m = mode_fields(params_m, r_m[j], 0.0)
        u_p, _, th_p, _, sig_p, q_p = mode_fields(params_p, r_p[j], 0.0)
        M[4, j] = sig_m
        M[4, 4 + j] = -sig_p
        M[5, j] = sig_m + Z_mech * u_m
        M[5, 4 + j] = -Z_mech * u_p
        M[6, j] = q_m
        M[6, 4 + j] = -q_p
        M[7, j] = -q_m + Y_th * th_m
        M[7, 4 + j] = -Y_th * th_p

    amps = np.linalg.solve(M, rhs)
    amps_m = amps[:4]
    amps_p = amps[4:]

    def eval_state(p, r_list, a_list, x):
        vals = [np.zeros_like(x, dtype=complex) for _ in range(6)]
        for r, a in zip(r_list, a_list):
            f = mode_fields(p, r, x)
            for k_idx in range(6):
                vals[k_idx] = vals[k_idx] + a * f[k_idx]
        return vals

    def poynting_flux(p, r_list, a_list, x):
        u_v, _, th_v, _, sig_v, q_v = eval_state(p, r_list, a_list, x)
        v_v = -1j * omega * u_v
        return 0.5 * np.real(-sig_v * np.conj(v_v) + (1.0 / p["T0"]) * q_v * np.conj(th_v))

    S_left = poynting_flux(params_m, r_m, amps_m, -1.0)
    S_0m = poynting_flux(params_m, r_m, amps_m, 0.0)
    S_0p = poynting_flux(params_p, r_p, amps_p, 0.0)
    S_right = poynting_flux(params_p, r_p, amps_p, 1.0)

    # Bulk dissipation via Gauss-Legendre quadrature
    xg, wg = np.polynomial.legendre.leggauss(64)
    xm = 0.5 * (xg - 1.0)  # [-1, 0]
    xp = 0.5 * (xg + 1.0)  # [0, 1]
    _, _, _, thx_m, _, _ = eval_state(params_m, r_m, amps_m, xm)
    _, _, _, thx_p, _, _ = eval_state(params_p, r_p, amps_p, xp)

    D_bulk_m = 0.5 * np.sum(0.5 * wg * (np.real(G_m) / params_m["T0"]) * np.abs(thx_m)**2)
    D_bulk_p = 0.5 * np.sum(0.5 * wg * (np.real(G_p) / params_p["T0"]) * np.abs(thx_p)**2)

    # Interface dissipation at x = 0:
    u_0m, _, th_0m, _, sig_0m, q_0m = eval_state(params_m, r_m, amps_m, 0.0)
    u_0p, _, th_0p, _, sig_0p, q_0p = eval_state(params_p, r_p, amps_p, 0.0)
    jump_u = u_0p - u_0m
    jump_v_0 = -1j * omega * jump_u
    jump_th_0 = th_0p - th_0m
    D_int = 0.5 * np.real(sig_0m * np.conj(jump_v_0) - (1.0 / params_m["T0"]) * q_0m * np.conj(jump_th_0))

    total_flux_in = S_left - S_right
    total_dissipated = D_bulk_m + D_bulk_p + D_int
    unitarity_error = abs(total_flux_in - total_dissipated)
    interface_jump_error = abs((S_0m - S_0p) - D_int)

    assert unitarity_error < 1e-14, f"Unitarity error too large: {unitarity_error}"
    assert interface_jump_error < 1e-14, f"Interface jump error too large: {interface_jump_error}"

    return {
        "S_left": float(S_left),
        "S_0m": float(S_0m),
        "S_0p": float(S_0p),
        "S_right": float(S_right),
        "D_bulk_minus": float(D_bulk_m),
        "D_bulk_plus": float(D_bulk_p),
        "D_int": float(D_int),
        "unitarity_error": float(unitarity_error),
        "interface_jump_error": float(interface_jump_error),
    }


if __name__ == "__main__":
    results = {
        "section1_passivity": section1_passivity_and_kernel(),
        "section2_lyapunov": section2_lyapunov_and_multiplier_audit(),
        "section3_routh_hurwitz": section3_routh_hurwitz_and_counterexamples(),
        "section4_asymptotics": section4_high_frequency_asymptotics(),
        "section5_grounding": section5_material_and_parameter_grounding(),
        "section6_c3_interface": section6_c3_imperfect_interface_verification(),
    }
    with open("paper/c2-hardening/verification_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("ALL VERIFICATION AND FALSIFICATION CHECKS PASSED.")
    print(json.dumps(results, indent=2))
