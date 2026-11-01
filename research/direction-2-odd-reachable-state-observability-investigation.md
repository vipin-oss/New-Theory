# Reachable-state observability and the exact odd kernel

**Date:** 1 November 2026

**Final verdict: NEW REACHABLE-STATE REDUCTION PROVED, INJECTIVITY OPEN.** The previous forward, factorization and adjoint calculations pass the audit, with proof details made explicit. The delayed observation operator is compact on the full restart space. More specifically, the reachable space is a graph over the finite-codimensional range of the delayed memory map plus a finite-dimensional vertical part. This yields a new exact reduction of its invisible states to the kernel of a compact quotient-output operator plus a finite-dimensional fiber. The compact quotient operator has not been shown injective or to have finite-dimensional kernel; neither the actual odd observation kernel nor a nonzero element of it is determined.

This is a single-agent Arena recalculation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. The frozen active experiment is not replaced by an equilibrium. No new theory or novelty, numerical finding, nonlinear inverse conclusion, or complete literature search is claimed.

## 1. Frozen system and audit setup

We read the complete preceding report `direction-2-odd-delayed-state-adjoint-investigation.md`, and checked its source calculations against `direction-2-odd-exact-kernel-investigation.md`, `direction-2-odd-channel-independent-audit.md`, `direction-2-active-base-regularity-independent-audit.md`, and the original formulation-A existence report. Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\). The symmetric base is the actual loaded solution with zero base initial memory. All frozen signs and couplings are retained:
\[
D=a+k,\ r=k/D,\ \alpha=a/D,\ \beta=b/D,\ \gamma=\lambda\beta,\ \mu=\lambda\alpha,\ d=b^2/D,\quad b\ne0.
\]
With \(Qv=v-\bar v\),
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b.\tag{1}
\]
The sufficient fixed-load condition \(0<q=|g_*|/L<s_*\) is assumed but numerically unverified. It yields positive \(m_0\le M_b\le m_1\), \(S\in L^\infty\), and \(B\in L^2((0,T)\times I)\). On \(J\), \(B\in L^6_{t,x}\cap L^\infty_tL^2_x\cap L^2_tL^\infty_x\), and \(M_b,\kappa/M_b\) are spatially Lipschitz and temporally \(3/4\)-Hölder, uniformly in the other variable. The coefficients are even in space; \(S\) is continuous by the base construction. None of these bounds implies \(B\in L^\infty_{t,x}\) or classical \(C^1\) coefficients.

Put \(H=H_o=L^2_o(I)\), \(V=V_o=H^1_0(I)\cap H\), \(X=X_o=H^2(I)\cap H\), \(Z_1=V\times H\), and \(Z=H\times H\). The actual odd input is \(h\in X\); it need not vanish at the spatial endpoints. The system is
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\\
Y(0,\cdot)=0,\quad P(0,\cdot)=h,\quad Y(t,0)=Y(t,L)=0,
\end{cases}\qquad
\mathcal T h=2A_0\kappa Y_x(\cdot,0)|_J.\tag{2}
\]
Time is written first in pointwise notation. The earlier bound extends the linear map from \(X\) to \(H\); it does not extend the nonlinear admissible set. We write the extension as \(\mathcal T\).

## 2. Independent audit of the latest report

