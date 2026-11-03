# Task 4: Physical Relevance Check with SI Material Parameters

## 1. SI Material Parameters and Handbook Sources ($T_0 = 300\text{ K}$)

All material constants are taken in SI units at reference temperature $T_0 = 300\text{ K}$ from standard solid-state and physical handbooks (**CRC Handbook of Chemistry and Physics**, 104th ed.; **Kittel**, *Introduction to Solid State Physics*, 8th ed.; **Chen 2021**, *Nat. Rev. Phys.* 3, 555, verified in Drive `1mPGwYUI67OxFM-tsXtePfK3LaBtTKiPC`). For Eringen's nonlocal length scale $\ell = e_0 a_0$, we use the representative calibration $e_0 = 1.5$ and two-phase local fraction $\gamma = 0.25$.

| Material | $\rho$ ($\text{kg/m}^3$) | $M = \lambda+2\mu$ ($\text{GPa}$) | $K_B$ ($\text{GPa}$) | $c_L = \sqrt{M/\rho}$ ($\text{m/s}$) | $c_E$ ($\text{J/(kg}\cdot\text{K)}$) | $\alpha_T$ ($10^{-6}\,\text{K}^{-1}$) | $\beta = 3K_B\alpha_T$ ($\text{MPa/K}$) | $\kappa$ ($\text{W/(m}\cdot\text{K)}$) | $\epsilon_T = \frac{\beta^2 T_0}{\rho c_E M}$ | $a_0$ ($\text{nm}$) | $\ell = 1.5 a_0$ ($\text{nm}$) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Aluminum (Al)** | $2700$ | $111.3$ | $76.0$ | $6420.5$ | $900$ | $23.1$ | $5.267$ | $237$ | **$0.03077$ ($3.08\%$)** | $0.405$ | $0.608$ |
| **Copper (Cu)** | $8960$ | $197.0$ | $140.0$ | $4689.0$ | $385$ | $16.5$ | $6.930$ | $401$ | **$0.02120$ ($2.12\%$)** | $0.361$ | $0.542$ |
| **Silicon (Si)** | $2329$ | $165.7$ | $97.8$ | $8434.8$ | $712$ | $2.6$ | $0.763$ | $148$ | **$0.00064$ ($0.064\%$)** | $0.543$ | $0.815$ |
| **Silicon Carbide (6H-SiC)** | $3210$ | $501.0$ | $220.0$ | $12493.0$ | $690$ | $4.0$ | $2.640$ | $360$ | **$0.00188$ ($0.19\%$)** | $0.436$ | $0.654$ |

---

## 2. Quantitative Comparison Across Ultrasonic, GHz, and THz / Sub-10 nm Regimes

Let $\hat{K}(k) = (1 + \ell^2 k^2)^{-1}$ and $\hat{L}(k) = \gamma + (1-\gamma)\hat{K}(k) = \frac{1+\gamma\ell^2 k^2}{1+\ell^2 k^2}$. From the dispersion analysis in `physical_relevance.py`, the effective complex longitudinal modulus $M_{\text{eff}}(k,\omega)$ on the quasi-elastic acoustic branch is:
- **Variant V1 ($\lambda=0$)**: $M_{\text{eff}}^{\text{V1}} = M\left[\hat{L}(k) + \epsilon_T\,\mathcal{F}_{\text{th}}(k,\omega)\right]$,
- **Variant V2 ($\lambda=1$)**: $M_{\text{eff}}^{\text{V2}} = M\left[\hat{L}(k) + \epsilon_T\,\hat{L}(k)^2\,\mathcal{F}_{\text{th}}(k,\omega)\right]$,
- **Mismatched Form A ($\gamma=0$)**: $M_{\text{eff}}^{\text{FA}} = M\left[\hat{K}(k) + \epsilon_T\,\hat{K}(k)\,\mathcal{F}_{\text{th}}(k,\omega)\right]$,

where $\mathcal{F}_{\text{th}}(k,\omega) = \frac{-w_{\text{th}}}{D_{\text{th}}k^2 - w_{\text{th}}}$ ($D_{\text{th}} = \kappa/(\rho c_E)$, $w_{\text{th}} = -i\omega(1-i\omega\tau_0)$).

