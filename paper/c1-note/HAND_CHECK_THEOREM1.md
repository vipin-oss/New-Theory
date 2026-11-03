# One-Page Hand-Check Sheet for Theorem 1

**Claim of Theorem 1**: For any $\ell > 0$ and $\gamma \in [0, 1)$, the constitutive pairing that applies the nonlocal operator to the thermal stress,
$$(1 - \ell^2\partial_x^2)\sigma = (1 - \gamma\ell^2\partial_x^2)(E\varepsilon - \beta\theta) \qquad (\text{reducing at }\gamma = 0\text{ to Class I: }(1 - \ell^2\partial_x^2)\sigma = E\varepsilon - \beta\theta), \tag{1}$$
while retaining the **local** constant-strain entropy density
$$\rho\eta^{\text{loc}} = \beta\varepsilon + \frac{\rho c_E}{T_0}\theta, \tag{2}$$
admits **(a)** no twice-differentiable Helmholtz free energy $\Psi[\varepsilon, \theta]$, **(b)** no stress-gradient Gibbs potential $G[\sigma, \theta]$ (where Gibbs reciprocity requires adding $+\frac{\beta\ell^2}{E}\partial_x^2\sigma$ to $\rho\eta^{\text{loc}}$), and **(c)** yields negative internal dissipation $\Delta\mathcal{D}_{\text{cycle}} < 0$ on closed harmonic cycles.

---

### Check 1: Helmholtz $(\varepsilon, \theta)$ Maxwell-Symmetry Defect (3 lines)
Take a single spatial Fourier mode $\varepsilon(x,t) = \hat{\varepsilon}(t)\cos(kx)$, $\theta(x,t) = \hat{\theta}(t)\cos(kx)$ ($k = n\pi/L > 0$) on $[0, L]$, where $-\partial_x^2[\cos(kx)] = k^2\cos(kx)$. Equations (1)–(2) become algebraic in the modal amplitudes:
$$\hat{\sigma}(\hat{\varepsilon}, \hat{\theta}) = \frac{1 + \gamma k^2\ell^2}{1 + k^2\ell^2}\left(E\hat{\varepsilon} - \beta\hat{\theta}\right), \qquad \rho\hat{\eta}^{\text{loc}}(\hat{\varepsilon}, \hat{\theta}) = \beta\hat{\varepsilon} + \frac{\rho c_E}{T_0}\hat{\theta}. \tag{3}$$
If a twice-differentiable modal Helmholtz free energy $\hat{\psi}(\hat{\varepsilon}, \hat{\theta})$ existed with $\hat{\sigma} = \partial\hat{\psi}/\partial\hat{\varepsilon}$ and $\rho\hat{\eta}^{\text{loc}} = -\partial\hat{\psi}/\partial\hat{\theta}$, Schwarz's theorem ($\partial^2\hat{\psi}/\partial\hat{\theta}\partial\hat{\varepsilon} = \partial^2\hat{\psi}/\partial\hat{\varepsilon}\partial\hat{\theta}$) would require $\frac{\partial\hat{\sigma}}{\partial\hat{\theta}} + \frac{\partial(\rho\hat{\eta}^{\text{loc}})}{\partial\hat{\varepsilon}} = 0$. Differentiating (3) by hand gives:
$$\frac{\partial\hat{\sigma}}{\partial\hat{\theta}} = -\beta\,\frac{1 + \gamma k^2\ell^2}{1 + k^2\ell^2}, \qquad \frac{\partial(\rho\hat{\eta}^{\text{loc}})}{\partial\hat{\varepsilon}} = +\beta \implies \Delta_{\text{Maxwell}}^{\text{Helm}}(k) = \frac{\partial\hat{\sigma}}{\partial\hat{\theta}} + \frac{\partial(\rho\hat{\eta}^{\text{loc}})}{\partial\hat{\varepsilon}} = \frac{\beta(1 - \gamma)k^2\ell^2}{1 + k^2\ell^2} \neq 0. \tag{4}$$
*(Check: For Variant V1, $\rho\hat{\eta}^{\text{V1}} = \beta\frac{1+\gamma k^2\ell^2}{1+k^2\ell^2}\hat{\varepsilon} + \frac{\rho c_E}{T_0}\hat{\theta} \implies \Delta_{\text{Maxwell}}^{\text{V1}} = 0$. For Variant V2, $\hat{\sigma}^{\text{V2}} = E\frac{1+\gamma k^2\ell^2}{1+k^2\ell^2}\hat{\varepsilon} - \beta\hat{\theta}$ and $\rho\hat{\eta}^{\text{V2}} = \rho\hat{\eta}^{\text{loc}} \implies \Delta_{\text{Maxwell}}^{\text{V2}} = 0$.)*

---

