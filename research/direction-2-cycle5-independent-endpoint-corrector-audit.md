# Cycle 5: fixed-feedback corrector and endpoint re-derivation

**Decision: CONDITIONALLY PROVED** for the frozen active system, assuming the strong forced-solution theorem stated below and the base conclusions in the companion audit. No injectivity, inverse stability, parameter validation or independent human certification follows. The proof reconstructs the corrector; only well-posedness/strong forcing is imported from the base/forced-solution audit.

## 1. Source smoothing, no artificial endpoint conditions

Let \(Q_T=(0,T)\times(0,L)\), \(\mathcal A=H^1_tL^2_x\cap L^2_tH^2_x\), and \(N=\|S\|_{L^2H^3}+\|S\|_{H^1H^1}+\|S\|_{H^2L^2}\). Use one fixed bounded time extension simultaneously on \(L^2,H^1,H^2\), e.g. finite linear combinations of reflected/rescaled values matching derivatives up to first order, followed by a fixed cutoff; apply Bochner-valuedly in \(H^3,H^1,L^2\). Use one fixed spatial extension simultaneously on \(H^1,H^2,H^3\). Average with reflection about the midpoint after restriction to preserve evenness. No reflection is imposed across spatial endpoints as a boundary condition: a general Sobolev extension is used.

On the extended rectangle, Fourier variables \(\omega,\xi\) give
\[(1+\omega^2)^{1/2}(1+\xi^2)^2\le\tfrac12[(1+\xi^2)^3+(1+\omega^2)(1+\xi^2)],\]
so \(S\in H^{1/2}_tH^2_x\), norm \(\le CN\). With a compactly supported unit-mass mollifier \(\eta\), put \(f_\tau=\eta_\tau*_t S\) after extension and restrict. Translation estimates for \(S\) in \(H^{1/2}_tH^2_x\) and for \(S_t\) in \(H^1_tL^2_x\) yield
\[\|S-f_\tau\|_{\mathcal A}\le C(\tau^{1/2}+\tau)N.\tag{1}\]
All four third derivatives obey
\[\|f_{xxx}\|_2\le CN,\quad\|f_{txx}\|_2\le C\tau^{-1/2}N,\quad
\|f_{ttx}\|_2\le C\tau^{-1}N,\quad\|f_{ttt}\|_2\le C\tau^{-1}N.\tag{2}\]
The first is convolution of \(S_{xxx}\); the second is the Fourier multiplier \(|\omega\widehat\eta(\tau\omega)|\lesssim\tau^{-1/2}(1+\omega^2)^{1/4}\); the third differentiates the mollifier once on \(S_{tx}\), and the fourth once on \(S_{tt}\). Lower orders are no worse. Hence \(\|f_\tau\|_{H^3(Q_T)}\le C(1+\tau^{-1})N\). A further smooth even approximation in isotropic \(H^3\) can be chosen with arbitrarily small error, including in \(\mathcal A\), so the classical trial below is legitimate. All extension/mollifier constants are fixed, independent of \(\tau\).

For \(\tau_j=2^{-j/4}\), (1)–(2) imply
\[\sum_{j\ge0}[\|S-f_j\|_{\mathcal A}^2+2^{-j}\|f_j\|_{H^3}^2]
\le CN^2\sum_{j\ge0}(2^{-j/4}+2^{-j/2})<\infty.\tag{3}\]
This is a direct construction for the actual \(S\), not an appeal to an abstract K-functional implication.

## 2. Uniform weak estimate for the actual feedback

