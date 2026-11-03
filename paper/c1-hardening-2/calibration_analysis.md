# Task 4 — Calibration & Frequency-Regime Audit: Physical Scale of Nonlocal Thermoelastic Effects in Real Materials

**Verification script**: [`calibration_audit.py`](./calibration_audit.py)  
**Automated test suite**: [`test_c1_round2.py`](./test_c1_round2.py) (`test_calibrated_aluminum_and_silicon_fourier_regime`)

---

## 1. Executive Answer to Task 4

We audited the two-phase nonlocal thermoelastic model (Variant V1 and Variant V2 vs. Camp 1) on two benchmark crystalline solids at $T_0 = 300\text{ K}$: **FCC Aluminum (Al)** (primary metallic benchmark, using exact atomistic 2NN MEAM characteristic lengths from **Lazar, Agiasofitou & Böhlke 2022** and lattice-dynamics calibration from **Eringen 1983**) and **crystalline Silicon (Si)** (semiconductor benchmark).

The findings are unambiguous and must be stated without softening:

1. **Calibration of $(\ell, \gamma)$**:
   - The intrinsic nonlocal length scale $\ell$ is independently calibrated from atomistic potentials and lattice dispersion in FCC Al as $\bar{\ell}_1 = 1.20272\text{ \AA} = 0.1203\text{ nm}$ (**Lazar, Agiasofitou & Böhlke 2022**, Tables 3 & 6) or $\ell = e_0 a = 0.39 \times 0.40495\text{ nm} = 0.1579\text{ nm}$ (**Eringen 1983**).
   - **However, the two-phase local fraction $\gamma \in (0, 1)$ has NO independent experimental or unique long-wavelength phonon-dispersion calibration.** In bulk plane-wave dispersion $\omega(k) = c_0 k\left[1 - \frac{1}{2}(1-\gamma)k^2\ell^2 + O(k^4\ell^4)\right]$, only the single effective combination $\ell_{\text{eff}} = \sqrt{1-\gamma}\,\ell$ is observable at leading order $O(k^2\ell^2)$, and Separating $\gamma$ from $\ell$ requires fitting either the $O(k^4\ell^4)$ lattice dispersion curvature or structural boundary-layer stiffness (which, as **Nobili & Pramanik 2025b**, Section 2.1 explicitly note, lacks consistent experimental calibration across loading configurations).
2. **Scale Mismatch Between $\ell$ and the Thermoelastic Characteristic Length $\ell^*$**:
   - In FCC Al at $300\text{ K}$, the characteristic thermoelastic frequency and length are $\omega^* = \frac{\rho c_E c_0^2}{\kappa} = 4.226 \times 10^{11}\text{ rad/s}$ ($f^* = 67.26\text{ GHz}$) and $\ell^* = \frac{c_0}{\omega^*} = 15.19\text{ nm}$.
   - Thus the dimensionless nonlocal-to-thermal length ratio is:
     $$\chi_{\text{nl}} := \frac{\ell}{\ell^*} = \begin{cases} 7.917 \times 10^{-3} & (\text{Lazar et al. 2022: }\bar{\ell}_1 = 0.1203\text{ nm}), \\[4pt] 1.040 \times 10^{-2} & (\text{Eringen 1983: }\ell = 0.1579\text{ nm}), \end{cases} \qquad \chi_{\text{nl}}^2 \in [6.27 \times 10^{-5},\, 1.08 \times 10^{-4}].$$