### Check 2: Complementary Gibbs $(\sigma, \theta)$ Stress-Gradient Check at $\gamma = 0$ (4 lines)
Suppose $(1 - \ell^2\partial_x^2)\sigma = E\varepsilon - \beta\theta$ is generated from the quadratic stress-gradient Gibbs functional $G[\sigma, \theta] = \int_0^L g(\sigma, \partial_x\sigma, \theta)\,dx$ with
$$g(\sigma, \partial_x\sigma, \theta) = \frac{1}{2E}\sigma^2 + \frac{\ell^2}{2E}(\partial_x\sigma)^2 + \frac{\beta}{E}\sigma\theta + \frac{\rho c_\sigma}{2T_0}\theta^2, \qquad \frac{\rho c_\sigma}{T_0} := \frac{\rho c_E}{T_0} + \frac{\beta^2}{E}. \tag{5}$$
1. **Strain state law** ($\partial_x\sigma = 0$ at $x = 0, L$):
   $$\varepsilon = \frac{\delta G}{\delta\sigma} = \frac{\partial g}{\partial\sigma} - \partial_x\!\left(\frac{\partial g}{\partial(\partial_x\sigma)}\right) = \frac{1}{E}(\sigma - \ell^2\partial_x^2\sigma) + \frac{\beta}{E}\theta \iff (1 - \ell^2\partial_x^2)\sigma = E\varepsilon - \beta\theta \quad\checkmark \tag{6}$$
2. **Mandatory Gibbs entropy law** (substitute $\sigma = E\varepsilon - \beta\theta + \ell^2\partial_x^2\sigma$ from (6) into $\partial g/\partial\theta$):
   $$\rho\eta^{\text{Gibbs}} = \frac{\partial g}{\partial\theta} = \frac{\beta}{E}\sigma + \frac{\rho c_\sigma}{T_0}\theta = \frac{\beta}{E}\left(E\varepsilon - \beta\theta + \ell^2\partial_x^2\sigma\right) + \left(\frac{\rho c_E}{T_0} + \frac{\beta^2}{E}\right)\theta = \underbrace{\beta\varepsilon + \frac{\rho c_E}{T_0}\theta}_{\rho\eta^{\text{loc}}} + \frac{\beta\ell^2}{E}\partial_x^2\sigma. \tag{7}$$
The $-\frac{\beta^2}{E}\theta$ and $+\frac{\beta^2}{E}\theta$ terms cancel identically, leaving the non-zero stress-Laplacian discrepancy $\rho\eta^{\text{Gibbs}} - \rho\eta^{\text{loc}} = \frac{\beta\ell^2}{E}\partial_x^2\sigma \neq 0$.

---

### Check 3: Closed Harmonic Cycle Yielding Negative Internal Dissipation $\Delta\mathcal{D}_{\text{cycle}} < 0$ (4 lines)
Prescribe the $2\pi/\omega$-periodic history $\varepsilon(x,t) = \varepsilon_0\cos(kx)\cos(\omega t)$, $\theta(x,t) = \theta_0\cos(kx)\sin(\omega t)$ ($\varepsilon_0, \theta_0, \omega > 0$) on $[0, L]$. Over one period $\mathcal{T} = 2\pi/\omega$, any state function $\Psi$ has $\oint \dot{\Psi}\,dt = 0$. Using $\int_0^L \cos^2(kx)\,dx = \frac{L}{2}$, $\int_0^{\mathcal{T}}\cos(\omega t)\sin(\omega t)\,dt = 0$, and $\int_0^{\mathcal{T}}\sin^2(\omega t)\,dt = \int_0^{\mathcal{T}}\cos^2(\omega t)\,dt = \frac{\pi}{\omega}$:
$$\oint\int_0^L \sigma\dot{\varepsilon}\,dx\,dt = \frac{L}{2}\int_0^{\mathcal{T}} \frac{1+\gamma k^2\ell^2}{1+k^2\ell^2}\left(E\varepsilon_0\cos\omega t - \beta\theta_0\sin\omega t\right)(-\omega\varepsilon_0\sin\omega t)\,dt = +\frac{\pi L}{2}\beta\varepsilon_0\theta_0\,\frac{1+\gamma k^2\ell^2}{1+k^2\ell^2}, \tag{8}$$
$$-\oint\int_0^L \rho\eta^{\text{loc}}\dot{\theta}\,dx\,dt = -\frac{L}{2}\int_0^{\mathcal{T}} \left(\beta\varepsilon_0\cos\omega t + \frac{\rho c_E}{T_0}\theta_0\sin\omega t\right)(\omega\theta_0\cos\omega t)\,dt = -\frac{\pi L}{2}\beta\varepsilon_0\theta_0. \tag{9}$$
Adding (8), (9), and the Fourier conduction dissipation $\oint\int_0^L \frac{\kappa}{T_0}(\partial_x\theta)^2\,dx\,dt = \frac{\pi L}{2\omega}\frac{\kappa k^2}{T_0}\theta_0^2$ gives:
$$\Delta\mathcal{D}_{\text{cycle}} = \frac{\pi L\theta_0}{2\omega}\left[-\frac{\beta(1-\gamma)k^2\ell^2}{1 + k^2\ell^2}\,\omega\varepsilon_0 + \frac{\kappa k^2}{T_0}\,\theta_0\right] < 0 \quad \text{whenever}\quad \varepsilon_0 > \frac{\kappa(1 + k^2\ell^2)}{\beta T_0(1-\gamma)\omega\ell^2}\,\theta_0. \qquad \blacksquare \tag{10}$$
