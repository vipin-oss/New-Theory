# Actual delayed graph and boundary uniqueness

**Classification: OPEN** for arbitrary \(H_o\) input, even in the audited small-load regime. Conditional equivalences below are exact, not a proof of density. The same answer applies to the weaker \(H^2\) prior unless separately shown; no physical invisible state has been constructed.

Let \(A_\delta h=Y[h](\delta)\), \(D_\delta h=P[h](\delta)\). Under the hypotheses and threshold of `direction-2-independent-audit-pre-delay-isomorphism.md`, \(D_\delta:H_o\to H_o\) is an isomorphism. Strong forward regularity gives bounded \(A_\delta:H_o\to V_o\); \(G=A_\delta D_\delta^{-1}\). The delayed reachable states are exactly \(\mathcal G_\delta=\{(Gp,p):p\in H_o\}\), not all \(V_o\times H_o\). With the actual restart flux \(\mathcal R_\delta\), \(O=\mathcal R_\delta(G, I)\), \(\mathcal T=OD_\delta\). These identities retain the full pre-delay history in \(G\); they do not reset memory.

## Boundary Cauchy route

If \(Op=0\), the restarted strong solution has \(Y=0\) and \(Y_x=0\) at both endpoints a.e. on \(J\), the second endpoint following from oddness. However it solves
\[M Y_t-\kappa Y_{xx}=BY+S\left(e^{-\mu(t-\delta)}p+\gamma\int_\delta^t e^{-\mu(t-s)}Y(s)ds\right),\quad Y(\delta)=Gp.\]
The spatial source \(Se^{-\mu(t-\delta)}p\) is unknown and not a potential times \(Y\). A scalar homogeneous boundary unique-continuation theorem therefore cannot be applied. A sufficient graph-sensitive assertion is: **every** \(p\in H_o\) whose strong solution above has zero observed flux is zero. A more stringent estimate that would prove it is \(\|p\|_{H^{-s}}\le C\|Op\|_{L^2(J)}\) for some finite \(s\), if actually proved; such a bound is not known or required for injectivity. Carleman treatment must retain the initial ODE term and a trace justified at the regularity of the actual coefficients; no verified theorem here absorbs that term from this single boundary trace.

## Exact adjoint test and synthesis

The transposition construction in `direction-2-exact-adjoint-and-observability.md` gives a bounded adjoint, mass inside \(-\partial_t(Mz)\), and no unproved classical adjoint trace. On the delayed state space,
\[O^*=(G^*,I)\mathcal R_\delta^*,\qquad \ker O=0\iff\overline{\operatorname{ran}O^*}^{H_o}=H_o.\]
Equivalently, for every odd sine \(\phi_n\), construct controls \(f_{n,j}\) whose graph-restricted adjoint states converge strongly to \(\phi_n\); unbounded control norms are allowed. Neither formal adjoint equations nor density in a larger state space is a proof. The full-time version is \(\mathcal T^*f=\Pi_o w_f(0)\), with the backward ODE and pre-delay propagation included.

The other exact formulation is \(\sum h_nk_n=0\Rightarrow h=0\) in \(L^2(J)\). The series converges because \(\mathcal T\) is bounded; a proof needs a legitimate whole-series separation, not every column nonzero or a finite Gram matrix. Reference exponential residues work for constant auxiliary coefficients, where continuation is justified; actual coefficients are nonautonomous and can mix modes, so those residues and time analyticity are unavailable. The proved high-frequency one-sign separator detects a nonzero sequence of one sign, but not a general signed sequence nor differences of two cone inputs.

## Counterexample search and prior distinctions

An admissible counterexample must give a nonzero actual \(h\), solve the frozen nonlinear-base-generated coefficients and the complete initial-value problem, and prove flux identically zero a.e. on \(J\). An arbitrarily small rank-one observation perturbation or finite numerical near-null vector does none of this. No such construction has been found. On \(X_o=H^2\cap H_o\), the precise condition is \(X_o\cap\ker\mathcal T=\{0\}\), weaker than \(H_o\)-injectivity. An ODE-compatible past realizing \(h\) is not necessarily a past satisfying the coupled thermomechanical equations. Even a proved linear \(H_o\) kernel statement would not alone yield nonlinear injectivity.

**Exact restart point:** establish graph-restricted adjoint approximate controllability by explicit controls or a coupled estimate that treats the \(p\) source and \(Gp\) jointly, or construct a complete physical invisible trajectory. Verify all boundary/transposition and past admissibility hypotheses before classifying either direction.
