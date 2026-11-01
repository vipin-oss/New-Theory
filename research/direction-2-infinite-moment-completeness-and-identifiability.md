# Infinite moment completeness and identifiability of the active system

**Final verdict: STABILITY OBSTRUCTION PROVED.** Conditional on the inherited actual-base and forced-forward hypotheses, the observation operator belongs to every Schatten class \(\mathcal S_p\), \(p>2/3\), and its singular values obey \(s_n(\mathcal T)=O(n^{-3/2+\varepsilon})\) for every \(\varepsilon>0\). On any nontrivial \(H^2\)-bounded odd class, no uniform \(L^2\)-recovery Hölder estimate with exponent greater than \(4/7\) can hold. These results do **not** settle actual injectivity, actual minimality, the exact kernel, or the augmented Gram criterion. They apply to the linearized operator, not automatically to nonlinear identification.

The proposed moment criterion is not ruled out by high-frequency collinearity: §5 gives an injective abstract example satisfying it and a noninjective abstract example with the *same* column rate and invertible every finite augmented Gram. The examples are not physical systems. Section 3 proves the exact distance/Schur formula and distinguishes the augmented family's inevitable nonminimality from minimality of the actual columns. Section 6 supplies an improved actual control error criterion that can succeed when the earlier absolute tail bound fails, but no actual controls satisfying it are established. Parameterized diagnostic code and **abstract-only** numerical checks are included; no physical material values or actual coefficient data were invented.

All results for the actual operator remain conditional on inherited base existence, positivity, coefficient regularity and forced-forward estimates, not numerically verified for the specified experiment. Arena's recalculation is not independent human certification. Dr. Vipin Gupta is Principal Researcher and final decision-maker, ChatGPT the designated Independent Scientific Supervisor and Auditor, Arena the Research Scholar / Builder / Literature Investigator. No new continuum theory, manuscript, priority or novelty is claimed.

## 1. Independent audit of the immediately preceding report

The preceding committed report, its high-frequency derivation and the independent transposition/regularity audit were inspected. The following classifications concern their exact statements, not the unsolved inverse problem.

| Claim in preceding report | Audit | Verification and qualification |
|---|---|---|
| (1)–(3), actual base, odd coefficients and observation | **CORRECT UNDER ADDITIONAL HYPOTHESES** | Substitution of \(P_t=\gamma Y-\mu P\) and \(W=-\alpha P+\beta Y\) gives \(M=c+d\theta_b\), \(S=\lambda\alpha(br\theta_b-2kw_b)\), \(B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b\); odd parity eliminates mean terms. Requires the inherited actual base and linear forward theorem. |
| Global sign regime (4) | **CORRECT UNDER ADDITIONAL HYPOTHESES** | If \(\|y_b\|_\infty\le C_yq\), \(\|w_b\|_\infty\le C_wq\) with constants valid uniformly on the stated small-load ball, the triangle inequality proves the displayed strict positive lower bound for \(\operatorname{sgn}(b)S\). Constants and numerical regime are not verified for the experiment. |
| Single separable sine-mode exclusion | **CORRECT UNDER ADDITIONAL HYPOTHESES** | Sign regime \(|S|\ge c_0\), strong traces and a.e. Fubini permit choosing an interior point with time-integrable coefficients. Vanishing flux gives \(\eta=0\) on \(J\); then \(Sp=0\), hence \(p=0\) there, and the two-dimensional ODE has backward uniqueness. It excludes only the separable ansatz, not general superpositions. |
| \(D_\delta=e^{-\mu\delta}I+K_\delta\), compactness and Fredholm index zero | **CORRECT UNDER ADDITIONAL HYPOTHESES** | Strong bound \(Y\in L^2_tH^2_x\) puts \(K_\delta h\) in \(H^2\cap H^1_0\), compact into \(H\); time traces define the state. The Neumann smallness bound is sufficient, unverified, and concerns memory snapshot—not boundary observability. |
| Remainder tail and approximation numbers | **CORRECT UNDER ADDITIONAL HYPOTHESES** | Square-summing the audited \(\rho_n\) gives \(\|R(I-P_N)\|\le C_\eta N^{-1+\eta}\); approximating \(\mathcal T\) by rank \(N+1\) gives \(s_{N+2}\) bounded by this error. A stronger result is proved in §7. |
| Neighboring-mode cancellation | **CORRECT UNDER ADDITIONAL HYPOTHESES** | \(\phi_n-(q_{n+1}/q_n)\phi_{n+1}\in\ker\Lambda\); the common leading profile cancels exactly, while the remainder gives \(O(q_n^{-3/2+\eta})\). It is only approximate invisibility. |
| Rank-one comparison obstruction | **CORRECT** | The modified operator preserves finitely many actual columns and has an exact smooth kernel vector. It is an abstract operator, not an actual coefficient perturbation or physical counterexample. |
| Augmented moment criterion | **CORRECT UNDER ADDITIONAL HYPOTHESES** | Positive finite augmented Gram and the stated inverse-Gram/tail limit imply \(\mathcal T^*f_{n,N}\to\phi_n\). Neither assumption is established for the actual system. |
| Primary literature table | **CORRECT, LIMITED SCOPE** | The cited statements checked in §10 are applicable only under their listed assumptions; this is not an exhaustive literature or novelty audit. |

