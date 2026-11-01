# An Infinite-Dimensional Smooth Kernel for an Exact Coupled Exponential Moment Operator

*Research manuscript for independent review; not a submission-ready priority claim.*

## Abstract

We consider a coupled exponential moment operator whose rows combine a rapidly decaying exponential with a slow analytic exponential. A positive Bessel-kernel operator transforms this problem into a fast Laplace transform plus a dependent analytic tail. For positive rates \(b_n\asymp n^2\) satisfying a uniform positive square-root gap, we construct, on every compactly contained interior time interval, an infinite-dimensional real space of smooth compactly supported corrections satisfying every coupled moment and an endpoint condition. The construction uses a biorthogonal estimate, Müntz incompleteness, and a Fredholm finite-codimension argument; it is exact and functional analytic, not a numerical limiting construction. We derive its conditional interpretation for a frozen linear odd heat–memory model and identify the corresponding terminal-memory coefficients. No nonlinear preparation or full-system inverse result follows.

## 1. Introduction

Paired moments occur when a two-component linear mode has one rapidly decaying and one slowly accumulating spectral branch. The zero-temperature condition couples their Laplace values: the slow contribution is not independently prescribed data. The fast exponentials alone are incomplete under a summable reciprocal-rate condition, but this does not by itself settle completeness of the coupled rows. Likewise, density of the range of a moment operator is not injectivity of that operator.

We establish an infinite-dimensional smooth nullspace for a specific coupled operator. The mechanism is the time separation between an interior-support fast transform and a tail starting at the terminal point. A biorthogonal family solves fast moment problems for exponentially decaying sequences; the dependent tail is compact into the required weighted sequence space. A Fredholm intersection with the infinite-dimensional fast-only nullspace gives exact solutions, and one further scalar constraint fixes the endpoint. This argument neither assumes that the compact perturbation is small nor treats the tail as arbitrary.

Our inputs include Cannarsa, Martinez and Vancostenoble [1], whose biorthogonal estimate concerns fast exponential families, and Almira's exposition of the Müntz theorem [2], which concerns the uncoupled exponential family. Guerrero and Imanuvilov [3] study noncontrollability for a heat equation with memory and some nonzero initial states; their target and initial-state question differ from the zero-start paired moments below. A related rest-controllability paper by Ivanov and Pandolfi is cited in [3]; its original proof was not accessible for this comparison. These observations do not establish chronological novelty or exhaust the literature.

## 2. Formulation and main theorem

Fix \(T,d,\mu>0\), and a strictly increasing positive sequence \((b_n)\) satisfying
\[b_n\asymp n^2,\qquad \inf_n(\sqrt{b_{n+1}}-\sqrt{b_n})>0.\tag{2.1}\]
The second assumption is separate: the asymptotic order alone does not exclude clustered pairs. Set \(\delta_n=d/b_n\) and \(H=L^2((0,T),t\,dt)\), over the reals. Define
\[H_d(t,s)=\sum_{j=0}^\infty\frac{(dts)^j}{j!(j+1)!},\qquad
(\mathsf Tv)(t)=d\int_0^T H_d(t,s)v(s)s\,ds.\tag{2.2}\]
The series is entire in t and bounded on \([0,T]^2\). Thus \(\mathsf T\) is compact and self-adjoint. Moreover
\[\langle\mathsf Tv,v\rangle_H=d\sum_{j=0}^\infty\frac{d^j}{j!(j+1)!}\left(\int_0^T s^{j+1}v(s)ds\right)^2\ge0.\tag{2.3}\]
Consequently \(Q=(I+\mathsf T)^{-1}\) exists on H, with \(\|Q\|\le1\). The extension \(\mathsf Tv\) in (2.2) is entire for every \(v\in H\). For smooth k, \(v=Qk=k-\mathsf Tv\) is smooth on \([0,T]\). The correction map is
\[(\mathsf Bk)_n=\int_0^T t e^{-b_nt}k(t)dt+
\int_T^\infty t e^{-b_nt}(\mathsf TQk)(t)dt.\tag{2.4}\]
The second term is a dependent tail; it is not free interpolation data. Define
\[\mathcal K_{\rm adm}=\{k\in C^\infty[0,T]:k^{(j)}(0)=0\ (j\ge0),\ (Qk)(T)=0\}.\tag{2.5}\]

