# Exact injectivity and nonautonomous coupled unique continuation

**Date:** 1 November 2026. **Decision: REFORMULATE.** No injectivity theorem or exact physical counterexample is established. This audit proves the bounded Volterra inverse on its full stated space, derives a quantitative finite-section estimate with an explicitly identified tail/conditioning obstruction, and proves that the actual output family cannot be a Riesz sequence. A coupled weighted ODE calculation isolates the memory snapshot that prevents the attempted Carleman absorption. These results do not settle the infinite-dimensional kernel.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is a single-agent mathematical audit, not independent human certification. The original model, material parameters, loading, interval, admissible input topology and boundary/initial conditions remain frozen. No new foundational continuum theory, proven novelty or manuscript is claimed.

## 1. Reconstructed forward and Volterra operators

The immediate report `direction-2-coupled-boundary-observability-and-exact-kernel.md` and its delayed-state/adjoint, boundary-flux, reachable-state, compact-quotient and base-regularity dependencies were inspected. Let \(I=(0,L)\), \(J=(\delta,T)\), \(T=10/\lambda\), \(\delta=T/100\), and \(H=L^2_o(I)\). The loaded base is driven by the prescribed \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\). With \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(d=b^2/D\), \(Qv=v-\bar v\), the actual odd equations are
\[
MY_t-\kappa Y_{xx}=BY+SP,\qquad P_t+\mu P=\gamma Y,\qquad
Y(0,\cdot)=0,\ P(0,\cdot)=h,\quad Y(t,0)=Y(t,L)=0, \tag{1}
\]
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b,\quad
\mathcal T h=2A_0\kappa Y_x(\cdot,0)|_J. \tag{2}
\]
The material signs and \(b\ne0\) are retained. The physical odd input belongs to \(X=H^2(I)\cap H\); the bounded extension to \(H\) is analytic, not a nonlinear admissibility assertion. Under the previously derived sufficient small-load condition \(0<|g_*|/L<s_*\), which is **not numerically verified**, the estimates supply
\[
0<m_0\le M\le m_1,\quad M,S\in L^\infty,\quad M_x\in L^\infty_tL^2_x,\quad B\in L^2_{t,x}, \tag{3}
\]
\(Y\in\mathscr E:=H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\subset C_tH^1_0\), and \(P\in H^1_tL^2_x\). On every strip \((a,T)\), \(a>0\), the audited base additionally has \(B\in L^\infty_tL^2_x\cap L^2_tL^\infty_x\cap L^6_{t,x}\), and \(M,\kappa/M\) are spatially Lipschitz and time-Hölder in the earlier stated senses. These strip bounds do not extend automatically to \(t=0\), and \(B\in L^\infty_{t,x}\) is not established.

For arbitrary \(F,G\in L^2((0,T)\times I)\), initial temperature \(y_0\in H^1_0\cap H\), memory \(p_0\in H\), the source problem
\[
My_t-\kappa y_{xx}=By+Sp+F,\qquad p_t+\mu p=\gamma y+G
\]
has the established estimate
\[
\|y\|_{\mathscr E}+\|p\|_{H^1_tL^2_x}\le C_E(\|y_0\|_{H^1_0}+\|p_0\|_2+\|F\|_{L^2}+\|G\|_{L^2}). \tag{4}
\]
To check its dependence, test the heat equation by \(y_t\), and the ODE by \(p\). Using \(\|y\|_\infty\le\sqrt L\|y_x\|_2\) yields for \(E=\kappa\|y_x\|_2^2+\|p\|_2^2\)
\[
E'(t)+m_0\|y_t\|_2^2\le C(1+\|B(t)\|_2^2)E(t)+C(\|F(t)\|_2^2+\|G(t)\|_2^2).
\]
Gronwall uses only \(B\in L^2_{t,x}\); the equation then bounds \(y_{xx}\in L^2\) and the ODE bounds \(p_t\in L^2\). Galerkin approximations, weak limits and uniqueness supply (4); no time derivative of \(M\) is used. The scalar source operator \(\mathscr H:F\mapsto y\) for \(My_t-\kappa y_{xx}-By=F\), zero initial/boundary temperature, is bounded by the same argument.

### Explicit bounded inverse, not merely formal

