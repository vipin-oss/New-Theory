# Certification dossier: frozen exact smooth kernel theorem

**Verdict: THEOREM VERIFIED UNDER STATED ASSUMPTIONS — same-agent mathematical reconstruction only, not independent certification.** No separate mathematician or AI reviewer was available or consulted. No proof was inferred from 63 passing tests, numerical ranks, or finite truncations. The operator proof below uses the two explicitly identified external results; it is suitable for independent review, which remains necessary.

## Frozen theorem and data

Let \(T,d,\mu>0\), let \(0<b_1<b_2<\cdots\) satisfy \(b_n\asymp n^2\) and \(\inf_n(\sqrt{b_{n+1}}-\sqrt{b_n})>0\), and take the real Hilbert space \(H=L^2((0,T),t\,dt)\). Define
\[H_d(t,s)=\sum_{j\ge0}\frac{(dts)^j}{j!(j+1)!},\quad (\mathsf Tv)(t)=d\int_0^T H_d(t,s)v(s)s\,ds,\quad Q=(I+\mathsf T)^{-1}.\]
For smooth flat k define
\[(\mathsf Bk)_n=\int_0^T t e^{-b_nt}k(t)dt+\int_T^\infty t e^{-b_nt}(\mathsf TQk)(t)dt.\]
For every open interval \(I\) with \(\overline I\subset(0,T)\), the real space
\[\{k\in C_c^\infty(I):\mathsf Bk=0,\ (Qk)(T)=0\}\]
is infinite-dimensional. As always, a vector space contains zero; the assertion is that it contains infinitely many independent **nonzero** elements. These are admissible because they are smooth and flat at 0. This is the unchanged theorem at starting commit `e1dfe145943b7c572c384442442517db6abf41f6`; the square-root gap is part of its hypothesis, not implied merely by \(b_n\asymp n^2\).

## External inputs and dependency map

