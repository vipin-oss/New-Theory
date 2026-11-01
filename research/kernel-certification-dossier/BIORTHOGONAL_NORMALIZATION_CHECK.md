# Biorthogonal normalization and C∞ right inverse

**Status: VERIFIED UNDER EXPLICIT ASSUMPTIONS.** This is a same-agent reconstruction, not independent certification. The external theorem is used as an input; its proof is not independently certified here.

## Input theorem — exact source location and applicable specialization

Cannarsa, Martinez and Vancostenoble, *Precise estimates for biorthogonal families under asymptotic gap conditions*, [arXiv:1706.02435v1, Theorem 2.1, equations (2.1)–(2.6)](https://arxiv.org/html/1706.02435#S2.ThmTheorem1). The source assumes \(\lambda_n\ge0\), a global lower square-root gap \(g>0\), and a larger lower gap \(g_*>g\) from some index \(N_*\). It asserts biorthogonality to \(e^{\lambda_nt}\) on \((0,\ell)\) and
\[\|\sigma_n^+\|_2^2\le e^{-2\lambda_n\ell}\exp\!\left(\frac{C}{\ell g_*^2}+\frac{C\sqrt{\lambda_n}}{g_*}\right)B^*(\ell,g,g_*,N_*,n),\]
with \(B^*\) explicitly defined in its equation (2.6). For the present strictly positive \(b_n\) with global gap \(g_0>0\), take \(g=g_0/2\), \(g_*=g_0\), \(N_*=1\). These satisfy both source hypotheses; in the source notation \(M_*=(1-g/g_*)(N_*-1)=0\). Equation (2.6) then simplifies to a fixed \(\ell,g,g_*\)-dependent factor times \(\exp(C_u b_1/(g\sqrt{b_n}))\), bounded uniformly because \(b_n\ge b_1>0\). Thus the exact consequence used is
\[\int_0^\ell \sigma_n^+(u)e^{b_mu}\,du=\delta_{nm},\qquad
\|\sigma_n^+\|_2\le C_0\exp(-\ell b_n+C_1\sqrt{b_n}).\tag{1}\]
The source statements are for complex L² as well; replacing a family by its real part preserves the real moments and does not increase its norm. No upper gap or asymptotic ratio is required for this specialization. The physical square-root gap is independently checked in the modal file.

## Direct computation of every factor

Choose \(0<a<a+\ell+\epsilon<T\) with \([a,a+\ell+\epsilon]\subset I\); choose \(\eta>0\) so \(a+\epsilon<T-\eta\), possible because \(\ell>0\). Extend \(\sigma_n^+\) by zero and put
\[p_n(u)=e^{b_n\ell}\sigma_n^+(\ell-u),\quad 0<u<\ell.\]
Substituting \(v=\ell-u\) gives
\[\int_{\mathbb R}e^{-b_m u}p_n(u)du
=e^{(b_n-b_m)\ell}\int_0^\ell e^{b_m v}\sigma_n^+(v)dv=\delta_{nm},\]
and \(\|p_n\|_2\le C_0e^{C_1\sqrt{b_n}}\). Now shift to \(p_n(u-a)\). Its \(m\)-th moment is \(e^{-ab_m}\delta_{mn}\).

Take a fixed real nonnegative nonzero \(\rho\in C_c^\infty(0,\epsilon)\), and write \(\rho_m=\int e^{-b_m u}\rho(u)du>0\). Multiplicativity of Laplace integrals under convolution, justified by compact support, yields
\[\int e^{-b_mt}[p_n(\cdot-a)*\rho](t)dt=e^{-ab_m}\delta_{mn}\rho_m.\]
Therefore
\[\psi_n(t)=\frac{e^{ab_n}}{t\rho_n}[p_n(\cdot-a)*\rho](t)\]
is supported in the same compact subset of I for every n, and
\[\int_I t e^{-b_mt}\psi_n(t)dt=\frac{e^{a(b_n-b_m)}\rho_m}{\rho_n}\delta_{mn}=\delta_{mn}.\tag{2}\]
The factor is exactly 1 when \(m=n\); no off-diagonal normalization is needed. Division by t is smooth and uniformly bounded on I because \(\inf I>0\).

## All derivative norms, not just L²

For every j, Young/Cauchy–Schwarz gives \(\|(p_n(\cdot-a)*\rho)^{(j)}\|_\infty\le\|p_n\|_2\|\rho^{(j)}\|_2\). Leibniz' rule for 1/t introduces only constants depending on j and a. As \(\rho_n\ge e^{-\epsilon b_n}\int\rho\),
\[\|\psi_n\|_{C^j(\mathbb R)}\le C_j e^{(a+\epsilon)b_n+C_1\sqrt{b_n}}.\tag{3}\]
For \(Y=\ell^2(e^{2(T-\eta)b_n})\), each derivative series has sum bounded by
\[C_j\|y\|_Y\left(\sum_ne^{-2[T-\eta-a-\epsilon]b_n+2C_1\sqrt{b_n}}\right)^{1/2}<\infty.\]
The sum converges since \(b_n\asymp n^2\) and the margin is strictly positive. Uniform convergence of each derivative and the common compact support imply \(Sy=\sum y_n\psi_n\in C_c^\infty(I)\), and convergence occurs in each C^j norm. Boundedness \(S:Y\to L^2(I,t\,dt)\) follows from the j=0 bound. Integral (2) and continuity justify \(ESy=y\) for every coordinate. E need not map X to Y, and S is not claimed to invert E on ordinary ℓ².
