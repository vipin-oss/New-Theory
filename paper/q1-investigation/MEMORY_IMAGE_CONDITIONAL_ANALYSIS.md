# Terminal memory map: conditional structural analysis

**Research note, not independently certified; no priority claim.** The following derives consequences of the existing manuscript's theorem and frozen linear odd model. It does not identify the exact reachable set, prove its density, establish physical nonlinear preparation, or prove any new global control theorem. The infinite-dimensionality input remains conditional on the original theorem and its external dependencies. The estimates below do not depend on a numerical truncation.

## Setup

Take the positive modal rates `b_n` from the frozen odd model, `delta_n=d/b_n`, `c_n=C_n gamma/b_n` and `C_n=2 kappa sqrt(2/L) q_n/M`, with `q_n=2 pi n/L`. Then `b_n asymp n²`, `delta_n` are distinct and tend to zero, `gamma != 0` because `d=gamma S/M>0`, and `sum |c_n|² < infinity`. Fix `I` with `closure I` inside `(0,T)`, let `X=L²(I,t dt)` and extend x by zero to `H=L²((0,T),t dt)`. Denote the Bessel operator by `T_hat` and its resolvent by `Q=(Id+T_hat)^-1`. Define

`(D x)_n = integral_0^T t (Qx)(t)[exp(-b_n t)+d b_n^-2 exp(delta_n t)] dt`,

`Lx = -d integral_0^T H_d(T,s)(Qx)(s) s ds`,

and set `K={x in X: Dx=0, Lx=0}`. D is bounded X to l²: the squared H-row norms of `t -> exp(-b_n t)` sum (indeed integral_0^T t exp(-2b_n t) dt <=1/(4b_n²)), and the slow rows have norms bounded by `C b_n^-2`. L is bounded by its H-kernel row and Q. Thus K is a closed real Hilbert subspace. Conditional on the manuscript's existing theorem, it is infinite-dimensional because it contains the constructed independent smooth corrections.

Define `G_x(z)=integral_0^T t exp(z t)(Qx)(t) dt`, and the abstract memory map

`(M x)_n = c_n G_x(delta_n)`.

For *smooth* x in K with the prescribed boundary lift, the manuscript's terminal formula identifies Mx with the zero-temperature terminal odd-memory coefficients. For arbitrary X-elements, M is a bounded abstract extension; no physical boundary-control interpretation is asserted without further admissibility analysis.

## A. Injectivity and a necessary range condition

If Mx=0, then `G_x(delta_n)=0` for all n because `c_n !=0`. The entire function G_x has zeros accumulating at 0, so it vanishes identically. Its derivatives at 0 give `integral t^(j+1)(Qx)(t)dt=0` for every j. Polynomials are dense in H (the finite measure `t dt` on `[0,T]` has continuous functions dense in L² and Weierstrass applies), hence Qx=0 in H and x=0. Therefore M is injective on X and on K. In particular, conditional on dim K=infinity, `M(K)` is infinite-dimensional.

The existing manuscript already proves the stronger fact that every nonzero smooth constructed control has all but finitely many nonzero memory coefficients. The analytic argument extends that observation to all x in X: if Mx has only finitely many nonzero coordinates, `G_x(delta_n)=0` for all sufficiently large n. The same identity theorem yields x=0. Thus

`M(K) intersect c_00 = {0}`.

This is a **necessary exact-range obstruction**: it does not imply that the closure of M(K) excludes `c_00`, nor determine whether M(K) is dense in l². The zero vector has finite support; every nonzero state in this particular exact range has infinitely many nonzero memory coordinates.

## B. Factorial approximation-number upper bound

Define bounded rank-at-most-m operators `M_m` by truncating the Taylor series in the scalar parameter:

`(M_m x)_n = c_n sum_{j=0}^{m-1} delta_n^j/j! integral_0^T t^(j+1)(Qx)(t)dt`.

Let `a=d/b_1`, `C_c=(sum |c_n|²)^(1/2)`, and `h=(integral_0^T t dt)^(1/2)=T/sqrt(2)`. For `0<=delta_n<=a` and `0<=t<=T`, Taylor's remainder satisfies

`|exp(delta_n t)-sum_{j<m}(delta_n t)^j/j!| <= exp(aT)(aT)^m/m!`.