Let \(\mathscr E_0=\{y\in\mathscr E:y(0)=0,\ y\text{ odd}\}\) with its usual Banach norm; the continuous \(C_tH^1_0\) trace is controlled by this norm. Define
\[
\mathscr D h=Se^{-\mu t}h,\quad
\mathscr V y=\mathscr H\left(\gamma S(t)\int_0^t e^{-\mu(t-r)}y(r)dr\right),\quad
\mathscr B y=2A_0\kappa y_x(\cdot,0)|_J. \tag{5}
\]
All are bounded between the stated spaces: the memory convolution is bounded from \(L^2_tL^2_x\) to itself; \(S\) is bounded; and the endpoint trace is continuous from \(L^2_tH^2_x\) to \(L^2_t\).

For **every** \(g\in\mathscr E_0\), set \(F_g=Mg_t-\kappa g_{xx}-Bg\). It lies in \(L^2_{t,x}\), with
\(\|F_g\|_2\le C(1+\|B\|_{L^2_{t,x}})\|g\|_{\mathscr E}\), because \(\|g\|_{L^\infty_{t,x}}\le C_L\|g\|_{\mathscr E}\). Solve the coupled source problem with \(F=F_g\), \(G=0\), and zero initial pair. Its memory is \(p=\gamma\int_0^t e^{-\mu(t-r)}y(r)dr\). Hence \(y-\mathscr V y\) and \(g\) solve the same scalar zero-initial source equation, so they coincide. Estimate (4) gives \(\|y\|_{\mathscr E}\le C\|g\|_{\mathscr E}\). If \((I-\mathscr V)y=0\), the same scalar and coupled uniqueness gives \(y=0\). Therefore
\[
(I-\mathscr V)^{-1}:\mathscr E_0\to\mathscr E_0\ \text{exists and is bounded},\qquad
\boxed{\mathcal T=\mathscr B(I-\mathscr V)^{-1}\mathscr H\mathscr D}. \tag{6}
\]
This is an exact causal operator identity, not an assertion of a classical Green kernel or convergence of a Neumann series. The proof uses uniform constants for all \(g\), not just the special physical forcing.

### Initial asymptotic and compactness audit

Set \(M_*=c+d\theta_*\), \(S_*=\lambda\alpha br\theta_*\), \(c_*=S_*/M_*\ne0\). The time-local energy estimate applied to the shifted memory \(P-e^{-\mu t}h\) gives
\[
\|Y_x(t)\|_2\le C\sqrt t\|h\|_2,\quad \|Y(t)\|_2\le Ct\|h\|_2,\quad
\|Y(t)\|_\infty\le Ct^{3/4}\|h\|_2,\quad P(t)=h-\mu th+O_{L^2}(t^2\|h\|_2). \tag{7}
\]
Divide the PDE by \(M\), put \(A=\kappa/M\), and test against \(\psi\in H^1_0\). Since \(A_x\in L^\infty_tL^2_x\),
\(|\langle AY_{xx},\psi\rangle|\le C\|Y_x\|_2\|\psi\|_{H^1_0}\). The time-averaged diffusion term tends to zero; the \(BY/M\) average is bounded by \(Ct^{1/4}\|B\|_{L^2((0,t)\times I)}\|h\|_2\); and \(S/M\to c_*\) uniformly while \(P\to h\) in \(L^2\). Hence
\[
Y(t)/t\to c_*h\quad\text{in }H^{-1}(I). \tag{8}
\]
This checks the predecessor's weak result but gives no endpoint derivative trace of the limit.

The solution map is bounded into \(H^1_tL^2\cap L^2_tH^2\). Aubin–Lions yields compactness into \(L^2_tH^s\), \(3/2<s<2\), whose endpoint derivative map is bounded; hence \(\mathcal T:H\to L^2(J)\) is compact. For each bounded \(H^s\), \(s>0\), set \(K=\ker\mathcal T\); the predecessor's modulus \(\sup\{\operatorname{dist}_H(h,K):\|h\|_{H^s}\le R,\|\mathcal T h\|\le\varepsilon\}\to0\) follows by compact embedding and continuity. It is nonquantitative and modulo the unknown kernel.

The adjoint identity also checks out: Riesz representation of the bounded forward residual/endpoint functional gives \(z_f\in L^2_{t,x}\), \(w_f\in H^1_tL^2\),
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\quad -w_{f,t}+\mu w_f-Sz_f=0,\quad w_f(T)=0,
\quad \mathcal T^*f=\Pi_o w_f(0). \tag{9}
\]
The one-end boundary input and heat terminal condition are encoded in the forward-residual transposition identity; no classical \(z_f\) trace is claimed. The Hilbert adjoint domain is all \(L^2(J)\).