No fatal error was found in those claims. The phrase “structural obstruction” in the previous report is correctly limited to abstract finite-data/absolute-norm perturbations; it is not an actual non-injectivity theorem.

## 2. Actual setting and the audited expansion

Let \(I=(0,L)\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), \(H=L^2_o(I)\), \(X=H^2(I)\cap H\), \(Z=L^2(J)\). The base is generated by the prescribed nonzero displacement \(g_*\sin^2(\pi t/T)\), not independently chosen frozen coefficients. With \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(d=b^2/D\), the base-dependent coefficients are
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{1}
\]
The actual odd linearized state obeys
\[
MY_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\ P(\cdot,0)=h,\ Y|_{\partial I}=0,\quad
\mathcal Th=2A_0\kappa Y_x(0,\cdot)|_J. \tag{2}
\]
No endpoint condition is imposed on \(h\) or \(P\). Assume the inherited \(M>0\), even coefficients, \(B\in L^2\), \(S\in C_tH^1_x\cap H^1_tL^2_x\cap L^2_tH^2_x\), and the strong solution and trace estimates described in the audit. These are not verified from numerical material data. The original small-load hypothesis is likewise unverified.

For \(q_n=2\pi n/L\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), define \(k_n=\mathcal T\phi_n\) and \(a=a_J=2A_0\sqrt{2/L}e^{-\mu t}S(t,0)\). The prior actual-system derivation proves, under the above hypotheses,
\[
k_n=\frac a{q_n}+\rho_n,\qquad
\|\rho_n\|_Z\le C_\eta q_n^{-3/2+\eta}\quad(0<\eta<1/2). \tag{3}
\]
Let \(g=\sum\phi_n/q_n\in H\), \(\Lambda h=(h,g)\), \(H_0=g^\perp\), and \(Rh=\sum h_n\rho_n\). Then \(\mathcal T=a\Lambda+R\) exactly. All subsequent actual-system conclusions are conditional on (3) and these inherited hypotheses.

## 3. Augmented Gram: exact Schur complement, singular case, and limiting spans

For fixed \(N\ge n\), let
\[
K_N(c_1,\ldots,c_N,c_*)=\sum_{j=1}^Nc_jk_j+c_*a,\quad G_N=K_N^*K_N,
\quad V_{n,N}=\operatorname{span}\{a,k_j:j\le N,j\ne n\}. \tag{4}
\]
Put \(d_{n,N}=\operatorname{dist}(k_n,V_{n,N})\), \(r_{n,N}=k_n-P_{V_{n,N}}k_n\). If \(G_N\) is invertible, the other columns are independent and the scalar Schur complement is
\[
\|k_n\|^2-g^*G_{-n}^{-1}g=\|r_{n,N}\|^2=d_{n,N}^2,
\qquad (G_N^{-1})_{nn}=d_{n,N}^{-2}. \tag{5}
\]
Here \(G_{-n}\) is the Gram matrix of the other \(N\) vectors and \(g\) their inner products with \(k_n\). To verify (5), the orthogonal projection has those normal-equation coefficients; block elimination yields the inverse diagonal. The minimum-norm control satisfying \((k_j,f)=\delta_{jn}\) for \(j\le N\), \((a,f)=0\), is
\[
f_{n,N}=r_{n,N}/d_{n,N}^2,\qquad \|f_{n,N}\|=1/d_{n,N}. \tag{6}
\]
Every feasible control differs from it by a vector orthogonal to the whole augmented span.

