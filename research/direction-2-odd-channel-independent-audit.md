# Independent mathematical audit of the odd-channel investigation

**Date:** 1 November 2026

**Overall result: AUDIT PASSED WITH CORRECTIONS.** The active parabolic–memory reduction, compactness obstruction and conditional injectivity implication survive independent recalculation under their stated hypotheses. In particular, the compactness obstruction is **mathematically valid**. The corrections concern precision: the Volterra convolution is not itself compact on space–time \(L^2\); compactness in the proof is the composition with the compact temperature solution map. The report's modal language should say active coefficients **can** couple modes rather than treating a specific nonzero off-diagonal entry as proved. Neither qualification invalidates the main theorem. Neither injectivity nor a nonzero exact kernel is established.

The audit independently recalculates the mathematical steps and checks the sources named in the report, but is an Arena single-agent audit, not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. There is no analysis of the even channel, nonlinear inverse problem, or new continuum theory here.

## 1. Claim-by-claim verdict

The audited file is `direction-2-odd-channel-kernel-investigation.md`. Its equation numbers are identified as “report” numbers where needed. The explicit data hypothesis \(0<q<s_*\) is understood in the fixed numerical units of the existence investigation and is not numerically verified for the unspecified physical experiment.

| Claim | Verdict | Reason / limitation |
|---|---|---|
| Active odd reduction and signs of \(M_b,B,S\) | **PASS** | Direct substitution yields all coefficients and the exact source \(SP\); §2. |
| ODE formula, scalar Volterra equation, equivalence and initial traces | **PASS** | The Bochner integral solves the ODE with initial \(h\), and all products are meaningful in the stated class; §2. |
| Active base and linearized solution regularity | **PASS** | Under the previously established strict threshold; traces are Sobolev traces, not corner-classical derivatives. |
| \(L^2\)-input estimate and odd \(L^2\) extension | **PASS WITH CORRECTION** | Correct; §3 supplies the missing explicit parameter-forcing estimate and distinguishes a linearized extension from nonlinear admissibility. |
| Endpoint-flux boundedness and compactness | **PASS** | The precise compact embedding and derivative trace at exponent \(s>3/2\) are given in §4. |
| Compactness of \(K\) in the memory formula | **PASS WITH CORRECTION** | \(K=\lambda\beta V\circ\mathcal Y\) is compact; \(V\) alone is bounded but generally **not** compact on space–time \(L^2\). |
| Failure of the full \(L^2\) memory-state observability inequality | **PASS** | A normalized weakly null odd sine sequence gives a positive limiting memory norm and vanishing flux. No bounded \(H^2\) norm is required for a uniform all-directions inequality. |
| Approximate invisibility versus exact kernel | **PASS** | Approximate invisible unit inputs do not give an exact nonzero element of the kernel. |
| Additional coefficient bound \(q<\min\{s_*,q_{\rm nd}\}\) | **PASS** | The stated lower bound holds for either sign of \(b\), with constants in the fixed unit convention. It is an additional unverified condition. |
| Injectivity assuming (UC), (BU), and the extra bound | **PASS** | The implication is logically valid; (UC), (BU) and the extra numerical bound are additional unproved assumptions, not established properties of the frozen experiment. |
| Literature statements and transfer | **PASS WITH CORRECTION** | The cited primary statements checked in §6 do not directly apply; a couple of scope qualifications are made there. This is not an exhaustive literature search. |
| Triviality or nontriviality of the actual odd kernel | **NOT ESTABLISHED** | Neither conclusion follows from the compactness result or the conditional theorem. |

## 2. Audit A — independent reduction and equivalence

Let \(I=(0,L)\), \(J=(\delta,T)\), \(T=10/\lambda\), \(\delta=T/100\), \(g(t)=g_*\sin^2(\pi t/T)\), \(g_*\ne0\). The base trajectory is the prescribed **nonzero-loading** solution with \(z_0=0\); it is not replaced by an equilibrium. As in the five frozen sources, set

\[
D=a+k,\quad r=k/D,\quad \alpha=a/D,\quad \beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D,\quad Qf=f-\bar f,
\]

with \(a,k,c,\kappa,\lambda,L,A_0,\theta_*,M>0\) and \(b\ne0\). The audited odd equation is

