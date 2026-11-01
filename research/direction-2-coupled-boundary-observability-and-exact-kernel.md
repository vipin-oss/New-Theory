# Coupled boundary observability and the exact odd kernel

**Date:** 1 November 2026. **Decision: REFORMULATE.** The exact nonautonomous Volterra input–output identity, a weak initial-time asymptotic for the actual coupled state, and a compact-class stability modulus *modulo the exact kernel* are established below. The kernel itself, delayed moment completeness, and adjoint approximate controllability remain unresolved. Neither a physical invisible state nor full odd injectivity is claimed. A formal constant-coefficient boundary-layer calculation is clearly separated from the actual system.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is a single-agent recalculation, not independent human certification. Direction 2 remains an observation/state question, not a new continuum theory; no mathematical novelty or nonlinear inverse theorem is asserted.

## 1. Frozen system and independent audit

The predecessor `direction-2-rigorous-boundary-positivity-and-adjoint-cone-investigation.md` and the earlier delayed-state/adjoint, boundary-flux, reachable-state and compact-quotient reports were inspected. We retain \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), the actual nonzero sinusoidal actuation \(g_*\sin^2(\pi t/T)\), \(q=|g_*|/L>0\), the base initialized as previously specified, and all prescribed material signs and nonzero couplings. Define
\[
D=a+k,\quad r=k/D,\quad \alpha=a/D,\quad \beta=b/D,\quad \gamma=\lambda\beta,\quad \mu=\lambda\alpha,\quad d=b^2/D,\quad Qv=v-\bar v.
\]
On the reflection-odd space \(H=L^2_o(I)\), the exact extended linearized system is
\[
M Y_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(0,\cdot)=0,\ P(0,\cdot)=h,\quad Y(t,0)=Y(t,L)=0, \tag{1}
\]
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b,\quad
\mathcal T h=2A_0\kappa Y_x(\cdot,0)|_J. \tag{2}
\]
Here time is the first argument, \(b\ne0\), and \(h\in H^2(I)\cap H\) is the physical input class; extension to \(H\) is a linear analytic device, not a nonlinear admissibility claim. Assume the existing sufficient existence hypothesis \(0<q<s_*\), not numerically verified. The inherited solution class is
\[
Y\in H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\cap C_tH^1_0,\quad P\in H^1_tL^2_x;\quad
0<m_0\le M\le m_1,\ M,S\in L^\infty,\ M_x\in L^\infty_tL^2_x,\ B\in L^2_{t,x}. \tag{3}
\]
On each positive-time strip \(B\in L^\infty_tL^2_x\cap L^2_tL^\infty_x\cap L^6_{t,x}\) and \(M,\kappa/M\) have the earlier spatial-Lipschitz and temporal-Hölder bounds; no joint \(L^\infty\) bound on \(B\) is asserted. \(S\) is continuous up to the cylinder boundary. Each trace \(Y_x(\cdot,0)\) is genuine in \(L^2_t\).

### Audit: zero set, comparison, scaling, and cone

On \(I_-=(0,L/2)\), take \(Z=\operatorname{sgn}\gamma P\), \(C_+=\operatorname{sgn}\gamma S\). If \(C_+\ge c_0>0\) on \((0,t_1)\times I_-\), the negative-part argument gives \(Y,Z\ge0\) for \(Z(0)\ge0\). The global estimate genuinely uses
\[
\int |B|v^2\le\|B\|_2\|v\|_\infty\|v\|_2
\le\varepsilon\|v_x\|_2^2+C_\varepsilon\|B\|_2^{4/3}\|v\|_2^2,
\]
using \(\|v\|_\infty^2\le2\|v\|_2\|v_x\|_2\). Together with the \(M_x\) cross term, the Gronwall coefficient is \(1+\|M_x\|_2^4+\|B\|_2^{4/3}\in L^1(0,T)\). The divided equation and \(-Y_-/M\) test avoid requiring \(M_t\); \(-Z_-\) tests the ODE. Thus the correction in the latest report is valid and no global \(L^\infty_tL^2_x\) assumption on \(B\) is needed.

