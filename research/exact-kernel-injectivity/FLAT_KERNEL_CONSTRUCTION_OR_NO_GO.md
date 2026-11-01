# Constructive Fredholm–biorthogonal kernel theorem

## Theorem (nontrivial admissible kernel; source theorem used explicitly)

Let \(T,d,\mu>0\). Let \(b_1<b_2<\cdots\), \(b_n>0\), satisfy both \(b_n\asymp n^2\) and the uniform square-root gap \(\inf_n(\sqrt{b_{n+1}}-\sqrt{b_n})>0\). Let \(\mathsf T\), \(\mathsf B\), and \(\mathcal K_{\rm adm}\) be exactly as in `../smooth-nonanalytic-investigation/EXACT_FLAT_CORRECTION_OPERATOR.md`. For every open interval \(I\) with \(\overline I\subset(0,T)\), there is an **infinite-dimensional real vector space** of \(k\in C_c^\infty(I)\) satisfying \(\mathsf Bk=0\) and \(((I+\mathsf T)^{-1}k)(T)=0\). Thus each such k belongs to \(\mathcal K_{\rm adm}\). The assumption \(b_n\asymp n^2\) alone does not imply the gap condition; both are stated deliberately.

For the frozen physical odd spectrum, \(b_n\) is the positive root of \(b_n-d/b_n=A_n-\mu\), \(A_n=(\kappa q_n^2-B_0)/M\), \(q_n=2\pi n/L\), with \(M,\kappa,L,d>0\). Thus \(b_n=\alpha n^2+\beta+O(n^{-2})\), \(\alpha=\kappa(2\pi/L)^2/M>0\), and \(\sqrt{b_{n+1}}-\sqrt{b_n}\to\sqrt\alpha\). The positive root is strictly increasing in \(A_n\), so the finite initial gaps are also positive; the theorem applies without changing the spectrum.

## Step 1: a smooth fast-moment right inverse on interior support

