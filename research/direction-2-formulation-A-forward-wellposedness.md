# Formulation A: forward well-posedness investigation

**Date:** 1 November 2026
**Decision: PARTIALLY ESTABLISHED**

## 1. Executive decision

For the unchanged experiment, the exact nonlocal reduction is verified. Initial mechanical equilibrium is solvable for every prescribed \(H^2\) memory field; a nonzero family satisfies all corner conditions needed by the particular \(C^{2,1}\)-type classical concept selected below. Under explicitly stated regularity and uniform positive-temperature hypotheses, a direct energy argument proves **forward uniqueness**, continuous dependence of the fields, and continuity of all three observation traces. Endpoint fluxes are bounded linear traces of \(L^2\)-in-time \(H^2\)-in-space temperatures. A conditional positivity estimate is proved.

**What is not established:** existence, even local in time, for the actual nonlocal nonlinear system in either proposed solution class; continuation to \(T=10/\lambda\); a priori \(\theta_*/2\) bound from the specified data; and a nonempty solution-defined admissible class for the nonzero actuation. The nonzero compatible data are **not** a construction of solutions. A formally energy-compatible model or a named general parabolic theorem does not fill these gaps. Accordingly, **the required forward framework has not been fully established**, but its compatibility, conditional uniqueness, observation and positivity components have been partially established.

**Single most important obstacle:** prove local maximal-regularity solvability for the temperature-dependent, rank-one nonlocal operator coupled to the pointwise memory ODE, and obtain a continuation estimate on the fixed horizon that also yields the required positive-temperature bound. Delayed measurement alone does not prove either existence or trace regularity. The conditional estimates below do not assume or investigate inverse injectivity.

The README and all seven existing research reports were read. The earlier formulation and audit remain binding; no file is changed except this new report. Direction 1 remains rejected as a new foundational continuum theory. Dr. Vipin Gupta is Principal Researcher and final decision-maker, ChatGPT is designated Independent Scientific Supervisor and Auditor, and Arena is Research Scholar / Builder / Literature Investigator. This is Arena's mathematical check, not evidence of a separate independent review. No novelty, new theory, simulation or manuscript is claimed.

## 2. Fixed model and exact reduction

Write \(I=(0,L)\), \(\bar f=L^{-1}\int_I f\,dx\), \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(d=b^2/D\), and \(\mu=\lambda\alpha\). All constants and the nonzero prescribed

\[
m(t)=\frac{g_*}{L}\sin^2(\pi t/T),\qquad T=10/\lambda,\qquad\delta=T/100
\]

are frozen. In particular \(b\ne0\) and \(g_*\ne0\); the sign of \(b\) is unrestricted. The unknown is \(z_0\in H^2(I)\), \(\|z_0\|_{H^2}\le M\), and \(\theta_0=\theta_*>0\). Mechanical equilibrium and \(\bar\varepsilon=m\) give

\[
\begin{aligned}
\varepsilon&=m+r p+\beta v,& \quad u(x,t)&=\int_0^x\varepsilon(y,t)\,dy,\\
\sigma&=Dm-b(\bar\theta-\theta_*)-k\bar z,&
 p&=z-\bar z,\quad v=\theta-\bar\theta,\\
\bar z_t&=\lambda(m-\bar z),&p_t&=-\mu p+\lambda\beta v.
\end{aligned}\tag{2.1}
\]

The explicit formulas are \(\bar z(t)=e^{-\lambda t}\bar z_0+\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds\) and \(p(t)=e^{-\mu t}p_0+\lambda\beta\int_0^t e^{-\mu(t-s)}v(s)ds\). Thus \(p\) has zero mean and need not have a boundary condition. Let

\[
w=m-\bar z-\alpha p+\beta v,\quad
E_0=m'+r(-\mu p+\lambda\beta v),\quad
\varepsilon_t=E_0+\beta(\theta_t-\overline{\theta_t}).\tag{2.2}
\]

The exact reduced heat equation is

