# Theorems: exact kernel, density and quasianalytic subclass

## Theorem 1: compact operator with dense, nonclosed range

Under the physical assumptions in `EXACT_FLAT_CORRECTION_OPERATOR.md`, \(\mathsf D:H=L^2((0,T),t\,dt)\to\ell^2\), (5) there, is Hilbert–Schmidt and has dense nonclosed range. Its restriction to the precise smooth flat-correction/endpoint class has dense image, but its kernel on that class is **not determined**.

*Proof.* Put \(r_n(t)=e^{-b_nt}+d b_n^{-2}e^{\delta_nt}\). In H,
\[\|e^{-b_nt}\|_H\le (2b_n)^{-1},\quad \|d b_n^{-2}e^{\delta_nt}\|_H\le Cb_n^{-2}.\]
Since \(b_n\asymp n^2\), the squared row norms are summable, so \(\mathsf D\) is Hilbert–Schmidt. To prove density let \(c\in\ell^2\) annihilate its range. The adjoint \(\sum c_nr_n(t)\) vanishes a.e. on (0,T). Its slow sum converges absolutely and locally uniformly on the complex plane because \(\sum |c_n|/b_n^2<\infty\), and the fast sum is holomorphic on \(\Re t>0\), by Cauchy–Schwarz and Gaussian frequency growth. Thus the sum vanishes for all positive t by the identity theorem. Its Laplace transform for real \(z>\delta_1\) is
\[\sum_n c_n\left[\frac1{z+b_n}+\frac{d/b_n^2}{z-\delta_n}\right].\]
Termwise integration is justified by \(\sum|c_n|/b_n<\infty\). The series converges normally off its poles and the finite accumulation point 0: on compact subsets the fast denominators gain \(b_n^{-1}\), and slow coefficients gain \(b_n^{-2}\). The complement is connected. Analytic continuation makes the function zero there. Each \(-b_n\) is an isolated distinct fast pole, whose residue is \(c_n\), so every \(c_n=0\). Hence \(\ker\mathsf D^*=0\) and \(\overline{\operatorname{ran}\mathsf D}=\ell^2\). A compact operator between infinite-dimensional Hilbert spaces cannot have closed infinite-dimensional range; the dense range is therefore nonclosed, so this is not a Fredholm problem.

The space \(C_c^\infty(0,T)\) is dense in H. To see the exact correction/endpoint domain is dense, take a smooth compact k, let \(v=(I+\mathsf T)^{-1}k\), and correct the scalar \(v(T)\) using k-bumps supported in intervals of width \(\epsilon\) near T with unit value at T. Their H norms tend to zero; since \(\mathsf T(I+\mathsf T)^{-1}\) is a bounded H-to-\(C[0,T]\) smoothing map, the corresponding v(T) tends to 1, allowing normalization. These bumps vanish near 0, so flatness remains. Thus the exact domain in (8) of the operator report is H-dense, and its image is dense by continuity of \(\mathsf B=\mathsf D(I+\mathsf T)^{-1}\). This conclusion is density in **moment-sequence space**, not physical joint-state reachability or kernel injectivity. ∎

## Theorem 2: unconditional fast-Laplace incompleteness

For every \(0<a<b<T\), there are infinitely many linearly independent real \(k\in C_c^\infty(a,b)\) with \(\int_0^T e^{-b_nt}k(t)dt=0\) for all n.

*Proof.* The full Müntz theorem away from the origin (Almira, [arXiv:0710.3570](https://arxiv.org/html/0710.3570), Theorem 29) states that distinct real exponents \(\lambda_n\) yield a dense power span in \(C[\alpha,\beta]\), \(0<\alpha<\beta\), iff \(\sum_{\lambda_n\ne0}1/|\lambda_n|=\infty\). Here \(\lambda_n=b_n\asymp n^2\), so the series converges. Under \(x=e^{-t}\), on any strictly smaller interval of (a,b), Hahn–Banach and Riesz provide a nonzero finite real signed measure whose Laplace transform vanishes at every \(b_n\). Convolve this measure with a nonzero \(C_c^\infty\) bump supported sufficiently near 0; the resulting nonzero smooth function remains supported in (a,b), and its Laplace values are products with the zero measure values. Nonzeroness follows because Fourier transforms of nonzero compactly supported distributions are nonzero entire functions, whose product cannot vanish identically. Repeating the construction on countably many disjoint subintervals gives independent functions. ∎

This theorem concerns the **fast-only** map, not \(\mathsf B\): the analytic tail term remains coupled to k through \((I+\mathsf T)^{-1}\), and may change the kernel. In particular, choosing \(k\) from this fast-only nullspace does not solve the paired moments.

## Theorem 3: quasianalytic uniqueness

Let \(\mathcal Q\) be a real vector space of smooth functions on [0,T] with the property that any member flat at 0 vanishes identically on [0,T], and suppose \(\mathcal Q\) contains every restriction of an entire function of exponential type at most \(\mu\). If \(f\in\mathcal Q\), \(f(0)=f(T)=0\), and its paired moments vanish, then \(f=0\). This includes any concrete quasianalytic Denjoy–Carleman vector class satisfying these two stated properties; no unverified criterion for its weight sequence is invoked.

*Proof.* The prior jet theorem shows that the Borel jet extension g of f is entire of type at most \(\mu\), belongs to \(\mathcal Q\), and \(h=f-g\) is flat at 0. Since h lies in \(\mathcal Q\), h=0 on [0,T]. The exact tail equation (4) gives \(\int_T^\infty e^{-x_nt}g(t)dt=0\) for all n. If g were not zero, its first nonzero derivative at T gives a nonvanishing leading Watson term for all large \(x_n\), contradiction. Thus g=f=0. ∎

This extends analytic-control uniqueness but not all smooth or nonquasianalytic Gevrey classes: compactly supported smooth flat functions already show quasianalyticity fails there. There is no theorem here that Gevrey regularity of order \(>1\) is sufficient for a nonzero exact solution.

For the fast term in (6), divide each constructed smooth function by t; its support is bounded away from 0, so it remains smooth and satisfies \(\int_0^T t e^{-b_nt}k(t)dt=0\) for all n. Such k are flat at 0, but generally fail the tail equation and endpoint condition.