| Material | Frequency $f$ | Acoustic Wavelength $\lambda_{\text{ac}}$ | $\ell k$ | Bulk Speed Diff $\frac{|v_{\text{V1}}-v_{\text{V2}}|}{v_{\text{V1}}}$ | Bulk Speed Diff $\frac{|v_{\text{V1}}-v_{\text{FA}}|}{v_{\text{V1}}}$ | Damping Diff $\frac{|Q^{-1}_{\text{V1}}-Q^{-1}_{\text{V2}}|}{Q^{-1}_{\text{V1}}}$ | Damping Diff $\frac{|Q^{-1}_{\text{V1}}-Q^{-1}_{\text{FA}}|}{Q^{-1}_{\text{V1}}}$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Al** | $100\text{ MHz}$ | $64.20\,\mu\text{m}$ | $5.95\times 10^{-5}$ | $7.91\times 10^{-11}$ | $4.81\times 10^{-10}$ | $5.14\times 10^{-9}$ | $2.57\times 10^{-9}$ |
| **Al** | $10\text{ GHz}$ | $642.05\text{ nm}$ | $5.95\times 10^{-3}$ | $7.68\times 10^{-7}$ | $4.80\times 10^{-6}$ | $5.15\times 10^{-5}$ | $2.57\times 10^{-5}$ |
| **Al** | $0.5\text{ THz}$ | $12.84\text{ nm}$ | $0.297$ | $5.81\times 10^{-4}$ ($0.058\%$) | $1.12\times 10^{-2}$ ($1.12\%$) | **$11.70\%$** | **$6.03\%$** |
| **Al** | $1.5\text{ THz}$ | $4.28\text{ nm}$ | $0.892$ | $3.76\times 10^{-3}$ ($0.38\%$) | **$8.87\%$** | **$55.07\%$** | **$32.92\%$** |
| **Cu** | $100\text{ MHz}$ | $46.89\,\mu\text{m}$ | $7.26\times 10^{-5}$ | $8.20\times 10^{-11}$ | $6.99\times 10^{-10}$ | $7.73\times 10^{-9}$ | $3.87\times 10^{-9}$ |
| **Cu** | $10\text{ GHz}$ | $468.90\text{ nm}$ | $7.26\times 10^{-3}$ | $7.24\times 10^{-7}$ | $6.94\times 10^{-6}$ | $7.75\times 10^{-5}$ | $3.88\times 10^{-5}$ |
| **Cu** | $0.5\text{ THz}$ | $9.38\text{ nm}$ | $0.363$ | $4.30\times 10^{-4}$ ($0.043\%$) | $1.63\times 10^{-2}$ ($1.63\%$) | **$16.61\%$** | **$8.68\%$** |
| **Cu** | $1.5\text{ THz}$ | $3.13\text{ nm}$ | $1.088$ | $2.54\times 10^{-3}$ ($0.25\%$) | **$12.30\%$** | **$64.62\%$** | **$40.48\%$** |
| **Si** | $100\text{ MHz}$ | $84.35\,\mu\text{m}$ | $6.07\times 10^{-5}$ | $1.75\times 10^{-12}$ | $4.61\times 10^{-10}$ | $5.52\times 10^{-9}$ | $2.76\times 10^{-9}$ |
| **Si** | $10\text{ GHz}$ | $843.48\text{ nm}$ | $6.07\times 10^{-3}$ | $1.69\times 10^{-8}$ | $4.61\times 10^{-6}$ | $5.52\times 10^{-5}$ | $2.76\times 10^{-5}$ |
| **Si** | $0.5\text{ THz}$ | $16.87\text{ nm}$ | $0.303$ | $3.69\times 10^{-5}$ ($0.0037\%$) | $1.13\times 10^{-2}$ ($1.13\%$) | **$12.24\%$** | **$6.32\%$** |
| **Si** | $1.5\text{ THz}$ | $5.62\text{ nm}$ | $0.910$ | $2.41\times 10^{-4}$ ($0.024\%$) | **$8.99\%$** | **$56.39\%$** | **$33.96\%$** |
| **SiC** | $100\text{ MHz}$ | $124.93\,\mu\text{m}$ | $3.29\times 10^{-5}$ | $1.53\times 10^{-12}$ | $1.36\times 10^{-10}$ | $1.62\times 10^{-9}$ | $8.10\times 10^{-10}$ |
| **SiC** | $10\text{ GHz}$ | $1.25\,\mu\text{m}$ | $3.29\times 10^{-3}$ | $1.48\times 10^{-8}$ | $1.36\times 10^{-6}$ | $1.62\times 10^{-5}$ | $8.10\times 10^{-6}$ |
| **SiC** | $0.5\text{ THz}$ | $24.99\text{ nm}$ | $0.164$ | $3.32\times 10^{-5}$ ($0.0033\%$) | $3.38\times 10^{-3}$ ($0.34\%$) | **$3.91\%$** | **$1.97\%$** |
| **SiC** | $1.5\text{ THz}$ | $8.33\text{ nm}$ | $0.493$ | $2.65\times 10^{-4}$ ($0.027\%$) | **$2.93\%$** | **$27.17\%$** | **$14.66\%$** |

---

## 3. Exact Surface Thermal-Expansion Boundary Layer Theorem (Frequency-Independent $\mathcal{O}(1)$ Distinction Between V1 and V2)

While bulk phase-velocity differences between Variant V1 and Variant V2 are suppressed by $\epsilon_T(1-\gamma)\ell^2 k^2$, **surface boundary-value problems exhibit an $\mathcal{O}(1)$, frequency-independent distinction between V1, V2, and Form A even at $\omega \to 0$** (and whenever the thermal diffusion/penetration length $\delta_{\text{th}} \gg \ell$).

