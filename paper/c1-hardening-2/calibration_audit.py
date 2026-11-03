"""
Round 2 — Task 4: Calibration & Frequency-Regime Audit for Candidate C1
=======================================================================
Evaluates the physical predictions of Candidate C1 (Variant V1 vs Variant V2 vs Camp 1)
for a real calibrated crystalline material — FCC Aluminum (Al) at T_0 = 300 K (primary)
and crystalline Silicon (Si) at T_0 = 300 K (comparison) — using published independent
calibrations of the nonlocal length scale ell:
  1. Lazar, Agiasofitou & Böhlke (2022), Continuum Mech. Thermodyn. 34:107-136,
     Tables 3 & 6 (2NN MEAM atomistic potential for FCC Al):
       a = 4.04950 Å = 0.404950 nm
       cubic ell_1 = 1.19303 Å = 0.119303 nm
       Voigt-averaged isotropic bar{ell}_1 = 1.20272 Å = 0.120272 nm (bar{ell}_1 / a = 0.2970)
  2. Eringen (1972, 1983) lattice-dynamics zone-boundary dispersion match:
       e_0 = 0.39 => ell = e_0 * a = 0.157931 nm (for Al)

Tests whether:
  (i)   Both parameters (ell, gamma) can be independently calibrated (Result: ell is
        calibrated at ~0.12-0.16 nm, whereas gamma in (0, 1) has NO independent experimental
        or unique long-wavelength phonon calibration because only ell_eff = sqrt(1-gamma)*ell
        enters O(k^2*ell^2) dispersion; Nobili & Pramanik 2025).
  (ii)  There exists a physically accessible frequency/wavelength regime in Al or Si where
        Fourier heat conduction holds (omega * tau_q <= 0.1 and lambda_ac >= 10 * Lambda_th)
        AND the nonlocal thermoelastic damping difference between V1, V2, and Camp 1 is
        simultaneously non-negligible (Result: NO — inside the Fourier-defensible regime,
        chi_nl = ell / ell^* ~ 0.008 - 0.010 for Al, so (k*ell)^2 <= 1e-4 and the relative
        damping differences between V1, V2, and Camp 1 are O(10^-5 to 10^-4), i.e., 0.001%-0.016%).
"""

from __future__ import annotations
import numpy as np


# ==============================================================================
# 1. Material Databases & Independent Length-Scale Calibrations
# ==============================================================================

ALUMINUM_300K = {
    "name": "FCC Aluminum (Al) at 300 K",
    "rho": 2700.0,               # kg / m^3
    "c_0": 6420.0,               # longitudinal speed of sound, m / s
    "E_1D": 2700.0 * 6420.0**2,  # rho * c_0^2 = 111.28 GPa (uniaxial P-wave modulus)
    "c_E": 900.0,                # specific heat, J / (kg K)
    "kappa": 237.0,              # thermal conductivity, W / (m K)
    "alpha_T": 23.1e-6,          # linear thermal expansion coeff, 1 / K
    "T_0": 300.0,                # reference temperature, K
    "epsilon_coupl": 0.0356,     # dimensionless thermoelastic coupling eps = beta^2 * T_0 / (rho * c_E * E_1D)
    "lattice_a_m": 4.04950e-10,  # Lazar et al. (2022) Table 3: 4.04950 Å
    "ell_lazar_cubic_m": 1.19303e-10,  # Lazar et al. (2022) Table 3: ell_1 = 1.19303 Å
    "ell_lazar_iso_m": 1.20272e-10,    # Lazar et al. (2022) Table 6: bar{ell}_1 = 1.20272 Å
    "ell_eringen_m": 0.39 * 4.04950e-10,  # Eringen (1983) e_0 * a = 1.57931 Å
    "tau_q_s": 1.5e-12,          # electron-phonon thermal relaxation time in Al at 300 K (~1.5 ps)
    "Lambda_th_m": 15.0e-9,      # thermal carrier mean free path in Al at 300 K (~15 nm)
}

