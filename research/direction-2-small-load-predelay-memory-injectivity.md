# Direction 2: pre-delay memory map for a smaller nonzero-load regime

**Status: CONDITIONALLY PROVED**, relying on the inherited active-base and forced-solution estimates, with no independent human certification. This result concerns the actual frozen nonautonomous system, not the alternative distributed-rate model. It does **not** prove delayed observation injectivity.

## Statement

Use exactly the frozen equations, material signs, geometry, sinusoidal nonzero loading and delay \(\delta=T/100\) of `direction-2-exact-adjoint-and-observability.md`. Assume the inherited small-load actual-base construction and its bounds and odd forced estimates. There is a positive data-dependent \(q_*>0\) such that, for \(0<q=|g_*|/L<q_*\), the actual memory-component map
\[D_\delta:L^2_o(I)\to L^2_o(I),\qquad D_\delta h=P[h](\delta),\]
is boundedly invertible. In particular the complete reachable-state map \(h\mapsto(Y(\delta),P(\delta))\) is injective. The additional threshold is not evaluated for an unspecified experiment.

## Proof

Use the constant-coefficient *comparison* system of `direction-2-finite-prior-independent-proof-audit.md` §2, not as a change of the actual experiment. Its odd sine modes have coefficients \(M_0>0\), \(S_0\gamma>0\), \(\mu>0\), and \(B_0<0\). For initial \(u_n(0)=0\), \(v_n(0)=1\), the heat component is
\[u_n(t)=\frac{S_0}{M_0\Delta_n}(e^{\lambda_{n,+}t}-e^{\lambda_{n,-}t}),\qquad \Delta_n>0,\quad \lambda_{n,+}>\lambda_{n,-}.\]
Hence \(\gamma u_n(t)\ge0\), and the exact ODE gives
\[v_n(t)=e^{-\mu t}+\gamma\int_0^te^{-\mu(t-s)}u_n(s)ds\ge e^{-\mu t}.\]
The comparison memory map \(D^0_\delta\) is the diagonal multiplier \(v_n(\delta)\) on the complete odd sine basis. Its boundedness follows from the inherited reference strong estimate; the lower bound above yields a bounded inverse with \(\|(D^0_\delta)^{-1}\|\le e^{\mu\delta}\).

For arbitrary \(h\in L^2_o\), let \((Y^0,P^0)\) be the comparison solution and \((Y,P)\) the actual one, with the same zero initial temperature and initial memory \(h\). By the reference strong estimate and one-dimensional embedding, there is a fixed \(C_0\) such that
\[\|Y_t^0\|_{L^2(Q_T)}+\|Y^0\|_{L^\infty(Q_T)}+\|P^0\|_{L^2(Q_T)}\le C_0\|h\|_2.\]
Subtracting on the entire \((0,T)\) gives the actual-coefficient forced system for \((u,p)=(Y-Y^0,P-P^0)\), zero initial data and
\[F=-(M-M_0)Y_t^0+(B-B_0)Y^0+(S-S_0)P^0.\]
The inherited coefficient estimates give \(\|M-M_0\|_\infty\le D_Mq\), \(\|B-B_0\|_{L^2(Q_T)}\le D_Bq\), \(\|S-S_0\|_\infty\le D_Sq\). Thus \(\|F\|_2\le C_Fq\|h\|_2\), with \(C_F=C_0(D_M+D_B+D_S)\). The inherited actual forced estimate is uniform on the stated small-load interval: \(\|u\|_{L^2(Q_T)}\le C_{\rm forc}\|F\|_2\). Its ODE and zero initial memory difference yield
\[\|(D_\delta-D^0_\delta)h\|_2=\|p(\delta)\|_2\le |\gamma|\sqrt\delta\,\|u\|_{L^2((0,\delta)\times I)}\le C_Dq\|h\|_2,\quad C_D=|\gamma|\sqrt\delta\,C_{\rm forc}C_F.\]
Therefore, if \(0<q<q_*:=\min\{s_*/2,e^{-\mu\delta}/(2C_D)\}\), the norm of \((D^0_\delta)^{-1}(D_\delta-D^0_\delta)\) is at most \(1/2\), so Neumann series proves invertibility. □

## Interpretation and audit

The comparison is analytical only: all actual couplings and the full pre-delay evolution remain. The lower bound depends on the sign product \(S_0\gamma>0\), not on a coupled maximum principle for the nonautonomous system; no sign of the actual solution is asserted. The proof applies to arbitrary odd \(L^2\) initial states, not only finite sine combinations; constants must be uniform in \(h\) as specified. A smaller unknown symbolic load threshold does not validate a numerical experiment. Invertibility of \(D_\delta\) is stronger than injectivity of the entire pre-delay graph, but does not prove that this graph has trivial intersection with the future observation kernel. The second condition in (11) of the adjoint report and full nonlinear uniqueness remain **OPEN**. Exact source-kernel \(H^1\) square summability also remains **OPEN**.
