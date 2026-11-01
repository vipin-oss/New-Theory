# Observation-kernel regularity: actual coupled system

## Finding and scope

For the frozen nonzero-loaded base in the previously established explicit small-load regime, the canonical odd observation kernel exists in \(L^2(J\times I)\); its rank-one-subtracted remainder has zero spatial endpoint trace and belongs to \(L^2(J;H^s(I))\) for every \(0\le s<1\). The exact missing endpoint is the square summability condition (9) below. We do **not** prove or disprove it for the actual base or for all coefficient triples in the stipulated class. No actual or coefficient-class counterexample is constructed. An explicit stronger regularity assumption does imply it, but has not been verified for the frozen experiment. This is an adversarial audit of earlier arguments, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder.

Let \(I=(0,L)\), \(J=(\delta,T)\), \(T=10/\lambda\), \(\delta=T/100\), and \(g(t)=g_*\sin^2(\pi t/T)\). The actual base has zero **initial** memory, nonzero \(g_*\), and coefficients
\[
M=c+d\theta_b,\quad B=-dQy_{b,t}-bE_b-br\gamma\theta_b+2k\gamma w_b,\quad S=\lambda\alpha(br\theta_b-2kw_b).
\]
The precise positive constants \(s_*\) and physical signs are in `direction-2-active-base-existence-and-regularity.md` §§1–3. In its nonempty regime \(0<|g_*|/L<s_*/2\), \(M\ge m_0>0\), \(M\in L^\infty\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2\), \(S\in\mathcal A:=H^1_tL^2_x\cap L^2_tH^2_x\). All three are even. Let \(H_o=L^2_o(I)\), with normalized odd sines
\[
\phi_n(x)=c_L\sin(q_nx),\quad c_L=\sqrt{2/L},\quad q_n=2\pi n/L.
\]
The actual odd forward system, including its nonautonomous mass and ODE history, is
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad Y(0)=0,\quad P(0)=h,\quad Y|_{\partial I}=0,
\quad \mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{1}
\]
The derivative trace exists in \(L^2(J)\) by the inherited strong forced estimate. Neither an endpoint condition on \(h,P\) nor independent data at the delay is introduced.

## 1. Construction and normalization of the actual kernel

Write \(k_n=\mathcal T\phi_n\). The prior actual-system corrector-and-cutoff proof, independently checked in `direction-2-critical-theorem-independent-audit.md`, gives
\[
k_n=\frac{a}{q_n}+\rho_n,\quad a(t)=2A_0c_Le^{-\mu t}S(t,0),\quad \|\rho_n\|_{L^2(J)}=o(q_n^{-3/2}). \tag{2}
\]
Since \(a\in L^2(J)\) and \(\sum q_n^{-2}<\infty\), \(\sum\|k_n\|_{L^2(J)}^2<\infty\). Thus \(\mathcal T:H_o\to L^2(J)\) is Hilbert–Schmidt and its canonical **source-odd** kernel is
\[
K(t,x)=\sum_{n\ge1}k_n(t)\phi_n(x)\quad\text{in }L^2(J\times I),\quad
(\mathcal Th)(t)=\int_I K(t,x)h(x)dx\quad\text{for a.e. }t. \tag{3}
\]
The latter equality holds for each fixed \(h\in H_o\), with a null set possibly depending on \(h\); it is not a classical impulse-response formula. A kernel acting only on odd inputs is not unique unless source parity is specified: adding any source-even \(L^2\) function changes no odd pairing and can change its apparent Sobolev regularity. (3) is the unique odd representative. We study **that** representative throughout.