## 2. Coupled continuation: three independent checks

### A. A weighted memory calculation and its actual obstruction

Choose \((t_c-H,t_c+H)\Subset J\), \(s>0\), \(a_w>0\), a bounded spatial weight \(\psi\), and
\[
W_s(t,x)=\exp\{s\psi(x)-sa_w(t-t_c)^2\}. \tag{10}
\]
The exact ODE, in both time directions, is
\[
P(t)=e^{-\mu(t-t_c)}P(t_c)+\gamma\int_{t_c}^{t}e^{-\mu(t-r)}Y(r)dr.
\]
For the oriented Volterra integral, the kernel ratio is \(\exp[-sa_w((t-t_c)^2-(r-t_c)^2)]\); on either side of \(t_c\), Schur's test gives \(C e^{\mu H}/\sqrt{sa_w}\) for the weighted \(L^2_t\) operator norm. The snapshot has \(\int e^{-2sa_w(t-t_c)^2}dt\le\sqrt{\pi/(2sa_w)}\). Thus the **proved** ODE inequality is
\[
\|W_sP\|_{L^2_{t,x}}^2\le
\frac{C e^{2\mu H}|\gamma|^2}{sa_w}\|W_sY\|_{L^2_{t,x}}^2+
\frac{C e^{2\mu H}}{\sqrt{sa_w}}\|e^{s\psi}P(t_c)\|_2^2. \tag{11}
\]
The second term is a genuinely unknown distributed snapshot, not zero initial memory. Even \(|S|\ge s_0>0\), if separately verified, does not turn it into a measured quantity. The actual scalar equation after division is
\(Y_t-A Y_{xx}=(B/M)Y+(S/M)P\). A putative parabolic estimate with weight (10) would have residual, endpoint normal derivative and time-cutoff terms on the right. One might absorb the first term in (11) at large \(s\), but one must also control the weighted \(P(t_c)\), prove the scalar Carleman inequality for the actual nonautonomous \(A\), \(B/M\in L^2_tL^\infty_x\), and justify traces. **No such scalar estimate is claimed here.** The actual boundary observation is one endpoint on \(J\), with the other endpoint derivative equal by oddness. No smallness threshold or admissible weight for the coupled PDE is verified. Formula (11) itself is not a coupled Carleman estimate.

### B. Boundary transposition/reachable graph

The a.e. zero observation supplies both Dirichlet values and, by oddness, both endpoint derivatives of \(Y\) on \(J\), in their genuine trace sense. It does not supply zero interior temperature for an inhomogeneous equation, nor a value for \(P(\delta)\). The exact restart pair belongs to \(\mathcal S_\delta H\subset(H^1_0\cap H)\times H\). The precise graph continuation target is
\[
(y_\delta,p_\delta)\in\mathcal S_\delta H,\quad \mathcal R_\delta(y_\delta,p_\delta)=0
\Longrightarrow (y_\delta,p_\delta)=0, \tag{12}
\]
**and separately** \(\ker\mathcal S_\delta=0\), to deduce \(h=0\). Even (12) would not imply the second implication. A different direct argument could bypass both. Nonautonomous backward continuation of an unknown source is not supplied by a scalar homogeneous heat theorem.

### C. Smoothing/approximation

A plausible approximation must preserve ellipticity, parity and the coupled equations and establish uniform source and trace estimates, e.g. \(M_j\to M\) in a multiplier topology, \(B_j\to B\) in \(L^2_{t,x}\), \(S_j\to S\) in \(L^\infty\), and \(Y_j\to Y\) in \(L^2_tH^s_x\), \(s>3/2\), so \(Y_{j,x}(0,\cdot)\to Y_x(0,\cdot)\) in \(L^2(J)\). Even these limits do not transfer injectivity: a sequence of injective finite-rank or smooth operators can converge to a noninjective operator. One needs a uniform **qualitative separation mechanism** or a suitable weak quantitative estimate stable under passage to the limit, not a uniform full-space Lipschitz observability estimate contradicted by compactness. No such coupled estimate is proved. Thus coupled boundary UC is **NOT ESTABLISHED**, and no claim is made that it is the only possible route to injectivity.

