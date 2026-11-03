# Task 4: Physical & Numerical Grounding

All numerical values below are computed reproducibly in `paper/c2-hardening/verify_c2_hardening.py` (`section5_material_and_parameter_grounding`) and saved in `paper/c2-hardening/verification_results.json`.

---

## 1. Evaluation on Four Real Physical Media

We evaluate the characteristic thermoelastic parameters, passivity margins for both the $(1,1,1)$ first-order-in-$\tau_q$ TPL model and the $(2,1,1)$ second-order-in-$\tau_q$ TPL model, hyperbolic MGT wavefront speeds $v_\pm$ (in the $\tau_T \to 0$ limit), and high-frequency elastic spatial attenuation $\kappa_\infty = \frac{\varepsilon\rho c_E c_1 \tau_q}{2 k \tau_T}$ (for $\tau_T > 0$) across four canonical physical media:

1. **Copper (Cu) at $T_0 = 293\text{ K}$** (polycrystalline metal; parameters from Sinha & Elsibai 1996, 1997; Sherief, Hamza & Saleh 2010):
   $\rho = 8954\text{ kg/m}^3$, $c_E = 383.1\text{ J/(kg}\cdot\text{K)}$, $k = 386\text{ W/(m}\cdot\text{K)}$, $\lambda_{\text{L}} = 77.6\text{ GPa}$, $\mu_{\text{L}} = 38.6\text{ GPa}$, $\alpha_T = 1.78\times 10^{-5}\text{ K}^{-1}$, $\tau_q = 20\text{ ps}$, $\tau_T = 10\text{ ps}$, $\tau_v = 5\text{ ps}$, $k^*/k = 10^{10}\text{ s}^{-1}$.
2. **Silicon (Si) at $T_0 = 300\text{ K}$** (semiconductor wafer; parameters from Zenkour & El-Mekawy 2020; Cahill et al. 2003):
   $\rho = 2330\text{ kg/m}^3$, $c_E = 710\text{ J/(kg}\cdot\text{K)}$, $k = 148\text{ W/(m}\cdot\text{K)}$, $\lambda_{\text{L}} = 64.0\text{ GPa}$, $\mu_{\text{L}} = 50.9\text{ GPa}$, $\alpha_T = 2.6\times 10^{-6}\text{ K}^{-1}$, $\tau_q = 100\text{ ps}$, $\tau_T = 50\text{ ps}$, $\tau_v = 20\text{ ps}$, $k^*/k = 5\times 10^9\text{ s}^{-1}$.
3. **Cryogenic Sodium Fluoride (NaF) at $T_0 = 15\text{ K}$** (dielectric crystal in the ballistic-diffusive second-sound window; Jackson, Walker & McNelly 1970; Dreyer & Struchtrup 1993):
   $\rho = 2850\text{ kg/m}^3$, $c_E = 1.8\text{ J/(kg}\cdot\text{K)}$, $k = 12,500\text{ W/(m}\cdot\text{K)}$, $\lambda_{\text{L}} = 29.0\text{ GPa}$, $\mu_{\text{L}} = 31.0\text{ GPa}$, $\alpha_T = 5.0\times 10^{-7}\text{ K}^{-1}$, $\tau_q = 0.75\ \mu\text{s}$, $\tau_T = 0\text{ s}$ (hyperbolic second-sound regime), $\tau_v = 0.15\ \mu\text{s}$, $k^*/k = 10^6\text{ s}^{-1}$.
4. **Porous Biological Tissue at $T_0 = 310\text{ K}$** (macroscopic phase-lag bioheat regime; Mitra et al. 1995; Liu & Wang 2020, *Sci. Rep.* 10:16379):
   $\rho = 1060\text{ kg/m}^3$, $c_E = 3600\text{ J/(kg}\cdot\text{K)}$, $k = 0.5\text{ W/(m}\cdot\text{K)}$, $\lambda_{\text{L}} = 10\text{ MPa}$, $\mu_{\text{L}} = 2\text{ MPa}$, $\alpha_T = 1.0\times 10^{-4}\text{ K}^{-1}$, $\tau_q = 16.0\text{ s}$, $\tau_T = 6.0\text{ s}$, $\tau_v = 2.0\text{ s}$, $k^*/k = 0.05\text{ s}^{-1}$.

### Table 4.1: Quantitative Thermoelastic, Passivity, and Wavefront Audit Across Four Physical Media