1. **Biorthogonal estimate.** Cannarsa–Martinez–Vancostenoble, [Theorem 2.1, eqs. (2.1)–(2.6)](https://arxiv.org/html/1706.02435#S2.ThmTheorem1), assumes \(\lambda_n\ge0\), global and asymptotic lower square-root gaps \(0<g<g_*\), and gives \(\sigma_n^+\in L^2(0,\ell)\) biorthogonal to \(e^{\lambda_mt}\) with \(\|\sigma_n^+\|_2^2\le e^{-2\ell\lambda_n}e^{C/(\ell g_*^2)+C\sqrt{\lambda_n}/g_*} B^*(\ell,g,g_*,N_*,n)\), where the exact piecewise \(B^*\) is the source's eq. (2.6). Here \(\lambda_n=b_n>0\), choose \(N_*=1\), \(g=g_0/2\), \(g_*=g_0\), with g₀ the frozen global lower gap. Then \(M_*=0\), and eq. (2.6) gives a uniform bound on \(B^*\). Hence (1) in `BIORTHOGONAL_NORMALIZATION_CHECK.md` follows. This input gives the sequence interpolator, not a theorem about the coupled system.
2. **Fast incompleteness.** Almira, [Theorem 29, §3.4](https://arxiv.org/html/0710.3570#Thmtheorem29): for distinct real \(\lambda_n\) and \(0<u<v\), the span of \(x^{\lambda_n}\) is dense in \(C[u,v]\) iff \(\sum_{\lambda_n\ne0}1/|\lambda_n|=\infty\). Our sum converges, so the fast exponential span is not dense on any interior subinterval after \(x=e^{-t}\).
3. **Standard functional analysis.** Hahn–Banach separation (Mederski, [§1.3–1.4](https://jmederski.impan.pl/FA_lecture.pdf)): if M is a proper closed subspace of a normed space, there is a nonzero bounded functional vanishing on M. The Riesz representation theorem for continuous functions on compact metric spaces ([Varadhan, first page](https://math.nyu.edu/~varadhan/real17/Part8.pdf)) says every bounded real functional on C(J) is integration against a finite signed Borel measure on J. These turn fast-span nondensity into a nonzero annihilating measure; convolution preserves moments and is nonzero by the Fourier-transform identity theorem. For a compact operator K on a real Hilbert space, the Fredholm alternative ([Howard, Theorem A.D.5](https://people.tamu.edu/~phoward/m612/s20/elliptic4.pdf)) states that I−K has finite-dimensional kernel, closed range equal to the orthogonal complement of the adjoint kernel, and equal kernel/adjoint-kernel dimensions. Apply it to −SR; the bounded inverse theorem on the kernel complement supplies exact preimages. These inputs supply fast-null seeds and exact solvability, respectively.

Dependencies: source 1 → smooth right inverse S; source 2 + Hahn–Banach/Riesz → infinite-dimensional seed space N; Bessel growth + Q → compact SR; Riesz–Schauder + N → infinitely many exact solutions; endpoint functional → codimension at most one; modal ODE and compatibility → physical linear odd interpretation. Source theorem 1 is never applied to the accumulating slow roots.

## Reconstruction from the frozen definitions

**(i) Bessel operator.** The series is symmetric and uniformly convergent on \([0,T]^2\). It defines a compact self-adjoint nonnegative operator because
\[\langle v,\mathsf Tv\rangle_H=d\sum_j\frac{d^j}{j!(j+1)!}\left|\int_0^T s^{j+1}v(s)ds\right|^2.\]
Thus \(Q\) exists and \(\|Q\|\le1\); the series also extends \(\mathsf Tv\) to an entire function.

**(ii) Right inverse.** Choose positive \(a,\ell,\epsilon,\eta\) with \([a,a+\ell+\epsilon]\subset I\) and \(a+\epsilon<T-\eta\). Reverse the source functions, shift by a, smooth by a fixed nonnegative \(\rho\in C_c^\infty(0,\epsilon)\), divide by its Laplace value and by t. Direct computation in the companion normalization file proves \(\int_I te^{-b_mt}\psi_n(t)dt=\delta_{mn}\) and \(\|\psi_n\|_{C^j}\le C_j e^{(a+\epsilon)b_n+C\sqrt{b_n}}\). For \(Y=\ell^2(e^{2(T-\eta)b_n})\), the series \(Sy=\sum y_n\psi_n\) converges in every C^j and has common compact support. Thus \(ES=I\) on Y, where \(E:X=L^2(I,t\,dt)\to\ell^2\) is the fast transform. No right inverse on all ℓ² is asserted.

**(iii) Actual tail.** For x extended by zero from X, \(|(\mathsf TQx)(t)|\le C e^{2\sqrt{dTt}}\|x\|_X\) for \(t\ge T\). Consequently \(|(Rx)_n|\le Ce^{-Tb_n}\|x\|_X\). The coordinate norms of \(R:X\to Y\) have a summable square majorant \(C^2e^{-2\eta b_n}\), so R is Hilbert–Schmidt, and \(SR:X\to X\) is compact.

**(iv) Fast seeds and exact Fredholm solvability.** The fast-null smooth space N is infinite-dimensional by input 2 and the convolution construction above. For \(A=I+SR\), the Riesz–Schauder theorem makes \(\operatorname{ran}A\) closed of finite codimension. Therefore \(N\cap\operatorname{ran}A\) is infinite-dimensional. Select independent \(h_i\) there and solve \(Ax_i=h_i\). Then \(x_i=h_i-SRx_i\in C_c^\infty(I)\), and \(Ex_i=-ESRx_i=-Rx_i\), **for every n**. Their A-images are independent, hence so are the x_i. This is an existence construction through an exact Fredholm inverse, not an explicit decimal formula or finite-mode approximation.

**(v) Endpoint.** On interior-supported X, define \(L(x)=-[\mathsf TQx](T)\). This is bounded: the Bessel row at T belongs to H. For smooth x it equals the ordinary value \((Qx)(T)\) because x vanishes near T. The kernel of L in the infinite-dimensional exact-solution space still has infinite dimension. Each of its nonzero elements satisfies all requirements.

**(vi) Modal reconstruction.** Under the separately stated frozen linear odd PDE assumptions, \(f(t)=e^{\mu t}tQk(t)\) is smooth and has \(f(0)=f(T)=0\). A direct calculation in `EXACT_MODAL_RECONSTRUCTION_CHECK.md` derives
\[Y_n(0)=\frac{C_nb_n}{b_n+d/b_n}(\mathsf Bk)_n,\quad
P_n(0)=\frac{C_n\gamma}{b_n}\int_0^T t e^{dt/b_n}(Qk)(t)dt.\]
The first identity holds for every n. Positivity of the rows forces f to change sign; compact support of k implies f is analytic near each endpoint but not on the full interval, and a Bessel injectivity argument excludes a terminal switch-off gap. For nonzero f, all but finitely many memory modes are nonzero. The full field interpretation relies on the smooth boundary-lift/linear odd model assumptions in the modal file, not on the operator theorem alone.

## Line-by-line external reviewer checklist

- [ ] Check source Theorem 2.1 and its \(N_*=1\), \(M_*=0\) specialization; verify the estimated norm is for positive exponentials.
- [ ] Recompute reversal, shift, Laplace convolution and \(1/(t\rho_n)\) in (2) of the normalization file.
- [ ] Verify the positive gap \(T-\eta-a-\epsilon\), every-derivative summability, and common compact support.
- [ ] Check Müntz's interval change, real signed-measure annihilator, Fourier nonvanishing, and disjoint supports.
- [ ] Verify Bessel growth, inverse Q and the weighted Hilbert–Schmidt tail estimate.
- [ ] Check exact closed range and that the seed-space intersection is infinite-dimensional, not just dense.
- [ ] Check smoothness of Fredholm preimages, coordinatewise ES, endpoint map and nonzero dimension after one constraint.
- [ ] Independently derive physical modal signs, coefficients, stability assumptions, boundary trace and memory formula.
- [ ] Distinguish this same-agent report from independent certification; examine original Ivanov–Pandolfi and broader priority literature separately.

## Open checks and scope

No separate human or AI has verified this proof or the cited proofs. The original Ivanov–Pandolfi paper was not retrieved; no priority claim is made. Nonlinear physical preparation, full-system identifiability, prescribed Gevrey order, a numerical explicit control, and quantitative control costs are outside this theorem. The operator result is mathematically checked under its stated hypotheses and external theorems; the modal conclusion additionally assumes the frozen linear odd PDE and its regularity framework.
