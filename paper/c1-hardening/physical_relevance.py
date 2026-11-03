"""
Task 4: Physical Relevance Check with Real SI Material Parameters (Al, Cu, Si, 6H-SiC)
across MHz, GHz, and THz / Sub-10 nm Regimes.

Sources for SI material constants at T0 = 300 K:
  - CRC Handbook of Chemistry and Physics (104th ed.)
  - Kittel, Introduction to Solid State Physics (8th ed.)
  - Chen (2021), Non-Fourier Phonon Heat Conduction, Nat. Rev. Phys. 3, 555
"""

from __future__ import annotations
import numpy as np


MATERIALS_SI = {
    "Al": {
        "name": "Aluminum (FCC metal)",
        "rho": 2700.0,          # kg/m^3
        "M": 111.3e9,           # Pa (lambda + 2*mu)
        "K_B": 76.0e9,          # Pa (bulk modulus)
        "c_E": 900.0,           # J/(kg*K)
        "alpha_T": 23.1e-6,     # 1/K (linear thermal expansion)
        "kappa": 237.0,         # W/(m*K)
        "a0": 0.405e-9,         # m (lattice parameter)
        "tau0": 1.0e-12,        # s (thermal relaxation time)
    },
    "Cu": {
        "name": "Copper (FCC metal)",
        "rho": 8960.0,
        "M": 197.0e9,
        "K_B": 140.0e9,
        "c_E": 385.0,
        "alpha_T": 16.5e-6,
        "kappa": 401.0,
        "a0": 0.361e-9,
        "tau0": 1.5e-12,
    },
    "Si": {
        "name": "Silicon (diamond cubic)",
        "rho": 2329.0,
        "M": 165.7e9,
        "K_B": 97.8e9,
        "c_E": 712.0,
        "alpha_T": 2.6e-6,
        "kappa": 148.0,
        "a0": 0.543e-9,
        "tau0": 10.0e-12,
    },
    "SiC": {
        "name": "Silicon Carbide (6H-SiC)",
        "rho": 3210.0,
        "M": 501.0e9,
        "K_B": 220.0e9,
        "c_E": 690.0,
        "alpha_T": 4.0e-6,
        "kappa": 360.0,
        "a0": 0.436e-9,
        "tau0": 8.0e-12,
    },
}


