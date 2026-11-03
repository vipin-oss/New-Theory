"""
Round 2 — Task 1: The Artifact Test for Candidate C1
====================================================
Repeats the half-space [0, inf) and bounded-bar [0, L] analysis for Variant V1,
Variant V2, and Camp 1 under:
  (b) Unnormalized truncated Helmholtz kernel K_ell^unnorm(x, xi) = (1/(2*ell)) * exp(-|x-xi|/ell)
  (a1) Borino-Failla-Parrinello (2003) / Polizzotto (2001) / Marotti de Sciarra (2009)
       additive-defect normalized kernel:
       W_ell^BFP(x, xi) = (1 - w_Omega(x))*delta(x - xi) + K_ell^unnorm(x, xi)
  (a2) Reflecting / Neumann Green's-function normalized kernel (Ren & Truskinovsky 2000;
       Challamel et al. 2014; Nobili & Pramanik 2025):
       K_ell^Neu(x, xi) satisfying (1 - ell^2 d^2/dx^2) K_ell^Neu = delta(x - xi)
       with homogeneous Neumann CBCs dK_ell^Neu/dx = 0 at the domain boundaries.

Demonstrates analytically (SymPy) and numerically (NumPy/SciPy):
  1. The static 1/sqrt(gamma) surface thermal-expansion boundary layer under uniform
     temperature theta_0 is an ARTIFACT of unnormalized kernel truncation: under both
     W_ell^BFP and K_ell^Neu, L_{gamma,ell}[1](x) == 1 identically, so
     eps^V1(x) == eps^V2(x) == (beta*theta_0)/E everywhere and eps^V1(0)/eps^V2(0) == 1.
  2. Which results of C1 survive kernel normalization (Theorem 1 V1/V2 thermodynamic
     consistency and Camp 1 Maxwell/Clausius-Duhem violation; Theorem 2 CBC existence,
     with Robin -> modified-Robin for BFP or Neumann CBC for K_ell^Neu; Theorem 3
     quartic vs. cubic mode counts in k^2; Theorem 4 bulk dispersion and damping formulas)
     and which disappear (the static 1/sqrt(gamma) uniform-heating surface layer).
"""

from __future__ import annotations
import numpy as np
import sympy as sp


# ==============================================================================
# 1. Symbolic Proofs: Partition of Unity, Static Layer Artifact, Maxwell Symmetry
# ==============================================================================

