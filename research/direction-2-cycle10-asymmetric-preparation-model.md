# Cycle 10: asymmetric thermal preparation, exact model

Use \(s\in[-T_p,0]\), \(I=(0,L)\), the frozen equations and initial relaxed state \(u=z=0,\theta=\theta_*>0\). For this analysis take \(g_p,\tau_0,\tau_L\in C_c^\infty((-T_p,0))\); they are finite-energy and vanish in a neighborhood of each time endpoint. The baths \(\theta_*+\tau_j\) must be positive. This is an explicit subclass of the user's smooth endpoint-restored controls, **not** the entire class: the consequences of this extra switch-off assumption are marked below. Fix a positive gap \(\varepsilon<T_p\) when using \(L^2\) control completions. Set \(\tau_a=(\tau_0-\tau_L)/2\), \(\tau_s=(\tau_0+\tau_L)/2\). Exactly at \(s=0\), require the **whole** \(y=\theta-\theta_*\) to vanish, not just both endpoint controls; this is an additional terminal constraint. Require \(g_p(0)=0\). No body forces, volumetric heat controls, or prescribed interior temperatures are introduced. The original nonzero post-zero sinusoidal experiment and delayed boundary observation are unchanged.

The unchanged coupled field equations and mechanical endpoints are
\[\sigma_x=0,\quad \sigma=(a+k)u_x-b(\theta-\theta_*)-kz,\quad z_s=\lambda(u_x-z),\quad c\theta_s=\kappa\theta_{xx}-b\theta(u_x)_s+k\lambda(u_x-z)^2,\]
\[u(0,s)=0,\qquad u(L,s)=g_p(s),\qquad \theta(0,s)=\theta_*+\tau_0(s),\quad \theta(L,s)=\theta_*+\tau_L(s).\]
Select positive strong solutions with lifted temperature \(Y\in H^1_sL^2_x\cap L^2_s(H^2_x\cap H^1_{0,x})\cap C_sH^1_{0,x}\), and \(p\in H^1_sH^2_x\), \(v\in H^1_s\), consistent with the zero-start Volterra formula. Existence for nonzero controls is not asserted.

Equilibrium integration, valid also for inhomogeneous baths, yields with \(m=g_p/L\), \(v=\bar z\), \(p=Qz\), \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(d=b^2/D\), \(\mu=\lambda\alpha\), \(\gamma=\lambda\beta\),
\[\sigma=Dm-b\bar y-kv,\qquad u_x=m+rp+\beta Qy,\qquad w=m-v-\alpha p+\beta Qy,\]
\[v_s=\lambda(m-v),\quad p_s=-\mu p+\gamma Qy,\quad (cI+d(\theta_*+y)Q)y_s=\kappa y_{xx}-b(\theta_*+y)(m'+rp_s)+k\lambda w^2.\tag{1}\]
Here \(y(0,s)=\tau_0(s),y(L,s)=\tau_L(s)\), zero initial \((v,p,y)\); \(u(x,s)=\int_0^x[m+rp+\beta Qy]d\xi\). The nonlocal mass has not been replaced. Terminal memory is
\[v(0)=\lambda\int_{-T_p}^{0}e^{\lambda s}m(s)ds,\quad p(0)=\gamma\int_{-T_p}^{0}e^{\mu s}Qy(s)ds,\quad z(0)=v(0)+p(0).\]
Thus the antisymmetric baths enter through the actual solution of (1), not through an independently chosen interior state. At \(s=0\), if \(y=0,m=0\), \(u_x=rp\), \(\sigma=-kv\); a pure odd terminal memory requires \(v=0\) and no even component of \(p\). The mechanical equilibrium is already built into the formula; terminal displacement endpoints do not imply the interior displacement vanishes.

For the nonlinear controlled problem use the affine lifting \(y=Y+\ell_s\tau_s+\ell_a\tau_a\), \(\ell_s=1\), \(\ell_a=1-2x/L\), with \(Y\) having homogeneous Dirichlet traces. Controls small in a stated smooth norm make boundary temperatures positive; interior positivity, existence and differentiability require the lifted quasilinear fixed-point estimates, not the boundary positivity alone. Zero controls give the trivial admissible trajectory. No positive nonzero terminal-compatible nonlinear trajectory is claimed.