| Item | Classification | Recalculation / qualification |
|---|---|---|
| 1. Forward restart with \((y_0,p_0)\in Z_1\) | **Correct as stated** | The proof needs the 1-D \(H^1_0\to L^\infty\) bound, Galerkin projection of the mass term, and the compactness/weak-limit argument given below. The positive-time coefficient upgrade is more than is needed for this estimate. |
| 2. \(\mathcal T=\mathcal R_\delta\mathcal S_\delta\) | **Correct as stated** | Restriction of the original solution has the same delayed trace and solves the restart problem; uniqueness identifies it. The \(H\) extension follows from the linear bound, not nonlinear admissibility. |
| 3. \(U_\delta\), \(K_\delta\), \(D_\delta\) | **Correct as stated** | \(U_\delta:H\to H\) is compact via \(V\Subset H\), not necessarily compact as a map into \(V\). \(K_\delta\) is bounded into \(H^2\cap H^1_0\), so \(D_\delta=e^{-\mu\delta}I+K_\delta\) is index-zero Fredholm on \(H\). |
| 4. Closed range and finite kernel in \(Z\) | **Correct as stated** | It is a compact perturbation of the bounded-below injection \(h\mapsto(0,e^{-\mu\delta}h)\); the contradiction argument below also verifies closed range. |
| 5. Closed range and infinite cokernel in \(Z_1\) | **Correct as stated** | A \(Z_1\)-convergent reachable sequence converges in \(Z\), where the range is closed. The quotient embeds \(V/U_\delta(\ker D_\delta)\); the denominator is finite-dimensional. |
| 6. Exact kernel sequence | **Correct as stated** | \(0\to N\to\ker\mathcal T\xrightarrow{\mathcal S_\delta}W\to0\) follows from factorization; the intersection alone does not exclude \(N\). The restricted \(X\) version is algebraic and its image need not be closed. |
| 7. Transposition adjoint and signs | **Correct as stated** | The forward source map is bounded in \(L^2\), and the Riesz construction gives the weak identity and \(w(T)=0\). The formal boundary data and \(M_b(T)z(T)=0\) are **transposition conditions**, not proven classical traces. |
| 8. \(X\) versus \(H\) injectivity | **Correct as stated** | \(\ker(\mathcal T|_X)=X\cap(\operatorname{ran}\mathcal T^*)^\perp\); \(H\)-density of the adjoint range is sufficient but not logically necessary for injectivity on \(X\). Sines are dense in \(H\), not in all \(X\) in its \(H^2\) norm. |

No mathematical contradiction to the preceding report was found. Its term “correct as stated” here includes its stated sufficient load condition and function-space qualifications; the proof details below are not extra assumptions.

### 2.1 Forward problem and endpoint trace

For \((y_0,p_0)\in V\times H\), or in the full non-parity space when constructing the adjoint, consider on \((a,b)\subseteq(0,T)\)
\[
M_by_t-\kappa y_{xx}=By+Sp+F,\quad p_t+\mu p=\gamma y+G,\quad y|_{\partial I}=0,\tag{3}
\]
with \(F,G\in L^2_{t,x}\). Galerkin approximations use Dirichlet sine functions for \(y\), an \(L^2\) orthonormal basis for \(p\), and positive mass matrices. Testing by \(y_t\) and \(p\), respectively, with \(E=\kappa\|y_x\|_2^2+\|p\|_2^2\), gives after Young's inequality
\[
E'(t)+m_0\|y_t\|_2^2
\le C(1+\|B(t)\|_2^2)E(t)+C(\|F(t)\|_2^2+\|G(t)\|_2^2).\tag{4}
\]
Indeed \(\|By\|_2\le\sqrt L\|B(t)\|_2\|y_x\|_2\); bounded \(S\) controls \(Sp\), while the \(\gamma y\) term is controlled by Poincaré. No derivative of \(M_b\) is introduced. Gronwall applies because \(\|B(t)\|_2^2\in L^1_t\). The projected equation implies
\[
\kappa\|y_{xx}\|_{L^2_{t,x}}\le
\|M_by_t\|_2+\|By\|_2+\|Sp\|_2+\|F\|_2.
\]
This bound is uniform for the approximations. The ODE bounds \(p_t\) in \(L^2\). A subsequence converges weakly in the strong-temperature spaces; \(By_n\) is bounded in \(L^2\) and converges in distributions to \(By\), since \(y_n\to y\) in \(L^2_tH^s_x\subset L^2_tC_x\) for \(1/2<s<1\), and \(B\in L^2_{t,x}\). Thus its weak \(L^2\) limit is \(By\). Other terms pass weakly. The same energy inequality for differences proves uniqueness. Standard Hilbert time-trace theory yields
\[
y\in\mathcal E(a,b):=H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0)\cap C_tH^1_0,\quad p\in H^1_tL^2_x,
\]
with a bound by \(\|y_0\|_V+\|p_0\|_H+\|F\|_2+\|G\|_2\). The 1-D trace \(H^2\to\mathbb R\), \(v\mapsto v_x(0)\), makes \(y_x(\cdot,0)\in L^2(a,b)\). It is this strong-temperature estimate, not a pointwise boundary PDE, that defines the observation.