If \(Z(0)\ge0\), \(Z(0)\ne0\), then \(Z(t)\ge e^{-\mu t}Z(0)\) a.e. If \(E=\{t:Y(t)=0\text{ in }L^2(I_-)\}\) has positive measure, \(Y_t(t)=0\) for a.e. \(t\in E\): choose a countable dense subset \(\{e_j\}\) of \(L^2\), apply the scalar fact that an absolutely continuous real function has zero derivative a.e. on each level set to \(\langle Y,e_j\rangle\), and intersect the countable full-measure sets. For a.e. \(t\in E\), (3) also gives \(Y(t)\in H^2\), hence \(Y_{xx}(t)=0\); \(BY(t)=0\), and (1) implies \(C_+Z(t)=0\), contradicting the uniform lower bound and nonzero \(Z(0)\). Here \(BY\in L^2_{t,x}\) since \(Y\in L^\infty_{t,x}\), and \(SZ\in L^2\). Thus nonzero temperature for a.e. time is correctly proved; no claim of strictly positive boundary flux or delayed overlap follows.

For \(\xi=x/L,\ \sigma=t/T,\ u=y_b/\theta_*\), the exact transformations are
\[
\|u_\sigma\|_{L^2((0,1)^2)}=\frac{\sqrt{T/L}}{\theta_*}\|y_{b,t}\|_{L^2_{t,x}},\qquad
\sup_\sigma\|u_\xi\|_2=\frac{\sqrt L}{\theta_*}\sup_t\|y_{b,x}\|_2.
\]
For \(\rho=\lambda T\), \(m(T\sigma)=(g_*/L)\sin^2(\pi\sigma)\), \(v_b=\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds\), direct integration yields
\[
\frac{m(T\sigma)-v_b(T\sigma)}{g_*/L}=
\pi\int_0^\sigma e^{-\rho(\sigma-v)}\sin(2\pi v)dv
=\frac{\pi[\rho\sin(2\pi\sigma)-2\pi\cos(2\pi\sigma)+2\pi e^{-\rho\sigma}]}{\rho^2+4\pi^2}.
\]
The fixed-unit existence bound must be rescaled componentwise; no fabricated parameter values are used. The previously established adjoint cone follows independently from \(\langle\mathcal T h,f\rangle\ge0\), for every half-interval cone input and \(f\ge0\) supported where \(C_+\ge0\): odd extension of all nonnegative \(L^2(I_-)\) tests proves \(\operatorname{sgn}\gamma\,\Pi_o w_f(0)\ge0\) on \(I_-\). This is non-strict and conditional on the actual sign interval. Finally \((\operatorname{ran}\mathcal T^*)^\perp=\ker\mathcal T\) is an exact Hilbert-space identity, not a proof that either side is zero.

## 2. Rigorous Volterra input–output operator

The Bochner ODE formula is
\[
P(t)=e^{-\mu t}h+\gamma\int_0^t e^{-\mu(t-s)}Y(s)ds. \tag{4}
\]
Substitution into (1) gives
\[
M Y_t-\kappa Y_{xx}-BY-\gamma S(t)\int_0^t e^{-\mu(t-s)}Y(s)ds=S(t)e^{-\mu t}h. \tag{5}
\]
The multiplier \(S(t,x)\) acts at the current time, and neither initial history nor delayed state has been discarded.

Let \(\mathscr E_0=\{y\in H^1_tL^2\cap L^2_t(H^2\cap H^1_0):y(0)=0,\ y\text{ odd}\}\). Let \(\mathscr H\) be the bounded zero-initial scalar source solution operator of \(My_t-\kappa y_{xx}-By=F\); the preceding Galerkin/energy result supplies \(\mathscr H:L^2_{t,x}\to\mathscr E_0\). Define the bounded causal maps
\[
(\mathscr D h)(t)=S(t)e^{-\mu t}h,\quad
(\mathscr V y)=\mathscr H\!\left[\gamma S(t)\int_0^t e^{-\mu(t-s)}y(s)ds\right],\quad
\mathscr B y=2A_0\kappa y_x(\cdot,0)|_J.
\]
Uniqueness and the established coupled forced-solution estimate imply that \(I-\mathscr V\) is a bounded bijection on \(\mathscr E_0\): for any \(g\in\mathscr E_0\), solve the coupled problem with heat source \(Mg_t-\kappa g_{xx}-Bg\) and zero initial pair. All source products belong to \(L^2\). Thus
\[
\boxed{\quad \mathcal T=\mathscr B(I-\mathscr V)^{-1}\mathscr H\mathscr D.\quad} \tag{6}
\]
This is an exact **operator-valued causal Volterra representation**, not a claimed pointwise Green function. It includes nonautonomous coefficients and is valid for all \(h\in H\). One may formally write \(Y(t)=\int_0^t U(t,s)[S(s)e^{-\mu s}h+\gamma S(s)\int_0^s e^{-\mu(s-r)}Y(r)dr]ds\), and then formally differentiate at the endpoint, but the evolution family \(U\), boundary kernel, its diagonal and interchange of boundary trace/integral require construction with appropriate singular estimates. They are not supplied by (6). In particular a time-diagonal of a spatial input-to-output kernel cannot simply be inverted as a scalar Volterra diagonal.

