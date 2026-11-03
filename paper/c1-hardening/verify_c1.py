"""
Independent Symbolic (SymPy) and Numerical (NumPy/SciPy) Verification for Candidate C1:
- Theorem 1: Master Two-Phase Nonlocal Helmholtz Free Energy Psi_lambda[eps, theta],
             Variants V1 (lambda=0) and V2 (lambda=1), and Betti-Maxwell reciprocity.
- Theorem 2: Non-existence of free energy, closed-cycle Clausius-Duhem violation,
             uncancelled availability residual, and broken reciprocity for Form A + local heating.
- Theorem 3: Exact integral-to-differential equivalence on [a, b] and [0, inf) via
             Two-Phase Thermoelastic Robin CBCs (3 decaying modes for V1, 4 decaying modes for V2,
             vs 2-mode collapse for gamma=0 Form A).
- Theorem 4: Exact nonlocal availability & surface-energy identity under Robin CBCs.
"""

from __future__ import annotations
import numpy as np
import sympy as sp


# =============================================================================
# 1. Theorem 1 & Theorem 2 Symbolic Checks (SymPy)
# =============================================================================

def symbolic_master_free_energy_and_cycle_check() -> dict:
    """
    Symbolically verify:
      1) Frechet derivatives of the master spectral free energy density psi_lambda
         at lambda=0 (V1) and lambda=1 (V2).
      2) Mixed second Frechet symmetry for all lambda in [0, 1] and failure for Form A + local entropy.
      3) Exact closed-cycle integral R_cycle = oint int (sigma * eps_t - rho*eta * theta_t) dx dt
         over x in [0, 2*pi/k] and t in [0, 2*pi/omega].
    """
    eps, theta = sp.symbols("eps theta", real=True)
    E, beta, rho, cE, T0 = sp.symbols("E beta rho cE T0", positive=True)
    ell, k, omega, t, x = sp.symbols("ell k omega t x", positive=True)
    gamma, lam = sp.symbols("gamma lam", real=True)
    eps0, theta0 = sp.symbols("eps0 theta0", real=True)

    # Fourier symbol of K_ell and L_{gamma, ell} and M_{lambda, gamma, ell}
    K_hat = 1 / (1 + ell**2 * k**2)
    L_hat = gamma + (1 - gamma) * K_hat
    M_hat = (1 - lam) + lam * L_hat

    # Spectral free energy density for a mode at wavenumber k
    psi_lam = sp.Rational(1, 2) * E * L_hat * eps**2 - beta * M_hat * eps * theta - (rho * cE / (2 * T0)) * theta**2

    sigma_lam = sp.diff(psi_lam, eps)
    rho_eta_lam = -sp.diff(psi_lam, theta)

    # Check V1 (lam = 0) and V2 (lam = 1)
    sigma_V1 = sp.simplify(sigma_lam.subs(lam, 0) - (E * L_hat * eps - beta * theta))
    eta_V1 = sp.simplify(rho_eta_lam.subs(lam, 0) - ((rho * cE / T0) * theta + beta * eps))

    sigma_V2 = sp.simplify(sigma_lam.subs(lam, 1) - L_hat * (E * eps - beta * theta))
    eta_V2 = sp.simplify(rho_eta_lam.subs(lam, 1) - ((rho * cE / T0) * theta + L_hat * beta * eps))

    # Mixed second Frechet symmetry: d(sigma)/d(theta) + d(rho*eta)/d(eps) == 0
    reciprocity_master = sp.simplify(sp.diff(sigma_lam, theta) + sp.diff(rho_eta_lam, eps))

    # Form A stress + local entropy (Class 1 in 12/25 coupled literature papers):
    sigma_FormA = K_hat * (E * eps - beta * theta)
    rho_eta_FormA = (rho * cE / T0) * theta + beta * eps
    reciprocity_FormA_defect = sp.simplify(sp.diff(sigma_FormA, theta) + sp.diff(rho_eta_FormA, eps))
    expected_FormA_defect = sp.simplify(beta * ell**2 * k**2 / (1 + ell**2 * k**2))

    # Closed harmonic standing-wave cycle on [0, 2*pi/k] x [0, 2*pi/omega]:
    eps_xt = eps0 * sp.cos(k * x) * sp.cos(omega * t)
    theta_xt = theta0 * sp.cos(k * x) * sp.sin(omega * t)
    eps_t = sp.diff(eps_xt, t)
    theta_t = sp.diff(theta_xt, t)

    # Integrate cycle residual for master family (covers V1 at lam=0 and V2 at lam=1)
    sig_xt_master = (E * L_hat * eps0 * sp.cos(omega * t) - beta * M_hat * theta0 * sp.sin(omega * t)) * sp.cos(k * x)
    eta_xt_master = ((rho * cE / T0) * theta0 * sp.sin(omega * t) + beta * M_hat * eps0 * sp.cos(omega * t)) * sp.cos(k * x)
    integrand_master = sig_xt_master * eps_t - eta_xt_master * theta_t
    R_cycle_master = sp.simplify(
        sp.integrate(sp.integrate(integrand_master, (x, 0, 2 * sp.pi / k)), (t, 0, 2 * sp.pi / omega))
    )

    # Integrate cycle residual for mismatched Form A + local entropy
    sig_xt_FA = K_hat * (E * eps0 * sp.cos(omega * t) - beta * theta0 * sp.sin(omega * t)) * sp.cos(k * x)
    eta_xt_FA = ((rho * cE / T0) * theta0 * sp.sin(omega * t) + beta * eps0 * sp.cos(omega * t)) * sp.cos(k * x)
    integrand_FA = sig_xt_FA * eps_t - eta_xt_FA * theta_t
    R_cycle_FormA = sp.simplify(
        sp.integrate(sp.integrate(integrand_FA, (x, 0, 2 * sp.pi / k)), (t, 0, 2 * sp.pi / omega))
    )
    expected_R_cycle_FormA = -sp.pi**2 * beta * eps0 * theta0 * ell**2 * k / (1 + ell**2 * k**2)

    return {
        "sigma_V1_residual": sigma_V1,
        "eta_V1_residual": eta_V1,
        "sigma_V2_residual": sigma_V2,
        "eta_V2_residual": eta_V2,
        "reciprocity_master_residual": reciprocity_master,
        "reciprocity_FormA_defect_match": sp.simplify(reciprocity_FormA_defect - expected_FormA_defect),
        "R_cycle_master": R_cycle_master,
        "R_cycle_FormA": R_cycle_FormA,
        "R_cycle_FormA_match": sp.simplify(R_cycle_FormA - expected_R_cycle_FormA),
    }