### 2.2 Compactness and exact state geometry

The actual solution bound gives \(U h=Y(\delta)\in V\) and
\[
D_\delta h=P(\delta)=e^{-\mu\delta}h+Kh,\qquad
Kh=\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr.\tag{5}
\]
\(U:H\to H\) is compact by \(V\Subset H\). The Bochner integral has a bounded range in \(H^2\cap H^1_0\), hence \(K:H\to H\) is compact. Thus \(D_\delta\) is Fredholm of index zero. The joint map \(\mathcal S h=(Uh,D_\delta h)\in Z_1\) obeys the exact factorization (by restart uniqueness)
\[
\mathcal T=\mathcal R\mathcal S,\qquad \mathcal R:Z_1\to L^2(J).\tag{6}
\]
Here \(\mathcal R(y_0,p_0)=2A_0\kappa y_x(\cdot,0)\) for the unique solution of (3) with \(a=\delta,F=G=0\). This is not an assertion that every \(Z_1\) state is reachable.

For the injection \(i:Z_1\hookrightarrow Z\), \(i\mathcal S=J_0+C\), where \(J_0h=(0,e^{-\mu\delta}h)\) is bounded below and \(C=(U,K):H\to Z\) is compact. If unit \(h_n\perp\ker\mathcal S\) had \(i\mathcal S h_n\to0\), compactness would give a convergent subsequence of \(Ch_n\), whence a strongly convergent subsequence of \(h_n\); its nonzero limit would lie in the kernel and its orthogonal complement. This proves a bound below on \((\ker\mathcal S)^\perp\), finite-dimensional kernel, and closed range in \(Z\). The range is then closed in the stronger \(Z_1\) topology. Because \(\operatorname{ran}\mathcal S\cap(V\times\{0\})=U(\ker D_\delta)\times\{0\}\), its cokernel in \(Z_1\) is infinite-dimensional. Hence \(\mathcal S:H\to Z_1\) is upper semi-Fredholm but not Fredholm; it is not compact because \(D_\delta\) is a nonzero identity plus compact.

## 3. Delayed observation: compactness and obstruction

**Theorem 1.** Under the frozen hypotheses, \(\mathcal R:Z_1\to L^2(J)\) is compact. It is neither Fredholm nor upper semi-Fredholm. Its restriction to the closed reachable subspace is compact and is not bounded below in the \(Z_1\) norm.

**Proof.** The restart estimate bounds the temperature solution operator from \(Z_1\) into \(H^1(J;L^2)\cap L^2(J;H^2)\). For \(3/2<s<2\), Aubin–Lions gives a compact embedding of this space into \(L^2(J;H^s(I))\). Since \(H^s(I)\ni v\mapsto v_x(0)\) is continuous, composition gives compactness of \(\mathcal R\).

A compact operator from an infinite-dimensional Hilbert space cannot have both closed range and finite-dimensional kernel: otherwise its restriction to the orthogonal complement of the kernel has a bounded inverse on its range, and the identity on that complement would be compact. Thus it is not upper semi-Fredholm and hence not Fredholm. The reachable subspace is closed and infinite-dimensional because \(\mathcal S\) has finite-dimensional kernel on infinite-dimensional \(H\). The same compactness argument shows \(\mathcal R\) cannot be bounded below on it. □

