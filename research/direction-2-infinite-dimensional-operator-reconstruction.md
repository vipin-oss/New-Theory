# Direction 2: reconstruction of the infinite-dimensional observation operator

**Status: CONDITIONALLY PROVED**, subject to the inherited actual-base and strong-forward estimates, not independently human-certified. The branch was already two commits ahead of the requested `cb904502bea00fb10e280e4c117575023b29bff4`; no history was discarded.

## Domains and forward map

The displayed equations in the request are the **odd subsystem**: the correct domain is \(H_o=\{h\in L^2(0,L):h(L-x)=-h(x)\}\), not unrestricted \(L^2(0,L)\). Its adjoint is projected by \(\Pi_o\); density in full \(L^2\) is impossible for this projected range. If all of \(L^2\) is intended, the full mean/nonlocal subsystem and full data must be analyzed separately. The admissible nonlinear odd prior \(H^2\cap H_o\) is smaller than this bounded linear extension. We keep the actual nonzero sinusoidal load, \(\delta=T/100\), full interval \((0,T)\), and coefficients from the active base, not arbitrary independent coefficients.

Under the inherited bounds \(0<m_0\le M\le m_1\), \(B\in L^2(Q_T)\), \(S\in L^\infty(Q_T)\), and the verified-regime forward estimate, the unique strong pair has
\[Y\in\mathcal E=H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x}),\quad P\in H^1_tL^2_x,\quad \|Y\|_{\mathcal E}+\|P\|_{H^1_tL^2_x}\le C\|h\|_2.\]
The spatial trace theorem yields \(\|Y_x(0,\cdot)\|_{L^2(0,T)}\le C\|Y\|_{L^2_tH^2_x}\); thus \(\mathcal T:H_o\to L^2(J)\) is bounded. Independently eliminating the ODE gives
\[P=e^{-\mu t}h+\gamma\int_0^te^{-\mu(t-s)}Y(s)ds,\quad MY_t-\kappa Y_{xx}-BY-\gamma S\int_0^te^{-\mu(t-s)}Y(s)ds=Se^{-\mu t}h.\]
The forcing and convolution have the signs shown and run from zero, not \(\delta\). The asserted solution estimate and positive active base are inherited, not re-proved for arbitrary material data.

## Adjoint and actual kernel

Let \(f\in L^2(J)\). Define \((z,w)\in L^2(Q_T)^2\) by the forward source-to-flux transposition functional, as in the independently reconstructed `direction-2-exact-adjoint-and-observability.md` (4). Testing with smooth compactly supported residuals gives
\[-\partial_t(Mz)-\kappa z_{xx}-Bz-\gamma w=0,\quad -w_t+\mu w-Sz=0,\quad w(T)=0,\quad w(t)=\int_t^T e^{-\mu(s-t)}S(s)z(s)ds.\]
The formal transposition data are \(z(0,t)=2A_0\mathbf1_Jf(t)\), \(z(L,t)=0\), \((Mz)(T)=0\); rough-coefficient traces are not asserted classically. Applying the identity to \(F=Se^{-\mu t}h,G=0\), which includes the full feedback via the forward solver, yields
\[\langle\mathcal Th,f\rangle=\langle h,w(0)\rangle,\qquad \mathcal T^*f=\Pi_ow(0).\]
The terminal condition for \(w\) is genuine in \(H^1_tL^2_x\); the terminal and boundary statements for \(z\) are transposition data.

Take \(\phi_n=\sqrt{2/L}\sin(2\pi nx/L)\), \(q_n=2\pi n/L\), and \(k_n=\mathcal T\phi_n\). Inherited \(\|k_n\|=O(q_n^{-1})\) gives \(\sum\|k_n\|^2<\infty\). Hence the series \(K(t,x)=\sum k_n(t)\phi_n(x)\) converges in \(L^2(J\times I)\), and \((\mathcal Th)(t)=\int K(t,x)h(x)dx\) a.e. The inherited refined expansion is \(k_n=a/q_n+\rho_n\), \(a(t)=2A_0\sqrt{2/L}e^{-\mu t}S(t,0)\), with \(\|\rho_n\|=o(q_n^{-3/2})\); this is not independently promoted to an endpoint square sum.

## Exact range and individual-state criteria

For any bounded operator between Hilbert spaces, \((\operatorname{ran}\mathcal T^*)^\perp=\ker\mathcal T\). Thus \(\ker(\mathcal T|_{H_o})=0\) iff \(\overline{\operatorname{ran}\mathcal T^*}=H_o\). For a specified \(h\), \(\mathcal Th=0\) iff \(h\perp\operatorname{ran}\mathcal T^*\); it is observable against **some** control iff \(h\notin(\operatorname{ran}\mathcal T^*)^\perp\). Exact recovery of the scalar functional \(\langle h,\cdot\rangle\) by a bounded output functional requires the stronger \(h\in\operatorname{ran}\mathcal T^*\), not merely its closure.

More precisely, for the nonzero singular pairs \(\mathcal T v_j=s_j u_j\), \(\mathcal T^*u_j=s_jv_j\), compactness implies
\[h\in\operatorname{ran}\mathcal T^*\iff h\perp\ker\mathcal T\quad\text{and}\quad \sum_j|\langle h,v_j\rangle|^2/s_j^2<\infty.\]
Proof: expand \(f=\sum f_ju_j+f_\perp\) and compare coefficients \(h_j=s_jf_j\); conversely the summability constructs \(f=\sum (h_j/s_j)u_j\). This is an exact individual-state range criterion, not a proof it holds for a given sine or that the range is closed.
