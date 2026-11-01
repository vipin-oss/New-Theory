# Singular-value novelty reassessment and restricted-prior audit

## Selected decision

**ACTUAL KERNEL REGULARITY REMAINS OPEN**

The actual rank-one-subtracted odd kernel has been constructed and is in \(L^2(J;H^s_0(I))\) in the appropriate spectral sense for every \(s<1\); its source endpoints vanish. The remaining question is exactly whether \(\sum q_n^2\|\rho_n\|^2<\infty\). Neither this endpoint square sum nor its failure is established for the actual active base. Therefore Volkov's \(H^1\) hypothesis is **not verified** under the frozen assumptions, and we cannot claim that his theorem subsumes this particular application. Under an explicitly stronger, currently unverified isotropic \(H^{2+\eta}\) hypothesis on \(S\), the endpoint follows and Volkov does subsume the singular-value conclusion. This conditional comparison is not evidence that the prescribed experiment satisfies the extra hypothesis.

The strongest presently justified unconditional singular-value theorem, in the inherited nonempty small-load regime for the prescribed nonzero-loading base, remains
\[
s_n(\mathcal T)=o(n^{-3/2})\quad\text{and}\quad \mathcal T\in\mathcal S_p\ (p>2/3), \tag{1}
\]
proved previously by actual PDE column estimates and a dyadic finite-rank argument, not by an unverified kernel \(H^1\) hypothesis. The present audit also proves the actual fractional **weighted** singular-value bounds \(\sum n^{2s}s_n(\mathcal T)^2<\infty\) for every fixed \(0<s<1\). Neither establishes the endpoint weighted sum or strong \(\mathcal S_{2/3}\). Results are mathematical, not verified experimental parameter ranges. No injectivity or nonuniqueness follows from these singular-value statements.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder. This audit is not independent human certification. Direction 1 remains rejected; no new foundational continuum theory or priority claim is asserted.

## Claim–evidence table

| Claim | Evidence | Status |
|---|---|---|
| Actual observation kernel exists | The actual delayed sine responses satisfy \(\sum\|k_n\|^2<\infty\); Hilbert–Schmidt representation gives the unique **odd-in-source** \(K\in L^2(J\times I)\). | **Proved**, as an \(L^2\) kernel, not a classical impulse kernel. Adding a source-even kernel would leave the odd operator unchanged, so canonical parity matters. |
| Exact rank-one normalization | \(\ell(x)=\sqrt{2/L}(L/4-x/2)\), \((\ell,\phi_n)=1/q_n\); \(K=a\ell+R\). | **Proved**; \(a\ell=A_0e^{-\mu t}S(t,0)(1-2x/L)\), matching the earlier report. |
| Remainder \(H^1\) | Zero source traces are proved from all \(H^s\), \(s<1\); therefore \(R\in L^2H^1\iff\sum q_n^2\|\rho_n\|^2<\infty\). Existing column proof supplies only \(o(\log N)\) growth of the partial sums. | **Open**, not a counterexample and not a verified Volkov application. |
| Fractional regularity | \(\rho_n=o(q_n^{-3/2})\) implies \(\sum q_n^{2s}\|\rho_n\|^2<\infty\) for \(s<1\); derivative-trace construction and feedback are those of the actual PDE. | **Proved** for every fixed \(s<1\), with no claim at \(s=1\). |
| Fractional singular-value theorem | Factorization \(\mathcal R=B_sD_s\), \(B_s\) Hilbert–Schmidt and \(s_n(D_s)\asymp n^{-s}\), gives \(\sum n^{2s}s_n^2<\infty\). Delgado–Ruzhansky Theorem 2.2(iii) gives the corresponding Schatten range. | **Proved** for fixed \(s<1\), but the resulting \(o(n^{-s-1/2})\) is weaker than (1). |
| Volkov hypothesis mapping | Volkov Theorem 1.1 needs ordinary source \(H^1\), not \(H^1_0\) and not a classical derivative; the odd operator extends canonically by zero on even inputs. | All geometric and \(L^2\) hypotheses verified; the actual source-derivative hypothesis remains unresolved. |
| Conditional \(H^1\) | A dyadic summable smooth-approximation error/cost criterion proves the weighted column sum. Isotropic \(S\in H^{2+\eta}(Q_T)\), \(\eta>0\), suffices by mollification. | **Conditional only**: extra time/space regularity is not established for the actual base. Under it Volkov yields the weighted singular-value sum and (1). |
| Whether existing theory already subsumes the application | Volkov is a genuine prior general theorem, but its endpoint hypothesis is unmapped to the actual coefficients. The column theorem and lower-order fractional theory alone do not fill the gap. | **Unresolved**; no claim of novelty or of subsumption. |
| Exact initial-memory uniqueness | Rank-one and compact-operator decay do not determine the infinite synthesis kernel. | **Open** for arbitrary odd initial memory; the prior one-mode result remains separate. |

