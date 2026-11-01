# Exact prior art and overlap audit

**Assessment:** exact overlap is unresolved, not absent. The strongest candidate for subsuming the singular-value conclusion is Volkov's kernel theorem; the strongest directly located delayed-boundary source comparison is Li–Li–Zhou. Neither has been shown to imply the full model theorem. The fixed-finite-memory and stronger-regularity calculations in the companion report are consistent generalizations of the same mechanism, not established novelty. Search was targeted, not exhaustive. No claim of priority follows.

This is Arena's mathematical/literature investigation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. Direction 1 remains **REJECTED AS A NEW FOUNDATIONAL CONTINUUM THEORY**; Direction 2 is an observation-and-state question, not a new continuum theory.

## 1. Actual equations and hypothesis reconciliation

Let \(I=(0,L)\), \(T=10/\lambda\), \(0<\delta<T\), \(J=(\delta,T)\). With \(a,k,\lambda,c,\kappa,\theta_*,L>0\), \(b,g_*\ne0\), the frozen experiment is
\[
\sigma_x=0,\quad \sigma=(a+k)u_x-b(\theta-\theta_*)-kz,\quad z_t=\lambda(u_x-z),\quad
c\theta_t=\kappa\theta_{xx}-b\theta(u_x)_t+k\lambda(u_x-z)^2, \tag{1}
\]
\(u(0,t)=0\), \(u(L,t)=g_*\sin^2(\pi t/T)\), \(\theta(0,t)=\theta(L,t)=\theta_*\), \(\theta(x,0)=\theta_*\), and \(z(x,0)=h(x)\). No other input, corner condition, or manufactured coefficient is substituted.

Put \(D=a+k,r=k/D,\alpha=a/D,\beta=b/D,d=b^2/D,\gamma=\lambda\beta,\mu=\lambda\alpha,m=g/L\), \(y=\theta-\theta_*\), \(p=Qz\), \(v=\langle z\rangle\), \(Q=I-\langle\cdot\rangle\), \(w=u_x-z\), and \(E=m'+rp_t\). Equilibrium exactly yields
\[
\sigma=Dm-b\langle y\rangle-kv,\quad u_x=m+rp+\beta Qy,\quad w=m-v-\alpha p+\beta Qy,
\quad v_t=\lambda(m-v),\quad p_t=-\mu p+\gamma Qy, \tag{2}
\]
\[
(cI+d\theta Q)y_t=\kappa y_{xx}-b\theta E+k\lambda w^2. \tag{3}
\]
The base has **initial** memory \(h=0\), not \(z=0\) for all times: the nonzero load creates \(z_b\). \(y\in\mathcal E=H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_0)\) with \(y(0)=0\), and \(p\) follows (2). Spatial Dirichlet conditions on temperature hold for all time; the ODE memory is not given artificial endpoint conditions. The actual \(H^2\) initial neighborhood need not vanish at endpoints.