def symbolic_robin_cbc_and_surface_energy_check() -> dict:
    """
    Symbolically verify Theorem 3 and Theorem 4 on [a, b]:
      1) For z(x) = int_a^b (1/(2*ell))*exp(-|x-xi|/ell)*f(xi) dxi with a test polynomial/exponential f(xi),
         (1 - ell^2 d^2/dx^2) z(x) == f(x) AND (d/dx - 1/ell)z(a) == 0, (d/dx + 1/ell)z(b) == 0.
      2) Exact surface-plus-bulk identity:
         int_a^b f(x)*z(x) dx == int_a^b (z(x)^2 + ell^2 * z'(x)^2) dx + ell*(z(a)^2 + z(b)^2).
    """
    x, xi, a, b = sp.symbols("x xi a b", real=True)
    ell = sp.Symbol("ell", positive=True)
    c0, c1 = sp.symbols("c0 c1", real=True)

    # Test with arbitrary linear function f(xi) = c0 + c1 * xi on [a, b]
    f_xi = c0 + c1 * xi
    f_x = c0 + c1 * x

    z_left = sp.integrate((1 / (2 * ell)) * sp.exp(-(x - xi) / ell) * f_xi, (xi, a, x))
    z_right = sp.integrate((1 / (2 * ell)) * sp.exp((x - xi) / ell) * f_xi, (xi, x, b))
    z_x = sp.simplify(z_left + z_right)

    ode_residual = sp.simplify(z_x - ell**2 * sp.diff(z_x, x, 2) - f_x)
    cbc_a = sp.simplify((sp.diff(z_x, x) - z_x / ell).subs(x, a))
    cbc_b = sp.simplify((sp.diff(z_x, x) + z_x / ell).subs(x, b))

    # Theorem 4 surface-plus-bulk energy identity check on [0, 1] with ell = 1/2, f(x) = 1 + 2*x
    subs_num = {a: sp.Integer(0), b: sp.Integer(1), ell: sp.Rational(1, 2), c0: sp.Integer(1), c1: sp.Integer(2)}
    z_num = sp.simplify(z_x.subs(subs_num))
    f_num = f_x.subs(subs_num)
    ell_num = sp.Rational(1, 2)

    lhs_energy = sp.integrate(f_num * z_num, (x, 0, 1))
    rhs_energy = (
        sp.integrate(z_num**2 + ell_num**2 * sp.diff(z_num, x)**2, (x, 0, 1))
        + ell_num * (z_num.subs(x, 0)**2 + z_num.subs(x, 1)**2)
    )
    energy_identity_residual = sp.simplify(lhs_energy - rhs_energy)

    return {
        "ode_residual": ode_residual,
        "cbc_a_residual": cbc_a,
        "cbc_b_residual": cbc_b,
        "energy_identity_residual": energy_identity_residual,
    }


