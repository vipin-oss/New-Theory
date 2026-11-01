# Actual endpoint: conditional logarithmic closure and early history

**Classification: CONDITIONALLY PROVED.** Assume the inherited actual-base and fixed-feedback weak/strong/corrector estimates, and the additional explicit small-load coercivity condition (1) of `direction-2-active-base-temporal-bootstrap.md`. Then, for the frozen nonzero-loaded system and fixed \(J=(\delta,T)\),
\[\boxed{\sum_{n\ge1}q_n^2\|\rho_n\|_{L^2(J)}^2<\infty,\qquad k_n=\frac{2A_0\sqrt{2/L}e^{-\mu t}S(t,0)}{q_n}+\rho_n.}\tag{1}\]
This is a symbolic sufficient regime, not a verified experimental load, an unconditional theorem for all previously allowed amplitudes, an injectivity theorem, or independent human certification. The original actual model and its complete memory are retained.

## 1. Quantitative logarithmic approximation

The companion bootstrap proves globally
\[S\in L^2_tH^3_x\cap H^1_tH^1_x\cap H^2_tL^2_x.\tag{2}\]
Let \(\mathcal A=H^1_tL^2_x\cap L^2_tH^2_x\), and let \(H^3(Q)\) denote all \(\partial_t^a\partial_x^b\) with \(a+b\le3\) in \(L^2\). Extend simultaneously in time for orders 0, 1 and 2 and in space for orders 1, 2 and 3; choose bounded extension operators on the rectangle, preserving even spatial parity by averaging. The earlier Fourier interpolation gives \(S\in H^{1/2}_tH^2_x\). Convolve in time at scale \(\tau\), then approximate in isotropic \(H^3\) by smooth even functions. A constant independent of \(\tau\) satisfies
\[\|S-f_\tau\|_\mathcal A\le C(\tau+\tau^{1/2})\mathfrak N,\qquad
\|f_\tau\|_{H^3(Q)}\le C(1+\tau^{-1})\mathfrak N,\tag{3}\]
where \(\mathfrak N\) is the sum of the norms in (2). Indeed, \(\partial_t(S-f_\tau)\) is \(O(\tau)\) in \(L^2\) by \(S_{tt}\in L^2\), while the \(L^2H^2\) error is \(O(\tau^{1/2})\). For the \(H^3\) cost: \(f_{xxx}\) uses \(L^2H^3\), \(f_{txx}\) uses the half-time derivative in \(H^2\) and costs \(O(\tau^{-1/2})\), \(f_{ttx}\) uses \(S_t\in L^2H^1\), and \(f_{ttt}\) uses \(S_{tt}\in L^2\); the last two cost \(O(\tau^{-1})\). Standard smooth approximation in \(H^3\) may be chosen with errors smaller than a fixed multiple of the displayed bounds, preserving parity.

Take \(\tau_j=2^{-j/4}\). Then
\[\|S-f_j\|_\mathcal A^2+2^{-j}\|f_j\|_{H^3}^2\le C\mathfrak N^2(2^{-j/4}+2^{-j/2}),\tag{4}\]
which is summable. Thus the exact logarithmic spectral condition of `direction-2-endpoint-anisotropic-regularity-and-dyadic-proof.md`, (6), holds. The older lacunary counterexample only showed that the weaker \(L^2H^3\cap H^1H^1\) assumptions alone do not imply this: its time derivative lacks the new \(H^1_tL^2\) property.

Fix **actual feedback** \(M,B,S,\gamma,\mu\) and vary only the direct source amplitude. The inherited uniform corrector estimate gives
\[\|\rho_n(S)\|_{L^2(J)}\le C q_n^{-3/2}\|S-f_j\|_\mathcal A+Cq_n^{-2}\|f_j\|_{H^3(Q)}.\tag{5}\]
The weak error includes the initial trial mismatch; the strong positive-time cutoff includes both \(M\chi'e\) and \(\chi'p\), with \(p\) the full Volterra feedback. \(C\) is fixed by the actual coefficients and delay, not by \(n,j,f_j\). Thus for \(\mathcal B_j=\{2^j\le n<2^{j+1}\}\),
\[\sum_{n\in\mathcal B_j}q_n^2\|\rho_n\|^2\le C\mathfrak N^2(2^{-j/4}+2^{-j/2}),\tag{6}\]
using \(\sum_{\mathcal B_j}q_n^{-1}=O(1)\), \(\sum_{\mathcal B_j}q_n^{-2}=O(2^{-j})\). Sum the blocks and add the finite head to obtain (1). The sum is over the **actual** columns, not a comparison model. The equivalent odd kernel residual satisfies \(R\in L^2(J;H^1_0(I))\). Since the leading spatial profile \(\ell\) is in \(H^1(I)\), the complete odd kernel \(K=a\ell+R\) is in \(L^2(J;H^1(I))\). Volkov's verified Theorem 1.1 therefore gives \(\sum_{m\ge1}m^2s_m(\mathcal T)^2<\infty\) under these same conditions (extend the odd kernel to all \(L^2(I)\); the nonzero singular values are those of the odd-domain operator). This is weighted square summability, not an observation lower bound.