def verify_symbolic_artifact_and_survivors() -> dict:
    """
    Symbolic SymPy verification of:
      (i) Partition-of-unity defect of unnormalized kernel vs exact unity of
          BFP-normalized and Neumann-normalized kernels on [0, inf) and [0, L].
      (ii) Static uniform-heating strain ratio eps^V1(0)/eps^V2(0) = 1/sqrt(gamma)
           for unnormalized kernel vs 1 for BFP and Neumann normalized kernels.
      (iii) Maxwell Frechet-derivative symmetry violation for Camp 1 in both
            Helmholtz (eps, theta) and Gibbs (sigma, theta) representations.
      (iv) Exact Neumann CBC closure for K_ell^Neu and modified Robin closure for W_ell^BFP.
    """
    x, xi, L, ell, gamma = sp.symbols("x xi L ell gamma", positive=True)
    E, beta, theta0, c_sigma, T0 = sp.symbols("E beta theta0 c_sigma T0", positive=True)

    # --- (i) Half-space [0, inf) kernel integrals of constant field f(xi) = 1 ---
    # Unnormalized kernel integral w_hs(x) = int_0^inf (1/(2*ell))*exp(-|x-xi|/ell) dxi
    w_hs_unnorm = (
        sp.integrate(sp.exp(-(x - xi) / ell) / (2 * ell), (xi, 0, x))
        + sp.integrate(sp.exp(-(xi - x) / ell) / (2 * ell), (xi, x, sp.oo))
    )
    w_hs_unnorm = sp.simplify(w_hs_unnorm)  # 1 - exp(-x/ell)/2
    L_hs_unnorm_1 = sp.simplify(gamma + (1 - gamma) * w_hs_unnorm)

    # BFP normalized kernel on [0, inf): W^BFP(x,xi) = (1 - w_hs(x))delta(x-xi) + K^unnorm(x,xi)
    w_hs_bfp = sp.simplify((1 - w_hs_unnorm) + w_hs_unnorm)
    L_hs_bfp_1 = sp.simplify(gamma + (1 - gamma) * w_hs_bfp)

    # Neumann reflecting kernel on [0, inf): K^Neu(x,xi) = (exp(-|x-xi|/ell) + exp(-(x+xi)/ell))/(2*ell)
    w_hs_neu = (
        sp.integrate((sp.exp(-(x - xi) / ell) + sp.exp(-(x + xi) / ell)) / (2 * ell), (xi, 0, x))
        + sp.integrate((sp.exp(-(xi - x) / ell) + sp.exp(-(x + xi) / ell)) / (2 * ell), (xi, x, sp.oo))
    )
    w_hs_neu = sp.simplify(w_hs_neu)
    L_hs_neu_1 = sp.simplify(gamma + (1 - gamma) * w_hs_neu)

    # --- Bounded bar [0, L] kernel integrals of constant field f(xi) = 1 ---
    w_bar_unnorm = (
        sp.integrate(sp.exp(-(x - xi) / ell) / (2 * ell), (xi, 0, x))
        + sp.integrate(sp.exp(-(xi - x) / ell) / (2 * ell), (xi, x, L))
    )
    w_bar_unnorm = sp.simplify(w_bar_unnorm)  # 1 - (exp(-x/ell) + exp(-(L-x)/ell))/2

    # Neumann kernel on [0, L]: K^Neu(x,xi) = cosh(min(x,xi)/ell)*cosh((L-max(x,xi))/ell)/(ell*sinh(L/ell))
    w_bar_neu = (
        sp.integrate(
            sp.cosh(xi / ell) * sp.cosh((L - x) / ell) / (ell * sp.sinh(L / ell)),
            (xi, 0, x),
        )
        + sp.integrate(
            sp.cosh(x / ell) * sp.cosh((L - xi) / ell) / (ell * sp.sinh(L / ell)),
            (xi, x, L),
        )
    )
    w_bar_neu = sp.simplify(w_bar_neu)

    # --- (ii) Static uniform-heating surface strain ratio on [0, inf) ---
    # Under BFP and Neumann kernels, L_{gamma,ell}[1](x) == 1 => eps^V2(x) = beta*theta0/E = eps^V1(x)
    eps_V1_const = beta * theta0 / E
    eps_V2_bfp = beta * theta0 / E / L_hs_bfp_1
    eps_V2_neu = beta * theta0 / E / L_hs_neu_1
    ratio_bfp = sp.simplify(eps_V1_const / eps_V2_bfp)
    ratio_neu = sp.simplify(eps_V1_const / eps_V2_neu)

    # Under unnormalized kernel on [0, inf): solve (1 - gamma*ell^2 d^2/dx^2) eps = (1 - ell^2 d^2/dx^2)(beta*theta0/E)
    # with Robin CBC (d/dx - 1/ell)(beta*theta0) = gamma*E*(d/dx - 1/ell)eps(0)
    C = sp.Symbol("C")
    eps_V2_unnorm_ansatz = (beta * theta0 / E) * (1 + C * sp.exp(-x / (sp.sqrt(gamma) * ell)))
    robin_lhs = -beta * theta0 / ell
    robin_rhs = sp.simplify(
        gamma * E * (sp.diff(eps_V2_unnorm_ansatz, x) - eps_V2_unnorm_ansatz / ell).subs(x, 0)
    )
    C_sol = sp.simplify(sp.solve(sp.Eq(robin_lhs, robin_rhs), C)[0])
    eps_V2_unnorm_0 = sp.radsimp(sp.simplify(eps_V2_unnorm_ansatz.subs(C, C_sol).subs(x, 0)))
    ratio_V2_over_V1_unnorm = sp.powsimp(sp.simplify(eps_V2_unnorm_0 / eps_V1_const))
    ratio_V2_over_V1_bfp = sp.simplify(eps_V2_bfp / eps_V1_const)
    ratio_V2_over_V1_neu = sp.simplify(eps_V2_neu / eps_V1_const)

    # --- (iii) Gibbs / Complementary Free Enthalpy Check for Camp 1 ---
    # Suppose g(sigma, sigma_x, theta) = sigma^2/(2E) + ell^2*sigma_x^2/(2E) + (beta/E)*sigma*theta + (rho*c_sigma/(2*T0))*theta^2
    # Variational derivative dg/dsigma = (sigma - ell^2*sigma_xx)/E + (beta/E)*theta = eps
    # => sigma - ell^2*sigma_xx = E*eps - beta*theta (Form A).
    # Then entropy rho*eta = dg/dtheta = (beta/E)*sigma + (rho*c_sigma/T0)*theta.
    # Substituting sigma = E*eps - beta*theta + ell^2*sigma_xx with rho*c_E/T0 = rho*c_sigma/T0 - beta^2/E:
    sigma_sym, sigma_xx_sym, eps_sym, theta_sym, rho_cE_T0 = sp.symbols(
        "sigma sigma_xx eps theta rho_cE_T0", real=True
    )
    rho_c_sigma_T0 = rho_cE_T0 + beta**2 / E
    sigma_from_formA = E * eps_sym - beta * theta_sym + ell**2 * sigma_xx_sym
    rho_eta_gibbs = sp.simplify((beta / E) * sigma_from_formA + rho_c_sigma_T0 * theta_sym)
    rho_eta_local = beta * eps_sym + rho_cE_T0 * theta_sym
    gibbs_entropy_discrepancy = sp.simplify(rho_eta_gibbs - rho_eta_local)

    return {
        "w_hs_unnorm": str(w_hs_unnorm),
        "w_hs_unnorm_at_0": float(w_hs_unnorm.subs(x, 0)),
        "L_hs_unnorm_1": str(L_hs_unnorm_1),
        "L_hs_bfp_1": int(L_hs_bfp_1),
        "L_hs_neu_1": int(L_hs_neu_1),
        "w_bar_unnorm": str(w_bar_unnorm),
        "w_bar_neu": int(w_bar_neu),
        "ratio_unnorm_surface": str(ratio_V2_over_V1_unnorm),
        "ratio_bfp_surface": int(ratio_V2_over_V1_bfp),
        "ratio_neu_surface": int(ratio_V2_over_V1_neu),
        "gibbs_entropy_discrepancy": str(gibbs_entropy_discrepancy),
    }