SILICON_300K = {
    "name": "Crystalline Silicon (Si) at 300 K",
    "rho": 2329.0,               # kg / m^3
    "c_0": 8433.0,               # longitudinal speed of sound along <100>, m / s
    "E_1D": 2329.0 * 8433.0**2,  # 165.6 GPa
    "c_E": 712.0,                # J / (kg K)
    "kappa": 148.0,              # W / (m K)
    "alpha_T": 2.6e-6,           # 1 / K
    "T_0": 300.0,                # K
    "epsilon_coupl": 0.0011,     # dimensionless thermoelastic coupling in Si at 300 K
    "lattice_a_m": 5.431e-10,    # 5.431 Å
    "ell_eringen_m": 0.39 * 5.431e-10,  # 2.118 Å
    "tau_q_s": 20.0e-12,         # phonon relaxation time in Si at 300 K (~20-40 ps)
    "Lambda_th_m": 100.0e-9,     # dominant phonon mean free path in Si at 300 K (~100 nm)
}


# ==============================================================================
# 2. Exact Dimensionless Dispersion Root Finder for V1, V2, and Camp 1
# ==============================================================================

def quasi_elastic_wavenumber(
    Omega: float,
    eps: float,
    chi_nl: float,
    gamma: float,
    model: str,
) -> complex:
    """
    Computes the dimensionless complex wavenumber K = k * ell^* (with Im(K) > 0 for
    spatial attenuation exp(i*(K*X - Omega*tau))) of the quasi-elastic forward wave
    at dimensionless frequency Omega = omega / omega^*, thermoelastic coupling `eps`,
    nonlocal-to-thermal length ratio `chi_nl = ell / ell^*`, and two-phase parameter `gamma`.

    Dispersion equations in Q = K^2 (with L_hat(Q) = (1 + gamma * chi_nl^2 * Q) / (1 + chi_nl^2 * Q)):
      - Variant V1:
          (Q * L_hat(Q) - Omega^2) * (Q - i * Omega) - i * eps * Omega * Q * (L_hat(Q))^2 = 0
          (Quartic in Q when gamma in (0, 1) and chi_nl > 0)
      - Variant V2:
          (Q * L_hat(Q) - Omega^2) * (Q - i * Omega) - i * eps * Omega * Q = 0
          (Cubic in Q)
      - Camp 1 (gamma = 0 unregularized Form A stress + local entropy):
          (Q / (1 + chi_nl^2 * Q) - Omega^2) * (Q - i * Omega) - i * eps * Omega * Q / (1 + chi_nl^2 * Q) = 0
          (Cubic in Q: (Q - Omega^2*(1 + chi_nl^2*Q))*(Q - i*Omega) - i*eps*Omega*Q = 0)
    """
    c2 = chi_nl**2
    iOm = 1j * Omega
    Om2 = Omega**2

    if model == "V1":
        # Clear denominator (1 + c2*Q)^2:
        # (Q*(1 + gamma*c2*Q) - Om2*(1 + c2*Q)) * (Q - iOm) * (1 + c2*Q)
        #   - i*eps*Omega * Q * (1 + gamma*c2*Q)^2 = 0
        # Polynomial in Q of degree 4:
        p1 = np.poly1d([gamma * c2, 1.0 - Om2 * c2, -Om2])
        p2 = np.poly1d([1.0, -iOm])
        p3 = np.poly1d([c2, 1.0])
        p_coupl = iOm * eps * np.poly1d([gamma**2 * c2**2, 2.0 * gamma * c2, 1.0, 0.0])
        poly = np.polymul(np.polymul(p1, p2), p3) - p_coupl
    elif model == "V2":
        # Clear denominator (1 + c2*Q):
        # (Q*(1 + gamma*c2*Q) - Om2*(1 + c2*Q)) * (Q - iOm) - i*eps*Omega * Q * (1 + c2*Q) = 0
        p1 = np.poly1d([gamma * c2, 1.0 - Om2 * c2, -Om2])
        p2 = np.poly1d([1.0, -iOm])
        p_coupl = iOm * eps * np.poly1d([c2, 1.0, 0.0])
        poly = np.polymul(p1, p2) - p_coupl
    elif model == "Camp1":
        # Clear denominator (1 + c2*Q):
        # (Q - Om2*(1 + c2*Q)) * (Q - iOm) - i*eps*Omega * Q = 0
        p1 = np.poly1d([1.0 - Om2 * c2, -Om2])
        p2 = np.poly1d([1.0, -iOm])
        p_coupl = iOm * eps * np.poly1d([1.0, 0.0])
        poly = np.polymul(p1, p2) - p_coupl
    elif model == "Local":
        p1 = np.poly1d([1.0, -Om2])
        p2 = np.poly1d([1.0, -iOm])
        p_coupl = iOm * eps * np.poly1d([1.0, 0.0])
        poly = np.polymul(p1, p2) - p_coupl
    else:
        raise ValueError(f"Unknown model: {model}")

    roots_Q = np.roots(poly.coeffs)
    # Convert to forward-going roots K = sqrt(Q) with Re(K) > 0
    roots_K = []
    for Q in roots_Q:
        K = np.sqrt(Q)
        if K.real < 0 or (abs(K.real) < 1e-14 and K.imag < 0):
            K = -K
        roots_K.append(K)
    roots_K = np.array(roots_K)

    # Identify the quasi-elastic branch: closest to the adiabatic elastic wavenumber K_el ~ Omega / sqrt(1 + eps)
    K_target = Omega / np.sqrt(1.0 + eps)
    idx = int(np.argmin(np.abs(roots_K - K_target)))
    return complex(roots_K[idx])