\[
(c+d\theta)\theta_t-d\theta\overline{\theta_t}
=\kappa\theta_{xx}-b\theta E_0+k\lambda w^2=:H,\tag{2.3}
\]

with \(\theta(0,t)=\theta(L,t)=\theta_*\) and \(\theta(x,0)=\theta_*\). In particular the two mean terms in (2.2)–(2.3) are indispensable.

**Mean-term inversion, checked:** for positive bounded \(\theta\), \(C=c+d\theta\ge c>0\). Dividing (2.3) by \(C\) and averaging yields

\[
\overline{\theta_t}=\frac{\overline{H/C}}{\overline{c/C}},\qquad
\theta_t=\frac{H+d\theta\,\overline{H/C}/\overline{c/C}}{C}.\tag{2.4}
\]

Indeed \(1-\overline{d\theta/C}=\overline{c/C}>0\). Boundedness of \(\theta\) gives a positive lower bound on the denominator; positivity alone gives pointwise invertibility when all averages are meaningful. This is an algebraic fact, **not** maximal regularity of the resulting nonlocal unbounded operator. The nonlocal second-order contribution after inversion is a scalar average of \(\theta_{xx}/C\) multiplied by \(d\theta/C\), so a purely local scalar-parabolic theorem does not automatically apply.

Dimensional check: \(p,w,m,\varepsilon,z\) are dimensionless; \([D]=\mathrm{Pa}\), \([b]=[c]=\mathrm{Pa/K}\), \([\beta]=\mathrm{K}^{-1}\), \([d]=\mathrm{Pa/K^2}\), \([\mu]=\mathrm{s}^{-1}\). Both sides of (2.3) have units Pa/s; \(C\) has Pa/K and \(d\theta\overline{\theta_t}\) has Pa/s. Stress times area is N and \(A_0\kappa\theta_x\) is W. These checks do not supply existence.

## 3. Solution concepts and boundary conditions

### 3.1 Classical comparison class

A **corner-classical solution** on \([0,\tau]\) means: \(\theta,\theta_t,\theta_x,\theta_{xx}\) are continuous on \([0,L]\times[0,\tau]\); \(p,p_t\) are continuous there; \(\bar z\in C^1[0,\tau]\); the equations hold in the interior and extend to the initial corners; \(\theta>0\); and the initial and boundary conditions hold pointwise. Reconstruct \(z,u,\varepsilon,\sigma\) by (2.1). The data \(z_0\in H^2(I)\) have continuous representatives in one dimension. One may impose additional Hölder regularity for a Schauder-based construction, but that is a **sufficient regularity choice**, not part of this definition and not itself an existence proof. This definition asks for one time and two spatial derivatives, not arbitrary higher derivatives.

The only corner conditions forced at this order are matching the initial/boundary temperature values and matching the PDE's initial \(\theta_t\) at both endpoints to the time derivative of the boundary values. The explicit conditions are in §4. They are **necessary** for the defined class; their sufficiency for a nonlinear solution is unproved. For a more regular class in which \(\partial_t^j\theta\) extends to the corners, further necessary conditions are obtained by differentiating (2.3) \(j-1\) times in time, using (2.1), and requiring \(\partial_t^j\theta(i,0)=0\), \(i=0,L\). Those extra derivatives and their compatibility are **not** required in the chosen class; no claim of sufficiency for any higher-order hierarchy is made.

### 3.2 Proposed strong/weak-initial framework

The more useful target allows an initial boundary layer, while requiring enough smoothing to read calorimeters. For \(\tau\le T\), set \(y=\theta-\theta_*\). A candidate **strong temperature / weak-initial solution** is

\[
y\in H^1(0,\tau;L^2(I))\cap L^2(0,\tau;H^2(I)\cap H^1_0(I)),\quad
z\in H^1(0,\tau;L^2(I)),\tag{3.1}
\]

