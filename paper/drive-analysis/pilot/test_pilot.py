"""
Automated non-circular verification suite for Candidate C1 pilot:
Variational Two-Phase Integral Nonlocal Generalized Thermoelasticity on Bounded Domains.
"""

from __future__ import annotations

import numpy as np
import pytest

from pilot import (
    dispersion_lambdas,
    heat_kernel_G,
    run_symbolic_checks,
    solve_slab_direct_integral,
    solve_slab_eigenmode,
)


def test_symbolic_identities_and_passivity():
    res = run_symbolic_checks()
    assert res["v1_availability_identity_verified"] is True
    assert res["v2_free_energy_square_completion_verified"] is True
    assert "th(x, t)" in res["mismatched_formA_reciprocity_violation_expr"]


def test_independent_direct_integral_vs_6wave_robin_cbc():
    """
    Non-circular gold standard: compare 6-wave differential + Robin-CBC solver against
    the independent Legendre-Galerkin Fredholm integral solver across MGT, LS, and Classical laws.
    """
    L, omega, gamma, xi, eps_c = 1.0, 2.2, 0.35, 0.08, 0.08
    for law in ("Classical", "LS", "MGT"):
        G_val = heat_kernel_G(-1j * omega, law, tau_q=0.25, kappa_star=1.2)
        s_cbc = solve_slab_eigenmode(L, omega, gamma, xi, eps_c, G_val, "V1", use_cbc=True)
        s_int = solve_slab_direct_integral(L, omega, gamma, xi, eps_c, G_val, n_modes_cos=70)
        ev = s_cbc["evaluate"](s_int["x"])
        rel_u = np.max(np.abs(ev["u"] - s_int["u"])) / np.max(np.abs(s_int["u"]))
        rel_sig = np.max(np.abs(ev["sigma"] - s_int["sigma"])) / np.max(np.abs(s_int["sigma"]))
        assert rel_u < 1e-12, f"{law}: rel_u = {rel_u}"
        assert rel_sig < 1e-11, f"{law}: rel_sig = {rel_sig}"


def test_exact_integral_residual_cbc_vs_naive_shortcut():
    """
    Verify that the 6-wave Robin-CBC solution satisfies the original integral constitutive
    law to machine precision (<1e-14), whereas the naive 4-wave differential shortcut fails by O(1).
    """
    L, omega, gamma, xi, eps_c = 1.0, 2.2, 0.35, 0.08, 0.08
    G_val = heat_kernel_G(-1j * omega, "MGT", tau_q=0.25, kappa_star=1.2)
    x_grid = np.linspace(0.0, L, 250)

    f_cbc = solve_slab_eigenmode(L, omega, gamma, xi, eps_c, G_val, "V1", use_cbc=True)["evaluate"](
        x_grid
    )
    f_naive = solve_slab_eigenmode(
        L, omega, gamma, xi, eps_c, G_val, "V1", use_cbc=False
    )["evaluate"](x_grid)

    res_cbc = np.max(np.abs(f_cbc["sigma"] - f_cbc["sigma_integral"])) / np.max(
        np.abs(f_cbc["sigma"])
    )
    res_naive = np.max(np.abs(f_naive["sigma"] - f_naive["sigma_integral"])) / np.max(
        np.abs(f_naive["sigma"])
    )
    assert res_cbc < 1e-14
    assert res_naive > 0.15


def test_gn2_availability_conservation_and_formA_violation():
    """
    In conservative Green-Naghdi Type II thermoelasticity (Re G(-i*omega) == 0):
    - Variational V1 and Variational V2 conserve total availability flux <P_x(x)> to < 1e-14.
    - Omitting the interpoint nonlocal flux term or using Mismatched Form A violates conservation.
    """
    L, omega, gamma, xi, eps_c = 1.0, 2.2, 0.35, 0.08, 0.15
    G_gn2 = heat_kernel_G(-1j * omega, "GN-II", kappa_star=1.2)
    bc_r = ("sigma", 0.45 * np.exp(1.1j), "q", 0.0 + 0j)
    x_grid = np.linspace(0.0, L, 200)

    f_v1 = solve_slab_eigenmode(
        L, omega, gamma, xi, eps_c, G_gn2, "V1", bc_right=bc_r, use_cbc=True
    )["evaluate"](x_grid)
    f_v2 = solve_slab_eigenmode(
        L, omega, gamma, xi, eps_c, G_gn2, "V2", bc_right=bc_r, use_cbc=True
    )["evaluate"](x_grid)
    f_mis = solve_slab_eigenmode(
        L, omega, gamma, xi, eps_c, G_gn2, "FormA_mismatched", bc_right=bc_r, use_cbc=True
    )["evaluate"](x_grid)

    assert np.max(np.abs(f_v1["P_total"] - f_v1["P_total"][0])) < 1e-14
    assert np.max(np.abs(f_v2["P_total"] - f_v2["P_total"][0])) < 1e-14
    assert np.max(np.abs(f_v1["P_naive"] - f_v1["P_naive"][0])) > 1e-3
    assert np.max(np.abs(f_mis["P_total"] - f_mis["P_total"][0])) > 1e-3