3. **Incompatibility Between $O(1)$ Nonlocal Damping Differences and the Validity of Fourier's Law**:
   - In Round 1 (`paper/c1-hardening/physical_relevance.md`, Section 3.3), the $O(1)$ divergence between V1, V2, and Camp 1 attenuation was demonstrated by choosing $\chi_{\text{nl}} = 0.5$ (which would require an unphysically large nonlocal length $\ell \approx 7.6\text{ nm} \approx 19$ lattice constants in Al!) and dimensionless frequencies $\Omega = \omega/\omega^* \in [1, 10]$.
   - With the **calibrated** atomistic length $\ell \in [0.120, 0.158]\text{ nm}$, achieving $k\ell \sim 1$ requires acoustic frequencies $f = \frac{c_0}{2\pi\ell} \approx 6.5\text{–}8.5\text{ THz}$ ($\Omega = \omega/\omega^* \approx 96\text{–}127$, wavelength $\lambda \approx 0.76\text{–}0.99\text{ nm} \approx 2a$), which is at the Brillouin zone edge where continuum elasticity itself breaks down and where $\omega\tau_q \approx 60\text{–}80 \gg 1$ and $\lambda \ll \Lambda_{\text{th}} \approx 15\text{ nm}$, violating Fourier's heat conduction law by nearly two orders of magnitude.
   - Conversely, within the frequency regime where Fourier heat conduction is physically defensible ($\omega\tau_q \lesssim 0.1 \implies f \lesssim 10.6\text{ GHz}$, or even generously up to the Zener thermal relaxation peak $\Omega \le 1$, $f \le 67.3\text{ GHz}$, $\lambda \ge 96\text{ nm}$), we have $k\ell \le 1.03 \times 10^{-2}$ and $(k\ell)^2 \le 1.06 \times 10^{-4}$. Across this entire Fourier-defensible band, **the relative difference in thermoelastic attenuation between Variant V1, Variant V2, and Camp 1 is at most $6.0 \times 10^{-5}$ to $1.3 \times 10^{-4}$ ($0.006\%$ to $0.013\%$)**.

**Plain conclusion**: In real crystalline metals (Al) and semiconductors (Si) with atomistically calibrated nonlocal length scales $\ell \sim 0.12\text{–}0.21\text{ nm}$, **there is NO frequency/wavelength window where Fourier heat conduction is physically valid and the bulk thermoelastic damping difference between V1, V2, and Camp 1 is experimentally measurable.** The surviving value of Candidate C1 is **foundational and mathematical** (correcting the Second-Law / Maxwell symmetry contradiction of Camp 1, explaining the $\gamma \to 0$ operator cancellation of Camp 2, and establishing well-posed Constitutive Boundary Conditions on bounded domains), not a claim of a large measurable bulk damping split in Fourier-regime crystals.

---

## 2. Independent Calibration of $(\ell, \gamma)$ from the Literature

### 2.1 Calibration of the Nonlocal Length Scale $\ell$ for FCC Aluminum and Silicon
1. **Lazar, Agiasofitou & Böhlke (2022)** (*"Mathematical modeling of the elastic properties of cubic crystals at small scales based on the Toupin–Mindlin anisotropic first strain gradient elasticity"*, *Continuum Mech. Thermodyn.* **34**, 107–136, open access, Tables 3 & 6 verified in full):
   - Using the Second Nearest-Neighbor Modified Embedded Atom Method (**2NN MEAM**) interatomic potential for FCC Aluminum ($a = 4.04950\text{ \AA}$), Lazar et al. compute the exact sixth-order strain-gradient / nonlocal constitutive tensor and extract the characteristic length scales at $T_0 = 300\text{ K}$:
     - Cubic longitudinal characteristic length (Table 3):
       $$\ell_1(\text{Al}) = 1.19303\text{ \AA} = 0.119303\text{ nm}, \qquad \frac{\ell_1}{a} = 0.2946.$$
     - Voigt-averaged isotropic longitudinal characteristic length (Table 6):
       $$\bar{\ell}_1(\text{Al}) = 1.20272\text{ \AA} = 0.120272\text{ nm}, \qquad \frac{\bar{\ell}_1}{a} = 0.2970.$$