A nonempty sufficient small-load condition is explicit. In one fixed consistent unit system, define \(K=\sqrt L\), \(H=L/\pi\), \(S_L=\sqrt{L^{-1}+L}\), \(C_*=c+d\theta_*\), \(b_0=b\theta_*r\mu\), \(c_0=b\theta_*r\gamma\),
\[
\begin{gathered}
K_0=\max\{3|b_0|^2/c+|\gamma|H,(3|c_0|^2H^2/c+|\gamma|H)/\kappa\},\quad
J_0=e^{K_0T/2}\max\{1,\sqrt{3/c}\},\\
U=\sqrt{(1+3/c+K_0TJ_0^2)/c},\quad
C_L=U+\frac{C_*U+1+(|b_0|\sqrt T+|c_0|H\sqrt{T/\kappa})J_0}{\kappa}+\sqrt{(1+H^2)/\kappa}J_0,\\
A_s=\pi/T+2r\mu S_L,\quad A_R=2r|\gamma|(1+\mu T)K,\quad W_s=2+(1+2\alpha)S_L,\quad W_R=2|\beta|(1+\alpha\lambda T)K,\\
C_N=dK+|b|K\sqrt{LT}\max(A_s,A_R)+k\lambda\sqrt{LT}\max(W_s,W_R)^2,\\
C'_N=2dK+|b|K\sqrt{LT}(A_s+2A_R)+2k\lambda\sqrt{LT}W_R(W_s+W_R),\\
C_B=C_L(|b|\theta_*\pi\sqrt{LT}/T+2\sqrt L S_L),\\
s_* =\min\{C_B/[2C_LC_N(1+2C_B)^2],\;1/[4C_LC'_N(1+2C_B)],\;\theta_*/(8KC_B)\}. \tag{4}
\end{gathered}
\]
All denominators are positive; \(s_*>0\), so \(0<|g_*|/L<s_*/2\) is a nonempty symbolic regime. It is not a measured physical range, and dimensional consistency requires one fixed unit system or prior nondimensionalization. The explicit contraction and full positive-class uniqueness are detailed in `direction-2-active-base-existence-and-regularity.md`, §§2–3, with dependencies in the formulation-A existence investigation and independent audit. They yield a unique positive weak-initial base, \(3\theta_*/4\le\theta_b\le5\theta_*/4\), and a genuine open \(H^2\) neighborhood for the nonlinear map. Full-class uniqueness is an inherited argument, not a consequence of the contraction alone.

## 2. Complete candidate theorem, not a priority claim

For that actual base put
\[
M=c+d\theta_b,\quad B=-dQy_{b,t}-bE_b-br\gamma\theta_b+2k\gamma w_b,\quad S=\lambda\alpha[br\theta_b-2kw_b]. \tag{5}
\]
Reflection symmetry and uniqueness make them even. The base supplies
\[
M\in L^\infty(Q),\quad M\ge c+3d\theta_*/4>0,\quad M_x\in L^\infty_tL^2_x,\quad B\in L^2(Q),\quad S\in\mathcal A:=H^1_tL^2_x\cap L^2_tH^2_x\hookrightarrow C_tH^1_x. \tag{6}
\]
For an odd initial perturbation \(h\in L^2_o(I)\), the odd derivative \((Y,P)\) satisfies
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad Y(0)=0,\ P(0)=h,\quad Y|_{\partial I}=0. \tag{7}
\]
In particular \(Y(\cdot,0)=0\) is not a spatial condition on \(P\); \(Y(0,t)=Y(L,t)=0\) are the bath conditions. The full memory history \(P=e^{-\mu t}h+\gamma\int_0^te^{-\mu(t-s)}Y(s)ds\) is retained. The actual observation is the **delayed outward flux difference**, \(\mathcal T h=2A_0\kappa Y_x(t,0)|_J\), for positive cross-sectional area \(A_0\); it is bounded \(L^2_o\to L^2(J)\) by the strong forced estimate. It is not the nonlinear map, nor the two-flux vector.

Let \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), an orthonormal basis of \(L^2_o(I)\), and \(a(t)=2A_0\sqrt{2/L}e^{-\mu t}S(t,0)\). Then
\[
\mathcal T\phi_n={a\over q_n}+\rho_n,\quad \|\rho_n\|_{L^2(J)}=o(q_n^{-3/2}),\qquad s_n(\mathcal T)=o(n^{-3/2}). \tag{8}
\]
The rank-one part is bounded since \((q_n^{-1})\in\ell^2\). The remainder columns alone imply the singular-value result via Hilbert–Schmidt dyadic tail bounds and finite-rank approximation. Neither \(a\ne0\) nor an asymptotic equivalence is asserted. Equation (8) implies \(\mathcal T\in\mathcal S_p\) for every \(p>2/3\), but not necessarily \(\mathcal S_{2/3}\). The diagonal sequence \(n^{-3/2}/\log(n+1)\) illustrates the endpoint failure of that implication abstractly.

For any fixed positive \(H^2\)-prior radius and local comparison about zero, same-parity adjacent columns cancel the rank-one part. Choosing \(h_n\propto q_n^{-2}(\phi_n-(q_{n+1}/q_n)\phi_{n+1})\) gives \(\|h_n\|_{H^2}=O(1)\), \(\|h_n\|_{L^2}\asymp q_n^{-2}\), \(\|\mathcal T h_n\|=o(q_n^{-7/2})\). Hence no uniform \(\|h\|_2\le C\|\mathcal T h\|^\xi\) on that ball for \(\xi\ge4/7\), including the endpoint. This is a linearized full-state assertion; it neither proves a kernel nor a lower bound.

Let \(\mathcal F(h)\) be the actual **nonlinear full output**: reaction force and both labeled outward heat powers on \(J\). Its derivative on odd \(h\) has zero force and opposite powers; the nonlinear map is \(C^2\) from a smaller actual \(H^2\) neighborhood, with \(O(\|h\|_{H^2}^2)\) full-output remainder. Write \(z_n=\phi_n-(q_{n+1}/q_n)\phi_{n+1}\) and \(\|\mathcal Tz_n\|=q_n^{-3/2}\varepsilon_n\), where \(\varepsilon_n\to0\). Set \(a_n=\max(\varepsilon_n,q_n^{-1})\) and \(h_n=a_nq_n^{-11/2}z_n\). Then \(\|h_n\|_2\asymp a_nq_n^{-11/2}\) and the full output is \(O(a_n^2q_n^{-7})\). Since \(a_n\to0\), the endpoint ratio diverges; this excludes \(\xi\ge11/14\), including the endpoint. The different threshold reflects the quadratic cost. It does **not** establish nonlinear \(4/7\), injectivity, optimality, or physical applicability beyond (4). The critical-audit report provides the cutoff, density and trace proof; the companion report extends it to non-even endpoints and fixed finite branches.

