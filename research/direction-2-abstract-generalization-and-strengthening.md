# Abstract generalization and strengthening: delayed boundary traces

## Scope and conclusion

The previous argument extends to **any fixed finite number of spatially distributed ODE memory branches**, non-even coefficients, both endpoint fluxes, and bounded linear combinations of those fluxes. The extension below is a mathematical PDE comparison, not a new constitutive law and not a modification of the frozen thermoviscoelastic experiment. Its proof is an adaptation of the same energy, corrector, cutoff and density machinery. We do not claim chronological novelty or that these assumptions are minimal. Under an additional isotropic space–time Sobolev assumption, a quantitative remainder rate follows; the actual base has not been shown to have that extra regularity.

For the candidate theorem concerning the original model and its explicit parameter threshold, see `direction-2-exact-prior-art-and-overlap-audit.md` §2. Exact injectivity remains independent and unresolved. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is not independent human certification.

## 1. A fixed finite-memory proposition

Let \(I=(0,L)\), \(Q=(0,T)\times I\), \(J=(\delta,T)\), \(0<\delta<T\), \(V=H^1_0(I)\), and \(\mathcal A=H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I))\). Fix \(N<\infty\), \(\kappa>0\), constants \(\mu_j>0\), \(\gamma_j\in\mathbb R\), and real coefficients satisfying
\[
0<m_0\le M\le m_1,\quad M_x\in L^\infty_tL^2_x,\quad B\in L^2(Q),\quad S_j\in\mathcal A. \tag{1}
\]
All coefficients are measurable and no reflection symmetry is assumed. Let \(Y(0)=0\), \(Y|_{\partial I}=0\), \(P_j(0)=h_j\in L^2(I)\), with no endpoint condition on \(h_j\), and solve
\[
MY_t-\kappa Y_{xx}=BY+\sum_{j=1}^NS_jP_j,\qquad P_{j,t}+\mu_jP_j=\gamma_jY. \tag{2}
\]
Let \(q_m=m\pi/L\), \(\phi_m=c_L\sin(q_mx)\), \(c_L=\sqrt{2/L}\). For input in only branch \(j\), \(h_j=\phi_m\), denote the two **outward heat powers**, divided by area, by
\(\mathbf k_{j,m}=\kappa(Y_x(t,0),-Y_x(t,L))|_J\). Then
\[
\boxed{\mathbf k_{j,m}={c_Le^{-\mu_jt}\over q_m}\bigl(S_j(t,0),-(-1)^m S_j(t,L)\bigr)+\mathbf r_{j,m},\quad
\|\mathbf r_{j,m}\|_{L^2(J;\mathbb R^2)}=o(q_m^{-3/2}).} \tag{3}
\]
For \(h_j=a_j\phi_m\) and fixed vector \(a\in\mathbb R^N\), sum the \(N\) leading terms and remainders. This is valid for each fixed system and \(j\); constants can depend on \(N\), coefficients, and \(\delta\). It does not imply uniformity for an unconstrained growing family of systems.

### 1.1 Forced estimates and their dependence on branches

For \(F,G_j\in L^2(Q)\), \(y_0\in V\), \(p_{j,0}\in L^2\), write the forced version of (2). Testing a sine Galerkin system by \(y_t\), each ODE by \(p_j\), and using \(\|y\|_\infty\le\sqrt L\|y_x\|_2\) gives, for \(X=\kappa\|y_x\|_2^2+\sum\|p_j\|_2^2\),
\[
X'+m_0\|y_t\|_2^2\le C\Big(1+\|B(t)\|_2^2+\sum_j\|S_j(t)\|_\infty^2+\sum_j\gamma_j^2\Big)X+C(\|F\|_2^2+\sum_j\|G_j\|_2^2). \tag{4}
\]
Here \(-\mu_j\|p_j\|^2\) is discarded; a bound on \(\max_j\mu_j\) is needed for the \(p_{j,t}\) norm. Gronwall, the projected heat equation and the ODE yield
\[
\|y\|_{H^1_tL^2\cap L^2_tH^2}+\Big(\sum_j\|p_j\|_{H^1_tL^2}^2\Big)^{1/2}
\le C_N\left(\|y_0\|_V+\|(p_{j,0})\|_{\ell^2L^2}+\|F\|_2+\|(G_j)\|_{\ell^2L^2}\right). \tag{5}
\]
Existence follows from the positive Galerkin mass matrix and compactness; \(By_m\) passes using the uniform \(L^\infty\) bound and almost-everywhere convergence, and the other terms pass weakly. The estimate also proves uniqueness. Its standard details parallel the one-branch proof in the active-base report, §4.

