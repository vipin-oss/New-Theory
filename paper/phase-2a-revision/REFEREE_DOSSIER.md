# Human referee dossier (request; no independent review performed)

The accompanying `main.tex`, `sections/` and `references.bib` are the self-contained draft and proofs. Please derive the modal equation and Bessel transform independently before reading our argument; then examine every displayed equality and functional domain. No author priority or novelty claim is made. Another Claude session is not independent review, and no separate human expert has reviewed these results. This request is not certification.

## Exact external results used

1. **Fattorini–Russell 1974, Theorems 1.2 and 1.5(b), pp. 47–49.** Let F be convex and strictly increasing on [0,infinity), F(0)=0, integral_1^infinity 1/F(v)dv finite, G=F^-1, and G(uv)<=C G(u)G(v). For a positive sequence satisfying G(lambda_1)>=l>0 and G(lambda_{n+1})-G(lambda_n)>=l, a biorthogonal family to exp(-lambda_n t) in L²(0,ell) obeys ||q_n|| <= B exp(K G(lambda_n)), with constants depending on the prescribed class and finite ell. Our specialization F(v)=v² gives G=sqrt, no upper square-root gap needed. Source proof: §§3–5, pp. 52–62; section 5 uses Montel and norm comparison, §4 product estimates. Please verify constants, endpoint conventions and the construction in `biorthogonal_construction.tex`.
2. **Müntz theorem away from zero**, Almira 2007, Theorem 29: for distinct real exponents on [a,b] with 0<a<b, density of their power span in C[a,b] is equivalent to divergence of the sum of 1/|lambda| over nonzero exponents. The present positive rates have a convergent reciprocal sum. Please check this exact form and the sign change z=exp(-t), plus signed-measure/bump nonvanishing.
3. **Fredholm alternative**: if K is compact on a Hilbert space, I+K has closed range of finite codimension. Verify it is used for I+SR (not the original moment map), with actual range intersection, no smallness assumption.
4. Identity theorem for holomorphic functions, density of polynomials in the relevant L² spaces, bounded inverse theorem, and Cauchy–Schwarz.

## Specific review attacks

- Verify boundary integration signs, roots, factors `d/b_n²`, projector constants, reversal and whether f(T)=0 really supplies compatibility. Verify arbitrary admissible smooth h in the implicit exact characterization, not just constructed controls.
- Inspect uniform support and every factor in the right-inverse biorthogonality; ensure R is Hilbert–Schmidt into the stated weighted sequence space and the Fredholm intersection produces infinitely many smooth independent corrections.
- Check no point-evaluation is taken on L², the canonical endpoint representative, and the endpoint functional.
- Verify the full-state uniqueness proposition from the accumulated slow roots, and its attribution to Ivanov–Pandolfi's obstruction mechanism. This is not a nonzero-control claim for full-state zero.
- For the memory image, test the implicit characterization in both directions, the exact versus closure distinction, the asymptotic conditions, zero and nonzero examples, and lower bound in the actual boundary-input L² norm. Check no claim of exponential control cost is being inferred from the fast-only interpolation estimate.
- Independently compare with Ivanov–Pandolfi 2009, Fattorini–Russell 1971/1974, Guerrero–Imanuvilov 2013, Halanay–Pandolfi 2015, Tenenbaum–Tucsnak 2011, partial controllability literature and memory moment literature. Decide whether any theorem or implication is already known, stronger or equivalent, and provide exact citations/pages.
- Assess whether the contribution, with no intrinsic range/closure description or proven novelty, meets a realistic journal's standards; journal indexing/quartile requires current primary verification.

## Open issues

No full novelty clearance, exact sequence-space characterization or density result; no sharp memory control-cost estimate; original source proofs not independently verified line-by-line; no TeX build; author/affiliation confirmation outstanding; no journal selected for submission. All frozen originals remain unchanged. Review findings: **not yet available**.