This theorem does **not** determine whether \(\ker\mathcal R\) or \(W=\ker\mathcal R\cap\operatorname{ran}\mathcal S\) is finite- or infinite-dimensional: compact maps may be injective or have a large kernel. There is no proven hidden exact nullspace caused by memory. For an explicit approximate obstruction, choose any \(H\)-orthonormal \(h_n\). Then \(\mathcal T h_n\to0\), but by (5) and compactness of \(K\),
\[
\|P[h_n](\delta)\|_H=\|e^{-\mu\delta}h_n+Kh_n\|_H\longrightarrow e^{-\mu\delta}>0.\tag{7}
\]
Thus no constant controls the reachable memory or \(Z_1\) norm by the fixed delayed \(L^2\) endpoint flux. The directions remain approximate, not exact kernel elements. No claim of a lower-rank, weaker-norm or conditional observability obstruction follows.

## 4. A stronger reachable-state reduction

Let
\[
E=\ker D_\delta,\quad H_1=E^\perp,\quad P_*=\operatorname{ran}D_\delta,\quad N=\ker\mathcal S.
\]
Fredholmness gives \(\dim E<\infty\), \(P_*\) closed with \(\operatorname{codim}P_*=\dim E\), and a bounded inverse
\[
D_1^{-1}:P_*\to H_1,\qquad D_1=D_\delta|_{H_1}.
\]
Set
\[
A_*=UD_1^{-1}:P_*\to V,\qquad F_*=U(E)\subset V.\tag{8}
\]
\(A_*\) is bounded; we do not assume it is compact into \(V\). \(F_*\) is finite-dimensional, with \(\dim F_*=\dim E-\dim N\).

**Theorem 2 (reachable graph and output quotient).** The actual reachable subspace is
\[
\operatorname{ran}\mathcal S
=\{(A_*p+v,p):p\in P_*,\ v\in F_*\}
=\operatorname{graph}(A_*)\oplus(F_*\times\{0\}).\tag{9}
\]
Let \(O_*:=\mathcal R(F_*\times\{0\})\), a finite-dimensional closed subspace of \(L^2(J)\), \(\pi:L^2(J)\to L^2(J)/O_*\) the quotient map, and define
\[
\Gamma:P_*\to L^2(J)/O_*,\qquad
\Gamma p=\pi\mathcal R(A_*p,p),\quad
F_0:=\{v\in F_*:\mathcal R(v,0)=0\}.\tag{10}
\]
Then \(\Gamma\) is compact and there is a bounded linear isomorphism
\[
W\cong\ker\Gamma\oplus F_0.\tag{11}
\]
In particular, \(W\cap(V\times\{0\})=F_0\times\{0\}\) is finite-dimensional, and \(\dim W=\dim\ker\Gamma+\dim F_0\), possibly infinite.

**Proof.** Each \(h\in H\) uniquely decomposes as \(h=h_1+e\), \(h_1\in H_1,e\in E\). Its delayed memory is \(p=D_1h_1\), and its temperature is \(A_*p+Ue\), giving (9); conversely each displayed pair is attained. The sum is direct because the second component of a graph element is \(p\). The graph map and \(\mathcal R\) are bounded, and Theorem 1 makes their composition, and hence \(\Gamma\), compact.

A reachable pair \((A_*p+v,p)\) is in \(W\) iff \(\mathcal R(A_*p,p)+\mathcal R(v,0)=0\), equivalently \(\Gamma p=0\) and \(v\) is a solution of a finite-dimensional linear equation. Choose the bounded right inverse of \(F_*\to O_*\), \(v\mapsto\mathcal R(v,0)\), on \(F_0^\perp\). For every \(p\in\ker\Gamma\) it provides the unique correction \(v_p\in F_0^\perp\) with \(\mathcal R(v_p,0)=-\mathcal R(A_*p,p)\). All other corrections are \(v_p+v_0\), \(v_0\in F_0\). The corresponding map \((p,v_0)\mapsto(A_*p+v_p+v_0,p)\) is a bounded bijection with bounded inverse by the displayed projections. This proves (11). □