def compute_material_table(T0: float = 300.0, e0: float = 1.5, gamma: float = 0.25) -> dict:
    """
    Compute derived thermoelastic parameters and regime comparisons across
    f = 100 MHz, 10 GHz, 0.5 THz, and 1.5 THz (plus sub-10 nm NEMS mode k = pi / L with L = 5 nm).
    """
    results = {}
    freqs_hz = [1.0e8, 1.0e10, 5.0e11, 1.5e12]

    for key, mat in MATERIALS_SI.items():
        rho = mat["rho"]
        M = mat["M"]
        K_B = mat["K_B"]
        c_E = mat["c_E"]
        alpha_T = mat["alpha_T"]
        kappa = mat["kappa"]
        a0 = mat["a0"]
        tau0 = mat["tau0"]

        c_L = np.sqrt(M / rho)
        beta = 3.0 * K_B * alpha_T
        eps_T = (beta**2 * T0) / (rho * c_E * M)
        ell = e0 * a0  # nonlocal length scale

        regime_rows = []
        for f in freqs_hz:
            omega = 2.0 * np.pi * f
            k0 = omega / c_L
            ell_k = ell * k0
            K_hat = 1.0 / (1.0 + ell_k**2)
            L_hat = gamma + (1.0 - gamma) * K_hat

            # Exact dispersion roots for acoustic branch k(omega) in V1, V2, and Form A:
            # Using perturbation / exact complex root of acoustic branch:
            w_th = -1j * omega * (1.0 - 1j * omega * tau0)
            D_th = kappa / (rho * c_E)

            # Effective complex modulus M_eff(k0) for acoustic branch:
            # V1: M * L_hat + eps_T * M * (-w_th) / (D_th * k0^2 - w_th)
            # V2: M * L_hat + eps_T * M * L_hat^2 * (-w_th) / (D_th * k0^2 - w_th)
            # Form A: M * K_hat + eps_T * M * K_hat * (-w_th) / (D_th * k0^2 - w_th)
            th_factor = (-w_th) / (D_th * (k0**2) - w_th)
            M_eff_V1 = M * (L_hat + eps_T * th_factor)
            M_eff_V2 = M * (L_hat + eps_T * (L_hat**2) * th_factor)
            M_eff_FA = M * (K_hat + eps_T * K_hat * th_factor)

            v_V1 = np.real(np.sqrt(M_eff_V1 / rho))
            v_V2 = np.real(np.sqrt(M_eff_V2 / rho))
            v_FA = np.real(np.sqrt(M_eff_FA / rho))

            # Thermoelastic loss factor (inverse quality factor Q^-1 = Im(M_eff)/Re(M_eff))
            Qinv_V1 = float(np.imag(M_eff_V1) / np.real(M_eff_V1))
            Qinv_V2 = float(np.imag(M_eff_V2) / np.real(M_eff_V2))
            Qinv_FA = float(np.imag(M_eff_FA) / np.real(M_eff_FA))

            rel_v_V1_V2 = abs(v_V1 - v_V2) / v_V1
            rel_v_V1_FA = abs(v_V1 - v_FA) / v_V1
            rel_Q_V1_V2 = abs(Qinv_V1 - Qinv_V2) / max(abs(Qinv_V1), 1e-30)
            rel_Q_V1_FA = abs(Qinv_V1 - Qinv_FA) / max(abs(Qinv_V1), 1e-30)

            regime_rows.append({
                "f_Hz": f,
                "wavelength_nm": (2.0 * np.pi / k0) * 1e9,
                "ell_k": ell_k,
                "rel_v_V1_V2": rel_v_V1_V2,
                "rel_v_V1_FA": rel_v_V1_FA,
                "rel_Qinv_V1_V2": rel_Q_V1_V2,
                "rel_Qinv_V1_FA": rel_Q_V1_FA,
            })

        # Sub-5 nm NEMS resonator fundamental / 3rd harmonic mode (effective k = 2.0 nm^-1, ell = 1.0 nm):
        k_nems = 1.0 / ell  # ell * k = 1.0
        K_hat_nems = 0.5
        L_hat_nems = gamma + (1.0 - gamma) * 0.5
        rel_Qinv_nems_V1_V2 = 1.0 - (L_hat_nems**2) / L_hat_nems  # Q^-1 = Im/Re scales as L_hat for V2 vs 1/L_hat for V1
        # Wait: let us compute exact Q^-1 ratio at ell*k = 1.0:
        # In V1: Im(M_eff)/Re(M_eff) = eps_T * Im(th_factor) / L_hat
        # In V2: Im(M_eff)/Re(M_eff) = eps_T * L_hat * Im(th_factor)
        # In Form A: Im(M_eff)/Re(M_eff) = eps_T * Im(th_factor)
        Qinv_ratio_V2_over_V1_at_ek1 = L_hat_nems**2
        Qinv_rel_diff_V1_V2_at_ek1 = 1.0 - L_hat_nems**2

        results[key] = {
            "name": mat["name"],
            "c_L_m_s": float(c_L),
            "beta_MPa_K": float(beta * 1e-6),
            "eps_T": float(eps_T),
            "ell_nm": float(ell * 1e9),
            "surface_strain_ratio_V1_over_V2": float(1.0 / np.sqrt(gamma)),
            "Qinv_rel_diff_V1_V2_at_ek1": float(Qinv_rel_diff_V1_V2_at_ek1),
            "regimes": regime_rows,
        }

    return results


