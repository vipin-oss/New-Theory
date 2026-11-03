"""Pytest suite for C2 (and C3 pivot) hardening evaluation."""

from verify_c2_hardening import (
    section1_passivity_and_kernel,
    section2_lyapunov_and_multiplier_audit,
    section3_routh_hurwitz_and_counterexamples,
    section4_high_frequency_asymptotics,
    section5_material_and_parameter_grounding,
    section6_c3_imperfect_interface_verification,
)


def test_section1_passivity_and_kernel():
    res = section1_passivity_and_kernel()
    assert res["Laplace_decomposition_verified"] is True


def test_section2_lyapunov_and_multiplier_audit():
    res = section2_lyapunov_and_multiplier_audit()
    assert res["filtered_identity_exact"] is True
    assert res["unfiltered_residual_nonzero"] is True


def test_section3_routh_hurwitz_and_counterexamples():
    res = section3_routh_hurwitz_and_counterexamples()
    assert "alpha*tau_T*xi2" in res["H2_uncoupled"]


def test_section4_high_frequency_asymptotics():
    res = section4_high_frequency_asymptotics()
    assert res["CaseI_diffusive_d2"] == "alpha*tau_T/tau_q"
    assert res["CaseI_spatial_attenuation_kappa_inf"] == "c_1*tau_q*varepsilon/(2*alpha*tau_T)"
    assert res["CaseII_5th_root_limit"] == "-alpha_star/(alpha + alpha_star*tau_v)"


def test_section5_material_grounding():
    res = section5_material_and_parameter_grounding()
    assert len(res["materials"]) == 4
    assert len(res["literature_sets"]) == 6


def test_section6_c3_imperfect_interface():
    res = section6_c3_imperfect_interface_verification()
    assert res["unitarity_error"] < 1e-14
    assert res["interface_jump_error"] < 1e-14