with \(y(0)=0\) in \(L^2\), \(z(0)=z_0\) in \(L^2\), (2.1) and (2.3) holding almost everywhere, and \(\theta\ge\theta_*/2\) almost everywhere. The time-Sobolev spaces provide continuous \(L^2\) representatives. From (2.1), \(\varepsilon\in H^1(0,\tau;L^2)\), \(u\in H^1(0,\tau;H^1(I))\), and the two displacement endpoint values hold in the one-dimensional Sobolev trace sense for all times of the continuous representative. The condition \(y(t)\in H^1_0(I)\) for almost every \(t\) gives precisely \(\theta(i,t)=\theta_*\) in the Dirichlet trace sense, \(i=0,L\). There is no initial \(\theta_t\) corner trace in (3.1), so the first-order classical corner condition is not imposed as part of this definition.

To make the products in (2.3) unambiguous in \(L^2\), additionally require \(\theta,p,w\in L^\infty((0,\tau)\times I)\). For \(H^2\) initial \(z_0\), if a solution has \(y\in L^2_tH^2_x\), the representation (2.1) indeed yields bounded \(p\): \(H^2(I)\hookrightarrow L^\infty(I)\), and \(\int_0^\tau\|y(s)\|_\infty ds<\infty\). The definition is meaningful but its existence, uniqueness at this exact weak-initial regularity and initial-data continuity are **UNPROVED** here. In particular, the conditional uniqueness theorem in §6 requires stronger coefficient bounds and is not asserted for every solution in (3.1).

An even weaker energy-space temperature \(y\in L^2_tH^1_0\), \(y_t\in L^2_tH^{-1}\), would require a separately justified weak meaning of the products \(\theta\varepsilon_t\) and \(w^2\); boundary normal derivatives are not automatically in \(L^2\). A mild formulation would use Duhamel's formula **only after** an appropriate generator/evolution family is established for the nonlocal principal operator. Neither ordinary heat-kernel smoothing nor an ODE integrating factor proves this. Thus (3.1), or a rigorously justified time-weighted analogue with the same delayed \(H^2\) trace regularity, is the recommended useful target, **not** an already established framework.

## 4. Initial and boundary compatibility

