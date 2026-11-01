# Investigation of the actual two-part separation problem

**Date:** 1 November 2026. **Decision: REFORMULATE.** Neither injectivity of the actual remainder on \(H_0\) nor exclusion of \(b_*\) from its exact range is proved or disproved. No physical invisible state is constructed. The strongest result below is an exact, equation-specific adjoint criterion for each condition, including a dual **unbounded-ratio** criterion for exact range exclusion; it is a rigorous reduction, not a new separation theorem. We also prove what full interior temperature data would imply under the inherited active-base initial nondegeneracy, and isolate why this does not follow from the prescribed endpoint flux. The prior expansion provides no established second mode-dependent term. All system-specific claims are conditional on the inherited active-base and strong forward/transposition hypotheses; the sufficient small-load condition has not been numerically verified.

Dr. Vipin Gupta is Principal Researcher and final decision-maker, ChatGPT is designated Independent Scientific Supervisor and Auditor, and Arena is Research Scholar / Builder / Literature Investigator. This is Arena's analysis, not independent human certification. Direction 1 remains rejected; this is not a new foundational continuum theory or a claim of publication priority.

## 1. Fixed active system and definitions

Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\); the fixed nonzero actuation is \(g_*\sin^2(\pi t/T)\). Put
\[
D=a_{\rm mat}+k,\quad r=k/D,\quad \alpha=a_{\rm mat}/D,\quad \beta=b/D,\quad
\gamma=\lambda\beta,\quad\mu=\lambda\alpha,\quad d=b^2/D,\quad Qv=v-\bar v.
\]
The actual reflection-even base coefficients, not independently prescribed or frozen, are
\[
M=c+d\theta_b,\qquad S=\lambda\alpha(br\theta_b-2kw_b),\qquad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{1}
\]
For \(H=L^2_o(I)\) (odd reflection about the midpoint), \(V=H^1_0(I)\cap H\), \(X=H^2(I)\cap H\), the fixed system and observation are
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\ P(\cdot,0)=h,\quad Y(0,t)=Y(L,t)=0,\quad
\mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{2}
\]
There is no spatial endpoint condition on \(h\) or \(P\). All material parameters and memory feedback are retained.

**Inherited conditional hypotheses.** Assume \(0<m_0\le M\le m_1\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\), \(S\in C_tH^1_x\cap H^1_tL^2_x\cap L^2_tH^2_x\), evenness, and the inherited strong forced solution estimate for \(L^2\) sources and \(H^1_0\) initial temperature, including the full-space forced problem used for transposition. In particular \(Y\in H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\), \(P\in H^1_tL^2_x\), and \(\mathcal T:H\to Z=L^2(J)\) is Hilbert–Schmidt. The prior audit derives these consequences from the stated assumptions; it does not establish experimental parameters, global admissibility, or the small-load condition. Strong-source transposition below uses the same forced forward theorem. No temporal analyticity is assumed.

Set \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(h_n=(h,\phi_n)\), and
\[
\ell=1-2x/L,\quad g=\sum_n\phi_n/q_n=\frac{\ell}{2\sqrt{2/L}},\quad
\Lambda h=(h,g)=\sum_n h_n/q_n,\quad H_0=g^\perp,\quad u=q_1\phi_1. \tag{3}
\]
The equality for \(g\) follows from \((\ell,\phi_n)=2\sqrt{2/L}/q_n\), and \(\Lambda u=1\). The inherited asymptotic for the **actual** solutions \((Y_n,P_n)\) gives
\[
k_n=\mathcal T\phi_n=\frac{a_J}{q_n}+\rho_n,\quad
 a_J(t)=2A_0\sqrt{2/L}\,e^{-\mu t}S(t,0),\quad
\|\rho_n\|_Z\le C_\eta q_n^{-3/2+\eta},\quad0<\eta<1/2. \tag{4}
\]
Define \(\mathcal Rh=\sum_n h_n\rho_n\), and \(b_*=\mathcal Tu=a_J+\mathcal Ru\). Cauchy–Schwarz and square summability yield convergence of both series in (3)–(4), a Hilbert–Schmidt \(\mathcal R:H\to Z\), and the exact, all-input identity
\[
\boxed{\mathcal T=a_J\Lambda+\mathcal R.} \tag{5}
\]
It holds first for finite sums and then for all \(H\) by continuity; \(\mathcal R=\mathcal T-a_J\Lambda\) is therefore the actual remainder, not a guessed family. Let
\[
A=\mathcal R|_{H_0}=\mathcal T|_{H_0},\qquad b=b_*=\mathcal Tu. \tag{6}
\]
Here \(A\) denotes an operator, not a material parameter. For \(h=v+cu\), \(v\in H_0\), \(c=\Lambda h\), the equation is \(\mathcal Th=Av+cb\). Consequently \(\ker\mathcal T=\{0\}\) iff \(\ker A=\{0\}\) and \(b\notin\operatorname{ran}A\). These are exact range statements, not statements about its closure.