Pick \(a,\ell,\epsilon>0\) such that \([a,a+\ell+\epsilon]\subset I\), and choose \(\eta>0\) with \(a+\epsilon<T-\eta\). Theorem 2.1 of Cannarsa–Martinez–Vancostenoble, [arXiv:1706.02435](https://arxiv.org/html/1706.02435), gives, for the **positive** exponentials \(e^{b_nt}\) on \((0,\ell)\), real \(\sigma_n\in L^2(0,\ell)\) biorthogonal to them and
\[\|\sigma_n\|_2\le C e^{-\ell b_n+C\sqrt{b_n}}.\tag{1}\]
The source assumes a global positive square-root gap and a positive asymptotic gap; the stated global gap supplies both (choose a smaller global constant). Its remaining bound is uniformly bounded for fixed positive \(b_1\), \(\ell\), and gap constants. The source's positive exponent convention is important.

Set \(\phi_n^0(t)=e^{b_n\ell}\sigma_n(\ell-t)\) on \((0,\ell)\), zero elsewhere. Then \(\int e^{-b_m t}\phi_n^0(t)dt=\delta_{mn}\) and \(\|\phi_n^0\|_2\le C e^{C\sqrt{b_n}}\). Shift by a and multiply by \(e^{ab_n}\). Choose a nonnegative, nonzero \(\rho\in C_c^\infty(0,\epsilon)\) and put \(\rho_n=\int e^{-b_nu}\rho(u)du\). Define
\[\psi_n(t)=\frac{e^{ab_n}}{t\rho_n}\bigl[\phi_n^0(\cdot-a)*\rho\bigr](t).\tag{2}\]
Then \(\psi_n\in C_c^\infty(I)\), all supports lie in one compact subinterval of I, and
\[\int_I t e^{-b_mt}\psi_n(t)dt=\delta_{mn}.\tag{3}\]
Because \(\rho_n\ge c e^{-\epsilon b_n}\), convolution with a fixed smooth function and division by t yield, for every integer \(j\ge0\),
\[\|\psi_n\|_{C^j}\le C_j e^{(a+\epsilon)b_n+C\sqrt{b_n}}.\tag{4}\]
This smoothing is essential: the original source only gives L² functions.

Let \(X=L^2(I,t\,dt)\), with elements extended by zero to \((0,T)\), and let
\[Y=\{y:\sum_n e^{2(T-\eta)b_n}|y_n|^2<\infty\},\quad
(Ek)_n=\int_I t e^{-b_nt}k(t)dt.\tag{5}\]
Define \(Sy=\sum_n y_n\psi_n\). Cauchy–Schwarz and (4) show absolute convergence in **every** \(C^j\) norm with a common compact support in I, so \(S:Y\to X\) is bounded and maps into \(C_c^\infty(I)\). Because \(a+\epsilon<T-\eta\) and \(b_n\asymp n^2\), the required series of bounds converges. Termwise integration in (3) gives
\[ES=I_Y.\tag{6}\]
The codomain of E is taken as ordinary \(\ell^2\); equation (6) uses the embedding \(Y\subset\ell^2\). We do **not** assert that E has a bounded right inverse on all of \(\ell^2\).

## Step 2: the coupled tail is small in an exponentially weighted sequence space

For k in X let \(v=(I+\mathsf T)^{-1}k\) in \(H=L^2((0,T),t\,dt)\), and define
\[(Rk)_n=\int_T^\infty t e^{-b_nt}(\mathsf Tv)(t)dt.\tag{7}\]
For real \(t\ge T\), the factorial Bessel series and Cauchy–Schwarz give
\[|\mathsf Tv(t)|\le C\|k\|_X e^{2\sqrt{dTt}}.\tag{8}\]
Since \(b_n\ge b_1>0\), (8) implies \(|(Rk)_n|\le C e^{-Tb_n}\|k\|_X\). Hence \(R:X\to Y\) is bounded, indeed Hilbert–Schmidt: \(\sum_n e^{-2\eta b_n}<\infty\). Let
\[A=I_X+SR:X\to X.\tag{9}\]
Then \(SR\) is compact. The Fredholm alternative gives \(\operatorname{ran}A\) closed of finite codimension and \(\ker A^*\) finite-dimensional. No assumption that \(A\) is invertible, or that a small-norm Neumann series exists, is made.

## Step 3: finite-codimension correction, convergence and endpoint

The fast-only nullspace \(N=\{h\in C_c^\infty(I):Eh=0\}\) is infinite-dimensional: on infinitely many disjoint subintervals, the full Müntz theorem away from 0 gives a nonzero annihilating finite measure for \(e^{-b_nt}\); convolution with a compact smooth bump preserves all moments, and division by t produces elements of N. Here \(\sum1/b_n<\infty\). A product of two nonzero entire Fourier transforms cannot vanish identically, so the convolution is nonzero.

Write \(m=\dim\ker A^*\), select a real basis \(w_1,\ldots,w_m\), and choose \(m+2\) linearly independent real \(h_j\in N\). The \(m\times(m+2)\) matrix \((\langle h_j,w_i\rangle_X)\) has at least two independent null vectors. Their two linear combinations \(h^{(1)},h^{(2)}\) are independent and lie in \(N\cap(\ker A^*)^\perp=N\cap\operatorname{ran}A\). Let \(x^{(i)}\) be the unique solution of \(Ax^{(i)}=h^{(i)}\) orthogonal to \(\ker A\); the inverse on that complement is bounded by the bounded inverse theorem. Then
\[x^{(i)}=h^{(i)}-SRx^{(i)}\in C_c^\infty(I),\quad
Ex^{(i)}=-ESRx^{(i)}=-Rx^{(i)}.\tag{10}\]
The second equality is exact in \(\ell^2\); hence every \(\mathsf Bx^{(i)}=(E+R)x^{(i)}=0\). The two \(x^{(i)}\) are independent because their A-images are independent. The endpoint map
\[L(x)=\bigl[(I+\mathsf T)^{-1}x\bigr](T)\tag{11}\]
is a well-defined real linear functional on \(C_c^\infty(I)\), explicitly \(L(x)=-[\mathsf T(I+\mathsf T)^{-1}x](T)\); it is in fact bounded on X by smoothing. If both \(L(x^{(i)})=0\), choose \(k=x^{(1)}\); otherwise choose the nonzero combination
\[k=L(x^{(2)})x^{(1)}-L(x^{(1)})x^{(2)}.\tag{12}\]
This gives a **specified functional-analytic construction**: it uses finite-dimensional nullspaces and the Fredholm inverse, not a finite-mode approximation. Replace m+2 by m+r+1 to see that the endpoint-constrained kernel is infinite-dimensional. Since k is compactly supported inside I, it is smooth and flat at zero. Its infinite series in (10) converges in every C^j norm by Step 1. Equations (6), (10) hold for every n, and (12) enforces the exact endpoint. Nonzero follows from independence. ∎

## Control properties and actual memory

Set \(f(t)=e^{\mu t}t v(t)\). It is real smooth, \(f(0)=f(T)=0\), and all paired temperature moments vanish by the exact equivalence in the earlier report. Each row in (5) of that report is strictly positive, so a nonzero real v cannot keep one sign on (0,T): f changes sign. Because k vanishes near 0, \(v=-\mathsf Tv\) there, and \(\mathsf Tv\) is entire. If f vanished on an initial terminal-time interval, analyticity would give \(\mathsf Tv=0\) everywhere; positivity of \(\mathsf T\) and polynomial density imply \(v=0\), then \(k=0\), contradiction. Thus f has no terminal switch-off gap. If f were analytic on a neighborhood of [0,T], k would be analytic there, yet k vanishes on an open interval and is nonzero; contradiction.

For the frozen odd model, \(C_n=2\kappa\sqrt{2/L}\,q_n/M\), \(\delta_n=d/b_n\). The exact terminal memory is calculated by
\[P_n(0)=\frac{C_n\gamma}{b_n}\int_0^T t e^{\delta_nt}v(t)dt
=\frac{C_n\gamma}{b_n}\sum_{j=0}^\infty\frac{\delta_n^j}{j!}\int_0^T t^{j+1}v(t)dt.\tag{13}\]
The series converges absolutely. The entire function in (13) is not identically zero: otherwise all moments vanish and polynomial density gives v=0. Thus, if \(j_*\) is its first nonzero Taylor index,
\[P_n(0)\sim \frac{C_n\gamma}{b_n}\frac{d^{j_*}}{j_*!\,b_n^{j_*}}\int_0^T t^{j_*+1}v(t)dt.\tag{14}\]
Consequently all but finitely many memory modes are nonzero. Formula (13) calculates the coefficients in terms of the constructed Fredholm solution; numerical values cannot be supplied without specifying physical parameters and the nonunique choices in (2), (12).

This is an exact statement about the specified linear odd moment system, not a nonlinear physical preparation, experiment, full-system counterexample, or publication-priority claim. The proof is a same-agent derivation using the cited biorthogonal theorem; independent expert verification is still necessary.