**Theorem 2.1.** Under (2.1), for every open interval \(I\) with \(\overline I\subset(0,T)\),
\[\{k\in C_c^\infty(I):\mathsf Bk=0,\ (Qk)(T)=0\}\tag{2.6}\]
is an infinite-dimensional real vector space. In particular \(\ker(\mathsf B|_{\mathcal K_{\rm adm}})\) is infinite-dimensional.

The proof uses [1, Theorem 2.1] and [2, Theorem 29] as external inputs. It constructs solutions through exact operators and finite-dimensional algebraic choices; it does not provide decimal-valued closed-form controls.

## 3. Proof of Theorem 2.1

### 3.1. Spectral gap and a positive-exponential family

The abstract hypotheses are precisely (2.1). In the modal application in §4, the positive root of \(b_n-d/b_n=A_n-\mu\) has the form \(b_n=\alpha n^2+\beta+O(n^{-2})\), \(\alpha>0\), and is strictly increasing; hence its square-root gaps tend to \(\sqrt\alpha>0\), and their global infimum is positive.

Choose \(a,\ell,\varepsilon>0\) with \([a,a+\ell+\varepsilon]\subset I\), and \(\eta>0\) with \(a+\varepsilon<T-\eta\). For any \(\ell>0\), [1, Theorem 2.1] supplies real \(\sigma_n\in L^2(0,\ell)\) such that
\[\int_0^\ell e^{b_m u}\sigma_n(u)du=\delta_{mn},\qquad
\|\sigma_n\|_2\le C e^{-\ell b_n+C\sqrt{b_n}}.\tag{3.1}\]
Indeed, if \(g_0\) is the lower gap in (2.1), take the source's global gap parameter \(g_0/2\), asymptotic parameter \(g_0\), and \(N_*=1\). Here \(\delta_{mn}\) is the Kronecker symbol. Its \(M_*=0\), and its remaining factor is uniformly bounded because \(b_1>0\). Real parts may be taken if necessary.

### 3.2. Reverse, shift, smooth, and interpolate

Let \(p_n(u)=e^{\ell b_n}\sigma_n(\ell-u)\) on \((0,\ell)\), extended by zero. Substitution shows
\[\int e^{-b_m u}p_n(u)du=\delta_{mn},\qquad \|p_n\|_2\le C e^{C\sqrt{b_n}}.\tag{3.2}\]
Choose nonzero \(\rho\in C_c^\infty(0,\varepsilon)\), \(\rho\ge0\), and put \(\rho_n=\int e^{-b_nu}\rho(u)du\). Define
\[\psi_n(t)=\frac{e^{ab_n}}{t\rho_n}\,[p_n(\cdot-a)*\rho](t).\tag{3.3}\]
All \(\psi_n\) have a common compact support in I. Laplace convolution and (3.2) give
\[\int_I t e^{-b_mt}\psi_n(t)dt=\delta_{mn}.\tag{3.4}\]
Also \(\rho_n\ge e^{-\varepsilon b_n}\int\rho>0\); Cauchy–Schwarz for convolution and Leibniz' rule give, for each j,
\[\|\psi_n\|_{C^j}\le C_j e^{(a+\varepsilon)b_n+C\sqrt{b_n}}.\tag{3.5}\]
Let \(X=L^2(I,t\,dt)\), extend its elements by zero to H, and let
\[Y=\{y:\|y\|_Y^2=\sum_n e^{2(T-\eta)b_n}|y_n|^2<\infty\},\quad
(Ex)_n=\int_I t e^{-b_nt}x(t)dt.\tag{3.6}\]
E is bounded X→ℓ². For \(y\in Y\) set \(Sy=\sum_n y_n\psi_n\). By (3.5) and Cauchy–Schwarz, the j-th derivative series is absolutely uniformly convergent, since
\[\sum_ne^{-2(T-\eta-a-\varepsilon)b_n+2C\sqrt{b_n}}<\infty.\tag{3.7}\]
Thus \(S:Y\to X\) is bounded and \(Sy\in C_c^\infty(I)\), with convergence in every \(C^j\). Equation (3.4) gives \(ESy=y\) coordinatewise. This is a right inverse only on Y, not a claim about arbitrary ℓ² data.