\[
\begin{gathered}
P_t=-\mu P+\lambda\beta Y,\quad P(\cdot,0)=h,\quad W=-\alpha P+\beta Y,\\
(c+d\theta_b)Y_t-\kappa Y_{xx}
=-dYQ(y_b)_t-bYE_b-br\theta_bP_t+2k\lambda w_bW,\\
Y(\cdot,0)=0,\quad Y(0,t)=Y(L,t)=0.\tag{2.1}
\end{gathered}
\]

Oddness makes \(QY=Y\) and \(QP=P\), but does **not** imply \(Q(y_b)_t=0\). Substituting \(P_t\) and \(W\) yields the coefficient of \(Y\)

\[
B=-dQ(y_b)_t-bE_b-br\lambda\beta\theta_b+2k\lambda\beta w_b
\]

and the coefficient of \(P\)

\[
S=br\mu\theta_b-2k\lambda\alpha w_b
=\lambda\alpha(br\theta_b-2kw_b).
\]

Thus, with \(M_b=c+d\theta_b\), the report's reduction is exactly

\[
M_bY_t-\kappa Y_{xx}=BY+SP,\qquad P_t=-\mu P+\lambda\beta Y.\tag{2.2}
\]

Every active term is retained. In particular, the coefficient of \(P\) has a **minus** contribution from the linearized quadratic heat source and the coefficient of \(Y\) has the \(-dQ(y_b)_t\) term. No sign assumption on \(b\) is needed.

For \(h\in H^2_o(I)\), or for the \(L^2_o\) linearized extension justified below, \(P\in H^1(0,T;L^2)\); solving the Bochner-valued ODE gives

\[
P(t)=e^{-\mu t}h+\lambda\beta\int_0^t e^{-\mu(t-s)}Y(s)\,ds\quad\text{in }L^2(I).\tag{2.3}
\]

The integral is in \(H^1_tL^2_x\), has zero time trace at zero, and the first term has initial trace \(h\). Substitution gives

\[
M_bY_t-\kappa Y_{xx}
=BY+S e^{-\mu t}h+\lambda\beta S(t,x)\int_0^t e^{-\mu(t-s)}Y(s,x)\,ds.\tag{2.4}
\]

Conversely, if \(Y\) in the specified \(\mathcal E_T\) space satisfies (2.4) with the stated initial/boundary data, (2.3) defines \(P\in H^1_tL^2_x\) with \(P(0)=h\); differentiating the Bochner integral recovers the ODE and hence (2.1). The terms \(BY\) and \(SP\) lie in \(L^2_{t,x}\), as checked below. Therefore equivalence holds in the stated weak/strong-temperature solution class, without assuming extra initial or boundary derivatives. All these claims **PASS**.

## 3. Audit B — solution spaces, estimate and extension

### 3.1 Base and solution regularity

Assume the existing sufficient hypothesis \(0<q=|g_*|/L<s_*\). The earlier existence theorem and its independent audit give the unique positive active base and an \(H^2\) neighborhood of actual weak-admissible data. For the active base,

\[
y_b\in H^1_tL^2_x\cap L^2_t(H^2_x\cap H^1_{0,x})\cap C_tH^1_{0,x},
\quad \theta_b,w_b,E_b\in L^\infty_{t,x},\quad Q(y_b)_t\in L^2_{t,x}.
\]

Hence \(M_b,S\in L^\infty\), \(M_b\ge c+d\theta_*/2>0\), and \(B\in L^2_{t,x}\) as the sum of an \(L^2\) term and bounded terms on a finite cylinder. There is no basis here for assuming \(B\in L^\infty\), time analyticity, or a classical endpoint trace of \((y_b)_t\).

The odd linearization from the parity audit has

\[
Y\in\mathcal E_T:=H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)\cap H^1_0(I)),\qquad P\in H^1(0,T;L^2(I)).\tag{3.1}
\]

The initial value of \(Y\) is zero and of \(P\) is \(h\). Standard time-trace theory gives \(Y\in C_tH^1_0\), and \(P\in C_tL^2\). In 1-D \(\mathcal E_T\hookrightarrow L^\infty_{t,x}\), so