## 2. Governing-equation investigation of \(\ker A\)

For arbitrary \(v\in H_0\), the memory equation is exactly
\[
P(t)=e^{-\mu t}v+\gamma\int_0^t e^{-\mu(t-r)}Y(r)dr,
\]
so the actual system is the zero-initial-temperature Volterra equation
\[
MY_t-\kappa Y_{xx}=BY+e^{-\mu t}Sv+
\gamma S(t)\int_0^t e^{-\mu(t-r)}Y(r)dr. \tag{7}
\]
Every term is in \(L^2_{t,x}\): \(S\) is bounded, \(Y\in C_tH^1_0\) and \(B\in L^2\). The condition \(Av=0\) is exactly \(Y_x(0,t)=0\) for almost every \(t\in J\), assuming the nonzero physical factor \(2A_0\kappa\). It also implies \(Y_x(L,t)=0\) by odd reflection. Both Dirichlet and derivative traces are legitimate, but \(Y_t\), \(Y_{xx}\), \(B\), and \(v\in L^2\) need not possess boundary traces. Therefore (7) cannot be evaluated at \(x=0\) to deduce a boundary identity for \(v\). Nor does the overdetermined boundary data make its inhomogeneous right-hand side vanish.

The condition \((v,g)=0\) cancels only the explicitly identified rank-one *output functional*. It does not cancel \(e^{-\mu t}S(t,x)v(x)\) pointwise, nor diagonalize the feedback. Projecting onto \(\phi_m\) gives
\[
(MY_t,\phi_m)+\kappa q_m^2(Y,\phi_m)=(BY+SP,\phi_m),\qquad P_m'+\mu P_m=\gamma Y_m. \tag{8}
\]
Multiplication by actual nonconstant \(M,B,S\) couples modes, and \((MY_t,\phi_m)\) is not a scalar mass times \(Y'_m\). No triangular system, independent moment family, or infinite coefficientwise vanishing follows. Finite sine sums are dense in \(H\), and projected finite sums can approximate \(H_0\), but knowing injectivity on a dense subspace would **not** imply injectivity on its closure.

**What interior recovery would give, and its limitation.** For the inherited active base, \(S(0,x)=\lambda\alpha br\theta_*\ne0\) uniformly, since \(\theta_b(0)=\theta_*\), \(w_b(0)=0\), and the frozen signs include \(b\ne0\). Because \(S\in C_tH^1_x\hookrightarrow C_tC_x\), there are \(\epsilon,s_0>0\) with \(|S|\ge s_0\) on \([0,\epsilon]\times\bar I\), with \(\epsilon\le T\). This is conditional on the inherited base and its initial data, not on numerically verified small loading. Define
\[
D_Y=MY_t-\kappa Y_{xx}-BY-\gamma S(t)\int_0^t e^{-\mu(t-r)}Y(r)dr.
\]
Equation (7) gives \(D_Y=e^{-\mu t}Sv\) in \(L^2_{t,x}\). Then the actual coefficient satisfies
\[
w(x):=\int_0^T e^{-2\mu t}|S(t,x)|^2dt\ge s_0^2\int_0^\epsilon e^{-2\mu t}dt>0\quad\text{for every }x. \tag{9}
\]
Full interior knowledge of \(Y\) therefore determines
\[
v(x)=\frac{\int_0^T e^{-\mu t}S(t,x)D_Y(t,x)dt}{w(x)}\quad\text{a.e. }x. \tag{10}
\]
This is proved by Fubini and (7), with no division where \(w=0\). It also proves that \(Y\equiv0\) on the full space–time cylinder implies \(v=0\) under (9). The proved lower bound gives \(\|v\|_{L^2_x}\le (\inf w)^{-1/2}\|D_Y\|_{L^2_{t,x}}\). This is conditional on existence of the inherited base, and applies to full-time interior data in the strong solution topology, not just to data on \(J\). Most importantly, **one delayed endpoint flux does not supply \(Y\)**, and no boundary-to-interior theorem for (7) has been established. Equation (10) is an additional-data implication, not a solution of the assigned inverse problem.

At delay \(\delta\), the true state is \((Y(\delta),P(\delta))\), with
\[
P(t)=e^{-\mu(t-\delta)}P(\delta)+\gamma\int_\delta^t e^{-\mu(t-r)}Y(r)dr,\quad
P(\delta)=e^{-\mu\delta}v+\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr. \tag{11}
\]
Neither coordinate is known from zero endpoint data. The pre-delay history in (11) cannot be set to zero, and the Fredholm property of the memory-state map does not imply injectivity of boundary observation.

## 3. Coupled transposition and the specific adjoint tests

For zero-initial strong forced solutions of
\[
F=My_t-\kappa y_{xx}-By-Sp,\qquad G=p_t+\mu p-\gamma y, \tag{12}
\]
the forced estimate and boundary trace bound make \((F,G)\mapsto 2A_0\kappa\int_J f y_x(0)dt\) bounded on \(L^2_{t,x}\times L^2_{t,x}\). Riesz gives \((z_f,w_f)\in L^2_{t,x}^2\) satisfying
\[
\iint(Fz_f+Gw_f)=2A_0\kappa\int_J f(t)y_x(t,0)dt. \tag{13}
\]
Testing with compactly supported smooth pairs yields, in distributions,
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\qquad
-w_{f,t}+\mu w_f-Sz_f=0. \tag{14}
\]
The \(-\gamma w_f\) and \(-Sz_f\) signs follow from (12), and no \(M_tz_f\) product is separately required. Testing (13) with \(y=0\) and arbitrary memory tests proves
\[
w_f(T)=0,\quad w_f(t)=\int_t^T e^{-\mu(r-t)}S(r)z_f(r)dr\in H^1_tL^2_x,\quad
\mathcal T^*f=\Pi_o w_f(0). \tag{15}
\]
The last identity follows by subtracting \(e^{-\mu t}h\) from \(P\), making (12) have zero initial states, \(F=e^{-\mu t}Sh\), \(G=0\). For full-space tests, \(Bz_f\in L^1\), so the distributional first equation is meaningful. The rigorous boundary and temperature-terminal conditions are encoded in (13). Formally, integration by parts gives boundary contribution
\[
\kappa\int_0^T[y_x(0)z_f(0)-y_x(L)z_f(L)]dt,
\]
with \(z_f(0)=2A_0 1_J f\), \(z_f(L)=0\), and terminal \(Mz_f(T)=0\); these are not asserted as established classical traces. Projecting to odd tests gives formal boundary values \(A_0 1_J f\), \(-A_0 1_J f\), respectively. Reflection then makes the two boundary contributions add to \(2A_0\kappa\int_J fy_x(0)\), confirming the normalization.

