# Exact coupled flat-correction operator

Throughout \(d=d_0>0\), \(T,\mu>0\), \(b_n>0\) strictly increasing, \(\delta_n=d/b_n\), \(x_n=\mu+b_n\), and \(b_n\asymp n^2\). The interval variable is \(t=-s\): t=0 is the physical terminal time. Work in the real Hilbert space \(H=L^2((0,T),t\,dt)\). Define
\[H_d(t,s)=\sum_{k=0}^\infty\frac{(dts)^k}{k!(k+1)!},\quad (\mathsf Tv)(t)=d\int_0^T H_d(t,s)v(s)s\,ds.\tag{1}\]
This entire kernel is symmetric, positive definite and bounded on the square, and \(\mathsf T\) is Hilbert–Schmidt, nonnegative and self-adjoint. Therefore \(I+\mathsf T\) is boundedly invertible on H. It maps \(C^\infty[0,T]\) bijectively to itself: if \(v+\mathsf Tv=k\), then \(v=k-\mathsf Tv\) and \(\mathsf Tv\) is entire. This last statement does not treat endpoint point evaluation as an H-continuous functional.

Given a smooth endpoint-compatible f, \(v=e^{-\mu t}f(t)/t\) extends smoothly to t=0. Its entire Borel jet candidate is
\[g_f(t)=-d e^{\mu t}t\int_0^T e^{-\mu s}f(s)H_d(t,s)ds=-e^{\mu t}t\mathsf Tv(t).\tag{2}\]
Let \(k=(I+\mathsf T)v\) and \(h=f-g_f=e^{\mu t}t k\). Then \(h\) is flat at 0 exactly when k is flat there. The map \(k\mapsto v=(I+\mathsf T)^{-1}k\) makes explicit that g depends on f and on k; no independent tail is chosen. Initial compatibility at physical time \(-T\) is the additional constraint \(v(T)=0\).

For \(x>\mu\), termwise integration yields
\[\int_0^\infty e^{-xt}g_f(t)dt=-\frac{d}{(x-\mu)^2}F\left(-\mu+\frac{d}{x-\mu}\right).\tag{3}\]
Indeed \(\int_0^\infty e^{-bt}tH_d(t,s)dt=b^{-2}e^{ds/b}\) for every \(b>0\). Absolute convergence follows from the factorial series and \(H_d(t,s)\le C e^{2\sqrt{dTt}}\). At \(x_n\) (3) becomes \(-d b_n^{-2}F(-\mu+\delta_n)\). Hence the exact moment equation is **equivalent** to
\[\int_0^T e^{-x_nt}h(t)dt=\int_T^\infty e^{-x_nt}g_f(t)dt,\quad n\ge1.\tag{4}\]
There is no extra factor or sign: the right side is the (possibly signed) tail of g itself.

Dividing both sides by the positive common exponential factors gives the compact operator \(\mathsf D:H\to\ell^2\):
\[(\mathsf Dv)_n=\int_0^T t v(t)\bigl[e^{-b_nt}+d b_n^{-2}e^{d t/b_n}\bigr]dt.\tag{5}\]
For k flat and \(v=(I+\mathsf T)^{-1}k\), the equivalent *flat-correction* residual is
\[(\mathsf Bk)_n=\int_0^T t e^{-b_nt}k(t)dt+\int_T^\infty t e^{-b_nt}(\mathsf Tv)(t)dt=(\mathsf Dv)_n.\tag{6}\]
The plus sign in (6) follows from \(g_f=-e^{\mu t}t\mathsf Tv\). Equation (6) is an exact equation, not merely matching jets.

## Exact kernel characterization

Let \(\mathcal F=\{k\in C^\infty[0,T]:k^{(j)}(0)=0\ \forall j\}\). The map
\[k\longmapsto f_k(t)=e^{\mu t}t(I+\mathsf T)^{-1}k(t)\tag{7}\]
is a linear bijection between
\[\{k\in\mathcal F:\ \mathsf Bk=0,\ ((I+\mathsf T)^{-1}k)(T)=0\}\tag{8}\]
and all smooth endpoint-compatible solutions of the **full infinite paired-moment problem**. Proof: given k in (8), (3)–(6) yield all exact moments, and the endpoint/regularity properties follow from the smooth inverse. Conversely any smooth exact solution has the entire jet identity established in the prior report; comparing the Borel transform with (2) shows \(f-g_f\) is flat at 0, so its k lies in (8). Injectivity of (7) follows from invertibility of \(I+\mathsf T\). A nonzero exact solution cannot be terminal-flat or have a positive gap by the prior theorem, must change sign by positivity of the first heat kernel, and must be nonanalytic on the full interval by the analytic-control theorem. No existence of a nonzero element of (8) is asserted.

Equivalently, flatness may be omitted from the *definition* of the solution set if \(v\in C^\infty\), \(v(T)=0\) and \(\mathsf Dv=0\): the previous jet theorem then forces \((I+\mathsf T)v\) to be flat. This is a rigorous equivalent kernel representation with explicit domain, codomain and endpoint condition, **not** a determination of whether the kernel is trivial.

For each fixed flat smooth k, (6) is a rapidly decreasing sequence: integration against the flat function gives \(O(b_n^{-N})\) for every N, and the tail is \(O(e^{-c b_n})\) for any fixed \(0<c<T\), using the subexponential growth of \(\mathsf Tv\). This necessary decay does not make the range closed or determine the kernel.