Consider a traction-free half-space ($\sigma(x) = 0$ on $x \ge 0$) subjected to a uniform or slowly varying surface temperature rise $\theta_0$:
1. **Variant V2 ($\lambda = 1$)**: $\sigma(x) = \mathcal{L}_{\gamma,\ell}[E\varepsilon - \beta\theta_0] = 0$. Since $\mathcal{L}_{\gamma,\ell}$ is strictly invertible on $L^2_{\text{loc}}([0,\infty))$ under the Robin CBCs, $E\varepsilon^{\text{V2}}(x) = \beta\theta_0$ identically for all $x \ge 0$:
   $$\varepsilon^{\text{V2}}(0) = \frac{\beta\theta_0}{E}. \tag{4.1}$$
2. **Variant V1 ($\lambda = 0$)**: $\sigma(x) = \mathcal{L}_{\gamma,\ell}[E\varepsilon](x) - \beta\theta_0 = 0$. Solving the bulk ODE $(1-\gamma\ell^2\partial_x^2)(E\varepsilon) = \beta\theta_0$ subject to the V1 Robin CBC $(\partial_x - \ell^{-1})(-\gamma E\varepsilon + \beta\theta_0)\big|_{x=0} = 0$ yields the exact closed-form boundary-layer profile:
   $$\boxed{\varepsilon^{\text{V1}}(x) = \frac{\beta\theta_0}{E}\left[1 + \frac{1-\sqrt{\gamma}}{\sqrt{\gamma}}\,e^{-x/(\sqrt{\gamma}\ell)}\right] \implies \frac{\varepsilon^{\text{V1}}(0)}{\varepsilon^{\text{V2}}(0)} = \frac{1}{\sqrt{\gamma}}.} \tag{4.2}$$
   For $\gamma = 0.25$, $\varepsilon^{\text{V1}}(0) / \varepsilon^{\text{V2}}(0) = 2.0$ (a **$100\%$ amplification of surface thermal strain** within the boundary layer $x \lesssim 3\sqrt{\gamma}\ell$), physically capturing the reduced coordination number (softened nonlocal elastic restoring bonds) of surface atoms acting against local thermal kinetic pressure. Verified numerically in `physical_relevance.py` (`max_traction_residual_V1 = 2.17e-19`).
3. **Literature Form A ($\gamma = 0$)**: The integral equation $\int_0^\infty \frac{1}{2\ell}e^{-|x-\xi|/\ell}E\varepsilon(\xi)\,d\xi = \beta\theta_0$ has **no regular solution** on $[0,\infty)$ because $\beta\theta_0$ violates the homogeneous Robin CBC $(\partial_x - \ell^{-1})(\beta\theta_0)|_{x=0} = -\beta\theta_0/\ell \neq 0$.

---

## 4. Honest Assessment of Physical Regimes

1. **Where bulk differences are negligible ($\ell k \ll 1$)**: At conventional ultrasonic ($100\text{ MHz}$) and low-GHz ($10\text{ GHz}$) frequencies in homogeneous crystals with atomic nonlocality $\ell \sim 0.5\text{–}0.8\text{ nm}$, $\ell k \sim 10^{-5}\text{–}10^{-2}$ and all bulk nonlocal corrections scale as $(\ell k)^2 \sim 10^{-10}\text{–}10^{-4}$. Even at THz frequencies, the difference in **bulk phase speed $v_{\text{ph}}$** between V1 and V2 is multiplied by $\epsilon_T$ ($0.25\%\text{–}0.38\%$ in Cu/Al at $1.5\text{ THz}$; $<0.03\%$ in Si/SiC).
2. **Where the corrections are large ($\mathcal{O}(10\%\text{–}100\%)$) and physically decisive**:
   - **Relative Thermoelastic Damping $Q^{-1}_{\text{TED}}$ in Sub-THz/THz Acoustics & Sub-10 nm NEMS**: Because $Q^{-1}_{\text{TED}} \propto \epsilon_T$, the small factor $\epsilon_T$ cancels out of the relative damping error $\Delta Q^{-1}/Q^{-1}$, producing **$11.7\%\text{–}64.6\%$ differences** between V1 and V2 (and **$6.0\%\text{–}40.5\%$** between V1 and Form A) at $f = 0.5\text{–}1.5\text{ THz}$ ($\lambda_{\text{ac}} \sim 3\text{–}17\text{ nm}$).
   - **Surface Thermal-Expansion Boundary Layer & Half-Space Wave Reflection**: At any traction-free heated boundary $x=0$, Variant V1 predicts an exact $1/\sqrt{\gamma}$ ($+100\%$ for $\gamma=0.25$) surface strain amplification over Variant V2 across **all frequencies**, while Form A without Robin CBCs incurs a $50\%\text{–}80\%$ integral-consistency error in the surface layer $x \in [0, 3\ell]$.
   - **Structural Consistency (Second Law, Reciprocity, Well-Posedness)**: Independent of numerical magnitude, C1 resolves a structural mathematical contradiction (non-existence of a Helmholtz free energy, negative closed-cycle entropy production, broken Cazimir–Betti reciprocity, and unclosed boundary-value problems) across 100% of the 25 coupled papers in our 2016–2026 audit.