**Singular-Gram case.** Formula (5) with \(G_N^{-1}\) is undefined if the Gram is singular. Nevertheless (6) and the distance interpretation remain valid whenever \(d_{n,N}>0\), even if the *other* vectors are dependent. If \(d_{n,N}=0\), the finite span is closed and no control can satisfy all the moment constraints, because \(k_n\in V_{n,N}\). The Moore–Penrose inverse may compute a particular consistent finite system, but its diagonal is not a substitute for (5) without checking consistency and dependence. Thus the necessary condition for finite recovery of mode \(n\) is \(d_{n,N}>0\), not invertibility of the entire Gram.

The subspaces \(V_{n,N}\) grow with \(N\), so \(d_{n,N}\downarrow d_{n,\infty}\ge0\). Since \(q_jk_j\to a\), for every fixed \(n\),
\[
a\in\overline{\operatorname{span}}\{k_j:j\ne n\}\quad\text{and}\quad
\overline{\operatorname{span}}\{a,k_j:j\ne n\}
=\overline{\operatorname{span}}\{k_j:j\ne n\}. \tag{7}
\]
This includes \(a=0\). If \(a\ne0\), the augmented infinite family is nonminimal at \(a\); if \(a=0\), the added zero vector is also nonminimal. **Neither fact implies that any fixed \(k_n\) is nonminimal.** The columns are minimal exactly when every \(d_{n,\infty}>0\). In that case \(f_n=r_{n,\infty}/d_{n,\infty}^2\) is a bona fide \(L^2(J)\) biorthogonal control for each fixed \(n\), where \(r_{n,\infty}\) is the residual from the closed span in (7). Conversely existence of such a control implies \(d_{n,\infty}\ge1/\|f_n\|>0\).

The previous sufficient condition is, exactly,
\[
N^{-1+\eta}/d_{n,N}\longrightarrow0. \tag{8}
\]
If every actual column is minimal, then \(d_{n,N}\ge d_{n,\infty}>0\), and (8) holds automatically for every fixed \(n\); finite full-Gram invertibility follows because all finite subsets of a minimal family plus \(a\) are independent unless \(a\) lies in a finite column span. More precisely, if \(a\) lies in some finite span, full augmented Gram invertibility can fail even though individual distance controls exist: use the singular-Gram version (6), for which the same tail argument proves injectivity. Thus a stronger and cleaner conditional theorem is:

**Minimality theorem.** If every actual \(k_n\) is minimal, then \(\mathcal T\) is injective. Proof: the biorthogonal \(f_n\) exists, and bounded synthesis yields \((\mathcal Th,f_n)=h_n\) for every \(h\in H\); zero output gives all \(h_n=0\). No output completeness is required. This assumption is unverified and is sufficient, not necessary. The fixed-mode estimate (8) can also hold with \(d_{n,\infty}=0\), if distances vanish more slowly than \(N^{-1+\eta}\); then no exact biorthogonal \(f_n\) exists but the approximate controls can still recover \(h_n\).

For a *moving* index, if the other block includes \(a\), then
\[
d_{n,N}\le\|\rho_n\|\le C_\eta n^{-3/2+\eta},\quad
\|f_{n,N}\|\ge c_\eta n^{3/2-\eta}\quad(n\le N), \tag{9}
\]
whenever the control exists. In particular the old tail-bound product for \(n=N\) is at least \(cN^{1/2}\), and cannot tend to zero. This is a genuine obstruction to **uniform moving-mode** use of that bound, not to the fixed-\(n\) criterion (8). Scaling the columns to \(q_nk_n\) does not change their closed linear spans or minimality, but changes control normalization and input topology; it does not turn an \(\ell^2\) synthesis question into another one without tracking weights.

## 4. Completeness, minimality, and synthesis: precise distinctions

For a bounded synthesis \(T:\ell^2\to Z\), \(Te_n=k_n\):

