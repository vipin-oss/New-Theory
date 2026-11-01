# Independent audit of the regularity-updated odd-channel UC investigation

**Date:** 1 November 2026

**Verdict: AUDIT PASSED WITH CORRECTIONS.** The scalar equations, signs, delayed-state formula, centered ODE inequality, nondegeneracy bound and central **NOT ESTABLISHED** conclusion survive independent recalculation. One correction is required to the scope of the weighted estimate: a measurable weight merely finite at the center and monotone away from it need not make the weighted trace integrable across space. The displayed inequality is valid in the extended-real sense; to assert finite terms, impose the explicit boundedness/integrability conditions in §4. Standard centered negative singular weights satisfy them. Further clarifications concern the theorem comparisons and the fact that the trace obstruction belongs to the particular proof route, not to every conceivable weight or proof.

This is an independent single-agent Arena recalculation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. The literature check is restricted to the four requested primary-source families; it is not exhaustive. No new constitutive theory is claimed.

## 1. Claim inventory and frozen system

| Claim in the audited report | Audit decision |
|---|---|
| Exact normalized and divergence-form scalar equations | **PASS**: signs and product classes checked in §2. |
| Positive-time principal and potential classes | **PASS WITH CLARIFICATION**: separate uniform Hölder/Lipschitz estimates, not a mixed Hölder norm or \(W^{1,\infty}_{t,x}\). |
| Four primary theorem families do not directly furnish the claimed coupled result | **PASS WITH CLARIFICATION**: exact statements, regularity, and residuals in §3; this is not a proof that no adaptation exists. |
| Centered weighted ODE bound and constants | **PASS WITH CORRECTION**: bound is correct; finiteness needs hypotheses on the spatial weight, §4. |
| Unknown delayed trace | **PASS** as a limitation of this argument, not a general impossibility result or counterexample. |
| Sufficient lower bound for \(S\) and interior residual estimate | **PASS** under the extra fixed-unit threshold, not verified for the experiment. |
| Failure of uniform strong memory observability | **PASS WITH CLARIFICATION**: its weighted version needs a strictly positive lower bound on the chosen compact strip and bounded boundary weight. |
| Earlier UC verdict **NOT ESTABLISHED** | **PASS**: neither the scalar theorem match nor the coupled memory closure has been proved; no counterexample follows. |

Let \(I=(0,L)\), \(J=(\delta,T)\), \(T=10/\lambda\), \(\delta=T/100\), and prescribed load \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\). Put
\[
D=a+k,\quad r=k/D,\quad\alpha=a/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D,\quad Qf=f-\bar f.
\]
Keep the frozen positive constants \(a,k,c,\kappa,\lambda,L,A_0,\theta_*,M\), and \(b\ne0\). The base is the actual nonzero-loading solution with zero base memory. Assume the existing sufficient condition \(0<q=|g_*|/L<s_*\), which is not numerically verified. For \(h\in H^2_o(I)\),
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\quad P_t=-\mu P+\lambda\beta Y,\\
Y(\cdot,0)=0,\quad P(\cdot,0)=h,\quad Y(0,t)=Y(L,t)=0,
\end{cases}\tag{1}
\]
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\lambda\beta\theta_b+2k\lambda\beta w_b.\tag{2}
\]
The observation is \(\mathcal T_oh=2A_0\kappa Y_x(0,\cdot)|_J\). The question is whether \(Y_x(0,\cdot)=0\) in \(L^2(J)\) forces \(Y=0\) in \(L^2(J\times I)\). Initial time and spatial endpoint traces remain distinct.

## 2. Independent scalar reduction and solution classes

