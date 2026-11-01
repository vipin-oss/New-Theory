# Exact kernel of the active odd observation map

**Date:** 1 November 2026
**Verdict: NOT ESTABLISHED.** Neither exact injectivity on the frozen odd \(H^2\) input space nor a nonzero exact kernel element has been proved. This investigation derives a legitimate integrated boundary identity, an exact coupled infinite moment system, and a Fredholm property of the correlated delayed memory map. None supplies the missing completeness or density property. No boundary-to-interior UC theorem is assumed, and none is asserted necessary for injectivity.

This is a single-agent Arena investigation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. The latest odd-channel independent audit and the preceding odd-channel, regularity-updated, and boundary-UC reports were reviewed. This is a direct calculation, not a new broad literature or Carleman search. No new continuum theory or demonstrated novelty is claimed.

## 1. Frozen problem, input topology, and observation

Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), and \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\). The active symmetric base is the actual driven solution with zero initial base memory. All fixed parameters \(a,k,\lambda,c,\kappa,L,A_0,\theta_*,M\) are positive and \(b\ne0\). Write
\[
D=a+k,\quad r=k/D,\quad\alpha=a/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad\gamma=\lambda\beta,\quad d=b^2/D,\quad Qf=f-\bar f.
\]
The established sufficient assumption is \(0<q=|g_*|/L<s_*\); it has not been numerically verified for the unspecified parameters. For
\[
X_o=\{h\in H^2(I):h(L-x)=-h(x)\},\qquad H_o=\{h\in L^2(I):h(L-x)=-h(x)\},
\]
the actual odd linearized fields satisfy
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\\
P_t=-\mu P+\gamma Y,\\
Y(\cdot,0)=0,\quad P(\cdot,0)=h,\\
Y(0,t)=Y(L,t)=0,
\end{cases}\tag{1}
\]
where
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\lambda\beta\theta_b+2k\lambda\beta w_b.\tag{2}
\]
The only observation used is
\[
\mathcal T_oh=2A_0\kappa\,Y_x(0,\cdot)|_J.\tag{3}
\]
Oddness imposes \(Y_x(L,t)=Y_x(0,t)\) for a.e. \(t\); consequently zero flux at \(0\) also gives zero flux at \(L\), but it gives no interior vanishing by itself. The memory input has **no spatial Dirichlet condition** in \(X_o\): oddness relates its endpoint values, it does not set them to zero.

For each \(h\in X_o\), the established class and estimate are
\[
\begin{gathered}
Y\in\mathcal E_T:=H^1(0,T;L^2)\cap L^2(0,T;H^2\cap H^1_0)\cap C([0,T];H^1_0),\\
P\in H^1(0,T;L^2)\cap C([0,T];L^2),\qquad
\|Y\|_{\mathcal E_T}+\|P\|_{H^1_tL^2_x}\le C_E\|h\|_2.
\end{gathered}\tag{4}
\]
At positive times \(M_b\) and \(A=\kappa/M_b\) are spatially Lipschitz and temporally \(3/4\)-Hölder in the separate uniform senses, \(M_b\) is uniformly positive, \(S\in L^\infty\), and
\[
B\in L^6(J\times I)\cap L^\infty(J;L^2(I))\cap L^2(J;L^\infty(I)).\tag{5}
\]
The earlier base construction also gives continuous \(S\) on the closed cylinder. No claim of \(B\in L^\infty\) or a bounded time derivative of \(M_b\) is made. Since \(Y\in L^2_tH^2_x\), its endpoint derivative is a well-defined \(L^2_t\) trace.

The estimate and density of \(X_o\) in \(H_o\) extend the linear solution map and (3) continuously to \(H_o\). This is an analytic extension of the linearized operator, not a claim that all \(L^2\) inputs are nonlinearly admissible. All conclusions about \(X_o\) below retain its original topology and arbitrary endpoint values. Denote the extension again by \(\mathcal T_o\).

## 2. Exact zero-observation consequences and boundary traces

