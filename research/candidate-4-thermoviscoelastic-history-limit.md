# Candidate 4: thermoviscoelastic singular-limit audit

**Question.** Can the precise hereditary plate of [arXiv:0806.0965](https://arxiv.org/html/0806.0965) (1.1) converge uniformly over a full energy ball, including initial histories, on one justified common state space? This model is not Direction 2.

**Primary overlap checked.** The paper rescales \(k_\epsilon(s)=\epsilon^{-1}k(s/\epsilon)\), \(h_\sigma(s)=\sigma^{-1}\tilde h(s/\sigma)\), treats a separately vanishing \(a_\tau\), and works with parameter-dependent phase spaces. Its introduction expressly states regular bounded initial sets and time intervals bounded away from zero; it points to Theorems 4.5 and 4.7 for the distinct estimates. Therefore an unqualified 'initial layer' is not a new discovery. Full theorem hypotheses, lifting maps and norms need line-by-line checking before an exact comparison.

**PROVED elementary obstruction on an explicitly chosen common space, not a plate theorem.** On \(\mathbb R\), \(q_\epsilon'=-q_\epsilon/\epsilon\), \(q_\epsilon(0)=q_0\), define the zero limit embedding \(q_0\mapsto0\). For \(T>0\) and \(0<\epsilon<T\),
\[\sup_{|q_0|\le1}\sup_{0\le t\le T}|q_\epsilon(t)-0|=1,\qquad |q_\epsilon(\epsilon)|=e^{-1}|q_0|.\]
Thus convergence to zero fails uniformly on intervals touching zero, even if \(t=0\) is removed; for each fixed \(\delta>0\), \(\sup_{t\ge\delta}|q_\epsilon(t)|\le e^{-\delta/\epsilon}|q_0|\). This is a fast-mode illustration only. It does not transfer to the plate's norms, its slow mechanical/thermal projections, or a different identification operator. In particular, an \(O(1)\) fast state may produce only \(O(\epsilon)\) accumulated forcing, so the toy result does not refute slow-variable convergence.

**OPEN actual plate:** specify a fixed Hilbert space and bounded identification maps for all history spaces, select compatible initial data, and derive an actual semigroup estimate or a normalized plate-state counterexample under the primary model's assumptions. Compare the exact terms in Theorems 4.5 and 4.7, not only abstracts. No new physical limit theorem is claimed.
