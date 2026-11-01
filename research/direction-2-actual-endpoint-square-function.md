# Actual endpoint square function

**Classification: OPEN.** The conditional sufficient criterion below is rigorous assuming the inherited fixed-feedback corrector estimates; no actual-model counterexample or unconditional endpoint theorem is claimed.

Write \(k_n=a/q_n+\rho_n\), \(a=2A_0\sqrt{2/L}e^{-\mu t}S(t,0)\), and \(R=\sum_n\rho_n\phi_n\). By Parseval and the Dirichlet spectral form domain,
\[\sum_nq_n^2\|\rho_n\|_{L^2(J)}^2<\infty\quad\Longleftrightarrow\quad R\in L^2(J;H^1_0(I)).\]
The actual proven individual \(o(q_n^{-3/2})\) and \(H^s\), \(s<1\), do not sum at \(s=1\).

## A new actual-coefficient positive-time spatial gain

For every \(\varepsilon>0\), the established difference-quotient result gives \(y_{b,t}\in L^2(\varepsilon,T;H^1_0)\) and \(y_b\in L^\infty(\varepsilon,T;H^2)\). The base ODE has \(p_b(t)=\gamma\int_0^te^{-\mu(t-s)}Qy_b(s)ds\), so \(p_b\in C([0,T];H^2)\) from \(y_b\in L^2(0,T;H^2)\); its time derivative is bounded in \(H^2\) on \((\varepsilon,T)\). The scalar mean \(v_b\), prescribed loading, and their needed time derivatives are bounded. Thus \(E_b=m'+rp_{b,t}\) and \(w_b=m-v_b-\alpha p_b+\beta Qy_b\) lie in \(L^\infty(\varepsilon,T;H^2)\). One-dimensional \(H^2\) is an algebra, so the actual base equation
\[\kappa y_{b,xx}=c y_{b,t}+d\theta_b Qy_{b,t}+b\theta_bE_b-k\lambda w_b^2\]
has right-hand side in \(L^2(\varepsilon,T;H^1)\). Consequently \(y_b\in L^2(\varepsilon,T;H^3)\), and its actual source amplitude satisfies
\[S\in L^2(\varepsilon,T;H^3)\cap H^1(\varepsilon,T;H^1).\]
The latter follows directly from \(S=\mu(br\theta_b-2kw_b)\) and \(w_{b,t}=m'-v'_b-\alpha p_{b,t}+\beta Qy_{b,t}\). No endpoint value of \(y_{b,xx}\), \(S_{xx}\), or \(M_t\) is used. Constants can deteriorate as \(\varepsilon\downarrow0\). This genuine spatial gain is **not** isotropic \(H^{2+\eta}\): it supplies no quantitative time modulus for \(S_t\).

## Dyadic target and time obstruction

Keep the feedback \(M,B,S,\gamma,\mu\) fixed and replace only the direct forcing amplitude by smooth even \(f\). The inherited corrector gives \(\|\rho_n(S)\|\le Cq_n^{-3/2}\|S-f\|_{\mathcal A}+Cq_n^{-2}\|f\|_{H^3}\), \(\mathcal A=H^1_tL^2_x\cap L^2_tH^2_x\). It includes feedback and the initial cutoff terms, with the actual pre-delay evolution. For \(2^j\le n<2^{j+1}\),
\[\sum q_n^2\|\rho_n\|^2\le C(\|S-f_j\|_{\mathcal A}^2+2^{-j}\|f_j\|_{H^3(Q_T)}^2).\]
Thus the endpoint follows if the right side sums over \(j\). This is the precise missing summable bound. Ordinary density gives convergence of approximation error but no rate relative to \(H^3\) cost. Space gain on \((\varepsilon,T)\) does not control time mollification of \(S_t\), and it says nothing quantitative at the initial corner. Merely dropping pre-delay terms or asserting their boundary smoothing is invalid.

A precise abstract obstruction to this **approximation route** is seen on a periodic time interval, not as a physical counterexample. Let \(g(t)=\sum_{k\ge1}2^{-k}k^{-1}\sin(2^kt)\) and \(S_{\rm abs}=g(t)\psi(x)\), with smooth nonzero \(\psi\). Then \(S_{\rm abs}\in H^1_tH^m_x\) for every \(m\), but \(g'\) has dyadic Fourier coefficients of size \(1/k\). For any periodic \(f_j\), orthogonality and the scalar minimization of the squared \(H^1_t\) error plus \(2^{-j}\) times the squared \(H^3_t\) cost give a lower bound \(c\sum_{k\ge j/4+C}k^{-2}\ge c'/j\). The sum over \(j\) diverges. This demonstrates that arbitrarily good spatial smoothness plus the stated first time derivative does not automatically give this kind of dyadic cost, in the periodic analogue. It neither proves the actual source has this time behavior nor excludes another PDE-specific endpoint proof.

**Restart:** either prove a quantitative time modulus/weighted interpolation estimate for the actual \(S\), including pre-delay contributions, that makes the dyadic costs summable, or derive a direct block trace estimate exploiting correlations between columns and feedback. Differentiating the nonlocal base mass in time requires controlling the mean term and dual spaces; formal \(y_{tt}\) and boundary traces are insufficient. Alternatively construct an actual base and show divergence, not an abstract sequence.
