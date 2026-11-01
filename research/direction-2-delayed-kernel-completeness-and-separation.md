# Delayed kernel completeness and separation

**Date:** 1 November 2026. **Decision: REFORMULATE.** Under the inherited active-base and forward hypotheses, this report proves an actual-system high-frequency boundary expansion with an \(o(q_n^{-1})\) error, identifies the boundary trace of the Hilbert–Schmidt impulse kernel, and proves a new high-mode near-collinearity estimate. The expansion holds even on \((0,T)\), so it does not require an unproved delayed heat-kernel damping estimate. It does **not** prove impulse-response completeness, full odd injectivity, or an exact physical invisible state. No literature priority or new foundational continuum theory is asserted.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is Arena's calculation, not independent human certification. Direction 1 remains rejected; Direction 2 is the fixed inverse boundary-identification problem.

## 1. Exact active problem and coefficient audit

The preceding report and the active-base regularity, forward existence, delayed-adjoint, compact-quotient and admissible-topology reports were inspected. Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\); the prescribed loading is \(g_*\sin^2(\pi t/T)\), \(g_*\ne0\). Write
\[
D=a+k,\ r=k/D,\ \alpha=a/D,\ \beta=b/D,\ \gamma=\lambda\beta,\ \mu=\lambda\alpha,\ d=b^2/D,\ Qv=v-\bar v.
\]
With the actual even active base,
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{1}
\]
Let \(H=L^2_o(I)\), \(V=H^1_0(I)\cap H\), \(X=H^2(I)\cap H\); odd means reflection about \(L/2\). For \(h\in H\) the strong-temperature solution of
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(0)=0,\ P(0)=h,\quad Y(t,0)=Y(t,L)=0,\quad
\mathcal Th=2A_0\kappa Y_x(\cdot,0)|_J \tag{2}
\]
is the analytic \(L^2\) extension of the physical odd linearization. No endpoint condition is imposed on \(P\) or general physical input \(h\in X\).

The sufficient small-load base condition is not numerically verified. All theorems below are conditional on the earlier base and strong-forward hypotheses, in particular
\[
0<m_0\le M\le m_1,\quad M_x\in L^\infty_tL^2_x,\quad B\in L^2_{t,x},\quad S\in L^\infty_{t,x}, \tag{3}
\]
\[
\mathcal E=H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0),\quad
\|Y\|_{\mathcal E}+\|P\|_{H^1_tL^2_x}\le C_E\|h\|_2. \tag{4}
\]
The same strong estimate holds for \(L^2\) source pairs and initial temperature in \(H^1_0\), initial memory in \(L^2\). The actual base also has
\[
S\in C([0,T];H^1(I))\cap H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)). \tag{5}
\]
Indeed \(y_b\in\mathcal E\cap C_tH^1_0\), \(p_b=\gamma\int_0^te^{-\mu(t-r)}Qy_b(r)dr\), and \(w_b=m-v_b-\alpha p_b+\beta Qy_b\); time differentiation and Bochner integration yield (5), with the scalar \(m,v_b\) smooth. Thus \(S_x\in L^2_tH^1_x\), \(S,S_x\in L^\infty_tL^2_x\), and \(S\in L^\infty_{t,x}\). Further \(A=\kappa/M\) has \(A_x\in L^\infty_tL^2_x\), and \(S/M,1/M\in L^\infty_tH^1_x\). All coefficients are even, so they preserve odd subspaces. No \(B\in L^\infty_tL^2_x\), \(M_t\in L^\infty\), or temporal analyticity is used.

## 2. Audit of the previous ansatz

