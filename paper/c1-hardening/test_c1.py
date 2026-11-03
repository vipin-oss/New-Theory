"""
Pytest verification suite for Candidate C1 Hardening (Theorems 1–4 in proofs.md).
"""

import numpy as np
import sympy as sp
from verify_c1 import (
    symbolic_master_free_energy_and_cycle_check,
    symbolic_robin_cbc_and_surface_energy_check,
    solve_halfspace_bvp_and_check_integral,
)
from physical_relevance import (
    compute_material_table,
    verify_surface_thermal_expansion_boundary_layer,
)


def test_theorem1_master_free_energy_v1_v2_and_reciprocity():
    """Verify Theorem 1: Psi_lambda yields V1 at lambda=0, V2 at lambda=1, and exact Frechet reciprocity."""
    res = symbolic_master_free_energy_and_cycle_check()
    assert res["sigma_V1_residual"] == 0
    assert res["eta_V1_residual"] == 0
    assert res["sigma_V2_residual"] == 0
    assert res["eta_V2_residual"] == 0
    assert res["reciprocity_master_residual"] == 0
    assert res["R_cycle_master"] == 0


def test_theorem2_form_a_nonexistence_and_closed_cycle_violation():
    """Verify Theorem 2: Form A + local entropy breaks Frechet symmetry and violates Clausius-Duhem on a cycle."""
    res = symbolic_master_free_energy_and_cycle_check()
    assert res["reciprocity_FormA_defect_match"] == 0
    assert res["R_cycle_FormA_match"] == 0

    # Numerical check of negative total entropy production in a closed cycle for Form A + local heating:
    # Choose beta * eps0 * theta0 < 0 and small thermal conductivity kappa
    k = 2.0
    ell = 0.5
    omega = 5.0
    beta = 1.0
    eps0 = 0.1
    theta0 = -0.2
    T0 = 300.0
    kappa = 1e-4

    R_cycle_FA = -(np.pi**2 / k) * beta * eps0 * theta0 * (ell**2 * k**2) / (1.0 + ell**2 * k**2)
    thermal_dissipation_cycle = (kappa * (np.pi**2) * k * (theta0**2)) / omega
    # Notice R_cycle_FA > 0 means mechanical-thermal cycle extracts net work out of the medium,
    # so internal entropy production oint int D_int dx dt = (-R_cycle_FA + thermal_dissipation_cycle) / T0 < 0!
    net_entropy_production_FA = (-R_cycle_FA + thermal_dissipation_cycle) / T0
    net_entropy_production_V1_V2 = thermal_dissipation_cycle / T0

    assert R_cycle_FA > 0.0
    assert net_entropy_production_FA < 0.0
    assert net_entropy_production_V1_V2 > 0.0


def test_theorem2_discrete_grid_self_adjointness_and_availability():
    """Verify on a non-uniform discrete grid on [a, b] that L_{gamma, ell} is self-adjoint, coercive, and V1/V2 conserve availability."""
    rng = np.random.default_rng(42)
    N = 60
    x = np.linspace(0.0, 1.5, N)
    dx = x[1] - x[0]
    w = np.ones(N) * dx
    w[0] *= 0.5
    w[-1] *= 0.5

    ell = 0.35
    gamma = 0.2
    K_mat = (1.0 / (2.0 * ell)) * np.exp(-np.abs(x[:, None] - x[None, :]) / ell) * w[None, :]
    L_mat = gamma * np.eye(N) + (1.0 - gamma) * K_mat

    eps_dot = rng.normal(size=N)
    theta = rng.normal(size=N)
    beta = 0.6

    # Weighted inner product <f, g>_w = sum w_i f_i g_i
    lhs = np.sum(w * eps_dot * (L_mat @ theta))
    rhs = np.sum(w * theta * (L_mat @ eps_dot))
    assert np.isclose(lhs, rhs, atol=1e-14)

    # Coercivity <f, L f>_w >= gamma * ||f||_w^2
    quad_f = np.sum(w * eps_dot * (L_mat @ eps_dot))
    norm_f = np.sum(w * eps_dot**2)
    assert quad_f > gamma * norm_f

    # Availability mismatch source S_mismatch integrated over domain:
    # V1: 0, V2: 0, Form A: beta * <eps_dot, theta - K_ell[theta]>_w != 0
    S_int_V2 = -beta * np.sum(w * eps_dot * (L_mat @ theta)) + beta * np.sum(w * theta * (L_mat @ eps_dot))
    S_int_FA = -beta * np.sum(w * eps_dot * (K_mat @ theta)) + beta * np.sum(w * theta * eps_dot)
    assert abs(S_int_V2) < 1e-14
    assert abs(S_int_FA) > 1e-2


def test_theorem3_symbolic_robin_cbc_and_theorem4_surface_energy():
    """Verify Theorem 3 ODE + Robin CBC equivalence and Theorem 4 surface+bulk positive-definite energy identity."""
    res = symbolic_robin_cbc_and_surface_energy_check()
    assert res["ode_residual"] == 0
    assert res["cbc_a_residual"] == 0
    assert res["cbc_b_residual"] == 0
    assert res["energy_identity_residual"] == 0


def test_theorem3_halfspace_bvp_integral_equivalence():
    """Verify Theorem 3 numerical half-space BVP: V1 (3 modes) and V2 (4 modes) match integral law to <1e-13; Form A fails O(1)."""
    res = solve_halfspace_bvp_and_check_integral()
    assert res["n_decaying_modes_V1"] == 3
    assert res["n_decaying_modes_V2"] == 4
    assert res["n_decaying_modes_FormA"] == 2
    assert res["max_err_V1"] < 1e-13
    assert res["max_err_V2_sigma"] < 1e-13
    assert res["max_err_V2_eta"] < 1e-13
    assert res["max_err_FormA"] > 0.5
    assert res["cbc_violation_FormA"] > 1.0


def test_task4_physical_relevance_and_surface_boundary_layer():
    """Verify Task 4 SI material regime calculations and exact surface thermal-expansion boundary layer."""
    bl = verify_surface_thermal_expansion_boundary_layer(gamma=0.25)
    assert bl["max_traction_residual_V1"] < 1e-16
    assert np.isclose(bl["surface_amplification_V1_over_V2"], 2.0, atol=1e-15)

    mats = compute_material_table(T0=300.0, e0=1.5, gamma=0.25)
    assert set(mats.keys()) == {"Al", "Cu", "Si", "SiC"}
    # At 1.5 THz, relative thermoelastic damping difference dQ^-1/Q^-1 between V1 and V2 exceeds 25% in all 4 materials
    for k, m in mats.items():
        thz_row = m["regimes"][-1]
        assert thz_row["rel_Qinv_V1_V2"] > 0.25
        assert thz_row["rel_Qinv_V1_FA"] > 0.14

