# Sign-changing no-gap moment problem: exact consequences and analytic uniqueness

## Decision

**STRONG PARTIAL THEOREM ESTABLISHED, FULL PROBLEM OPEN.** A genuinely sign-changing, no-gap analytic-control uniqueness theorem is proved below. For arbitrary smooth nonanalytic controls, we prove the full endpoint-jet hierarchy, exponential bounds on every jet, an exact infinite memory-tail consequence, and a bounded-cost obstruction for finite-sine targets. These results do not establish uniqueness or existence for the requested full \(C^\infty\) class. All are linear odd results; same-agent auditing is not independent human verification. Priority remains unverified.

## 1. Model and modal formulas

Let \(q_n=2\pi n/L\), \(c_L=\sqrt{2/L}\), \(A_n=(\kappa q_n^2-B)/M\), \(d=d_0=\gamma S/M>0\), \(C_n=2\kappa c_Lq_n/M\). The constant input matrix is
\[D_n=\begin{pmatrix}-A_n&S/M\\\gamma&-\mu\end{pmatrix}.\]
Its characteristic polynomial is \((z+A_n)(z+\mu)-d\). Evaluating it at \(-\mu\) gives \(-d\), while the physical relation \(\mu B+\gamma S=0\) gives positive product \(\mu\kappa q_n^2/M\); hence \(\lambda_{n,-}<-\mu<\lambda_{n,+}<0\). Let \(\delta_n=\lambda_{n,+}+\mu>0\), \(b_n=-\lambda_{n,-}-\mu>0\). Then \(\delta_nb_n=d\), \(\Delta_n=\delta_n+b_n\), \(b_n\sim\kappa q_n^2/M\), \(\delta_n\sim dM/(\kappa q_n^2)\).

Variation of constants from zero yields \((y_n(0),p_n(0))^T=C_n\int_0^T e^{tD_n}(1,0)^Tf(t)dt\), \(f(t)=a(-t)\). Spectral projectors give first column \(\Delta_n^{-1}(\delta_ne^{\lambda_+t}+b_ne^{\lambda_-t},\gamma(e^{\lambda_+t}-e^{\lambda_-t}))^T\). Therefore, with entire \(F(z)=\int_0^T e^{zt}f(t)dt\),
\[y_n(0)=\frac{C_n}{\Delta_n}[\delta_nF(-\mu+\delta_n)+b_nF(-\mu-b_n)],\quad p_n(0)=\frac{C_n\gamma}{\Delta_n}[F(-\mu+\delta_n)-F(-\mu-b_n)].\tag{1}\]
The boundary factor follows from \(Y(0)\phi_n'(0)-Y(L)\phi_n'(L)=2a c_Lq_n\). For smooth \(H^1_0\)-compatible controls, a homogeneous Dirichlet lift justifies the terminal \(L^2\) field and these coefficients. For mere \(L^1\) controls we use only the individual moment formula; a general \(L^2\) full terminal trace is not assumed.

## 2. The entire function and complete endpoint-jet hierarchy

For \(f\in L^1(0,T)\), \(|F(z)|\le\|f\|_1 e^{T\max(\Re z,0)}\), and \(F^{(k)}(z)=\int_0^T t^ke^{zt}f(t)dt\). Thus F is entire of exponential type at most T with Paley–Wiener support restrictions; the type bound by itself does not make the paired constraints a uniqueness set.

If \(f\in C^\infty([0,T])\), Taylor's theorem at 0 and splitting the Laplace integral yield, for every integer \(N\ge0\),
\[F(-x)=\sum_{j=0}^{N} f^{(j)}(0)x^{-j-1}+O(x^{-N-2}),\quad x\to\infty.\tag{2}\]
The remainder is uniform on the positive real axis for sufficiently large x; the endpoint T gives an exponentially small contribution. Assume \(f(0)=0\) and \(y_n(0)=0\). With \(w=\delta_n\), \(b_n=d/w\), the moment equation is
\[F(-\mu-d/w)=-\frac{w^2}{d}F(-\mu+w).\tag{3}\]
Substitute (2), take arbitrarily high finite orders, and compare coefficients: any first nonzero Taylor coefficient of the difference would dominate along the infinite sequence \(w=\delta_n\downarrow0\). Set \(\xi=w/(d+\mu w)\), equivalently \(w=d\xi/(1-\mu\xi)\). It follows, as a formal power-series identity,
\[\sum_{j\ge0} f^{(j)}(0)\xi^{j+1}=-\frac{d\xi^2}{(1-\mu\xi)^2}F\left(-\mu+\frac{d\xi}{1-\mu\xi}\right)=:J(\xi).\tag{4}\]
The right side is analytic for \(|\xi|<1/\mu\). Cauchy's bound gives \(|f^{(j)}(0)|\le C_RR^{-j-1}\) for every \(R<1/\mu\). In particular
\[f'(0)=-dF(-\mu),\quad f''(0)=-d[2\mu F(-\mu)+dF'(-\mu)].\tag{5}\]
This determines **all** jets from weighted moments; it does not imply f is analytic, because nonzero flat perturbations can have the same jet.