## 3. Delayed-state operator and finite exceptional fiber

With \(U h=Y(\delta)\), \(D_\delta h=P(\delta)\),
\[
D_\delta=e^{-\mu\delta}I+K_\delta,\qquad K_\delta h=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr,
\]
\(K_\delta:H\to H^2\cap H^1_0\) is bounded, hence compact into \(H\). Thus \(D_\delta\) is index-zero Fredholm; its finite-dimensional kernel consists exactly of solutions of \(h=-e^{\mu\delta}K_\delta h\), and lies in \(H^2\cap H^1_0\cap H\). This eigen-equation is exact but not an explicit physical profile. The sufficient Neumann condition \(\|K_\delta\|<e^{-\mu\delta}\) proves invertibility, but the available data do not verify it. A forward energy upper bound cannot become a backward lower bound; a sign condition valid only on a cone cannot exclude signed eigenvectors. Neither injectivity nor noninjectivity of \(D_\delta\) has been shown.

Set \(E=\ker D_\delta\), \(N=E\cap\ker U\), \(F_*=U(E)\), and choose a \(H^1_0\)-orthonormal basis \(v_i\) of \(F_*\) with representatives \(e_i\in E\), \(Ue_i=v_i\). The exact finite Gram matrix
\[
G_{ij}=\langle\mathcal T e_i,\mathcal T e_j\rangle_{L^2(J)}
\]
is positive definite iff the vertical observation kernel \(F_0=\{v\in F_*:\mathcal R_\delta(v,0)=0\}\) is zero. A basis of all \(E\) instead tests \(E\cap\ker\mathcal T\), including \(N\). No entries or rank are known. On \(H_1=E^\perp\), \(D_1=D_\delta|_{H_1}:H_1\to\operatorname{ran}D_\delta\) has bounded inverse and determines the graph temperature \(A_*p=UD_1^{-1}p\), modulo \(F_*\); this is an operator relation, not an independent measurement of \(p\).

The known quotient operator on the graph is compact and has the exact decomposition
\(\dim\ker\mathcal T=\dim N+\dim F_0+\dim\ker\Gamma\), with the last dimension possibly infinite. Fredholmness of \(D_\delta\) cannot be transferred to compact \(\mathcal T\). In fact compact \(\mathcal T\) on infinite-dimensional \(H\) is not Fredholm: a closed-range compact operator has finite-dimensional range, hence an infinite-dimensional kernel. No infinite-dimensional lower bound, rank or nonzero null vector follows.

## 4. Initial-corner boundary response

