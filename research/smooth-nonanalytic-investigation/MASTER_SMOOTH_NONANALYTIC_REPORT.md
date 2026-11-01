# Exact smooth nonanalytic paired moments — interim research report

**Status:** exact full kernel characterized; full smooth injectivity versus a nonzero solution remains **open**. The results below are same-agent mathematics and audit, not independent certification. Started from `55df4a71ae4f91e0dd76b11e6d13d7ed87e309d0`; see companion reports and executable code for assumptions and derivations. They concern the frozen linear odd subsystem, not nonlinear physical preparation or identification of the complete system.

## Strongest results

1. The full infinite paired moments and both endpoint conditions are equivalent, without an analyticity assumption, to the explicit correction kernel (8) in `EXACT_FLAT_CORRECTION_OPERATOR.md`. The entire jet extension is uniquely and linearly determined by the control, and by the flat correction via the bounded inverse of a positive compact Bessel operator. The correction is not independent of the tail. Both directions of the equivalence, including smoothness and endpoint constraints, are proved; this is not a proof the kernel is nontrivial or trivial.
2. The explicit rescaled moment operator is Hilbert–Schmidt and has **dense nonclosed** range in \(\ell^2\), by an adjoint analytic continuation and residue argument. Its restriction to smooth flat corrections with the initial endpoint constraint also has dense range. This proves an output-sequence density statement, not row completeness, not injectivity, and not physical joint controllability. The compact operator is not Fredholm.
3. Every quasianalytic vector class containing the relevant entire jet extensions, with flat-at-zero uniqueness, has exact uniqueness. This genuinely goes beyond assuming the control is analytic, but leaves the nonquasianalytic \(C^\infty\) and Gevrey \(s>1\) cases open.
4. The fast exponential family alone has infinitely many compactly supported smooth annihilators on every interior interval; a rigorous construction follows from the Müntz theorem and smoothing measures. The coupled analytic tail makes this **not** an exact solution of the original problem.

## Five requested routes and the exact obstruction

**A — Laplace completeness.** The unperturbed fast transform is incomplete (Theorem 2); it has an infinite-dimensional smooth nullspace away from zero. But the slow term is coupled, and compact/nonclosed-range perturbation is not a valid completeness test. The precise remaining obligation is to prove or refute completeness of \(\{e^{-b_nt}+d b_n^{-2}e^{dt/b_n}\}\) in the relevant smooth endpoint class, not merely for fast exponentials.

**B — operator/Fredholm.** The positive Bessel operator has a stable inverse \(I+T\); the resulting moment operator is compact with dense nonclosed range. No Fredholm alternative applies. Dense range follows from absence of \(\ell^2\) relations among rows, not from density of their span in the control domain. The two questions are not interchangeable.

**C — entire interpolation.** For any admissible f, \(F\) is entire of finite exponential type and the slow values are tied to the fast values by \(F(-\mu+\delta_n)=-b_n^2F(-\mu-b_n)/d\). The slow points accumulate at \(-\mu\), forcing the jet but not the flat remainder. The adjoint residue proof settles sequence-range density, not the direct interpolation uniqueness problem. No canonical product or interpolation construction controlling the coupling and support was found.

**D — regularity.** The quasianalytic theorem is proved under precisely stated abstract class conditions. Ordinary smooth and Gevrey orders greater than one admit nonzero flat bumps; no Gevrey nonexistence or existence conclusion is justified merely from this observation.

**E — convergent construction.** Three correction bases and growing finite mode systems were examined. Conditioning, quadrature, and rank thresholds prevent passage to a limiting exact control; no actual solution sequence with a proved convergent nonzero limit is available. Data, double-quadrature comparisons, and high-precision identity checks are documented separately.

## Memory and cost

A nonzero exact-null control, if it exists, has infinite-sine-support memory; indeed all but finitely many memory coefficients are nonzero. A finite-order endpoint jet fixes the earlier audited leading power-law coefficient tail. No exact memory support beyond these constraints is characterized. For every nonzero memory target with infinitely many zero sine coefficients, control norms must diverge when temperature and memory errors simultaneously tend to zero; conditional prior gap-density supplies approximation sequences for finite-sine targets. No exact cost or quantitative rate is obtained for general targets; existence of an exact no-gap target is itself unresolved.

## Adversarial same-agent audit / restart

Check independently: (i) the prior jet theorem under the exact modal hypotheses and transposition class; (ii) the entire Bessel extension and both signs in (3)–(6); (iii) the adjoint series normal convergence and residue continuation around the accumulation point 0; (iv) the Müntz theorem's interval and exponent hypotheses; (v) endpoint-correction density in H, where point evaluation is not continuous; (vi) quasianalytic flatness on the actual one-sided interval; (vii) physical reachability and prior gap-density if used. The primary Ivanov–Pandolfi proof is still inaccessible and priority unresolved. Human review is not implied. Do not draft a publication-ready novelty claim.

Restart at (8): either establish row completeness in the specified smooth domain, or construct a nonzero k there satisfying every equation and the endpoint, with a justified convergence and support argument. Preserve the physical coefficients and initial/loading structure.