## 3. Analytic no-gap uniqueness theorem

Assume f is real analytic on an open neighborhood of \([0,T]\), has \(f(0)=f(T)=0\), and satisfies every moment. The exponential jet bound makes
\[g(t)=\sum_{j\ge0}f^{(j)}(0)t^j/j!\]
entire, with \(|g(t)|\le C_RR^{-1}e^{|t|/R}\). Since f is real analytic on the connected interval, the real-analytic identity theorem gives \(f=g\) on \([0,T]\). For \(x>1/R\), absolute convergence and termwise integration give
\[\int_0^\infty e^{-xt}g(t)dt=\sum_{j\ge0}f^{(j)}(0)x^{-j-1}=J(1/x).\tag{6}\]
By (4), for \(x_n=\mu+b_n\),
\[J(1/x_n)=-\frac d{b_n^2}F(-\mu+d/b_n)=F(-x_n),\tag{7}\]
where the last equality is exactly (3). Since \(f=g\) on \([0,T]\), (6)–(7) imply
\[\int_T^\infty e^{-x_nt}g(t)dt=0\quad\text{for all sufficiently large }n.\tag{8}\]
If entire g were nonzero, let k be the first index with \(g^{(k)}(T)\ne0\). Its Laplace tail has the asymptotic
\[\int_T^\infty e^{-xt}g(t)dt=e^{-xT}[g^{(k)}(T)x^{-k-1}+O(x^{-k-2})],\quad x\to\infty,\]
using local Taylor expansion and the exponential growth bound for the remote tail. This is nonzero for all sufficiently large x, contradicting (8). Therefore \(g=f=0\). This proof uses sign changes freely and does not assume a gap or terminal flatness. It relies essentially on analyticity **throughout the interval**; merely analytic near t=0 leaves a possible smooth deviation elsewhere.

## 4. Terminal memory: exact result for any no-gap control

If \(y_n(0)=p_n(0)=0\), (1)'s two independent equations imply \(F(-\mu+\delta_n)=F(-\mu-b_n)=0\). If this happens for infinitely many n, the distinct slow roots accumulate at \(-\mu\), so the identity theorem gives \(F\equiv0\), and Laplace/Fourier uniqueness gives \(f=0\). Thus a nonzero nulling control necessarily yields nonzero memory in all but finitely many modes; exact zero memory and every nonzero finite-sine target are ruled out, independently of any smoothness or sign assumption.

Under the thermal moments, simplify (1) to
\[p_n(0)=\frac{C_n\gamma}{b_n}F(-\mu+\delta_n).\tag{9}\]
If j is the first nonzero derivative of smooth f at 0, the fast expansion in (3) yields \(F(-\mu+w)\sim-f^{(j)}(0)w^{j-1}/d^j\) along \(w=\delta_n\). Since F is analytic, this is also its exact leading Taylor order. Therefore the tail is exactly as stated in theorem 4 of `THEOREM_STATEMENTS.md`. The established flat theorem excludes a nonzero smooth solution with all derivatives zero; a hypothetical nonzero solution must possess a finite first nonzero jet and the displayed polynomial memory tail.

## 5. Bounded-cost approximate preparation

For \(U=L^2(0,T)\), each temperature moment functional in (1) is bounded on U, whether or not a particular control has a full \(L^2\) terminal trace. The full memory map \(\mathcal K:U\to H_o\) is Hilbert–Schmidt: \(|C_n/\Delta_n|=O(1/q_n)\), both exponentials are uniformly bounded on \([0,T]\), and \(\sum q_n^{-2}<\infty\).

Let \(h\ne0\) have infinitely many zero sine coefficients, including every nonzero \(h\in V_N\). Suppose \(f_j\) is bounded in U, \(\mathcal Kf_j\to h\), and the terminal temperatures tend to 0 in \(L^2\). A weakly convergent subsequence has limit f. Compactness gives \(\mathcal Kf=h\); boundedness of each coefficient functional gives all terminal temperature moments of f equal 0. Section 4 then forces f=0, contradiction. Therefore no such bounded sequence exists and, for each finite R, the constrained joint squared-error infimum is strictly positive. Gap controls, a subset of no-gap controls, have dense joint range by the previous report's signed-synthesis proof, so the infimum tends to zero as R tends to infinity. This conclusion applies to the class of no-gap controls with a meaningful \(L^2\) terminal temperature, and is conditional only where it invokes prior gap joint density. It proves no finite-R lower bound formula, nor a physical small-amplitude preparation theorem. For an infinite-support h the analogous obstruction remains open, because exact nulling with such h is not excluded.