The established solution class is
\[
Y\in H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x})\cap C_tH^1_{0,x},\qquad
P\in H^1_tL^2_x\subset C_tL^2_x.\tag{3}
\]
The 1-D embedding \(H^1(I)\hookrightarrow L^\infty(I)\) gives \(Y\in L^\infty_{t,x}\). For any cutoff before \(\delta\), the audited base result supplies positive \(m_0\le M_b\le m_1\), spatial Lipschitz and temporal \(3/4\)-Hölder estimates for \(M_b\) and \(A=\kappa/M_b\), \(S\in L^\infty\), and
\[
B\in L^6(J\times I)\cap L^\infty(J;L^2)\cap L^2(J;L^\infty).
\]
The bound is uniform separately in \(x,t\), and implies Lipschitz regularity for the metric \(|x-x'|+|t-t'|^{1/2}\) on the delayed cylinder. It does not imply a bounded classical time derivative or \(B\in L^\infty_{t,x}\); no estimate is extended to \(t=0\).

Define \(V=B/M_b\), \(C=S/M_b\). Since the positive reciprocal is bounded, \(V\) inherits the three classes of \(B\), and \(C\in L^\infty\). Divide (1) to obtain in \(L^2(J\times I)\)
\[
Y_t-A Y_{xx}=VY+CP.\tag{4}
\]
Indeed \(VY\in L^2\) because \(V\in L^2\) on a bounded cylinder and \(Y\in L^\infty\); \(CP\in L^2\) because \(P\in C_tL^2_x\). Since \(A_x\in L^\infty\) and \(Y_x\in L^2\), the product rule in distributions gives
\[
Y_t-\partial_x(A Y_x)=VY+CP-A_xY_x.\tag{5}
\]
Moving the drift on the right to the left gives **\(+A_xY_x\)**. The audited signs are correct. From \(Y\in L^2_tH^2_x\), the 1-D trace theorem gives \(Y_x(0,\cdot)\in L^2(J)\); zero flux is a Sobolev trace statement. These observations justify every displayed unweighted product, not a particular weighted Carleman inequality.

For a weight \(W\) such that \(WY\in L^3\), Hölder gives
\[
\|WVY\|_2\le\|V\|_6\|WY\|_3.\tag{6}
\]
For fixed bounded standard weights, all quantities are finite. This does not automatically give the parameter-small estimate needed to absorb \(VY\) in a Carleman functional. The multiplier \(VY\) and the independent ODE source \(CP\) are distinct; no bounded function \(p\) with \(CP=pY\) has been shown to exist.

## 3. Verification of the four primary theorem families

The texts below were reopened at their actual numbered statements, not inferred from abstracts. “Not directly applicable” means the required mapping or extension is not proved; it does not mean the theorem or a future adaptation is false.

### 3.1 Gaitan, Theorem 2.2 — scalar boundary estimate

