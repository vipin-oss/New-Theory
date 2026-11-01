# Odd-channel boundary continuation after the regularity upgrade

**Date:** 1 November 2026

**Verdict: NOT ESTABLISHED.** The audited positive-time regularity makes the scalar principal coefficient spatially Lipschitz and temporally \(3/4\)-Hölder and improves the potential to \(L^6\). This is a genuine improvement, but none of the inspected boundary estimates directly covers all established hypotheses. More importantly, even a matching scalar estimate would retain the independent distributed source \(SP\). The ODE estimates below do not eliminate its unknown delayed state. No proof or exact counterexample for the actual coupled implication is obtained.

This is a new independent mathematical recalculation and targeted primary-source check by Arena, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. The search is not exhaustive. The investigation does not change the model, claim a new theory, or investigate the other parity channel or nonlinear inverse problem.

## 1. Frozen system and what changed

Use the prescribed nonzero load \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\), \(T=10/\lambda\), \(\delta=T/100\), \(I=(0,L)\), \(J=(\delta,T)\). The base has zero initial memory and is the actual driven trajectory, not a static or constant-coefficient substitute. Let
\[
D=a+k,\quad r=k/D,\quad\alpha=a/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D,\quad Qf=f-\bar f,
\]
where \(a,k,c,\kappa,\lambda,L,A_0,\theta_*,M>0\), \(b\ne0\). Assume only the existing sufficient \(0<q=|g_*|/L<s_*\), not numerically verified. For odd \(h\in H^2_o(I)\), the exact odd pair is
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\\
P_t=-\mu P+\lambda\beta Y,\\
Y(x,0)=0,\quad P(x,0)=h(x),\\
Y(0,t)=Y(L,t)=0,
\end{cases}\tag{1}
\]
with
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\lambda\beta\theta_b+2k\lambda\beta w_b.\tag{2}
\]
The observed odd difference is \(\mathcal T_oh=2A_0\kappa Y_x(0,\cdot)|_J\). The precise target is
\[
Y_x(0,\cdot)=0\text{ in }L^2(J)\quad\Longrightarrow\quad Y=0\text{ a.e. on }J\times I.\tag{UC}
\]
The initial time trace \(Y(\cdot,0)\) is not a spatial endpoint condition. The solution class is
\[
Y\in H^1(0,T;L^2)\cap L^2(0,T;H^2\cap H^1_0)\cap C([0,T];H^1_0),\quad P\in H^1(0,T;L^2)\cap C([0,T];L^2).\tag{3}
\]
In 1-D \(Y\in L^\infty_{t,x}\) and the endpoint derivative is in \(L^2_t\). The audited coefficient result, including the corrected difference-quotient identity, gives for any \(a_1\in(0,\delta)\):
\[
0<m_0\le M_b\le m_1,\quad M_b,\ \kappa/M_b\in C_x^{0,1}C_t^{0,3/4}\text{ in the separate uniform senses},\tag{4}
\]
\[
B\in L^6(J\times I)\cap L^\infty(J;L^2(I))\cap L^2(J;L^\infty(I)),\qquad S\in L^\infty(J\times I).\tag{5}
\]
The constants may depend on \(a_1\); (4)–(5) are **positive-time** bounds, not estimates to the initial corner. The earlier boundary report's statement that parabolic-metric Lipschitz regularity was not yet established is superseded by the audited upgrade, not by an edit of that report. \(M_b\in W^{1,\infty}_{t,x}\) and \(B\in L^\infty_{t,x}\) remain unproved.

## 2. Exact scalar equation and the residual