### 3.3. Tail compactness

For \(x\in X\), define
\[(Rx)_n=\int_T^\infty t e^{-b_nt}(\mathsf TQx)(t)dt.\tag{3.8}\]
The Bessel series gives, for \(t\ge T\),
\[|(\mathsf TQx)(t)|\le C e^{2\sqrt{dTt}}\|x\|_X.\tag{3.9}\]
Since \(b_n\ge b_1>0\), \(|(Rx)_n|\le C e^{-Tb_n}\|x\|_X\). The squared norms of the weighted coordinate functionals are bounded by \(C^2e^{-2\eta b_n}\), a summable sequence. Hence \(R:X\to Y\) is Hilbert–Schmidt, \(SR:X\to X\) is compact, and
\[A=I_X+SR\tag{3.10}\]
is Fredholm with closed finite-codimension range [4]. No invertibility or Neumann-series assumption on A is made.

### 3.4. Fast-null seeds and exact preimages

Because \(\sum 1/b_n<\infty\), [2, Theorem 29] and \(x=e^{-t}\) show that \(\{e^{-b_nt}\}\) is not dense in C on any interval strictly inside I. Hahn–Banach and the Riesz representation theorem [5] give a nonzero finite real signed measure annihilating the entire family. Convolution with a nonzero compact smooth bump preserves all moments and is nonzero: the Fourier transforms of the two compactly supported factors are nonzero entire functions, so their product cannot vanish identically. Dividing by t is smooth on I. Repeating on pairwise disjoint subintervals gives infinitely many independent elements of
\[N=\{h\in C_c^\infty(I):Eh=0\}.\tag{3.11}\]
Since \(\operatorname{ran}A\) is closed and has finite codimension, \(N\cap\operatorname{ran}A\) is infinite-dimensional. Select independent \(h_i\) in this intersection, and solve \(Ax_i=h_i\). Then
\[x_i=h_i-SRx_i\in C_c^\infty(I),\qquad Ex_i=-ESRx_i=-Rx_i.\tag{3.12}\]
The first identity is in X and gives a smooth representative because the right side is smooth; the series converges in every \(C^j\). The second holds for every n, because \(Rx_i\in Y\) and \(ES=I_Y\). The \(x_i\) are independent since their A-images are independent. No truncated system is used.

### 3.5. Endpoint constraint

For arbitrary \(x\in X\), ordinary point evaluation in H is not defined. Since x is zero a.e. near T, \(Qx=-\mathsf TQx\) there in the canonical smooth representative. Define
\[L(x)=-d\int_0^T H_d(T,s)(Qx)(s)s\,ds.\tag{3.13}\]
The kernel row belongs to H, so L is bounded on X. For smooth x, \(L(x)=(Qx)(T)\). Restriction of one linear functional to the infinite-dimensional span of the \(x_i\) has a kernel of codimension at most one. Every element of that kernel satisfies all equations in (2.6). This proves Theorem 2.1. ∎

## 4. Conditional linear odd-model interpretation

Assume a frozen linear odd heat–memory system with \(M,\kappa,L,\mu>0\), \(d=\gamma S/M>0\), zero initial odd fields at time \(-T\), opposite boundary inputs \(Y(0,s)=a(s)\), \(Y(L,s)=-a(s)\), and smooth compatible boundary lift. Let \(f(t)=a(-t)\). On odd modes \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(q_n=2\pi n/L\), write
\[D_n=\begin{pmatrix}-A_n&S/M\\\gamma&-\mu\end{pmatrix},\quad
A_n=(\kappa q_n^2-B_0)/M,\quad C_n=2\kappa\sqrt{2/L}\,q_n/M.\tag{4.1}\]
Here the frozen PDE is \(M Y_s=\kappa Y_{xx}+B_0Y+SP\), \(P_s=-\mu P+\gamma Y\). Integration by parts gives boundary input \(C_na(s)\). Its eigenvalues are \(-\mu+\delta_n\), \(-\mu-b_n\), with \(\delta_nb_n=d\), and the positive branch b satisfies (2.1), as noted in §3.1. The physical relation \(\mu B_0+\gamma S=0\) ensures negative roots; the abstract theorem does not require this extra relation.