2. **Eringen (1972, 1983)** (*J. Appl. Phys.* **54**, 4703–4710):
   - Matching the 1D Helmholtz differential dispersion relation $\omega^2(k) = \frac{c_0^2 k^2}{1 + \ell^2 k^2}$ to the Born–von Kármán lattice dispersion $\omega^2(k) = \frac{4c_0^2}{a^2}\sin^2(ka/2)$ at the Brillouin zone boundary $k = \pi/a$ gives $e_0 = \frac{\ell}{a} = \frac{\sqrt{\pi^2 - 4}}{2\pi} \approx 0.3855 \approx 0.39$, yielding:
     $$\ell_{\text{Eringen}}(\text{Al}) = 0.39 \times 0.404950\text{ nm} = 0.157931\text{ nm}, \qquad \ell_{\text{Eringen}}(\text{Si}) = 0.39 \times 0.5431\text{ nm} = 0.211809\text{ nm}.$$

### 2.2 Non-Identifiability of $\gamma$ from Long-Wavelength Bulk Dispersion
For the two-phase operator $\mathcal{L}_{\gamma,\ell}$, the Fourier symbol is
$$\hat{\mathcal{L}}_{\gamma,\ell}(k) = \frac{1 + \gamma k^2\ell^2}{1 + k^2\ell^2} = 1 - (1-\gamma)k^2\ell^2 + (1-\gamma)k^4\ell^4 - O(k^6\ell^6).$$
Comparing the $O(k^2)$ dispersion shift against the exact lattice / Toupin–Mindlin gradient-elasticity dispersion $\omega^2(k) = c_0^2 k^2\left(1 - \bar{\ell}_1^2 k^2 + O(k^4)\right)$ fixes only the product:
$$(1 - \gamma)\ell^2 = \bar{\ell}_1^2 \implies \ell_{\text{eff}} := \sqrt{1 - \gamma}\,\ell = \bar{\ell}_1 = 0.120272\text{ nm}.$$
Thus:
- At leading order $O(k^2\ell^2)$, $\gamma$ and $\ell$ are **degenerate**: any pair $(\gamma, \ell)$ with $\sqrt{1-\gamma}\,\ell = \bar{\ell}_1$ produces the exact same $O(k^2)$ dispersion shift!
- Moreover, because $(1 - \gamma)\ell^2 = \bar{\ell}_1^2$ is fixed by the atomistic second moment of the interatomic force constants, increasing $\ell$ by taking $\gamma \to 1^-$ leaves the leading-order nonlocal thermoelastic effect $(1 - \gamma)k^2\ell^2 = k^2\bar{\ell}_1^2$ **completely unchanged**!
- As **Nobili & Pramanik (2025b, Section 2.1)** explicitly point out, the two-phase volume fraction $\gamma = \xi_1 \in (0, 1)$ has no direct experimental calibration and acts mathematically as a singular-perturbation regularization parameter ensuring positive-definiteness of $\mathcal{L}_{\gamma,\ell}$ on $L^2(\Omega)$ and solvability of the boundary-value problem.

---

## 3. Validity Bounds of Fourier's Heat Conduction Law vs. Nonlocal Scale

For Fourier's heat conduction law $q = -\kappa\partial_x\theta$ to be physically defensible in a continuum thermoelastic wave model, two microscopic transport constraints must hold:
1. **Temporal (Cattaneo / thermal relaxation) constraint**: The wave angular frequency $\omega$ must satisfy $\omega \tau_q \lesssim 0.1$, where $\tau_q$ is the microscopic thermal relaxation time ($\tau_q \approx 1.5\text{ ps}$ for electron–phonon thermalization in Al at $300\text{ K}$; $\tau_q \approx 20\text{ ps}$ for phonon–phonon Umklapp relaxation in Si at $300\text{ K}$).
2. **Spatial (Knudsen / ballistic mean-free-path) constraint**: The acoustic wavelength $\lambda = 2\pi/k$ must exceed the thermal carrier mean free path $\Lambda_{\text{th}}$ by roughly an order of magnitude ($\lambda \gtrsim 10\Lambda_{\text{th}}$, i.e., $k\Lambda_{\text{th}} \lesssim 2\pi/10 \approx 0.628$, where $\Lambda_{\text{th}} \approx 15\text{ nm}$ in Al and $\Lambda_{\text{th}} \approx 100\text{ nm}$ in Si at $300\text{ K}$).

### Characteristic Scales for FCC Aluminum and Silicon at $T_0 = 300\text{ K}$
From [`calibration_audit.py`](./calibration_audit.py):