Let \(\Pi_0=I-(\cdot,g)g/\|g\|_2^2\) and put
\[
W_f=\Pi_o w_f(0),\quad W_{0,f}=\Pi_0 W_f,\quad d_f=(u,W_f)_H=(f,b)_Z. \tag{16}
\]
Then \(A^*f=W_{0,f}\), because \(A=\mathcal T|_{H_0}\). The actual equations give the following **exact** tests:
\[
\boxed{\ker A=\{0\}\ \Longleftrightarrow\
\overline{\{W_{0,f}:f\in L^2(J)\}}^{H}=H_0.} \tag{17}
\]
The set is a linear range, and the proof is \((\operatorname{ran}A^*)^\perp=\ker A\). An equation-specific equivalent formulation is: for every nonzero \(v\in H_0\), some \(f\in L^2(J)\) has
\[
\int_0^T e^{-\mu t}\langle v,S(t)z_f(t)\rangle dt\ne0. \tag{18}
\]
This is an exact statement about the actual transposition system and the delayed controls, not a theorem that the density holds. It includes all \(v\in H_0\), not just finite sums. Constructing controls or a PDE uniqueness proof establishing (18) is the missing substantive step. Smooth coefficients alone are not claimed sufficient; the exact minimum structural assumptions on active \(M,B,S\) and their coupling are unknown.

