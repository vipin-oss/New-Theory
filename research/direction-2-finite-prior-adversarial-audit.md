# Adversarial check: finite prior and nonlinear extension

Arena rederived the finite-prior estimates in `direction-2-finite-prior-independent-proof-audit.md` and the nonlinear argument in `direction-2-finite-prior-nonlinear-identifiability.md`; this is not independent human certification by the designated auditor.

| Attack | Finding |
|---|---|
| Coalescing characteristic roots | \(d_0>0\) yields two strictly distinct roots per mode; both branches strictly decrease and are on opposite sides of \(-\mu\). No coalescence. |
| Delayed data removes Gram positivity | A nonzero finite exponential polynomial cannot vanish a.e. on a nonempty open interval. The argument uses the reference system only; actual time analyticity is not assumed. |
| Wrong input or flux normalization | Both systems start with \(P(0)=h\), \(Y(0)=0\), use normalized odd sine inputs and flux \(2A_0\kappa Y_x(0)\). |
| Lost pre-delay memory | Entire interval \((0,T)\) is solved, subtracted, and estimated; restriction occurs only at observation. |
| \(B\) falsely bounded | \(B-B_0\in L^2(Q_T)\) multiplies the explicitly bounded finite reference temperature, and the energy uses \(\int\|B(t)\|_2^2\). |
| Missing coefficient difference | Exact subtraction gives the three stated forcing terms and no ODE residual; the actual coefficient \(S\) multiplies the difference \(p\). |
| Trace or energy constant too small | Recomputed with \(2/L\), which is larger than the \(1/L\) trace term. \(\Xi,E_*,U_*,V_*,C_{tr}\) are sufficient as written in the adopted numerical norm convention. |
| Projection creates injectivity | Projection is only applied after the actual \(L_N\) is proved injective; full equality implies projected equality. The range is finite-dimensional and closed. |
| Difference of nonlinear remainders | A quadratic single-point bound alone is insufficient; the two-point proof uses inherited \(C^2\) and the mean-value formula. |
| Radius zero or inadmissible | Continuity of \(D^2\mathcal N\), strict small-load condition and finite \(K_N\) give a positive relative \(H^2\) ball within the inherited weak-initial positive solution domain. Its numerical size is not given. |
| Uniform infinite-dimensional conclusion | None follows: each \(N\) requires its own threshold and Gram. Compactness independently rules out a uniform \(L^2\) lower bound, but neither proves nor refutes injectivity. |
| Physical experiment changed | The constant system appears only in an exact subtraction; the theorem's actual state uses strictly nonzero frozen sinusoidal loading and all nonzero couplings. No observation or boundary condition is replaced. |
| Hidden \(h\) or load dependence | Bounds use \(q_0\) and fixed \(N\), material parameters, time and interval; \(H_N\), \(\sigma_N\), \(C_{tr}\) do not depend on \(h\) or the variable \(q<q_0\). \(K_2,r_1\) in the nonlinear theorem may depend on the fixed actual base and \(q\). |
| Wrong solution domain | Claims are restricted to the inherited open weak-initial \(H^2\) neighborhood; no claim is made about additional corner-classical compatibility. |

**Decision:** no fatal mathematical gap found under explicitly inherited assumptions. The transfer from an injective finite-dimensional derivative to a local Lipschitz inverse is standard functional analysis, not novelty by itself. The coefficient/Gram calculation is model-specific; literature priority and experimental relevance remain unverified.
