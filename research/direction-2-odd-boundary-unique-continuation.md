# Boundary unique continuation for the active odd parabolic–memory system

**Date:** 1 November 2026
**Verdict: NOT ESTABLISHED**

Neither a proof of (UC) for the frozen experiment nor an exact counterexample has been obtained. The obstruction below is an identified gap in a particular Carleman approach, not a proof that every such approach must fail. The literature check is targeted, not exhaustive. This is an Arena single-agent investigation, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator.

## 1. Frozen problem and meaning of the question

Let \(I=(0,L)\), \(J=(\delta,T)\), \(T=10/\lambda\), \(\delta=T/100\), and the prescribed **nonzero** load be \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\). Put
\[
D=a+k,\quad r=k/D,\quad\alpha=a/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D,\quad Qf=f-\bar f.
\]
Here \(a,k,\lambda,c,\kappa,L,A_0,\theta_*,M>0\), \(b\ne0\). The base is the actual symmetric solution driven by that load, with base initial memory zero. It is not an equilibrium or a constant-coefficient surrogate. Set
\[
M_b=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\lambda\beta\theta_b+2k\lambda\beta w_b.
\]
For odd \(h\in X_o=\{h\in H^2(I):h(L-x)=-h(x)\}\), the exact active system is
\[
\begin{cases}
M_bY_t-\kappa Y_{xx}=BY+SP,\\
P_t=-\mu P+\lambda\beta Y,\\
Y(x,0)=0,\quad P(x,0)=h(x),\\
Y(0,t)=Y(L,t)=0.
\end{cases}\tag{1}
\]
The fixed observation is \(\mathcal T_oh=2A_0\kappa Y_x(0,\cdot)|_J\). All time and boundary statements are Sobolev traces; the endpoint derivative is in \(L^2(J)\). The question is exactly
\[
Y_x(0,t)=0\ \text{a.e. on }J\quad\Longrightarrow\quad Y=0\ \text{a.e. on }J\times I.\tag{UC}
\]
The Dirichlet trace at \(x=0\) already vanishes. The implication concerns solutions generated from the specified initial pair, not arbitrary scalar heat solutions. We assume only \(0<q=|g_*|/L<s_*\), the explicit sufficient threshold in the frozen existence investigation. It is not numerically verified for the unspecified experiment. No additional coefficient hypothesis below is asserted to follow from it.

## 2. Established coefficient and solution class

The existence investigation and its independent audit prove, for the active base,
\[
y_b\in H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)\cap H^1_0(I))
\cap C([0,T];H^1_0(I)),\qquad \theta_b=\theta_*+y_b,
\]
\[
\theta_*/2\le\theta_b\le3\theta_*/2,\qquad
w_b,E_b,\theta_b\in L^\infty((0,T)\times I),\qquad Q(y_b)_t\in L^2((0,T)\times I).
\]
One-dimensional Sobolev embedding makes \(y_b,\theta_b\) jointly continuous; the frozen memory representations also give \(w_b\), hence \(S\), jointly continuous on the closed cylinder. Thus \(M_b\in C_{t,x}\cap L^\infty\),
\[
c+d\theta_*/2\le M_b\le c+3d\theta_*/2,\quad
S\in C_{t,x}\cap L^\infty,\quad B\in L^2_{t,x}
\]
with \(B\) explicitly the sum of \(-dQ(y_b)_t\in L^2\) and bounded terms. In fact \(M_b\) inherits \(H^1_tL^2_x\cap L^2_tH^2_x\cap C_tH^1_x\) from \(y_b\). These assertions do not establish \(M_b\in W^{1,\infty}\), \(B\in L^\infty\), time analyticity, or classical traces of \((y_b)_t\). Dividing by \(M_b\) preserves positivity but yields the principal coefficient \(\kappa/M_b\) only in the inherited class, not automatically the \(C^1\) or Lipschitz class required by standard estimates cited below. Also \(B/M_b\in L^2\), not automatically bounded.

The frozen derivative solution satisfies
\[
Y\in\mathcal E_T:=H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x})\subset C_tH^1_{0,x},\qquad P\in H^1_tL^2_x\subset C_tL^2_x.
\]
In one dimension \(Y\in L^\infty_{t,x}\), so \(BY,SP\in L^2_{t,x}\). The equation and all traces have meaning in this class. The established linearized estimate extends the solution map continuously to odd \(L^2\) data, but the frozen question retains the original \(H^2\) topology. Nothing here claims additional regularity of \(Y_t\), \(B_t\), or endpoint traces of \(P\).

## 3. Carleman attempt and the independent memory trace