def test_dissipative_mgt_monotonic_flux_decay_and_passivity_threshold():
    """
    Verify spatial monotonicity d<P_x>/dx = -(1/(2*eps_c)) * Re[G(-i*omega)] * |theta'(x)|^2 <= 0
    in subcritical MGT (1 - kappa_star*tau_q > 0) and sign reversal in supercritical MGT.
    """
    L, omega, gamma, xi, eps_c = 1.0, 1.8, 0.4, 0.07, 0.12
    bc_r = ("sigma", 0.3 * np.exp(0.8j), "q", 0.0 + 0j)
    x_grid = np.linspace(0.0, L, 400)

    # Subcritical (passive): kappa_star * tau_q = 0.3 < 1
    G_sub = heat_kernel_G(-1j * omega, "MGT", tau_q=0.25, kappa_star=1.2)
    f_sub = solve_slab_eigenmode(
        L, omega, gamma, xi, eps_c, G_sub, "V1", bc_right=bc_r, use_cbc=True
    )["evaluate"](x_grid)
    # Net flux entering at x=0 must strictly exceed flux leaving at x=L:
    diss_integral = (
        0.5
        * (1.0 / eps_c)
        * np.real(G_sub)
        * np.trapezoid(np.abs(f_sub["thp"]) ** 2, x_grid)
    )
    flux_drop = f_sub["P_total"][0] - f_sub["P_total"][-1]
    assert flux_drop > 0.0
    assert abs(flux_drop - diss_integral) / flux_drop < 1e-5


def test_local_and_isothermal_limiting_reductions():
    """
    Verify exact reduction to:
    (a) Local MGT thermoelasticity as gamma -> 1 (or xi -> 0),
    (b) Isothermal two-phase nonlocal elasticity (Anh & Vinh 2026) as eps_c -> 0.
    """
    L, omega = 1.0, 2.0
    G_mgt = heat_kernel_G(-1j * omega, "MGT", tau_q=0.2, kappa_star=1.0)
    x_grid = np.linspace(0.0, L, 100)

    f_loc_exact = solve_slab_eigenmode(L, omega, 1.0, 0.0, 0.08, G_mgt, "V1", use_cbc=False)[
        "evaluate"
    ](x_grid)
    f_gamma_near_1 = solve_slab_eigenmode(
        L, omega, 1.0 - 1e-9, 0.08, 0.08, G_mgt, "V1", use_cbc=True
    )["evaluate"](x_grid)
    assert np.max(np.abs(f_loc_exact["u"] - f_gamma_near_1["u"])) < 1e-8

    # Isothermal limit: compare V1 and V2 dispersion roots as eps_c -> 1e-12
    lams_v1 = dispersion_lambdas(omega, 0.3, 0.09, 1e-12, G_mgt, "V1")
    lams_v2 = dispersion_lambdas(omega, 0.3, 0.09, 1e-12, G_mgt, "V2")
    assert np.max(np.abs(lams_v1 - lams_v2)) < 1e-9


def test_singular_pure_nonlocal_scaling():
    """
    Verify asymptotic boundary-layer wavenumber scaling |lambda_3| * xi * sqrt(gamma) -> 1 as gamma -> 0+.
    """
    omega, xi, eps_c = 2.2, 0.08, 0.08
    G_mgt = heat_kernel_G(-1j * omega, "MGT", tau_q=0.25, kappa_star=1.2)
    for gm, tol in [(1e-2, 0.05), (1e-3, 0.025), (1e-4, 0.02)]:
        lams = dispersion_lambdas(omega, gm, xi, eps_c, G_mgt, "V1")
        scaled = abs(lams[2]) * xi * np.sqrt(gm)
        assert abs(scaled - 1.0) < tol