| Quantity | Symbol / Formula | Copper (Cu, 293 K) | Silicon (Si, 300 K) | Cryogenic NaF (15 K) | Biological Tissue (310 K) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Longitudinal elastic speed | $c_1 = \sqrt{(\lambda_{\text{L}}+2\mu_{\text{L}})/\rho}$ | $4157.93\text{ m/s}$ | $8435.57\text{ m/s}$ | $5650.65\text{ m/s}$ | $114.92\text{ m/s}$ |
| Shear elastic speed | $c_2 = \sqrt{\mu_{\text{L}}/\rho}$ | $2076.28\text{ m/s}$ | $4673.92\text{ m/s}$ | $3298.06\text{ m/s}$ | $43.44\text{ m/s}$ |
| Thermal diffusivity | $\alpha = k/(\rho c_E)$ | $1.1253\times 10^{-4}\text{ m}^2\text{/s}$ | $8.9464\times 10^{-5}\text{ m}^2\text{/s}$ | $2.4366\text{ m}^2\text{/s}$ | $1.3103\times 10^{-7}\text{ m}^2\text{/s}$ |
| Characteristic frequency | $\omega^* = c_1^2/\alpha$ | $1.5364\times 10^{11}\text{ rad/s}$ | $7.9539\times 10^{11}\text{ rad/s}$ | $1.3104\times 10^7\text{ rad/s}$ | $1.0080\times 10^{11}\text{ rad/s}$ |
| Thermoelastic coupling | $\varepsilon = \frac{\beta^2 T_0}{\rho c_E(\lambda_{\text{L}}+2\mu_{\text{L}})}$ | $1.6801\times 10^{-2}$ | $6.3822\times 10^{-4}$ | $1.7834\times 10^{-4}$ | $6.7078\times 10^{-5}$ |
| $(1,1,1)$ Passivity margin | $\chi_{111} = k + k^*(\tau_v - \tau_q)$ | $+328.1\text{ W/(m}\cdot\text{K)}$ | $+88.8\text{ W/(m}\cdot\text{K)}$ | $+5000.0\text{ W/(m}\cdot\text{K)}$ | $+0.15\text{ W/(m}\cdot\text{K)}$ |
| Normalized $(1,1,1)$ margin | $\chi_{111}/k = 1 + \frac{k^*}{k}(\tau_v - \tau_q)$ | $+0.8500$ (**PASSIVE**) | $+0.6000$ (**PASSIVE**) | $+0.4000$ (**PASSIVE**) | $+0.3000$ (**PASSIVE**) |
| $(2,1,1)$ 2nd passivity margin | $\kappa_{211} = \tau_T k - \frac{\tau_q}{2}(k + k^*\tau_v)$ | $-1.93\times 10^{-10}$ (**FAILS**) | $-7.40\times 10^{-10}$ (**FAILS**) | $-5.39\times 10^{-3}$ (**FAILS**) | $-1.40$ (**FAILS**) |
| Uncoupled MGT thermal speed | $c_T = \sqrt{(k+k^*\tau_v)/(\rho c_E\tau_q)}$ | $2430.57\text{ m/s}$ | $992.02\text{ m/s}$ | $1932.92\text{ m/s}$ | $0.0030\text{ m/s}$ |
| Coupled fast wavefront ($\tau_T=0$) | $v_+$ (Eq. 2.34) | $4209.99\text{ m/s}$ | $8438.30\text{ m/s}$ | $5651.22\text{ m/s}$ | $114.93\text{ m/s}$ |
| Coupled slow wavefront ($\tau_T=0$) | $v_-$ (Eq. 2.34) | $2400.51\text{ m/s}$ | $991.70\text{ m/s}$ | $1932.73\text{ m/s}$ | $0.0030\text{ m/s}$ |
| High-freq. elastic attenuation ($\tau_T>0$) | $\kappa_\infty = \frac{\varepsilon\rho c_E c_1 \tau_q}{2 k \tau_T}$ | $6.2080\times 10^5\text{ m}^{-1}$ | $6.0178\times 10^4\text{ m}^{-1}$ | $0$ ($\tau_T = 0$) | $7.8446\times 10^4\text{ m}^{-1}$ |

---

## 2. Audit of Published TPL Parameter Sets in the Literature

A major physical finding of our numerical audit is the contrast between the $(1,1,1)$ model and the $(2,1,1)$ model under the textbook TPL ordering $0 \le \tau_v < \tau_T < \tau_q$ (imposed e.g. in Choudhuri 2007, Akbarzadeh & Pasini 2014, Zenkour & El-Mekawy 2020, and Liu & Wang 2020):

