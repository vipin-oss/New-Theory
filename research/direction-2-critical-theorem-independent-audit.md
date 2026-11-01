# Adversarial audit of the critical high-frequency theorem

## 1. Verdict and scope

The critical little-o proof in §§3–5 of `direction-2-critical-high-frequency-asymptotic-investigation.md` is **correct under its stated coefficient and strong-solution hypotheses**; no erroneous sign, illicit boundary trace, or missing memory term was found. The companion `direction-2-active-base-existence-and-regularity.md` supplies a nonempty explicit small-load regime in which those hypotheses hold for the prescribed active base, using the earlier explicit fixed-point theorem and a new odd forced estimate. This does not verify an unknown actual amplitude against the threshold, prove large-data existence, or prove novelty.

The audit is by Arena in the same research environment; it is not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder. All prior reports remain unchanged.

| Step audited | Classification | Qualification |
|---|---|---|
| Exact trial, ODE residual and neighboring cancellation | PROVED CORRECTLY | §2, including initial mismatch and the exact \((n+1)/n\). |
| Weak \(V'\) energy | CORRECT ONLY UNDER AN ADDITIONAL EXPLICIT ASSUMPTION | A priori for already existing strong solutions, \(M^{-1}\in L^\infty_tH^1_x\), \(S/M\in L^\infty_tH^1_x\), \(B\in L^2\); these are consequences of the previous report's displayed assumptions, not a new restriction on its theorem. |
| Smooth corrected residual | PROVED CORRECTLY | Exact expansion (6) includes every derivative of the trial; none falls on actual \(M,B,S\). |
| Memory and time cutoff | CORRECT ONLY UNDER AN ADDITIONAL EXPLICIT ASSUMPTION | The cutoff pair must be admitted to the strong forced problem with its actual pre-delay history, as assumed and supplied by companion §4. |
| Approximation and order of limits | PROVED CORRECTLY | \(\mathcal A\hookrightarrow C_tH^1\); parity-preserving density with no spatial endpoint condition, §5. |
| Singular-value deduction | PROVED CORRECTLY | Explicit dyadic rank/tail allocation, §6; strong Schatten endpoint does not follow. |
| Exclusion of \(4/7\) for linearized full state | PROVED CORRECTLY | For the specified odd flux-difference observation and fixed \(H^2\) ball; not a kernel or nonlinear injectivity assertion. |
| Nonlinear \(11/14\) scaling | CORRECT ONLY UNDER AN ADDITIONAL EXPLICIT ASSUMPTION | Requires an actual neighborhood and quadratic full-output remainder; companion §6 supplies these in its small-data weak-initial regime. |
| Physical parameter verification / global solution | INCOMPLETE | No measured constants or amplitude supplied; small-data regime is sufficient, not shown for the unspecified experiment. |
| Historical novelty | INCOMPLETE | Exact overlap not excluded; §8 and publication decision. |

## 2. Exact algebra and neighbor residual

Let \(q=2\pi n/L\), \(c_L=\sqrt{2/L}\), \(\phi=c_L\sin(qx)\). For \(f\in\mathcal A\) and fixed actual \(M,B,S\), solve
\[
MY_t-\kappa Y_{xx}=BY+Sp+e^{-\mu t}f\phi,\quad p_t+\mu p=\gamma Y,\quad Y(0)=p(0)=0. \tag{1}
\]
This is linear in \(f\); for \(f=S\), \(p=P-e^{-\mu t}\phi\) and the original initial memory is recovered. Put \(A=e^{-\mu t}f\phi/(\kappa q^2)\). Define \(D_f=M(f_t-\mu f)-Bf-\kappa f_{xx}\). Direct differentiation gives
\[
\mathcal R_A:=MA_t-\kappa A_{xx}-BA-e^{-\mu t}f\phi
={c_Le^{-\mu t}\over\kappa q^2}[D_f\sin(qx)-2\kappa q f_x\cos(qx)]. \tag{2}
\]
For the actual pair \((A,e^{-\mu t}\phi)\), the ODE residual is \(-\gamma A\), not zero. The error is initialized by \(Y-A=-A(0)\), \(P-e^{-\mu t}\phi=0\), and receives forcing \((-\mathcal R_A,\gamma A)\). Its initial \(L^2\) and \(H^1\) sizes are \(O(q^{-2})\), \(O(q^{-1})\).

For \(q_+=q_{n+1}\), \(Q_n=q_+/q=(n+1)/n\), the exact neighboring residual is
\[
{c_Le^{-\mu t}\over\kappa}\left\{D_S\left({\sin qx\over q^2}-{Q_n\sin q_+x\over q_+^2}\right)
-2\kappa S_x\left({\cos qx\over q}-{Q_n\cos q_+x\over q_+}\right)\right\}. \tag{3}
\]
The latter coefficient is \(-2\kappa S_x[\cos qx-\cos q_+x]/q\), not a small interior difference just because \(Q_n\to1\). The exact trial boundary flux cancels because \(Q_n/q_+=1/q\); the initial error is \(-A_n(0)+Q_nA_{n+1}(0)\), and memory forcing is \(\gamma(A_n-Q_nA_{n+1})\).

## 3. Weak energy and critical uniform estimate

Let \(V=H^1_0\cap L^2_o\), \(V'\) its dual. Assume \(M,M^{-1}\in L^\infty\), \(M_x\in L^\infty_tL^2_x\), \(S\in L^\infty_tH^1_x\), \(B\in L^2_{t,x}\), all even, and the strong solution of
\(My_t-\kappa y_{xx}=By+Sp+F\), \(p_t+\mu p=\gamma y+G\). Division by \(M\) is legitimate in \(L^2\). \(a=\kappa/M\) has \(a_x\in L^\infty_tL^2_x\); multiplication by \(1/M\) and \(S/M\) preserves \(V\) because \(H^1(I)\) is an algebra, preserves oddness, and preserves zero trace. Thus their dual multipliers are well-defined on \(V'\).

Testing the divided equation by \(y\) and the ODE by \(( -\partial_{xx}|_V)^{-1}p\) gives, using one-dimensional Gagliardo–Nirenberg and Young,
\[
\begin{aligned}
|\int a_x y_xy|&\le\epsilon\|y_x\|_2^2+C_\epsilon\|a_x\|_2^4\|y\|_2^2,\\
|\int (B/M)y^2|&\le\epsilon\|y_x\|_2^2+C_\epsilon\|B/M\|_2^{4/3}\|y\|_2^2,\\
|\langle p,(S/M)y\rangle|&\le\epsilon\|y_x\|_2^2+C_\epsilon\|S/M\|_{H^1}^2\|p\|_{V'}^2,\\
|\langle F/M,y\rangle|&\le\epsilon\|y_x\|_2^2+C_\epsilon\|F\|_{V'}^2.
\end{aligned}\tag{4}
\]
The second line follows from \(\|y\|_4^2\le C\|y\|_2^{3/2}\|y_x\|_2^{1/2}\), and \(\|B(t)\|_2^{4/3}\in L^1(0,T)\). For the ODE use the Hilbert chain rule in \(V'\), valid since \(p\in H^1_tL^2\), to get \(d\|p\|_{V'}^2/dt\le C(\|p\|_{V'}^2+\|y\|_2^2+\|G\|_{V'}^2)\). Gronwall gives the earlier estimate (12). No derivative of \(M\) in time occurs. This is an a priori bound on strong solutions, not a construction with arbitrary \(V'\) sources.

For \(h\in H^1\), \(\|h\cos(qx)\|_{V'}\le Cq^{-1}\|h\|_{H^1}\): integrate by parts using \(v\in V\), so the boundary term vanishes. Applying it to (2) and the embedding \(\mathcal A\hookrightarrow C_tH^1_x\) gives \(\|\mathcal R_A\|_{L^2V'}\le Cq^{-2}\|f\|_\mathcal A\), \(\|\mathcal R_A\|_2\le Cq^{-1}\|f\|_\mathcal A\). The weak estimate and companion (17) give
\[
\|Y-A\|_{L^2H^1}\le Cq^{-2}\|f\|_\mathcal A,\quad
\|Y-A\|_{L^2H^2}\le Cq^{-1}\|f\|_\mathcal A. \tag{5}
\]
The constant depends on the actual fixed base, never on \(n\) or \(f\). For \(v\in H^1\), \(|v(0)|^2\le L^{-1}\|v\|_2^2+2\|v\|_2\|v_x\|_2\). Applying it to \((Y-A)_x\) and integrating yields the uniform \(q^{3/2}\|\rho_n(f)-\rho_n(g)\|_Z\le C\|f-g\|_\mathcal A\). This is a multiplicative estimate on \(H^2\) functions, not a false bounded derivative trace on \(H^{3/2}\).

## 4. Complete corrector, initial mismatch and delay

Let smooth \(f\) be even, \(\ell=1-2x/L\), \(H=f_x\cos(qx)-f_x(t,0)\ell\), and
\(C=2c_Le^{-\mu t}H/(\kappa q^3)\). Its two boundary values vanish because \(f_x(L)=-f_x(0)\); it is odd. The **complete** corrected first residual is
\[
\begin{aligned}
\mathcal R_{A+C}={c_Le^{-\mu t}\over\kappa q^2}
&[D_f\sin(qx)-2\kappa q f_x\cos(qx)]\\
+{2c_Le^{-\mu t}\over\kappa q^3}\{&M[(f_{xt}-\mu f_x)\cos(qx)-(f_{xt}(t,0)-\mu f_x(t,0))\ell]\\
&-BH-\kappa[f_{xxx}\cos(qx)-2q f_{xx}\sin(qx)-q^2f_x\cos(qx)]\}. \tag{6}
\end{aligned}
\]
The last \(+2c_Le^{-\mu t}f_x\cos/q\) cancels the first line's \(-2c_Le^{-\mu t}f_x\cos/q\). The remaining \(D_f\), \(BH\), \(M H_t\), \(f_{xxx}\), \(q f_{xx}\) and \(\ell\) terms have \(L^2\) norm \(\le C_fq^{-2}\); \(B\) is merely \(L^2\), and no derivative of \(M,B,S\) occurs. The notation \(H_t\) here is only a mnemonic for the explicitly displayed smooth \(f\) terms; the exponential was already differentiated.

With \(e=Y-A-C\), \(p\) as in (1), forcing is \((-\mathcal R_{A+C},\gamma(A+C))\), and initial data are \((-(A+C)(0),0)\). The weak estimate gives \(\|e\|_{L^\infty L^2}+\|e\|_{L^2H^1}=O_f(q^{-2})\). Since
\[
p(t)=\gamma\int_0^te^{-\mu(t-s)}[e+A+C](s)ds, \tag{7}
\]
\(\|p\|_{L^2_{t,x}}=O_f(q^{-2})\), using the entire history. A fixed \(\chi\) vanishing near zero and equal to one on \([\delta,T]\) produces sources \(-\chi\mathcal R_{A+C}+M\chi'e\), \(\chi\gamma(A+C)+\chi'p\), both \(L^2\) of order \(q^{-2}\). Their initial data are zero. The strong estimate gives \(\|e\|_{L^2(\delta,T;H^2)}=O_f(q^{-2})\). Further,
\(C_x(t,0)=2c_Le^{-\mu t}[f_{xx}(t,0)+2f_x(t,0)/L]/(\kappa q^3)\), legitimate for smooth \(f\) only. Thus \(\rho_n(f)=O_f(q^{-2})\) on \(J\).

## 5. Density, limits, and the actual theorem

Use a bounded spatial extension operator on both \(L^2\) and \(H^2\), a bounded reflection extension in time for both \(L^2\) and \(H^1\), then mollify and restrict. This converges in \(H^1_tL^2\cap L^2_tH^2\). Averaging the approximants with their spatial reflection preserves convergence and evenness; no Neumann or Dirichlet condition is inserted. The Lions–Magenes interpolation trace gives continuous embedding into \(C_tH^1\), so the initial \(H^1\) trace and \(\|B(f-S)\|_2\le\|B\|_2\|f-S\|_\infty\) converge as well.

For any \(\epsilon>0\), first choose smooth even \(f\) with \(\|S-f\|_\mathcal A<\epsilon\). Then
\(q^{3/2}\|\rho_n(S)\|\le C\epsilon+C_fq^{-1/2}\). Let \(n\to\infty\) **before** \(\epsilon\downarrow0\); no uniform bound on \(C_f\) is needed. Hence \(\rho_n=o(q^{-3/2})\). For \(z_n=\phi_n-Q_n\phi_{n+1}\), leading terms cancel and \(\mathcal Tz_n=\rho_n-Q_n\rho_{n+1}=o(q_n^{-3/2})\). With \(h_n=cq_n^{-2}z_n\), \(\|h_n\|_2\asymp q_n^{-2}\) and \(\|\mathcal Th_n\|=o(q_n^{-7/2})\), contradicting a full-state \(4/7\) Hölder bound. The conclusion applies for any fixed positive \(\delta\); no uniform limit as \(\delta\to0\) is claimed.

## 6. Little-o singular values

Write \(R\phi_n=\rho_n\) and \(\varepsilon_N=\sup_{n>N}n^{3/2}\|\rho_n\|\to0\). Split off the first \(N\) columns (rank \(\le N\)). On block \(N2^k<n\le N2^{k+1}\), the Hilbert–Schmidt norm is \(\le C\varepsilon_N(N2^k)^{-1}\). For \(0\le k\le K=\lfloor2\log_2N\rfloor\), assign rank \(m_k=\lfloor N2^{-k/2}\rfloor\); total assigned rank is \(O(N)\), and each truncated error is \(\le C\varepsilon_NN^{-3/2}2^{-3k/4}\). The remaining tail has Hilbert–Schmidt norm \(O(\varepsilon_NN^{-3})\). Thus \(s_{CN}(R)\le C\varepsilon_NN^{-3/2}\). Monotonicity extends this to all indices, and the rank-one leading term shifts the index by one: \(s_n(\mathcal T)=o(n^{-3/2})\). The abstract diagonal \(n^{-3/2}/\log(n+1)\) demonstrates that little-o alone does not imply \(\mathcal S_{2/3}\).

## 7. Nonlinear scaling and all channels

Assume \(\mathcal F(h)-\mathcal F(0)=\mathcal Lh+\mathcal N(h)\) on an actual \(H^2\)-neighborhood and \(\|\mathcal N(h)\|\le C\|h\|_{H^2}^2\), with \(\|\mathcal Lz_n\|=q_n^{-3/2}\varepsilon_n\), \(\varepsilon_n\to0\). Set \(a_n=\max(\varepsilon_n,q_n^{-1})\to0\), \(h_n=a_nq_n^{-11/2}z_n\). Then
\[
\|h_n\|_2\asymp a_nq_n^{-11/2},\quad \|h_n\|_{H^2}\asymp a_nq_n^{-7/2},\quad
\|\mathcal F(h_n)-\mathcal F(0)\|\le C a_n(\varepsilon_n+a_n)q_n^{-7}. \tag{8}
\]
For \(\alpha=11/14\), the ratio of the left side of a proposed recovery estimate to the \(\alpha\)-power of its right side is at least \(c a_n^{1-2\alpha}\to\infty\). If the output is exactly zero for some index, the estimate already fails there. Since \(h_n\to0\) in \(H^2\), the constructed open weak-initial neighborhood admits the sequence eventually.

The companion proves the quadratic remainder for **all three** output channels in its regime. For odd initial \(h\), \(Y,P\) are odd, hence the linearized force \(-b\bar Y-k\bar P\) vanishes and \(Y_x(0)=Y_x(L)\). The two labeled outward heat powers are opposite, so the full linearized output is a fixed vector multiple of the flux difference. Nonlinear even corrections are included in the quadratic full-output remainder. Therefore \(\alpha\ge11/14\) is excluded for the full nonlinear observation vector **in the explicit weak-initial regime**, not for unspecified loads or the classical domain. The stronger nonlinear \(4/7\) conclusion still requires an unproved tame remainder. This corrects the previous report's unresolved status of the \(H^2\)-quadratic hypothesis within this regime only.

## 8. Targeted prior art and limitations

Source passages and theorem statements were checked, not inferred from abstracts. This search is targeted, non-exhaustive, and cannot establish priority.

| Primary source and exact location | Actual assumptions and result | Comparison |
|---|---|---|
| Volkov, [arXiv:2309.00153v2](https://arxiv.org/html/2309.00153), Theorem 1.1 and §4.3 | An integral kernel in \(L^2(\Omega';H^p(\Omega))\), bounded Lipschitz \(\Omega\), yields weighted square summability and \(s_n=o(n^{-p/d-1/2})\). | Little-o singular improvements are established prior art; our actual residual has not been shown to have the required full \(H^1\) input kernel. Dyadic block deduction is not a claimed new general technique. |
| Koch–Rüland–Salo, [arXiv:2012.01855v4](https://arxiv.org/html/2012.01855), Appendix A.4, Propositions A.4/A.6/A.8 | Singular-value and reference-basis instability on specified compact Hilbert scales; examples distinguish endpoints. | Endpoint instability via rapidly decaying observations is prior art. No automatic alignment with this active PDE. |
| Li–Li–Zhou, [arXiv:2609.10071v1](https://arxiv.org/html/2609.10071), Theorem 1.3, §§3.1–3.2 | Scalar heat, separated source, sector-holomorphic time factor, spectral prior, specific boundary geometry, delayed \(\partial_t\partial_\nu u\) observation: double-log stability. | Close delayed boundary problem, but not initial ODE memory, nonautonomous feedback or our observation norm. |
| Jha–George, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), Theorem 3.10, Assumptions 3.9/3.11/3.12, Lemma 3.13 | Parabolic memory and delay with moving interior control, temporal cutoff, assumed short-time closure and adjoint continuation. | Positive-time cutoffs and coupled memory estimates are not novel ideas; geometry and objective differ. |
| Apraiz–Lecaros–Zamorano, [arXiv:2610.26157v1](https://arxiv.org/html/2610.26157), Theorem 2.3 and its proof, §1.2 | Kelvin–Voigt parabolic–ODE factorization combines a heat Carleman inequality with a weighted ODE estimate; its inverse-coefficient setup uses an interior observation and positive-time Cauchy snapshot. | Relaxation/PDE–ODE inverse methods are established; it does not directly prove a delayed boundary initial-memory asymptotic. The introductory and model passages were inspected; no claim about all proofs or exact overlap is made. |
| Montalto–Stefanov, [arXiv:1306.1978v1](https://arxiv.org/html/1306.1978), Theorem A.1 and proof | Higher-order remainder, conditional linear stability, interpolation and differential continuity give nonlinear conditional stability in Banach scales. | Different elliptic interior-measurement problem. It confirms nonlinear transfer needs separately verified hypotheses, not this instability theorem. |

The particular application combines a nonzero-loaded nonautonomous coupled base, odd initial memory, one boundary flux difference and minimal inherited Sobolev coefficient regularity. That is a **system-specific verified estimate**, not proof that the approximation-plus-corrector technique, cutoff, dyadic estimate, or publication-level theorem is chronologically novel. Exact parabolic corrector prior art was not exhaustively surveyed. The 1980 singular-parabolic boundary-layer article found during search was accessible only as an abstract; no statement about its theorem or proof is made. No genuinely new foundational continuum theory has been demonstrated.


## 9. Verification record

Starting commit: `cdb52b46b364b88d7795507afd60bf0eb21395ea` on the session branch. No previous report or code was altered and no new numerical experiment was added. The following commands ran on this checkout after installing NumPy, SciPy and Matplotlib in a temporary Python environment:

```text
python -m venv .venv
.venv/bin/pip -q install numpy scipy matplotlib
.venv/bin/python -m unittest discover -s code/direction-2-moment-analysis -v
Ran 11 tests in 5.020s
OK
.venv/bin/python -m unittest discover -s code/direction-2-critical-asymptotics -v
Ran 3 tests in 0.006s
OK
```

These tests check prior artificial discretizations and formulas only; passing them does not verify the active base, uniqueness, constants or analytic proof. The three new reports are the only intended tracked additions. Final commit and remote status are recorded in the accompanying response.