* Output completeness, \(\overline{\operatorname{span}}\{k_n\}=Z\), means \(\ker T^*=0\), not \(\ker T=0\).
* Minimality of every column implies injective \(\ell^2\) synthesis by the biorthogonal argument above; it does not imply output completeness.
* Injective synthesis does not require minimality: let \(T e_1=(1/n^2)_{n\ge1}\), and for \(n\ge2\) let \(T e_n=n^{-2}e_{n-1}\), in \(\ell^2(\mathbb N)\). Then \(Te_1\) lies in the closure of the span of the other columns. If \(Th=0\), the \(m\)-th coordinate gives \(h_{m+1}= -((m+1)/m)^2h_1\), which is square summable only when \(h_1=0\), hence \(h=0\). The columns are square-summable, so \(T\) is bounded and compact. In general injection gives only \(e_n\in\overline{\operatorname{ran}T^*}\), not necessarily \(e_n\in\operatorname{ran}T^*\).
* Finite linear independence, even for every \(N\), does not exclude a nonzero square-summable relation. Completeness and minimality are separate properties.

The actual \(\{k_n\}\)'s minimality, finite-block independence, output completeness, and synthesis injectivity are all unknown. The sign regime of \(S\) and (3) show only sufficiently high single columns are nonzero; they do not establish any of those four properties. Removing finitely many columns changes the problem by finitely many directions; it does not automatically preserve output completeness or resolve a hidden infinite relation.

## 5. Two exact abstract examples with the same high-frequency estimates

The following operators are **not the actual PDE**. Identify \(H=\ell^2(\mathbb N)\), \(Z=\ell^2(\{0\}\cup\mathbb N)\) with basis \(e_0,e_1,\ldots\), set \(a=e_0\), \(q_n=n\), \(D e_n=n^{-2}e_n\), and \(\Lambda h=\sum h_n/n\). The latter is bounded.

**Injective example.** Define \(T_+h=a\Lambda h+Dh\), so \(k_n^+=a/n+n^{-2}e_n\). Then \(\rho_n^+=n^{-2}e_n\), satisfying (3) for every \(\eta>0\). \(T_+\) is injective because projecting onto \(e_n\) gives \(n^{-2}h_n\). It is output-complete: if \(y\perp k_n^+\), then \(y_n=-ny_0\), impossible in \(\ell^2\) unless \(y_0=0\). Its column family is minimal, with control \(n^2e_n\); its augmented family is nonminimal at \(a\). For fixed \(n\), \(d_{n,N}=n^{-2}\) and the original criterion holds.

**Noninjective example, with every finite augmented Gram positive.** Choose an infinite-support real unit vector \(v\in\ell^2\) with \(v_n\ne0\) for all \(n\), \(v_n=O(n^{-2})\), and \(\Lambda v=0\): take \(v_n=Cn^{-2}\) for \(n\ge2\) and \(v_1=-C\sum_{n\ge2}n^{-3}\), with normalizing \(C>0\). Define
\[
T_-h=a\Lambda h+D(I-v\otimes v)h. \tag{10}
\]
Then \(T_-v=0\), and its columns are \(k_n^-=a/n+D(e_n-v_nv)\) with
\(\|\rho_n^-\|\le n^{-2}+|v_n|\|Dv\|=O(n^{-2})\). Every finite augmented family \(\{a,k_1^-,\ldots,k_N^-\}\) is independent: a finite relation projected away from \(a\) gives \(D(I-v\otimes v)c=0\); injectivity of \(D\) gives \(c\in\operatorname{span}\{v\}\), impossible for finite support unless \(c=0\), then the \(a\) coefficient is zero. The actual infinite kernel is exactly \(\operatorname{span}\{v\}\).

Each column is nonminimal because \(\sum_jv_j k_j^-=0\) is a convergent \(\ell^2\) synthesis and \(v_n\ne0\). Indeed, for fixed \(n\le N\), \(v_nk_n^-=-\sum_{j\le N,j\ne n}v_jk_j^- -\sum_{j>N}v_jk_j^-\). Removing the tail's \(a\) component using the augmented \(a\) column gives
\[
d_{n,N}\le |v_n|^{-1}\Big\|\sum_{j>N}v_j\rho_j^-\Big\|
\le C_n N^{-3}, \tag{11}
\]
since \(\sum_{j>N}j^{-4}=O(N^{-3})\) and \(\|D(v\mathbf1_{j>N})\|=O(N^{-7/2})\). Thus \(\|f_{n,N}\|\ge c_nN^3\), and (8) fails for every \(0<\eta<1/2\), despite positive **all** finite augmented Grams. This is an exact infinite-series calculation, not a numerical inference. These examples prove that (3), finite independence and the shared profile alone cannot decide actual minimality, actual criterion validity or actual injectivity. Both are output-complete; e.g. for \(T_-^*y=0\), the tail equations imply \(y_n=-ny_0+C\) for large \(n\), forcing \(y_0=C=0\), then all coordinates vanish. Output completeness still coexists with a nonzero synthesis kernel.

