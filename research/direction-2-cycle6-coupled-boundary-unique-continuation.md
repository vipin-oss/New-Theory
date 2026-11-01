# Cycle 6: coupled boundary identity and graph obstruction

**Actual graph UC: OPEN.** Work under the base/forcing and graph-isomorphism conditions in `direction-2-cycle5-combined-threshold-and-status.md`, with real odd \(p\in H_o=L^2_o(I)\), \(G:H_o\to V_o=H^1_0\cap H_o\), and \((Y,P)(\delta)=(Gp,p)\). On \(J=(\delta,T)\),
\[MY_t-\kappa Y_{xx}-BY-SP=0,\quad P_t+\mu P-\gamma Y=0,\quad Y|_{x=0,L}=0.\tag{1}\]
The actual positive \(M\), \(B,S\) are even, with \(M,M_t,S,S_t,B\in L^\infty(Q_J)\), \(M_x\in L^\infty_tL^2_x\), \(B_x\in L^\infty_tL^2_x\), \(B_t\in L^2(Q_J)\), under the Cycle 5 bootstrap. The strong solution has \(Y\in H^1_tL^2\cap L^2_tH^2\cap C_tV_o\), \(P\in H^1_tL^2\). Flux \(Y_x(0,\cdot)\in L^2(J)\) is a Sobolev trace. The positive-time quotient gain gives \(Y_x(0,\cdot)\in H^1(J)\); no spatial trace for \(P\) follows for general \(p\in L^2\). The graph itself contains the full pre-delay evolution.

## A first-principles weighted identity, not a Carleman theorem

Take the smooth nonsingular weight \(\varphi(x,t)=x-\eta(t-t_c)^2\), \(\eta>0\), \(t_c\in J\), \(s>0\). It has no spatial or temporal singularity, \(\varphi_x=1,\varphi_{xx}=0\). Put \(v=e^{s\varphi}Y\), \(r=e^{s\varphi}P\), \(V=sM\varphi_t+\kappa s^2+B\). Formally, for smooth solutions and coefficients,
\[\mathcal A v=-\kappa v_{xx}-Vv,\quad \mathcal Dv=Mv_t+2\kappa s v_x,\quad \mathcal A v+\mathcal Dv=Sr,\tag{2}\]
\[r_t+(\mu-s\varphi_t)r=\gamma v.\tag{3}\]
With \([F]_{0}^{L}=F(L)-F(0)\), direct integration by parts on \(I\times(t_1,t_2)\subset I\times J\) gives
\[\begin{aligned}
2\!\iint \mathcal Av\,\mathcal Dv
={}&\left[\int_I(\kappa Mv_x^2-MVv^2)dx\right]_{t_1}^{t_2}
+\iint\{-\kappa M_t v_x^2+2\kappa M_xv_xv_t+(MV)_t v^2+2\kappa sV_xv^2\}\\
&-2\kappa\!\int_{t_1}^{t_2}[Mv_xv_t]_{0}^{L}dt
-2\kappa^2s\!\int_{t_1}^{t_2}[v_x^2]_{0}^{L}dt
-2\kappa s\!\int_{t_1}^{t_2}[Vv^2]_{0}^{L}dt.\end{aligned}\tag{4}\]
For smooth Dirichlet \(v\), the first and last spatial boundary terms vanish; the middle is \(2\kappa^2s\int(v_x(0)^2-v_x(L)^2)dt\). Oddness gives \(Y_x(L,t)=Y_x(0,t)\), hence zero measured flux also kills the unmeasured endpoint derivative, although the weight itself is not symmetric. For (3), setting \(a=\mu-s\varphi_t\),
\[\iint|r_t+ar|^2=\iint(|r_t|^2+(a^2-a_t)r^2)+\left[\int_I a r^2dx\right]_{t_1}^{t_2}=\gamma^2\iint v^2.\tag{5}\]
No spatial boundary term for \(r\) is introduced. For the actual coefficients, (4) is presented first for smooth approximations; \(M_t\in L^\infty\), \(B_t\in L^2\), \(M_x,B_x\in L^\infty_tL^2\), and strong-solution spaces support the displayed products via 1D embeddings on interior time slabs, provided approximations converge in the indicated norms. This is a computation, not an asserted closed Carleman inequality.

The graph contributes \(v(\delta)=e^{s\varphi(\delta)}Gp\), \(r(\delta)=e^{s\varphi(\delta)}p\), so the temporal terms in (4)–(5) are unknown. \(\mathcal A+\mathcal D=Sr\) leaves \(\iint |S r|^2\) on the heat side, and (5) leaves the signed endpoint graph term \(\int a(\delta)e^{2s\varphi(\delta)}p^2\). The flat spatial weight has \(\varphi_{xx}=0\), so this identity by itself gives no coercive parabolic \(s^3\)-bulk term. Choosing a standard singular, pseudoconvex weight would require proving the full new estimate and justifying its singular limits and graph terms; no such proof is available. A cutoff that vanishes at \(\delta\) removes the graph trace but introduces \(M\chi'Y\) and \(\chi'P\) in the PDE–ODE equations, neither controlled by the zero boundary output. This is an exact unabsorbed term, not a proof that all Carleman routes fail.

Differentiating (1), justified only in the upgraded positive-time class, gives the source \(B_tY+S_tP\) in the equation for \(Y_t\). The available \(B_t\in L^2\), \(Y\in L^\infty\), \(S_t\in L^\infty\), \(P\in C_tL^2\) make it \(L^2\), but do not bound it by the boundary observation. Zero flux does not make it vanish. The Volterra formula
\[P(t)=e^{-\mu(t-\delta)}p+\gamma\int_\delta^te^{-\mu(t-s)}Y(s)ds\tag{6}\]
retains the initial graph slice even if the integral can be absorbed by a time-weighted estimate.

## Analyticity is conditional, not a rescue theorem

A possible analytic-semigroup setup would take \(X=H_o\times H_o\), common domain \(D=(H^2\cap H^1_0\cap H_o)\times H_o\), and \(\mathcal A(t)(y,p)=(M(t)^{-1}[\kappa y_{xx}+B(t)y+S(t)p],\gamma y-\mu p)\). Establishing sectoriality with uniform resolvent bounds, a common-domain nonautonomous evolution and analytic dependence in \(t\), plus boundary-compatible trace smoothing on positive-time slabs, is still required; the base quasilinear nonlocal mass \(cI+d\theta Q\) and ODE need an independently verified maximal-regularity isomorphism and analytic implicit-map argument. The finite Sobolev bootstrap alone gives none of these. Even analyticity of \(t\mapsto Op\) would only continue zero output; a graph-specific residue or continuation argument must still eliminate \(p\). The reference semigroup provides neither an actual nonautonomous theorem nor a physical counterexample.