## 6. Four proof routes, including failures

**A. Endpoint jets and analytic continuation (success in analytic class).** Derive (4), continue the jet to the entire g, identify g with f throughout the interval via real analyticity, then use the positive-real Laplace tail in (8). This fails for general smooth f: a smooth flat correction can share every derivative at 0 without being zero elsewhere. No unjustified quasianalytic conclusion is drawn.

**B. Flat and sign cone estimates (known partial).** For flat controls fast moments are superalgebraic; accumulation forces F to vanish to all orders. For one-sign f, the first temperature kernel is strictly positive. Both arguments fail for finite nonzero jets with sign changes: (5) allows cancellation.

**C. Canonical-product/Paley–Wiener interpolation (unresolved).** The exact two-branch condition prescribes nonzero coupled values rather than zeros at the accumulating slow points. A canonical product vanishing at fast points alone cannot enforce the slow constraints without also forcing F=0. The fast frequencies grow quadratically, so standard Müntz completeness is not available as a shortcut. No supported entire function satisfying all paired conditions has been constructed.

**D. Compactness and duality (partial).** Hilbert–Schmidt memory map plus weak compactness excludes bounded-cost approximation of finite-sine targets. The kernel \(\ker\mathcal A\) for general no-gap inputs is not characterized, and an \(L^2\) boundary input has no automatic strong terminal temperature. A finite numerical nullspace is not a proof of an infinite nullspace.

**E. Formal construction through a flat correction (unresolved).** Equation (4) defines an entire jet extension g. For real-analytic f on all of \([0,T]\), g=f and the analytic theorem applies. For a general smooth f, \(h=f-g\) is flat at 0 but need not vanish. The formal condition equates its fast Laplace samples to a tail of g, while g itself depends on F of f. No convergent construction solves this coupled interpolation; assuming h=0 would be circular.

## 7. Full control and nonlinear consequence