def audit_material_scales(mat: dict, ell_key: str) -> dict:
    """
    Computes characteristic thermal frequency omega^*, length ell^*, nonlocal-to-thermal
    ratio chi_nl = ell / ell^*, and Fourier-validity ceiling for a given material.
    """
    rho = mat["rho"]
    c_0 = mat["c_0"]
    c_E = mat["c_E"]
    kappa = mat["kappa"]
    ell = mat[ell_key]
    tau_q = mat["tau_q_s"]
    Lambda_th = mat["Lambda_th_m"]

    omega_star = rho * c_E * c_0**2 / kappa
    f_star = omega_star / (2.0 * np.pi)
    ell_star = c_0 / omega_star
    chi_nl = ell / ell_star

    # Fourier validity ceilings:
    # 1. Temporal (Cattaneo): omega * tau_q <= 0.1 => omega_max_temp = 0.1 / tau_q
    omega_max_temp = 0.1 / tau_q
    Omega_max_temp = omega_max_temp / omega_star

    # 2. Spatial (ballistic phonon/electron MFP): k * Lambda_th <= 2*pi / 10 => omega_max_spat = (2*pi/10) * c_0 / Lambda_th
    omega_max_spat = (0.2 * np.pi) * c_0 / Lambda_th
    Omega_max_spat = omega_max_spat / omega_star

    Omega_fourier_ceiling = min(Omega_max_temp, Omega_max_spat)
    k_ell_at_ceiling = Omega_fourier_ceiling * chi_nl

    return {
        "omega_star_rad_s": omega_star,
        "f_star_Hz": f_star,
        "ell_star_m": ell_star,
        "ell_m": ell,
        "chi_nl": chi_nl,
        "chi_nl_sq": chi_nl**2,
        "Omega_max_temp": Omega_max_temp,
        "Omega_max_spat": Omega_max_spat,
        "Omega_fourier_ceiling": Omega_fourier_ceiling,
        "f_fourier_ceiling_Hz": Omega_fourier_ceiling * f_star,
        "k_ell_at_ceiling": k_ell_at_ceiling,
        "k_ell_sq_at_ceiling": k_ell_at_ceiling**2,
    }