Assume for the remainder of this section that \(\mathcal T_oh=0\), equivalently \(Y_x(0,\cdot)=0\) in \(L^2(J)\). The imposed Dirichlet trace is zero at both ends. These are statements about Sobolev traces, not pointwise classical Cauchy data. Reflection gives the same zero normal derivative at \(L\). Neither condition says \(Y=0\) in \(I\).

The PDE is an equality in \(L^2(J\times I)\). In general \(Y_t\) and \(Y_{xx}\) are only \(L^2\) in space-time, so the available hypotheses give **no spatial endpoint trace** for either. Multiplying by the bounded \(M_b\) does not create one. Although the equation equates their difference to \(BY+SP\), it does not license taking separate endpoint values of its \(L^2\) terms. In divergence form
\[
Y_t-(AY_x)_x=VY+CP-A_xY_x,\quad V=B/M_b,\ C=S/M_b,\tag{6}
\]
\(AY_x\in L^2(J;H^1(I))\) has a boundary trace, but its spatial derivative is merely \(L^2\); this does not supply a trace of \((AY_x)_x\). The plus sign is obtained if \(A_xY_x\) is moved to the left.

There is additional structure for the *products*, which must not be confused with a boundary PDE. First, on \(J\), \(B\in L^2_tL^\infty_x\) and \(Y\in L^\infty_tH^1_0\), so for a.e. \(x\)
\[
\|B(x,\cdot)Y(x,\cdot)\|_{L^2(J)}
\le \sqrt{x}\,\|Y\|_{L^\infty_tH^1_x}\|B\|_{L^2_tL^\infty_x}.\tag{7}
\]
Thus \(BY\) has a zero **essential cross-section limit** in \(L^2_t\) as \(x\downarrow0\), even though \(B\) need not have a boundary trace. For the actual \(h\in X_o\), the Bochner formula
\[
P(t)=e^{-\mu t}h+\gamma\int_0^t e^{-\mu(t-r)}Y(r)\,dr\tag{8}
\]
and \(Y\in L^1_tH^2_x\) imply \(P\in C([0,T];H^2(I))\). With the established continuous representative of \(S\), \(SP\) has a continuous boundary value; specifically
\[
P(0,t)=e^{-\mu t}h(0),\qquad P(L,t)=e^{-\mu t}h(L)=-e^{-\mu t}h(0).\tag{9}
\]
The integral in (8) has zero endpoint trace because \(Y(r)\in H^1_0\) a.e. This calculation is valid for \(H^2\) input, not automatically for an arbitrary \(H_o\) input. Equations (7)–(9) do **not** imply \(S(0,t)P(0,t)=0\): no separate trace is available for \(M_bY_t\) or \(Y_{xx}\), and the unknown source can be balanced by them. Thus even \(h(0)=0\) has not been deduced.

The zero Dirichlet trace and zero flux may each be differentiated as a time distribution: the derivatives of those **trace functions** are zero. However, \(Y_t\in L^2_{t,x}\) has no justified spatial trace, and \(Y_x(0,\cdot)\in L^2(J)\) has no established classical time derivative or identified trace of \(Y_{xt}\). Hence the distributional differentiation does not justify substituting \(Y_t(0,t)=0\) or \(Y_{xt}(0,t)=0\) into the PDE. No extra boundary smoothness is assumed.

### A genuine weak spatial boundary identity

For any fixed \(\psi\in H^2(I)\), multiply (1) by \(\psi\) and integrate over \(I\). For a.e. \(t\), the 1-D integration-by-parts identity, using the Dirichlet traces of \(Y\), yields
\[
\begin{aligned}
\langle M_bY_t,\psi\rangle
&-\kappa\langle Y,\psi''\rangle
+\kappa Y_x(0,t)\psi(0)-\kappa Y_x(L,t)\psi(L)\\
&=\langle BY+SP,\psi\rangle.\tag{10}
\end{aligned}
\]
All scalar functions in (10) belong to \(L^2(J)\), since \(BY,SP,M_bY_t\in L^2\) and endpoint derivatives are in \(L^2_t\). The trace signs follow from \(\langle Y_{xx},\psi\rangle=[Y_x\psi]_0^L+\langle Y,\psi''\rangle\). No time derivative of \(M_b\) is used. Taking, for example, \(\psi(x)=1-x/L\), \(\psi(0)=1\), \(\psi(L)=0\), gives the exact boundary representation
\[
\kappa Y_x(0,t)=\langle BY+SP,\psi\rangle-\langle M_bY_t,\psi\rangle+\kappa\langle Y,\psi''\rangle.\tag{11}
\]
On the zero-observation set, the right side is zero in \(L^2(J)\). More generally (10) has no boundary terms for every \(\psi\in H^2\) when the odd observation vanishes. These are valid integral constraints, but the three unknown interior terms can cancel. Testing with a single \(\psi\), or all such \(\psi\), has not yielded \(h=0\); the latter merely restates the coupled equation with zero boundary traces, without proving injectivity.