The delayed factorization \(\mathcal T=\mathcal R_\delta\mathcal S_\delta\), \(\mathcal S_\delta h=(Y(\delta),P(\delta))\), is exact by forward uniqueness. The pair is on the reachable graph, not arbitrary independent data. From (4), \(D_\delta h=P(\delta)=e^{-\mu\delta}h+K_\delta h\), with \(K_\delta:H\to H^2\cap H^1_0\) bounded and compact into \(H\). Fredholmness and finite pre-delay kernel follow, but neither zero observation nor the delay implies \(P(\delta)=0\). A finite-dimensional \(\ker D_\delta\) does not imply a finite-dimensional observation kernel.

## 3. Actual small-time state response and boundary-layer diagnostic

At \(t=0\), the frozen symmetric base has \(y_b=w_b=0\); write
\[
M_*=c+d\theta_*,\quad S_*=\lambda\alpha br\theta_*,\quad
A_*=\kappa/M_*,\quad c_*=S_*/M_*\ne0. \tag{7}
\]
Here \(c_*\) is a coefficient, not the heat capacity \(c\); \(b\) can have either sign. Under (3), the source-problem energy estimate applied on \((0,t)\) with \(F=S e^{-\mu s}h\) and zero initial pair gives, with a constant uniform for \(0<t\le T\),
\[
\sup_{0\le s\le t}\|Y_x(s)\|_2+\|Y_t\|_{L^2(0,t;L^2)}\le C\sqrt t\|h\|_2,\quad
\|Y(s)\|_2\le Cs\|h\|_2,\quad \|Y(s)\|_\infty\le Cs^{3/4}\|h\|_2. \tag{8}
\]
The Gronwall constant uses \(\int_0^T\|B(s)\|_2^2ds<\infty\); (8) follows from the explicit energy inequality in the delayed-state predecessor, not a postulated smoothing theorem. The ODE then implies in \(L^2\)
\[
P(t)=h-\mu t h+O(t^2\|h\|_2). \tag{9}
\]
More substantially, the actual temperature has the weak spatial first-order asymptotic
\[
\boxed{\ Y(t)/t\longrightarrow c_*h\quad\text{in }H^{-1}(I)\quad(t\downarrow0).\ } \tag{10}
\]
To verify it, divide (1) by \(M\), put \(A=\kappa/M\), and integrate against \(\psi\in H^1_0(I)\). The diffusion contribution satisfies
\[
|\langle A Y_{xx},\psi\rangle|=| -\!\int Y_x(A\psi)_x|\le C\|Y_x\|_2\|\psi\|_{H^1_0},
\]
using \(A\in L^\infty\), \(A_x\in L^\infty_tL^2_x\), and the one-dimensional embedding for \(\psi\). Its time integral divided by \(t\) tends to zero by (8). The potential contribution has average bounded by
\(Ct^{-1}\|B\|_{L^2((0,t)\times I)}(\int_0^t s^{3/2}ds)^{1/2}\|h\|_2\), which tends to zero. Finally \((S/M)(t)\to c_*\) uniformly in space by continuity of the active base, and \(P(t)\to h\) in \(L^2\); thus the averaged source converges to \(c_*h\). This proves (10) without boundary compatibility for \(h\). It is not an \(H^2\) or boundary-derivative asymptotic.