[P. Gaitan, *Inverse Conductivity Problem for a Parabolic Equation using a Carleman Estimate with One Observation*, arXiv:0706.1422, §2.1](https://arxiv.org/html/0706.1422#S2.Thmtheorem2): The setup uses a bounded \(C^1\) domain \(\Omega\subset\mathbb R^n\), \(n\le3\), a positive smooth time-independent scalar \(c(x)\), and \((t_0,T)\). Assumption 2.1 requires a positive \(C^4\) spatial weight with nonzero gradient and \(\partial_\nu\widetilde\beta\le0\) on the unobserved boundary. The displayed theorem applies to zero-Dirichlet \(q\in H^1(t_0,T;H^2(\Omega))\). For sufficiently large parameters it bounds weighted conjugated norms, gradient, and \(q\) terms by the weighted boundary normal derivative on \(\Gamma_0\) **plus** the squared weighted residual \(q_t-\nabla\cdot(c\nabla q)\). No initial ODE state is present.

The report accurately states this theorem and its mismatch. A 1-D endpoint and delayed interval have natural geometric counterparts, but \(A(x,t)\) is not shown to be this smooth, time-independent coefficient and (3) is not the theorem's displayed \(H^1_tH^2_x\) class. The theorem contains no \(L^6\) potential as a built-in coefficient; putting \(VY\) in its residual is possible, but absorption needs proof. A density extension or another scalar estimate might exist; it has not been demonstrated here. Even if all scalar gaps were closed, \(CP\) remains in the residual. **NOT APPLICABLE DIRECTLY.**

### 3.2 Albano–Tataru, Theorem 3.1 and coupled theorem

[P. Albano and D. Tataru, *Carleman estimates and boundary observability for a coupled parabolic-hyperbolic system*, primary PDF, §2–§5](https://ejde.math.txstate.edu/Volumes/2000/22/albano.pdf): H1 requires uniformly elliptic \(C^1\) principal coefficients and bounded measurable lower-order coefficients for their scalar parabolic operator \(Q=\partial_t-\partial_i(b^{ij}\partial_j)+b^i\partial_i+b\). The scalar problem has homogeneous Dirichlet boundary, \(f\in L^2\) and \(\theta_0\in H^1_0\). Theorem 3.1 uses a smooth spatially noncritical weight and time-singular factor and bounds a weighted anisotropic norm by the weighted residual \(f\) and a signed normal-derivative boundary integral. A positive delayed interval can be reparameterized, and the boundary sign must be checked for the chosen endpoint.

The report's scalar comparison is substantively correct: our divergence drift \(+A_xY_x\) is bounded, but \(A\) is not established \(C^1\) in space-time and \(V\) is not known bounded. Taking \(VY+CP\) as \(f\) avoids imposing boundedness of \(V\) on the scalar operator, but does **not** control that residual from the boundary. The paper's Theorem 5.1 is a genuinely coupled **hyperbolic–parabolic** estimate under H1 and pseudoconvexity H2, and its right side observes normal derivatives of **both** the wave and heat components. A time ODE has no wave principal symbol or wave boundary derivative, and no admissible specialization to (1) with only the heat trace follows from the stated theorem. **NOT APPLICABLE DIRECTLY.**

### 3.3 Jha–George, Lemma 3.5 and Proposition 3.8

[D. P. Jha and R. K. George, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, arXiv:2506.22221v2, §3.1–3.4](https://arxiv.org/html/2506.22221): In their bounded smooth \(\Theta\subset\mathbb R^n\), Lemma 3.5 assumes the moving-region geometry and delay-compatible weights of Lemma 3.2 and Assumption 3.3, \(\mu>0\), and \(q_t+\mu q=G\), \(q(0)=0\). For sufficiently large parameters it states
\[
I_O(q)\le C\iint |G|^2e^{-2s\phi}+C\iint_{(0,T)\times\varpi(t)}(\lambda s\xi)^2|q|^2e^{-2s\phi}.
\]
The ODE functional controls weighted \(q_t,q\); the observation is an **interior moving-region** integral of \(q\). The functional is introduced for \(q\in L^2(Q)\) satisfying a first-order equation in time; the statement does not spell out a separate full Sobolev class, and its weighted derivative must be meaningful. Proposition 3.8 treats a constant-principal Dirichlet heat equation coupled to finite exponential ODE variables with \(q_j(0)=0\), a temporal cutoff, weighted forcing \(F\), moving interior temperature observation and a short-time remainder. The text's later removal of a terminal remainder additionally assumes an adjoint continuation property.

The quoted zero state, interior observations and residual/remainder are accurately represented in the audited report. Taking one exponential is algebraically possible, and a zero-initial *convolution part* can be separated, but the actual delayed state \(P(\delta)\) becomes an additional distributed forcing; it is not eliminated by the proposition. The fixed boundary trace, \(A(x,t)\), and \(V\in L^6\) are not its hypotheses. The statement check is not a certification of the full preprint's proof. **NOT APPLICABLE DIRECTLY.**

### 3.4 Apraiz–Lecaros–Zamorano, Lemma 2.2 and Theorem 2.3

[J. Apraiz, R. Lecaros and S. Zamorano, *A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations*, arXiv:2610.26157v1, §2.1](https://arxiv.org/html/2610.26157): In their smooth bounded \(\Omega\subset\mathbb R^N\), \(N=2,3\), and symmetric interval \((t_-,t_+)\) around \(t_0\), the centered singular weight is
\[
\phi_\ell(x,t)=\frac{e^{\ell\eta(x)}-e^{2\ell\|\eta\|_\infty}}{(t-t_-)(t_+-t)}.
\]
Lemma 2.2 states for every \(v\in H^1((t_-,t_+);L^2(\Omega))\), \(\mathcal Pv=v_t+v\), sufficiently large \(s\),
\[
\iint |v|^2e^{2s\phi_\ell}\le\frac C s\iint |\mathcal Pv|^2e^{2s\phi_\ell}
+\frac C{\sqrt{s}}\int_\Omega|v(t_0)|^2e^{2s\phi_\ell(t_0)}dx.\tag{7}
\]
No zero initial state is required. Theorem 2.3, for \(b\in L^\infty(\Omega)\) with \(\|b\|_\infty\le M\) and sufficiently regular \(v=0\) on the lateral boundary, controls \(I_{s,\ell}(\mathcal Pv)\) by a weighted residual of \(H_bv=v_{tt}-\Delta v-\Delta v_t+bv_t\), an **interior** observation of \(\mathcal Pv\), and the weighted fixed-time trace of \(v\). Its scalar heat component has constant principal coefficient.

The audited report correctly identifies the trace and interior observation. The ODE lemma is a useful model for deriving a related estimate with a different decay rate, but it is stated for \(\partial_t+1\) and its specific weights/domain; an adaptation to \(\partial_t+\mu\) is not itself a boundary UC theorem. Theorem 2.3's factorization, \(N=2,3\) context, unknown and observations do not give an endpoint-flux-only theorem for (1). **NOT APPLICABLE DIRECTLY.**

## 4. Re-derivation of the delayed and centered ODE bounds

The Bochner ODE in (1) implies
\[
P(\delta)=e^{-\mu\delta}h+\lambda\beta\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr,\quad
P(t)=e^{-\mu(t-\delta)}P(\delta)+\lambda\beta\int_\delta^t e^{-\mu(t-r)}Y(r)dr.\tag{8}
\]
These equalities are in \(L^2(I)\); a.e. \(x\), the same formula holds pointwise in time for an \(H^1\) representative. The delayed field is unknown, but it is **not claimed arbitrary independent of the prior trajectory**: it is exactly the correlated state in (8). Vanishing measured flux for \(t>\delta\) has not been shown to make it vanish.

Let \(J_0=(t_-,t_+)\Subset J\), \(t_0=(t_-+t_+)/2\), \(H=|J_0|\), and \(\gamma=\lambda\beta\). For \(t\ge t_0\),
\[
P(t)=e^{-\mu(t-t_0)}P(t_0)+\gamma\int_{t_0}^{t}e^{-\mu(t-r)}Y(r)dr.
\]
For \(t<t_0\),
\[
P(t)=e^{\mu(t_0-t)}P(t_0)-\gamma\int_t^{t_0}e^{\mu(r-t)}Y(r)dr.\tag{9}
\]
Thus both signs and time orientations in the report are correct. Suppose for a.e. \(x\), \(\phi(x,t)\) is finite at \(t_0\) and nonincreasing as one moves away from \(t_0\); set \(W_s=e^{s\phi}\), \(s>0\). For \(r\) between \(t\) and \(t_0\), \(W_s(x,t)\le W_s(x,r)\). Since \(e^{-\mu(t-r)}\le e^{\mu H}\) in both directions,
\[
\begin{aligned}
W_s(x,t)|P(t,x)|\le{}&e^{\mu H}W_s(x,t_0)|P(t_0,x)|\\
&+|\gamma|e^{\mu H}\int_{\min(t,t_0)}^{\max(t,t_0)}W_s(x,r)|Y(r,x)|dr.
\end{aligned}\tag{10}
\]
Squaring with \((u+v)^2\le2u^2+2v^2\), integrating the first term in \(t\), and using Cauchy–Schwarz in \(r\), then Tonelli, for the second gives
\[
\begin{aligned}
\iint_{J_0\times I}W_s^2|P|^2
&\le 2e^{2\mu H}H\int_I W_s(x,t_0)^2|P(t_0,x)|^2dx\\
&\quad+2e^{2\mu H}|\gamma|^2H^2\iint_{J_0\times I}W_s^2|Y|^2.\tag{11}
\end{aligned}
\]
The interval factors in the audited report are valid but not sharp; the constant is independent of \(s\). Tonelli permits the inequality as an extended-real statement, but **pointwise finiteness of \(\phi(x,t_0)\) alone does not ensure finite right-hand terms**. For a finite estimate, it is sufficient that \(W_s(\cdot,t_0)P(t_0)\in L^2(I)\) and \(W_sY\in L^2(J_0\times I)\); a simple sufficient condition is \(W_s(\cdot,t_0)\in L^\infty(I)\), because the maximum property makes \(W_s\) bounded throughout the cylinder. For example, on \((0,1)\), a time-constant weight \(\phi(x,t)=1/x\) is finite a.e. and monotone in time, but its exponential times a nonzero constant is not \(L^2\). This illustrates the missing hypothesis; it is not an active-system counterexample.

For the standard weight in (7), its numerator is negative and uniformly bounded away from zero under its nontrivial-weight assumptions; the denominator is positive inside and vanishes at each time endpoint. Thus \(\phi_\ell\to-\infty\) uniformly as \(t\to t_\pm\), \(0<W_s\le W_s(\cdot,t_0)\le1\), and the trace and space-time terms are finite. Endpoint singularities cause no boundary-time term in (11), and the bound is valid for this exponential weight; a different polynomially weighted factor must separately satisfy the monotonicity and integrability assumptions. The result is an ODE inequality, not the scalar boundary Carleman estimate.

### Is the trace inherent in every possible approach?

No. The explicit calculation proves only that the chosen centered estimate contains \(P(t_0)\). An ODE-only estimate with no state term cannot hold for arbitrary ODE solutions: \(Y=0\), \(P=e^{-\mu(t-t_0)}p(x)\) obeys the ODE for \(p\ne0\), but need not obey the heat equation. A different direction changes the term. For example, on \((\delta,T)\), with the nonsingular one-sided weight \(W=e^{-\sigma(t-\delta)}\), \(\sigma>0\), (8) and Young's convolution inequality yield
\[
\|WP\|_{L^2(J\times I)}^2
\le \frac{1}{\sigma+\mu}\|P(\delta)\|_2^2
+\frac{2|\gamma|^2}{(\sigma+\mu)^2}\|WY\|_{L^2(J\times I)}^2.\tag{12}
\]
The factor \(1/(\sigma+\mu)\) comes from \(2\int_0^{T-\delta}e^{-2(\sigma+\mu)t}dt\); the convolution kernel has \(L^1\) norm at most \((\sigma+\mu)^{-1}\). This bounds the convolution with a small parameter but leaves \(P(\delta)\), and the chosen weight is not asserted to provide the needed heat boundary estimate. A backward-oriented integration could instead use a terminal state; it does not make that state known. A genuinely coupled mechanism or different weight might control such a term; this audit neither proves nor rules it out.

## 5. Additional coupling bound and residual

The original existence estimates give, at zero base memory, \(\|y_b\|_{\mathcal E_T}\le2C_Bq\) and \(\|w_b\|_\infty\le W_s q+W_R\|y_b\|_{\mathcal E_T}\le C_wq\), with \(C_w=W_s+2C_BW_R>0\) in the fixed-unit convention. If the **additional**, unverified condition
\[
0<q<\min\{s_*,q_{\rm nd}\},\quad q_{\rm nd}=\frac{|b|r\theta_*}{8kC_w}
\]
holds, the established \(\theta_b\ge\theta_*/2\) gives
\[
|S|=\lambda\alpha|br\theta_b-2kw_b|
\ge\lambda\alpha(|b|r\theta_*/2-2kC_wq)
>\lambda\alpha|b|r\theta_*/4=:s_0.\tag{13}
\]
The sign of \(b\) is immaterial. The bound and constants match the original record. Because \(M_b\le m_1\), \(|C|\ge s_0/m_1\), so from (4), for weights for which the products are in \(L^2\),
\[
\|WP\|_2\le(m_1/s_0)\|W(Y_t-A Y_{xx}-VY)\|_2.\tag{14}
\]
This is an interior residual identity, not a measurement estimate; the scalar inequality ordinarily estimates temperature *in terms of* this residual. It is circular to insert (14) and infer the residual is controlled by the endpoint flux. The lower bound can be useful in a future cascade proof, but it does not by itself eliminate the trace in (11). If \(Y=0\) were already known on \(J\), then (1) would give \(SP=0\) there and (13) would imply \(P=0\) there; that is a consequence of the desired temperature conclusion, not its proof.

## 6. Alternatives and logical distinctions

- **Coupled boundary Carleman or augmented observability:** the four inspected families do not provide a theorem with our coefficient class, independent delayed ODE state, and one endpoint heat derivative. A valid proof would need a precise coupled estimate, or another mechanism controlling the source from the actual measurement. The centered trace is an identified gap, not proof that all such estimates fail.
- **Volterra/inverse source:** (8) gives \(Y_t-AY_{xx}=VY+C e^{-\mu(t-\delta)}P(\delta)+\gamma C\int_\delta^te^{-\mu(t-r)}Y(r)dr\). The actual \(C(x,t)\) is nonautonomous and the initial field is unknown. No inspected inverse-source theorem removes this term under exactly the given conditions.
- **Adjoint density:** the bounded \(L^2_o\)-extension has \(\ker\mathcal T_o=\{0\}\) iff the adjoint range is dense in \(L^2_o\). Such density would be sufficient for the frozen \(H^2_o\) injectivity question but is stronger than necessary. No derivation of the boundary adjoint range and its density is provided; abstract duality alone proves neither density nor (UC).
- **Compactness:** the earlier sine-sequence argument rules out uniform control of \(\|P\|_{L^2(J'\times I)}\) by \(\|Y_x(0,\cdot)\|_{L^2(J)}\) for all odd directions, for each positive-length \(J'\subset J\). The report's weighted consequence is valid if the fixed weight is **bounded below by a positive constant** on a compact strip and its boundary weight is bounded above: such a weighted estimate would imply the forbidden unweighted estimate. Mere pointwise positivity without a uniform lower bound would not be enough. Weaker norms, additional terms or stronger observations are not excluded.

Boundary-to-interior **UC** concerns \(Y\) on \(J\); qualitative **odd injectivity** concerns whether \(\mathcal T_oh=0\) forces \(h=0\). They are not identical: even with (UC), recovering \(h\) requires additional arguments, including treatment of the delayed state. **Backward uniqueness** asks whether an earlier state is determined by a later coupled state; no such property is established here. **Quantitative observability** is an inequality with specified norms, while **stability of reconstruction** can use different norms or conditional moduli. Compactness disproves one strong uniform inequality, not qualitative injectivity or every form of stability. No exact nonzero odd input with zero observed flux and nonzero interior temperature has been constructed; failure to prove (UC) is not its negation.

## 7. Final decision

**AUDIT PASSED WITH CORRECTIONS.** The prior **NOT ESTABLISHED** UC verdict survives. Both a direct theorem mismatch and the unresolved treatment of the distributed delayed memory are real gaps in the inspected proof routes; neither has been proved an unavoidable obstruction to every possible method. The centered ODE estimate is correct once weight integrability is stated, and its uncontrolled trace is not a counterexample to the full coupled system. No UC theorem, exact counterexample, or full-kernel conclusion is claimed.