This is a theorem about **actual reachable states**, not simply restating \(W\): the memory component lies in a closed finite-codimensional subspace and determines the temperature up to the finite-dimensional vertical fiber. It reduces a two-field observation kernel to one compact operator on \(P_*\) and the explicitly finite-dimensional \(F_0\). It does **not** prove \(\ker\Gamma\) finite-dimensional or zero. The exact short sequence
\[
0\to N\to\ker(\mathcal T:H\to L^2(J))\xrightarrow{\mathcal S}W\to0\tag{12}
\]
remains valid; bounded inverse on \(N^\perp\) gives \(\ker\mathcal T\cong N\oplus W\). For \(X\), replace \(W\) by \(\ker\mathcal R\cap\mathcal S(X)\); that smaller set is not asserted closed.

A further exact regularity consequence is
\[
E\subset H^2(I)\cap H^1_0(I)\cap H\subset X,\quad N\subset E\subset X.\tag{13}
\]
Indeed \(D_\delta h=0\) implies \(h=-e^{\mu\delta}Kh\), and \(K\)'s range is contained in \(H^2\cap H^1_0\). Thus any nonzero loss of the joint pre-delay state would already be an admissible **linearized** odd \(H^2\) direction with zero endpoint values; it would be an exact observation-kernel element because of (6). We have not shown that such an element exists. In particular the pre-delay factor cannot hide a kernel exclusively in the \(H\setminus X\) extension.

## 5. Continuation, backward uniqueness and the pre-delay map

### 5.1 What zero endpoint derivatives imply

For a reachable trajectory, odd symmetry gives \(Y_x(t,L)=Y_x(t,0)\); hence zero measured derivative means both vanish a.e. on \(J\), alongside zero Dirichlet data. For every \(\psi\in H^2(I)\),
\[
\langle M_bY_t,\psi\rangle-\kappa\langle Y,\psi''\rangle
+\kappa Y_x(t,0)\psi(0)-\kappa Y_x(t,L)\psi(L)
=\langle BY+SP,\psi\rangle.\tag{14}
\]
All terms are \(L^2_t\), with the signs obtained by two spatial integrations by parts. When both derivatives vanish, the integrated identity still contains the unknown distributed source. No termwise trace of \(Y_t\) or \(Y_{xx}\) is justified, and this calculation does not prove \(Y=0\) on the delayed cylinder. The needed continuation is precisely a coupled, variable-coefficient statement for reachable trajectories; it has not been derived here. It is sufficient but not necessary for odd injectivity.

If the stronger conclusion \(Y=0\) were independently obtained on \(J\), then (2) yields \(SP=0\) there and \(P(t)=e^{-\mu(t-\delta)}P(\delta)\). Under the additional, unverified \(q<q_{\rm nd}=|b|r\theta_*/(8kC_w)\), the previously proved \(|S|>s_0:=\lambda\alpha|b|r\theta_*/4\) gives \(P=0\) and thus \(\mathcal S h=0\). Without that uniform bound, a weaker sufficient condition is that for a.e. \(x\), the set \(\{t\in J:S(x,t)\ne0\}\) has positive measure; this condition has not been proved under \(q<s_*\). In either case recovery of \(h\) requires \(N=0\), which remains open. The full ODE history (5) is retained.

### 5.2 An improved conditional Neumann criterion

The previous data-only bound \(\|Y_t\|_{L^2(0,\delta;H)}\le C_Y\|h\|_H\) is valid with the explicit \(C_Y\) given in §4 of the preceding report; it uses the fixed reference solver and contraction margin, not the unknown \(h\). Since \(Y(r)=\int_0^rY_t(s)ds\), Fubini gives
\[
Kh=\gamma\int_0^\delta \frac{1-e^{-\mu(\delta-s)}}{\mu}Y_t(s)ds,
\quad
\|K\|\le |\gamma|C_Y H_\mu(\delta),\tag{15}
\]
\[
H_\mu(\delta)=\left[\int_0^\delta\left(\frac{1-e^{-\mu u}}\mu\right)^2du\right]^{1/2}
\le\delta^{3/2}/\sqrt3<2\delta^{3/2}/3.\tag{16}
\]
Thus the additional condition \(|\gamma|C_YH_\mu(\delta)<e^{-\mu\delta}\) makes \(D_\delta\) invertible and \(N=0\) by Neumann series. It sharpens the previous \((2/3)|\gamma|C_Y\delta^{3/2}\) criterion without altering \(T,\delta\), or parameters. It has not been checked for actual data and does not establish \(W=0\).