### 3.1 The parabolic residual cannot be discarded

Write \(\mathcal L_bY=M_bY_t-\kappa Y_{xx}\). On a delayed cylinder \(J\times I\), the exact equation is \(\mathcal L_bY=BY+SP\). In a scalar boundary Carleman inequality for a sufficiently regular principal operator, schematically
\[
\mathcal C_s(Y)\le C\{\mathcal O_s(Y_x(0,\cdot))+
\|e^{s\varphi}(BY+SP)\|^2_{L^2(J\times I)}\}.\tag{2}
\]
This display is a **candidate template**, not an asserted theorem for \(M_b,B\) or \(Y\) in §2. In particular, extension of such an estimate to the actual principal regularity and absorption of \(BY\) with only \(B\in L^2_{t,x}\) remain to be justified; the unweighted product estimate alone does not supply the required uniform weighted absorption. Even if those issues were resolved, zero measured flux would remove only \(\mathcal O_s\), not the unknown \(SP\).

A precise primary boundary estimate and the difference between its hypotheses and (1) are in §4. One cannot assert \(SP=0\) from zero lateral Cauchy data: that is precisely part of what a coupled proof would have to establish.

### 3.2 What an ODE estimate actually yields

Fix any \(t_0\in J\), for example its midpoint. For almost every \(x\), the \(H^1\)-in-time ODE gives, for \(t\in J\),
\[
P(t,x)=e^{-\mu(t-t_0)}P(t_0,x)
+\lambda\beta\int_{t_0}^{t}e^{-\mu(t-s)}Y(s,x)\,ds,\tag{3}
\]
where the oriented integral is valid also for \(t<t_0\). This is independent of any estimate. Let \(\varphi(x,t)\) be a standard two-sided weight maximal at \(t_0\) and nonincreasing away from \(t_0\), for each \(x\). Set \(w_s=e^{s\varphi}\). Since \(w_s(x,t)\le w_s(x,r)\) whenever \(r\) lies between \(t\) and \(t_0\), Cauchy–Schwarz and Fubini yield the rigorous, non-sharp inequality
\[
\|w_sP\|_{L^2(J\times I)}^2
\le C_J\left(\int_I w_s(x,t_0)^2|P(t_0,x)|^2dx
+|\lambda\beta|^2\|w_sY\|_{L^2(J\times I)}^2\right).\tag{4}
\]
Here \(C_J\) is finite, depending on \(\mu\) and \(|J|\), but not on \(s\), \(P\), or \(Y\). Indeed, the exponential factors in (3) are bounded by \(e^{\mu|J|}\), and the triangular Volterra integration is bounded on \(L^2\). The inequality is valid for the actual solution class by the Bochner ODE formula; the integral trace is well defined because \(P(t_0)\in L^2(I)\).