| Parameter | Symbol | FCC Aluminum (Al, $300\text{ K}$) | Crystalline Silicon (Si, $300\text{ K}$) |
| :--- | :---: | :---: | :---: |
| Density | $\rho$ | $2700\text{ kg/m}^3$ | $2329\text{ kg/m}^3$ |
| Longitudinal wave speed | $c_0$ | $6420\text{ m/s}$ | $8433\text{ m/s}$ |
| Specific heat | $c_E$ | $900\text{ J/(kg}\cdot\text{K)}$ | $712\text{ J/(kg}\cdot\text{K)}$ |
| Thermal conductivity | $\kappa$ | $237\text{ W/(m}\cdot\text{K)}$ | $148\text{ W/(m}\cdot\text{K)}$ |
| Thermoelastic coupling | $\epsilon = \frac{\beta^2 T_0}{\rho c_E E}$ | $0.0356$ | $0.0011$ |
| Characteristic thermal frequency | $\omega^* = \frac{\rho c_E c_0^2}{\kappa}$ | $4.226 \times 10^{11}\text{ rad/s}$ ($f^* = 67.26\text{ GHz}$) | $7.968 \times 10^{11}\text{ rad/s}$ ($f^* = 126.8\text{ GHz}$) |
| Characteristic thermal length | $\ell^* = \frac{c_0}{\omega^*}$ | **$15.19\text{ nm}$** | **$10.58\text{ nm}$** |
| Calibrated nonlocal length | $\ell$ | **$0.1203\text{ nm}$** (Lazar 2022) / **$0.1579\text{ nm}$** (Eringen 1983) | **$0.2118\text{ nm}$** (Eringen 1983) |
| **Nonlocal-to-thermal length ratio** | $\chi_{\text{nl}} = \ell / \ell^*$ | **$7.92 \times 10^{-3}$** (Lazar) / **$1.04 \times 10^{-2}$** (Eringen) | **$2.00 \times 10^{-2}$** |
| **Squared length ratio** | $\chi_{\text{nl}}^2 = (\ell / \ell^*)^2$ | **$6.27 \times 10^{-5}$** (Lazar) / **$1.08 \times 10^{-4}$** (Eringen) | **$4.01 \times 10^{-4}$** |
| Thermal relaxation time | $\tau_q$ | $\sim 1.5\text{ ps}$ | $\sim 20\text{ ps}$ |
| Thermal mean free path | $\Lambda_{\text{th}}$ | $\sim 15\text{ nm}$ | $\sim 100\text{ nm}$ |
| Strict Fourier ceiling ($\omega\tau_q \le 0.1$) | $\Omega_{\max}^{\text{Fourier}} = \frac{0.1}{\omega^*\tau_q}$ | $\Omega \le 0.158$ ($f \le 10.6\text{ GHz}$) | $\Omega \le 0.0063$ ($f \le 0.80\text{ GHz}$) |
| Value of $(k\ell)^2$ at strict Fourier ceiling | $(k\ell)^2\big|_{\Omega_{\max}^{\text{Fourier}}}$ | **$1.56 \times 10^{-6}$** (Lazar) / **$2.69 \times 10^{-6}$** (Eringen) | **$1.58 \times 10^{-8}$** |

---

## 4. Quantitative Damping Comparison Across Frequency Regimes in FCC Aluminum

The table below (generated by [`calibration_audit.py`](./calibration_audit.py) for FCC Aluminum at $300\text{ K}$ with $\gamma = 0.5$) reports the acoustic frequency $f$, acoustic wavelength $\lambda$, dimensionless nonlocal wavenumber $k\ell$, and the exact relative attenuation differences $|\alpha^{\text{V1}} - \alpha^{\text{V2}}|/\alpha^{\text{V1}}$ and $|\alpha^{\text{Camp 1}} - \alpha^{\text{V1}}|/\alpha^{\text{V1}}$ from sub-GHz ultrasonic waves up to the Brillouin zone boundary:

