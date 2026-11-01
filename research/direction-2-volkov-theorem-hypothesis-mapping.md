# Volkov hypothesis mapping and fractional alternative

## 1. The primary theorem, exactly

Darko Volkov, [*Optimal decay rates in Sobolev norms for singular values of integral operators*, arXiv:2309.00153v2](https://arxiv.org/html/2309.00153), Theorem 1.1, §4.2 proof, (30)–(33), and Appendix A.1 were inspected. The full text and the relevant proof passage are accessible and were inspected; this is a mathematical mapping, not a claim of independent external certification. The theorem assumes a bounded Lipschitz input domain \(\Omega\subset\mathbb R^d\), an open output domain \(\Omega'\subset\mathbb R^{d'}\), and a real kernel \(k\in L^2(\Omega';H^p(\Omega))\) for an integer \(p\ge1\). It defines
\[
K:L^2(\Omega)\to L^2(\Omega'),\quad Kf(z)=\int_\Omega k(z,x)f(x)dx.
\]
\(H^p\) is ordinary Sobolev space: the required source derivatives are **weak** \(L^2\) derivatives, not classical derivatives, and no zero Dirichlet endpoint or Neumann condition on the kernel is assumed. The source domain is Lipschitz; the target here is the interval \(J\). With \(d=p=1\), the theorem states
\[
\sum_{n\ge1}n^2s_n(K)^2<\infty,\qquad s_n(K)=o(n^{-3/2}). \tag{1}
\]
The proof removes the constant input (finite codimension), uses a Neumann inverse-Laplacian factorization with derivative kernels and singular-value product inequalities, then uses Hilbert–Schmidt summability. The displayed limit is stronger than a generic compactness estimate. This is not a theorem about injectivity.

## 2. Map every hypothesis to the actual odd kernel

Let \(I=(0,L)\), \(J=(\delta,T)\), \(H_o=L^2_o(I)\), \(a,\ell,K,R\) and \(\rho_n\) be as in `direction-2-observation-kernel-regularity-audit.md`. The actual operator is initially defined only on \(H_o\); extend it canonically to all \(L^2(I)\) by composition with odd projection \(\Pi_o\). Its kernel is the unique source-odd \(K\), and its nonzero singular values are exactly those of \(\mathcal T:H_o\to L^2(J)\). Similarly extend the remainder by zero on the even subspace. This is an operator-theoretic extension, not a change to the physical system.

| Volkov hypothesis | Actual status |
|---|---|
| Input bounded Lipschitz domain | \(I=(0,L)\), **verified**. |
| Open output domain | \(J=(\delta,T)\), **verified**. |
| Actual integral operator | The PDE-defined \(\mathcal T\) is Hilbert–Schmidt and has canonical odd \(K\in L^2(J\times I)\); \(R=K-a\ell\) is also \(L^2\), **verified**. |
| Source weak derivative \(\partial_xR\in L^2(J\times I)\) | Equivalent to the actual square sum \(\sum q_n^2\|\rho_n\|^2<\infty\), because \(R\) has zero endpoint trace. **Not verified** under the stipulated base regularity, and not disproved. |
| Ordinary \(H^1\), no artificial trace | Canonical \(a\ell\in L^2(J;H^1(I))\) even though \(\ell(0),\ell(L)\ne0\). The actual remainder happens to have zero source trace, but Volkov does not require it. |
| Rank-one operator | \(a\ell\) itself has ordinary \(H^1\) source regularity; subtraction is useful but not mathematically required if \(K\in H^1\). Since \(a\ell\in H^1\), \(R\in H^1\iff K\in H^1\). |
| Physical parameter/data status | All conclusions use inherited symbolic small-load assumptions; no experimental constants or measured active coefficient fields were provided. |

Thus the specific hoped-for application is **not yet justified**. If an actual weak derivative in the missing row is established, Volkov immediately yields (1) for the zero-extended remainder. With \(Fh=a(\ell,h)\), the finite-rank inequality
\[
s_{n+1}(\mathcal T)\le s_n(R),\qquad s_{n+1}(R)\le s_n(\mathcal T), \tag{2}
\]
shows that \(\sum n^2s_n(\mathcal T)^2<\infty\) as well as \(s_n(\mathcal T)=o(n^{-3/2})\). The finite rank shifts the comparison index by one, though it can change every singular value; it does not change this tail order; no lower or asymptotic-equivalence claim follows. The weighted sum and monotonicity imply little-o directly: \(n^3s_n^2\le C\sum_{k=\lfloor n/2\rfloor}^{n}k^2s_k^2\to0\). The existing theorem already proves the same little-o bound by column-block approximation, but it has **not** proved the weighted singular-value sum.

Under the additional hypothesis \(S\in H^{2+\eta}(Q_T)\), \(0<\eta\le1\), the approximation-cost criterion in the kernel report §3 yields \(R\in L^2(J;H^1_0)\), and this mapping is valid. It is a stronger **conditional** theorem: the actual \(S\) has only the inherited anisotropic \(\mathcal A\) regularity established. Alternatively, the dyadic approximation condition (12) in that report suffices. Neither is silently added to the physical model.

## 3. Fractional-kernel route: proven but weaker exponent

For every \(0<s<1\), the kernel report proves the actual weighted estimate
\[
\sum_{n\ge1}q_n^{2s}\|\rho_n\|_{L^2(J)}^2<\infty. \tag{3}
\]
Let \(D_s\phi_n=q_n^{-s}\phi_n\), and define the operator \(B_s\phi_n=q_n^s\rho_n\). Equation (3) says \(B_s:H_o\to L^2(J)\) is Hilbert–Schmidt. Hence the actual remainder factors exactly as
\[
\mathcal R=B_sD_s,\qquad s_n(D_s)=q_n^{-s}\asymp n^{-s}. \tag{4}
\]
The singular-value product inequality gives \(s_{2n-1}(\mathcal R)\le s_n(B_s)s_n(D_s)\). Pairing odd and even indices and summing yields
\[
\sum_{n\ge1}n^{2s}s_n(\mathcal R)^2<\infty,\qquad
s_n(\mathcal R)=o(n^{-s-1/2})\quad(0<s<1). \tag{5}
\]
The same tail estimate holds for \(\mathcal T\) after the rank-one index shift. It is an actual PDE-derived fractional kernel consequence, but for every fixed \(s<1\) it is **weaker** than the already proved \(o(n^{-3/2})\). It does not give the missing \(s=1\) sum by taking \(s\uparrow1\): constants may diverge.

For an original fractional/operator theorem, Delgado–Ruzhansky, [*Schatten-von Neumann classes of integral operators*, arXiv:1709.06446](https://arxiv.org/html/1709.06446), Theorem 2.2(iii), §2 proof (2.4), was inspected. It assumes an \(L^2\) kernel, an invertible source operator \(E\) with \(E^{-1}\in\mathcal S_p\), and \(E_xk\in L^2\); it proves \(T\in\mathcal S_r\) whenever \(1/r\le1/2+1/p\). Its proof factors a Hilbert–Schmidt differentiated-kernel operator with \(E^{-1}\). On \(H_o\), choose \(E\phi_n=q_n^s\phi_n\), so (3) verifies its differentiated-kernel assumption and \(E^{-1}\in\mathcal S_p\) for \(p>1/s\). To apply the theorem literally on full \(L^2(I)\), extend \(E\) diagonally by any invertible Dirichlet spectral operator of order \(s\) on the even complement; the canonical odd kernel has zero even coefficients. Thus \(\mathcal R\in\mathcal S_r\) for every \(r>1/(s+1/2)\). This is consistent with, and weaker in detail than, (5); taking \(s<1\) gives the familiar \(r>2/3\), not the strong endpoint. The proof of (5) is included above rather than attributing its weighted-sum conclusion to Delgado–Ruzhansky.

## 4. Comparison levels and a logical counterexample

1. The physical result is the **column-wise** \(\rho_n=o(q_n^{-3/2})\), which gives (3) for every \(s<1\) and the independent sharp-exponent little-o singular bound by the previous dyadic proof.
2. The stronger Hilbert–Schmidt statement \(\sum q_n^2\|\rho_n\|^2<\infty\) is exactly the zero-trace source \(H^1\) kernel statement here, not yet proved.
3. Weighted singular-value summability \(\sum n^2s_n(\mathcal R)^2<\infty\) follows from level 2 or Volkov, but is distinct from level 2 and not a substitute for source-variable derivative regularity.

The abstract diagonal kernel with columns \(n^{-3/2}/\sqrt{\log(n+1)}\) times orthonormal output functions satisfies level 1 and every fractional (3), but fails level 2 and the weighted singular-value sum. It is fully specified in the kernel report and is **not** an admissible-coefficient or physical counterexample. A nonzero-boundary affine kernel separately shows why one cannot identify ordinary \(H^1\) with the Dirichlet weighted sine sum until the boundary trace has been removed. For the actual \(R\), the trace removal has been proved.

## 5. Conclusion

Volkov is a decisive prior general theorem **if** its source-\(H^1\) hypothesis is independently proved. At present neither that hypothesis nor its failure has been established for the actual base. Conditional stronger regularity subsumes the singular-value result via Volkov, but the frozen experiment has not been shown to satisfy that additional regularity. No priority claim, strong \(\mathcal S_{2/3}\), or initial-memory injectivity follows.