### 5.3 A coefficient-class counterexample, not a physical counterexample

Even smooth, symmetric coefficients, positive mass and nonzero coupling alone do not force \(D_\delta\) injective. To see this, consider only the *abstract class* of systems (2), not the active constitutive coefficients (1). Let \(M_b=1\), \(\kappa=1\), \(\mu>0\), \(\gamma\ne0\), \(\rho_1=(2\pi/L)^2\), \(\omega=\pi/(2\delta)\), \(B=\rho_1-\mu\), and \(S=-\omega^2/\gamma\), all constants. For initial \(h=\phi_1=\sqrt{2/L}\sin(2\pi x/L)\), the separated solution is
\[
P(t,x)=e^{-\mu t}\cos(\omega t)\phi_1(x),\quad
Y(t,x)=-\frac\omega\gamma e^{-\mu t}\sin(\omega t)\phi_1(x).
\tag{17}
\]
Direct differentiation gives \(P_t+\mu P=\gamma Y\), and \(Y_t+\rho_1Y=BY+SP\). The initial and spatial boundary conditions hold, and \(P(\delta)=0\) although \(h\ne0\). The temperature at \(\delta\) is nonzero, so this is **not** a counterexample to joint-state injectivity, nor to observation injectivity, nor to the actual physical model: its constant coefficients are deliberately not asserted to arise from (1) or from the given loading. It shows why a proof of \(D_\delta\) injectivity must use more than the broad regularity and positivity class. No abstract-class example of nontrivial \(N\) is claimed.

## 6. Re-derived adjoint and density

For \(F,G\in L^2((0,T)\times I)\), let \((u,v)\) solve (3) on the full space, with zero initial data. By §2, \(F,G\mapsto u_x(\cdot,0)|_J\) is bounded. For \(f\in L^2(J)\), Riesz representation uniquely defines \(z_f,w_f\in L^2_{t,x}\) by
\[
\iint(Fz_f+Gw_f)=2A_0\kappa\int_J f(t)u_x(t,0)dt.\tag{18}
\]
This is the boundary transposition solution on the full space; restriction to odd initial inputs is made later. Taking smooth compactly supported \(u,v\) as forward test pairs yields
\[
-\partial_t(M_bz_f)-\kappa(z_f)_{xx}-Bz_f-\gamma w_f=0,\qquad
-(w_f)_t+\mu w_f-Sz_f=0\quad\text{in distributions}.\tag{19}
\]
Because \(S\in L^\infty\), \(w_f\in H^1(0,T;L^2(I))\). Choosing zero \(u\) and arbitrary smooth \(v\) with \(v(0)=0\) in (18) establishes the genuine terminal trace \(w_f(T)=0\) and
\[
w_f(t)=\int_t^T e^{-\mu(s-t)}S(s)z_f(s)ds.\tag{20}
\]
The resulting a priori estimates are \(z_f\in L^2_{t,x}\), \(w_f\in H^1_tL^2_x\), with norm \(\le C\|f\|_{L^2(J)}\). More regularity of \(z_f\), especially a classical boundary or terminal trace, is not established here.

For smooth fields, integration by parts gives boundary term \(\kappa[y_x(0)z(0)-y_x(L)z(L)]\), terminal term \(\langle M_b(T)y(T),z(T)\rangle+\langle p(T),w(T)\rangle\), and the negative initial pairing. Thus (18) encodes \(z(0,t)=2A_0\mathbf1_J f(t)\), \(z(L,t)=0\), and \(M_b(T)z(T)=0\) **in the transposition sense**, not as classical traces. On \((0,\delta)\), the boundary input in that sense is zero, while (19) continues to hold. In particular, from (20), for \(0\le t\le\delta\)
\[
w_f(t)=e^{-\mu(\delta-t)}w_f(\delta)+\int_t^\delta e^{-\mu(s-t)}S(s)z_f(s)ds.\tag{21}
\]
This is the actual backward pre-observation evolution of the memory component; it does not show that the possible \(w_f(0)\) are dense.