\[
\|BY\|_{L^2_{t,x}}\le\|B\|_{L^2_{t,x}}\|Y\|_{L^\infty_{t,x}},\qquad
\|SP\|_{L^2_{t,x}}\le\|S\|_\infty\|P\|_{L^2_{t,x}}.
\]

The claimed solution spaces and the treatment of coefficients **PASS**.

### 3.2 Independent justification of the \(L^2\)-input estimate

The audited report invokes the derivative of the earlier contraction map. The following explicit calculation shows why the input forcing is controlled in \(L^2\), even though the original nonlinear data topology is \(H^2\).

Let \(\mathcal L\) denote the temperature part of the reference linear heat–memory solver in (3.2)–(3.3) of the existence investigation. It is bounded from \(L^2_{t,x}\times L^2_x\) to \(\mathcal E_T\). At fixed trial temperature \(y_b\), for an odd input direction \(h\), the variations of the input memory representations are

\[
\delta p=e^{-\mu t}h,\quad \delta v=0,\quad
\delta E=-r\mu e^{-\mu t}h,\quad \delta w=-\alpha e^{-\mu t}h.
\]

Differentiating the nonlinear forcing \(N=-dyQy_t-byE+k\lambda w^2\) at fixed \(y_b\) produces

\[
\delta_hN=br\mu y_b e^{-\mu t}h-2k\lambda\alpha w_b e^{-\mu t}h.\tag{3.2}
\]

The two coefficients are bounded, so \(\|\delta_hN\|_{L^2_{t,x}}\le C\|h\|_2\). The reference solver also receives \(p_0=h\), so its input derivative \(G h=\mathcal L(\delta_hN,h)\) obeys \(\|Gh\|_{\mathcal E_T}\le C\|h\|_2\).

Choose a common fixed-point ball for the data with strict threshold, as in §8 of `direction-2-parity-decomposition-independent-audit.md`. The derivative \(A=D_y\Phi\) at the base has norm at most the common contraction constant \(\gamma\le1/2\); the base lies in the interior of that common ball. The implicit derivative satisfies

\[
(I-A)Y=Gh,\qquad \|Y\|_{\mathcal E_T}\le(1-\gamma)^{-1}C\|h\|_2.\tag{3.3}
\]

From (2.3), convolution on finite time and the ODE give \(\|P\|_{H^1_tL^2_x}\le C(\|h\|_2+\|Y\|_{L^2_{t,x}})\). Consequently

\[
\|Y\|_{\mathcal E_T}+\|P\|_{H^1_tL^2_x}\le C\|h\|_{L^2(I)}.\tag{3.4}
\]

This is the precise justification of the report's estimate, initially for \(h\in X_o=H^2_o\). The constant may depend on the fixed active base, coefficients, interval and contraction margin, but not on \(h\).

Smooth odd functions, for example odd projections of \(C^\infty\) functions, are dense in \(H_o=L^2_o(I)\). Thus (3.4) extends the **linearized** solution operator uniquely to \(H_o\). The equation, oddness and initial conditions pass to the limit: \(Y\to Y_*\) in \(\mathcal E_T\), hence in \(L^\infty_{t,x}\), and \(P\to P_*\) in \(H^1_tL^2_x\). In particular, \(B Y_n\to B Y_*\) in \(L^2\). This does **not** assert nonlinear forward existence or membership in the actual weak-admissible \(H^2\)-ball for arbitrary \(L^2\) data. The extension is legitimate for the estimates and compactness proof.