At \(t=0\), the prescribed actuation satisfies \(m(0)=m'(0)=0\), and the temperature is spatially constant. For every \(z_0\in H^2\), the unique initial quasistatic equilibrium is

\[
p_0=z_0-\bar z_0,\quad \varepsilon_0=r p_0,\quad
u_0(x)=r\int_0^x p_0(y)dy,\quad \sigma_0=-k\bar z_0.\tag{4.1}
\]

Both endpoint displacements are zero. Thus initial displacement compatibility and the zeroth-order temperature compatibility hold throughout the full \(H^2\) ball. Physical accessibility from a real preparation is a separate unproved issue.

For the corner-classical concept, let \(w_0=-\bar z_0-\alpha p_0\) and \(C_*=c+d\theta_*\). Since \(\theta_{xx}(x,0)=0\), averaging (2.3) gives

\[
\overline{\theta_t}(0)=\frac{k\lambda}{c}\overline{w_0^2},\quad
C_*\theta_t(x,0)=b\theta_*r\mu p_0(x)+k\lambda w_0(x)^2+
\frac{d\theta_*k\lambda}{c}\overline{w_0^2}.\tag{4.2}
\]

The necessary and exhaustive conditions **at this differential order** are that the right-hand side in (4.2) vanish at \(x=0\) **and** at \(x=L\). Their derivation uses continuous \(\theta_t,\theta_{xx}\) through the corners; they are not necessary for every weak-initial solution. They are not proven sufficient for a solution. Every nonzero constant \(z_0=s\) violates both conditions: the right-hand side is \(k\lambda s^2(1+d\theta_*/c)>0\). Such constants of arbitrarily small magnitude lie in any positive-radius \(H^2\) ball, so the full ball is **not** corner-classically compatible.

The necessary conditions nevertheless admit a **nontrivial explicitly constructed data family**. For small \(s\), set

\[
z_0(x)=s\sin(2\pi x/L)+h(s)\cos(2\pi x/L),\quad \bar z_0=0,
\]

where \(h(s)\) is defined locally by

\[
b\theta_*r\mu h+k\lambda\alpha^2\left[h^2+\frac{d\theta_*}{2c}(s^2+h^2)\right]=0.\tag{4.3}
\]

Both endpoint values equal \(h\) and \(\overline{z_0^2}=(s^2+h^2)/2\), so (4.3) imposes both equations in (4.2). The left side is smooth, vanishes at \((0,0)\), and its \(h\)-derivative there is \(b\theta_*r\mu\ne0\). The finite-dimensional implicit-function theorem gives a unique smooth \(h(s)\) locally, \(h(0)=h'(0)=0\), hence \(h(s)=O(s^2)\). For sufficiently small nonzero \(s\), \(z_0\ne0\), its \(H^2\) norm is below any given \(M>0\), and all compatibility conditions *required by §3.1* hold. This is a nonempty compatible **data** set, not a nonempty set of solutions. The nonzero fixed \(g_*\) remains in force; it does not enter the first condition because \(m'(0)=0\).

## 5. Existence, local continuation and exact points where arguments stop

The heat equation without its nonlocal coefficient is a standard Dirichlet parabolic equation; the memory equation alone is an explicitly solvable ODE in a function space. Their combination is not automatically covered by adding two standard conclusions: (2.4) turns the highest-order operator into a temperature-dependent multiplication **plus a nonlocal rank-one term acting on \(\theta_{xx}\)**, and the memory evolution feeds back into the source. A product-space evolution would have a parabolic temperature block and an ODE block, not a uniformly parabolic system in all components. For (3.1), a proof must also treat time-dependent coefficients, the nonlocal operator domain, nonlinear products, Dirichlet traces and data-to-solution dependence. One cannot simply treat the nonlocal term as a bounded perturbation on \(L^2\): \(\theta\mapsto\overline{\theta_{xx}/C}\) is not bounded on \(L^2\), and the boundary domain matters.

**Status by requested component:**

| Component | Finding |
|---|---|
| Local existence for fixed \(z_0\) and nonzero \(g_*\) | **UNPROVED** in both §3 classes. No local time is asserted. |
| Uniqueness | **PROVED conditionally** in the classical/uniform-coefficient class by §6. Not established for all weak-initial solutions (3.1). |
| Continuation to \(T\) | **UNPROVED**. A formal first law is not an \(H^2\), \(\theta_t\), or temperature upper-bound estimate. A continuation criterion itself requires a local theorem with a specified phase space. |
| Data dependence | **PROVED conditionally** on an actual uniformly regular family by §6; existence and continuity of such a family are not established. |
| Boundary conditions | **PROVED conditional on the chosen solution existing:** the reconstructed displacement satisfies its endpoints, and (3.1) imposes the bath values as Sobolev traces. |
| Nonempty active-experiment solution class | **UNPROVED** even for the compatible family in §4, and even for \(z_0=0\). Zero memory with a nonzero \(g_*\) is not an equilibrium solution. |

A possible route, not a theorem application, is to freeze a positive \(\theta\), establish maximal \(L^2\) regularity of the Dirichlet realization of \(M_\theta^{-1}\kappa\partial_{xx}\), where \(M_\theta h=(c+d\theta)h-d\theta\bar h\), then prove Lipschitz dependence on coefficients, couple the memory ODE, and close a contraction or quasilinear fixed point. The algebraic positivity of \(M_\theta\) in a weighted pairing (§6) is useful, but it does not by itself establish this entire operator theory. A second step would need a parameter-explicit small-data finite-horizon estimate; no smallness threshold for the actual \(g_*\) has been derived.

## 6. Conditional uniqueness and continuous dependence: direct proof

This section proves a forward estimate, not an existence theorem. Let \((\theta_i,p_i,\bar z_i)\), \(i=1,2\), be two **existing corner-classical solutions** on \([0,\tau]\), with identical fixed parameters, loading and initial/boundary temperature but possibly different \(z_{0i}\). Suppose for some constants \(0<\theta_{\min}\le\theta_{\max}<\infty\), \(K<\infty\),

\[
\theta_{\min}\le\theta_i\le\theta_{\max},\quad
\|\theta_{1x}\|_\infty+\|\theta_{1t}\|_\infty+
\|\varepsilon_{2t}\|_\infty+\|w_1+w_2\|_\infty\le K.\tag{6.1}
\]

For classical solutions on a compact cylinder these bounds hold with solution-dependent constants. Denote differences \(V=\theta_1-\theta_2\), \(P=p_1-p_2\), \(Z=\bar z_1-\bar z_2\), \(W=w_1-w_2\). Then \(V\) has zero initial and Dirichlet values, and

\[
Z_t=-\lambda Z,\quad P_t=-\mu P+\lambda\beta(V-\bar V),\quad
W=-Z-\alpha P+\beta(V-\bar V).\tag{6.2}
\]

Subtract the **original** thermal equations and use (6.2), with \(d=b\beta\). The exact difference equation is

\[
(c+d\theta_1)V_t-d\theta_1\overline{V_t}-\kappa V_{xx}
=-bV\varepsilon_{2t}-b\theta_1 rP_t+k\lambda(w_1+w_2)W=:R.\tag{6.3}
\]

All coefficients and signs follow from \(\varepsilon_{1t}-\varepsilon_{2t}=rP_t+\beta(V_t-\overline{V_t})\). The mean term is retained. Divide by \(\theta_1\), multiply by \(V_t\), and integrate over \(I\). Since

\[
\int_I\left(\frac c{\theta_1}+d\right)V_t^2dx-dL\overline{V_t}^{\,2}
\ge \frac c{\theta_{\max}}\|V_t\|_{L^2}^2,\tag{6.4}
\]

by Cauchy–Schwarz, the **weighted** time-derivative form is coercive. This calculation is valid for either sign of \(b\) because \(d=b^2/D>0\). Integrating \(V_{xx}\) by parts uses \(V_t=0\) at both endpoints for the classical class. With

\[
\mathcal E(t)=\frac\kappa2\int_I\frac{|V_x|^2}{\theta_1}dx,
\]

we get the exact identity

\[
\begin{aligned}
\int_I\left(\frac c{\theta_1}+d\right)V_t^2dx-dL\overline{V_t}^{\,2}
+\mathcal E'(t)
&=\int_I\frac{R V_t}{\theta_1}dx
+\kappa\int_I\frac{V_xV_t\theta_{1x}}{\theta_1^2}dx\\
&\quad-\frac\kappa2\int_I\frac{|V_x|^2\theta_{1t}}{\theta_1^2}dx.
\end{aligned}\tag{6.5}
\]

The sign of the last term follows by differentiating \(\theta_1^{-1}\). By (6.1)–(6.2), Poincaré's inequality and Young's inequality, for a constant \(C\) depending only on the stated bounds and fixed parameters,

\[
\mathcal E'(t)+\frac{c}{2\theta_{\max}}\|V_t\|_2^2
\le C\bigl(\|V_x\|_2^2+\|P\|_2^2+|Z|^2\bigr).\tag{6.6}
\]

Here and below \(\|\cdot\|_2\) is the spatial \(L^2(I)\) norm; constants may absorb the fixed factor \(L\) associated with a spatially constant \(Z\). Moreover,

\[
\frac d{dt}(\|P\|_2^2+L|Z|^2)
\le C(\|P\|_2^2+L|Z|^2+\|V_x\|_2^2).\tag{6.7}
\]

Because \(\mathcal E\) is equivalent to \(\|V_x\|_2^2\), \(V(0)=0\), and \(\|P(0)\|_2^2+L|Z(0)|^2=\|z_{01}-z_{02}\|_2^2\), Gronwall's inequality gives

\[
\sup_{0\le t\le\tau}\!\left(\|V(t)\|_{H^1}^2+\|P(t)\|_2^2+L|Z(t)|^2\right)
+\int_0^\tau\|V_t\|_2^2dt
\le C\|z_{01}-z_{02}\|_2^2.\tag{6.8}
\]

Finally (6.3) gives \(\|V_{xx}\|_2\le C(\|V_t\|_2+\|P\|_2+|Z|+\|V\|_2)\), including the \(\overline{V_t}\) term. Integrating in time yields

\[
\|V\|_{L^2(0,\tau;H^2)}+\|V_t\|_{L^2(0,\tau;L^2)}+
\sup_t\bigl(\|V(t)\|_{H^1}+\|z_1(t)-z_2(t)\|_2\bigr)
\le C\|z_{01}-z_{02}\|_2.\tag{6.9}
\]

If the initial memory fields agree, (6.9) proves equality of temperature and memory, and then (2.1) proves equality of strain, displacement and stress. This is uniqueness **within the specified existing-solution class**, not existence or uniqueness among every weaker solution. The estimate extends to another class only after the integration-by-parts and bounded coefficient hypotheses are justified there. Uniform constants in (6.1) over a family make (6.9) uniform on that family; if the constants vary without a common bound, no uniform continuity assertion follows.

## 7. Positive-temperature estimates

Take any existing classical solution on \([0,\tau]\) with \(\varepsilon_t\) bounded. Set

\[
B(t)=\max\{0,\operatorname*{ess\,sup}_{x\in I}[b\varepsilon_t(x,t)/c]\},\quad
\underline\theta(t)=\theta_*\exp\!\left(-\int_0^tB(s)ds\right).\tag{7.1}
\]

The exact original equation gives

\[
\theta_t-\frac\kappa c\theta_{xx}+\frac{b\varepsilon_t}{c}\theta
=\frac{k\lambda}{c}w^2\ge0.\tag{7.2}
\]

The function \(\underline\theta\) is a spatially constant subsolution because \(-B+b\varepsilon_t/c\le0\); it does not exceed either bath value \(\theta_*\), and equals the initial temperature. The parabolic comparison principle, or multiplying the difference equation by the negative part and applying Gronwall, therefore yields

\[
\theta(x,t)\ge\theta_*\exp\!\left(-\int_0^t B(s)ds\right)>0.\tag{7.3}
\]

This is strict **and** uniform positivity on any finite interval on which \(B\in L^1\), with an explicit solution-dependent lower bound. The specific \(\theta_*/2\) bound follows if

\[
\int_0^T B(s)ds\le\log2.\tag{7.4}
\]

This condition is sufficient, not necessary. It does not imply existence and is not yet an explicit condition on data alone.

To expose the missing a priori estimate, assume for an existing solution that
\(\|p_0\|_\infty\le P\), \(\|\theta-\bar\theta\|_{L^\infty((0,T)\times I)}\le V_*\), and \(\|\theta_t\|_{L^\infty((0,T)\times I)}\le H_*\). Formula (2.1) gives \(\|p(t)\|_\infty\le P+\lambda|\beta|tV_*\). Since \(\|m'\|_\infty=\pi|g_*|/(LT)\) and \(\|\theta_t-\overline{\theta_t}\|_\infty\le2H_*\), (2.2) gives the explicit bound

\[
\|\varepsilon_t\|_\infty\le E_*:=\frac{\pi|g_*|}{LT}
+r\{\mu(P+\lambda|\beta|TV_*)+\lambda|\beta|V_*\}+2|\beta|H_*.\tag{7.5}
\]

Consequently \(\theta\ge\theta_*/2\) if \((|b|/c)TE_*\le\log2\). \(P\) can be controlled by the initial \(H^2\) norm via the one-dimensional Sobolev embedding, but \(V_*\) and \(H_*\) are **assumed solution bounds**, not proved functions of the known parameters, \(M\) and \(g_*\). Thus (7.5) is a checkable conditional criterion, not an independently verified data-only smallness theorem. Strict positivity alone is weaker than the original specification's \(\theta_*/2\) requirement.

## 8. Boundary observations and continuity

The requested outputs on \((\delta,T)\) are

\[
F_m=A_0\sigma,\qquad Q_0=A_0\kappa\theta_x(0,\cdot),\qquad
Q_L=-A_0\kappa\theta_x(L,\cdot).\tag{8.1}
\]

For any actual solution with \(\theta-\theta_*\in L^2(\delta,T;H^s(I))\) for some \(s>3/2\), the one-dimensional Sobolev trace theorem gives \(\theta_x(0,\cdot),\theta_x(L,\cdot)\in L^2(\delta,T)\). The stronger but convenient sufficient hypothesis \(L^2(\delta,T;H^2(I))\) supplies the direct estimate

\[
|f'(0)|^2+|f'(L)|^2\le C_L\|f\|_{H^2(I)}^2,\quad f\in H^2(I).\tag{8.2}
\]

Indeed \(f'\in H^1(I)\) has continuous endpoint traces, bounded by its \(H^1\) norm; integrate (8.2) in time. This is a **sufficient** and near-threshold spatial condition, not a claim that \(s>3/2\) is the weakest possible anisotropic/hidden-trace hypothesis for solutions of a PDE. For the force it suffices that \(\bar\theta,\bar z\in L^2(\delta,T)\), since \(m\) is smooth; this follows from (3.1). At the baseline energy level \(y\in L^2_tH^1_0\), endpoint traces of \(y_x\) are not provided by the trace theorem. \(\delta>0\) permits an initial layer but **does not itself prove** delayed \(H^s\) regularity for this coupled system.

On a family of existing classical solutions satisfying the **same** constants in (6.1), (6.9), (8.2), (2.1) and the boundedness of spatial averaging imply the proved estimate

\[
\|F_A(z_{01})-F_A(z_{02})\|_{L^2(\delta,T)^3}
\le C\|z_{01}-z_{02}\|_{L^2(I)}.\tag{8.3}
\]

Thus the forward observation map is well-defined and Lipschitz continuous **on any such actual family**, assuming both solutions exist through \(T\); the constants depend on its uniform regularity/temperature bounds, parameters and \(T\). This conditional statement does not prove the family is nonempty or that every member of the original \(H^2\) ball belongs to it. The weaker proposal (3.1) would directly define fluxes even without delay if existence in that space were proved; a merely local-in-positive-time version needs \(L^2(\delta,T;H^2)\), including integrability up to \(T\).

## 9. Theorem and source verification ledger

The named elementary results used in the proof are stated below with their hypotheses in the form actually used. They are not asserted to solve the nonlinear forward problem.

| Result and verification | Hypotheses actually used; conclusion and applicability |
|---|---|
| Finite-dimensional implicit-function theorem | A \(C^1\) map \(G:\mathbb R^2\to\mathbb R\) near \((0,0)\), \(G(0,0)=0\), \(\partial_hG(0,0)\ne0\), gives a locally unique \(C^1\) function \(h(s)\) satisfying \(G(s,h(s))=0\); smooth \(G\) gives smooth \(h\). Directly applicable to the polynomial in (4.3), whose derivative is nonzero under frozen parameter conditions. This proves compatible **data**, not PDE solutions. |
| One-dimensional Sobolev trace and Poincaré inequalities | On finite \((0,L)\), \(H^1\) functions have endpoint traces bounded by the \(H^1\) norm; \(H^1_0\) functions satisfy \(\|f\|_2\le C_L\|f_x\|_2\). Applying the first to \(f'\in H^1\) proves (8.2); applying the second to \(V\) gives (6.6). These are elementary interval results; no hidden PDE trace theorem is invoked. |
| Parabolic comparison / negative-part estimate | \(\kappa/c>0\); a sufficiently regular solution, bounded coefficient \(b\varepsilon_t/c\), nonnegative source, initial and Dirichlet values at least the subsolution. Then \(\theta\) stays above the subsolution; alternatively the negative part obeys a Gronwall inequality. Applies to (7.2) only **after** a solution with the stated coefficient bound exists. |
| Gronwall inequality | If a nonnegative absolutely continuous \(Y\) obeys \(Y'\le CY\) a.e. with finite \(C\), then \(Y(t)\le Y(0)e^{Ct}\). Applied to (6.6)–(6.7), after adding a positive multiple of the memory norms; the dissipative \(V_t\) term integrates to (6.8). All constants in the proof require (6.1). |
| Lindemulder, [*Maximal Regularity with Weights for Parabolic Problems with Inhomogeneous Boundary Conditions*](https://arxiv.org/html/1702.02803), arXiv:1702.02803v2, introduction and Theorem 3.4/Example 3.6 consulted | Source studies **linear** vector-valued differential parabolic operators on smooth domains, with ellipticity and Lopatinskii–Shapiro conditions, specified UMD and weighted trace spaces; under its detailed assumptions its theorem gives maximal regularity, and certain weights avoid some compatibility conditions. These are not a verified match to the temperature-dependent nonlocal rank-one highest-order operator in (2.4), nor to the ODE-coupled nonlinear equation. It is a possible method/reference, **not invoked as an existence theorem for A**. |
| [Parabolic equations with dynamical boundary conditions and source terms on interfaces](https://link.springer.com/article/10.1007/s10231-013-0329-7), full publisher text, introduction and quasilinear section inspected | The source studies a different divergence-form problem with mixed/dynamical/interface conditions. Its quasilinear theorem requires, among other detailed assumptions, maximal parabolic regularity for the frozen operators and the stated interpolation/data hypotheses. Those hypotheses are not verified for \(M_\theta^{-1}\partial_{xx}\) and coupled memory, so its conclusion is not imported. |
| [*A model in one-dimensional thermoelasticity*](https://arxiv.org/abs/2003.03806), arXiv:2003.03806, accessible abstract and search-indexed primary PDF introduction; direct PDF retrieval failed | Source reports local strong existence/uniqueness and positive-temperature discussion for a **different dynamic hyperbolic–parabolic** model, with its own data and boundary conditions. The complete theorem hypotheses and proof were not independently checked here; no theorem is applied to A. |

The source search was focused, not exhaustive. Lindemulder's linear theorem and the interface paper can guide a future proof but do not establish the required nonlocal operator assumptions. The older inaccessible memory/thermoelastic sources remain documented in the prior audit. No theorem has been attributed from an unavailable full text.

## 10. Unproved claims, limits and recommendation

- **UNPROVED:** a local solution for any nonzero active loading and any candidate \(z_0\), including the formally compatible family; an a priori continuation criterion and existence through \(T\).
- **UNPROVED:** a data-only threshold involving only \(a,k,\lambda,c,\kappa,b,\theta_*,L,M,g_*\) that ensures \(\theta\ge\theta_*/2\). Equations (7.4)–(7.5) require actual solution bounds.
- **UNPROVED:** nonempty admissible solution class, smoothing for weak-initial solutions, weak-class uniqueness and continuity, or the existence of a uniformly bounded family to which (8.3) applies. An implicitly defined admissible class may be empty.
- **PROVED conditionally:** exact reduction and weighted coercivity; compatibility conclusions; comparison bound; classical-class uniqueness and forward continuity under (6.1); trace regularity under (8.2). These are not unconditional forward well-posedness.
- **Not investigated:** inverse injectivity, inverse stability, simulations, publication, new continuum theory, or preparation procedures. None is authorized by this audit.

**Recommendation to Dr. Vipin Gupta:** accept **PARTIALLY ESTABLISHED**, not a full forward framework. The next scientific decision is yours. If further forward analysis is authorized, prioritize a precise maximal-regularity or direct fixed-point proof for the nonlocal operator and an explicit finite-horizon estimate under the unchanged loading, followed by proof that delayed fluxes and \(\theta_*/2\) hold for a genuinely nonempty class. Do not infer failure or success of the physical experiment from the present proof gap.