For an original input \(h\in H\), define \(v=P-e^{-\mu t}h\). Then \((Y,v)\) has zero initial values and solves (3) with \(F=Se^{-\mu t}h\), \(G=0\). Equations (18)–(20) give
\[
\langle\mathcal T h,f\rangle_{L^2(J)}
=\left\langle h,\Pi_o w_f(0)\right\rangle_H,\qquad
\mathcal T^*f=\Pi_o w_f(0).\tag{22}
\]
Thus, if \(\mathscr A=\{\Pi_o w_f(0):f\in L^2(J)\}\),
\[
\ker(\mathcal T|_H)=\mathscr A^\perp,\quad
\ker(\mathcal T|_X)=X\cap\mathscr A^\perp.\tag{23}
\]
Density of \(\mathscr A\) is equivalent to injectivity on \(H\) and sufficient for \(X\); the restricted annihilator may be zero even if \(\mathscr A\) is not dense. By (6), \(\mathcal T^*=\mathcal S^*\mathcal R^*\). If \(\mathcal R^*f=(a_f,b_f)\in V\times H\) is represented using the chosen product inner product, then
\[
\Pi_o w_f(0)=U^*a_f+D_\delta^*b_f.\tag{24}
\]
This legitimate operator identity retains the pre-delay propagation; it is not a proof of density, and \(U^*:V\to H\) is not asserted compact.

## 7. Moments, transformations and completeness

Use \(\phi_n=\sqrt{2/L}\sin(2n\pi x/L)\), \(\rho_n=(2n\pi/L)^2\), \(u_n=\langle Y,\phi_n\rangle\), \(p_n=\langle P,\phi_n\rangle\). The exact projected equations are
\[
\sum_m\langle M_b\phi_m,\phi_n\rangle u_m'+\kappa\rho_nu_n
=\langle BY,\phi_n\rangle+\sum_m\langle S\phi_m,\phi_n\rangle p_m,
\quad p_n'+\mu p_n=\gamma u_n,\quad p_n(0)=h_n.\tag{25}
\]
The mass and source series converge by Parseval, \(BY\in L^2\), and the derivative trace obeys
\[
Y_x(\cdot,0)=\lim_{N\to\infty}\sum_{n\le N}\phi'_n(0)u_n(\cdot)
\quad\text{in }L^2(J),\tag{26}
\]
using spectral convergence in \(L^2H^s\), \(3/2<s<2\). Multiplication by \(M_b(t)\) is bounded and uniformly invertible on \(H\), so inverting its infinite matrix is legitimate as an \(\ell^2\) operator a.e. in time; it does **not** commute with the Laplacian or diagonalize the other multipliers, nor does it justify differentiating that time-dependent matrix. The ODE gives the exact Volterra relation
\[
p_n(t)=e^{-\mu t}h_n+\gamma\int_0^t e^{-\mu(t-r)}u_n(r)dr,
\]
but \(S(x,t)\) and the initial source still couple modes. No bounded invertible triangularizing transformation for these actual coefficients has been obtained.

For \(\psi_n=\mathcal T\phi_n\), boundedness yields \(\sum_{n\le N}h_n\psi_n\to\mathcal T h\) in \(L^2(J)\), even when \(h\in X\) has nonzero endpoint values. A sufficient completeness theorem would show that the only \(h\in X\) with this limit zero is \(h=0\); the stronger condition is that for each \(n\) there exist \(f_{n,j}\) with \(\|\Pi_ow_{f_{n,j}}(0)-\phi_n\|_H\to0\). No such functions, Riesz basis, or exact nonzero annihilator has been constructed. Compactness rules out a uniform \(\ell^2\) Riesz lower bound for \((\psi_n)\), but not qualitative independence. Differentiating (26) termwise is unjustified; finite matrix rank or small singular values decide neither the infinite kernel nor density.

