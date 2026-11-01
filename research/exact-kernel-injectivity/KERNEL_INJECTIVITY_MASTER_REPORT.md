# NONTRIVIAL KERNEL CONSTRUCTED

**Verdict:** Under the frozen odd-model spectrum and stated modal assumptions, \(\ker\mathsf B_{\rm adm}\) is not trivial. Indeed, for every \(I\Subset(0,T)\), it contains an infinite-dimensional real space of corrections \(k\in C_c^\infty(I)\). This is an exact functional-analytic construction, not a finite-dimensional null vector. The construction is specified through biorthogonal functions, a finite-dimensional nullspace and a Fredholm inverse; it is not a numerical closed-form example. The proof is same-agent work, not an independent expert certification or priority claim.

## The decisive mechanism

Write the exact correction map as \(\mathsf B=E+R\), with \(E\) the fast transform and \(R\) the dependent Bessel tail. On \(X=L^2(I,t\,dt)\), the tail maps into sequences decaying exponentially at rate T. A published fast-exponential biorthogonal theorem, plus reversal, shifting and smooth convolution, gives a smooth compact-interior right inverse S for E on a *strictly weaker* exponentially weighted sequence space. Thus \(A=I_X+SR\) is identity plus compact. The fast nullspace contains infinitely many smooth compactly supported functions by Müntz incompleteness; the range of A has finite codimension. Choose two independent fast-null seeds inside that range, solve their exact Fredholm equations, and take a nonzero linear combination enforcing \(v(T)=0\). The infinite correction series converges in every C^j norm. All moments and the endpoint hold exactly. Full proof and selection formula: `FLAT_KERNEL_CONSTRUCTION_OR_NO_GO.md`.

This does not infer injectivity or noninjectivity from compactness, density, finite rank or approximate controllability. It uses the strict temporal margin between interior support and the analytic tail at T. The uniform square-root spectral gap is essential to the invoked biorthogonal estimate; \(b_n\asymp n^2\) by itself is not enough. The actual spectrum has the required gap, as proved in the construction report.

## Consequences and scope

For each constructed k, \(v=(I+\mathsf T)^{-1}k\) and \(f=e^{\mu t}t v\) are real and smooth; f changes sign, is analytic near both endpoints but nonanalytic on the full interval, and has no terminal switch-off gap. The temperature paired moments vanish exactly. The terminal-memory coefficients are given by (13) of the construction report; all but finitely many are nonzero and (14) gives their leading power law in terms of the first nonzero weighted v-moment. Values depend on the chosen exact solution and physical parameters; none are invented.

This settles the stated **linear odd paired-moment operator**, conditional on the previous modal derivation and its solution/trace framework. It does not prove nonlinear physical invisibility, preparation from a coupled past, or full-system identifiability failure. It does not establish a novelty or chronological priority claim.

The fast rows alone are incomplete; the coupled perturbed rows are also incomplete, now proved by an exact nonzero orthogonal vector. The adjoint remains injective and the original operator has dense range, illustrating why that prior result could not decide its kernel. An exact nonzero correction cannot itself have zero fast moments at infinitely many nodes: the entire tail enforces a precise nonzero exponential asymptotic. Corrections must oscillate in sign infinitely often near the first point of their support; see `FUNCTION_SPACE_AND_REGULARITY_THEOREMS.md`.

## Audit and remaining work

The critical external input is Theorem 2.1 of Cannarsa–Martinez–Vancostenoble ([arXiv:1706.02435](https://arxiv.org/html/1706.02435)); its sign and spectral-gap hypotheses are checked in the construction. The same-agent adversarial audit lists the exact points needing independent mathematical review. The original Ivanov–Pandolfi paper remains inaccessible, and literature/priority comparison is incomplete. A numerical closed-form control, prescribed Gevrey regularity, and physical realization are not established.