Set
\[
A=\kappa/M_b,\qquad V=B/M_b,\qquad C=S/M_b.
\]
Division is legitimate because \(M_b\ge m_0>0\). On the delayed cylinder, in \(L^2\),
\[
Y_t-A Y_{xx}=VY+CP.\tag{6}
\]
Here \(A\) is uniformly positive, spatially Lipschitz and \(3/4\)-Hölder in time; \(V\) has the classes of (5), while \(C\in L^\infty\). Products are meaningful: \(VY\in L^2\) by \(Y\in L^\infty\), and \(CP\in L^2\) by \(P\in C_tL^2_x\). One can also write
\[
Y_t-\partial_x(A Y_x)=VY+CP-A_xY_x,\tag{7}
\]
where \(A_x\in L^\infty\) by the audited base regularity. The signs follow from \(\partial_x(A Y_x)=A Y_{xx}+A_xY_x\).

The potential \(VY\) is a zero-order multiplier of the *temperature*. In contrast \(CP\) is a distributed source with its own unknown initial field; (1) does not imply that \(P\) is a bounded multiple of \(Y\), so it cannot be renamed a scalar potential. Given a candidate scalar Carleman weight \(e^{s\phi}\), even if a matching principal estimate existed its right-hand side would contain the weighted norm of \(VY+CP\), plus the weighted boundary normal trace. Zero flux removes the boundary term, not the source.

The improved \(V\in L^6\) permits the concrete fixed-weight estimate
\[
\|e^{s\phi}VY\|_{L^2(J\times I)}
\le\|V\|_{L^6(J\times I)}\|e^{s\phi}Y\|_{L^3(J\times I)}.\tag{8}
\]
This is an ordinary Hölder inequality, not by itself an absorption estimate: a proof must control the \(L^3\) norm by the specific weighted Carleman functional with sufficiently small constants uniformly in the large parameter, including derivatives of the weight. No such weighted absorption at the actual \(A,V\) is asserted here. Thus the improved classes narrow the mismatch, but do not automatically establish a scalar boundary inequality or the coupled implication.

## 3. Targeted primary-source applicability audit

Four primary statements were inspected in their actual texts. The two scalar boundary estimates are the closest inspected endpoint candidates; the latter two are coupled/ODE comparisons. No conclusion is inferred solely from an abstract. “Not applicable directly” does not exclude a future adaptation.

### 3.1 Scalar boundary estimates