## 3. Complete odd moments: equations and convergence

Let
\[
\phi_n(x)=\sqrt{2/L}\sin(2n\pi x/L),\quad \rho_n=(2n\pi/L)^2,\quad n\ge1.
\]
These form a complete orthonormal basis of \(H_o\). For \(h\in X_o\) put
\[
u_n(t)=\langle Y(t),\phi_n\rangle,\quad p_n(t)=\langle P(t),\phi_n\rangle,\quad h_n=\langle h,\phi_n\rangle.
\]
Testing the **original**, undivided equation by \(\phi_n\), whose endpoint values are zero, gives for a.e. time
\[
\sum_{m\ge1}M_{nm}(t)u_m'(t)+\kappa\rho_nu_n(t)
=\langle B(t)Y(t),\phi_n\rangle+\sum_{m\ge1}S_{nm}(t)p_m(t),\tag{12}
\]
\[
p_n'(t)=-\mu p_n(t)+\gamma u_n(t),\quad u_n(0)=0,\quad p_n(0)=h_n,\tag{13}
\]
where \(M_{nm}=\langle M_b\phi_m,\phi_n\rangle\) and \(S_{nm}=\langle S\phi_m,\phi_n\rangle\). The first moment is the \(n=1\) instance; it is not closed because its mass and source projections contain all other modes. Equation (13) integrates to
\[
p_n(t)=e^{-\mu t}h_n+\gamma\int_0^t e^{-\mu(t-r)}u_n(r)\,dr.\tag{14}
\]
Putting (14) into (12) produces an infinite **coupled** Volterra system: \(S(t)\) multiplies the memory integral at the current time, and \(M_b,B,S\) are spatially varying active coefficients. The underlying \(Q(y_b)_t\) appears inside \(B\); no modal diagonalization, triangular structure, or nonzero off-diagonal coefficient is assumed or proved. \(M_b(t)\) is a positive bounded multiplication operator and thus invertible on \(H_o\), but this does not make its matrix diagonal or decouple the system.

The convergence is substantive, not a finite-truncation heuristic. The sine projections \(u=(u_n)\) satisfy \(u\in H^1(0,T;\ell^2)\), and \(\sum\rho_n^2|u_n|^2\in L^1_t\) by \(Y\in L^2_t(H^2\cap H^1_0)\). Similarly \(p\in H^1_t\ell^2\). For each fixed \(n\), the \(M\)-series converges by Parseval to \(\langle M_bY_t,\phi_n\rangle\) and the \(S\)-series to \(\langle SP,\phi_n\rangle\). The \(B\) term is intentionally written as an inner product: \(BY\in L^2(J\times I)\), while \(B\) need not define a uniformly bounded spatial multiplier at every time. If desired, the partial sums of \(Y\) converge to \(Y\) in \(L^\infty_tH^1_x\) after using the compact time-continuous image and spectral approximation; the estimate (5) then justifies the \(BY\) projections in \(L^2(J)\). No conclusion depends on an unproved infinite matrix inversion.