Substitution of (4) into the *hypothetical* scalar estimate (2) might allow the weighted \(Y\) term to be absorbed if an appropriately coercive scalar estimate at the actual coefficients were proved. But it leaves
\[
C\|S\|_\infty^2\int_I e^{2s\varphi(x,t_0)}|P(t_0,x)|^2dx,\tag{5}
\]
an uncontrolled spatial memory trace. Its value is not supplied by the boundary observation, nor is it bounded by the displayed scalar Carleman functional. Setting it to zero would be an **additional assumption**, not a consequence of \(Y_x(0,\cdot)=0\). Taking a time cutoff of \(P\) does not remove it for free: the ODE for \(\chi P\) has \(\chi'P\) on its right. A sharper ODE Carleman bound could improve the \(Y\) coefficient but still needs a treatment of the independent homogeneous ODE solution. The elementary example \(Y=0\), \(P=e^{-\mu(t-t_0)}p(x)\) shows that an ODE-only bound of \(P\) solely by \(Y\), with no trace or observation, is false; this example is **not** asserted to solve the heat equation with the active \(S\).

This calculation does not rule out a more sophisticated coupled argument exploiting \(SP\), coefficient structure, oddness, and lateral data. No such estimate is established here. In particular, a smooth-coefficient formal manipulation, time differentiation of \(B\) or \(S\), and a scalar theorem for the homogeneous equation do not furnish the missing proof in the class of §2.

### 3.3 The delayed interval

Exactly,
\[
P(\delta)=e^{-\mu\delta}h+\lambda\beta\int_0^\delta e^{-\mu(\delta-s)}Y(s)\,ds,\tag{6}
\]
\[
P(t)=e^{-\mu(t-\delta)}P(\delta)+\lambda\beta\int_\delta^t e^{-\mu(t-s)}Y(s)\,ds,\quad t\in J.\tag{7}
\]
A calculation localized to \(J\) must therefore carry both the unknown \(P(\delta)\) and the unknown \(Y(\delta)\). The prior history appears in (6); zero flux on \(J\) does not by itself set either delayed state to zero. In (3)–(5), \(P(t_0)\) is the same unknown state propagated to an interior time. Imposing \(P(\delta)=0\) eliminates the homogeneous term in (7), but is not established by observation and does not by itself eliminate \(Y(\delta)\), nor does it justify the actual-coefficient boundary Carleman estimate. Imposing both delayed states zero trivially yields zero later by forward uniqueness, but is additional information and does not answer (UC). No information before \(\delta\) is inferred from observations after \(\delta\).

## 4. Primary-source theorem and applicability audit

The following statements were inspected in the linked primary texts; paraphrases include the hypotheses relevant to transfer, not all definitions of the cited weights. None is invoked as a proof for (1). “Not applicable directly” is not a claim that an adaptation is impossible. Source checking does not independently certify every proof in these papers.

1. **P. Gaitan, [Theorem 2.2](https://arxiv.org/html/0706.1422#S2.Thmtheorem2)**, *Inverse Conductivity Problem for a Parabolic Equation using a Carleman Estimate with One Observation*. On a bounded \(C^1\) domain, \(n\le3\), over \((t_0,T)\), the paper assumes a positive \(C^4\) spatial weight with nonzero gradient and appropriate normal-derivative sign on the unobserved boundary, and a smooth positive time-independent scalar conductivity \(c(x)\). For zero Dirichlet \(q\in H^1(t_0,T;H^2(\Omega))\), its theorem bounds the squared conjugated-operator norms plus weighted \(s|\nabla q|^2+s^3|q|^2\) terms by the weighted boundary normal derivative on \(\Gamma_0\) **plus** \(\int e^{-2s\eta}|q_t-\nabla\cdot(c\nabla q)|^2\). No independent ODE state occurs. Boundary Cauchy/normal observation can be on part of the boundary. In 1-D an endpoint is a boundary component and the geometric sign choice is plausible, but the theorem's smooth spatial principal coefficient, displayed function class, and scalar residual do not match the active \(\kappa/M_b(x,t)\), \(B\in L^2\), and independently initialized \(P\). **NOT APPLICABLE DIRECTLY.**

2. **P. Albano and D. Tataru, [Theorem 3.1](https://ejde.math.txstate.edu/Volumes/2000/22/albano.pdf)**, *Carleman estimates and boundary observability for a coupled parabolic-hyperbolic system*. For their scalar Dirichlet parabolic equation \(Q\theta=f\) on a smooth bounded domain, with \(C^1\) principal coefficients and bounded measurable lower-order coefficients (H1), and smooth spatial weight with nonzero gradient, their singular-time-weight estimate bounds a weighted anisotropic order-two norm of \(\theta\) by \(\|e^{\tau\psi}f\|_2^2\) plus an explicitly signed weighted boundary normal-derivative integral. Arbitrary heat initial data are allowed; there is no ODE state in this theorem. The paper's full coupled result instead concerns a **wave** coupled to heat and observes normal derivatives of both components under additional pseudoconvex geometry. Neither result supplies a one-endpoint heat-only observation of (1); the scalar residual remains \(BY+SP\), and the actual principal/lower-order regularity is not their H1. **NOT APPLICABLE DIRECTLY.**

3. **D. P. Jha and R. K. George, [Lemma 3.5 and §3](https://arxiv.org/html/2506.22221)**, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, arXiv v2. Their ODE Carleman lemma estimates a weighted ODE state using its residual and a weighted observation of that state on a moving interior region, under the stated moving-weight geometry and zero initial ODE state; their finite exponential realization represents a zero-initial convolution. The accompanying scalar heat estimate is an interior moving-observation estimate, not the present endpoint flux. Their later Corollary 3.14 also explicitly assumes their adjoint unique continuation (Assumption 3.11) and terminal compactness condition (Assumption 3.12), rather than deriving this question from boundary data. The autonomous heat and finite-kernel framework is not the active variable-mass system; independent \(P(\delta)\) and an unobserved ODE component are not covered by the cited lemma. **NOT APPLICABLE DIRECTLY.**

4. **S. Vessella, [§3.2–3.3](https://arxiv.org/html/0710.2192)**, *Quantitative estimates of unique continuation for parabolic equations*. The primary text develops a scalar parabolic Carleman estimate (Theorem 3.2.3) and interior/boundary two-sphere one-cylinder estimates under its explicit ellipticity and regularity conditions; its introduction describes scalar strong continuation for a principal coefficient Lipschitz in parabolic distance and bounded lower-order coefficients. These results concern scalar homogeneous equations/controlled scalar residuals, not an independently initialized ODE or its distributed source. The present principal coefficient is not established in that Lipschitz class and \(B\) is not established bounded. A boundary scalar continuation theorem does not absorb \(SP\). **NOT APPLICABLE DIRECTLY.**

5. **[A unified Carleman approach to inverse problems for coupled parabolic and hyperbolic-ODE equations, §2, Lemma 2.2 and Theorem 2.3](https://arxiv.org/html/2610.26157)**. The inspected preprint treats a Kelvin–Voigt equation factored into a heat operator and a time ODE on a smooth bounded domain in dimensions 2 or 3. Its centered weighted ODE estimate includes a **fixed-time trace**, and its coupled estimate uses an **interior observation** plus such a trace; the inverse problem additionally has a global Cauchy snapshot. This is a useful warning against silently dropping the homogeneous ODE contribution. It neither treats the active coefficients nor gives an endpoint-flux-only result; it does not provide an estimate for an independently unknown \(P(\delta)\) with no added trace. **NOT APPLICABLE DIRECTLY.**

6. **Green–Liu, [Theorems 1.1–1.3](https://arxiv.org/html/2004.10842)**, *Source reconstruction and stability via boundary control of abstract viscoelastic systems*. Under the paper's self-adjoint compact-resolvent wave operator and memory-free observability hypotheses, \(M\in H^2\), \(T>T_0\), and for the source result \(\sigma\in C^1\), \(\sigma(0)\ne0\) and zero initial wave data, the authors give source reconstruction/stability from a time-differentiable observation. This accommodates an unknown spatial source, but in a second-order wave–memory equation with a known temporal factor and its own observation assumptions. It is not a boundary Cauchy theorem for (1), does not model an independent initial ODE state driven by \(Y\), and does not match the rough nonautonomous coefficients or delayed \(L^2\) flux. **NOT APPLICABLE DIRECTLY.**

The sources collectively cover boundary parabolic estimates, coupled parabolic–ODE estimates, distributed source reconstruction, and coefficient regularity, but no inspected result supplies every hypothesis of the frozen question. Some publications found by search were inaccessible or had only abstracts accessible; no theorem is inferred from those abstracts. The search does not prove that no applicable theorem exists elsewhere.

## 5. Counterexample and qualitative versus quantitative obstruction

A counterexample to (UC) would require a **nonzero temperature on \(J\times I\)** together with an odd \(h\in H^2(I)\), the actual base coefficients, equations (1), all original time and boundary conditions, and \(Y_x(0,t)=0\) a.e. on \(J\). Merely choosing arbitrary smooth \(Y\) supported away from the endpoint and declaring its heat residual to be a source is insufficient: the same source must equal \(SP\) with (3), (6), and the fixed prescribed base. In particular, even solving the ODE for an arbitrary such \(Y\) does not make its heat residual equal \(SP\). No such construction was obtained. Nor is a hypothetical pair with \(Y=0\) but \(P\ne0\) on \(J\) a counterexample to the stated implication, whose conclusion concerns \(Y\).

The earlier audit proves compactness of \(h\mapsto Y_x(0,\cdot)|_J\) and constructs unit odd directions with flux tending to zero while their memory norm remains nonzero. Hence uniform strong \(L^2\) memory observability fails and **approximate** invisibility occurs. This does not produce exact zero flux for any nonzero direction, does not show nonzero \(Y\) with zero flux, and cannot decide qualitative (UC). Conversely, qualitative (UC) would not imply the failed uniform memory estimate. None of the coefficient-class or ODE-trace gaps is itself a counterexample.

## 6. Decision and precise open points

**NOT ESTABLISHED.** Under the existing sufficient smallness condition, neither the boundary implication (UC) nor its negation has been shown for the actual nonzero-loading base. The concrete remaining tasks are: (i) a valid endpoint scalar estimate at the established variable-mass and \(L^2\) lower-order regularity, or a separately proved regularity upgrade; (ii) a coupled mechanism that controls or eliminates the independent memory trace in (5) from exactly the observed boundary data; (iii) treatment of the unknown delayed states and odd initial-data restriction without assuming away their prehistory; or (iv) construction of an exact active-system counterexample meeting all conditions in §5. The additional assumptions in the cited source theorems and the illustrative zero delayed-state assumptions do not follow from the established existence theory. No later-time-to-earlier-time property, full kernel conclusion, even-channel result, or nonlinear inverse conclusion is claimed.