Let \(V=H^1_0\cap H_o\), \(V'\) its dual. Fix actual even \(M,B,S,\gamma,\mu\), with \(0<m_0\le M\le m_1\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2(Q_T)\), \(S\in L^\infty_tH^1_x\). For a strong solution of
\[Me_t-\kappa e_{xx}=Be+Sp+F,\qquad p_t+\mu p=\gamma e+G,\tag{4}\]
we derive
\[\|e\|_{L^\infty L^2}+\|e\|_{L^2V}+\|p\|_{L^\infty V'}
\le C_W(\|e_0\|_2+\|p_0\|_{V'}+\|F\|_{L^2V'}+\|G\|_{L^2V'}).\tag{5}\]
Divide the heat equation by \(M\) and pair with \(e\). With \(a=\kappa/M\), the diffusion is \(\int a|e_x|^2+\int a_x e_xe\); \(\|a_x\|_2\le C\|M_x\|_2\). Young gives \(|\int a_xe_xe|\le\epsilon\|e_x\|^2+C_\epsilon\|a_x\|_2^4\|e\|^2\). Similarly \(|\int (B/M)e^2|\le\epsilon\|e_x\|^2+C_\epsilon\|B/M\|_2^{4/3}\|e\|^2\). Multiplication by \(1/M,S/M\) maps \(V\to V\) with norm controlled by \(m_0,m_1,\|M_x\|_{L^\infty L^2},\|S\|_{L^\infty H^1}\); pair \(p\) in \(V'\) with \((S/M)e\), and \(F\) with \(e/M\). Pair the ODE with the inverse Dirichlet Laplacian applied to \(p\). The derivative of \(\|p\|_{V'}^2\) is legitimate for the already-existing strong solution. Integrability of \(\|B(t)\|_2^{4/3}\) and Gronwall prove (5). It is not used to construct arbitrary \(V'\)-forced solutions.

The strong theorem we retain explicitly is, for \(F,G\in L^2(Q_T),e_0\in V,p_0\in H_o\),
\[\|e\|_{H^1L^2\cap L^2H^2}+\|p\|_{H^1L^2}\le C_E(\|e_0\|_V+\|p_0\|_2+\|F\|_2+\|G\|_2).\tag{6}\]
The earlier strong Galerkin energy uses \(m_0,\kappa,\|B\|_2,\|S\|_\infty,T,L\); it is not a reference-model estimate.

## 3. Trial and weak-first critical bound

For even amplitude \(f\in\mathcal A\), define the auxiliary zero-initial coupled system
\[MY_t-\kappa Y_{xx}=BY+Sp+e^{-\mu t}f\phi_n,\quad p_t+\mu p=\gamma Y.\tag{7}\]
Only the direct amplitude varies. Here \(\phi_n=c_L\sin(q_nx)\), \(c_L=\sqrt{2/L}\), and \(q_n=2\pi n/L\). Define \(A=e^{-\mu t}f\phi_n/(\kappa q_n^2)\), \(e=Y-A\). Then \(e_0=-A(0),p_0=0\) and forcing in (4) is \(F=-\mathcal E_A,G=\gamma A\), with
\[\mathcal E_A=\frac{c_Le^{-\mu t}}{\kappa q_n^2}\{D_f\sin(q_nx)-2\kappa q_n f_x\cos(q_nx)\},\quad D_f=M(f_t-\mu f)-Bf-\kappa f_{xx}.\tag{8}\]
\(\mathcal A\hookrightarrow C_tH^1_x\hookrightarrow L^\infty(Q_T)\), so \(\|D_f\|_2\le C\|f\|_{\mathcal A}\). Integration by parts against \(V\) proves \(\|f_x\cos(q_nx)\|_{V'}\le Cq_n^{-1}\|f_x\|_{H^1}\); endpoint terms vanish because the **test** is Dirichlet, not because \(f_x\) is zero. Thus
\[\|\mathcal E_A\|_{L^2V'}+\|A\|_{L^2V'}+\|A(0)\|_2\le Cq_n^{-2}\|f\|_{\mathcal A}.\]
Equation (5) first gives \(\|e\|_{L^\infty L^2\cap L^2H^1}+\|p\|_{L^\infty V'}\le Cq_n^{-2}\|f\|_{\mathcal A}\). Separately \(\|\mathcal E_A\|_2+\|A(0)\|_V+\|A\|_2\le Cq_n^{-1}\|f\|_{\mathcal A}\); (6) gives \(\|e\|_{L^2H^2}\le Cq_n^{-1}\|f\|_{\mathcal A}\). For \(v=e_x\),
\[|v(0)|^2\le L^{-1}\|v\|_2^2+2\|v\|_2\|v_x\|_2.\tag{9}\]
Time integration and Cauchy–Schwarz give \(\|e_x(0,\cdot)\|_{L^2(J)}\le Cq_n^{-3/2}\|f\|_{\mathcal A}\) after enlarging \(C\) for the finite modes. The leading trial flux is \(2A_0\kappa A_x(0)=2A_0c_Le^{-\mu t}f(t,0)/q_n\); it is well-defined because \(\mathcal A\subset C_tH^1\). Therefore the remainder is linear in the amplitude and has the same critical bound, with actual \(S\) inside (7) unchanged.

## 4. Smooth corrector, initial mismatch, two cutoff terms

For smooth even \(f\), set \(\ell=1-2x/L\), \(H_f=f_x\cos(q_nx)-f_x(t,0)\ell\), and
\[C_n=\frac{2c_Le^{-\mu t}}{\kappa q_n^3}H_f.\tag{10}\]
Evenness gives \(f_x(t,L)=-f_x(t,0)\), so \(C_n\) vanishes at both endpoints and is odd. Inserting \(U=A+C_n\) in the left-minus-right heat residual gives the \(-2\kappa q_nf_x\cos\) part of (8) plus \(-\kappa(C_n)_{xx}\); the latter contains \(+2c_Le^{-\mu t}f_x\cos/q_n\), cancelling it exactly. Remaining terms are combinations of \(D_f/q_n^2\), \(Mf_{xt}/q_n^3\), \(BH_f/q_n^3\), \(f_{xxx}/q_n^3\), \(f_{xx}/q_n^2\), and the indicated endpoint traces multiplied by \(\ell\). The space-time \(H^3\) norm controls \(f_x\) in \(L^\infty\), \(f_x(t,0), f_{xt}(t,0), f_{xx}(t,0)\) in \(L^2_t\), and initial \(f(0),f_x(0)\) in the trace spaces needed below. Consequently
\[\|\mathcal E_U\|_{L^2}\le Cq_n^{-2}\|f\|_{H^3},\quad \|U\|_{L^2}+\|U(0)\|_2\le Cq_n^{-2}\|f\|_{H^3},\quad \|U(0)\|_V\le Cq_n^{-1}\|f\|_{H^3}.\tag{11}\]
The constants use fixed space-time trace/embedding constants, \(\|B\|_2\), \(m_1\), \(\mu,\kappa,L,T\); they do **not** depend on \(n\) or \(f\). For \(e=Y-U\), (5) yields \(\|e\|_{L^\infty L^2\cap L^2V}+\|p\|_{L^\infty V'}\le Cq_n^{-2}\|f\|_{H^3}\). Since \(p(t)=\gamma\int_0^te^{-\mu(t-s)}[e(s)+U(s)]ds\), its actual full feedback satisfies \(\|p\|_{L^2}\le Cq_n^{-2}\|f\|_{H^3}\).

Let \(\chi=0\) near 0 and \(\chi=1\) on \(J\). The pair \((\chi e,\chi p)\) has zero initial state and forcing
\[(F_\chi,G_\chi)=(-\chi\mathcal E_U+M\chi'e,\ \chi\gamma U+\chi'p).\tag{12}\]
Both commutators, including \(\chi'p\), are in \(L^2\) and \(O(q_n^{-2}\|f\|_{H^3})\); (6) gives \(\|e\|_{L^2(J;H^2)}\le Cq_n^{-2}\|f\|_{H^3}\). Also \(C_{n,x}(t,0)=2c_Le^{-\mu t}[f_{xx}(t,0)+2f_x(t,0)/L]/(\kappa q_n^3)\), hence its \(L^2(J)\) norm is at most \(Cq_n^{-3}\|f\|_{H^3}\). Thus \(\|\rho_n(f)\|_{L^2(J)}\le Cq_n^{-2}\|f\|_{H^3}\).

Using linearity in direct amplitude, the critical bound applied to \(S-f_j\) and the smooth bound to \(f_j\) give
\[\|\rho_n(S)\|_Z\le Cq_n^{-3/2}\|S-f_j\|_{\mathcal A}+Cq_n^{-2}\|f_j\|_{H^3}.\tag{13}\]
Here \(C\) depends on \(L,T,\delta,\kappa,\mu,\gamma,A_0,m_0,m_1,\|M_x\|_{L^\infty L^2},\|B\|_2,\|S\|_{L^\infty H^1}\), and the strong/weak constants and fixed cutoff, but not \(n,j,f_j\). For \(f=S\), \(P=e^{-\mu t}\phi_n+p\) is exactly the full physical linearized memory. Summing (13) squared over \(2^j\le n<2^{j+1}\), \(q_n\asymp n\), yields \(C(\|S-f_j\|_{\mathcal A}^2+2^{-j}\|f_j\|_{H^3}^2)\). Equation (3) proves \(\sum_nq_n^2\|\rho_n\|^2<\infty\). The finite low modes are harmless.