The corresponding moment identity, valid for all \(\ell^2\) coefficients, is
\[
\sum_n v_n\int_J f(t)\rho_n(t)dt
=\int_0^T e^{-\mu t}\langle v,Sz_f\rangle dt,\quad v\in H_0. \tag{19}
\]
Convergence follows from the Hilbert–Schmidt bound. It does not exhibit independent moments: the \(z_f\)'s solve the coupled nonautonomous problem, and no biorthogonal family is derived.

## 4. Exact range exclusion: a dual criterion that does not replace range by closure

For \(A:H_0\to Z\), \(b=\mathcal Tu\), define the extended number
\[
\mathcal C_b=\sup_{f\in Z}\frac{|d_f|}{\|W_{0,f}\|_H}, \tag{20}
\]
with ratio \(+\infty\) when denominator is zero and numerator nonzero, and ratio zero when both vanish. Then, with no injectivity or closed-range assumption,
\[
\boxed{b\in\operatorname{ran}A\ \Longleftrightarrow\ \mathcal C_b<\infty;\qquad
b\notin\operatorname{ran}A\ \Longleftrightarrow\ \mathcal C_b=\infty.} \tag{21}
\]
Proof: if \(b=Av\), then \(|d_f|=|(v,A^*f)|\le\|v\|\|A^*f\|\). Conversely, if the quotient is bounded, \(L(A^*f)=(b,f)\) is well-defined (it vanishes whenever \(A^*f=0\)) and bounded on \(\operatorname{ran}A^*\). Extend continuously to its closure and apply the Hilbert-space Riesz theorem to obtain \(v\in H_0\) with \((b,f)=(v,A^*f)=(Av,f)\) for every \(f\), hence \(b=Av\). This is an exact test derived for the actual adjoint solutions in (14)–(16). It shows the specific missing estimate is **unboundedness**, not a uniform observability bound.

If \(b=Av\), then \(h=u-v\ne0\), \(\Lambda h=1\), and \(\mathcal Th=0\). Conversely any kernel element with \(\Lambda h\ne0\) rescales to this form. This would be an exact physical-system \(L^2\) invisible input, but such a \(v\) has not been found; an \(H^2\) physical input would additionally require \(v\in X\).

A **bounded** separating functional \(f\in Z\) with \(A^*f=0\), \((b,f)\ne0\) exists iff \(b\notin\overline{\operatorname{ran}A}\). Via (16), this asks for a boundary control for which \(W_f\) is a nonzero multiple of \(g\). It is a sufficient but generally stronger criterion than (21), and is not established for (14). If \(b\in\overline{\operatorname{ran}A}\setminus\operatorname{ran}A\), no bounded separator exists. Nevertheless the algebraic map \(L(Av+cb)=c\) is well-defined on \(\operatorname{ran}A+\operatorname{span}\{b\}\), zero on \(\operatorname{ran}A\) and one on \(b\); it is then necessarily unbounded in the \(Z\)-norm. This construction uses exact exclusion as a premise and does not prove it.

For a second precise exact-range diagnostic, let \((\sigma_j,v_j,z_j)\) be the nonzero singular system of compact \(A\), finite or countable, with \(Av_j=\sigma_jz_j\). Then
\[
b\in\operatorname{ran}A\quad\Longleftrightarrow\quad b\perp\ker A^*\ \text{and}\
\sum_j\frac{|(b,z_j)_Z|^2}{\sigma_j^2}<\infty. \tag{22}
\]
Proof: necessity follows from Bessel applied to any preimage. Conversely the square-summable coefficients give \(v=\sum_j(b,z_j)\sigma_j^{-1}v_j\in H_0\) and \(Av=b\) by completeness in \(\overline{\operatorname{ran}A}\). An actual-system proof would need the exact singular system or an equivalent analytic estimate; neither is available. Approximate solutions or positive finite Gram eigenvalues do not decide the infinite sum.

