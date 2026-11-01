# Alternative distributed memory: finite-spatial-mode reachable injectivity

**Status: CONDITIONALLY PROVED** under the exact alternative model and hypotheses below, subject to an independent human audit. This is a restricted mathematical result, not a theorem for the frozen Direction 2 model, not a physical experiment, and not a novelty claim.

## Statement

Let \(0<a<b\), \(\kappa>0\), \(\gamma\ne0\), and \(I=(0,L)\). Consider the PDE–ODE system of `autonomous-five-candidate-discovery-audit.md` §6 with zero initial temperature and initial memory \(h\). Assume \(h(x,r)=\sum_{n\in E}h_n(r)\phi_n(x)\), where \(E\) is a finite set of distinct positive integers, \(\phi_n=\sqrt{2/L}\sin(n\pi x/L)\), and every \(h_n\) has a holomorphic extension to a complex neighborhood of the whole interval \([a,b]\). This includes the finite-spatial-mode part of the common \(L^2\) history range, but also a larger analytic class. If \(u_x(0,t)=0\) on any nonempty open time interval in \((0,\infty)\), then \(h=0\).

## Proof

The finite-mode evolution is closed. The generator on \(\oplus_{n\in E}(\mathbb C\oplus L^2(a,b))\) is bounded, so the scalar output \(u_x(0,t)\) is entire in \(t\); vanishing on an interval gives vanishing for all positive \(t\). For \(\operatorname{Re}z\) sufficiently large, Laplace transformation of the complete initial-value system yields
\[
U_n(z)=\frac{H_n(z)}{D_n(z)},\quad H_n(z)=\int_a^b\frac{h_n(r)}{z+r}dr,\quad D_n(z)=z+\lambda_n-\gamma F(z),\quad F(z)=\int_a^b\frac{dr}{z+r},\quad \lambda_n=\kappa(n\pi/L)^2,
\]
and \(\sum_{n\in E}c_nU_n(z)=0\), where \(c_n=\phi_n'(0)\ne0\). The identity continues meromorphically to \(\mathbb C\setminus[-b,-a]\); this domain is connected, and all denominators differ by nonzero constants \(\lambda_n-\lambda_m\).

Near \(z=-a\), put \(w=z+a\), choose a branch of \(\log w\), and write
\[
F=A(z)-\log w,\quad H_n=B_n(z)-q_n(z)\log w,\quad q_n(z)=h_n(-z),
\quad B_n(z)=q_n(z)A(z)+\int_a^b\frac{h_n(r)-q_n(z)}{z+r}dr.
\]
Here \(A(z)=\log(z+b)\) and \(A,B_n,q_n\) are holomorphic in a sufficiently small disk around \(-a\): the divided difference is holomorphic there because \(h_n\) extends through the compact interval. Define \(d_n=z+\lambda_n-\gamma A\). Multiplying the output identity by all denominators gives a polynomial identity in \(\log w\) with holomorphic coefficients:
\[
\sum_n c_n(B_n-q_n\log w)\prod_{m\ne n}(d_m+\gamma\log w)=0.
\]
All its coefficients vanish. Indeed analytic continuation around \(w=0\) changes \(\log w\) by \(2\pi i k\) for every integer \(k\), while all coefficients return to their original values; at each fixed \(w\ne0\) the polynomial has infinitely many roots. Substituting the formal value \(-d_j/\gamma\) and using \(c_j\ne0\), \(d_m-d_j=\lambda_m-\lambda_j\ne0\), yields
\[B_j+q_jd_j/\gamma=0,\qquad H_j=-(q_j/\gamma)D_j\quad\text{near }-a.\tag{1}\]
Consequently \(U_j=-q_j/\gamma\) there and has no branch singularity at the endpoint. The identity theorem extends (1) throughout a connected neighborhood of the cut on which \(h_j(-z)\) is holomorphic, so \(U_j\) continues analytically through the whole cut, including both endpoints. Away from the cut, any pole of \(U_j\) cannot be shared by another \(U_m\), because their denominators differ by a nonzero constant; the zero-output identity therefore removes every such pole. Thus each \(U_j\) is entire. Since \(H_j=O(1/z)\), \(F=O(1/z)\), and \(D_j\sim z\) uniformly as \(|z|\to\infty\), we have \(U_j=O(1/z^2)\); Liouville gives \(U_j=0\). Hence \(H_j=0\), and uniqueness of the compact-interval Cauchy transform gives \(h_j=0\). □

## Adversarial scope checks and obstruction

The proof uses finitely many spatial modes in three essential places: bounded finite-mode generator/output, a finite polynomial in the logarithm, and isolated uncancelled poles. It does **not** imply injectivity for infinitely many modes; an infinite product, uniform continuation, and exchange of sums with endpoint monodromy are unjustified. The finite-mode prior is on the initial state itself, not merely an approximation or each individual column. Coalescence is excluded by distinct Dirichlet eigenvalues. Both signs of \(\gamma\) are allowed. One boundary flux suffices in this restricted class; no stability estimate follows. The common prehistory is a mathematical input class, not automatically the coupled physically admissible past. Finite-time common controls can be dense but are not automatically exactly controllable or mechanically compatible. General reachable injectivity remains **OPEN**.