For the weak estimate divide by \(M\), test by \(y\), and test each ODE in \(V'\). Since \(M^{-1},S_j/M\in L^\infty_tH^1_x\) and multiply \(V\) into itself, the cross term is bounded by
\[
\left|\sum_j\langle p_j,(S_j/M)y\rangle\right|
\le\epsilon\|y_x\|_2^2+C_\epsilon\Big(\sum_j\|S_j/M\|_{H^1}^2\Big)\sum_j\|p_j\|_{V'}^2. \tag{6}
\]
Together with \(\|B(t)\|_2^{4/3}\in L^1_t\) and \(\|(\kappa/M)_x\|_2^4\in L^\infty_t\), Gronwall gives
\[
\|y\|_{L^\infty L^2}+\|y\|_{L^2V}+\|(p_j)\|_{L^\infty\ell^2V'}
\le C_N(\|y_0\|_2+\|(p_{j,0})\|_{\ell^2V'}+\|F\|_{L^2V'}+\|(G_j)\|_{L^2\ell^2V'}). \tag{7}
\]
This is an a priori bound for the strong solutions constructed above, not an existence claim for arbitrary \(V'\) forcing.

For a family indexed by \(N\), (4)–(7) can be made uniform if \(m_0,m_1,\|M_x\|_{L^\infty L^2},\|B\|_{L^2}\), \(\sum_j\|S_j\|_{\mathcal A}^2\), \(\sum_j\gamma_j^2\), and \(\max_j\mu_j\) have uniform bounds (with fixed \(L,T,\kappa\)). The subsequent source estimates are uniform for amplitudes bounded in \(\ell^2\mathcal A\); uniform little-o additionally requires a **uniform smooth approximation modulus** for the family. Without these conditions no such claim is possible: in the abstract comparison problem \(M=1,B=0,S_j=1,\gamma_j=0,\mu_j=1\), initial data \(h_j=\phi_m/\sqrt N\) create a source \(\sqrt N e^{-t}\phi_m\), so its endpoint response grows like \(\sqrt N\). This example is not the physical model.

### 1.2 Exact source, corrector and memory history

Subtract \(e^{-\mu_jt}\phi_m\) from branch \(j\). More generally use auxiliary amplitudes \(f_j\in\mathcal A\) with *fixed feedback coefficients* \(S_j\):
\[
MY_t-\kappa Y_{xx}=BY+\sum_jS_jp_j+\phi_m F_a,\quad p_{j,t}+\mu_jp_j=\gamma_jY,\quad Y(0)=p_j(0)=0,\quad F_a=\sum_je^{-\mu_jt}f_j. \tag{8}
\]
The original branch input corresponds to \(f_j=S_j\) and all other amplitudes zero. Take
\[
A_m={c_LF_a\sin(q_mx)\over\kappa q_m^2},\quad
C_m={2c_L\over\kappa q_m^3}\bigl[F_{a,x}\cos(q_mx)-\ell_m(t,x)\bigr], \tag{9}
\]
where \(\ell_m\) is the affine interpolation of the endpoint values
\(\ell_m(t,0)=F_{a,x}(t,0)\), \(\ell_m(t,L)=(-1)^mF_{a,x}(t,L)\). This is well-defined for smooth amplitudes, makes \(C_m\) Dirichlet at both ends, and does not require \(F_a\) to be even.

Set \(D=MF_{a,t}-BF_a-\kappa F_{a,xx}\), \(H=F_{a,x}\cos(q_mx)-\ell_m\). The full corrected parabolic residual is
\[
\begin{aligned}
\mathcal R_m={c_L\over\kappa q_m^2}[D\sin(q_mx)-2\kappa q_mF_{a,x}\cos(q_mx)]
+{2c_L\over\kappa q_m^3}[MH_t-BH-\kappa H_{xx}],\\
H_{xx}=F_{a,xxx}\cos(q_mx)-2q_mF_{a,xx}\sin(q_mx)-q_m^2F_{a,x}\cos(q_mx),\qquad \ell_{m,xx}=0. \tag{10}
\end{aligned}
\]
The \(q_m^{-1}\) cosine terms cancel exactly. The other terms have norm \(O_f(q_m^{-2})\); only the auxiliary amplitudes are differentiated. For \(e=Y-A_m-C_m\), initial data are \(e(0)=-(A_m+C_m)(0)\), \(p_j(0)=0\), and the forcing pair is \((-\mathcal R_m,\gamma_j(A_m+C_m))\). Its \(L^2\) size and initial \(L^2\) mismatch are \(O_f(q_m^{-2})\). Equation (7) gives \(\|e\|_{L^\infty L^2\cap L^2H^1}=O_f(q_m^{-2})\). For each \(j\),
\[
p_j(t)=\gamma_j\int_0^te^{-\mu_j(t-s)}[e+A_m+C_m](s)ds, \tag{11}
\]
so the \(\ell^2L^2(Q)\) norm of \(p\) is \(O_f(q_m^{-2})\). A fixed \(\chi=0\) near zero and \(\chi=1\) on \(J\) yields cutoff sources \(-\chi\mathcal R_m+M\chi'e\) and \(\gamma_j\chi(A_m+C_m)+\chi'p_j\). They remain \(O_f(q_m^{-2})\) in the forcing space of (5). Consequently \(\|e\|_{L^2(J;H^2)}=O_f(q_m^{-2})\). The derivatives of \(C_m\) at both endpoints are \(O_f(q_m^{-3})\). Hence (3) holds with \(O_f(q_m^{-2})\) for smooth amplitudes.

For rough amplitudes, the uncorrected trial \(A_m\) has residual \(O(q_m^{-1})\) in \(L^2\) and \(O(q_m^{-2})\) in \(L^2V'\), using \(\|a\cos(q_mx)\|_{V'}\le Cq_m^{-1}\|a\|_{H^1}\). The initial mismatches and \(\gamma_j A_m\) are included. Equations (5) and (7), plus the multiplicative trace inequality at **both** endpoints, yield the uniform-in-\(m\) source approximation estimate
\[
q_m^{3/2}\|\mathbf r_m(f)-\mathbf r_m(g)\|_{L^2(J;\mathbb R^2)}\le C_N\|(f_j-g_j)\|_{\ell^2\mathcal A}. \tag{12}
\]
Smooth functions are dense in \(\mathcal A\) by simultaneous spatial/time extension and mollification, without any endpoint condition. Fix the approximant, let \(m\to\infty\), then let approximation error tend to zero. This proves (3). For \(N=1\), the method requires only (1) and general oddness is unnecessary; the thermoviscoelastic structure supplies these generic hypotheses but is not used by (9)–(12).

## 2. Sensors and cancellation

For \(N=1\), let \(a_0=c_Le^{-\mu t}S(t,0)\), \(a_L=c_Le^{-\mu t}S(t,L)\). The physical vector of powers multiplies (3) by \(A_0\). Channel-by-channel,
\[
\begin{array}{c|c}
\text{observation (outward powers divided by area)}&\text{leading coefficient of }q_m^{-1}\\\hline
\text{left}&a_0\\
\text{right}&-(-1)^m a_L\\
\text{sum}&a_0-(-1)^m a_L\\
\text{difference}&a_0+(-1)^m a_L\\
\text{vector}&(a_0,-(-1)^m a_L)
\end{array} \tag{13}
\]
All have little-o remainders by bounded linearity. For the odd thermoviscoelastic sector, \(q_n=2\pi n/L\), \(S(t,L)=S(t,0)\), and the leading vector is \((a_0,-a_0)/q_n\); the sum vanishes identically by parity for the entire *linear* odd solution, not just its leading term. The difference has \(2a_0/q_n\). Nonlinear even corrections need not vanish.

Without reflection symmetry, **consecutive** integer modes have alternating second-endpoint profiles; one cannot cancel both channels by the same adjacent-mode combination. Instead \(\phi_m-(q_{m+2}/q_m)\phi_{m+2}\) cancels both leading components exactly, since \((-1)^{m+2}=(-1)^m\). For a fixed finite set of endpoint traces, or any fixed bounded linear operator on their two trace functions, the result follows by composition. In one spatial dimension there are only two geometrically distinct boundary points; interior point sensors and unbounded time differentiators are **not** covered. For the actual odd experiment, the full linearized force channel vanishes and the two fluxes are opposite; the full nonlinear three-output estimate additionally uses the previously verified quadratic remainder.

## 3. Quantitative rate from explicitly stronger regularity

A quantitative condition can be expressed without pretending that \(\mathcal A\) alone has an approximation rate. In the one-branch problem assume in addition
\[
S\in H^{2+\eta}(Q),\qquad 0<\eta\le1, \tag{14}
\]
where \(H^{s}(Q)\) is the isotropic Sobolev space in the two variables on the rectangle. This is stronger than \(\mathcal A\), including extra **time** regularity; it is not derived for the actual base.

A bounded extension for \(H^s(Q)\), \(2\le s\le3\), followed by a standard two-variable mollifier gives smooth \(f_\varepsilon\) with
\[
\|S-f_\varepsilon\|_\mathcal A\le C\varepsilon^\eta\|S\|_{H^{2+\eta}(Q)},\qquad
\|f_\varepsilon\|_{H^3(Q)}\le C\varepsilon^{-(1-\eta)}\|S\|_{H^{2+\eta}(Q)},\quad 0<\varepsilon\le1. \tag{15}
\]
For the odd physical sector, average approximants with reflection; the same estimates remain valid. The smooth-corrector constant has the explicit bound
\[
\|\mathbf r_m(f)\|_{L^2(J;\mathbb R^2)}\le C_{\delta,M,B,S,\mu,\gamma}\,q_m^{-2}\|f\|_{H^3(Q)}. \tag{16}
\]
Indeed (10) requires \(f_{xxx},f_{xt}\in L^2\), \(f_x\in L^\infty\), and endpoint traces of \(f_{xt}\) controlled by \(\|f_{xt}\|_{L^2_tH^1_x}\). Initial \(f,f_x\) in \(L^2_x\) are controlled by the \(H^3\) time trace. The \(B H\) term uses the two-dimensional embedding \(H^3(Q)\hookrightarrow W^{1,\infty}(Q)\); no derivative of \(B\) or \(M\) is used. These bounds also cover the affine endpoint interpolant. Combining (12), (15), (16) and choosing \(\varepsilon=q_m^{-1/2}\) for large \(m\) yields
\[
\boxed{\|\mathbf r_m(S)\|\le C q_m^{-3/2-\eta/2}\|S\|_{H^{2+\eta}(Q)}.} \tag{17}
\]
For \(\eta=1\) this gives \(O(q_m^{-2})\). Constants depend on the fixed actual feedback coefficients and delay; no assertion is made that (14) follows from (1) or is realized by the experiment. This is a sufficient regularity tradeoff, not a sharp rate or leading coefficient.

No universal algebraic approximation rate follows from a bare \(\mathcal A\)-norm bound: choose time-independent spatial oscillations \(S_K(x)=K^{-2}\cos(K\pi x/L)\), with \(K\) even for reflection symmetry. Their \(\mathcal A\)-norms stay bounded, while their \(H^2\) energy concentrates at frequency \(K\); any smoothing at scale \(\varepsilon\) loses an order-one part when \(K\varepsilon\) is large. Thus no uniform power of \(\varepsilon\) holds on the entire \(\mathcal A\) unit ball. This statement concerns approximation, not a constructed lower bound on physical PDE remainders.

## 4. Identifiability and operator consequences

For each fixed branch and same-parity mode pairs, (3) produces approximate invisibility and excludes certain full-state Hölder estimates; it gives no nonzero \(h\in\ker\mathcal T\) and no proof that \(\overline{\operatorname{ran}\mathcal T^*}\) is all of the input space. A compact injective diagonal operator and the same operator with one diagonal entry set to zero can share identical high-frequency tail estimates. Those are abstract illustrations, not physical examples. Conversely, finite-truncation rank, a positive column norm, or the decay rate (17) cannot establish the infinite moment synthesis is injective. Actual exact kernel, adjoint density, optimality and strong \(\mathcal S_{2/3}\) remain open.

The fixed \(N\) leading operator for unrestricted input has rank at most \(2N\): each branch has left and right endpoint functionals with sine coefficients \(1/q_m\) and \((-1)^m/q_m\). The remainders satisfy column little-o, so the dyadic-block approximation proof gives \(s_n=o(n^{-3/2})\) after an \(N\)-dependent index shift. This does not produce a uniform-in-\(N\) singular-value statement or a lower bound.
