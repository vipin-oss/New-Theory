"""
Pytest Suite for Round 2 Hardening of Candidate C1
==================================================
Tests:
  1. Task 1 (Artifact Test):
     - Partition-of-unity defect of unnormalized kernel vs exact unity of
       Borino-Failla-Parrinello (2003) / Polizzotto (2001) normalized kernel W_ell^BFP
       and reflecting Neumann Green's-function kernel K_ell^Neu on [0, inf) and [0, L].
     - Disappearance of the static 1/sqrt(gamma) surface thermal-expansion boundary layer
       under uniform temperature rise theta_0 for both normalized kernels
       (eps^V1(0)/eps^V2(0) == 1.0 to < 1e-13).
     - Survival of Theorem 1 (self-adjointness of L_{gamma,ell} on L^2(Omega) for all three
       kernels, and Maxwell/Gibbs/Helmholtz violation of Camp 1).
     - Survival of Theorem 2 (interior ODE and homogeneous Neumann CBC closure for K_ell^Neu).
  2. Task 4 (Calibration & Frequency-Regime Audit):
     - Exact physical scales for FCC Aluminum at 300 K (Lazar, Agiasofitou & Böhlke 2022
       bar{ell}_1 = 0.120272 nm and Eringen 1983 ell = 0.157931 nm).
     - Verification that inside the Fourier-defensible frequency regime (Omega <= 1,
       f <= 67.15 GHz), chi_nl = ell / ell^* ~ 0.0079 - 0.0104 and the relative damping
       difference between V1, V2, and Camp 1 is O(10^-5 to 10^-4) (< 2e-4).
"""

import numpy as np
from artifact_test import (
    verify_symbolic_artifact_and_survivors,
    run_bounded_bar_artifact_test,
    verify_neumann_ode_and_cbc_equivalence,
)
from calibration_audit import (
    ALUMINUM_300K,
    SILICON_300K,
    audit_material_scales,
    evaluate_damping_discrepancies,
)


def test_symbolic_partition_of_unity_and_static_layer_artifact():
    sym = verify_symbolic_artifact_and_survivors()
    assert sym["w_hs_unnorm_at_0"] == 0.5
    assert sym["L_hs_bfp_1"] == 1
    assert sym["L_hs_neu_1"] == 1
    assert sym["w_bar_neu"] == 1
    assert sym["ratio_unnorm_surface"] == "1/sqrt(gamma)"
    assert sym["ratio_bfp_surface"] == 1
    assert sym["ratio_neu_surface"] == 1
    assert sym["gibbs_entropy_discrepancy"] == "beta*ell**2*sigma_xx/E"


def test_bounded_bar_normalized_vs_unnormalized_kernels():
    res = run_bounded_bar_artifact_test(L=10.0, ell=1.0, gamma=0.25, N=200)

    # All three symmetric kernels are self-adjoint on L^2([0, L]) -> Theorem 1 survives
    for ktype in ("unnorm", "bfp", "neu_bar"):
        assert res[ktype]["self_adjoint_defect"] < 1e-13

    # Unnormalized kernel produces the ~1/sqrt(gamma) = 2.0 surface strain ratio artifact
    assert abs(
        res["unnorm"]["ratio_V2_over_V1_0_uniform"]
        - res["unnorm"]["exact_ratio_V2_over_V1_0_uniform"]
    ) < 1e-3
    assert abs(res["unnorm"]["ratio_V2_over_V1_0_uniform"] - 2.0) < 1e-3

    # Both normalized kernels (BFP and Neumann) satisfy L[1](x) == 1 and eliminate the static layer!
    for ktype in ("bfp", "neu_bar"):
        assert res[ktype]["unity_max_err"] < 1e-13
        assert abs(res[ktype]["ratio_V2_over_V1_0_uniform"] - 1.0) < 1e-13
        assert res[ktype]["max_diff_uniform"] < 1e-13
        # Under non-zero linear temperature gradient, a small gradient-driven O(ell/L) difference remains
        assert res[ktype]["max_diff_linear_grad"] > 1e-4


def test_neumann_kernel_ode_and_cbc_closure():
    neu = verify_neumann_ode_and_cbc_equivalence(L=5.0, ell=0.8, gamma=0.3)
    assert neu["neumann_ode_residual"] < 1e-13
    assert neu["neumann_cbc_0_err"] < 1e-13
    assert neu["neumann_cbc_L_err"] < 1e-13
    # Confirm that the unnormalized Robin functional does NOT vanish on the Neumann kernel
    assert neu["robin_functional_on_neumann_kernel"] > 0.1


def test_calibrated_aluminum_and_silicon_fourier_regime():
    # Lazar et al. (2022) 2NN MEAM calibration for Al (bar{ell}_1 = 0.120272 nm)
    sc_lazar = audit_material_scales(ALUMINUM_300K, "ell_lazar_iso_m")
    assert 0.007 < sc_lazar["chi_nl"] < 0.009
    assert sc_lazar["k_ell_sq_at_ceiling"] < 1e-4

    rows_lazar = evaluate_damping_discrepancies(
        ALUMINUM_300K, "ell_lazar_iso_m", gamma=0.5, Omega_grid=(1e-3, 1e-2, 1e-1, 0.5, 1.0)
    )
    for r in rows_lazar:
        # Inside the Fourier-defensible regime (Omega <= 1), relative damping differences are < 1e-4
        assert r["rel_diff_V1_vs_V2"] < 1e-4
        assert r["rel_diff_Camp1_vs_V1"] < 2e-4

    # Eringen (1983) zone-edge calibration for Al (ell = 0.157931 nm)
    sc_er = audit_material_scales(ALUMINUM_300K, "ell_eringen_m")
    assert 0.010 < sc_er["chi_nl"] < 0.011
    rows_er = evaluate_damping_discrepancies(
        ALUMINUM_300K, "ell_eringen_m", gamma=0.5, Omega_grid=(1e-3, 1e-2, 1e-1, 0.5, 1.0)
    )
    for r in rows_er:
        assert r["rel_diff_V1_vs_V2"] < 2e-4
        assert r["rel_diff_Camp1_vs_V1"] < 3e-4

    # Silicon at 300 K
    sc_si = audit_material_scales(SILICON_300K, "ell_eringen_m")
    assert sc_si["chi_nl"] < 0.03
    assert sc_si["k_ell_sq_at_ceiling"] < 1e-6
