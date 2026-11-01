# Exponential completeness and the decisive distinction

Let \(H=L^2((0,T),t\,dt)\) and \(r_n(t)=e^{-b_nt}+d b_n^{-2}e^{dt/b_n}\). The exact row identity is
\[\mathsf Bk=\mathsf D(I+\mathsf T)^{-1}k,\qquad (\mathsf Dv)_n=\langle v,r_n\rangle_H.\]
Therefore \(\{r_n\}\) is complete in H iff \(\mathsf D\) is injective iff the bounded extension of \(\mathsf B\) to H is injective. Completeness would imply injectivity on the smaller smooth flat endpoint class; the converse need not hold in general.

Under the spectral gap and frozen-spectrum assumptions verified in `FLAT_KERNEL_CONSTRUCTION_OR_NO_GO.md`, that report constructs nonzero smooth admissible k. Thus \(\mathsf Dv=0\) for \(v=(I+\mathsf T)^{-1}k\ne0\); the perturbed rows are **incomplete in H**. In fact their orthogonal complement contains the injective images of an infinite-dimensional admissible k-space. Unlike a numerical rank assertion, this follows from exact fast moment interpolation and the Fredholm finite-codimension construction.

The fast rows alone are incomplete by the full Müntz theorem away from zero, but this does not by itself imply the coupled claim: no nonzero exact k can annihilate the fast *correction* transform at infinitely many nodes, by (5) in `FUNCTION_SPACE_AND_REGULARITY_THEOREMS.md`. The decisive added fact is not small operator norm. It is that the coupled tail lies in an exponentially weighted sequence space for which the incomplete fast operator has a smooth supported right inverse; its composition with that tail is compact. Fredholm finite codimension then leaves an infinite-dimensional intersection with the fast-only smooth nullspace.

For direct v, the slow expansion is
\[d b_n^{-2}\int_0^T t v(t)e^{dt/b_n}dt
=\sum_{j\ge0}\frac{d^{j+1}}{j!b_n^{j+2}}\int_0^T t^{j+1}v(t)dt.\]
The series converges for each n. The first fast term cancels the entire series at the exact sample nodes; it is not legitimate to set the series coefficients separately to zero. Indeed the constructed nonzero v provides an exact witness that such coefficientwise vanishing would be false. In contrast, if both the direct fast transform and the full row vanish on infinitely many n, the slow entire transform vanishes at \(d/b_n\to0\) and hence v=0. This is not contradicted by our construction: the two terms cancel rather than vanish separately.