* **Why the $(2,1,1)$ hyperbolic TPL model fails on standard literature parameter sets**:
  In the $(2,1,1)$ model, the second passivity inequality $\kappa_{211} = \tau_T k - \frac{\tau_q}{2}(k + k^*\tau_v) \ge 0$ requires
  $$\frac{\tau_T}{\tau_q} \ge \frac{1}{2}\Bigl(1 + \frac{k^*}{k}\tau_v\Bigr) > \frac{1}{2}. \tag{4.1}$$
  Whenever authors select $\tau_T \le \tau_q/2$ (as in Cu with $\tau_T/\tau_q = 0.5$, Si with $\tau_T/\tau_q = 0.5$, and Liu & Wang 2020 bioheat with $\tau_T = 6\text{ s}, \tau_q = 16\text{ s} \implies \tau_T/\tau_q = 0.375 < 0.5$), the $(2,1,1)$ model **violates Second-Law passivity** ($\operatorname{Re} G^{(2,1,1)}(-\mathrm{i}\omega) < 0$ at high frequencies $\omega \gg \tau_q^{-1}$) and exhibits high-frequency instability!
* **Why the $(1,1,1)$ TPL model also fails when $k^*/k > (\tau_q - \tau_v)^{-1}$**:
  In the $(1,1,1)$ model, $\chi_{111} = k + k^*(\tau_v - \tau_q) \ge 0$ requires
  $$\tau_q - \tau_v \le \frac{k}{k^*} =: \tau_{\text{GN}}. \tag{4.2}$$
  In **Akbarzadeh & Pasini (2014, *Int. J. Heat Mass Transfer* 75:656–667, Fig. 2)**, the dimensionless TPL parameters are chosen as $k = 1, k^* = 1, \tau_q = 1.5, \tau_T = 1.0, \tau_v = 0.2$, which yields
  $$\chi_{111} = 1.0 + 1.0(0.2 - 1.5) = -0.3 < 0!$$
  Thus that published TPL benchmark curve lies in the **thermodynamically active (non-passive) regime** where long-wavelength modes amplify exponentially unless stabilized by a small bounded domain ($\mu_1(\Omega) > \xi_{\text{crit}}^2$, Counterexample 1).

### Table 4.2: Passivity Audit of Six Published / Canonical TPL Parameter Sets

| Literature Reference | Parameter Values $(k, k^*, \tau_q, \tau_T, \tau_v)$ | $\chi_{111} = k + k^*(\tau_v - \tau_q)$ | $(1,1,1)$ Passive? | $\kappa_{211} = \tau_T k - \frac{\tau_q}{2}(k + k^*\tau_v)$ | $(2,1,1)$ Passive? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Quintanilla & Racke (2008)** (*IJHMT* 51:24–29) — Stable Case | $(1.0, 0.5, 1.0, 0.5, 0.2)$ | $+0.6000$ | **YES** | $-0.0500$ | **NO** ($\tau_T/\tau_q = 0.5$ too small) |
| **Quintanilla & Racke (2008)** (*IJHMT* 51:24–29) — Unstable Case | $(1.0, 2.0, 1.0, 0.5, 0.2)$ | $-0.6000$ | **NO** | $-0.2000$ | **NO** |
| **Akbarzadeh & Pasini (2014)** (*IJHMT* 75:656–667, Fig. 2 TPL) | $(1.0, 1.0, 1.5, 1.0, 0.2)$ | $-0.3000$ | **NO** (violates $\tau_q - \tau_v \le k/k^*$) | $+0.1000$ | **NO** ($\chi_{111} < 0$) |
| **Zenkour & El-Mekawy (2020)** (*ICHMT* 116:104722, Sec. 3) | $(1.0, 0.2, 0.05, 0.03, 0.01)$ | $+0.9920$ | **YES** | $+0.0049$ | **YES** ($\tau_T/\tau_q = 0.6 > 0.501$) |
| **Liu & Wang (2020)** (*Sci. Rep.* 10:16379, Bioheat TPL) | $(0.5, 0.025, 16.0, 6.0, 2.0)$ | $+0.1500$ | **YES** | $-1.4000$ | **NO** ($\tau_T/\tau_q = 0.375 < 0.55$) |
| **Ad-hoc High-$k^*$ Nondimensional Set** | $(1.0, 2.0, 0.8, 0.4, 0.1)$ | $-0.4000$ | **NO** | $-0.0800$ | **NO** |