### Case A: Lazar, Agiasofitou & Böhlke (2022) Atomistic Calibration ($\bar{\ell}_1 = 0.1203\text{ nm}$, $\chi_{\text{nl}} = 7.917 \times 10^{-3}$)

| $\Omega = \omega/\omega^*$ | Frequency $f$ (GHz) | Wavelength $\lambda$ (nm) | $k\ell$ | $\frac{|\alpha^{\text{V1}} - \alpha^{\text{V2}}|}{\alpha^{\text{V1}}}$ | $\frac{|\alpha^{\text{Camp 1}} - \alpha^{\text{V1}}|}{\alpha^{\text{V1}}}$ | Physical Regime Assessment |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| $0.001$ | $0.067\text{ GHz}$ | $97,137\text{ nm}$ | $7.78 \times 10^{-6}$ | $6.50 \times 10^{-11}$ | $1.25 \times 10^{-10}$ | **Fourier valid** ($\omega\tau_q = 6.3\times 10^{-4}$); nonlocal diff $\sim 10^{-10}$ (unmeasurable) |
| $0.010$ | $0.673\text{ GHz}$ | $9,714\text{ nm}$ | $7.78 \times 10^{-5}$ | $5.32 \times 10^{-9}$ | $1.02 \times 10^{-8}$ | **Fourier valid** ($\omega\tau_q = 6.3\times 10^{-3}$); nonlocal diff $\sim 10^{-8}$ (unmeasurable) |
| $0.100$ | $6.726\text{ GHz}$ | $971.2\text{ nm}$ | $7.78 \times 10^{-4}$ | **$5.34 \times 10^{-7}$** | **$1.02 \times 10^{-6}$** | **Fourier valid** ($\omega\tau_q = 0.063 \le 0.1$); nonlocal diff $\le 0.0001\%$ |
| $0.500$ | $33.63\text{ GHz}$ | $193.7\text{ nm}$ | $3.90 \times 10^{-3}$ | **$1.40 \times 10^{-5}$** | **$2.35 \times 10^{-5}$** | **Pre-ballistic transition** ($\omega\tau_q = 0.32$); nonlocal diff $\approx 0.002\%$ |
| $1.000$ | $67.26\text{ GHz}$ | $96.32\text{ nm}$ | $7.85 \times 10^{-3}$ | **$5.98 \times 10^{-5}$** | **$7.80 \times 10^{-5}$** | **Zener peak** ($\omega\tau_q = 0.63$, $\lambda \approx 6.4\Lambda_{\text{th}}$); nonlocal diff $\approx 0.008\%$ |
| $10.00$ | $672.6\text{ GHz}$ | $9.53\text{ nm}$ | $7.93 \times 10^{-2}$ | $6.28 \times 10^{-3}$ ($0.63\%$) | $4.79 \times 10^{-3}$ ($0.48\%$) | **Fourier invalid** ($\omega\tau_q = 6.3 \gg 1$, $\lambda < \Lambda_{\text{th}}$: ballistic heat regime) |
| $100.0$ | $6,726\text{ GHz}$ | $0.84\text{ nm}$ | $8.98 \times 10^{-1}$ | $6.58 \times 10^{-1}$ ($65.8\%$) | $1.01 \times 10^{0}$ ($101\%$) | **Continuum & Fourier invalid** ($\lambda \approx 2a$: Brillouin zone edge, $\omega\tau_q = 63$) |

### Case B: Eringen (1983) Zone-Edge Calibration ($\ell = 0.1579\text{ nm}$, $\chi_{\text{nl}} = 1.040 \times 10^{-2}$)