The exact base bounds yield \(\|M(t)-M_*\|_\infty=O(t^{1/4})\), \(\|S(t)-S_*\|_\infty=O(t^{1/4})\), using \(y_b(0)=0\), the base energy estimate and its exact memory integrals. Only \(B\in L^2\) is established across the initial corner. For \(h\in H^2_o\), endpoint values \(h(0)\) and \(h'(0)\) exist, and oddness gives \(h(L)=-h(0)\), not \(h(0)=0\).

The frozen half-line diagnostic in the predecessor gives coefficients \(2c_*h(0)/\sqrt{\pi A_*}\) for \(\sqrt t\), and \(c_*h'(0)\) for \(t\), where \(A_*=\kappa/M_*\). It is not an actual-system theorem. Freezing creates residuals \((A-A_*)Y_{xx}\), \((S/M-c_*)P\), \((B/M)Y\), and the ODE-history correction; their weighted integrability does not by itself give a boundary normal trace error \(o(t)\), or even \(o(\sqrt t)\), in pointwise time. In particular the \(O(t^{1/4})\) coefficient estimate and an \(L^2\) potential do not establish the required Green-kernel derivative asymptotics. Spatial nonlocality in \(Q(y_b)_t\) is retained. No evaluation of the heat PDE at the endpoint is justified. The strongest verified actual asymptotic is (8) plus (7), not a boundary-jet expansion. Nor is the active output known time-analytic, so initial jets cannot be propagated from the fixed delayed interval by analytic continuation.

## 5. Moment family and a stronger quantitative obstruction

Let \(\phi_n=\sqrt{2/L}\sin(2n\pi x/L)\), \(\rho_n=(2n\pi/L)^2\). The exact moment equations retain all entries \(M_{nm}=\langle M\phi_m,\phi_n\rangle\), \(B_{nm}=\langle B\phi_m,\phi_n\rangle\), \(S_{nm}=\langle S\phi_m,\phi_n\rangle\), as in the previous report. For \(k_n=\mathcal T\phi_n\), boundedness implies
\[
\mathcal T h=\lim_{N\to\infty}\sum_{n=1}^N h_n k_n\quad\text{in }L^2(J),\qquad
Y_x(0,\cdot)=\lim_{N\to\infty}\sum_{n\le N}\sqrt{2/L}(2n\pi/L)u_n(\cdot). \tag{13}
\]
The trace convergence follows from \(L^2_tH^2_x\) convergence and interpolation; it is not termwise vanishing. The increasing boundary weights do not by themselves separate the coupled time functions.

**Structural result.** The sequence \((k_n)\) is Bessel and \(\|k_n\|_{L^2(J)}\to0\). Indeed \(\sum_n|\langle f,k_n\rangle|^2=\|\mathcal T^*f\|_H^2\le\|\mathcal T\|^2\|f\|^2\), and \(\phi_n\rightharpoonup0\) while \(\mathcal T\) is compact. Therefore \((k_n)\) is **not a Riesz sequence**: a Riesz lower bound would give \(\|k_n\|\ge c>0\) for every \(n\). The synthesis operator is compact, and its positive Gram operator \(\mathcal T^*\mathcal T\) has zero in its spectrum; this does not prove a zero eigenvalue. Completeness of \(\{k_n\}\) in \(L^2(J)\) is equivalent to \(\ker\mathcal T^*=0\), a different property from injectivity of \(\mathcal T\). Minimality and completeness are unproved. A bounded biorthogonal family cannot exist, because \(1=|\langle k_n,g_n\rangle|\le\|k_n\|\|g_n\|\); an unbounded biorthogonal family is not ruled out.

Let \(P_N\) project onto \(\operatorname{span}\{\phi_1,\ldots,\phi_N\}\). Compactness gives the useful uniform convergence
\[
e_N:=\|\mathcal T(I-P_N)\|_{H\to L^2(J)}\to0. \tag{14}
\]
This follows from strong \(P_N\to I\) and compactness of \(\mathcal T^*\). It does **not** show injectivity: the finite output columns can be independent for every \(N\) while an infinite \(\ell^2\) combination cancels. The general point follows by taking a compact operator with kernel spanned by a vector with infinitely many nonzero coordinates: it is injective on each finite coordinate span, e.g. a compact diagonal injection composed with projection onto that vector's orthogonal complement. This is an abstract illustration, not the physical system.

### Certified finite-section conditional estimate

For the actual \(\mathcal T\), define
\[
\sigma_N=\inf\{\|\mathcal T v\|_{L^2(J)}:v\in P_NH,\ \|v\|_2=1\}=\sqrt{\lambda_{\min}(G_N)},\quad
(G_N)_{mn}=\langle k_m,k_n\rangle. \tag{15}
\]
Whenever a particular \(\sigma_N>0\) is **independently certified**, any \(h\in H^1(I)\cap H\) with \(\|h\|_{H^1}\le R\) obeys
\[
\boxed{\quad
\|h\|_2\le\frac{\|\mathcal T h\|_{L^2(J)}}{\sigma_N}
+\left(1+\frac{e_N}{\sigma_N}\right)\frac{C_LR}{\sqrt N}.\quad} \tag{16}
\]
Proof: \(\sigma_N\|P_Nh\|\le\|\mathcal T h\|+e_N\|(I-P_N)h\|\). Integration by parts and the endpoint trace inequality give \(|h_n|\le C_L\|h\|_{H^1}/n\), including nonzero \(h(0)\); summation gives the displayed tail. The actual \(H^2\) class is included. This is a rigorous **conditional quantitative inequality**, not a computed stability modulus: \(\sigma_N\) might vanish, and no certified bounds or asymptotic relation between \(e_N\) and \(\sigma_N\) are available. Even if every \(\sigma_N>0\), (16) does not automatically converge to zero as \(N\to\infty\). If, as an additional unverified condition, there exists a sequence \(N_j\to\infty\) with \((1+e_{N_j}/\sigma_{N_j})/\sqrt{N_j}\to0\), then (16) proves restricted \(H^1\)-input injectivity and supplies a quantitative modulus by optimizing over \(j\). This is a concrete separation target, not an assumed rank or demonstrated theorem for the experiment.

## 6. Duality and possible controls

For each \(f\in L^2(J)\), the unique transposition pair in (9) is defined by testing against every strong zero-initial forward source pair; this defines the boundary and temperature terminal conditions weakly. The reachable set \(\{\Pi_ow_f(0):f\in L^2(J)\}\) has closure \((\ker\mathcal T)^\perp\). It is dense in \(H\) **iff** full odd \(H\)-injectivity holds. Controls are supported only after \(\delta\), but their adjoint trajectories propagate through the earlier interval; neither delay-induced failure nor backward uniqueness is established. In particular compactness of this control-to-memory map forbids a uniform full-space lower observability bound, not density.

Under the previously proved sign condition \(C_+=\operatorname{sgn}(\gamma)S\ge0\) on the whole interval \((0,t_1)	imes(0,L/2)\), with \(t_1>\delta\), and nonnegative controls supported in \(J\cap(0,t_1)\), the initial projected memory is in the appropriate non-strict dual cone. That does not assert signs of individual \(z_f,w_f\), strict pairing, or all-input separation. A strict pairing against each positive input would exclude only the sign cone; two signed components may cancel. A restricted smooth-class observability estimate would require a proved modulus such as (16) with verified constants, not an assumed cone result. Density in \(H\) implies separation of \(X\subset H\); separation of \(X\) alone does not imply \(H\)-density because a nonzero \(H\) kernel element may not lie in \(X\).

## 7. Physical meaning and reproducible diagnostic

Even a proof that \(\mathcal T\) is injective would give only linearized qualitative identification. A nonlinear local inverse needs an actual nonlinear forward map on a specified admissible neighborhood, Fréchet differentiability in compatible topologies, and a separate nonlinear stability or inverse theorem. The standard Banach inverse function theorem requires a boundedly invertible derivative between the chosen spaces; the compact infinite-dimensional derivative cannot be bounded below on full \(H\). Qualitative injectivity of a derivative alone does not guarantee nonlinear local injectivity. The modulo-kernel compact-class modulus is not an explicit logarithmic rate. The actual sufficient sign test is
\[
|b|r\theta_*-|b|r\|y_b(t)\|_\infty-2k\|w_b(t)\|_\infty>0, \tag{17}
\]
which gives \(S\gamma>0\) there. Initial continuity yields a positive interval near zero, but does not prove it overlaps \(J\). Physical \(a,k,b,c,\kappa,\lambda,\theta_*,L,g_*\), consistent units and existing data-only existence constants are needed to evaluate (17) and its dimensionless version; numerical values are absent.

A diagnostic protocol, not a proof:

```text
INPUT: verified dimensional parameters and units, active sinusoidal load,
       exact initial/base/boundary conditions, T=10/lambda, delta=T/100,
       chosen space/time discretizations, and observation noise model.
1. Check the stated sufficient base-existence inequalities; if unverified, label
   all subsequent runs conditional. Solve the actual active nonlinear base.
2. Solve the full variable-coefficient linearized PDE–ODE for odd inputs in the
   fixed input topology. Retain e^{-mu t}h and the entire memory history.
3. Independently refine base, PDE mesh, time step, and boundary-flux quadrature;
   compare primal flux and adjoint-duality calculations in L2(delta,T).
4. Assemble finite Gram matrices using basis inputs, including H2-odd functions
   with nonzero endpoint traces; normalize in the intended input norm.
5. Report singular values with independently estimated discretization error,
   data noise, and basis/truncation tail bounds separately. Refine all of them.
6. Compare small singular vectors across refinements and estimate their actual
   residuals in the continuum equations; do not declare an exact zero from a
   small singular value or a convergent-looking finite-rank null vector.
7. For a candidate exact h, require an analytical residual and zero output proof
   for all t in J and the actual coefficients, not merely computed samples.
```
Sine bases alone are dense in \(H\), but their finite sums have zero endpoints and do not approximate all \(H^2_o\) inputs in the \(H^2\) norm. This distinction matters for a physical-norm singular-value study. No computation, invented parameters or numerical ranks are reported.

## 8. Primary-theorem checks

The search was narrow and not exhaustive. The actual theorem text and cited proof passages were inspected; proof dependency chains not independently checked are identified.

* **P. Gaitan**, “Inverse Conductivity Problem for a Parabolic Equation using a Carleman Estimate with One Observation,” [arXiv:0706.1422](https://arxiv.org/html/0706.1422), Assumption 2.1 and Theorem 2.2: the weight is \(e^{-s\eta}\), with \(\eta=(e^{2\lambda K}-e^{\lambda\beta(x)})/[(t-t_0)(T-t)]\), a \(C^4\) noncritical spatial weight and boundary sign condition. The displayed estimate assumes time-independent conductivity, high-regularity \(q\), and retains the scalar residual and an observed boundary derivative. The source is itself a recalled theorem; its underlying source proof was not separately checked here. It does not prove a coupled estimate for the actual time-dependent principal coefficient and independent \(SP\).
* **J. Apraiz, R. Lecaros and S. Zamorano**, “A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations,” [arXiv:2610.26157](https://arxiv.org/html/2610.26157), Lemma 2.2 and its Schur-kernel proof: a centered time weight gives an \(s^{-1}\) squared Volterra term **plus** an \(s^{-1/2}\) squared center-time snapshot. This is the mechanism independently reproduced in (11), not an endpoint-only result that removes our snapshot. Their Theorem 2.3 includes an interior observation and snapshot for a different Kelvin–Voigt operator.
* **D. P. Jha and R. K. George**, “Observability and Null Controllability for Parabolic Systems with Delay and Memory,” [arXiv:2506.22221](https://arxiv.org/html/2506.22221), Lemma 3.5 and Proposition 3.8: the ODE estimate assumes zero initial auxiliary memory, moving interior observation and specific weight hypotheses; its proof invokes a previous moving-control estimate. The coupled proposition uses a constant Laplacian and a remainder. It does not identify an arbitrary delayed memory snapshot from one endpoint.
* **Guillaume Olive**, “Boundary approximate controllability of some linear parabolic systems,” [arXiv:2609.09982](https://arxiv.org/html/2609.09982), Theorem 1.1 and appendix proof: an autonomous \(C_0\) generator with compact resolvent and complete adjoint root vectors supports a Fattorini spectral test; the proof uses root-subspace projection and analytic resolvents. The actual nonautonomous PDE–ODE system has not been shown to possess those hypotheses, and finite-time analyticity is not established.

None of these sources is claimed to preclude a different valid continuation or moment argument. No full literature priority or publication claim is made.

## 9. Required status table

| Mathematical question | Verdict | Exact scope |
|---|---|---|
| Volterra operator factorization | **PROVED** | (6), within the inherited sufficient forward hypotheses. |
| Bounded inverse of \(I-\mathscr V\) | **PROVED** | Arbitrary \(g\in\mathscr E_0\), source bound and coupled uniqueness above. |
| Actual boundary asymptotics | **NOT ESTABLISHED** | Only state asymptotics (7)–(8); frozen half-line is diagnostic. |
| Coupled boundary unique continuation | **NOT ESTABLISHED** | Weighted snapshot and actual nonautonomous scalar estimate unresolved. |
| Delayed-state injectivity | **NOT ESTABLISHED** | Fredholm and conditional Neumann criterion only. |
| Infinite moment completeness | **NOT ESTABLISHED** | Bessel/not-Riesz proved; synthesis injectivity and output completeness open. |
| Adjoint range density | **NOT ESTABLISHED** | Equivalent to the original exact kernel question. |
| Approximate controllability | **NOT ESTABLISHED** | Specific adjoint memory projection has unproved dense range. |
| Full odd-channel injectivity | **NOT ESTABLISHED** | No proof from any route above. |
| Exact nonzero invisible state | **NOT CONSTRUCTED** | No candidate satisfies actual active coefficients and vanishing output. |
| Quantitative conditional stability | **CONDITIONAL** | (16) holds if the actual finite \(\sigma_N>0\); no values or decaying modulus verified. |
| New mathematical theorem | **NOT ESTABLISHED** | Structural consequences derived here; priority and novelty not demonstrated. |
| New foundational continuum theory | **REFORMULATE** | No new constitutive principle or foundation. |

The most concrete independent targets are: prove a coupled graph separation estimate controlling the snapshot in (11), or certify the finite-section quantities in (16) with a rate sufficient to separate the \(H^2_o\) input class. Either could fail; neither is verified for the actual experiment. Dr. Gupta makes the final research decision.