For \(F(z)=\int_0^T e^{zt}f(t)dt\), zero-start Duhamel and the spectral projectors yield
\[Y_n(0)=\frac{C_n}{b_n+\delta_n}[\delta_nF(-\mu+\delta_n)+b_nF(-\mu-b_n)],\quad
P_n(0)=\frac{C_n\gamma}{b_n+\delta_n}[F(-\mu+\delta_n)-F(-\mu-b_n)].\tag{4.2}\]
If \(v=Qk\) and \(f=e^{\mu t}t v\), direct termwise integration of (2.2) gives
\[\int_0^\infty t e^{-bt}H_d(t,s)dt=b^{-2}e^{ds/b},\quad b>0.\tag{4.3}\]
It follows that
\[(\mathsf Bk)_n=\int_0^T t v(t)\left[e^{-b_nt}+d b_n^{-2}e^{\delta_nt}\right]dt,\quad
Y_n(0)=\frac{C_n b_n}{b_n+\delta_n}(\mathsf Bk)_n.\tag{4.4}\]
All integral interchanges follow from the factorial kernel series and the bound (3.9). Thus each k in (2.6) has zero odd terminal-temperature coefficients and \(f(0)=f(T)=0\). Under the smooth boundary-lift solution framework these coefficients represent the terminal odd \(L^2\) field. Under nulling, (4.2) reduces to the separate memory formula
\[P_n(0)=\frac{C_n\gamma}{b_n}\int_0^T t e^{\delta_nt}v(t)dt.\tag{4.5}\]
The framework does not assert terminal \(L^2\) temperature for arbitrary \(L^2\) boundary inputs.

## 5. Consequences and limitations

For a nonzero real solution, the weight in (4.4) is strictly positive, so v and f change sign. Since k vanishes near 0, \(v=-\mathsf Tv\) there. If f vanished on a terminal-time neighborhood, the entire function \(\mathsf Tv\) would vanish identically. Equation (2.3) and density of polynomials in H would give \(v=0\), a contradiction. The same relation makes f analytic near both endpoints, but f cannot be real analytic on a connected neighborhood of \([0,T]\): otherwise k would be analytic there and vanish identically because it is zero near 0.

The entire function \(G(z)=\int_0^T t e^{zt}v(t)dt\) is nonzero for nonzero v by polynomial density. Its zeros cannot accumulate at 0; since \(\delta_n\to0\), (4.5) shows that all but finitely many memory coefficients are nonzero. No prescribed Gevrey order, numerical closed form, quantitative control cost, nonlinear preparation theorem, or full-system non-identifiability follows. The theorem's proof and its source applications have been audited only by the same agent; independent mathematical and physical-model review, and chronological priority assessment, remain necessary.

## References

[1] P. Cannarsa, P. Martinez, J. Vancostenoble, “Precise estimates for biorthogonal families under asymptotic gap conditions,” *Discrete and Continuous Dynamical Systems – S* **13** (2020), 1441–1472, [doi:10.3934/dcdss.2020082](https://www.aimsciences.org/article/doi/10.3934/dcdss.2020082); [arXiv version, Theorem 2.1](https://arxiv.org/html/1706.02435#S2.ThmTheorem1).

[2] J. M. Almira, “Müntz type theorems I,” *Surveys in Approximation Theory* **3** (2007), 152–194, [arXiv:0710.3570, Theorem 29](https://arxiv.org/html/0710.3570#Thmtheorem29).

[3] S. Guerrero, O. Yu. Imanuvilov, “Remarks on non controllability of the heat equation with memory,” *ESAIM: Control, Optimisation and Calculus of Variations* **19** (2013), 288–300, [doi:10.1051/cocv/2012013](https://www.numdam.org/articles/10.1051/cocv/2012013/).

[4] P. Howard, “Second Order Elliptic PDE: The Fredholm Alternative, I,” MATH 612 notes, Texas A&M University (2020), [Theorem A.D.5](https://people.tamu.edu/~phoward/m612/s20/elliptic4.pdf).

[5] “Riesz Representation Theorem,” NYU lecture notes, [first page](https://math.nyu.edu/~varadhan/real17/Part8.pdf); Hahn–Banach is used in its standard separation form.