Define the actual leading spatial profile, avoiding a guessed Fourier normalization,
\[
\ell(x)=c_L\left(\frac L4-\frac x2\right). \tag{4}
\]
It is odd about \(L/2\) and belongs to \(H^1(I)\). Direct integration gives \((\ell,\phi_n)=q_n^{-1}\), so its odd sine series is \(\sum q_n^{-1}\phi_n\) in \(L^2\). Its actual endpoint values are \(\ell(0)=c_LL/4\), \(\ell(L)=-c_LL/4\), and \(\ell'=-c_L/2\). Moreover \(\|\ell\|_2=L/\sqrt{24}\); \(h\mapsto a(\ell,h)\) is rank at most one and has norm \(\|a\|_{L^2(J)}L/\sqrt{24}\). In the older notation \(K_{\rm lead}=A_0e^{-\mu t}S(t,0)(1-2x/L)\), the same normalization follows from \(a\ell\).

The **actual remainder**, not a prescribed kernel, is
\[
R(t,x)=K(t,x)-a(t)\ell(x)=\sum_{n\ge1}\rho_n(t)\phi_n(x)\quad\text{in }L^2(J\times I). \tag{5}
\]
It arises by solving (1) for each initial sine, including \(P=e^{-\mu t}h+\gamma\int_0^te^{-\mu(t-s)}Y(s)ds\), taking the actual delayed boundary trace, then subtracting (4). No pre-delay state or boundary ODE condition is inserted.

## 2. Proven fractional mapping, endpoint behavior, and the exact barrier

For every \(0\le s<1\), (2) implies for all sufficiently large \(n\), \(\|\rho_n\|\le C q_n^{-3/2}\); hence
\[
\sum_{n\ge1}(1+q_n^2)^s\|\rho_n\|_{L^2(J)}^2<\infty\qquad(0\le s<1). \tag{6}
\]
Indeed the summand is \(O(n^{2s-3})\). The spectral norm of the Dirichlet Laplacian on odd sines and interpolation of \(L^2,H^1_0\) give
\[
R\in L^2(J;H^s(I)\cap H_o),\quad 0\le s<1;\qquad R(t,0)=R(t,L)=0\quad\text{a.e. }t\quad(1/2<s<1). \tag{7}
\]
This is a mapping estimate derived from the actual PDE column bound: for each \(s<1\), its norm is bounded by a constant times the weighted sum in (6), whose finite head and tail are controlled by the strong/weak/cutoff estimates. At \(s=1/2\), the spectral space is the appropriate Lions–Magenes space; the ordinary \(H^{1/2}\) statement follows without claiming a point trace. It follows that for a.e. \(t\),
\[
K(t,0)=A_0e^{-\mu t}S(t,0),\qquad K(t,L)=-A_0e^{-\mu t}S(t,0). \tag{8}
\]
These are **source-kernel** traces, not endpoint conditions on physical \(h\) or \(P\). In particular the nonzero endpoint of \(K\) is compatible with \(K\in H^1\); sine coefficients of \(a\ell\) do not obey a Dirichlet \(H^1_0\) spectral sum.

Because (7) already gives zero trace of \(R\), the endpoint question has an exact necessary and sufficient form:
\[
\boxed{\ R\in L^2(J;H^1(I))\quad\Longleftrightarrow\quad
\sum_{n\ge1}q_n^2\|\rho_n\|_{L^2(J)}^2<\infty.\ } \tag{9}
\]
For the forward implication, the assumed \(H^1\) regularity combined with the zero traces in (7) gives \(R(t)\in H^1_0\); the Dirichlet energy identity on the odd subspace gives the sum. Conversely, finite weighted sum makes the partial sums Cauchy in \(L^2(J;H^1_0)\), and their \(L^2\) limit is (5). If (9) holds, the actual weak derivative is
\[
\partial_xR=\lim_{N\to\infty}\sum_{n=1}^Nq_n\rho_n(t)c_L\cos(q_nx)\quad\text{in }L^2(J\times I),\quad
\|\partial_xR\|_2^2=\sum_nq_n^2\|\rho_n\|_2^2. \tag{10}
\]
No such convergence is currently established. By (2), \(\sum_{n\le N}q_n^2\|\rho_n\|^2=o(\log N)\), since \(q_n^3\|\rho_n\|^2\to0\) and harmonic means of a null sequence tend to zero. This is better than an unspecified logarithmic bound but need not be bounded. The barrier is therefore an **actual coupled-PDE weighted square sum**, not a mere question of taking a pointwise trace.

The established proof controls each column by a smooth-source corrector and then sends the source-approximation error to zero *after* \(n\to\infty\). Its two limits do not supply the simultaneous \(\ell^2\)-weighted sum (9). The weak estimate divides by \(M\), keeps \(M_x\), estimates \(B\in L^2\), and controls memory in \(H^{-1}\); the strong cutoff estimate retains \(M\chi'e\) and \(\chi'p\), including the entire history. Those estimates justify (2), not an unproved square-function estimate. The positive delay controls corrected initial mismatch but does not independently smooth the nondiffusive initial \(h\). No \(S_{xx}(t,0)\), \(M_t(t,0)\), or unproved classical boundary derivative is used.

## 3. A concrete additional sufficient approximation condition

Fix the actual feedback \(M,B,S,\mu,\gamma\), and vary **only** the auxiliary direct source amplitude \(f\) in \(MY_t-\kappa Y_{xx}=BY+Sp+e^{-\mu t}f\phi_n\), \(p_t+\mu p=\gamma Y\), zero initial data. Let \(\rho_n(f)\) subtract the matching leading \(e^{-\mu t}f(t,0)\) coefficient. The established source-approximation and smooth-corrector estimates imply, with constants independent of \(n\) and smooth even \(f\),
\[
\|\rho_n(S)\|\le Cq_n^{-3/2}\|S-f\|_{\mathcal A}+Cq_n^{-2}\|f\|_{H^3(Q_T)}. \tag{11}
\]
The fixed-feedback distinction is essential: otherwise an uncancelled \((f-S)\phi_n\) source appears. For each dyadic \(2^j\le n<2^{j+1}\), choose a smooth even \(f_j\). Summing (11) gives the sufficient criterion
\[
\boxed{\quad \sum_{j\ge0}\left(\|S-f_j\|_{\mathcal A}^2+2^{-j}\|f_j\|_{H^3(Q_T)}^2\right)<\infty\quad\Longrightarrow\quad R\in L^2(J;H^1_0(I)).\quad} \tag{12}
\]
Indeed \(\sum_{2^j\le n<2^{j+1}}q_n^{-1}=O(1)\) and \(\sum q_n^{-2}=O(2^{-j})\); sum over blocks and invoke (9). Constants depend on the actual fixed coefficients and \(\delta\), not \(j\). Mere density in \(\mathcal A\) does **not** establish this coupled error/cost summability; no claim that (12) is necessary is made.

As a concrete stronger sufficient hypothesis, \(S\in H^{2+\eta}(Q_T)\) isotropically for some \(0<\eta\le1\) permits even smooth approximants \(f_j\), with mollification scale \(\varepsilon_j=2^{-j/2}\), satisfying
\[
\|S-f_j\|_{\mathcal A}\le C2^{-j\eta/2}\|S\|_{H^{2+\eta}},\qquad
\|f_j\|_{H^3}\le C2^{j(1-\eta)/2}\|S\|_{H^{2+\eta}}. \tag{13}
\]
Both terms in (12) are \(O(2^{-j\eta})\). The extension/mollification bounds and \(H^3\)-cost of the complete corrector are detailed in `direction-2-abstract-generalization-and-strengthening.md` §3: it controls \(f_{xxx}\), \(f_{xt}\) endpoint traces via \(L^2_tH^1_x\), initial traces, and \(Bf_x\) via \(H^3(Q_T)\hookrightarrow W^{1,\infty}\). No derivative of \(M,B\) is needed. The premise includes extra time derivatives and is **not** a consequence established for the actual base. Thus (12)–(13) are conditional, not a modification of the frozen experiment or an unconditional Volkov application.

## 4. Why column little-o does not establish (9)

Let \(v_n\) be any orthonormal sequence in \(L^2(J)\) and put
\[
R_{\rm abs}(t,x)=\sum_{n\ge2}d_nv_n(t)\phi_n(x),\qquad d_n=\frac{n^{-3/2}}{\sqrt{\log(n+1)}}. \tag{14}
\]
This is an **abstract operator**, not coefficients or a solution of the physical PDE. It has \(\|R_{\rm abs}\phi_n\|=d_n=o(n^{-3/2})\), lies in every \(L^2(J;H^s)\), \(s<1\), and has zero endpoints in the trace sense. However \(\sum q_n^2d_n^2\asymp\sum 1/(n\log(n+1))=\infty\), so (9) rules out \(H^1\). Thus little-o plus the proved fractional and zero-trace properties does not logically yield the endpoint. This example does not prove that the actual \(R\) fails it.