## 3. Targeted primary-source comparison

Access labels mean the cited statements and named proof passages were actually inspected where indicated, not that every paper was exhaustively audited. Citations below are direct primary texts, except where explicitly labeled metadata only. Negative comparisons apply to inspected statements, not the whole literature.

| Source, location, access | Unknown / spaces / geometry | Actual overlap; exact obstacle to subsumption |
|---|---|---|
| Volkov, [Optimal decay rates](https://arxiv.org/html/2309.00153), Theorem 1.1, §4 proof, Appendix A.1: **FULL TEXT AND RELEVANT PROOF INSPECTED** | integral operator from \(L^2(\Omega)\) to \(L^2(\Omega')\); kernel \(L^2(\Omega';H^p(\Omega))\); bounded domain, \(d=1,p=1\) here | Gives \(\sum n^2s_n^2<\infty\), hence \(o(n^{-3/2})\). Strongest located candidate for *that conclusion*. To map it, remove the actual rank-one leading operator and prove its remainder kernel has a source-variable \(H^1\) derivative in \(L^2\). Our column little-o does not prove this; no such kernel regularity was established. Does not furnish the leading term, active-base existence, or nonlinear obstruction. |
| Delgado–Ruzhansky, [Schatten-von Neumann classes](https://arxiv.org/html/1709.06446), Theorem 2.2 and proof (2.4): **FULL TEXT AND RELEVANT PROOF INSPECTED** | general measure-space integral kernels; weighted source/target derivative operators with Schatten inverses | Direct predecessor of Volkov. Uses a Hilbert–Schmidt differentiated kernel and factorization. The missing differentiated-kernel hypothesis is not supplied by our proof. Gives substantial generic prior art, but no model-specific flux decomposition. |
| Birman–Solomyak, *Estimates of singular numbers of integral operators*, Russian Math. Surveys 32(1), 1977, cited by Volkov Appendix A.1: **EXACT OVERLAP UNRESOLVED** | original paper's precise hypotheses and proof not accessed | Direct predecessor; no assertion about exact theorem strength, endpoints or ability to subsume this PDE. |
| Li–Li–Zhou, [Inverse Heat Source Problems](https://arxiv.org/html/2609.10071), Theorem 1.3, §§3, 5, Lemmas 5.1–5.2: **FULL TEXT AND RELEVANT PROOF INSPECTED** | scalar heat, separated \(f(x)g(t)\), delayed boundary flux, spectral regularity and sector-holomorphic \(g\), specified geometry | Strong delayed-source comparison; proves conditional stability using analyticity and retains source history. Actual \(S(t,x)\), nonautonomous \(M,B\), and feedback \(SP\) are not known to be separable or time analytic. No matching column theorem found in inspected passages. |
| Jha–George, [parabolic equation with memory](https://arxiv.org/html/2506.22221v2), Assumptions 3.9, 3.11–3.12, Theorem 3.10: **THEOREM STATEMENT INSPECTED, PROOF NOT FULLY ACCESSIBLE** | coupled PDE–ODE adjoint and moving interior observations; specified regularity, assumed unique continuation and compactness–uniqueness | Memory and observability are directly related, but not the initial distributed memory with delayed endpoint-flux output and above mass/corrector. Its assumed UC cannot be silently imported. |
| Apraiz–Lecaros–Zamorano, [Kelvin–Voigt inverse problem](https://arxiv.org/html/2610.26157v1), §1.2, Theorem 2.3 proof: **FULL TEXT AND RELEVANT PROOF INSPECTED** | heat/ODE factorization, interior observation plus positive-time snapshot and weighted estimates | Related coupled nondiffusive component. Different unknown and observations; does not prove (8) in inspected proof. |
| Benabdallah et al., [two reaction-diffusion equations](https://arxiv.org/html/math/0603484), §2 and §4, Lemma 4.2 and Theorem 4.3: **FULL TEXT AND RELEVANT PROOF INSPECTED** | two *diffusive* components; interior data and snapshot, coefficient assumptions, \(H^4\) initial priors in Lemma 4.2 | Initial-state stability and coupled inverse problem are close; its logarithmic-convexity step uses a two-component elliptic diagonal generator. Our second component is a nondiffusive ODE and the observation is different. |
| Halanay–Pandolfi, [boundary control of diffusion with memory](https://arxiv.org/html/1404.2745), §1.1 and Theorems 2–3: **THEOREM STATEMENT INSPECTED, PROOF NOT FULLY ACCESSIBLE** | scalar Coleman–Gurtin memory and boundary control | Memory kernel and control precedents including finite exponentials; not identified as theorem about arbitrary initial distributed ODE memory and our delayed flux. |
| Choulli, [parabolic inverse problem](https://arxiv.org/html/1512.07421), Theorem 3.1: **THEOREM STATEMENT INSPECTED, PROOF NOT FULLY ACCESSIBLE** | scalar one-dimensional heat initial-data recovery, interior point time trace and \(H^2\) prior | State reconstruction is related; scalar initial heat state and observation differ. This access label records our limited proof inspection, not a claim the document itself is paywalled. |
| Koch–Rüland–Salo, [instability mechanisms](https://arxiv.org/html/2012.01855), Appendix A.4, Propositions A.4, A.6, A.8: **FULL TEXT AND RELEVANT PROOF INSPECTED** | compact Hilbert-scale operators; singular values and basis-dependent instability | General inverse instability framework and endpoint subtleties; matching its basis, prior and exact quantitative hypotheses to (7) is not automatic. It does not itself supply the PDE columns. |
| Montalto–Stefanov, [stability of nonlinear inverse problems](https://arxiv.org/html/1306.1978), Theorem A.1 and proof: **FULL TEXT AND RELEVANT PROOF INSPECTED** | nonlinear map, order-\(>1\) remainder and assumed linear conditional stability on interpolation scales | Transfers stability under hypotheses; not a proof of our nonlinear instability threshold. Our Taylor quadratic remainder and rescaled sequence are separate. |
| Hào–Oanh, [boundary observations](https://doi.org/10.1515/jiip-2015-0055), 2016: **ABSTRACT OR METADATA ONLY** | abstract identifies parabolic initial-condition recovery from boundary observations, variational adjoint, FD and singular values; detailed spaces, geometry, theorem not inspected | Directly relevant prior art; whether any theorem or calculation subsumes (8) is **EXACT OVERLAP UNRESOLVED**. Do not infer its hypotheses or conclusions from the abstract. Their later [integral-observations paper](https://www.tandfonline.com/doi/pdf/10.1080/17415977.2016.1229778) explicitly cites it as a predecessor, but inspected search excerpts concern scalar time-dependent parabolic integral measurements rather than our memory system. |

The only accessible source named above for which the kernel hypotheses are a candidate to subsume the *singular-value result* is Volkov, not a demonstrated subsuming theorem for the full package. In fact column decay alone cannot fill that gap: on an interval, take orthonormal Dirichlet sines \(e_n\), orthonormal output functions \(v_n\), and kernel \(K(t,x)=\sum_{n\ge2}d_nv_n(t)e_n(x)\), \(d_n=n^{-3/2}/\sqrt{\log n}\). It is Hilbert–Schmidt and its columns are \(o(n^{-3/2})\), yet \(\sum n^2d_n^2=\infty\); its distributional spatial derivative is not in \(L^2\). This is an abstract counterexample to a hypothesis implication, **not** a claim about the physical kernel. A separate PDE regularity proof could still establish Volkov's assumption for the actual remainder.

## 4. Exact kernel, range and history: still open

For the actual map \(\mathcal T\), \(\ker\mathcal T=(\operatorname{ran}\mathcal T^*)^\perp\); injectivity is equivalent to density of the actual adjoint range, not to its being closed. The adjoint must be constructed by justified boundary transposition for the nonautonomous coupled system; a formal Riesz adjoint alone does not establish PDE boundary regularity or range density. A delayed zero trace neither makes \(P(\delta)=0\) nor turns the reachable state at \(\delta\) into arbitrary independent data. Two legitimate paths remain: prove completeness of the actual adjoint range on the reachable graph including pre-delay history, or construct a physically admissible nonzero initial memory whose exact infinite time trace vanishes. Neither was completed. No physical invisible state is inferred.

Writing \(k_n=\mathcal T\phi_n\), zero synthesis \(\sum h_nk_n=0\) for \(h\in\ell^2\) is the kernel question. Completeness of \(\{k_n\}\) in the **output** is a different question from injectivity of that synthesis. Compactness, the rank-one leading term, individually nonzero columns and finite matrix rank do not decide either exact question. The pre-delay map can be Fredholm without making the observation operator Fredholm. Numerical protocols and required supplied active-base inputs are in `direction-2-publication-readiness-decision.md` and the moment package; discretization, coefficient error, observation truncation and roundoff must be separated.