def verify_surface_thermal_expansion_boundary_layer(
    beta_theta0_over_E: float = 1.0e-3,
    ell: float = 0.5,
    gamma: float = 0.25,
) -> dict:
    """
    Verify the exact closed-form surface strain boundary-layer theorem for a traction-free
    half-space (sigma(x) = 0) under uniform temperature rise theta0:
      - Variant V2: eps^V2(x) = (beta*theta0/E) identically -> eps^V2(0) = beta*theta0/E.
      - Variant V1: eps^V1(x) = (beta*theta0/E) * [1 + ((1 - sqrt(gamma))/sqrt(gamma)) * exp(-x/(sqrt(gamma)*ell))]
                    -> eps^V1(0) = (1/sqrt(gamma)) * (beta*theta0/E).
    Checks that plugging eps^V1(x) into the exact Eringen two-phase integral operator
    L_{gamma, ell}[E * eps^V1](x) reproduces beta*theta0 to machine precision across x >= 0.
    """
    x_grid = np.linspace(0.0, 5.0 * ell, 60)
    C_amp = (1.0 - np.sqrt(gamma)) / np.sqrt(gamma)
    s_bl = 1.0 / (np.sqrt(gamma) * ell)

    eps_V1 = beta_theta0_over_E * (1.0 + C_amp * np.exp(-s_bl * x_grid))
    eps_V2 = beta_theta0_over_E * np.ones_like(x_grid)

    # Exact integral evaluation of K_ell[eps_V1](x) on [0, inf):
    # int_0^inf (1/(2*ell)) exp(-|x-xi|/ell) dxi = 1 - 0.5*exp(-x/ell)
    # int_0^inf (1/(2*ell)) exp(-|x-xi|/ell) exp(-s_bl*xi) dxi
    #   = exp(-s_bl*x)/(1 - ell^2*s_bl^2) - exp(-x/ell)/(2*ell*(s_bl - 1/ell))
    K_const = 1.0 - 0.5 * np.exp(-x_grid / ell)
    K_exp = np.exp(-s_bl * x_grid) / (1.0 - (ell * s_bl) ** 2) + np.exp(-x_grid / ell) / (
        2.0 * ell * (s_bl - 1.0 / ell)
    )
    K_eps_V1 = beta_theta0_over_E * (K_const + C_amp * K_exp)
    L_eps_V1 = gamma * eps_V1 + (1.0 - gamma) * K_eps_V1

    max_traction_residual_V1 = float(np.max(np.abs(L_eps_V1 - beta_theta0_over_E)))
    surface_amplification = float(eps_V1[0] / eps_V2[0])

    return {
        "max_traction_residual_V1": max_traction_residual_V1,
        "surface_amplification_V1_over_V2": surface_amplification,
        "expected_amplification": float(1.0 / np.sqrt(gamma)),
    }


if __name__ == "__main__":
    res = compute_material_table()
    bl = verify_surface_thermal_expansion_boundary_layer()
    print("=== Material Parameters & Regime Table (T0 = 300 K, e0 = 1.5, gamma = 0.25) ===")
    for k, v in res.items():
        print(f"\n[{k}] {v['name']}: c_L={v['c_L_m_s']:.1f} m/s, beta={v['beta_MPa_K']:.3f} MPa/K, eps_T={v['eps_T']:.5f}, ell={v['ell_nm']:.3f} nm")
        for r in v["regimes"]:
            print(
                f"  f={r['f_Hz']:.1e} Hz (lambda={r['wavelength_nm']:.2f} nm, ell*k={r['ell_k']:.3e}): "
                f"dv/v(V1-V2)={r['rel_v_V1_V2']:.3e}, dv/v(V1-FA)={r['rel_v_V1_FA']:.3e}, "
                f"dQ^-1/Q^-1(V1-V2)={r['rel_Qinv_V1_V2']:.3e}, dQ^-1/Q^-1(V1-FA)={r['rel_Qinv_V1_FA']:.3e}"
            )
    print("\n=== Surface Thermal-Expansion Boundary Layer Check ===")
    print(bl)