## 6. Three constructive density approaches and exact missing estimates

### 6.1 Exact-leakage projection controls

For a fixed \(n\), whenever \(d_{n,N}>0\), use (6), even for singular Gram. Its **exact** adjoint error is
\[
\|\mathcal T^*f_{n,N}-\phi_n\|_H^2
=\sum_{j>N}|(\rho_j,f_{n,N})|^2, \tag{12}
\]
because \((a,f_{n,N})=0\) and the first \(N\) moments are exact. Hence the weakest condition for this particular construction is that the right side tend to zero; (8) is merely a Cauchy–Schwarz upper bound. This actual leakage condition may hold even when \(N^{-1+\eta}\|f_{n,N}\|\not\to0\), due to cancellations. Its value depends on the exact unknown \(\rho_j\), not column norms alone. If a finite control family satisfies (12) tending to zero for every fixed \(n\), actual injectivity follows. No such actual sequence has been computed or proved.

### 6.2 Tikhonov adjoint controls

For each \(n\) and \(\epsilon>0\), define the actual \(f_{n,\epsilon}=\mathcal T(\mathcal T^*\mathcal T+\epsilon I)^{-1}\phi_n\in Z\). Spectral calculus gives
\[
\mathcal T^*f_{n,\epsilon}=\phi_n-\epsilon(\mathcal T^*\mathcal T+\epsilon I)^{-1}\phi_n,
\quad \|f_{n,\epsilon}\|\le(2\sqrt\epsilon)^{-1}. \tag{13}
\]
As \(\epsilon\downarrow0\), the error converges in \(H\) to \(\Pi_{\ker\mathcal T}\phi_n\); this limit is zero iff \(\phi_n\perp\ker\mathcal T\). Thus these controls construct all coefficients **if and only if** the missing actual kernel property holds. The explicit norm bound and exact error reveal the obstruction; they do not prove the limit vanishes. No full-time analyticity or boundary Carleman estimate is imported.

### 6.3 \(H_0\) differences and leading-profile projection

Let \(z_n=\phi_n-(q_{n+1}/q_n)\phi_{n+1}\in H_0\). Then \(\mathcal Tz_n=\rho_n-(q_{n+1}/q_n)\rho_{n+1}\), which removes \(a\) without adding an augmented column. The span of these \(z_n\) is dense in \(H_0\): a vector in \(H_0\) orthogonal to all satisfies \(h_n/q_n^{-1}\) constant, hence is proportional to \(g\), and also orthogonal to \(g\). A blockwise Gram of \(\mathcal Tz_n\) therefore targets \(H_0\), but a dense set of test vectors or positive block Gram does not prove synthesis injectivity on \(H_0\); the noninjective abstract example already has these finite properties. An independent range-exclusion condition is still needed for the distinguished direction.

Alternatively, when \(a\ne0\), set \(Q_a=I-a\otimes a/\|a\|^2\). The projected operator \(Q_a\mathcal T=Q_aR\) is bounded and cancels the leading profile, but it can discard information: \(\ker(Q_a\mathcal T)=\{h:\mathcal Th\in\operatorname{span}a\}\) can be larger than \(\ker\mathcal T\). Proving this projected map injective would suffice but is stronger than needed. The coordinate transformation \(h=v+(\Lambda h)u\), \(v\in H_0\), is a bounded isomorphism with bounded inverse because \(u=q_1\phi_1\in H\); it preserves the \(L^2\) input topology, but its output remains \(Rv+c\mathcal Tu\), with no established triangularity or Fredholm property. \(R|_{H_0}\) is compact, and a Fredholm alternative for \(I+R\) is not a theorem about this observation map.