**1. P. Gaitan, [Theorem 2.2](https://arxiv.org/html/0706.1422#S2.Thmtheorem2), *Inverse Conductivity Problem for a Parabolic Equation using a Carleman Estimate with One Observation*.** The paper uses a bounded \(C^1\) domain in \(\mathbb R^n\), \(n\le3\), a positive smooth time-independent conductivity \(c(x)\), zero lateral Dirichlet data, and a \(C^4\) positive spatial weight with nonzero gradient and the required normal-sign condition on the unobserved boundary. Its time interval is \((t_0,T)\), and its displayed solution class is \(q\in H^1(t_0,T;H^2(\Omega))\). With weights \(e^{-s\eta}\), \(\varphi\), its conclusion bounds conjugated operator norms plus weighted \(s\lambda^2\varphi|\nabla q|^2+s^3\lambda^4\varphi^3|q|^2\) by a weighted \(\partial_\nu q\) integral on \(\Gamma_0\) **plus**
\(\iint e^{-2s\eta}|q_t-\nabla\cdot(c\nabla q)|^2\). It has no unknown ODE state. The interval geometry and one endpoint observation are plausible 1-D counterparts, and a delayed interval is built in. However the active \(A(x,t)\) is not established to be the theorem's smooth time-independent coefficient, and (3) is not its displayed \(H^1_tH^2_x\) class. An arbitrary \(L^6\) potential is not incorporated in the theorem; it may be placed in the residual but then requires a separate absorption proof. **NOT APPLICABLE DIRECTLY.**

**2. P. Albano and D. Tataru, [Theorem 3.1](https://ejde.math.txstate.edu/Volumes/2000/22/albano.pdf), *Carleman estimates and boundary observability for a coupled parabolic-hyperbolic system*.** The scalar part considers \(Q\theta=f\), \(Q=\partial_t-\partial_i(b^{ij}\partial_j)+b^i\partial_i+b\), zero Dirichlet data on the smooth bounded domain, \(f\in L^2\) and initial \(\theta_0\in H^1_0\). Assumption H1 requires uniformly elliptic \(C^1\) principal coefficients and bounded measurable lower-order coefficients. For a smooth weight with nonvanishing spatial gradient and singular time factors, the theorem controls a weighted anisotropic order-two norm by \(\|e^{\tau\psi}f\|_2^2\) and a signed weighted normal-derivative boundary integral. A monotone 1-D weight can select a boundary side, and a time-translated positive interval is possible. Our \(Y\) and \(CP+VY\) have the necessary basic \(L^2\) forcing/Dirichlet class, and (7) has a bounded drift \( +A_xY_x \) when the right-hand drift term is moved to the left. But the improved \(A\) is not established \(C^1\) in space-time; \(V\in L^6\) is not established bounded. Treating \(VY+CP\) as the nonzero residual preserves the second gap even if a scalar principal-coefficient extension were proved. The paper's coupled result is heat–wave, not heat–ODE with only the heat flux measured. **NOT APPLICABLE DIRECTLY.**

### 3.2 ODE and coupled-memory comparisons

**3. D. P. Jha and R. K. George, [Lemma 3.5 and Proposition 3.8](https://arxiv.org/html/2506.22221), *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, arXiv v2.** Under their moving-control weight construction and delay-compatible cutoff assumptions, Lemma 3.5 states for \(q_t+\mu q=G\), \(q(0)=0\), an ODE weighted functional estimate by the weighted residual \(G\) **plus an interior moving-region observation of \(q\)**. Proposition 3.8 treats a constant-principal heat equation coupled to finitely many zero-initial exponential ODE realizations, with a moving interior observation and a history remainder. The observations are interior, not a single endpoint normal derivative; their initial ODE states are zero, unlike independent \(P(\delta)\). Their geometric/weight assumptions and coefficient class are not verified for (1). The preprint also explicitly assumes an adjoint continuation property later in its compactness–uniqueness step; it is not a theorem furnishing (UC) here. **NOT APPLICABLE DIRECTLY.** This audit checks these primary statements, not every proof in the preprint.

**4. J. Apraiz, R. Lecaros and S. Zamorano, [Lemma 2.2 and Theorem 2.3](https://arxiv.org/html/2610.26157), *A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations*, arXiv v1.** On a smooth bounded domain in the paper's \(N=2,3\) setting and a time interval symmetric around \(t_0\), the inspected Lemma 2.2 states for \(v\in H^1_tL^2_x\), \(\mathcal P v=v_t+v\), and its centered weight \(\phi\):
\[
\iint |v|^2e^{2s\phi}\le \frac{C}{s}\iint |\mathcal Pv|^2e^{2s\phi}
+\frac{C}{\sqrt s}\int |v(x,t_0)|^2e^{2s\phi(x,t_0)}dx.\tag{9}
\]
Its Kelvin–Voigt coupled estimate uses a constant heat operator, an interior observation and a fixed-time trace, not an endpoint-only flux. Its residual and trace are explicit. The factorization, dimensions, weights and regularity are different from (1), and no identification of the fixed-time term with the observed boundary flux is provided. The lemma illustrates a possible trace-dependent estimate, not a directly applicable boundary theorem for \(P\). **NOT APPLICABLE DIRECTLY.**

None of these four inspected statements establishes a boundary scalar Carleman estimate with the entire actual coefficient class *and* an estimate eliminating \(CP\). Other potentially relevant rough-coefficient results were located only at abstract/secondary-description level in this targeted search; their primary theorem hypotheses were not verified and no claims are based on them. This is not an exhaustive negative literature result.

## 4. Independent weighted ODE and delay calculation

### 4.1 Localized delayed state

The actual \(H^1_tL^2_x\) ODE gives the exact Bochner formulas
\[
P(\delta)=e^{-\mu\delta}h+\lambda\beta\int_0^\delta e^{-\mu(\delta-r)}Y(r)\,dr,\tag{10}
\]
\[
P(t)=e^{-\mu(t-\delta)}P(\delta)+\lambda\beta\int_\delta^t e^{-\mu(t-r)}Y(r)\,dr,\quad t\in J.\tag{11}
\]
The first term in (11) is the independent delayed state, including *all* pre-observation history (10). Zero endpoint flux on \(J\) is not an initial condition for \(P\) and has not been shown to determine \(P(\delta)\). An ODE estimate beginning at \(\delta\) with a zero initial state would therefore be an extra assumption, not a consequence of (UC)'s hypothesis.

### 4.2 A derived centered weighted estimate

Pick a subinterval \(J_0=(t_-,t_+)\Subset J\), symmetric around \(t_0=(t_-+t_+)/2\). Let \(\phi(x,t)\) be a measurable weight finite at \(t_0\) and nonincreasing as \(t\) moves away from \(t_0\), separately in either direction. For \(s>0\), set \(W_s=e^{s\phi}\). The ODE for a.e. \(x\) has the oriented variation-of-constants formula
\[
P(t,x)=e^{-\mu(t-t_0)}P(t_0,x)+\lambda\beta\int_{t_0}^{t}e^{-\mu(t-r)}Y(r,x)\,dr.\tag{12}
\]
For \(r\) between \(t\) and \(t_0\), \(W_s(x,t)\le W_s(x,r)\); also \(e^{-\mu(t-r)}\le e^{\mu|J_0|}\). Cauchy–Schwarz and Fubini separately on the two sides yield the explicit bound
\[
\begin{aligned}
\iint_{J_0\times I}W_s^2|P|^2
&\le 2e^{2\mu|J_0|}|J_0|\int_I W_s(x,t_0)^2|P(t_0,x)|^2dx\\
&\quad+2e^{2\mu|J_0|}|\lambda\beta|^2|J_0|^2
\iint_{J_0\times I}W_s^2|Y|^2.\tag{13}
\end{aligned}
\]
For instance, \(|\int_{t_0}^t W_s(x,r)Y(r,x)dr|^2\le |J_0|\int_{J_0}W_s^2|Y|^2dr\), and integrating in \(t\) gives the displayed \(|J_0|^2\) bound. All terms are finite for standard negative singular Carleman weights, and \(P(t_0)\in L^2\). This is a **valid but non-sharp ODE estimate** for (1); it does not use a scalar Carleman theorem. A sharper estimate might reduce the coefficient of the weighted \(Y\) term, as in the inspected lemma (9), but the unknown fixed-time memory contribution still needs separate control.

For comparison, a coupled proof would need a justified estimate enabling the weighted source term
\[
\iint W_s^2 |CP|^2\le \|C\|_\infty^2\iint W_s^2|P|^2\tag{14}
\]
to be absorbed by a valid temperature Carleman functional plus measured boundary data, with no uncontrolled trace. Equations (13)–(14) instead leave
\[
\int_I e^{2s\phi(x,t_0)}|P(t_0,x)|^2dx,\tag{15}
\]
whose value is not known from the endpoint observation. Formula (12) with \(Y=0\) and \(P=e^{-\mu(t-t_0)}p(x)\), \(p\ne0\), shows that the **ODE alone** cannot bound weighted \(P\) purely by weighted \(Y\); this pair is not asserted to solve the heat equation with the active \(C\), and is not a counterexample to (UC). No conclusion is drawn that all more sophisticated coupled estimates must contain this exact trace.

### 4.3 What a coupling lower bound does and does not do

The earlier audited calculation provides \(C_w=W_s+2C_BW_R\), \(q_{\rm nd}=|b|r\theta_*/(8kC_w)\), and, under the **additional** unverified hypothesis \(0<q<\min\{s_*,q_{\rm nd}\}\),
\[
|S|>s_0:=\lambda\alpha|b|r\theta_*/4>0.\tag{16}
\]
This concerns the same physical experiment, but is stronger than the existing hypothesis and its numerical validity is unknown. It gives \(|C|\ge s_0/m_1\), so formally the heat equation makes the source visible *as an interior residual*:
\[
\|W_sP\|_2\le (m_1/s_0)\|W_s(Y_t-A Y_{xx}-VY)\|_2.\tag{17}
\]
Equation (17) is a legitimate interior identity in \(L^2\); it is not a bound by endpoint flux. The scalar estimate controls temperature by the residual, not that residual by the boundary trace. Inserting (17) into a scalar inequality produces a circular dependence unless an additional coupled estimate closes it. Nondegeneracy therefore does not eliminate (15), nor does it prove \(Y=0\).

## 5. Alternative routes and quantitative constraints

- **Volterra reduction.** Combining (6) and (11) produces the exact equation
\[
Y_t-A Y_{xx}=VY+C e^{-\mu(t-\delta)}P(\delta)
+\lambda\beta C(t,x)\int_\delta^t e^{-\mu(t-r)}Y(r,x)dr.\tag{18}
\]
Even if the integral term could be absorbed by a suitable time-weight estimate, the spatially distributed source \(C e^{-\mu(t-\delta)}P(\delta)\) remains. The coefficients vary in space and time, so a known-time-factor inverse-source theorem is not automatically applicable. No cancellation or mode decoupling is assumed.
- **Coupled Carleman/cascade.** A future proof needs a scalar endpoint estimate at the actual \(A,V\), or a precisely justified absorption of \(VY\), combined with a genuinely coupled mechanism controlling the unknown memory trace or residual using the one boundary observation. The inspected moving-region estimates impose different observations and/or zero ODE state. Equation (13) does not supply this mechanism.
- **Augmented observability.** A uniform estimate of the full \(L^2\) memory on any interior strip solely by the fixed \(L^2\) endpoint flux is already ruled out by the earlier compactness argument. For a fixed standard positive weight on a compact substrip and a boundary weight bounded for that fixed parameter, an estimate controlling that full weighted memory only by the weighted flux would likewise imply the prohibited unweighted strip estimate. This does not rule out weaker norms, extra terms, stronger observations, constants depending on a priori regularity, or a *qualitative* temperature continuation result.
- **Other routes.** An adjoint-density argument or an exact constrained inverse-source theorem might settle a qualitative question, but neither has been proved here for the active, nonautonomous coefficients and delayed initial-memory state. No assertion of modal independence or spectral completeness is made.

An arbitrary smooth interior-supported scalar heat solution with its residual chosen as a source is not an exact counterexample: it has not been shown to satisfy \(CP\) with the prescribed ODE and the fixed initial/boundary conditions. No nonzero odd \(h\) generating an exact zero flux with nonzero temperature on \(J\) has been constructed.

## 6. Distinct conclusions and final decision

The established compactness result gives approximate invisibility and failure of a uniform strong \(L^2\) memory observability inequality. It does not prove a nontrivial exact kernel, failure of (UC), or instability in every weaker topology. Conversely, a proof of (UC) would not by itself establish recovery of the initial memory: \(Y=0\) on \(J\) is a boundary-to-interior statement, whereas a separate question concerns determining the earlier state from delayed information. No such additional inference is made here. Stability and quantitative observability are stronger and different questions from qualitative continuation or injectivity.

**NOT ESTABLISHED.** The improved coefficient classes survive the prior independent audit and are useful, but no inspected theorem directly supplies the full scalar boundary estimate at those classes, and the independent delayed memory trace remains uncontrolled in the coupled argument. Neither a complete conditional theorem with verified nontrivial hypotheses nor an exact counterexample is proved in this investigation. The full odd kernel remains unresolved.