**Most valuable next theorem.** Under the weakest actually verified active-base assumptions, establish (18) for every nonzero \(v\in H_0\) **and** construct controls \(f_j\) satisfying
\[
\frac{|(u,W_{f_j})|}{\|\Pi_0W_{f_j}\|_H}\longrightarrow\infty \tag{23}
\]
with the conventions above. By (17) and (21) these two conclusions prove full injectivity, even if \(b\) lies in the closure of the range. Either could fail; a full counterexample requires an actual coefficient-consistent \(v\), not an abstract operator. The two clauses are equivalent to the goal and are not themselves presented as an advance proving it. A successful proof could use a coupled boundary-to-interior result, a genuinely independent moment construction, or a different route; none is asserted necessary.

## 5. Can one compute a further mode-dependent term?

The previously audited ansatz is
\[
Y_n^a=\frac{e^{-\mu t}}{\kappa q_n^2}S\phi_n,\qquad P_n^a=e^{-\mu t}\phi_n.
\]
It has the nonzero initial mismatch \(Y_n^a(0)\) and the memory error is driven by \(\gamma Y_n^a\). Its residual is
\[
F_n^a=\frac{e^{-\mu t}}{\kappa q_n^2}
\{[M(S_t-\mu S)-BS-\kappa S_{xx}]\phi_n-2\kappa S_x\phi_n'\}. \tag{24}
\]
It is \(O(q_n^{-1})\) in \(L^2\) and \(O(q_n^{-2})\) in \(L^2V'\). The established weak/strong interpolation gives only \(O(q_n^{-3/2+\eta})\) for the actual flux error, which is larger than \(q_n^{-2}\); this estimate cannot isolate any coefficient at order \(q_n^{-2}\).

A plausible **formal**, not validated, correction to cancel the dominant cosine in (24) is
\[
Y_n^{(1)}=\frac{2\sqrt{2/L}\,e^{-\mu t}}{\kappa q_n^3}
[S_x(t,x)\cos(q_nx)-S_x(t,0)\ell(x)]. \tag{25}
\]
The affine lift makes both endpoint values zero because \(S_x\) is odd and \(\cos(q_nL)=1\). Formally, \(-\kappa\partial_{xx}Y_n^{(1)}\) has leading \(+2\sqrt{2/L}e^{-\mu t}S_x\cos(q_nx)/q_n\), cancelling the leading residual in (24). However, this does **not** prove a second boundary term:

* \(S_x\in L^2_tH^1_x\) does give \(S_x(t,0)\) a.e., but (25)'s \(H^2_x\) regularity needs, for example, \(S\in L^2_tH^3_x\); its strong time derivative needs control of \(S_{xt}\) and the time derivative of the endpoint lift. These are not established by \(S\in H^1_tL^2\cap L^2_tH^2\).
* The formal boundary derivative of (25) involves \(S_{xx}(t,0)\), not defined by \(S_{xx}\in L^2_{t,x}\). Explicitly, evaluation of a second derivative is not bounded on \(H^2(I)\): smooth bumps \(s_\varepsilon(x)=\varepsilon^{3/2}\psi(x/\varepsilon)\), reflected evenly about the midpoint, have uniformly bounded \(H^2\) norm but \(|s_\varepsilon''(0)|\sim\varepsilon^{-1/2}|\psi''(0)|\). This is a functional-space obstruction, not a counterexample for the actual base.
* \(B\in L^2\) provides no \(B_x\) for integrating differentiated \(BS\) terms; \(M_t\) is not controlled by (2)'s stated \(M_x\) bounds. The active-base equations may provide further time regularity on positive-time strips under additional hypotheses, but no sufficient higher regularity or boundary trace for this calculation has been verified here. One must not differentiate \(B\) or infer a boundary value of \(M_t\) from its distributional existence.
* A legitimate corrected trial would also require its initial mismatch, its contribution to the \(P\) equation, and a forced estimate demonstrating a boundary error \(o(q_n^{-2})\) on \(J\). Simply subtracting the spatial residual does not prove that bound; delayed damping for the nonautonomous coupled evolution is itself unproved.

Even if a second term \(c(t)/q_n^2\) with a *shared* \(c\) were rigorously obtained, it would be another finite-rank leading profile, not a proof of independent columns. No actual mode-dependent coefficient, useful recurrence, or separating lower bound has been derived. We prove the stated regularity obstruction to this **particular** expansion method, not that every possible second-order asymptotic is impossible.

## 6. \(H^2\) and endpoint questions are separate

Take \(X=H^2\cap H\), \(X_0^\Lambda=X\cap H_0\), \(A_X=A|_{X_0^\Lambda}\). Since \(u=q_1\phi_1\in X\), every \(h\in X\) decomposes uniquely as \(h=v+cu\), \(v\in X_0^\Lambda\). Hence
\[
\ker\mathcal T\cap X=\{0\}\quad\Longleftrightarrow\quad
\ker A_X=\{0\}\ \text{and}\ b\notin A_X(X_0^\Lambda). \tag{26}
\]
This is strictly a restricted-class criterion: \(b\in\operatorname{ran}A\) with a preimage outside \(X\) would not alone disprove (26). Conversely \(L^2\)-injectivity implies the restricted statement, but is stronger. Neither clause of (26) is known.

For \(E(h)=h(0)\), \(E(u)=0\), so endpoint uniqueness on \(X\) is exactly the conjunction
\[
\ker A_X\subset\ker E,\qquad
\text{every }v\in X_0^\Lambda\text{ with }A_Xv=b\text{ satisfies }E(v)=0. \tag{27}
\]
The second clause is vacuous if there is no such \(v\). Proof: if \(Av+cb=0\), for \(c=0\) use the first clause; for \(c\ne0\) set \(w=-v/c\), so \(Aw=b\), and \(E(h)=-cE(w)\). The reverse follows by testing \(v\) in \(\ker A_X\) and \(u-v\) for each \(Av=b\). These are exact logical tests, not proofs of either endpoint or profile uniqueness.

If (26) is independently shown, compactness of bounded \(H^2\) sets in \(L^2\) yields a qualitative full \(L^2\) stability modulus on each bounded ball. If only (27) is shown, compactness in \(C^0\) yields a qualitative endpoint modulus. Without either, the already proved modulus is solely distance to \(\ker\mathcal T\subset H\); no explicit rate follows. No bounded output functional for \(h(0)\) exists on all \(X\), by density of zero-endpoint smooth odd functions in \(H\). Shared high-frequency profile measures \(\Lambda h=(h,g)\), not \(h(0)\).

## 7. Diagnostics and literature

No numerical experiment was run: the actual active-base coefficient functions and verified parameter values have not been supplied as numerical data. A legitimate diagnostic would first solve the prescribed nonzero-loaded base with validated coefficient errors, then solve the coupled mode problems and resolve \(q_n^{-2}\) initial layers. One would compute \(A\) on finite sections of \(H_0\), approximate \(b\), inspect both singular values and regularized least-squares solution norms, and refine space, time, trace evaluation and mode count separately. Exact finite-section error enclosures still do not prove infinite injectivity or range exclusion; an apparently divergent inverse norm or small singular value is not an exact result. No parameters or numerical rank are invented.

Targeted primary passages inspected; no exhaustive search, cited-dependency verification or priority claim:

* [Jha–George, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*](https://arxiv.org/html/2506.22221), Lemma 3.7 and Proposition 3.8: the exponential auxiliary memory starts at zero, weights and cutoff obey stated structural assumptions, and the estimate includes a moving interior observation and short-time remainder. Theorem 3.10 additionally assumes short-time energy closure; Lemma 3.13 assumes adjoint unique continuation and compactness–uniqueness. They do not provide (18) for arbitrary initial nondiffusive memory and a single delayed boundary flux. Proof passages and stated assumptions were checked; dependencies were not independently verified.
* [Apraiz–Lecaros–Zamorano, *A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations*](https://arxiv.org/html/2610.26157), Lemma 2.2 proof and Theorem 2.3: centered-time Volterra control retains a weighted center-time snapshot, and the Kelvin–Voigt result includes an interior observation. Neither snapshot nor interior observation is given by (2); no inference to (18) or (23).
* [Kian–Sambou–Soccorsi, *Logarithmic stability inequality in an inverse source problem for the heat equation on a waveguide*](https://arxiv.org/html/1612.07942), Theorem 1.2 and §1: scalar heat with \(F=\sigma(t)\beta(x)\), \(\sigma\in C^1\), \(\sigma(0)\ne0\), spatial a priori restrictions and partial boundary observations. Their introduction explicitly notes zero Cauchy data need not identify an arbitrary source. The actual \(S(t,x)v\) and unknown feedback/history are not that separated-source problem.
* [*Boundary controllability for a coupled system of degenerate/singular parabolic equations*](https://arxiv.org/html/2104.00610), Theorem 1.1 and §2 duality: a biorthogonal family for exponentials is obtained under sector, gap and summability conditions, applied to an autonomous system with two diffusive components. The actual columns have not been shown to be exponentials with those gaps; nondiffusive memory and time-dependent coupling preclude direct application.
* [Clason, *Regularization of Inverse Problems*](https://arxiv.org/html/2001.00617), Theorem 3.10 and its proof: for a compact Hilbert operator, exact solvability is characterized by orthogonality to the adjoint kernel and the Picard series. This applies to abstract compact \(A\) and justifies (22), but its actual singular data are unknown and the theorem itself gives neither part of (6).
* [Choulli–Kian, *Stability of the determination of a time-dependent coefficient in parabolic equations*](https://arxiv.org/html/1202.5392), Theorem 1: a smooth scalar parabolic problem with prescribed boundary nondegeneracy determines a time coefficient using differentiated boundary data. It is not a unique-continuation theorem for our distributed unknown initial memory and its nonautonomous feedback.

No inspected primary theorem was found that resolves (18) and (23) for the actual time-dependent PDE–ODE and the fixed delay. Search failure is not evidence of novelty. The sources on coupled heat equations or nonautonomous scalar inverse problems must not be treated as results for the present nondiffusive memory state.

## 8. Decision table and explicit answers

| Proposition | Classification | Scope |
|---|---|---|
| Actual decomposition and adjoint identities | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | Inherited active-base, forced forward and transposition hypotheses; (3)–(6), (12)–(16). |
| Dual density and exact range/unbounded-ratio criteria | PROVED | Functional analysis, (17), (21), (22); applying them requires the actual conditional operator. |
| Full interior \(Y\) determines input | PROVED UNDER EXPLICIT ADDITIONAL ASSUMPTIONS | Inherited base gives (9) near initial time; full interior data, (10); not the prescribed boundary observation. |
| Second actual mode-dependent expansion | NOT ESTABLISHED | Trial (25) is formal; missing traces, regularity and smaller error. |
| Actual \(\mathcal R|_{H_0}\) injectivity | NOT ESTABLISHED | (18) unproved for the active system. |
| \(b_*\notin\operatorname{ran}(\mathcal R|_{H_0})\) | NOT ESTABLISHED | Neither the bounded nor unbounded alternative in (21) resolved. |
| A physical invisible input or failure of either condition | NOT ESTABLISHED | No actual \(v\) constructed; near-cancellation is insufficient. |
| Restricted \(H^2\) profile or endpoint identification | NOT ESTABLISHED | Exact criteria (26)–(27), no verification of their hypotheses. |
| Zero Cauchy traces automatically eliminate an unknown distributed source | FALSE | Inhomogeneous equation; no such implication follows. |
| Full initial-memory identification and foundational novelty | NOT ESTABLISHED | No actual injectivity or physical counterexample; no priority claim. |

**Answers.** (1) Unknown. (2) Unknown, including whether \(b_*\) is in the range or only its closure. (3) No failure proved and no physical kernel element constructed. (4) A further separating mode-dependent asymptotic has not been established; §5 gives a precise obstruction to the obvious correction. (5) Full identification remains unresolved. (6) The strongest rigorous conclusion is the exact actual-adjoint pair (17), (21), with the separate conditional interior-data identity (10); none resolves the assigned one-flux experiment. Dr. Gupta is the final decision-maker.