The full first variation has \(\mathcal M=cI+d_{phys}\theta_*Q\), \(\mathcal M Y_s=\kappa Y_{xx}+BQY+SP-b\theta_*m'\), \(P_s=-\mu P+\gamma QY\), \(V_s=\lambda(m-V)\). Spatial reflection leaves odd and even sectors invariant: scalar \(m\) and symmetric baths are even, hence cannot change these odd moment equations. This says nothing conclusive about nonzero even/mean memory with thermal nulling. Nonlinear even–odd products can generate odd second variations, but controlled nonlinear well-posedness, differentiability and a singular endpoint existence/no-go theorem remain unproved. There is no nonlinear physical preparation or inverse theorem.

## 8. Numerical adversarial investigation

`code/sign-changing-nogap/study.py` computes synthetic finite-dimensional fits in three endpoint-compatible bases, with the actual quadrature \(L^2\) Gram metric, modes 5, 10, 20, 40 and 80 with 600 vs 1200 Gauss points, plus N=160 with 1200 vs 2400 points, ten withheld modes, and stable slow-root evaluation. The output `diagnostic.csv` reports rank, singular values, conditioning, Gram norm, endpoint derivative, truncated memory norm and residuals. For the analytic sine basis with N=5, fitting produces unit first-memory coefficient, \(L^2\) norm about 4.785, fit residual about \(4.4\times10^{-16}\), yet withheld-mode temperature residual about \(2.5\times10^{-8}\). An independent 60-digit sine-transform calculation confirms that withheld residual. At larger N, numerical ranks fall well below the number of constraints and apparent condition numbers exceed \(10^{16}\); quadrature discrepancy can exceed the fit residual. Some fitted polynomial controls have small residuals at further finite modes, but no candidate was verified in the infinite system. No analytic fit can exactly satisfy all moments by section 3. These computations neither construct a counterexample nor prove smooth uniqueness. At N=160 the numerical rank is only 14–27 of 161 rows, and withheld residuals and quadrature differences are at comparable scales; it is not a precision-converged N=160 study. These are not material measurements, PDE simulations, or verified optimal controls.

## 9. Literature and audit

See `LITERATURE_PRIORITY.md` for the primary-source theorem/proof comparisons and `PROOF_AUDIT.md` for the same-agent adversarial check. Prior art on heat-memory non-controllability and interpolation is substantial; the precise analytic-control theorem has not been subjected to an exhaustive novelty search or independent expert review. No publication-ready claim is made. The next exact problem is to prove or disprove the existence of a smooth nonanalytic flat correction that solves the paired interpolation while satisfying the jet identity (4).

## 10. Constructive counterexample to sufficiency of the entire jet hierarchy

The infinite jet identity is a strong necessary condition, but even all of it is not enough to prove uniqueness. We construct infinitely many smooth endpoint-compatible sign-changing nonflat functions that satisfy it exactly; they are **not** asserted to solve the discrete moment equations.

Define the entire symmetric kernel
\[H(t,s)=\sum_{k=0}^\infty\frac{(dts)^k}{k!(k+1)!},\qquad 0\le s,t\le T,\]
and let \(\mathsf T\) act on the real Hilbert space \(L^2((0,T),s\,ds)\) by
\[(\mathsf T v)(t)=d\int_0^T H(t,s)v(s)s\,ds.\tag{10}\]
It is Hilbert–Schmidt, self-adjoint and nonnegative: for real v,
\[\langle\mathsf T v,v\rangle=d\sum_{k\ge0}\frac{d^k}{k!(k+1)!}\left(\int_0^T s^{k+1}v(s)ds\right)^2\ge0.\]
Consequently \(I+\mathsf T\) is boundedly invertible (indeed coercive). Choose any nonzero \(h\in C_c^\infty((0,T))\), put \(v=(I+\mathsf T)^{-1}h\), and set
\[f(t)=e^{\mu t}t\,v(t).\tag{11}\]
Since \(\mathsf T v\) is entire in t by locally uniform convergence and \(v=h-\mathsf T v\), v and f are smooth; f is analytic near t=0. For this f, define the entire function
\[g(t)=-d e^{\mu t}t\int_0^T e^{-\mu s}f(s)H(t,s)ds=-e^{\mu t}t(\mathsf T v)(t).\tag{12}\]
Hence \(f-g=e^{\mu t}t h(t)\), which vanishes on a neighborhood of 0. For \(x>\mu\), termwise integration gives
\[\int_0^\infty e^{-xt}g(t)dt=-\frac{d}{(x-\mu)^2}F\!\left(-\mu+\frac d{x-\mu}\right)=J(1/x).\tag{13}\]
Both sides are absolutely convergent: the series is positive-term dominated after absolute values and factorials control the entire kernel. Equating large-x expansions proves that every derivative of f at 0 equals the corresponding derivative of g, and hence the formal jet identity (4) is satisfied. This shows the jet condition alone is compatible with smooth nonzero inputs.

Finally impose \(f(T)=0\) and \(\int_0^T f(t)dt=0\). These are two linear conditions on the infinite-dimensional space \(C_c^\infty((0,T))\) of h; their common kernel is infinite-dimensional. The injectivity of \(I+\mathsf T\) ensures each nonzero h gives nonzero f. A real continuous nonzero function of zero integral changes sign. Moreover f is **not flat** at 0: if it were, v would be flat there, so \(\mathsf T v=h-v\) would be an entire function flat at 0, hence identically zero. The quadratic expansion above would then imply \(\int s^{k+1}v(s)ds=0\) for all k; polynomial density in \(L^2(s\,ds)\) gives v=0 and h=0, a contradiction. Thus an infinite-dimensional family of smooth, endpoint-compatible, sign-changing, nonflat controls satisfies every jet constraint. Their exact paired spectral moments have **not** been shown to vanish; in fact a compactly supported h does not imply f has a terminal switch-off gap. This is an explicit obstruction to completing the main theorem through endpoint jets alone.

## 11. Other regularity classes and limitations

For \(C^1\) endpoint-compatible f, the first part of (5), \(f'(0)=-dF(-\mu)\), follows from the first-order Laplace expansion. For \(C^2\), the second identity follows as well. For real-analytic controls on the whole interval, uniqueness follows from §3; for flat smooth and sign-definite integrable controls, prior results apply. Nonflat Gevrey, smooth nonanalytic, piecewise smooth, \(H^1_0\), \(H^2\), and arbitrary \(L^2\) sign-changing kernels are not settled here. The jet construction even gives analytic-near-both-endpoints examples satisfying every necessary jet identity but not known to satisfy exact moments. Endpoint traces for \(H^1_0\) are meaningful; an \(L^2\)-time boundary input need not have a strong terminal \(L^2\) temperature, so individual coefficient equations or a specified weaker transposition topology must be used.

No true 6–10-hour execution, complete literature survey, independent human audit, certified high-precision large-N solve, nonlinear well-posedness theorem, or completed manuscript was achieved. The end result is an interim partial theorem, not a solution of the full user-requested problem.