# =============================================================================
# 2. Theorem 3 Numerical Half-Space Wave BVP Verification (V1, V2, vs Form A)
# =============================================================================

def solve_halfspace_bvp_and_check_integral(
    E: float = 2.0,
    rho: float = 1.0,
    beta: float = 0.4,
    T0: float = 1.0,
    cE: float = 1.0,
    kappa: float = 0.5,
    tau0: float = 0.2,
    ell: float = 0.3,
    gamma: float = 0.25,
    omega: float = 1.7,
    sigma0: float = 1.0,
    theta0: float = 0.5,
) -> dict:
    """
    Solve the coupled thermoelastic harmonic half-space BVP on x >= 0 for:
      - Variant V1 (3 decaying modes + 1 Robin CBC),
      - Variant V2 (4 decaying modes + 2 Robin CBCs),
      - Literature Form A (gamma=0, 2 decaying modes, no Robin CBC),
    and measure the maximum discrepancy between the differential BVP solution and
    the exact Eringen integral convolution across x in [0, 2.0].
    """
    w_th = -1j * omega * (1 - 1j * omega * tau0)
    x_grid = np.linspace(0.0, 2.0, 80)

    # --- 1. Variant V1 (lambda = 0): cubic in q = s^2 (3 decaying roots) ---
    q_poly_V1 = np.polymul(
        [gamma * (ell**2) * E, (rho * (omega**2) * (ell**2) - E), -rho * (omega**2)],
        [kappa, -w_th * rho * cE],
    ) - np.array([0.0, w_th * (beta**2) * T0 * (ell**2), -w_th * (beta**2) * T0, 0.0])
    roots_q_V1 = np.roots(q_poly_V1)
    s_V1 = np.sqrt(roots_q_V1)
    s_V1 = np.where(np.real(s_V1) < 0, -s_V1, s_V1)

    theta_vec_V1 = -w_th * beta * T0 * s_V1 / (kappa * (s_V1**2) - w_th * rho * cE)
    z1_vec_V1 = -s_V1 / (1.0 - (ell**2) * (s_V1**2))
    sigma_vec_V1 = gamma * E * (-s_V1) + (1.0 - gamma) * E * z1_vec_V1 - beta * theta_vec_V1

    M_V1 = np.vstack([
        sigma_vec_V1,
        theta_vec_V1,
        (-s_V1 - 1.0 / ell) * z1_vec_V1,
    ])
    A_V1 = np.linalg.solve(M_V1, np.array([sigma0, theta0, 0.0], dtype=complex))

    sigma_diff_V1 = np.zeros_like(x_grid, dtype=complex)
    sigma_int_V1 = np.zeros_like(x_grid, dtype=complex)
    for idx, x in enumerate(x_grid):
        u_x_val = np.sum(A_V1 * (-s_V1) * np.exp(-s_V1 * x))
        th_val = np.sum(A_V1 * theta_vec_V1 * np.exp(-s_V1 * x))
        z1_val = np.sum(A_V1 * z1_vec_V1 * np.exp(-s_V1 * x))
        sigma_diff_V1[idx] = gamma * E * u_x_val + (1.0 - gamma) * E * z1_val - beta * th_val
        z1_int = np.sum(
            A_V1
            * (-s_V1)
            * (
                np.exp(-s_V1 * x) / (1.0 - (ell**2) * (s_V1**2))
                + np.exp(-x / ell) / (2.0 * ell * (s_V1 - 1.0 / ell))
            )
        )
        sigma_int_V1[idx] = gamma * E * u_x_val + (1.0 - gamma) * E * z1_int - beta * th_val

    max_err_V1 = float(np.max(np.abs(sigma_diff_V1 - sigma_int_V1)))

    # --- 2. Variant V2 (lambda = 1): quartic in q = s^2 (4 decaying roots) ---
    p1 = np.polymul([-rho * (omega**2)], np.polymul([-ell**2, 1.0], [-ell**2, 1.0]))
    p2 = np.polymul([-E, 0.0], np.polymul([-gamma * (ell**2), 1.0], [-ell**2, 1.0]))
    mech_poly = np.polyadd(p1, p2)
    term1 = np.polymul(mech_poly, [kappa, -w_th * rho * cE])
    term2 = np.polymul(
        [-w_th * (beta**2) * T0, 0.0],
        np.polymul([-gamma * (ell**2), 1.0], [-gamma * (ell**2), 1.0]),
    )
    q_poly_V2 = np.polyadd(term1, term2)
    roots_q_V2 = np.roots(q_poly_V2)
    s_V2 = np.sqrt(roots_q_V2)
    s_V2 = np.where(np.real(s_V2) < 0, -s_V2, s_V2)

    L_V2 = (1.0 - gamma * (ell**2) * (s_V2**2)) / (1.0 - (ell**2) * (s_V2**2))
    theta_vec_V2 = -w_th * beta * T0 * s_V2 * L_V2 / (kappa * (s_V2**2) - w_th * rho * cE)
    z1_vec_V2 = -s_V2 / (1.0 - (ell**2) * (s_V2**2))
    z2_vec_V2 = theta_vec_V2 / (1.0 - (ell**2) * (s_V2**2))
    sigma_vec_V2 = gamma * (E * (-s_V2) - beta * theta_vec_V2) + (1.0 - gamma) * (E * z1_vec_V2 - beta * z2_vec_V2)

    M_V2 = np.vstack([
        sigma_vec_V2,
        theta_vec_V2,
        (-s_V2 - 1.0 / ell) * z1_vec_V2,
        (-s_V2 - 1.0 / ell) * z2_vec_V2,
    ])
    A_V2 = np.linalg.solve(M_V2, np.array([sigma0, theta0, 0.0, 0.0], dtype=complex))

    sigma_diff_V2 = np.zeros_like(x_grid, dtype=complex)
    sigma_int_V2 = np.zeros_like(x_grid, dtype=complex)
    eta_diff_V2 = np.zeros_like(x_grid, dtype=complex)
    eta_int_V2 = np.zeros_like(x_grid, dtype=complex)
    for idx, x in enumerate(x_grid):
        u_x_val = np.sum(A_V2 * (-s_V2) * np.exp(-s_V2 * x))
        th_val = np.sum(A_V2 * theta_vec_V2 * np.exp(-s_V2 * x))
        z1_val = np.sum(A_V2 * z1_vec_V2 * np.exp(-s_V2 * x))
        z2_val = np.sum(A_V2 * z2_vec_V2 * np.exp(-s_V2 * x))
        sigma_diff_V2[idx] = gamma * (E * u_x_val - beta * th_val) + (1.0 - gamma) * (E * z1_val - beta * z2_val)
        eta_diff_V2[idx] = (rho * cE / T0) * th_val + beta * (gamma * u_x_val + (1.0 - gamma) * z1_val)

        z1_int = np.sum(
            A_V2
            * (-s_V2)
            * (
                np.exp(-s_V2 * x) / (1.0 - (ell**2) * (s_V2**2))
                + np.exp(-x / ell) / (2.0 * ell * (s_V2 - 1.0 / ell))
            )
        )
        z2_int = np.sum(
            A_V2
            * theta_vec_V2
            * (
                np.exp(-s_V2 * x) / (1.0 - (ell**2) * (s_V2**2))
                + np.exp(-x / ell) / (2.0 * ell * (s_V2 - 1.0 / ell))
            )
        )
        sigma_int_V2[idx] = gamma * (E * u_x_val - beta * th_val) + (1.0 - gamma) * (E * z1_int - beta * z2_int)
        eta_int_V2[idx] = (rho * cE / T0) * th_val + beta * (gamma * u_x_val + (1.0 - gamma) * z1_int)

    max_err_V2_sigma = float(np.max(np.abs(sigma_diff_V2 - sigma_int_V2)))
    max_err_V2_eta = float(np.max(np.abs(eta_diff_V2 - eta_int_V2)))

    # --- 3. Literature Form A (gamma = 0): quadratic in q = s^2 (2 decaying roots, no Robin CBC) ---
    q_poly_FA = np.polymul(
        [(rho * (omega**2) * (ell**2) - E), -rho * (omega**2)],
        [kappa, -w_th * rho * cE],
    ) - np.array([0.0, w_th * (beta**2) * T0, 0.0])
    roots_q_FA = np.roots(q_poly_FA)
    s_FA = np.sqrt(roots_q_FA)
    s_FA = np.where(np.real(s_FA) < 0, -s_FA, s_FA)

    theta_vec_FA = -w_th * beta * T0 * s_FA / (kappa * (s_FA**2) - w_th * rho * cE)
    sigma_vec_FA = (E * (-s_FA) - beta * theta_vec_FA) / (1.0 - (ell**2) * (s_FA**2))
    M_FA = np.vstack([sigma_vec_FA, theta_vec_FA])
    A_FA = np.linalg.solve(M_FA, np.array([sigma0, theta0], dtype=complex))

    sigma_diff_FA = np.zeros_like(x_grid, dtype=complex)
    sigma_int_FA = np.zeros_like(x_grid, dtype=complex)
    for idx, x in enumerate(x_grid):
        sigma_diff_FA[idx] = np.sum(A_FA * sigma_vec_FA * np.exp(-s_FA * x))
        src_modes = A_FA * (E * (-s_FA) - beta * theta_vec_FA)
        sigma_int_FA[idx] = np.sum(
            src_modes
            * (
                np.exp(-s_FA * x) / (1.0 - (ell**2) * (s_FA**2))
                + np.exp(-x / ell) / (2.0 * ell * (s_FA - 1.0 / ell))
            )
        )

    max_err_FA = float(np.max(np.abs(sigma_diff_FA - sigma_int_FA)))
    cbc_violation_FA = float(np.abs(np.sum(A_FA * (-s_FA - 1.0 / ell) * sigma_vec_FA)))

    return {
        "n_decaying_modes_V1": len(s_V1),
        "n_decaying_modes_V2": len(s_V2),
        "n_decaying_modes_FormA": len(s_FA),
        "max_err_V1": max_err_V1,
        "max_err_V2_sigma": max_err_V2_sigma,
        "max_err_V2_eta": max_err_V2_eta,
        "max_err_FormA": max_err_FA,
        "cbc_violation_FormA": cbc_violation_FA,
    }


if __name__ == "__main__":
    sym1 = symbolic_master_free_energy_and_cycle_check()
    sym2 = symbolic_robin_cbc_and_surface_energy_check()
    num3 = solve_halfspace_bvp_and_check_integral()
    print("=== Symbolic Theorem 1 & 2 Checks ===")
    for k, v in sym1.items():
        print(f"  {k}: {v}")
    print("\n=== Symbolic Theorem 3 & 4 Checks ===")
    for k, v in sym2.items():
        print(f"  {k}: {v}")
    print("\n=== Numerical Half-Space BVP Integral-Equivalence Checks ===")
    for k, v in num3.items():
        print(f"  {k}: {v}")
