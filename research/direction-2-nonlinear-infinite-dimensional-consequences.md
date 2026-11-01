# Direction 2: nonlinear consequences of possible infinite-dimensional injectivity

**Decision: OPEN** for local injectivity of the actual nonlinear observation map on an infinite-dimensional neighborhood. The derivative \(\mathcal T\) is compact under the inherited kernel estimates. Its injectivity has not been established, and even if it were, derivative injectivity alone would not imply local nonlinear injectivity.

## Exact obstruction to a linear lower bound

For any orthonormal \(h_n\in H_o\), \(h_n\rightharpoonup0\); a compact \(\mathcal T\) satisfies \(\|\mathcal Th_n\|\to0\). Hence no \(c>0\) can make \(\|\mathcal Th\|\ge c\|h\|_2\) for all \(h\in H_o\). Approximate null sequences do not produce an exact nonzero kernel.

## Conditional compact-prior modulus

**CONDITIONALLY PROVED.** Let \(K\) be a compact subset of a metric input space \((X,d)\), and let \(F:K\to Y\) be continuous and injective. Then there exists a modulus \(\omega(\epsilon)\to0\) such that \(d(h_1,h_2)\le\omega(\|F(h_1)-F(h_2)\|_Y)\) for all \(h_1,h_2\in K\). Proof: define \(\omega(\epsilon)\) as the supremum of \(d(h_1,h_2)\) over pairs with output difference at most \(\epsilon\). Compactness of \(K^2\) and continuity imply that if \(\omega(\epsilon_n)\not\to0\) for \(\epsilon_n\downarrow0\), a convergent pair subsequence has equal output but unequal inputs, contradicting injectivity. This theorem gives no explicit rate and does not prove the hypotheses for the actual nonlinear flux map.

A closed \(H^2\) ball is compact in the \(L^2\) topology: boundedness gives relative compactness, and weak \(H^2\) compactness shows its \(L^2\) limit remains in the ball. A general strongly \(H^2\)-closed bounded prior need not itself be \(L^2\)-closed. Applying the lemma requires actual \(L^2\)-continuity and nonlinear injectivity on that prior; neither follows merely from \(C^2\) as a map on an \(H^2\)-open neighborhood. Conditional linear application is possible if \(\mathcal T\) is injective on the compact prior. No logarithmic modulus has been established.

The finite-dimensional local nonlinear theorem remains valid only on each fixed prior \(V_N\), under its \(N\)-dependent threshold and radius. Neither its inverse constant nor its radius is uniform in \(N\). The actual restricted nonlinear \(11/14\) obstruction in the prior audits is inherited, not a general ban on all weaker moduli or a proof of nonuniqueness.
