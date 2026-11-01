# Local nonlinear identification on a fixed finite spectral prior

## Theorem and assumptions

Under all assumptions and the explicit nonzero-load condition of `direction-2-finite-prior-independent-proof-audit.md`, fix \(N\ge1\) and \(V_N=\operatorname{span}\{\sqrt{2/L}\sin(2\pi nx/L):1\le n\le N\}\). Let \(\mathcal F(h)\) be the actual nonlinear **labeled outward heat-flux difference** on \(J=(\delta,T)\), where the initial internal state is \(h\in H^2(I)\), the original prescribed loading is unchanged, and the weak-initial solution is the positive solution of the frozen full nonlinear equations in `direction-2-active-base-existence-and-regularity.md` §1. Set \(\mathcal N(h)=\mathcal F(h)-\mathcal F(0)\); its derivative on odd directions is \(L_N=\mathcal T|_{V_N}\).

The inherited §6 proves that \(\mathcal N\) is \(C^2\) on an \(H^2(I)\) ball \(B_{H^2}(0,r_0)\), containing only admissible weak-initial data with positive temperature and a unique solution throughout \([0,T]\). We explicitly use this \(C^2\) statement, not just a pointwise quadratic remainder. For the fixed active nonzero load, there exist \(K_2<\infty\) and \(r_1\in(0,r_0)\) such that
\[\sup_{\|h\|_{H^2}<r_1}\|D^2\mathcal N(h)\|_{\mathcal L^2(H^2,L^2(J))}\le K_2.\]
Existence of such a bound follows by continuity at zero after shrinking the ball; a numerical value is not supplied. Let \(K_N=(1+q_N^2+q_N^4)^{1/2}\) for the standard sum-of-derivatives \(H^2\) norm. For a different equivalent \(H^2\) convention choose any known embedding constant \(K_N\ge\sup_{v\ne0,v\in V_N}\|v\|_{H^2}/\|v\|_2\).

For every
\[
0<r_N<\min\{r_1,\sigma_N/(4K_2K_N)\},
\]
with the second restriction omitted if \(K_2=0\), the actual flux difference satisfies for all \(h_1,h_2\in V_N\) with \(\|h_i\|_{H^2}<r_N\),
\[
\boxed{\quad\|\mathcal F(h_1)-\mathcal F(h_2)\|_{L^2(J)}\ge\frac{\sigma_N}{4}\|h_1-h_2\|_{L^2(I)}.\quad} \tag{1}
\]
In particular \(\mathcal F\) is injective on this ball. The \(K_2\)-dependent radius is a positive existence radius, not a numerically verified or material-only threshold. \(N\), the actual load and data can affect it; no uniform-in-\(N\) radius is claimed.

## Construction and proof

By the audited linear theorem \(\|L_Nv\|_{L^2(J)}\ge(\sigma_N/2)\|v\|_{L^2(I)}\). Thus \(L_N:V_N\to R_N:=L_N(V_N)\) is a linear isomorphism between finite-dimensional spaces, and \(R_N\) is closed in \(L^2(J)\). Let \(\Pi_{R_N}\) be the orthogonal projection onto this **actual**, not reference, response range. It has norm one. Equip \(V_N\) with either \(L^2\) or \(H^2\) norm; finite dimensionality makes these equivalent. Define
\[
\mathcal G_N(h)=L_N^{-1}\Pi_{R_N}\mathcal N(h),\qquad h\in V_N,\ \|h\|_{H^2}<r_1.
\]
The inverse is bounded (\(\|L_N^{-1}\|\le2/\sigma_N\) in \(L^2\) norms). The map is \(C^2\), and for every \(v\in V_N\), \(D\mathcal G_N(0)v=L_N^{-1}\Pi_{R_N}L_Nv=v\). The finite-dimensional inverse function theorem therefore yields open neighborhoods of zero on which \(\mathcal G_N\) is a bijection with a \(C^1\) inverse. If two full observations coincide, their projected observations and hence their \(\mathcal G_N\) values coincide, proving local injection. The projection discards information but cannot create a false separation when full data agree.

A quantitative two-point proof gives (1) on an explicit ball in terms of the derivative bound. Put \(v=h_1-h_2\) and \(h_s=h_2+sv\); the \(H^2\)-ball is convex. The fundamental theorem of calculus in \(L^2(J)\) gives
\[
\mathcal N(h_1)-\mathcal N(h_2)-L_Nv=\int_0^1[D\mathcal N(h_s)-D\mathcal N(0)]v\,ds.
\]
The second-derivative bound and norm equivalence yield
\[
\|[D\mathcal N(h_s)-D\mathcal N(0)]v\|\le K_2\|h_s\|_{H^2}\|v\|_{H^2}\le K_2r_NK_N\|v\|_2\le(\sigma_N/4)\|v\|_2.
\]
Subtract this from the linear lower bound \((\sigma_N/2)\|v\|_2\), proving (1). The same estimate also holds with the left side replaced by the norm of its \(\Pi_{R_N}\) projection, since \(\Pi_{R_N}L_Nv=L_Nv\). Only \(N\) scalar inner products against an orthonormal basis of \(R_N\) are needed mathematically; calculating those exact actual responses is a separate practical inverse problem.

The single-point estimate \(\|\mathcal N(h)-L_Nh\|=O(\|h\|_{H^2}^2)\) at the base alone would not control \(\mathcal N(h_1)-\mathcal N(h_2)\) by \(\|h_1-h_2\|\). The proof explicitly uses \(C^2\) continuity to obtain the derivative estimate. All states evolve from time zero, not from \(\delta\); positivity and admissibility follow from the inherited actual weak-initial contraction, not from a reference approximation. The result is on an open relative ball of the prescribed odd \(H^2\) state class; it does not assert unproved corner-classical compatibility.

## Scope ledger

| Assertion | Status |
|---|---|
| Linear injectivity/stability on fixed \(V_N\) | PROVED conditionally on the inherited base and the audited small nonzero-load threshold. |
| Local nonlinear injectivity on fixed \(V_N\) | PROVED under the same hypotheses plus inherited \(C^2\) map. |
| Local nonlinear \(L^2\)-Lipschitz inverse on \(V_N\) | PROVED with constant \(4/\sigma_N\) on the displayed relative ball. |
| Linear injectivity on all odd \(L^2\) or \(H^2\) | UNRESOLVED. |
| Nonlinear injectivity on an infinite-dimensional neighborhood | UNRESOLVED. |

This is a standard finite-dimensional inverse argument applied to a model-specific linear lower bound; it is not by itself a new continuum theory or a demonstrated publication-level innovation. The finite-dimensional radius and Gram can deteriorate severely as \(N\to\infty\). Self-review by Arena is not independent human certification.
