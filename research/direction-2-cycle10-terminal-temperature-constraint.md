# Cycle 10: a linearized terminal-temperature obstruction with a switch-off gap

## Theorem (linearized odd system only)

Assume \(a\in L^2(-T_p,-\varepsilon)\), extended by zero on \((-\varepsilon,0)\), \(\varepsilon>0\). For the exact linearization about the relaxed state with the stated nonzero coupling, if \(Y(\cdot,0)=0\), then \(a=0\) and hence \(P(\cdot,0)=0\). This is not a nonlinear theorem and does not cover smooth controls acting arbitrarily close to \(s=0\).

**Proof.** Put \(F(z)=\int_{\varepsilon}^{T_p}e^{zt}a(-t)dt\). This is entire. With the modal notation in the linearized report, solving (3) from zero yields
\[y_n(0)=C_n\left[\frac{\lambda_{n,+}+\mu}{\Delta_n}F(\lambda_{n,+})+\frac{-\lambda_{n,-}-\mu}{\Delta_n}F(\lambda_{n,-})\right],\tag{1}\]
\[p_n(0)=\frac{C_n\gamma}{\Delta_n}[F(\lambda_{n,+})-F(\lambda_{n,-})].\tag{2}\]
Boundary forcing and both branches are retained. Let \(\delta_n=\lambda_{n,+}+\mu>0\), \(b_n=-\lambda_{n,-}-\mu>0\). Distinct roots satisfy \(\delta_n b_n=d_0>0\), \(\delta_n\asymp q_n^{-2}\), \(b_n\asymp q_n^2\), and \(\lambda_{n,-}\le-cq_n^2\) for large \(n\). If \(Y(0)=0\), each sine coefficient in (1) is zero and
\[F(\lambda_{n,+})=-\frac{b_n}{\delta_n}F(\lambda_{n,-}).\tag{3}\]
The ratio is \(O(q_n^4)\), while Cauchy–Schwarz and the positive gap give \(|F(\lambda_{n,-})|\le\sqrt{T_p}\|a\|_2e^{-c\varepsilon q_n^2}\). Therefore \(|F(-\mu+\delta_n)|\) decays faster than every power of \(\delta_n\). If the entire function \(F\) had a nonzero first Taylor coefficient of order \(j\) at \(-\mu\), the ratio \(|F(-\mu+\delta_n)|/\delta_n^j\) would tend to a nonzero value. This contradiction makes every Taylor coefficient zero; analyticity implies \(F\equiv0\), and injectivity of the Fourier transform of the compactly supported time function gives \(a=0\). Equation (2) gives \(P(0)=0\). ∎

The linearized **odd** thermal state is independent of the symmetric bath control and scalar displacement, so they cannot cancel it at first order. This calculation does not show the full nonlinear terminal constraint implies \(a=0\): nonlinear mode mixing can create terms not represented by (1), and the constrained nonlinear control set may have singular geometry. It also does not settle controls that merely satisfy \(a(0)=0\) but have no terminal gap. Smooth flat-at-zero controls could be studied separately; no such extension is needed or asserted.
