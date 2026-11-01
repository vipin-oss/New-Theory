# Formulation A: admissible-data topology audit

**Date:** 1 November 2026
**Status: topology of candidate sets proved; actual solution-admissible sets remain unverified.**

## 1. Executive findings and scope

The ambient space is frozen as \(X=H^2(0,L)\) with the full strong norm, and the a priori set as its closed ball \(B_M\), \(M>0\). The weaker \(L^2\) metric is a separately specified observation/comparison topology, not a replacement for the \(H^2\) bound. Both \(B_M\) and the exact first-order compatibility set \(C_M\) are **compact in the inherited \(L^2\) metric**, and complete and closed in the strong \(H^2\) metric. The \(L^2\)-compactness of \(C_M\) is a specific consequence of the fixed \(H^2\) bound and continuity of the endpoint constraints under bounded weak \(H^2\) convergence; it does **not** follow just from strong closedness. \(C_M\) contains arbitrarily small nonzero fields, but no corresponding active-experiment solution has been proved to exist.

The candidate weak-initial domain is \(W_M=B_M\), without imposing corner derivative conditions. Neither actual solution-admissible set defined below has been proved nonempty, closed or compact in \(L^2\). Both are relatively compact in \(L^2\) because they are subsets of \(B_M\). They are set-theoretically well-defined predicates, possibly empty; this is not a constructive existence theorem. The observation map is well-defined on each such set **by its definition and the stated trace regularity**, but no nonempty domain with unconditional forward continuity has been established. Uniform \(L^2\)-Lipschitz continuity holds only on an actual family satisfying the earlier audit's uniform solution bounds.

The README and three named primary documents were read. This is an Arena functional-analysis check, not a claim of independent certification by another auditor. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. Direction 1 remains rejected as a new foundational continuum theory; Direction 2 remains reformulated. No change to the experiment, inverse uniqueness investigation, new theory, simulation or manuscript is made.

## 2. Physical problem and notation: unchanged

All statements concern the existing 1-D model, not a modified experiment. In particular \(a,k,\lambda,c,\kappa,\theta_*,L,A_0>0\), \(b\ne0\), and the prescribed displacement is \(g_*\sin^2(\pi t/T)\) with fixed \(g_*\ne0\), \(T=10/\lambda\), \(\delta=T/100\). The two baths are held at \(\theta_*\), the initial temperature equals \(\theta_*\), and the force and two **labeled outward** heat powers are unchanged. Set

\[
D=a+k,\quad r=k/D,\quad\alpha=a/D,\quad\beta=b/D,\quad
\mu=\lambda\alpha,\quad d=b^2/D,\quad \bar f=L^{-1}\int_0^L f(x)dx.
\]