## 2. Exact restart decomposition and early-history block estimate

Let \(t_0=\delta/2\), \(A=A_{t_0}\), \(K=K_{t_0}\), and let \(\mathcal R_{t_0}\) be the actual coupled restart-to-flux map on \(J\). Exact uniqueness of the forward problem gives, for every \(h\in H_o\),
\[\mathcal Th=\mathcal R_{t_0}(Ah,0)+\mathcal R_{t_0}(0,Kh)+\mathcal R_{t_0}(0,e^{-\mu t_0}h).\tag{7}\]
The first is early heat, the second is the early accumulated memory \(Kh=\gamma\int_0^{t_0}e^{-\mu(t_0-s)}Y(s)ds\), and the third is the surviving unsmoothed memory. **Every** restart solution uses the actual feedback after \(t_0\); none resets or drops it. The last term can be written as a late direct source \(e^{-\mu t}S(t)h\) plus a zero-initial ODE feedback \(p_t+\mu p=\gamma Y\).

The actual full-history weak-corrector estimate gives uniformly in \(t\in[0,t_0]\), \(\|Y[\phi_n](t)\|_2\le Cq_n^{-2}\), so
\[\|A\phi_n\|_2+\|K\phi_n\|_2\le Cq_n^{-2}.\tag{8}\]
For the memory restart, the inherited strong estimate gives \(\|\mathcal R_{t_0}(0,p_0)\|_Z\le C\|p_0\|_2\). For the heat restart, the weak estimate with \(P(t_0)=0\) yields \(\|Y\|_{L^2_tH^1}+\sup_t\|Y\|_2\le C\|Y(t_0)\|_2\); the ODE formula then controls \(P\) in \(L^2_tL^2\). Choose a smooth cutoff zero near \(t_0\) and one on \(J\). The strong zero-initial estimate applied to \((\chi Y,\chi P)\) has sources \(M\chi'Y\) and \(\chi'P\), both controlled in \(L^2\). Therefore
\[\|\mathcal R_{t_0}(y_0,0)\|_Z\le C\|y_0\|_2\quad(y_0\in V_o).\tag{9}\]
This proves positive-gap smoothing for the **coupled** heat component in the required observation norm, without claiming an unsupported heat-kernel derivative. Combining (8)–(9),
\[\sum_{n\in\mathcal B_j}q_n^2\bigl(\|\mathcal R_{t_0}(A\phi_n,0)\|_Z^2+\|\mathcal R_{t_0}(0,K\phi_n)\|_Z^2\bigr)\le C2^{-j}.\tag{10}\]
These are uniform whole-block bounds for both early components, not independent-memory assumptions.

For the third term, on \((t_0,T)\) apply the same fixed-feedback corrector and (3)–(6) to \(S\) restricted to that interval, with observation separated from the restart by \(\delta-t_0>0\); the exponential is \(e^{-\mu t}\), so the subtracted leading term is exactly \(a/q_n\). Its zero-initial auxiliary ODE feedback is retained. Equations (7), (10) and this late bound give an independent decomposition-based proof of (1). The global proof above already includes all early terms through the cutoff; (7) makes their individual roles explicit.

## 3. Status outside the threshold

Without the additional mass-coercivity bound (1) in the companion report, the earlier positive-time anisotropic regularity remains established but does not by itself give the square-Dini condition or logarithmic criterion. No physical endpoint failure is constructed; outside this smaller proven regime the actual endpoint remains **OPEN**.