For the output, spectral projections \(Y_N=\sum_{n\le N}u_n\phi_n\) converge to \(Y\) in \(L^2(0,T;H^s(I))\) for \(3/2<s<2\). This follows from the Dirichlet spectral characterization and interpolation between \(L^2\) and \(H^2\cap H^1_0\). The derivative trace is continuous on \(H^s(I)\), hence
\[
Y_x(0,\cdot)=\lim_{N\to\infty}\sum_{n=1}^N \phi_n'(0)u_n(\cdot)
\quad\text{in }L^2(J).\tag{15}
\]
Thus the zero observation is precisely the vanishing of this limit, not the vanishing of every \(u_n\). The simultaneous use of (12)–(15) is exact, but no completeness theorem for this variable-coefficient coupled family is proved here. In particular, finite modal uniqueness or increasingly small singular values would not decide the infinite exact kernel.

## 4. The pre-delay trajectory and correlated memory state

The exact state at the observation start is
\[
P(\delta)=e^{-\mu\delta}h+\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)\,dr,\qquad Y(\delta)=\mathcal Y_\delta h.\tag{16}
\]
Both depend on the *same* input and on the actual evolution on \((0,\delta)\); \(P(\delta)\) is neither an arbitrary independent state nor a known zero state. Restricting (8) to \(t\ge\delta\), substitution into (1) yields
\[
\begin{aligned}
M_bY_t-\kappa Y_{xx}={}&BY+S e^{-\mu(t-\delta)}P(\delta)\\
&+\gamma S(t)\int_\delta^t e^{-\mu(t-r)}Y(r)\,dr,\qquad Y(\delta)=\mathcal Y_\delta h.
\end{aligned}\tag{17}
\]
Together with (16), this is an exact inverse-source formulation. The measured zero flux imposes (10)–(15) for \(t\in J\), now with source (17), but these identities do not separate the correlated source from the nonzero temperature trajectory. The observation starts only at \(\delta\); no zero observation on \((0,\delta)\) follows.

There is nevertheless a precise Fredholm consequence. Define \(D_\delta:H_o\to H_o\), \(D_\delta h=P(\delta)\). From (16),
\[
D_\delta=e^{-\mu\delta}I+K_\delta,\qquad
K_\delta h=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y[h](r)\,dr.\tag{18}
\]
By (4), \(K_\delta\) maps bounded \(L^2\) input sets into bounded \(H^2(I)\) sets: the integral is a Bochner \(H^2\) integral and \(\|K_\delta h\|_{H^2}\le |\gamma|\sqrt\delta C_E\|h\|_2\). Since \(H^2(I)\Subset L^2(I)\), \(K_\delta\) is compact on \(H_o\). Thus \(D_\delta\) is Fredholm of index zero and \(\ker D_\delta\) is finite-dimensional. In particular, if a separate argument ever established \(P(\delta)=0\), it would only place \(h\) in this finite-dimensional kernel; it would not automatically give \(h=0\). \(Y(\delta)\) is also a compact map \(H_o\to H_o\), since (4) bounds it in \(H^1_0\). The combined state map's zero set is a subspace of \(\ker D_\delta\), hence finite-dimensional, but its triviality has not been proved.

As a check on what additional quantitative information could close just this pre-delay step, \(Y(0)=0\) and (4) imply \(\|Y(r)\|_2\le\sqrt r\,C_E\|h\|_2\), so
\[
\|K_\delta\|_{H_o\to H_o}\le\tfrac23|\gamma|C_E\delta^{3/2}.\tag{19}
\]
If the **additional, unverified** inequality \(\tfrac23|\gamma|C_E\delta^{3/2}<e^{-\mu\delta}\) held for an established constant \(C_E\), the Neumann series would make \(D_\delta\) invertible. This is a conditional observation, not a permitted change of \(\delta\), load, coefficients, or a claim that the inequality holds. Even then, zero flux has not been shown to imply \(P(\delta)=0\), so (19) alone does not prove observation injectivity.

## 5. Adjoint and output-family route without assuming UC