For an **illustration only**, freeze coefficients at their initial values and consider the auxiliary half-line heat problem \(y_t-A_*y_{xx}=c_*h(x)\), \(y(0,t)=0\), \(y(x,0)=0\). Its explicit Dirichlet heat kernel yields
\[
y_x(0,t)=c_*\int_0^t\!\int_0^\infty
\frac{x}{A_*\tau\sqrt{4\pi A_*\tau}}e^{-x^2/(4A_*\tau)}h(x)\,dx\,d\tau
=\frac{2c_*h(0)}{\sqrt{\pi A_*}}\sqrt t+c_*h'(0)t+o(t) \tag{11}
\]
for a sufficiently regular bounded extension of \(h\), with the \(o(t)\) justified by Taylor expansion/dominated convergence. This is **not** the actual Green function or an experimentally valid asymptotic. It shows why the first boundary layer can see \(h(0)\), the next can see \(h'(0)\), and before expansion the response is a nonlocal Gaussian-weighted integral. It cannot be transferred to (1) without coefficient/source remainder estimates at the derivative trace, especially near the initial corner. Smooth odd \(H^2\) functions need not vanish at the endpoints: oddness imposes \(h(L)=-h(0)\), not \(h(0)=0\). No actual \(o(\sqrt t)\) boundary error or trace asymptotic is proved here.

Even a fully proved initial-time boundary expansion identifies at most endpoint jets at that order; it would not automatically recover an arbitrary profile. More importantly, \(J\) starts at \(\delta>0\), and the nonautonomous active coefficients are not shown time analytic. Initial asymptotics cannot be analytically continued from \(J\) by assumption. No reduction to a zero-actuation equilibrium is made.

## 4. Coupled moments, truncations and a precise missing completeness test

Let \(\phi_n=\sqrt{2/L}\sin(2n\pi x/L)\), \(\rho_n=(2n\pi/L)^2\), \(u_n=\langle Y,\phi_n\rangle\), \(p_n=\langle P,\phi_n\rangle\), \(h_n=\langle h,\phi_n\rangle\). Projection of (1) gives in the appropriate \(L^2_t\) sense
\[
\sum_{m\ge1}M_{nm}(t)u'_m+\kappa\rho_nu_n
=\sum_{m\ge1}B_{nm}(t)u_m+\sum_{m\ge1}S_{nm}(t)p_m,
\quad p'_n+\mu p_n=\gamma u_n,\quad u_n(0)=0,\ p_n(0)=h_n, \tag{12}
\]
where \(M_{nm}=\langle M\phi_m,\phi_n\rangle\), \(S_{nm}=\langle S\phi_m,\phi_n\rangle\), and \(B_{nm}=\langle B\phi_m,\phi_n\rangle\) for a.e. time. These sums mean the corresponding \(L^2\) product/projection limits; \(B\) is not assumed an \(L^\infty\) multiplier on \(L^2\). For a fixed \(N\), the legitimate Galerkin diagnostic is
\[
M_N(t)u_N'(t)+\kappa\operatorname{diag}(\rho_1,\ldots,\rho_N)u_N=B_N(t)u_N+S_N(t)p_N,\qquad p_N'+\mu p_N=\gamma u_N,
\quad p_N(0)=(h_1,\ldots,h_N).
\]
The mass matrix is uniformly positive; the variable matrices couple different modes, and no diagonalization is assumed. These finite systems need convergence under the established Galerkin bounds; their ranks are not infinite-system proofs.

Let \(P_N\) be odd sine projection. Since \(P_NY\to Y\) in \(L^2(J;H^s(I))\) for \(3/2<s<2\), by interpolation of strong convergence in \(L^2H^2\),
\[
Y_x(\cdot,0)=\lim_{N\to\infty}\sum_{n=1}^N\sqrt{2/L}\,(2n\pi/L)u_n(\cdot)\quad\text{in }L^2(J). \tag{13}
\]
The output weights grow linearly in \(n\), but this alone gives no temporal separation. Smooth odd \(H^2\) inputs may have nonzero endpoint trace; their Dirichlet sine coefficients can decay only as \(1/n\), so a sine truncation need not converge in the full \(H^2\) topology.

A useful exact reformulation uses \(k_n=\mathcal T\phi_n\in L^2(J)\): boundedness implies
\[
\mathcal T h=\lim_{N\to\infty}\sum_{n\le N}h_n k_n\quad\text{in }L^2(J). \tag{14}
\]
Consequently the missing statement is the **\(\ell^2\)-synthesis injectivity property** that the only \(\ell^2\) sequence for which (14) vanishes is zero. Equivalently, the infinite positive form
\(\lim_N\|\sum_{n\le N}h_n k_n\|_{L^2(J)}^2\) is strictly positive for every nonzero \(h\in H\). For every fixed \(N\), positive definiteness of \((\langle k_m,k_n\rangle)_{m,n\le N}\) is equivalent to injectivity on that finite span; even positive definiteness for every finite \(N\) does **not** imply the infinite \(\ell^2\) property. No actual Gram entries, ranks or lower bounds have been computed.

Müntz/exponential-family and nonharmonic Fourier theorems require a proved family of scalar exponentials and a completeness/biorthogonality hypothesis. Here time-dependent matrices mix modes, while the distributed ODE contributes a nonsmoothing component; (12) provides neither such a family nor the uniform biorthogonal estimates. A zero \(L^2\)-limit of a sum does not make its individual terms zero. This is an exact target for a moment method rather than a claimed solution.

## 5. Adjoint, controllability, and exact invisible-state search

For arbitrary zero-initial forward sources \((F,G)\in L^2_{t,x}^2\), solve
\(My_t-\kappa y_{xx}-By-Sp=F\), \(p_t+\mu p-\gamma y=G\), with homogeneous temperature boundary data. The strong-source estimate and endpoint trace make
\(\Lambda_f(F,G)=2A_0\kappa\int_J f(t)y_x(t,0)dt\) bounded for each \(f\in L^2(J)\). Riesz gives unique \((z_f,w_f)\in L^2_{t,x}^2\), satisfying for every such forward pair
\[
\iint[(My_t-\kappa y_{xx}-By-Sp)z_f+(p_t+\mu p-\gamma y)w_f]
=2A_0\kappa\int_J f y_x(0)dt. \tag{15}
\]
Using compactly supported tests gives
\[
-\partial_t(Mz_f)-\kappa z_{f,xx}-Bz_f-\gamma w_f=0,\quad
-w_{f,t}+\mu w_f-Sz_f=0 \quad\text{in distributions}. \tag{16}
\]
\(w_f\in H^1_tL^2_x\), \(w_f(T)=0\), \(w_f(0)=\int_0^T e^{-\mu s}S(s)z_f(s)ds\). The formal boundary values \(z_f(t,0)=2A_0\mathbf1_Jf(t)\), \(z_f(t,L)=0\), and \(Mz_f(T)=0\) are encoded by (15), not asserted as classical traces. Set \(p=P-e^{-\mu t}h\) in (15); then \((y,p)\) has zero initial pair and source \(F=Se^{-\mu t}h,G=0\), giving
\[
\mathcal T^*f=\Pi_o w_f(0),\qquad
(\operatorname{ran}\mathcal T^*)^\perp=\ker\mathcal T. \tag{17}
\]
Since \(\mathcal T:H\to L^2(J)\) is bounded, the Hilbert adjoint domain is all of \(L^2(J)\). The boundary-controlled transposition system is a mathematically valid dual experiment; its reachable **memory projection** at initial time is dense iff the actual forward kernel is zero. It is not the same assertion as full two-component approximate controllability.

Delay restricts controls to \(J\), but their backward solution still traverses \((0,\delta)\); no automatic propagation of observability through that strip is established. One-end control is sufficient to encode the measured odd flux through the reflection projection; it does not make the pair independent. The active coefficients vary in both space and time; the memory component is not diffusive. A purported dual proof would have to show that every \(h\in H\) with the solution of (1) satisfying \(Y_x(0,t)=0\) a.e. on \(J\) is zero. Oddness also yields \(Y_x(L,t)=0\), but the scalar heat equation is inhomogeneous with unknown \(SP\), so standard homogeneous boundary unique continuation is not directly applicable. Adjoint density and approximate controllability remain open.

We searched exact candidates without modifying (2). Odd symmetry does **not** make \(Y_x(0,t)\) vanish: both endpoint derivatives agree, and their measured difference doubles the signal. Imposing \(h(0)=0\) or extra endpoint compatibility does not make the distributed forcing vanish or prove zero flux. Even and odd channels cannot cancel in the odd-difference observation because parity separates them. A possible member of \(\ker D_\delta\) may still have nonzero delayed temperature/output, and Fredholmness neither constructs it nor makes the full observation kernel finite-dimensional. The only rigorous adjoint-orthogonality condition is (17), which is equivalent to the original unknown kernel, not an explicit element. No nonzero physical invisible state has been found.

## 6. Stability: a proved modulus modulo the kernel

The previous restart/trace argument proves \(\mathcal T:H\to L^2(J)\) compact. Therefore an orthonormal sequence \(h_n\) has \(\mathcal T h_n\to0\). No global lower bound \(\|h\|_2\le C\|\mathcal T h\|_{L^2(J)}\) or continuous inverse on the full infinite-dimensional \(H\) range can hold. Compactness alone proves neither an exact invisible input nor noninjectivity, nor a particular logarithmic rate.

There is, however, an unconditional **qualitative conditional stability modulo the exact kernel**. For \(s>0\), \(R>0\), let \(K=\ker\mathcal T\) (closed in \(H\)) and
\[
\omega_{s,R}(\varepsilon)=\sup\{\operatorname{dist}_H(h,K): h\in H^s(I)\cap H,\ \|h\|_{H^s}\le R,\ \|\mathcal T h\|_{L^2(J)}\le\varepsilon\}. \tag{18}
\]
The supremum is finite and \(\omega_{s,R}(\varepsilon)\to0\) as \(\varepsilon\downarrow0\). Proof: the \(H^s\)-ball is relatively compact in \(H\). If not, choose \(h_j\) with \(\varepsilon_j\downarrow0\) and distance at least \(c>0\). A subsequence converges in \(H\) to \(h\); boundedness of \(\mathcal T\) implies \(\mathcal T h=0\), hence \(h\in K\), contradicting \(\operatorname{dist}(h_j,K)\le\|h_j-h\|_2\to0\). Thus (18) is a genuine, nonconstructive modulus, not a quantified rate and not a bound on distance to the true input if \(K\ne0\).

If additionally \(K\cap H^s(I)=\{0\}\), compactness of the \(H^s\)-ball plus weak compactness in \(H^s\) gives \(\sup\{\|h\|_2:\|h\|_{H^s}\le R,\|\mathcal T h\|\le\varepsilon\}\to0\); this is full \(H\)-norm conditional stability on that ball, contingent on an **unproved** restricted injectivity hypothesis. The same observation applies to differences on bounded Sobolev classes, with radius doubled. No logarithmic, Hölder, or Lipschitz modulus is claimed, and delay alone is not shown to create a finite-dimensional invisible subspace.

## 7. Primary-source literature checks

The search is targeted and non-exhaustive. Statements and specified proof passages were inspected, not just abstracts; no theorem is assumed to transfer through an unverified hypothesis.

1. **Andrei Halanay and Luciano Pandolfi**, “Approximate controllability and lack of controllability to zero of the heat equation with memory,” [arXiv:1404.2745v1](https://arxiv.org/html/1404.2745). Theorem 2 and §3 proof treat a \(C^1\) time-convolution kernel multiplying the Laplacian on a bounded \(C^2\) domain, with distributed or admissible boundary control; the proof reduces reachable targets to the memoryless heat equation via a scalar Volterra equation and carefully handles boundary-control endpoint admissibility. Our memory is the lower-order \(S(t,x)\gamma\int e^{-\mu(t-s)}Y(s,x)ds\), with variable \(M,B,S\) and unknown initial memory. Their commuting Laplacian/eigenfunction construction and target state are not ours; no direct density result follows.
2. **Guillaume Olive**, “Boundary approximate controllability of some linear parabolic systems,” [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), Theorem 1.1 and Remark 1.3. The theorem explicitly requires an autonomous \(C_0\) generator with compact resolvent, complete adjoint root vectors and a relatively generator-bounded observation. Its all-time Fattorini criterion becomes finite-time in the paper's analytic heat systems; the paper's cascade has diffusion in both components. The theorem statement and the appendix proof were inspected, including the root-subspace and spectral-projection steps; no common autonomous generator, compact resolvent, root completeness or time analyticity is proved for our coupled PDE–ODE. No spectral rank test is transferred.
3. **Ze Li, Zhiyuan Li and Zhi Zhou**, “Inverse Heat Source Problems from Boundary Flux and Interior Observations on Sets of Low Hausdorff Dimension,” [arXiv:2609.10071v1](https://arxiv.org/html/2609.10071). Hypothesis 1 and Theorems 1.1–1.2 concern \(d\ge2\), a \(C^{1,1}\) domain, a separated source \(g(t)f(x)\), \(g\in W^{1,\infty}\), \(g(0)\ne0\), and stated spectral/a priori and boundary-trace hypotheses. The paper's §3 proof uses analyticity of the autonomous heat semigroup and its boundary spectral inequality; its delayed stability is not a result for our one-dimensional variable-coefficient coupled memory system. No logarithmic rate is imported.
4. **Sergei A. Avdonin, Sergei A. Ivanov and Jun Min Wang**, “Inverse Problems for the Heat Equation with Memory,” [arXiv:1612.02129v2](https://arxiv.org/html/1612.02129). Sections 1.3 and 2 formulate recovery of a time-convolution kernel for a Gurtin–Pipkin equation from a boundary Dirichlet-to-Neumann response operator, with zero initial temperature and a stated Laplace-transform asymptotic; the stationary proof uses Laplace transformation and solves a spatial ODE. Our unknown is an initial distributed memory profile in a nonautonomous equation, with one measured trace rather than the full response operator. The main proof dependencies and direct applicability are not established, so this is a contrast, not a transfer.
5. **Alfredo S. Gamboa, Juan Limaco and Luis P. Yapu**, “Controllability of a system of non-autonomous degenerate coupled parabolic equations,” [arXiv:2508.17546v1](https://arxiv.org/html/2508.17546). Their displayed system has two diffusive equations, bounded lower-order coefficients, \(b(t)\in W^{1,\infty}\), a positive coupling on an interior control set, and an interior control. Their null-control proof in §4 uses a Carleman/HUM construction. Our second component is an ODE, our coupling/principal dependence differs, \(B\) is not known bounded, and control is at one endpoint. Theorem 4's proof passage was inspected but its full dependency chain was not independently certified.

These sources establish useful techniques for different models; the present search does not establish an exhaustive absence of an applicable theorem.

## 8. Final theorem and research decision

| Question | Required verdict | Scope |
|---|---|---|
| Volterra input-output representation | **PROVED** | Exact causal operator identity (6); no pointwise Green kernel asserted. |
| Short-time boundary asymptotics | **CONDITIONAL** | Formula (11) is proved for the explicitly identified frozen half-line auxiliary problem only; actual-system boundary remainder is not established. Actual state asymptotics (9)–(10) are proved. |
| Delayed moment completeness | **NOT ESTABLISHED** | Exact infinite \(\ell^2\) condition (14), no independence theorem. |
| Adjoint range density | **NOT ESTABLISHED** | Equivalent to the unresolved coupled zero-output implication. |
| Approximate controllability | **NOT ESTABLISHED** | Density of the specific transposition memory-projection range is open. |
| Exact nonzero invisible input | **NOT CONSTRUCTED** | None satisfies the actual prescribed coefficients and loading. |
| Full odd-channel injectivity | **NOT ESTABLISHED** | Neither uniqueness nor an exact counterexample. |
| Conditional stability | **PROVED** | Qualitative, nonquantitative modulus (18) **only modulo the actual kernel**; full-input modulus is conditional on unproved restricted injectivity. |
| New mathematical theorem | **NOT ESTABLISHED** | Derivations here are elementary consequences; novelty and priority not demonstrated. |
| New foundational continuum theory | **REFORMULATE** | This is an inverse-observation question, not a new foundational theory. |

The best next route is a genuine nonautonomous boundary separation theorem for (5) on the actual reachable graph, or a proof of the \(\ell^2\)-completeness property (14) with estimates that survive mode coupling. Either would be independent of strict Hopf. A separately verified coupled boundary continuation theorem is one possible route, not assumed necessary. The missing theorem is qualitative; compactness already rules out full-space Lipschitz observability, so requiring such an estimate would be unnecessarily strong.