Weighted Cauchy–Schwarz and `||Q||<=1` give

`||M-M_m||_{X -> l²} <= C_c h exp(aT) (aT)^m/m!`.

The same bound applies to the restriction to K. Consequently, for Hilbert-space singular values,

`s_{m+1}(M|_K) <= C_c (T/sqrt(2)) exp(dT/b_1) (dT/b_1)^m/m!`,  `m=0,1,...`.

The result is an **upper bound** based on low-rank approximation, not a matching asymptotic or sharp rate. It is valid for the memory coefficient map with domain norm `||x||_X`; it is not a computed control-cost estimate. The constants also involve the physical coefficients through `C_c` and `b_1`; no uniformity in unknown material parameters is claimed.

## C. Nonclosed exact image and instability

M|K is compact by the operator-norm convergence of M_m (or by the displayed factorial estimate). Since K is infinite-dimensional and M|K is injective, its image cannot be closed: if it were closed, the inverse from its range to K would be bounded by the bounded inverse theorem, making the identity on the infinite-dimensional K compact. Equivalently, there is no constant c>0 such that `||Mx||_l² >= c||x||_X` for all x in K. Thus exact reconstruction in the X-norm from this output has no uniform inverse bound. This does not say the range is all l², dense, physically reachable in a nonlinear system, or that the temperature-null map is noninjective for arbitrary physical histories.

## D. Transfer of the instability to smooth physical boundary controls

This part is still conditional on the frozen linear odd model, the existing theorem and the smooth-lift reconstruction; it does not apply to arbitrary prehistories or nonlinear dynamics. For a smooth x in K let `v=Qx`, `f(t)=exp(mu t)t v(t)` and `a(s)=f(-s)`. Write `alpha=inf I>0`. The forward bound is immediate:

`||f||_L²(0,T) <= exp(mu T) sqrt(T) ||v||_H <= exp(mu T) sqrt(T) ||x||_X`.

There is also a reverse bound for corrections supported in I, not for general v. On I, `||v||_X <= alpha^(-1/2)||f||_2`. Moreover, for `t in I`,

`|(T_hat v)(t)| <= d sup_[0,T]^2 |H_d| integral_0^T s|v(s)|ds <= C ||f||_2`,

because `s v(s)=exp(-mu s) f(s)` and the kernel is bounded on the compact square. Using `x=v+T_hat v` on I gives `||x||_X <= C_I ||f||_2`. Both constants depend on the frozen parameters and I, and no claimed estimate is uniform in them.

Let V be the infinite-dimensional smooth correction subspace supplied by the existing theorem. Gram–Schmidt applied to a countable linearly independent sequence in V gives a sequence `x_j in V` orthonormal in X. Compactness of M yields `||M x_j||_l² -> 0`; the reverse bound gives `||f_j||_2 >= C_I^-1`. Normalize each control by its nonzero L² norm. The normalized controls are smooth and compatible, have unit L² boundary-input norm, and still produce exactly zero terminal temperature. Their terminal-memory norms tend to zero. Thus even restricted to these smooth constructed corrections, there is **no uniform lower estimate of boundary-input L² norm by terminal-memory L² norm**. It is not a nonzero control with exactly zero full terminal state; injection above rules that out for this family. It is not a cost of steering arbitrary initial data, nor an inverse assertion for the active nonlinear model. The manuscript's no-finite-support statement is already present, but this norm comparison and compactness consequence require independent verification and literature comparison before being advertised as new.

## Adversarial checklist and limitations

1. Verify the original infinite-dimensional theorem independently; none of the nonclosed-range conclusion follows without infinite-dimensional K.
2. Check the field reconstruction and the physical control norm. In particular, x is a compactly supported correction, not an arbitrary physical prehistory, and the abstract closure K contains rough elements.
3. Verify that the full odd model's `C_n`, `b_n`, `gamma` are precisely those used in the terminal formula, and distinguish M from the terminal-memory map off the thermal-null subspace.
4. Investigate whether the analytic interpolation constraint is already known, and whether it leads to an exact description of M(K) or a density theorem. Neither has been established here. The factorial bound is not claimed novel or optimal.
5. The separate-agent adversarial review requested by the user has not been performed; this note is a same-agent derivation and is not a paper-ready theorem.