| $\Omega = \omega/\omega^*$ | Frequency $f$ (GHz) | Wavelength $\lambda$ (nm) | $k\ell$ | $\frac{|\alpha^{\text{V1}} - \alpha^{\text{V2}}|}{\alpha^{\text{V1}}}$ | $\frac{|\alpha^{\text{Camp 1}} - \alpha^{\text{V1}}|}{\alpha^{\text{V1}}}$ | Physical Regime Assessment |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| $0.100$ | $6.726\text{ GHz}$ | $971.2\text{ nm}$ | $1.02 \times 10^{-3}$ | **$9.20 \times 10^{-7}$** | **$1.76 \times 10^{-6}$** | **Fourier valid** ($\omega\tau_q = 0.063$); nonlocal diff $< 0.0002\%$ |
| $1.000$ | $67.26\text{ GHz}$ | $96.32\text{ nm}$ | $1.03 \times 10^{-2}$ | **$1.03 \times 10^{-4}$** | **$1.35 \times 10^{-4}$** | **Zener peak** ($\omega\tau_q = 0.63$); nonlocal diff $\approx 0.01\%$ |
| $10.00$ | $672.6\text{ GHz}$ | $9.52\text{ nm}$ | $1.04 \times 10^{-1}$ | $1.08 \times 10^{-2}$ ($1.08\%$) | $8.29 \times 10^{-3}$ ($0.83\%$) | **Fourier invalid** ($\omega\tau_q = 6.3 \gg 1$, $\lambda < \Lambda_{\text{th}}$) |
| $100.0$ | $6,726\text{ GHz}$ | $0.80\text{ nm}$ | $1.25 \times 10^{0}$ | $1.07 \times 10^{0}$ ($107\%$) | $5.66 \times 10^{2}$ | **Continuum & Fourier invalid** ($\lambda \approx 2a$: Brillouin zone edge) |

---

## 5. Why $O(1)$ Nonlocal Damping Splits Require Either Non-Fourier Regimes or Micro-Architectured Metamaterials

From the asymptotic expansion of Theorem 4 for $k\ell \ll 1$:
$$\frac{\alpha^{\text{V1}}(\omega) - \alpha^{\text{V2}}(\omega)}{\alpha^{\text{loc}}(\omega)} = O\!\left((1-\gamma)k^2\ell^2\right) = O\!\left((1-\gamma)\chi_{\text{nl}}^2 \Omega^2\right),$$
$$\frac{\alpha^{\text{Camp 1}}(\omega) - \alpha^{\text{V1}}(\omega)}{\alpha^{\text{loc}}(\omega)} = O\!\left((1+\gamma)k^2\ell^2\right) = O\!\left((1+\gamma)\chi_{\text{nl}}^2 \Omega^2\right).$$
Therefore, for the relative damping discrepancy between V1, V2, and Camp 1 to reach even $1\%$ ($10^{-2}$) inside the Fourier-defensible regime ($\Omega \lesssim 0.2\text{–}1$), one would need $\chi_{\text{nl}} = \ell/\ell^* \gtrsim 0.1\text{–}0.5$.
- In a **monolithic crystal** (where $\ell \sim 0.12\text{–}0.21\text{ nm}$ is fixed by the lattice spacing $a$ and $\ell^* \sim 10\text{–}15\text{ nm}$ is fixed by thermal diffusivity), $\chi_{\text{nl}} \sim 10^{-2}$ is a material constant, so $(k\ell)^2 \lesssim 10^{-4}$ throughout the Fourier regime.
- Consequently, any manuscript on Candidate C1 **must not claim** that V1 vs. V2 produces a large measurable bulk ultrasonic damping split in Fourier-regime crystalline metals or semiconductors. Instead, the dispersion and damping analysis (Theorems 3–4) must be presented strictly as:
  1. **A mathematical structural and asymptotic analysis** of the PDE systems (proving the quartic $N=4$ vs. cubic $N=3$ spatial mode count, the $\gamma \to 0$ singular perturbation mechanism behind Camp 2's operator cancellation, and the high-$k$ ill-behaved attenuation scaling $\alpha_1 \propto k^{-2}$ of the thermodynamically inconsistent Camp 1 PDE vs. V1/V2), and
  2. **An explicit order-of-magnitude physical audit** demonstrating that for atomistically calibrated crystals ($\ell \approx 0.12\text{ nm}$ in Al) inside the Fourier validity window, nonlocal corrections to bulk thermoelastic damping are $O((k\ell)^2) \lesssim 10^{-4}$.