## 8. Narrow primary-source check

Only the following primary theorem families were checked; no theorem is claimed applicable from an abstract or from a spectral analogy.

1. **G. Olive**, *Boundary approximate controllability of some linear parabolic systems*, [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), Theorem 1.1 and Remark 1.3. The theorem assumes an autonomous \(C_0\) semigroup generator with **compact resolvent**, complete adjoint root vectors, and a relatively generator-bounded observation. It equates the all-positive-time observable-state property on the generator domain with the Fattorini eigenvector condition; the paper uses analyticity to pass to a finite observation interval in its heat examples. Its systems have Laplacians in each heat component and constant matrix or specified cascade couplings. Our active coefficients are time-dependent, the second component is a distributed ODE without diffusion, and no common autonomous generator, compact resolvent, completeness, or analytic time continuation has been established. Therefore neither the spectral test nor its finite-time specialization applies directly. We checked the theorem statement, not all proofs of its applications.

2. **D. P. Jha and R. K. George**, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), Lemma 3.5 and Proposition 3.8. The displayed ODE realization has zero initial auxiliary memory; the parabolic operator has constant principal Laplacian and their estimate includes moving **interior** observation, forcing and a short-time remainder under their weight/geometric assumptions. This is neither the fixed-endpoint derivative nor arbitrary correlated \(P(\delta)\) of (2). It supplies no direct density or backward-uniqueness theorem here. This statement comparison does not certify the whole preprint.

No inspected primary theorem settles the requested active reachable kernel. The search is narrow, not exhaustive; no DOI is supplied where not verified.

## 9. Status and decision

| Question | Status | Exact reason |
|---|---|---|
| Forward restart well-posedness | **Proved under frozen hypotheses** | Energy/Galerkin estimate (4), sources and traces in §2. |
| Delayed-state factorization | **Proved** | Uniqueness of restart, (6). |
| Closed range of state map | **Proved** | Compact perturbation of a bounded-below injection, §2.2. |
| Finite-dimensional pre-delay kernel | **Proved** | \(N\subset\ker D_\delta\), with \(D_\delta\) Fredholm; (13) strengthens regularity. |
| Delayed observation kernel on all states | **Dimension unresolved** | \(\mathcal R\) is compact, but compactness does not determine its exact kernel. |
| Reachable delayed observation kernel \(W\) | **New reduction; dimension unresolved** | \(W\cong\ker\Gamma\oplus F_0\), \(F_0\) finite-dimensional, \(\Gamma\) compact. |
| Adjoint transposition formulation | **Proved** | Riesz construction and source-pairing (18)–(22); classical boundary traces not asserted. |
| Adjoint-density criterion | **Proved** | Orthogonal-complement identities (23). |
| Adjoint density | **Open** | No proof of approximate generation of every initial odd memory state. |
| Injectivity on \(X_o\) | **Open** | Neither \(N=0\) nor the restricted reachable observation kernel has been established. |
| Injectivity on \(H_o\) | **Open** | Full adjoint density / \(N=W=0\) remains unproved. |
| Exact nonzero invisible input | **Not constructed** | Approximate invisible sequences and the abstract \(D_\delta\) example do not satisfy the required full conclusion for the active experiment. |

The best next target is either to prove \(\ker\Gamma=\{0\}\), \(F_0=\{0\}\), and \(N=\{0\}\), or to prove directly that the adjoint initial memory states separate \(X\); the latter would automatically eliminate any \(N\subset X\). Neither a full boundary-to-interior UC theorem nor a strong norm observability inequality is logically necessary. There is no verified numerical parameter/base data for the actual experiment, so no numerical approximation was fabricated.

**Final verdict: NEW REACHABLE-STATE REDUCTION PROVED, INJECTIVITY OPEN.**