## Independent check of the previous restricted-prior theorem

Set \(q=|g_*|/L\), \(C_y=2KC_B\), \(C_w=W_s+2C_BW_R\) and
\[
q_{\rm sign}=\frac{|br|\theta_*}{2(|br|C_y+2kC_w)},\qquad 0<q<\min(s_*/2,q_{\rm sign}). \tag{2}
\]
The exact definitions and units of \(s_*,K,C_B,W_s,W_R\) are in `direction-2-active-base-existence-and-regularity.md` (5)–(7); all constants and the denominator are positive in a fixed consistent unit system. The fixed-point bound \(\|y_b\|_\mathcal E\le2C_Bq\) and the audited \(\|w_b\|_\infty\le W_sq+W_R\|y_b\|_\mathcal E\) give
\[
\|y_b\|_\infty\le C_yq,\quad \|w_b\|_\infty\le C_wq,\quad
\operatorname{sgn}(b)S\ge\lambda\alpha\{ |br|\theta_*-(|br|C_y+2kC_w)q\}
>\tfrac12\lambda\alpha|br|\theta_*>0. \tag{3}
\]
The inequalities hold on the whole cylinder via continuous representatives, hence on \(J\); they preserve the actual nonzero loading and memory. Consequently
\[
A:=\|a\|_{L^2(J)}\ge 2A_0\sqrt{2/L}\,(\tfrac12\lambda\alpha|br|\theta_*)\left(\int_\delta^T e^{-2\mu t}dt\right)^{1/2}>0. \tag{4}
\]
Since \(q_n\|\rho_n\|\to0\), there exists \(N_*\) such that \(\|k_n\|\ge A/(2q_n)>0\) for every \(n\ge N_*\). Thus \(c\mapsto c\phi_n\mapsto ck_n\) is injective for each **fixed known** such \(n\). The little-o density proof itself gives only an existential \(N_*\), because the approximant's high-derivative cost is not quantified in that proof.

An explicit **symbolic conditional** cutoff is possible if a certified constant \(C_{\rm col}\) in the uniform bound \(\|\rho_n\|\le C_{\rm col}q_n^{-3/2}\) is supplied: it suffices that \(q_n>(2C_{\rm col}/A)^2\), or \(n>\frac L{2\pi}(2C_{\rm col}/A)^2\). The approximation estimate with auxiliary source \(f=0\) supplies such a finite model-dependent constant, but the prior reports do not give a closed numerical evaluation of it from the physical parameters; no numerical cutoff or experimental claim is invented. A valid explicit material-only cutoff would require tracking those energy, trace, and cutoff constants and the \(\mathcal A\)-norm bound for the actual base.

For the nonlinear line result, let \(\mathcal F\) be the actual force/two-outward-flux map and let \(D\) subtract its labeled flux components in the convention giving \(D\mathcal F'(0)\phi_n=k_n\). Define
\[
F_n(c)=\langle D[\mathcal F(c\phi_n)-\mathcal F(0)],k_n\rangle_{L^2(J)}. \tag{5}
\]
The previously proved \(C^2\) map on an actual \(H^2\) neighborhood gives \(F_n'(0)=\|k_n\|^2>0\). Continuity of the derivative yields an \(\varepsilon_n>0\) such that \(F_n'(c)>0\) for \(|c|<\varepsilon_n\), with \(c\phi_n\) inside that neighborhood; hence \(F_n\) is strictly increasing there. No uniform-in-\(n\) radius is claimed. This proves local nonlinear identification **only on that fixed line**, not for unions, multi-mode priors, or an open infinite-dimensional neighborhood. The outward-flux difference normalization is essential; reversing the difference reverses the response; choosing the test consistently again gives its positive squared norm and leaves injectivity unchanged.

## Single next step and verification

Prove or refute the actual PDE square-function estimate
\[
\sum_{n\ge1}q_n^2\big\|2A_0\kappa Y_{n,x}(0,\cdot)|_J-a/q_n\big\|_{L^2(J)}^2<\infty, \tag{6}
\]
with \(Y_n,P_n\) solving the original nonautonomous system from \((0,\phi_n)\). A successful proof must control the weak/strong cutoff terms and nondiffusive pre-delay feedback jointly across \(n\), not just mode by mode. The dyadic approximation condition in the kernel report identifies a sufficient quantitative target; alternatively a legitimate coefficient-class counterexample could refute a generic theorem, but would not automatically refute the actual thermoviscoelastic base. If (6) is proved, apply Volkov exactly as mapped; if it fails for the actual base, identify the actual weak-derivative obstruction.

No implementation changed, so tests were not required and were not run. Primary Volkov and Delgado–Ruzhansky statements and relevant proof passages were reinspected. The three new reports are the only intended changes; the model and prior reports are untouched.