For a.e. \(t\), \(Y(t)\in H^2(I)\), and the bounded 1-D trace \(H^2(I)\ni f\mapsto f'(0)\in\mathbb R\) gives

\[
\|Y_x(0,\cdot)\|_{L^2(0,T)}\le C\|Y\|_{L^2(0,T;H^2(I))}.
\]

Therefore \(\mathcal T_o h=2A_0\kappa Y_x(0,\cdot)|_J\) is a bounded \(H^2_o\to L^2(J)\) map and also has a bounded extension \(H_o\to L^2(J)\). These statements **PASS WITH CORRECTION** in the sense of the explicit justifications and scope above; no erroneous estimate was found.

## 4. Audit C — compactness and observability obstruction

### 4.1 Exact compact embeddings and trace

Choose any fixed \(s\in(3/2,2)\), for example \(s=7/4\). On the bounded interval,

\[
H^2(I)\hookrightarrow\hookrightarrow H^s(I)\hookrightarrow L^2(I).
\]

With \(Y\) bounded in \(L^2(0,T;H^2(I))\) and \(Y_t\) bounded in \(L^2(0,T;L^2(I))\), the Aubin–Lions compactness theorem yields

\[
\mathcal E_T\hookrightarrow\hookrightarrow L^2(0,T;H^s(I)).\tag{4.1}
\]

The trace \(f\mapsto f'(0)\) is continuous on \(H^s(I)\) exactly because \(s>3/2\). Thus convergence in the right-hand space implies convergence of \(Y_x(0,\cdot)\) in \(L^2(0,T)\). Restriction to \(J\) and multiplication by \(2A_0\kappa\) are bounded. Combining (3.4) and (4.1) proves

\[
\mathcal T_o:H_o\to L^2(J)\quad\text{is compact}.\tag{4.2}
\]

The lower-order coefficient \(B\) is not required to multiply \(H^s\) compactly in this step; it has already been controlled in obtaining the solution bound. Nothing here assumes \(B\in L^\infty\).

### 4.2 The compact memory correction — precise qualification

Let \(\mathcal Y:H_o\to L^2((0,T)\times I)\) denote the temperature solution operator. The embedding (4.1), followed by continuous inclusion into \(L^2_{t,x}\), shows \(\mathcal Y\) is compact. Define

\[
(Vf)(t,x)=\int_0^t e^{-\mu(t-s)}f(s,x)\,ds.
\]

Young's inequality (or Cauchy–Schwarz on the finite time interval) gives boundedness of \(V\) on \(L^2((0,T)\times I)\). Restriction to \(J'\times I\) is bounded; therefore

\[
K=\lambda\beta\,\operatorname{Res}_{J'}\,V\mathcal Y:
H_o\to L^2(J'\times I)\quad\text{is compact},\tag{4.3}
\]

and (2.3) yields \(P[h]=e^{-\mu t}h+Kh\) on \(J'\).

**Precision correction:** \(V\) alone is generally **not compact** on space–time \(L^2\): take \(f_n(t,x)=f(t)e_n(x)\) for a fixed nonzero \(f\) and an orthonormal spatial family \(e_n\); then \(Vf_n=(Vf)(t)e_n(x)\) has no strongly convergent subsequence if \(Vf\ne0\). The audited report in fact uses the bounded-operator-after-compact-operator argument, so its claim about \(K\) is valid; it should not be paraphrased as compactness of \(V\) itself.

### 4.3 Independent contradiction proof — PASS

Let \(J'\subseteq J\) be any positive-length interval and define

\[
h_n(x)=\sqrt{2/L}\sin(2n\pi x/L),\quad n\ge1.
\]

Each \(h_n\in H^2_o(I)\), \(Rh_n=-h_n\), and \(\{h_n\}\) is orthonormal in the Hilbert space \(H_o\). Hence \(h_n\rightharpoonup0\) in \(H_o\). Compact operators take weakly convergent sequences to strongly convergent sequences, so by (4.2)–(4.3)

\[
\|\mathcal T_o h_n\|_{L^2(J)}\to0,\qquad
\|Kh_n\|_{L^2(J'\times I)}\to0.
\]

At the same time,

\[
\|e^{-\mu t}h_n\|_{L^2(J'\times I)}
=\left(\int_{J'}e^{-2\mu t}\,dt\right)^{1/2}=:c_{J'}>0.
\]

By the reverse triangle inequality, \(\|P[h_n]\|_{L^2(J'\times I)}\to c_{J'}\). Thus there cannot be one finite \(C\) for which

\[
\|P[h]\|_{L^2(J'\times I)}\le C\|\mathcal T_o h\|_{L^2(J)}
\quad\text{for every }h\in H^2_o(I).\tag{4.4}
\]

Likewise \(\|h\|_2\le C\|\mathcal T_o h\|\) cannot hold uniformly, since \(\|h_n\|_2=1\). This is the claim in report §5.1, and **the compactness obstruction is valid**.

The \(H^2\) norms of \(h_n\) grow. That is not a flaw: (4.4) was asserted to have the same constant for **all** \(H^2_o\) directions, not just a bounded \(H^2\) ball with fixed \(L^2\) normalization. Because the system and both sides of (4.4) are linear/homogeneous, even a constant claimed for all inputs in any fixed \(H^2\)-ball would extend to every direction by scaling. This does not rule out an estimate with an additive term, a priori \(H^2\)-dependent constant, nonlinear modulus, weaker input norm, stronger output norm, or additional observations.

The sequence proves **approximate invisibility** (unit \(L^2\) inputs and outputs tending to zero). It does not yield \(\mathcal T_o h_n=0\) for any \(n\), does not construct an exact kernel element, and does not disprove injectivity. Compact injective operators can lack a uniform lower bound. Nor does the failed strong observability estimate disprove a purely qualitative unique-continuation implication.

## 5. Audit D — nondegeneracy and conditional theorem

### 5.1 Numerical sufficient condition

Using the existence investigation's explicit fixed-unit constants \(W_s,W_R,C_B\), define \(C_w=W_s+2C_BW_R>0\) and \(q_{\rm nd}=|b|r\theta_*/(8kC_w)>0\). Under \(0<q<s_*\), the active base has \(\|y_b\|_{\mathcal E_T}\le2C_Bq\); estimate (5.2) of that investigation, applied at zero initial memory, yields

\[
\|w_b\|_\infty\le W_sq+W_R\|y_b\|_{\mathcal E_T}\le C_wq.
\]

If in addition \(q<q_{\rm nd}\), the previous positivity bound gives \(\theta_b\ge\theta_*/2\), and

\[
|br\theta_b-2kw_b|\ge |b|r\theta_*/2-2kC_wq
>|b|r\theta_*/4.
\]

Therefore \(|S|>\lambda\alpha|b|r\theta_*/4\) a.e., for either sign of \(b\). The constants and threshold are sufficient and fixed-unit dependent, not a verified numerical property of the supplied experiment. This algebra **PASSES**.

### 5.2 Logical chain

Assume all of the following for the actual active odd system:

- \(0<q<\min\{s_*,q_{\rm nd}\}\);
- **(UC)** for every odd \(h\in H^2\), \(Y_x(0,\cdot)=0\) in \(L^2(J)\) implies \(Y=0\) in \(L^2(J\times I)\);
- **(BU)** for every such generated solution, \(Y(\delta)=P(\delta)=0\) in \(L^2(I)\) implies \(h=0\).

If \(\mathcal T_o h=0\), since \(A_0\kappa>0\) its endpoint derivative is zero, and (UC) gives \(Y=0\) on \(J\times I\). Because \(Y\in H^1_tL^2_x\cap L^2_tH^2_x\), both \(Y_t\) and \(Y_{xx}\) vanish there as weak derivatives. Equation (2.2) then yields \(SP=0\) a.e. The positive lower bound on \(|S|\) gives \(P=0\) there. The continuous \(L^2\) time representatives of \(Y,P\) therefore satisfy \(Y(\delta)=P(\delta)=0\). Applying (BU) yields \(h=0\).

This is a valid **conditional** implication. (BU) is a property of the coupled evolution with the restricted initial states \((Y(0),P(0))=(0,h)\), not an already-proved scalar heat backward-uniqueness theorem; it may be weaker than backward injectivity for arbitrary two-component data. The exact relation

\[
P(\delta)=e^{-\mu\delta}h+\lambda\beta\int_0^\delta e^{-\mu(\delta-s)}Y(s)\,ds
\]

shows why the pre-observation history cannot simply be discarded. Neither (UC) nor (BU) is established from the current coefficients, regularity and observations. The theorem therefore **does not prove unconditional odd injectivity**, and its verdict **PASSES** only as a conditional theorem.

## 6. Audit E — existing primary-source transfer claims

Only the already cited sources were checked; no broad new search was performed. Primary pages/theorem statements were accessible in this audit. “Does not directly apply” means the required mapping of hypotheses has not been supplied, not that a future adaptation is impossible.

| Existing citation and inspected statement | Verification and transfer |
|---|---|
| **Green–Liu**, [arXiv:2004.10842](https://arxiv.org/html/2004.10842), Theorems 1.1–1.3 and conditions (A),(B), DOI [10.1080/00036811.2021.1877682](https://doi.org/10.1080/00036811.2021.1877682). | **PASS.** Theorem 1.2 assumes the stated abstract self-adjoint second-order operator and memory-free observability, \(M\in H^2\), \(T>T_0\), \(\sigma\in C^1\), \(\sigma(0)\ne0\), zero initial wave data; it estimates the spatial source from an \(H^1_t\) observation. Theorem 1.3 gives the reconstruction expansion. These hypotheses do not establish the active non-autonomous parabolic–ODE result or its delayed \(L^2\) endpoint observation. |
| **Avdonin–Ivanov–Wang**, [arXiv:1612.02129](https://arxiv.org/html/1612.02129), model, assumption (5), Theorem 4, DOI [10.3934/ipi.2019002](https://doi.org/10.3934/ipi.2019002). | **PASS.** The paper's Gurtin–Pipkin equation has zero initial temperature and a Dirichlet-to-Neumann response operator. Under the paper's transform asymptotics and \(T_*=Ta\le L\), Theorem 4 relates equality of response operators to equality of temporal kernels on the stated interval. This is not a theorem for the independent initial \(P\), single prescribed experiment or active coefficients. |
| **Ma–Wang–Zhang**, [arXiv:2411.14382](https://arxiv.org/html/2411.14382), definitions and Theorem 1.7. | **PASS WITH CLARIFICATION.** For \(M\in C^2\), the theorem assumes backward uniqueness at selected times and shows the geometric observation condition implies their two-sided \(\mathcal H^{-4}\) estimate, which implies a weak geometric condition. Their observations are \(L^2\) restrictions to spatial sets at selected instants; sets are relatively open in \(\bar\Omega\) and may touch the boundary, but are not endpoint Neumann flux traces. Unknown data are initial temperature, not an independent initial memory field. |
| **Green–Liu–Mitkovski**, [author PDF](https://www.math.wustl.edu/~awgreen/files/papers/visco-control-siamjco-2020.pdf), Proposition 2.2 and Theorem 3.1, DOI [10.1137/18M1180736](https://doi.org/10.1137/18M1180736). | **PASS.** The primary PDF was accessible in this audit. Theorem 3.1 gives the Riesz property of their wave-memory boundary modes under their \(C^3\) domain/geometric subset, \(M\in H^2\), and \(T>2R\); Proposition 2.2 connects the lower Riesz estimate to wave boundary observability. The autonomous wave system and wave energy state are not (2.1), so no direct odd parabolic–ODE conclusion follows. |
| **Jha–George**, [arXiv:2506.22221](https://arxiv.org/html/2506.22221), §3 Lemmas 3.4–3.6. | **PASS WITH CLARIFICATION.** The primary text states estimates under its moving-control/weight and delay assumptions, including an interior observation and history remainder; its ODE lemma is for zero initial ODE data, and its realization lemma represents a zero-initial convolution. This does not establish either (UC) or (BU) for fixed endpoint heat flux and independent \(P(0)=h\). This audit checks the lemma statements and hypothesis mismatch, not an independent verification of the entire preprint's proofs. |
| **P. Gaitan**, [arXiv:0706.1422](https://arxiv.org/html/0706.1422), Theorem 2.2. | **PASS.** The scalar parabolic Carleman estimate includes both the boundary normal trace and the weighted PDE residual on its right side under its regularity/weight hypotheses. For (2.2) the residual contains the unknown \(SP\); dropping it is not justified by this theorem. |

None of these inspected statements directly proves the endpoint delayed observability or backward uniqueness of the active coupled system at its established coefficient regularity. No blanket claim about all literature, novelty, or inapplicability of every possible adaptation is made.

## 7. Final decision and scope

The central theorem that a uniform full-\(L^2\) memory-state estimate by the frozen delayed endpoint flux is impossible is **valid**, as independently proved in §4. The same reasoning proves approximate invisibility and the absence of a uniform \(L^2\)-input lower bound. It does **not** decide the kernel. The conditional theorem in §5 is valid only with its additional, presently unproved assumptions; the sufficient smallness thresholds themselves have not been checked for numerical experimental values.

**Overall classification: AUDIT PASSED WITH CORRECTIONS.**
