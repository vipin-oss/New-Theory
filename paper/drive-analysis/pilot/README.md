# Pilot Verification — Candidate C1

**Model:** Variational Two-Phase Integral Nonlocal Generalized Thermoelasticity on Bounded Domains (`[0, L]`), coupled to the three-lag / Moore–Gibson–Thompson / Green–Naghdi heat-flux template.

## What this pilot verifies

1. **Thermodynamic Reciprocity & Free-Energy Resolution (`Review Gap 8`):**
   - `run_symbolic_checks()` in `pilot.py` uses SymPy to verify exact Helmholtz free-energy reciprocity and localized availability balance for **Variational Model V1** ($\mathcal{M}_\varepsilon$: strain-kernel nonlocality $\implies$ Form B stress + constant-strain entropy) and **Variational Model V2** ($\mathcal{M}_{\varepsilon^{\mathrm{el}}}$: elastic-strain-kernel nonlocality $\implies$ Form A stress + constant-stress entropy), and proves algebraically why the literature's standard **mismatched Form A** (Form A stress paired with constant-strain local dilatation heating) leaves an uncompensated internal power source that violates the Second Law.
2. **Three-Lag Heat-Flux Template Passivity (`Review Gap 1`):**
   - Proves $\operatorname{Re} G(-i\omega) = \frac{k + k^*(\tau_v - \tau_q) + k\tau_T\tau_q\omega^2}{1 + \omega^2\tau_q^2}$, establishing passivity for all $\varepsilon > 0$ iff $k + k^*(\tau_v - \tau_q) \ge 0$ and $k\tau_T\tau_q \ge 0$.
3. **Non-Circular Integral Equivalence & Boundary-Layer Mode (`Questions R1, R2, R6`):**
   - Cross-verifies the analytical **3-mode (6-wave) differential + Robin-CBC solver** ($\partial_x w(0) - \xi^{-1}w(0) = 0$, $\partial_x w(L) + \xi^{-1}w(L) = 0$) against a completely independent **Legendre spectral-Galerkin Fredholm integral solver** that discretizes $\int_0^L K_\xi(x,x')\phi(x')\,dx'$ directly without differential reduction or CBCs: relative $L^\infty$ displacement error `4.75e-15`, exact integral-law residual `7.41e-16` (versus `22.3%` error for the naive 2-mode differential shortcut used across 2019–2026 literature).
   - Verifies exact spatial constancy of the new **interpoint nonlocal availability flux** $\langle P_x(x)\rangle$ in conservative GN-II thermoelasticity (`1.67e-16` for V1, `2.22e-16` for V2, versus `4.71e-3` when omitting the nonlocal flux term and `2.96e-3` for mismatched Form A).
4. **Singular Pure-Nonlocal Limit $\gamma \to 0^+$:**
   - Tracks the nonlocal boundary-layer eigenvalue $|\lambda_3|\xi \sim \gamma^{-1/2}$ and boundary strain-layer blow-up as the local elastic mixture fraction $\gamma \to 0^+$.

## Reproducing all results and tests

```bash
python pilot.py
pytest -q test_pilot.py
```

Outputs: `data.json`, `fig1_integral_residual.png`, `fig2_reciprocity_energy_conservation.png`, `fig3_dispersion_and_damping_cutoff.png`, `fig4_singular_mixture_limit.png`.