def evaluate_damping_discrepancies(
    mat: dict,
    ell_key: str,
    gamma: float = 0.5,
    Omega_grid: tuple[float, ...] = (1e-3, 1e-2, 1e-1, 0.5, 1.0, 10.0, 100.0),
) -> list[dict]:
    """
    Evaluates the quasi-elastic attenuation Im(K) for V1, V2, Camp 1, and Local
    across dimensionless frequencies Omega = omega / omega^*.
    """
    scales = audit_material_scales(mat, ell_key)
    chi_nl = scales["chi_nl"]
    eps = mat["epsilon_coupl"]
    f_star = scales["f_star_Hz"]
    ell_star = scales["ell_star_m"]

    rows = []
    for Om in Omega_grid:
        K_V1 = quasi_elastic_wavenumber(Om, eps, chi_nl, gamma, "V1")
        K_V2 = quasi_elastic_wavenumber(Om, eps, chi_nl, gamma, "V2")
        K_C1 = quasi_elastic_wavenumber(Om, eps, chi_nl, 0.0, "Camp1")
        K_Loc = quasi_elastic_wavenumber(Om, eps, 0.0, 1.0, "Local")

        a_V1 = K_V1.imag
        a_V2 = K_V2.imag
        a_C1 = K_C1.imag
        a_Loc = K_Loc.imag

        rel_V1_V2 = abs(a_V1 - a_V2) / abs(a_V1)
        rel_C1_V1 = abs(a_C1 - a_V1) / abs(a_V1)
        rel_V1_Loc = abs(a_V1 - a_Loc) / abs(a_Loc)

        rows.append(
            {
                "Omega": Om,
                "freq_GHz": (Om * f_star) * 1e-9,
                "wavelength_nm": (2.0 * np.pi * ell_star / K_V1.real) * 1e9,
                "k_ell": K_V1.real * chi_nl,
                "alpha_V1_dimless": a_V1,
                "alpha_V2_dimless": a_V2,
                "alpha_Camp1_dimless": a_C1,
                "rel_diff_V1_vs_V2": rel_V1_V2,
                "rel_diff_Camp1_vs_V1": rel_C1_V1,
                "rel_diff_V1_vs_Local": rel_V1_Loc,
                "in_fourier_regime": Om <= max(1.0, scales["Omega_fourier_ceiling"]),
            }
        )
    return rows


def main() -> None:
    print("======================================================================")
    print("ROUND 2 — TASK 4: CALIBRATION & FREQUENCY-REGIME AUDIT")
    print("======================================================================")

    for label, ell_key in [
        ("Al (Lazar et al. 2022 2NN MEAM Voigt bar{ell}_1 = 0.1203 nm)", "ell_lazar_iso_m"),
        ("Al (Eringen 1983 zone-edge e_0*a = 0.1579 nm)", "ell_eringen_m"),
    ]:
        print(f"\n--- {label} ---")
        sc = audit_material_scales(ALUMINUM_300K, ell_key)
        for k, v in sc.items():
            print(f"  {k:26s}: {v:.6e}")

        rows = evaluate_damping_discrepancies(ALUMINUM_300K, ell_key, gamma=0.5)
        print("\n  Omega    f (GHz)   lambda (nm)   k*ell       |a_V1-a_V2|/a_V1   |a_C1-a_V1|/a_V1")
        for r in rows:
            print(
                f"  {r['Omega']:7.3f}  {r['freq_GHz']:8.3f}  {r['wavelength_nm']:11.3f}  "
                f"{r['k_ell']:10.3e}  {r['rel_diff_V1_vs_V2']:17.4e}  {r['rel_diff_Camp1_vs_V1']:17.4e}"
            )

    print("\n--- Si (Eringen 1983 zone-edge e_0*a = 0.2118 nm) ---")
    sc_si = audit_material_scales(SILICON_300K, "ell_eringen_m")
    for k, v in sc_si.items():
        print(f"  {k:26s}: {v:.6e}")


if __name__ == "__main__":
    main()
