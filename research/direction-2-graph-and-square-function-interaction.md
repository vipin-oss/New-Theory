# Graph uniqueness versus endpoint regularity

These are distinct questions about the same actual linear operator. Under the pre-delay isomorphism, graph uniqueness is exactly \(\ker\mathcal T=0\); endpoint regularity is a spatial derivative square sum of the observation kernel. Neither property logically implies the other from these operator-level facts alone.

Two explicit **abstract** examples use mutually orthonormal \(v_0,v_1,\ldots\) in the output space and \(q_n\asymp n\); neither is an actual coefficient field or physical solution.

* Set \(k_n=v_0/q_n\). Then all residuals vanish, so the endpoint holds, every column is nonzero, and the high-frequency one-sign separator holds; yet \(q_1\phi_1-q_2\phi_2\) is invisible. Thus endpoint smoothness, nonzero columns and the cone property together do not imply signed injectivity.
* Set \(k_n=v_0/q_n+d_nv_n\), with \(d_n=n^{-3/2}/\sqrt{\log(n+1)}\). The synthesis is bounded and injective, as its \(v_n\) coefficient is \(d_nh_n\); nevertheless \(\sum q_n^2d_n^2=\infty\). This example has the inherited column little-o and every fractional \(s<1\) residual regularity. Thus injectivity alone does not imply the endpoint.

Neither construction resolves the actual system. The first demonstrates why smoothness of the residual does not force graph-adjoint density; the second why density alone gives no regularity. Even at the endpoint, the decomposition is rank one plus an \(H^1\)-kernel operator, not an invertible-operator perturbation theorem; compact operators can be injective and still have nonclosed ranges.

The full \(H_o\) graph condition is stronger than trivial kernel on \(X_o=H^2\cap H_o\); the corresponding physical-past class is different again and requires coupled equilibrium/thermal evolution through the past. The derivative cannot by itself establish nonlinear local injectivity. A bounded scalar-functional reconstruction additionally needs exact adjoint range, not just dense closure. Earlier restricted finite-dimensional and cone results remain valid only in their stated scopes.

**Priority:** independently pursue adjoint-density controls or an actual graph-sensitive coupled estimate, and the dyadic/temporal-modulus endpoint estimate. A resolution of one cannot be used to silently classify the other. No new foundational theory or demonstrated novelty follows from these analytic observations.
