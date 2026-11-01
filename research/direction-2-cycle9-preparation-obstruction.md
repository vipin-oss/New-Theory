# Cycle 9: exact reflection obstruction

## Theorem — restricted protocol, not a universal impossibility

Take any \(T_p>0\), fixed homogeneous material coefficients with \(a,k,\lambda,c,\kappa,\theta_*,L>0\) and \(b\ne0\). Suppose a scalar prescribed endpoint displacement \(g_p\), equal fixed bath temperatures and symmetric initial data \(z(-T_p)=0,\theta(-T_p)=\theta_*\) give a unique solution in a reflection-invariant solution class on the preparation interval. Then
\[z(s,L-x)=z(s,x),\quad \theta(s,L-x)=\theta(s,x)\quad\text{a.e. for every }s,\]
and hence the terminal odd component is identically zero. In particular, among full terminal memories in \(V_N\), only \(h=0\) can be produced. This remains true after imposing the exact terminal temperature and endpoint-displacement constraints. The obstruction is **proved conditional on uniqueness in the stated class**; it is not an assertion of existence/uniqueness for every amplitude. The zero trajectory explicitly satisfies all constraints.

**Proof.** For \(Rf(x)=f(L-x)\), transform a solution by
\[\widetilde u(s,x)=g_p(s)-u(s,L-x),\quad \widetilde z=Rz,\quad \widetilde\theta=R\theta,\quad \widetilde\sigma=R\sigma.\]
Then \(\widetilde u_x=R u_x\), and both displacement boundary values, both equal baths, and symmetric initial data are preserved. Reflection commutes with \(\partial_{xx}\), while the scalar stress equilibrium is preserved: \(\partial_x\widetilde\sigma=-R(\sigma_x)=0\). The internal ODE and nonlinear thermal equation transform exactly, including the square and nonzero \(b,k,\lambda\). Thus the transformed fields solve the same initial-boundary problem. Uniqueness gives \(\widetilde z=z\), \(\widetilde\theta=\theta\). This uses neither linearization, approximate controllability, entropy monotonicity nor terminal exact controllability. It also works for symmetric, not necessarily zero, initial \(z\) and \(\theta\), provided the transformed initial mechanical data are compatible.

## Exact and approximate obstruction

Let \(H_e=\ker(I-R)\), \(H_o=\ker(I+R)\). They are closed orthogonal subspaces of \(L^2(I)\), and \(V_N\subset H_o\). For any reachable \(z_f\in H_e\) and any nonzero \(v\in V_N\),
\[\|z_f-v\|_{L^2}^2=\|z_f\|_{L^2}^2+\|v\|_{L^2}^2\ge\|v\|_{L^2}^2.\tag{1}\]
Consequently no sequence of these preparations approximates a **fixed nonzero** odd target in \(L^2\), or in \(H^2\) whenever the terminal states have that regularity (\(H^2\) convergence implies \(L^2\) convergence). States tending to zero are not approximation of a fixed nonzero target. The projected odd state and its finite-prior coefficients are exactly zero.

This is a symmetry selection rule, not backward instability or a claim that dissipation by itself forbids memory preparation. It does not exclude asymmetric initial states, asymmetric thermal baths or other physically admissible controls. If symmetry or uniqueness is lost, the proof does not apply. It does not establish that nonzero symmetric terminal-compatible states exist or that zero is the only **full** reachable memory. It is not a counterexample to the Cycle 8 abstract inverse theorem or a statement about the observation operator's infinite-dimensional kernel.
