# Cycle 5: early-history and actual coupled restart

**Decision: PASS under the same conditional solution and feedback estimates.** Take \(t_0=\delta/2>0\). For the actual full-history solution from \((Y,P)(0)=(0,h)\), define
\[Ah=Y(t_0),\quad Kh=\gamma\int_0^{t_0}e^{-\mu(t_0-s)}Y(s)\,ds,\quad P(t_0)=e^{-\mu t_0}h+Kh.\tag{1}\]
Let \(\mathcal R_{t_0}(y_0,p_0)\) be the output \(2A_0\kappa Y_x(0,\cdot)|_J\) of the *same* post-\(t_0\) system, with actual \(M,B,S,\gamma,\mu\), and initial state \((y_0,p_0)\). \(A:H_o\to V_o\) and \(K:H_o\to H_o\) are bounded by the strong solution and the Volterra formula. Strong forward uniqueness and linearity prove
\[\mathcal T h=\mathcal R_{t_0}(Ah,0)+\mathcal R_{t_0}(0,Kh)+\mathcal R_{t_0}(0,e^{-\mu t_0}h).\tag{2}\]
This is an algebraic decomposition of the actual reachable state, not a physical assertion that the three states can independently be prepared.

For \(h=\phi_n\), the trial \(A_n(t)=e^{-\mu t}S(t)\phi_n/(\kappa q_n^2)\) has \(\sup_t\|A_n(t)\|_2\le Cq_n^{-2}\); the explicit weak estimate in the companion corrector audit gives \(\sup_t\|Y-A_n\|_2\le Cq_n^{-2}\). \(S\in C_tH^1_x\), \(Y\in C_tL^2\), so the bound holds at the prescribed \(t_0\), not merely almost everywhere. Therefore
\[\|A\phi_n\|_2\le Cq_n^{-2},\quad \|K\phi_n\|_2\le |\gamma|\int_0^{t_0}e^{-\mu(t_0-s)}\|Y(s)\|_2ds\le Cq_n^{-2}.\tag{3}\]

For memory-only initial data, the actual strong estimate with \(y_0=0\) and \(p_0\in H_o\) gives \(\|\mathcal R_{t_0}(0,p_0)\|_Z\le C\|p_0\|_2\). For heat-only data \(y_0\in V_o\), the weak estimate with \(p_0=0\) gives \(\|Y\|_{L^\infty L^2\cap L^2V}+\|P\|_{L^\infty V'}\le C\|y_0\|_2\). In fact the Volterra equation gives \(\|P\|_{L^2L^2}\le C\|Y\|_{L^2L^2}\). Choose \(\chi=0\) near \(t_0\), \(\chi=1\) on \(J\), \(\|\chi'\|_\infty<\infty\). The zero-initial pair \((\chi Y,\chi P)\) solves the actual system with forcings \((M\chi'Y,\chi'P)\). Both belong to \(L^2\) and are bounded by \(C\|y_0\|_2\); the strong estimate plus \(H^2\to\) boundary derivative trace implies
\[\|\mathcal R_{t_0}(y_0,0)\|_Z\le C\|y_0\|_2.\tag{4}\]
The fixed gap \(\delta-t_0\) is essential; \(C\) may blow up as it tends to zero. It is not a bound for an arbitrary nonsmooth endpoint trace at \(t_0\).

Combining (3)–(4) and the memory bound, on \(\mathcal B_j=\{2^j\le n<2^{j+1}\}\),
\[\sum_{\mathcal B_j}q_n^2(\|\mathcal R_{t_0}(A\phi_n,0)\|_Z^2+\|\mathcal R_{t_0}(0,K\phi_n)\|_Z^2)\le C\sum_{\mathcal B_j}q_n^{-2}\le C2^{-j}.\tag{5}\]
For the third term set \(P=e^{-\mu(t-t_0)}e^{-\mu t_0}\phi_n+p=e^{-\mu t}\phi_n+p\). Then \(p(t_0)=0\), \(p_t+\mu p=\gamma Y\), and the direct source is exactly \(e^{-\mu t}S(t)\phi_n\), with the same \(2A_0\sqrt{2/L}e^{-\mu t}S(t,0)/q_n\) leading term. Applying the companion fixed-feedback construction on \((t_0,T)\), using a cutoff zero near \(t_0\), controls this component; the smoothing construction restricts to that interval with fixed extension constants. The full Volterra feedback \(p\), its \(\chi'p\) commutator, and the trial mismatch at \(t_0\) are retained. Combining (5) with its dyadic bound yields the same endpoint conclusion as the global proof.
