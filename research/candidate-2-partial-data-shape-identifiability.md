# Candidate 2: disjoint patches and full-data reduction

This is an alternative antiplane model, not frozen Direction 2. The following reduction is an exact qualitative result, not a stability theorem or a novelty claim. It uses boundary unique continuation and reciprocity, **not** the interface-density lemma. It assumes ideal operator data for every boundary control, not one scalar current.

## Exact reduction

Let \(\Omega\subset\mathbb R^2\) have connected smooth boundary and let each of two smooth inclusions \(D_1,D_2\Subset\Omega\) carry the real symmetric coercive variational model in the companion audit, with the same known positive exterior modulus \(\mu_+\). The two interior parameters and interfaces may differ. Define their Dirichlet-to-Neumann maps \(\Lambda_j:H^{1/2}(\partial\Omega)\to H^{-1/2}(\partial\Omega)\) variationally. Existence for arbitrary data follows by an exterior-collar lifting supported away from either inclusion, followed by Lax–Milgram; the maps are bounded and symmetric. Let \(\Gamma_c,\Gamma_o\) be nonempty relatively open patches, even disjoint. Assume
\[\langle(\Lambda_1-\Lambda_2)f,g\rangle=0\quad\text{for all }f\in C_c^\infty(\Gamma_c),\ g\in C_c^\infty(\Gamma_o).\tag{1}\]
Then \(\Lambda_1=\Lambda_2\) on the full boundary.

**Proof.** The inclusions are compactly contained, so a connected boundary collar is disjoint from both. For fixed \(f\) supported in \(\Gamma_c\), the difference of the two solutions is harmonic in this collar, has zero Dirichlet data on the entire exterior boundary, and by (1) has zero weak conormal data on \(\Gamma_o\). Boundary unique continuation gives zero near \(\Gamma_o\); interior unique continuation propagates this throughout the connected collar. Consequently \((\Lambda_1-\Lambda_2)f=0\) on all of \(\partial\Omega\). Symmetry gives \(\langle(\Lambda_1-\Lambda_2)h,f\rangle=0\) for arbitrary \(h\in H^{1/2}(\partial\Omega)\) and every \(f\in C_c^\infty(\Gamma_c)\). Repeating the same collar argument with \(h\) as input and \(\Gamma_c\) as the zero-conormal patch yields \((\Lambda_1-\Lambda_2)h=0\) everywhere. □

The proof requires neither connectedness of the complement of the *union* of inclusions nor overlap of the patches: the common exterior collar is enough. It also uses equality of the **full spatially resolved partial operator**, not equality of a single integrated force. Unique continuation is qualitative and may be severely unstable; no bounded continuation map or noise stability follows.

## Consequence and prior overlap

If a full-data theorem identifies the inclusion in a particular admissible class, the same theorem transfers to the above disjoint-patch data, provided its equations, operator, parameter and geometry hypotheses match. In particular [arXiv:2509.15171](https://arxiv.org/html/2509.15171) Theorem 5.3 gives a full-DtN shape reconstruction criterion in its own hypotheses and with an anchor point inside the inclusion; its energy lacks a zeroth-order surface term, consistent with the above model. Its proof also depends on earlier factorization and positivity assumptions, including the range specified around its Theorems 3.3–3.4; those hypotheses must be checked in full before asserting a concrete corollary. This reduction is likely a standard consequence of elliptic unique continuation and reciprocity; the exact partial-data literature is not yet audited. **No novelty or new continuum theory is claimed.**

## Unfinished derivative and kernel

The requested actual shape derivative and kernel have not yet been derived. Full nonlinear data uniqueness under an imported full-data theorem does not itself establish injectivity of its shape derivative: an injective nonlinear map can have a zero derivative. Next compute the material derivative of both bulk domains and the fourth-order surface energy under a smooth vector-field deformation, including geometry, transported parameters and stationary-state cancellation, prove it in appropriate trace spaces, and use the collar/reciprocity argument on the derivative before analyzing its bilinear kernel. Do not replace this calculation with interface density alone.