The bounded extended map has a genuine Hilbert adjoint \(\mathcal T_o^*:L^2(J)\to H_o\), defined by
\[
\langle\mathcal T_oh,f\rangle_{L^2(J)}=\langle h,\mathcal T_o^*f\rangle_{H_o}.\tag{20}
\]
The abstract adjoint exists by Riesz representation and the bound in (4); no unproved boundary-value problem is needed for (20). Define \(\psi_n=\mathcal T_o\phi_n\). Then \(\langle\mathcal T_o^*f,\phi_n\rangle=\langle f,\psi_n\rangle\), and for every \(h\in H_o\),
\[
\mathcal T_oh=\lim_{N\to\infty}\sum_{n=1}^N h_n\psi_n\quad\text{in }L^2(J).\tag{21}
\]
Here \(\phi_n\in X_o\), but their finite spans are not dense in \(X_o\) in its \(H^2\) norm because they vanish at endpoints; (21) follows instead from completeness in \(L^2_o\) and boundedness. This point matters because a general \(h\in X_o\) may have nonzero endpoint values.

The exact abstract equivalences are
\[
\ker(\mathcal T_o:H_o\to L^2(J))=\{0\}
\iff \overline{\operatorname{ran}\mathcal T_o^*}^{\,H_o}=H_o,
\tag{22}
\]
and
\[
\ker(\mathcal T_o|_{X_o})=\{0\}
\iff X_o\cap(\operatorname{ran}\mathcal T_o^*)^\perp=\{0\}.\tag{23}
\]
Thus full \(H_o\)-density is sufficient but stronger than the actual \(X_o\) requirement. A rigorous PDE-adjoint strategy would need a boundary transposition theorem for this nonautonomous system, including the delayed interval and the \(L^6\) coefficient, to identify \(\mathcal T_o^*f\) with an initial adjoint memory state. It would then need to prove the range condition (23), or the stronger (22). Neither follows just from writing a formal backward parabolic equation or from (20). The coupled moment family (21) offers a second direct formulation: prove that for every \(h\in X_o\), convergence of the indicated series to zero in \(L^2(J)\) entails \(h=0\). Complete spatial sines do not by themselves imply this independence of their *time-output* images.

The earlier compactness result makes this distinction important: \(\mathcal T_o:H_o\to L^2(J)\) is compact, and normalized odd sine inputs have output tending to zero. Compactness prohibits a uniform lower bound in the strong input norm, but it is compatible with both injective and noninjective compact maps. It proves neither an exact kernel element nor its absence. No stronger boundary observation, time derivative of the output, or altered input norm has been substituted.

## 6. Smallest missing result and outcome

A sufficient theorem tailored to the actual question is the following **qualitative coupled-output completeness statement**:

> Under the fixed active base, \(0<q<s_*\), the solution class (4), coefficients (2), prescribed \(T,\delta\), and the exact odd basis above, if \(h\in X_o\) and the \(L^2(J)\) limit in (21) is zero, then \(h=0\).

Everything needed to *formulate* it—the active solution map, basis completeness in \(H_o\), and convergence—is verified in §§1 and 3–5. The missing content is the independence of the actual output family for all coefficient sequences generated by \(X_o\); it is not implied by completeness of the sine basis, (12)–(15), or compactness. A concrete stronger sufficient result would construct, for each \(n\), a sequence \(f_{n,j}\in L^2(J)\) such that \(\|\mathcal T_o^*f_{n,j}-\phi_n\|_{L^2(I)}	o0\). Then (20) forces every Fourier coefficient of an unobserved \(h\) to vanish. The functions may have unbounded norms; no uniform observability estimate is required. Their existence for the actual active coefficients and the observation supported in \(J\) is the unproved part. An adjoint proof may instead establish the precisely equivalent restricted range condition (23), after a justified transposition construction if one wants PDE formulas. An alternative structured-source theorem could prove injectivity directly for (17) with (16), retaining the correlated temperature state and true pre-delay history. None needs to first establish boundary-to-interior UC, and none has been established here.

The three logically distinct possibilities remain: (i) the exact kernel is trivial; (ii) a nonzero \(h\in X_o\) solves the **full** active system with zero flux on \(J\); or (iii) neither is proved. The present result is **(iii)**. No exact counterexample is constructed, no strong observability or nonlinear inverse conclusion is claimed, and the conditional pre-delay Fredholm result does not decide between (i) and (ii).

**Final verdict: NOT ESTABLISHED.**