The previous reduction gives \(\varepsilon=m+r(z-\bar z)+\beta(\theta-\bar\theta)\), \(m=g/L\), \(\sigma=Dm-b(\bar\theta-\theta_*)-k\bar z\), together with the memory and thermal equations in the forward audit. At time zero \(m=m'=0\), and for every \(z_0\in H^2\), initial equilibrium is uniquely reconstructed as \(u_0(x)=r\int_0^x(z_0-\bar z_0)dy\). This satisfies both prescribed initial endpoint displacements. It does not prove that an active solution exists.

## 3. Ambient space, metrics and compactness

Let \(I=(0,L)\), and freeze the real Hilbert space

\[
X=H^2(I),\quad \|z\|_X^2=\int_0^L(|z|^2+|z_x|^2+|z_{xx}|^2)dx,\quad
B_M=\{z\in X:\|z\|_X\le M\}.
\]

On \(B_M\), use either the inherited strong metric \(d_X(z,\tilde z)=\|z-\tilde z\|_{H^2}\) or the weaker metric \(d_0(z,\tilde z)=\|z-\tilde z\|_{L^2}\). The latter is genuinely a metric on \(H^2\) equivalence classes: zero \(L^2\) distance means equality almost everywhere and hence equality as Sobolev elements. Strong \(H^2\) convergence means convergence in \(L^2\) of the functions and both weak derivatives through order two; \(L^2\) convergence alone does not require derivative convergence. The former implies the latter, not conversely, including on \(B_M\).

**Proof of compactness facts.** \(X\) is a Hilbert space, so its closed bounded ball is weakly sequentially compact; its norm is weakly lower semicontinuous. Rellich compactness on the bounded interval gives compact embeddings \(H^2(I)\hookrightarrow H^1(I)\hookrightarrow L^2(I)\); also \(H^1(I)\hookrightarrow C^0([0,L])\) continuously, hence bounded \(H^2\) sequences have subsequences converging in \(C^0\). If \(z_n\in B_M\) converges in \(L^2\) to \(z\), a subsequence converges weakly in \(H^2\) to \(v\in B_M\); compact embedding identifies \(v=z\) as an \(L^2\) element. Thus \(z\in B_M\). Consequently \(B_M\), regarded as a subset of \(L^2(I)\), is **closed and compact**, not merely relatively compact. It is complete in \(d_X\) and \(d_0\). It is not compact in \(d_X\): any orthonormal sequence in infinite-dimensional \(X\), multiplied by a fixed \(0<q<M\), is contained in the ball and has pairwise \(H^2\) distance \(q\sqrt2\).

As a useful refinement, if a sequence in \(B_M\) converges in \(L^2\), it converges weakly in \(H^2\) to the same limit, and converges strongly in \(H^1\) and \(C^0\). To see the full-sequence claim, otherwise an offending subsequence would have a further weak \(H^2\) and strong \(H^1\) convergent subsequence whose unique \(L^2\) limit is the prescribed limit, a contradiction. Thus on the bounded ball, strong \(L^2\) convergence is equivalent to weak \(H^2\) convergence for sequences, but neither implies strong \(H^2\) convergence.

## 4. Classical corner-compatibility set

For \(z\in X\), put \(p=z-\bar z\), \(w=-\bar z-\alpha p\), and define

\[
G_i(z)=b\theta_*r\mu\,p(i)+k\lambda w(i)^2+
\frac{d\theta_*k\lambda}{c}\overline{w^2},\qquad i\in\{0,L\},\tag{4.1}
\]

\[
C_M=\{z\in B_M:G_0(z)=G_L(z)=0\}.\tag{4.2}
\]

These are exactly the previous audit's first-order corner expressions: for a corner-classical solution, \((c+d\theta_*)\theta_t(x,0)=G_x(z_0)\), where (4.1)'s expression is evaluated at arbitrary \(x\) in place of \(i\). The fixed bath makes \(\theta_t(i,0)=0\). This assumes \(\theta_t\) and \(\theta_{xx}\) extend continuously to the corners; it is not imposed on all weak-initial solutions. The prior solution concept requires no higher time derivatives; if a stronger concept does, extra compatibility conditions may be needed. The two constraints are **necessary, not proved sufficient**, for a corner-classical solution.

**Well-definedness and \(H^2\) continuity.** On an interval, \(H^2\hookrightarrow C^1([0,L])\), so the endpoint values of the unique continuous representatives exist and are bounded linear functionals of \(z\). Averaging is bounded on \(L^2\); \(z\mapsto w\) is linear and bounded on \(H^2\) and \(L^2\); \(w\mapsto\overline{w^2}\) is continuous in \(L^2\). Endpoint squaring is continuous. Therefore each \(G_i:X\to\mathbb R\) is strongly \(H^2\)-continuous, and \(C_M\) is a strongly closed subset of the complete space \(X\), hence complete in \(d_X\).

**\(L^2\)-closedness and compactness of this particular set.** Let \(z_n\in C_M\) and \(z_n\to z\) in \(L^2\). The bound \(\|z_n\|_{H^2}\le M\) gives a subsequence weakly convergent in \(H^2\) and strongly convergent in \(H^1\), hence uniformly. The \(L^2\) limit identifies the subsequence's limit as \(z\), and weak lower semicontinuity gives \(z\in B_M\). Uniform convergence supplies \(p_n(i)\to p(i)\) and \(w_n(i)\to w(i)\), while \(L^2\) convergence supplies \(\overline{w_n^2}\to\overline{w^2}\). Thus \(G_i(z)=0\) at both endpoints, so \(z\in C_M\). This proves \(C_M\) is closed **in all of \(L^2(I)\)**, not just relatively closed in \(B_M\). Since \(B_M\) is \(L^2\)-compact, so is \(C_M\), and it is complete in \(d_0\). In fact both \(G_i\) are continuous on \(B_M\) in the \(d_0\) topology, as the full-sequence convergence argument in §3 shows.

This bounded-ball result does not say \(G_i\) is \(L^2\)-continuous on all of \(X\). For example, a smooth bump supported in \([0,1/n]\), of fixed endpoint height \(s\), tends to zero in \(L^2\) while its endpoint value stays \(s\), and its \(H^2\) norms are unbounded. Choose nonzero \(s\) such that \(b\theta_*r\mu s+k\lambda\alpha^2s^2\ne0\); then \(G_0\) does not approach \(G_0(0)=0\). The uniform \(H^2\) bound is essential in the preceding proof.

**Nonzero members for every \(M>0\).** Let

\[
z_s=s\sin(2\pi x/L)+h(s)\cos(2\pi x/L).
\]

Its spatial mean is zero and both endpoints equal \(h\). Both conditions in (4.1) reduce exactly to

\[
B h+k\lambda\alpha^2\left[h^2+\frac{d\theta_*}{2c}(s^2+h^2)\right]=0,
\qquad B=b\theta_*r\mu\ne0.\tag{4.3}
\]

The implicit-function theorem at \((s,h)=(0,0)\) yields a smooth \(h(s)\) with \(h(0)=h'(0)=0\), so \(h(s)=O(s^2)\). For sufficiently small nonzero \(s\), \(z_s\ne0\), belongs to \(C_M\), and has norm below any prescribed \(M>0\). Also \(0\in C_M\). These are compatible data, not proved realizable solutions or physically prepared histories.

**\(C_M\) is not strongly \(H^2\)-compact.** Fix a small \(A>0\) and for large integers \(n\) set \(s_n=A/n^2\) and

\[
z_n=s_n\sin(2\pi n x/L)+h(s_n)\cos(2\pi x/L).
\]

The mean is zero, the endpoints both equal \(h(s_n)\), and orthogonality gives \(\overline{z_n^2}=(s_n^2+h(s_n)^2)/2\). Therefore (4.3) again yields \(z_n\in C_M\), after choosing \(A\) small enough and \(n\) large enough to satisfy the norm bound. The sequence tends to zero in \(L^2\), while \(\|z_{n,xx}\|_2\to A(2\pi/L)^2\sqrt{L/2}>0\); hence no subsequence converges strongly in \(H^2\). This also gives a concrete sequence distinguishing the two topologies within \(C_M\).

## 5. Weak-initial candidate domain and trace conditions

Define \(W_M=B_M\), with either \(d_X\) or \(d_0\) explicitly specified. It does **not** include a first-order corner restriction merely because that restriction is necessary for continuous classical \(\theta_t\) at \(t=0\). Failing a classical corner condition does not establish existence of a weaker solution; it only means the classical argument cannot exclude a solution whose initial derivatives have no such corner trace.

The proposed solution concept is exactly the previous forward audit's strong-temperature/weak-initial class, not a theorem of existence. On \([0,T]\), set \(y=\theta-\theta_*\) and require

\[
y\in H^1(0,T;L^2(I))\cap L^2(0,T;H^2(I)\cap H_0^1(I)),\quad
z\in H^1(0,T;L^2(I)),\tag{5.1}
\]

with \(y(0)=0\), \(z(0)=z_0\) in \(L^2\); the exact reduced equations hold almost everywhere; \(\theta\ge\theta_*/2\) almost everywhere; and \(\theta,p,w\in L^\infty((0,T)\times I)\) so the products have the meaning required in the previous report. Reconstruct \(u,\varepsilon,\sigma\) as in §2.

- \(H^1(0,T;L^2)\hookrightarrow C([0,T];L^2)\): the temperature and memory initial values have well-defined continuous \(L^2\) time traces. No endpoint value of \(\theta_t\) at \(t=0\) follows.
- \(y(t)\in H_0^1(I)\) for almost every \(t\): the spatial boundary traces of \(y\) vanish for almost every \(t\); the bath condition holds in this trace sense, not necessarily pointwise at every initial corner.
- The reduced strain belongs to \(H^1(0,T;L^2)\), because \(z,y\) do and averaging is bounded. The integrated displacement belongs to \(H^1(0,T;H^1(I))\); its continuous-time \(H^1\) representative has spatial traces \(u(0,t)=0\) and \(u(L,t)=g(t)\) for every \(t\).
- The heat-gradient endpoint traces are in \(L^2(0,T)\) by §7, since \(y\in L^2_tH^2_x\). Delayed traces are therefore meaningful **if such a solution exists**; neither existence nor smoothing from a weaker energy class is implied.

No physical preparation history or weak-solution well-posedness is established by this definition.

## 6. Actual solution-admissible predicates and their topology

Define the **corner-classical class** as in §3.1 of the forward audit: \(\theta,\theta_t,\theta_x,\theta_{xx}\), \(p,p_t\) continuous on the closed space-time cylinder, \(\bar z\in C^1\), equations holding in the interior and extending to the corners, pointwise data and positive temperature. Require the reconstructed fields and the fixed experiment. Define \(\mathcal S_{\rm cl}(z_0)\) to be the set of all such solutions for that datum.

Similarly define \(\mathcal S_{\rm w}(z_0)\) to be the set of solutions in exactly (5.1), with all additional boundedness, positivity, equation and trace requirements listed in §5. The sets are the following **solution-dependent predicates**, not explicit computational tests:

\[
\begin{aligned}
\mathcal A_T^{\rm cl}&=\{z_0\in C_M:\ \mathcal S_{\rm cl}(z_0)\text{ has exactly one element},\\
&\hspace{34mm}\theta\ge\theta_*/2\text{ on }[0,L]\times[0,T],\ F_A(z_0)\in Y\},\\
\mathcal A_T^{\rm w}&=\{z_0\in W_M:\ \mathcal S_{\rm w}(z_0)\text{ has exactly one element},\\
&\hspace{34mm}\theta\ge\theta_*/2\text{ a.e.},\ F_A(z_0)\in Y\}.
\end{aligned}\tag{6.1}
\]

Here \(F_A(z_0)\) denotes the traces **of that unique solution**, not an independently assumed map. \(Y\) is defined in §7. For the weak class the temperature bound is already part of the class definition, and for either class the trace condition is automatic from the specified regularity; both are retained in (6.1) for clarity. The predicates have definite set-theoretic meanings, even if empty, but give no existence proof or usable membership test. Uniqueness means within the **selected class**; it is not a claim that every weaker distributional or measure-valued solution coincides.

The prior energy estimate proves uniqueness between existing positive corner-classical solutions, because their relevant coefficients and derivatives are bounded on the compact cylinder; this does not prove existence. Classical solutions with \(\theta\ge\theta_*/2\) also satisfy the weak-class regularity and boundedness, but \(\mathcal A_T^{\rm cl}\subseteq\mathcal A_T^{\rm w}\) is **not established**: uniqueness among classical solutions does not imply uniqueness among all weak-initial solutions. Conversely, a weak-initial solution need not have continuous corner derivatives, so no reverse inclusion follows. If both classes contain a solution for the same datum and uniqueness in the weak class holds, the two solutions coincide; this conditional statement does not establish either inclusion.

For each \(\mathcal A\in\{\mathcal A_T^{\rm cl},\mathcal A_T^{\rm w}\}\):

| Property | Conclusion and reason |
|---|---|
| Nonempty | **UNPROVED.** The data family in §4 is not a solution construction, and \(z_0=0\) under nonzero loading is not an equilibrium solution. |
| Relative compactness in \(L^2\) | **PROVED.** \(\mathcal A\subseteq B_M\), which is compact in \(L^2\). This is true even if \(\mathcal A\) is empty. |
| Strong \(H^2\) closedness and completeness | **UNPROVED.** A strong limit of data need not be known to preserve the existence and selected-class uniqueness requirements. If closed, it is complete; completeness of a subset of a complete metric space is equivalent to closedness. |
| \(L^2\) closedness, completeness and compactness | **UNPROVED.** Relative compactness alone does not prove the limit is admissible. Because \(B_M\) is compact, these three properties are equivalent for \(\mathcal A\), but no one is established. |
| Stability under strong \(H^2\) limits within the set's ambient space | **UNPROVED.** It is precisely strong sequential closedness, which is equivalent to strong closedness in a metric space. |
| Stability under \(L^2\) limits in \(L^2\) | **UNPROVED.** Any such data limit lies in \(B_M\), and for the classical set in \(C_M\), by §§3–4; existence, selected-class uniqueness, temperature and observation requirements must still pass to the limit. |

A solution-admissible subset **may** fail to be closed when existence, uniqueness or uniform bounds are not stable, but no counterexample to closure for this particular physical problem has been proved. The lower bound \(\theta\ge\theta_*/2\) would pass to a limit under suitable convergence (e.g. strong \(L^2\) space-time convergence plus an a.e. convergent subsequence), but a convergent sequence of solutions with adequate uniform bounds has not been constructed. Equalities defining compatibility are stable; the full PDE admissibility predicate is a separate issue.

## 7. Observation space and forward operator

Freeze

\[
Y=L^2(\delta,T)^3,\qquad \|(f_1,f_2,f_3)\|_Y^2=\sum_{j=1}^3\|f_j\|_{L^2(\delta,T)}^2.
\]

For \(\mathcal A_T\) equal to either set in (6.1), define the **forward** observation operator

\[
F_A:\mathcal A_T\to Y,\quad z_0\mapsto
\left(A_0\sigma,\ A_0\kappa\theta_x(0,\cdot),\ -A_0\kappa\theta_x(L,\cdot)\right)\Big|_{(\delta,T)},\tag{7.1}
\]

using that set's unique solution. This is well-defined even if the domain happens to be empty, in which case it has no practical nontrivial content. In the classical class the endpoint derivatives are continuous; in (5.1), for a.e. \(t\), \(y(t)\in H^2(I)\), and

\[
|y_x(0,t)|^2+|y_x(L,t)|^2\le C_L\|y(t)\|_{H^2(I)}^2.\tag{7.2}
\]

Integrating proves that both endpoint gradients are in \(L^2(0,T)\) and hence \(L^2(\delta,T)\). More generally \(L^2(\delta,T;H^s(I))\), \(s>3/2\), suffices by the one-dimensional derivative trace theorem; this is not claimed to be the weakest PDE-specific trace hypothesis. The force is in \(L^2\) since \(m\) is smooth and the spatial means of \(\theta,z\) are continuous in time in \(L^2\). The delay does not prove any of these solution-space properties.

### Continuity, exactly qualified

Well-definedness is not continuity. Neither \(d_X\)-continuity nor \(d_0\)-continuity on all of either \(\mathcal A_T\) has been established from (6.1). If a map is \(d_0\)-continuous, then it is \(d_X\)-continuous because \(d_0\le d_X\); the converse does not hold in general. For example, the \(H^2\)-norm is \(d_X\)-continuous on \(B_M\) but not \(d_0\)-continuous at zero, as a scaled orthonormal \(H^2\) sequence tends to zero in \(L^2\) while its \(H^2\) norm is fixed.

The previous forward report §6 assumes two existing corner-classical solutions \(i=1,2\) through \(T\), common fixed parameters/loading, and constants \(0<\theta_{\min}\le\theta_{\max}<\infty\), \(K<\infty\), such that

\[
\theta_{\min}\le\theta_i\le\theta_{\max},\quad
\|\theta_{1x}\|_\infty+\|\theta_{1t}\|_\infty+
\|\varepsilon_{2t}\|_\infty+\|w_1+w_2\|_\infty\le K.\tag{7.3}
\]

Under those **pairwise** hypotheses, that report's weighted energy estimate and (7.2) yield

\[
\|F_A(z_{01})-F_A(z_{02})\|_Y\le C\|z_{01}-z_{02}\|_{L^2(I)},\tag{7.4}
\]

with \(C\) depending on the fixed problem and the bounds in (7.3). A subset \(S\subseteq\mathcal A_T^{\rm cl}\) whose solutions satisfy the **same** finite constants in (7.3) for every ordered pair has uniformly \(d_0\)-Lipschitz, hence uniformly \(d_X\)-continuous, observations. Such a subset is not proved nonempty. Merely knowing each individual classical solution has some finite bound does not give a bound uniform for all pairs or a neighborhood; (7.4) therefore cannot be extended to all of \(\mathcal A_T^{\rm cl}\) without further work. It is not established for the weak-initial class as a whole.

## 8. General topology claims and their limits

1. **Weak sequential compactness:** proved in §3: \(B_M\) is closed and bounded in a reflexive Hilbert space. In fact it is weakly compact.
2. **Compact embedding:** proved in §3 by Rellich on the bounded interval; bounded \(H^2\) sequences have \(L^2\)-convergent subsequences. The ball is \(L^2\)-closed as shown there, hence \(L^2\)-compact.
3. **Strong closed subset is complete:** if \(S\subset B_M\) is \(H^2\)-closed, then it is closed in the complete Hilbert space \(X\) and is complete in its inherited \(d_X\). This assertion is not a claim of compactness.
4. **Strong closedness alone does not imply \(L^2\) closedness:** let \((e_n)\) be an orthonormal sequence in \(X\), set \(z_n=q e_n\) for \(0<q<M\), and \(S=\{z_n:n\ge1\}\). The points are separated in \(H^2\), so \(S\) is strongly closed. Since \(e_n\rightharpoonup0\) in \(H^2\), the compact embedding gives \(z_n\to0\) in \(L^2\), but \(0\notin S\). This general counterexample does not apply to the specially structured \(C_M\), whose \(L^2\) closedness was proved in §4.
5. **Failure of admissible-set closure is possible, not proved for A:** a simple abstract illustration is \(\{z\in B_M:0<\|z\|_2<1\}\), when nonempty, which has \(0\) as an \(L^2\) limit outside the set. An analogous failure could occur if PDE admissibility is not stable, but this illustration says nothing about whether (6.1) actually fails to be closed.
6. **General compact-to-inverse-modulus fact, not applied to A:** let \(K\) be a nonempty compact metric space in the \(L^2\) metric, let \(F:K\to Y\) be continuous and injective, and define

\[
\omega(r)=\sup\{\|z-\tilde z\|_{L^2}:z,\tilde z\in K,\ \|F(z)-F(\tilde z)\|_Y\le r\}.
\]

The diagonal ensures the set is nonempty for \(r\ge0\); compactness bounds \(\omega\). If \(\omega(r)\not\to0\), choose pairs with output distance tending to zero but state distance bounded below; compactness gives convergent subsequences, continuity gives equal limit outputs, and injectivity identifies the limits, a contradiction. Hence \(\omega(r)\to0\), a uniform inverse modulus without an asserted rate. This is a general topological implication, not an investigation or claim of injectivity of \(F_A\). It cannot be applied to either actual admissible set without proofs of nonemptiness, \(L^2\)-compactness, forward \(d_0\)-continuity, and injectivity.

## 9. Consolidated topology specification

All closedness and completeness entries name their ambient metric. **PROVED**, **CONDITIONAL**, and **UNPROVED** are the only evidence labels. For the actual sets, relative compactness in \(L^2\) is unconditional even if the set is empty.

| Set or space | Definition | Topology/metric | Nonempty? | Closed? | Complete/compact? | Status |
|---|---|---|---|---|---|---|
| \(X\) | \(H^2(I)\), full norm | strong \(H^2\) | Yes | Yes, in itself | Complete; not compact | **PROVED** |
| \(B_M\) | \(\|z\|_{H^2}\le M\) | \(d_X\); separately \(d_0\) | Yes, contains zero | Yes in \(H^2\) and \(L^2\) | Complete in both; compact in \(d_0\), not in \(d_X\); weakly sequentially compact in \(H^2\) | **PROVED** |
| \(C_M\) | \(B_M\cap\{G_0=G_L=0\}\) | \(d_X\); separately \(d_0\) | Yes, including nonzero elements | Yes in \(H^2\) and \(L^2\) | Complete in both; compact in \(d_0\), not in \(d_X\) | **PROVED** |
| \(W_M\) | \(B_M\), no corner restriction | \(d_X\); separately \(d_0\) | Yes | Yes in \(H^2\) and \(L^2\) | Same properties as \(B_M\) | **PROVED** |
| \(\mathcal A_T^{\rm cl}\) | Solution-dependent predicate (6.1), subset of \(C_M\) | \(d_X\); separately \(d_0\) | Unknown | Unknown in both | \(L^2\)-relatively compact; completeness and \(L^2\)-compactness unknown | **PROVED** relative compactness; **UNPROVED** remaining properties |
| \(\mathcal A_T^{\rm w}\) | Solution-dependent predicate (6.1), subset of \(W_M\) | \(d_X\); separately \(d_0\) | Unknown | Unknown in both | \(L^2\)-relatively compact; completeness and \(L^2\)-compactness unknown | **PROVED** relative compactness; **UNPROVED** remaining properties |
| \(Y\) | \(L^2(\delta,T)^3\) | product \(L^2\) norm | Yes, contains zero | Yes, in itself | Hilbert and complete; not compact | **PROVED** |

For either actual set, closedness would imply completeness in its respective ambient complete metric space and \(L^2\) closedness would imply \(L^2\) compactness; these are **CONDITIONAL** implications, not assertions that the sets are closed.

## 10. Final recommendation to Dr. Vipin Gupta

1. **Freeze \(H^2\) strong topology** as the primary ambient data topology, with the full norm and bounded ball specified in §3. Retain \(L^2\) as an explicitly separate weaker comparison topology; its compactness is valuable but does not replace the admissibility proof.
2. **Presently justified domains:** \(B_M=W_M\) as an explicit candidate weak-initial data set, and \(C_M\) as an explicit classical *compatibility* set. The actual predicates \(\mathcal A_T^{\rm cl}\) and \(\mathcal A_T^{\rm w}\) are precisely defined, but not justified as nontrivial solution domains.
3. **Neither actual admissible set is proved nonempty.** Nonzero elements of \(C_M\) do not prove solutions exist under the fixed actuation.
4. **Neither actual admissible set is proved \(L^2\)-compact.** Both are \(L^2\)-relatively compact; closure is missing. In contrast, \(B_M\) and \(C_M\) themselves are \(L^2\)-compact.
5. The forward observation operator is set-theoretically defined on each actual predicate and conditionally continuous on uniformly regular classical families, but **cannot currently be treated as a continuous map on a rigorously established nonempty solution-admissible domain**.

The next decision belongs to Dr. Gupta. No conclusion about inverse injectivity is made.
