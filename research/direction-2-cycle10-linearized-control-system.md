# Cycle 10: linearized odd boundary system

At the relaxed base put \(M=c+d\theta_*>0\), \(B=-br\gamma\theta_*<0\), \(S=br\mu\theta_*\ne0\), \(d_0=\gamma S/M>0\). For perturbations with odd midpoint parity, \(QY_o=Y_o\), \(m\) is even, and
\[M Y_s-\kappa Y_{xx}=B Y+S P,\qquad P_s=-\mu P+\gamma Y,\tag{1}\]
\[Y(0,s)=a(s),\quad Y(L,s)=-a(s),\quad (Y,P)(-T_p)=0,\quad a=\tau_a.\]
The odd mechanical boundary forcing is zero. The odd lifting \(Y=X+\ell a\), \(\ell=1-2x/L\), gives homogeneous \(X\) with
\[M X_s-\kappa X_{xx}=B X+S P+B\ell a-M\ell a',\qquad P_s=-\mu P+\gamma X+\gamma\ell a.\tag{2}\]
The input terms are consequences of boundary lifting, not artificial volumetric heat sources. With \(a\in H^1_0(-T_p,0)\), standard forced energy estimates give \(X\in H^1_sL^2_x\cap L^2_s(H^2\cap H^1_0)\), \(P\in H^1_sH^2_x\) via the Volterra formula. Thus \(\mathcal K_o:a\mapsto P(0)\) is bounded \(H^1_0\to H^2\cap H_o\). This is the **linearized** map, not nonlinear preparation.

For \(\phi_n=c_L\sin(q_nx)\), \(q_n=2\pi n/L\), \(c_L=\sqrt{2/L}\), define \(A_n=(\kappa q_n^2-B)/M\), \(\Delta_n=\sqrt{(A_n-\mu)^2+4d_0}\), \(\lambda_{n,\pm}=-(A_n+\mu\mp\Delta_n)/2\), and \(C_n=2\kappa c_Lq_n/M\). Integration by parts for the inhomogeneous Dirichlet boundary gives
\[y_n'=-A_ny_n+(S/M)p_n+C_n a,\quad p_n'=\gamma y_n-\mu p_n.\tag{3}\]
Both endpoint contributions add: \(Y(0)\phi_n'(0)-Y(L)\phi_n'(L)=2a c_Lq_n\). These equations are valid for smooth controls; use the lifting to justify weak limits, not a pointwise trace of an arbitrary \(L^2\) control.

On a fixed switch-off gap \(a=0\) for \(-\varepsilon<s\le0\), the terminal map extends boundedly from \(L^2(-T_p,-\varepsilon)\) into \(H_o\): the adjoint series below has columns \(O(1/q_n)\), square summable uniformly on the positive time gap. For this unconstrained linear map, its range is dense in \(H_o\) and its projection onto each \(V_N\) is surjective (proof in the adjoint report). The same finite-dimensional surjectivity can be realized using \(C_c^\infty((-T_p,-\varepsilon))\) controls, by density and stability of an invertible finite matrix. These statements do **not** impose \(Y(0)=0\), do not mean \(P(0)\in V_N\), and are not nonlinear physical preparation. Exact finite-sine reachability under this gap and exact thermal nulling are analyzed separately.