The actual PDE supplies \(M Y_t-\kappa Y_{xx}=BY+SP\), \(P_t+\mu P=\gamma Y\), and the exact residual term \(-2e^{-\mu t}S_x\phi_n'/q_n^2\). Its negative-norm estimate is cancellation, not a verified sign or triangular diagonal. Actual multiplication by spatially variable \(M,B,S\) couples all odd modes, and no recurrence or nonautonomous moment theorem has been proved. The transposition pair is
\(-\partial_t(Mz)-\kappa z_{xx}-Bz-\gamma w=0\), \(-w_t+\mu w-Sz=0\), \(w(T)=0\), with boundary data encoded by the audited functional; \(\mathcal T^*f=\Pi_o w(0)\). No Carleman/unique-continuation theorem has been matched to this pair, a nondiffusive memory state, and one delayed endpoint control. These are genuine construction failures, not proofs of noninjectivity.

## 7. Stronger singular-value, Schatten and conditional-stability results

**Theorem 1 (Schatten regularity).** Under (3), for every \(p>2/3\), \(\mathcal T\in\mathcal S_p(H,Z)\); in particular it is trace class. Moreover for every \(\varepsilon>0\),
\[
s_n(\mathcal T)\le C_\varepsilon n^{-3/2+\varepsilon}. \tag{14}
\]
**Proof.** Choose \(0<s<1\) and \(0<\eta<1-s\). The operator \(B_s:H\to Z\) with \(B_s\phi_n=q_n^s\rho_n\) is Hilbert–Schmidt because \(\sum q_n^{2s-3+2\eta}<\infty\). Let \(D_s\phi_n=q_n^{-s}\phi_n\). Then \(R=B_sD_s\), and \(D_s\in\mathcal S_r\) whenever \(sr>1\). Schatten Hölder gives \(R\in\mathcal S_p\) whenever \(1/p=1/2+1/r\), and by choosing \(s\uparrow1\), \(r\downarrow1/s\), every \(p>2/3\) is reached; membership for larger \(p\) follows by nesting. The rank-one \(a\Lambda\) is in every \(\mathcal S_p\). For the explicit bound, \(s_j(B_s)\le\|B_s\|_{\mathcal S_2}j^{-1/2}\), \(s_j(D_s)=O(j^{-s})\), and the product inequality gives \(s_{2j-1}(R)\le s_j(B_s)s_j(D_s)\). A rank-one perturbation shifts the singular-value index by at most one. Taking \(s>1-\varepsilon\) proves (14). □

The previously proved \(O(n^{-1+\eta})\) bound is correct but not sharp as an implication of its column estimates. The new threshold is sharp **for the abstract assumption (3)**: choose \(\rho_n=n^{-3/2}(\log(n+1))^{-1}e_n\) and a rank-one \(a/n\). It satisfies (3) for all \(\eta>0\), but the diagonal has \(\sum_n s_n^{2/3}=\sum_n n^{-1}(\log(n+1))^{-2/3}=\infty\); a rank-one perturbation cannot change Schatten membership. This is not a singular-value asymptotic or counterexample for the actual system. No matching actual lower bound or asymptotic law follows merely from nonzero \(S_x\).

**Theorem 2 (no strong Hölder recovery above \(4/7\)).** Fix any \(R>0\). Under (3), there are no constants \(C<\infty\), \(\alpha>4/7\) such that for all \(h\in X\) with \(\|h\|_{H^2}\le R\),
\[
\|h\|_{L^2}\le C\|\mathcal Th\|_Z^\alpha. \tag{15}
\]
The same conclusion holds for a two-point estimate on that ball. **Proof.** Let \(z_n=\phi_n-(q_{n+1}/q_n)\phi_{n+1}\); then \(\|z_n\|_2\asymp1\), \(\|z_n\|_{H^2}\asymp q_n^2\), and \(\|\mathcal Tz_n\|\le C_\eta q_n^{-3/2+\eta}\). Set \(h_n=c_Rq_n^{-2}z_n\) with a constant small enough for the entire sequence to be in the ball. Then \(\|h_n\|_2\asymp q_n^{-2}\), \(\|\mathcal Th_n\|\le C q_n^{-7/2+\eta}\). For \(\alpha>4/7\), choose \(\eta>0\) so \(\alpha(7/2-\eta)>2\); (15) would imply \(q_n^{-2}\le C'q_n^{-\alpha(7/2-\eta)}\), impossible. Taking the comparison state zero gives the two-point result. □

This does **not** rule out a Hölder exponent at most \(4/7\), a logarithmic modulus, or an \(H^2\)-bounded modulus modulo \(\ker\mathcal T\). If \(\ker\mathcal T\cap X=\{0\}\) were proved, compact embedding gives some qualitative full \(L^2\) modulus on each bounded \(H^2\) ball, but no numerical rate. Without it only distance to the full unknown \(L^2\) kernel has a qualitative modulus. The theorem is not asserted for a nonlinear admissible set without verifying its topology, uniform local neighborhood and nonlinear remainder.

## 8. Exact-kernel attempts on the actual system

1. **Infinite cancellation:** \(\sum h_n k_n=0\) is a convergent \(Z\)-series, but the norm bounds yield only \(a\Lambda h+Rh=0\). The noninjective example (10) shows upper estimates and positive finite Grams cannot determine whether an \(\ell^2\) relation exists. No actual coefficients \(h_n\) were constructed.
2. **Finite near-null sequence:** the normalized \(z_n\) in §7 has output tending to zero but converges weakly to zero and has no nonzero strong subsequence. Compactness makes this behavior expected; it cannot be converted into a nonzero exact kernel vector without extra compactness of the input sequence or another invariant estimate. A hypothetical strongly convergent sequence of actual unit inputs with output tending to zero would yield a nonzero exact kernel element by continuity, but no such sequence is known.
3. **Reachable-state/adjoint approach:** at \(\delta\), \(P(\delta)=e^{-\mu\delta}h+\gamma\int_0^\delta e^{-\mu(\delta-r)}Y(r)dr\); the compact perturbation of the identity has a finite-dimensional possible kernel, but no actual nonzero vector in the joint state kernel has been found. Orthogonality to *all* actual transposition states is equivalent to the original problem, not constructed here. In the actual model \(S(0)=\lambda\alpha br\theta_*\ne0\), so a construction imposing \(S\equiv0\) contradicts the frozen positive material assumptions and is not physically relevant to this experiment.

## 9. Computational mathematics: executed abstract tests and parameterized solvers

`code/direction-2-moment-analysis/` contains a parameterized finite-difference active-base solver and a sine-Galerkin linearized forward/augmented-moment diagnostic. They use the actual equations (1)–(2) and require user-supplied parameters or arrays; they do not certify coefficient provenance, base existence, accuracy, or rank. The finite base discretization uses trapezoidal means \(Q_h\), \(\theta=\theta_*+y\), and solves
\[
[cI+d\operatorname{diag}(\theta)Q_h]\dot y=\kappa\Delta_h y-b\theta E+k\lambda w^2,\quad
\dot p=-\mu p+\gamma Q_hy,\quad\dot v=\lambda(m-v), \tag{16}
\]
while the Galerkin diagnostic uses \(M_N\dot Y+\kappa\operatorname{diag}(q_n^2)Y=B_NY+S_NP\), \(\dot P=-\mu P+\gamma Y\), with the input identity matrix. Coefficient arrays are interpolated in time and space; BDF and discrete spatial/time quadrature are used. The README specifies the input contract, independent convergence requirements, and separation of physical and abstract diagnostics. No actual parameter set or actual coefficient array was available, so these physical commands were **not run or validated on the experiment**; no second independent physical discretization is claimed.

The abstract test suite was run using NumPy 2.4.6 and SciPy 1.17.1. Five tests passed: exact injective distances, finite truncation of the explicit infinite kernel, quadrature weights, a tolerance-based Schur/inverse comparison, and an artificial constant-coefficient Galerkin software test against a matrix exponential. That artificial test is not an active physical experiment. The latter illustrates that normal equations lose precision, hence the primary diagnostic computes projection residuals using SVD-based least squares. For output dimension 4096, first mode and \(\eta=0.1\), the executed illustrative results were:

| \(N\) | injective distance | injective \(N^{-0.9}/d\) | noninjective distance | noninjective \(N^{-0.9}/d\) |
|---:|---:|---:|---:|---:|
| 4 | 1.0000 | 0.2872 | 0.013650 | 21.04 |
| 8 | 1.0000 | 0.1539 | 0.001438 | 107.0 |
| 16 | 1.0000 | 0.08247 | 0.0001391 | 592.8 |
| 32 | 1.0000 | 0.04419 | 0.00001286 | 3435 |
| 64 | 1.0000 | 0.02368 | 0.000001163 | 20365 |

These are **abstract finite computations**, with output truncation and floating-point error, not experimental data or proof. The proofs of both infinite examples are in §5; see the code README for reproduction and parameterized input requirements.

## 10. Targeted primary literature and what actually transfers

The following primary statements/proofs were inspected; cited dependencies and the full literature were not exhaustively checked. Titles, authors and arXiv identifiers were checked against title pages.

| Source | Theorem/result and exact assumptions | What transfers | Missing for (2) |
|---|---|---|---|
| P. Cannarsa, P. Martinez, J. Vancostenoble, *Precise estimates for biorthogonal families under asymptotic gap conditions*, [arXiv:1706.02435v1](https://arxiv.org/html/1706.02435), 2017 | Theorem 2.1: exponential families with specified global and asymptotic square-root spectral gaps; bounds depend on gaps. | Demonstrates how norm growth is quantified in an established moment setting. | Actual nonautonomous \(k_n\) are not established as such exponentials; their scaled leading profiles coalesce. |
| Brahim Allal, Abdelkarim Hajjaj, Jawad Salhi, Amine Sbai, *Boundary controllability for a coupled system of degenerate/singular parabolic equations*, [arXiv:2104.00610v1](https://arxiv.org/html/2104.00610), 2021 | Theorem 1.1: biorthogonal exponentials under sector, separation and summability; application to an autonomous two-diffusion system. | The theorem is a valid template if its spectral hypotheses are independently proved. | Neither a common generator nor those gaps for the actual heat–ODE columns is known. |
| Guillaume Olive, *Boundary approximate controllability of some linear parabolic systems*, [arXiv:2609.09982v1](https://arxiv.org/html/2609.09982), 2026 | Theorem 1.1 and appendix: autonomous semigroup/root-space argument with complete adjoint root vectors. | Explains a rigorous route from a verified spectral condition to observability. | Active time dependence and nondiffusive state do not satisfy its established assumptions. |
| Andrei Halanay, Luciano Pandolfi, *Approximate controllability and lack of controllability to zero of the heat equation with memory*, [arXiv:1404.2745v1](https://arxiv.org/html/1404.2745), 2014 | Theorem 2: scalar Coleman–Gurtin equation with \(C^1\) Laplacian-convolution kernel, admissible boundary controls. | Memory/heat-control distinction and proof structure. | Different state, coupling and observation; not arbitrary initial ODE memory. |
| Dev Prakash Jha, Raju K. George, *Observability and Null Controllability for Parabolic Systems with Delay and Memory*, [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), 2026 | Theorem 3.10 and Lemma 3.13 require moving interior observation, short-time closure and assumed unique continuation/compactness. | A coupled Carleman/ODE framework under its own hypotheses. | The assumptions are not verified for a single delayed endpoint and arbitrary initial memory. |
| Christian Clason, *Regularization of Inverse Problems*, [arXiv:2001.00617v2](https://arxiv.org/html/2001.00617), 2021 | Theorem 3.10 and proof: Picard criterion for exact range of compact Hilbert operators. | General singular-system and exact-range machinery. | It does not supply actual singular values, minimality, or density. |

The Hilbert-space distance, factorization, and stability arguments in this report are derived directly; they may be standard consequences of existing mathematics. No verified literature comparison establishes novelty or publication priority for any bound.

## 11. Verdict and single next target

1. Actual minimality: **unknown**. 2. Actual output completeness: **unknown**. 3. Augmented Gram criterion: **unverified**, not impossible by (3). 4. Actual inverse-Gram growth relative to tail: **not bounded**; moving-mode use of the old estimate is rigorously impossible, while fixed-mode behavior is undecided. 5. Actual adjoint density: **not proved**. 6. Exact physical kernel element: **none constructed**. 7. Uniform strong recovery: **impossible**, and Hölder exponents \(>4/7\) are excluded on bounded \(H^2\) balls for the linearized map. 8. Weaker logarithmic/Hölder moduli and modulo-kernel stability remain possible; a full qualitative modulus requires separate injectivity on \(X\). 9. No literature novelty has been demonstrated. 10. The strongest actual theorems are conditional Schatten membership/singular upper bound (14), the stability obstruction (15), and the exact control-error identity (12).

**Recommended single theorem:** establish a lower bound for the actual fixed-mode distance \(d_{n,\infty}>0\) for every \(n\), or directly prove the exact-leakage limit (12) for actual boundary controls. Either would prove linearized injectivity without requiring the augmented family to be minimal at \(a\); neither has been proved. Failure of that sufficient condition would not itself prove noninjectivity. Final decision remains with Dr. Gupta.