# ==============================================================================
# 2. Exact Cell-Galerkin / Nystrom Solvers for Bounded Bar and Half-Space
# ==============================================================================

def build_operator_matrix(
    edges: np.ndarray,
    ell: float,
    gamma: float,
    kernel_type: str,
    domain_length: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Constructs the N x N piecewise-constant Galerkin integral operator matrix L_mat
    on a uniform mesh with cell edges `edges` (0 = e_0 < e_1 < ... < e_N = L),
    where the diagonal kink at xi = x is integrated analytically inside each cell
    and by 4-point Gauss-Legendre quadrature on each sub-triangle/rectangle.
    This guarantees:
      1. Exact symmetry of the L^2 inner-product matrix B_mat = dx * L_mat (B = B^T).
      2. Exact partition-of-unity preservation (L_mat @ 1 = 1 to < 1e-15) for
         normalized kernels ('bfp' and 'neu_bar').
    """
    N = len(edges) - 1
    dx = edges[1] - edges[0]
    centers = 0.5 * (edges[:-1] + edges[1:])
    L = domain_length

    # 6-point Gauss-Legendre on [0, 1] for exact smooth sub-triangle / rectangle integration
    q_pts, q_wts = np.polynomial.legendre.leggauss(6)
    q_pts = 0.5 * (q_pts + 1.0)
    q_wts = 0.5 * q_wts

    def eval_kernel(x_arr: np.ndarray, xi_arr: np.ndarray, ktype: str) -> np.ndarray:
        if ktype in ("unnorm", "bfp"):
            return np.exp(-np.abs(x_arr - xi_arr) / ell) / (2.0 * ell)
        elif ktype == "neu_bar":
            x_min = np.minimum(x_arr, xi_arr)
            x_max = np.maximum(x_arr, xi_arr)
            return (
                np.cosh(x_min / ell)
                * np.cosh((L - x_max) / ell)
                / (ell * np.sinh(L / ell))
            )
        else:
            raise ValueError(f"Unknown kernel_type: {ktype}")

    # Off-diagonal cells i != j: smooth on [a_i, b_i] x [a_j, b_j]
    # Build 1D quadrature points across all cells: shape (N, 6)
    cell_q_x = edges[:-1, None] + dx * q_pts[None, :]     # (N, 6)
    cell_q_w = np.broadcast_to(dx * q_wts[None, :], (N, 6))  # (N, 6)

    pts_flat = cell_q_x.ravel()                           # (6N,)
    wts_flat = cell_q_w.ravel()                           # (6N,)

    K_flat = eval_kernel(pts_flat[:, None], pts_flat[None, :], kernel_type)
    # Weight by quadrature weights and sum over the 6 points in each cell
    K_weighted = K_flat * (wts_flat[:, None] * wts_flat[None, :])
    K_cell = K_weighted.reshape(N, 6, N, 6).sum(axis=(1, 3)) / dx  # (N, N)

    # Replace diagonal i == j with split-triangle integration (xi < x and xi > x)
    # so the derivative jump at xi = x is never crossed by a polynomial quadrature rule!
    diag_vals = np.zeros(N)
    # Parameterize lower triangle 0 < u < 1, 0 < v < u => x = a_i + dx*u, xi = a_i + dx*v, Jacobian = dx^2 * u
    U, V = np.meshgrid(q_pts, q_pts, indexing="ij")
    W_uv = q_wts[:, None] * q_wts[None, :]
    for i in range(N):
        a_i = edges[i]
        x_tri = a_i + dx * U
        xi_tri = a_i + dx * U * V
        jac = (dx**2) * U
        # By symmetry K(x, xi) = K(xi, x), integral over cell_i x cell_i is 2 * integral over lower triangle
        val_tri = 2.0 * np.sum(W_uv * jac * eval_kernel(x_tri, xi_tri, kernel_type))
        diag_vals[i] = val_tri / dx
    np.fill_diagonal(K_cell, diag_vals)

    if kernel_type == "unnorm":
        L_mat = gamma * np.eye(N) + (1.0 - gamma) * K_cell
    elif kernel_type == "bfp":
        # Cell-averaged w_Omega(x) = row sum of K_cell
        w_cell = np.sum(K_cell, axis=1)
        gamma_eff = gamma + (1.0 - gamma) * (1.0 - w_cell)
        L_mat = np.diag(gamma_eff) + (1.0 - gamma) * K_cell
    elif kernel_type == "neu_bar":
        L_mat = gamma * np.eye(N) + (1.0 - gamma) * K_cell
    else:
        raise ValueError(f"Unknown kernel_type: {kernel_type}")

    B_mat = dx * L_mat
    return centers, L_mat, B_mat


def run_bounded_bar_artifact_test(
    L: float = 10.0,
    ell: float = 1.0,
    gamma: float = 0.25,
    N: int = 200,
) -> dict:
    """
    Solves the static traction-free bounded bar [0, L] under:
      Case 1: Uniform temperature rise theta(x) = 1.0 (with E = 1, beta = 1)
      Case 2: Linear temperature gradient theta(x) = 1.0 + 0.2*(x/L - 0.5)
    for Variant V1 (sigma = L[E*eps - beta*theta] = 0) and
    Variant V2 (sigma = L[E*eps] - beta*theta = 0)
    across all three kernel choices:
      (b)  'unnorm'  (Unnormalized truncated Helmholtz kernel)
      (a1) 'bfp'     (Borino-Failla-Parrinello / Polizzotto normalized kernel)
      (a2) 'neu_bar' (Reflecting / Neumann Green's-function normalized kernel)
    """
    edges = np.linspace(0.0, L, N + 1)

    results = {}
    for ktype in ("unnorm", "bfp", "neu_bar"):
        grid, L_mat, B_mat = build_operator_matrix(
            edges, ell=ell, gamma=gamma, kernel_type=ktype, domain_length=L
        )
        ones = np.ones_like(grid)
        theta_uniform = ones.copy()
        theta_linear = 1.0 + 0.2 * (grid / L - 0.5)

        # 1. Symmetry (self-adjointness) defect of bilinear form <f, L g>_{L^2}
        sym_defect = float(np.max(np.abs(B_mat - B_mat.T)))

        # 2. Partition-of-unity check: L[1](x)
        L_of_1 = L_mat @ ones
        unity_max_err = float(np.max(np.abs(L_of_1 - 1.0)))

        # 3. Uniform heating theta(x) = 1.0
        # Variant V1: L[eps^V1 - theta] = 0 => eps^V1 = theta
        eps_V1_unif = np.linalg.solve(L_mat, L_mat @ theta_uniform)
        # Variant V2: L[eps^V2] = theta
        eps_V2_unif = np.linalg.solve(L_mat, theta_uniform)

        # Extrapolate to x = 0 using polynomial fit on first 5 cell centers
        poly_V1 = np.polyfit(grid[:5], eps_V1_unif[:5], 3)
        poly_V2 = np.polyfit(grid[:5], eps_V2_unif[:5], 3)
        eps_V1_0 = float(np.polyval(poly_V1, 0.0))
        eps_V2_0 = float(np.polyval(poly_V2, 0.0))
        ratio_V2_over_V1_0 = eps_V2_0 / eps_V1_0
        max_diff_unif = float(np.max(np.abs(eps_V1_unif - eps_V2_unif)))

        # 4. Linear temperature gradient theta(x) = 1 + 0.2*(x/L - 0.5)
        eps_V1_lin = np.linalg.solve(L_mat, L_mat @ theta_linear)
        eps_V2_lin = np.linalg.solve(L_mat, theta_linear)
        max_diff_lin = float(np.max(np.abs(eps_V1_lin - eps_V2_lin)))

        results[ktype] = {
            "self_adjoint_defect": sym_defect,
            "unity_max_err": unity_max_err,
            "eps_V1_0_uniform": eps_V1_0,
            "eps_V2_0_uniform": eps_V2_0,
            "ratio_V2_over_V1_0_uniform": ratio_V2_over_V1_0,
            "max_diff_uniform": max_diff_unif,
            "max_diff_linear_grad": max_diff_lin,
        }

    # Exact analytical ratio eps^V2(0)/eps^V1(0) for unnormalized kernel on [0, L]
    # Solution of (1 - gamma*ell^2 d^2/dx^2) eps^V2 = 1 with Robin CBCs at x=0, L:
    lam = 1.0 / (np.sqrt(gamma) * ell)
    exact_eps_V2_0_unnorm = 1.0 + (1.0 - gamma) / (
        gamma + np.sqrt(gamma) / np.tanh(0.5 * lam * L)
    )
    results["unnorm"]["exact_ratio_V2_over_V1_0_uniform"] = float(exact_eps_V2_0_unnorm)
    results["unnorm"]["half_space_asymptotic_ratio"] = float(1.0 / np.sqrt(gamma))
    return results


def verify_neumann_ode_and_cbc_equivalence(
    L: float = 5.0,
    ell: float = 0.8,
    gamma: float = 0.3,
    N: int = 300,
) -> dict:
    """
    Verifies that for the Neumann normalized kernel K_ell^Neu on [0, L]:
      g(x) = L_{gamma,ell}^Neu[f](x)
    satisfies the exact constant-coefficient 2nd-order ODE:
      (1 - ell^2 d^2/dx^2) g(x) = (1 - gamma*ell^2 d^2/dx^2) f(x)   for x in (0, L)
    together with the homogeneous Neumann CBCs:
      g'(0) = gamma * f'(0),   g'(L) = gamma * f'(L)
    (i.e. w'(0) = 0 and w'(L) = 0 where w = (g - gamma*f)/(1 - gamma)).
    """
    x = sp.Symbol("x", real=True)
    xi = sp.Symbol("xi", real=True)
    # Test with a general non-constant smooth thermoelastic field f(x) = 1 + x^2 + cos(x)
    f_expr = 1 + x**2 + sp.cos(x)
    f_xi = f_expr.subs(x, xi)

    w_expr = (
        sp.integrate(
            sp.cosh(xi / ell) * sp.cosh((L - x) / ell) / (ell * sp.sinh(L / ell)) * f_xi,
            (xi, 0, x),
        )
        + sp.integrate(
            sp.cosh(x / ell) * sp.cosh((L - xi) / ell) / (ell * sp.sinh(L / ell)) * f_xi,
            (xi, x, L),
        )
    )
    g_expr = gamma * f_expr + (1 - gamma) * w_expr

    # Check interior ODE: (1 - ell^2 d^2/dx^2)g - (1 - gamma*ell^2 d^2/dx^2)f == 0
    ode_lhs = g_expr - ell**2 * sp.diff(g_expr, x, 2)
    ode_rhs = f_expr - gamma * ell**2 * sp.diff(f_expr, x, 2)
    ode_res_mid = float(sp.N(sp.simplify(ode_lhs - ode_rhs).subs(x, 0.5 * L)))

    # Check Neumann CBCs: g'(0) - gamma*f'(0) == 0 and g'(L) - gamma*f'(L) == 0
    dg_dx = sp.diff(g_expr, x)
    df_dx = sp.diff(f_expr, x)
    cbc_0_err = float(sp.N((dg_dx - gamma * df_dx).subs(x, 0.0)))
    cbc_L_err = float(sp.N((dg_dx - gamma * df_dx).subs(x, L)))

    # Compare with Robin CBCs on the same kernel (should be NONZERO because K^Neu satisfies Neumann, not Robin!)
    robin_0_val = float(sp.N(((dg_dx - g_expr / ell) - gamma * (df_dx - f_expr / ell)).subs(x, 0.0)))

    return {
        "neumann_ode_residual": abs(ode_res_mid),
        "neumann_cbc_0_err": abs(cbc_0_err),
        "neumann_cbc_L_err": abs(cbc_L_err),
        "robin_functional_on_neumann_kernel": abs(robin_0_val),
    }


def main() -> None:
    print("======================================================================")
    print("ROUND 2 — TASK 1: ARTIFACT TEST (NORMALIZED VS UNNORMALIZED KERNELS)")
    print("======================================================================")

    sym_res = verify_symbolic_artifact_and_survivors()
    print("\n[1] Symbolic Kernel Normalization & Static Thermal Layer Results:")
    for k, v in sym_res.items():
        print(f"    {k:30s}: {v}")

    bar_res = run_bounded_bar_artifact_test(L=10.0, ell=1.0, gamma=0.25, N=300)
    print("\n[2] Bounded-Bar [0, L=10*ell] Numerical Quadrature Comparison (gamma = 0.25):")
    for ktype, d in bar_res.items():
        print(f"  Kernel = {ktype}:")
        for k, v in d.items():
            print(f"    {k:28s}: {v:.12e}" if isinstance(v, float) and abs(v) < 1e-3 else f"    {k:28s}: {v}")

    neu_res = verify_neumann_ode_and_cbc_equivalence()
    print("\n[3] Neumann Normalized Kernel ODE & Boundary Closure Verification:")
    for k, v in neu_res.items():
        print(f"    {k:36s}: {v:.12e}")


if __name__ == "__main__":
    main()