Let \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \((Y_n,P_n)\) solve (2) with \(h=\phi_n\), and define
\[
P_n^a=e^{-\mu t}\phi_n,\qquad Y_n^a=\frac{e^{-\mu t}}{\kappa q_n^2}S\phi_n. \tag{6}
\]
By (5), \(Y_n^a\in\mathcal E\), with zero spatial traces and \(Y_n^a(0)=S(0)\phi_n/(\kappa q_n^2)\in H^1_0\). It need not satisfy the prescribed zero initial temperature. \(P_n^a\in H^1_tL^2_x\) and \(P_n^a(0)=\phi_n\). Product differentiation gives exactly
\[
R_n=MY^a_{n,t}-\kappa Y^a_{n,xx}-BY_n^a-SP_n^a
=\frac{e^{-\mu t}}{\kappa q_n^2}
\{[M(S_t-\mu S)-BS-\kappa S_{xx}]\phi_n-2\kappa S_x\phi_n'\}. \tag{7}
\]
Here \(S_t,S_{xx}\in L^2_{t,x}\), \(BS\in L^2_{t,x}\), and the sine and cosine factors are bounded; (3)–(5) justify every product. In particular
\[
\|R_n\|_{L^2_{t,x}}\le C(q_n^{-1}+q_n^{-2}),\quad
\|Y_n^a\|_{L^2_{t,x}}\le Cq_n^{-2},\quad
\|Y_n^a(0)\|_{H^1_0}\le C(q_n^{-1}+q_n^{-2}). \tag{8}
\]
For \(e_n=Y_n-Y_n^a\), \(r_n=P_n-P_n^a\),
\[
Me_{n,t}-\kappa e_{n,xx}=Be_n+Sr_n-R_n,\quad
r_{n,t}+\mu r_n=\gamma e_n+\gamma Y_n^a,\quad
(e_n,r_n)(0)=(-Y_n^a(0),0),\ e_n|_{\partial I}=0. \tag{9}
\]
The inherited strong forced estimate gives \(\|e_n\|_{\mathcal E}+\|r_n\|_{H^1_tL^2_x}\le Cq_n^{-1}\), after absorbing finitely many small modes. Therefore the previous \(O(q_n^{-1})\) column bound and Hilbert–Schmidt conclusion are valid. The prior conclusion was deliberately conservative: a same-order error was not called a leading asymptotic. The next section strengthens it using oscillation in a weaker spatial norm, not by silently enhancing the regularity of \(B\).

## 3. A sharper actual-system boundary expansion

### 3.1 Negative-norm cancellation of the distributed residual

For \(V'\) the dual of odd \(H^1_0(I)\), with \(\|v\|_V=\|v_x\|_2\), the following oscillatory estimate holds for any \(a\in H^1(I)\):
\[
\|a\cos(q_nx)\|_{H^{-1}(I)}\le \frac{C_L}{q_n}\|a\|_{H^1(I)}. \tag{10}
\]
Indeed for \(v\in H^1_0\), integration by parts using \(\cos(q_nx)=q_n^{-1}(\sin(q_nx))_x\) and \(v|_{\partial I}=0\) gives
\[
\left|\int a\cos(q_nx)v\,dx\right|\le q_n^{-1}\big(\|a_x\|_2\|v\|_\infty+\|a\|_\infty\|v_x\|_2\big)
\le C_Lq_n^{-1}\|a\|_{H^1}\|v_x\|_2.
\]
This also bounds the \(V'\) norm of the actual odd residual. As \(S_x\in L^2_tH^1_x\), applying (10) to \(a=S_x(t)\) gains one full power of \(q_n\); all other terms of (7) are already \(q_n^{-2}\) in \(L^2\). Hence
\[
\boxed{\|R_n\|_{L^2(0,T;V')}\le Cq_n^{-2}.} \tag{11}
\]
The constants depend on \(\|S_x\|_{L^2H^1}\), \(\|S_t\|_2\), \(\|S_{xx}\|_2\), \(\|BS\|_2\), \(\|M\|_\infty\), \(L,T,\kappa,\mu\), not on \(n\). The \(L^2\) norm of \(R_n\) remains only \(O(q_n^{-1})\); (11) is not a false claim that its strong norm is smaller.

### 3.2 Two-level error estimate

We prove the weak estimate needed for (9). For odd strong solutions of
\[
My_t-\kappa y_{xx}=By+Sp+F,\quad p_t+\mu p=\gamma y+G, \tag{12}
\]
with \(y|_{\partial I}=0\), divide by \(M\), test by \(y\), and test the second equation in \(V'\). Multiplication by an even \(H^1\) function acts on \(V\) and its dual, so \(F/M\in V'\) and \(\|F/M\|_{V'}\le C\|F\|_{V'}\). The same Young inequalities as in the independent audit give
\[
\frac d{dt}(\|y\|_2^2+\|p\|_{V'}^2)+c\|y_x\|_2^2
\le C(t)(\|y\|_2^2+\|p\|_{V'}^2)+C(\|F\|_{V'}^2+\|G\|_{V'}^2), \tag{13}
\]
where \(C\in L^1(0,T)\), depending on \(1+\|A_x\|_2^4+\|B\|_2^{4/3}+\|S/M\|_{H^1}^2\). This uses \(B\in L^2_{t,x}\) only. All pairings are legitimate for the already-constructed strong solutions; no weak-existence theorem for arbitrary \(V'\) data is needed. Gronwall gives
\[
\|y\|_{L^\infty_tL^2_x\cap L^2_tH^1_0}+\|p\|_{L^\infty_tV'}
\le C(\|y(0)\|_2+\|p(0)\|_{V'}+\|F\|_{L^2_tV'}+\|G\|_{L^2_tV'}). \tag{14}
\]
For (9), \(\|Y_n^a(0)\|_2\le Cq_n^{-2}\), \(\|\gamma Y_n^a\|_{L^2_tV'}\le Cq_n^{-2}\), and (11) applies. Combining (14) with the strong bound (8)–(9),
\[
\|e_n\|_{L^2_tH^1_x}\le Cq_n^{-2},\qquad
\|e_n\|_{L^2_tH^2_x}\le Cq_n^{-1}. \tag{15}
\]
The same two estimates hold separately for the coupled solution driven by the initial mismatch and for that driven by the distributed sources, by linear superposition. They give a uniform error after the delay, but do **not** prove exponential-in-\(q_n^2\) decay of the initial-mismatch component: in the nonautonomous coupled system a uniform evolution-family boundary smoothing theorem would be an additional result. The improved estimate does not require such decay.

For \(s=3/2+\eta\), \(0<\eta<1/2\), interpolation and the strict derivative trace theorem yield
\[
\|e_{n,x}(0,\cdot)\|_{L^2(0,T)}\le C_\eta\|e_n\|_{L^2H^1}^{2-s}\|e_n\|_{L^2H^2}^{s-1}
\le C_\eta q_n^{-3/2+\eta}. \tag{16}
\]
The exponent comes from \(2(2-s)+(s-1)=3-s\). The endpoint \(s=3/2\) is deliberately excluded.

### 3.3 Theorem: actual boundary response, with an \(o(q_n^{-1})\) remainder

For every \(0<\eta<1/2\), under (3)–(5) and the inherited forced estimate,
\[
\boxed{\quad k_n(t)=\frac{a(t)}{q_n}+\rho_n(t),\quad
 a(t)=2A_0\sqrt{2/L}\,e^{-\mu t}S(t,0),\quad
\|\rho_n\|_{L^2(0,T)}\le C_\eta q_n^{-3/2+\eta}.\quad} \tag{17}
\]
Proof: (6) has \(Y^a_{n,x}(t,0)=\sqrt{2/L}e^{-\mu t}S(t,0)/(\kappa q_n)\), and (16) controls the true trace error after multiplying by \(2A_0\kappa\). Restriction to \(J\) gives the requested delayed expansion and \(q_n\rho_n\to0\) in \(L^2(J)\). This is a single leading term plus a quantified smaller remainder; no \(q_n^{-2}a_2\) is claimed. It uses the true \(M,B,S\), actual memory feedback, and initial mismatch; the rate constant is for each **fixed** admissible base and specified coefficient bounds, not uniform over all material parameters without uniform bounds. No frozen-coefficient model is used.

If \(\|a\|_{L^2(J)}>0\), then \(q_n\|k_n\|_{L^2(J)}\to\|a\|_{L^2(J)}\), and all sufficiently high columns are nonzero. This sign/nonvanishing premise is **not** verified for the fixed experiment. If \(a=0\) a.e. on \(J\), (17) only yields \(O(q_n^{-3/2+\eta})\); it does not identify the next nonzero term or imply zero output. The inherited sign test gives positivity near initial time but does not itself establish overlap with \(J\).

### 3.4 What the new leading term cannot prove

All normalized columns satisfy \(q_n k_n\to a\) in \(L^2(J)\): their leading time profiles are **the same**. For \(N\ge2\), choose \(v_N=\phi_{N-1}-(q_N/q_{N-1})\phi_N\). Its leading \(a/q\) terms cancel, while \(\|v_N\|_2\) is bounded below and above. Therefore the actual finite-section smallest singular value satisfies
\[
\sigma_N\le C_\eta q_{N-1}^{-3/2+\eta}. \tag{18}
\]
This is an **upper** bound on conditioning, not a lower bound, and neither proves nor disproves any finite or infinite kernel. It explains why nonzero columns and the first asymptotic profile cannot establish completeness; finer, genuinely mode-dependent information is necessary. Cancellation of two leading terms is not an exact invisible input.

## 4. Regularity and boundary values of the actual kernel

The preceding report established Hilbert–Schmidt \(\mathcal T:H\to L^2(J)\), so
\[
K(t,x)=\sum_{n\ge1}k_n(t)\phi_n(x)\quad\text{in }L^2(J\times I),\qquad
\mathcal Th(t)=\langle K(t),h\rangle_H\text{ a.e.} \tag{19}
\]
Let \(\ell(x)=1-2x/L\). Since \(\ell_n=2\sqrt{2/L}/q_n\), (17) yields the exact \(L^2(J\times I)\) decomposition
\[
\boxed{\quad K(t,x)=A_0e^{-\mu t}S(t,0)\ell(x)+R(t,x),\qquad
R=\sum_{n\ge1}\rho_n(t)\phi_n(x).\quad} \tag{20}
\]
For every \(0\le s<1\), choose \(0<\eta<\min(1/2,1-s)\). Then
\[
\sum_{n\ge1}q_n^{2s}\|\rho_n\|_{L^2(J)}^2\le C_\eta\sum_n q_n^{2s-3+2\eta}<\infty. \tag{21}
\]
The spectral characterization of the Dirichlet Laplacian therefore gives
\[
R\in L^2(J;H^s(I)\cap H),\quad 0\le s<1;\qquad
R(t,0)=R(t,L)=0\text{ a.e. }t\text{ if }1/2<s<1. \tag{22}
\]
For \(1/2<s<1\) the spectral space is the zero-trace \(H^s_0\); no endpoint claim at \(s=1/2\) is made. Since \(\ell\) is smooth,
\[
K\in L^2(J;H^s(I)\cap H)\quad(s<1),\qquad
K(t,0)=A_0e^{-\mu t}S(t,0),\quad K(t,L)=-K(t,0)\quad\text{a.e.} \tag{23}
\]
These are traces of the **input-space kernel**, not a boundary condition on the physical memory \(P\). There is no contradiction with sine coefficients of order \(1/n\): a smooth nonzero-endpoint function need not belong to the Dirichlet spectral domain of order \(s>1/2\). Moreover \(\mathcal T^*:L^2(J)\to H^s(I)\cap H\) is bounded for each \(s<1\), with endpoint trace
\[
(\mathcal T^*f)(0)=A_0\int_J e^{-\mu t}S(t,0)f(t)dt. \tag{24}
\]
This is an exact bounded functional for adjoint outputs; it does **not** recover the endpoint of an arbitrary input by a bounded pairing, which the prior report proved impossible.

The construction supplies \(K\in L^2_tH^s_x\), not a continuous \(H\)-valued or \(H^{-r}\)-valued time representative; nor does it prove Hölder or analytic time dependence. \(K(t)\) is defined at almost every vector-valued Lebesgue point. Its sign in the interior is not determined by (20): \(R\) may change sign, and no strict positivity theorem is invoked. The trace is known but may itself change sign.

For an exact distributional equation, let \(\mathcal L\) denote the coupled forward residual map in the prior report. For each \(f\in L^2(J)\), the unique transposition pair \((z_f,w_f)\in L^2_{t,x}^2\) satisfies
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\quad
-w_{f,t}+\mu w_f-Sz_f=0,\quad w_f(T)=0,\quad
\int_J f(t)K(t,\cdot)dt=\Pi_ow_f(0). \tag{25}
\]
The first two identities hold in distributions, the terminal \(w\) trace in \(L^2\), and boundary forcing through the full forward-residual identity. Equation (25) defines the boundary impulse response weakly in the observation-time variable without asserting classical delta-controlled traces or an independent initial value at \(t=0\). The high-frequency proof gives \(L^2(0,T;H^s)\) for the corresponding all-time kernel as well; no pointwise initial-time limit or singularity is established.

## 5. Completeness: five routes and the precise gap

The actual family obeys
\[
\overline{\operatorname{ran}\mathcal T^*}=\overline{\operatorname{span}}\{K(t):t\in J\text{ outside a fixed null set}\},\quad
\ker\mathcal T=\{h\in H:\langle K(t),h\rangle=0\text{ a.e. }t\in J\}. \tag{26}
\]
The following checks do not equate nonzero columns with this infinite-dimensional completeness.

**A. Time evolution.** The forward coupled system defines a bounded evolution on the appropriate strong-temperature restart space. But \(K(t)\) is an adjoint response propagated from an observation impulse at time \(t\) back to time zero. Changing \(t\) also changes the impulse terminal data and the nonautonomous evolution; no common autonomous semigroup orbit or time-translation identity follows. A theorem showing completeness of this *two-parameter boundary impulse family* on the actual initial-memory subspace is missing.

**B. Adjoint boundary controls.** Equation (25) and vector-valued Lebesgue differentiation give \(K(t)\) as the strong \(H\) limit of normalized interval-control responses at a.e. \(t\). Those controls have unbounded norms. The missing separation lemma is: for every nonzero odd \(h\), there exists \(f\in L^2(J)\) with \(\int_0^T e^{-\mu r}\langle h,S(r)z_f(r)\rangle dr\ne0\). Non-strict cone pairing and the trace (24) do not prove it.

**C. Moment route.** If \(h=\sum h_n\phi_n\) is orthogonal to all \(K(t)\), then \(\sum h_nk_n=0\) in \(L^2(J)\), with a rigorously convergent synthesis. Equation (17) gives only \(a(t)\sum h_n/q_n+\sum h_n\rho_n(t)=0\), with both sums convergent in \(L^2\). The first term is rank one; the remainder is an unknown compact synthesis. Neither side must vanish separately. Proving the remainder separates the codimension-one subspace \(\sum h_n/q_n=0\), allowing cancellation with \(a\), is a concrete unresolved lemma. Formula (18) shows that leading temporal collinearity makes a diagonal-dominance argument especially delicate.

**D. Continuation.** The actual base supplies Sobolev/time-Hölder coefficient regularity, not analyticity. Zero endpoint trace of an inhomogeneous heat equation does not imply zero \(Y\) or \(P\), and scalar homogeneous backward uniqueness is not applicable. A coupled boundary-to-interior continuation result on the reachable graph, or another route bypassing it, remains unproved. No propagation of zero observation from \(J\) back to \(0\) is inferred.

**E. Spectral/biorthogonal route.** The actual time-dependent multiplication matrices couple the odd sines and the ODE contributes a nondiffusive component. No common autonomous generator, root-vector completeness or scalar exponential family is established. \(k_n\to0\) precludes a Riesz sequence; (17) makes scaled columns converge to the same vector. This does not rule out an unbounded biorthogonal family or a different valid method. No theorem here proves or disproves completeness.

## 6. Restricted classes, modulus, and additional measurements

For \(h\in X\), write \(h=h(0)\ell+g\), \(g\in X_0=H^2\cap H^1_0\cap H\). The exact \(L^2\) tail is
\[
\|(I-P_N)h\|_2\le |h(0)|\frac{\sqrt{2L}}{\pi\sqrt N}+q_{N+1}^{-2}\|h''\|_2. \tag{27}
\]
The new \(a(t)/q_n\) structure describes a **shared high-frequency** response, but it does not produce a bounded functional that isolates \(h(0)\) from \(X_0\): \(X_0\) is dense in \(H\) and \(\mathcal T\) is bounded. The lift and interior outputs can still conceivably be separated by a nonlinear or unbounded procedure on bounded \(H^2\) sets; no such proof is available. In particular \(\mathcal T\ell\ne0\) is not established solely by (17).

Let \(K_0=\ker\mathcal T\subset H\) and \(\mathcal B_R=\{h\in X:\|h\|_{H^2}\le R\}\). Compact embedding \(H^2\Subset L^2\), closedness of \(K_0\), and continuity of \(\mathcal T\) prove
\[
\omega_R(\varepsilon):=\sup\{\operatorname{dist}_H(h,K_0):h\in\mathcal B_R,\ \|\mathcal Th\|\le\varepsilon\}\to0. \tag{28}
\]
Proof: a contrary sequence has an \(L^2\)-convergent subsequence; its limit lies in \(K_0\), forcing the distances to zero. This is a qualitative **modulo-kernel** modulus, not a rate or physical identification if \(K_0\cap X\) is nontrivial. If a separate theorem establishes \(K_0\cap X=\{0\}\), compactness of \(\mathcal B_R\) in \(L^2\) gives a full-norm modulus on this class; the premise remains unproved. A finite-dimensional physical chart would have a local inverse only after proving differentiability and injectivity of the actual derivative restricted to its tangent space; no actual finite Gram positivity is established.

One sufficient **additional distributed measurement** is the full \(P(\delta,\cdot)\) and the interior temperature history \(Y|_{(0,\delta)\times I}\). Then the exact ODE gives
\[
h=e^{\mu\delta}\left[P(\delta)-\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr\right] \quad\text{in }H. \tag{29}
\]
This is a mathematically sufficient augmented experiment, not a claim of minimality, feasibility, or that one boundary flux is insufficient. Another sufficient augmentation is \(D_\delta h=P(\delta)\) plus the finitely many exact scalar coordinates of \(h\) along a basis of \(E=\ker D_\delta\): \(D_\delta h\) determines the \(E^\perp\) component, those coordinates determine \(E\). If a separately verified criterion proves \(E=0\), the full memory snapshot alone suffices. These proposed measurements change the data and are not used to claim a result for the frozen experiment.

## 7. Delayed restart and second boundary

The exact restart at \(\delta\) is
\[
\begin{cases}
MY_t-\kappa Y_{xx}=BY+SP,\\
P(t)=e^{-\mu(t-\delta)}P(\delta)+\gamma\int_\delta^te^{-\mu(t-r)}Y(r)dr,\\
Y(\delta)=Uh,\quad P(\delta)=D_\delta h,\quad Y|_{\partial I}=0.
\end{cases} \tag{30}
\]
The state \((Uh,D_\delta h)\) is constrained by pre-delay evolution; neither coordinate is known merely from the observed trace. \(D_\delta=e^{-\mu\delta}I+K_\delta\) is index-zero Fredholm with compact \(K_\delta\), and its exact finite Schur test in the independent audit remains valid, but invertibility and reconstruction of the boundary-observation graph are separate questions. The joint delayed-state kernel is finite-dimensional because it lies in \(\ker D_\delta\); the subsequent observation kernel on the reachable graph may be infinite-dimensional. No uniqueness of either delayed coordinate from one flux is proved.

Reflection oddness gives \(Y_x(t,L)=Y_x(t,0)\) in the established \(L^2\) trace sense. Therefore a second endpoint derivative supplies exactly the same time signal, and labeled outward heat fluxes differ only by their known normal signs; no independent odd-channel information or kernel reduction is gained. This statement is for the odd channel, not for arbitrary even-plus-odd perturbations.

## 8. Targeted primary-source audit

Search and theorem/proof inspection were targeted rather than exhaustive. No priority claim is made from missing search results.

* Sergei A. Avdonin, S. A. Ivanov, Jun Min Wang, *Inverse Problems for the Heat Equation with Memory*, [arXiv:1612.02129v2](https://arxiv.org/html/1612.02129), 2017. Theorem 4 and §§2–3 use a Gurtin–Pipkin convolution on the Laplacian, zero initial state, and a full Dirichlet-to-Neumann response operator to recover a time kernel; their transform argument and finite-speed hypotheses differ from (2)'s variable lower-order PDE–ODE coupling and unknown initial memory. The displayed theorem/proof passages were inspected; they do not yield (26).
* Andrei Halanay and Luciano Pandolfi, *Approximate controllability and lack of controllability to zero of the heat equation with memory*, [arXiv:1404.2745v1](https://arxiv.org/html/1404.2745), 2014. Theorem 2 and §3 transform a scalar Coleman–Gurtin equation with \(C^1\) convolution multiplying the Laplacian; boundary-control admissibility is explicitly treated. The proof is not a density theorem for (25)'s projected initial memory.
* Guillaume Olive, *Boundary approximate controllability of some linear parabolic systems*, [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), 2026. Theorem 1.1 and appendix use an autonomous generator, compact resolvent and complete adjoint root vectors; the proof uses spectral projections and resolvents. The actual time-dependent PDE–ODE does not have those assumptions established; the theorem does not transfer.
* Michel Duprez, *Controllability of a 2×2 parabolic system by one force with space-dependent coupling term of order one*, [arXiv:1701.05315v1](https://arxiv.org/html/1701.05315v1), 2017, §§1 and 5: two autonomous diffusive equations and space-dependent coupling support a moment/Fattorini analysis. The actual memory equation has no diffusion and coefficients are nonautonomous. Selected proof/statement portions, not all cited dependencies, were inspected.
* Jone Apraiz, Rodrigo Lecaros, Sebastián Zamorano, *A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations*, [arXiv:2610.26157v1](https://arxiv.org/html/2610.26157), 2026, Lemma 2.2 and proof: centered weights yield a Volterra estimate **with** a center-time snapshot; their Kelvin–Voigt inverse problem supplies different data. This does not control our unknown memory snapshot from one boundary.

The negative-norm oscillation proof in §3 is independently written from the inherited coefficient bounds. No matching primary theorem was located and fully verified; this is not evidence of novelty. Abstract-only or inaccessible sources were not treated as applicable.

## 9. Decision table

| Target | Result | Exact theorem or missing lemma | Consequence |
|---|---|---|---|
| Previous high-frequency ansatz | **VERIFIED under inherited hypotheses** | (6)–(9), including \(S_t,S_{xx},BS\) and nonzero initial mismatch | Previous Hilbert–Schmidt conclusion stands. |
| Delayed \(o(q_n^{-1})\) remainder | **PROVED under inherited hypotheses** | (10)–(17), in fact on all of \((0,T)\) | Actual leading time profile; nonzero only if \(a\not\equiv0\) on \(J\). |
| Kernel spatial regularity | **PROVED** | (20)–(24): \(K\in L^2(J;H^s)\), \(s<1\), exact endpoint trace | More structure, not completeness. |
| Kernel time regularity | **L² ONLY ESTABLISHED** | No continuous/Hölder/analytic \(H^{-r}\)-valued representative proved | Cannot use analytic continuation. |
| Impulse-response completeness | **NOT ESTABLISHED** | Need (26) separation, including cancellation between rank-one and remainder | High columns asymptotically collinear. |
| Restricted \(H^2\) identification | **NOT ESTABLISHED** | (28) is modulo unknown kernel; injectivity on \(X\) missing | No full identification modulus asserted. |
| Delayed state reconstruction | **NOT ESTABLISHED** | Fredholm memory map and graph observation are distinct | Neither coordinate follows from flux alone by current proof. |
| Second-endpoint measurement | **REDUNDANT IN ODD CHANNEL** | \(Y_x(L)=Y_x(0)\), with outward signs | No extra independent odd information. |
| Exact physical kernel | **NO NONZERO ELEMENT CONSTRUCTED** | Must satisfy (2) with zero trace throughout \(J\) | Approximate cancellation is not a counterexample. |
| Full odd-channel injectivity | **NOT ESTABLISHED** | Actual impulse-family completeness or another separation proof | Central question remains open. |

**Final classification: REFORMULATE.** The new asymptotic removes the prior same-order remainder obstacle but exposes a rank-one leading profile, not separation. The next mathematical target is the actual remainder family in (20): prove or refute infinite synthesis separation on the relevant codimension-one subspace, while controlling its possible cancellation with \(a\). Dr. Gupta remains the final decision-maker.
