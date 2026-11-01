# Recalculation of the finite-prior proof

**Decision: VERIFIED AS WRITTEN**, conditional on the explicitly cited active-base fixed-point/strong-solution hypotheses and their fixed numerical unit convention. This is a fresh calculation by Arena in the same environment, **not an independent human certification**; the designated Independent Scientific Auditor has not certified it. The unspecified experimental load has not been checked. The earlier report is unchanged.

## Model and inherited hypotheses

On \(I=(0,L)\), \(Q_T=(0,T)\), with \(T=10/\lambda\), \(m=g_*\sin^2(\pi t/T)/L\), \(q=|g_*|/L>0\), the active base has \(z_0=0\) and the original displacement, heat-bath and initial data of `direction-2-active-base-existence-and-regularity.md` §1. Constants are interpreted after fixing one consistent numerical unit system, or by first nondimensionalizing. The prior \(H^2\) and \(\mathcal E\) norm sums are not unit-invariant formulas; in particular none of these numerical tests can be converted by simply replacing meters by millimeters without transforming all constants. We retain that limitation rather than claim a new dimensional material threshold.

We invoke the inherited fixed-point solution for \(0<q<q_0=s_*/2\), its bound \(\|y_b\|_{\mathcal E}\le2C_Bq\), its positive temperature, and its odd strong forced-solution result. We recheck the bounds needed below, not a separate proof of all global uniqueness claims in the source. Let \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(d=b^2/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(Q=I-\langle\cdot\rangle\). With \(E_b=m'+rp_{b,t}\), \(w_b=m-v_b-\alpha p_b+\beta Qy_b\), the actual coefficients are
\[
M=c+d(\theta_*+y_b),\quad B=-dQy_{b,t}-bE_b-br\gamma(\theta_*+y_b)+2k\gamma w_b,\quad S=\mu[br(\theta_*+y_b)-2kw_b].
\]
The actual linear initial-state problem is \(MY_t-\kappa Y_{xx}=BY+SP,\ P_t+\mu P=\gamma Y,\ (Y,P)(0)=(0,h)\), \(Y|_{\partial I}=0\), observation \(\mathcal Th=2A_0\kappa Y_x(0,\cdot)|_{(\delta,T)}\). The coefficients are even and \(h\) odd, so \(QY=Y\). No thermal derivative of \(M\) or boundary condition on \(P\) is used.

## 1. Coefficient constants from the actual base

Let \(K=\sqrt L\), \(S_L=\sqrt{L^{-1}+L}\), and \(A_s,A_R,W_s,W_R,C_B,s_*\) be precisely those in (5)–(7) of the inherited base report. \(\|Q\|_{L^2\to L^2}=1\), \(\|Q\|_{L^\infty\to L^\infty}\le2\). Because \(y_b\in C_tH^1_0\), \(|y_b(x,t)|\le\sqrt L\|y_{b,x}(t)\|_2\), hence \(\|y_b\|_\infty\le 2KC_Bq=:C_yq\). With \(p_b(0)=v_b(0)=0\), directly from the full-time Volterra formulas,
\[
\|p_b\|_\infty\le2|\gamma|TK\|y_b\|_{\mathcal E},\quad
\|E_b\|_\infty\le (\pi/T)q+2r|\gamma|(1+\mu T)K\|y_b\|_{\mathcal E}
\le(A_s+2C_BA_R)q,
\]
\[
\|w_b\|_\infty\le 2q+2|\beta|(1+\alpha\lambda T)K\|y_b\|_{\mathcal E}\le (W_s+2C_BW_R)q=:C_wq.
\]
Here \(\|v_b\|_\infty\le q\), \(|m|\le q\), \(|m'|\le\pi q/T\), and the last \(E\)-estimate is conservative since \(A_s\ge\pi/T\). The bounds use neither time traces of \(y_t\) nor pointwise bounds on \(Qy_t\).

Set \(M_0=c+d\theta_*\), \(B_0=-br\gamma\theta_*\), \(S_0=\mu br\theta_*\), \(D_M=dC_y\), \(D_S=\mu(|br|C_y+2kC_w)\),
\[
D_B=2dC_B+\sqrt{LT}\{ |b|(A_s+2C_BA_R)+|br\gamma|C_y+2k|\gamma|C_w\}.
\]
Then \(\|M-M_0\|_\infty\le D_Mq\), \(\|S-S_0\|_\infty\le D_Sq\), and, using only the \(L^2\)-contraction of \(Q\),
\[
\|B-B_0\|_{L^2(Q_T)}\le d\|y_{b,t}\|_2+\sqrt{LT}\bigl(|b|\|E_b\|_\infty+|br\gamma|\|y_b\|_\infty+2k|\gamma|\|w_b\|_\infty\bigr)\le D_Bq.
\]
\(M=c+d\theta_b\ge c\) because the base is positive; \(\sqrt{LT}\) appears only when a spacetime supremum is converted to an \(L^2(Q_T)\) norm. \(B\) itself is not assumed bounded in spacetime.

## 2. Reference Gram, from scratch

\(b\gamma=\lambda b^2/D>0\), so \(B_0<0\), \(S_0\ne0\), \(d_0=\gamma S_0/M_0>0\). For the constant comparison system, not the physical experiment, \(\phi_n=c_L\sin(q_nx)\), \(c_L=\sqrt{2/L}\), \(q_n=2\pi n/L\), \((Y^0,P^0)=(u_n,v_n)\phi_n\). Its matrix is
\[
\begin{pmatrix}-a_n&S_0/M_0\\\gamma&-\mu\end{pmatrix},\quad a_n=(\kappa q_n^2-B_0)/M_0>0.
\]
Its characteristic polynomial \(z^2+(a_n+\mu)z+a_n\mu-d_0\) has roots
\[
\lambda_{n,\pm}=-\tfrac12(a_n+\mu)\pm\sqrt{(a_n-\mu)^2/4+d_0}.
\]
\(a_n\mu-d_0=\mu\kappa q_n^2/M_0>0\), and evaluation at \(-\mu\) gives \(-d_0<0\), so \(\lambda_{n,-}<-\mu<\lambda_{n,+}<0\). Derivatives of both roots in \(a\) are \(-1/2\pm(a-\mu)/(4\sqrt{(a-\mu)^2/4+d_0})<0\). Increasing \(n\) strictly increases \(a_n\), making each branch strictly decreasing; the two branches are separated by \(-\mu\). Thus no roots coincide even across different modes.

The initial conditions \(u_n(0)=0\), \(v_n(0)=1\) imply \(u_n'(0)=S_0/M_0\), hence
\[
u_n(t)=\frac{S_0}{M_0\Delta_n}(e^{\lambda_{n,+}t}-e^{\lambda_{n,-}t}),\quad \Delta_n=\lambda_{n,+}-\lambda_{n,-}>0,\quad k_n^0=2A_0\kappa c_Lq_nu_n.
\]
Both exponential coefficients are nonzero. If a linear combination vanishes in \(L^2(\delta,T)\), continuity makes it zero everywhere on that open interval; real analyticity and the Vandermonde determinant of its \(2N\) distinct exponents imply every coefficient is zero. Consequently \(G_N=(\int_\delta^T k_m^0 k_n^0)\) is positive definite and \(\sigma_N=\sqrt{\lambda_{\min}(G_N)}>0\). Positive delay is permitted, but \(\delta<T\) is essential. The normalization \(\phi_n'(0)=c_Lq_n\) and the physical factor \(2A_0\kappa\) are exact.

## 3. Comparison forcing

Subtract the actual and reference equations in the direction \(u=Y-Y^0\), \(p=P-P^0\). Initial values cancel exactly and
\[
Mu_t-\kappa u_{xx}=Bu+Sp+F,\quad p_t+\mu p=\gamma u,\quad F=-(M-M_0)Y_t^0+(B-B_0)Y^0+(S-S_0)P^0.
\]
This is a direct subtraction of both ODEs, so their whole initial-to-current memory is already present; there is no additional source or reset at \(\delta\). Let \(c_n=|S_0|/(M_0\Delta_n)\), and
\[
f_n=D_M\sqrt T c_n(|\lambda_{n,+}|+|\lambda_{n,-}|)+2D_Bc_Lc_n+D_S\sqrt T(1+2|\gamma|Tc_n),\quad H_N=(\sum_{n=1}^N f_n^2)^{1/2}.
\]
All roots are negative, whence \(|u_n|\le2c_n\), \(|u'_n|\le c_n(|\lambda_{n,+}|+|\lambda_{n,-}|)\). The exact ODE formula gives \(|v_n|\le 1+2|\gamma|Tc_n\). For a single mode, the \(B\)-term uses \(\|B-B_0\|_2\|Y_n^0\|_\infty\le D_Bq\,2c_Lc_n\), not \(\|B-B_0\|_\infty\). The other two use \(L^\infty\times L^2\). Apply the triangle inequality and Cauchy–Schwarz over the finite coefficients to obtain \(\|F\|_{L^2(Q_T)}\le qH_N\|h\|_2\). No hidden constant depends on \(h\) or \(q\).

## 4. Energy, trace, and exact constants

Let \(X=\kappa\|u_x\|_2^2+\|p\|_2^2\), and \(P_L=L/\pi\). Test the heat equation by \(2u_t\), the ODE by \(2p\). With \(M\ge c\), three applications of \(2ab\le(c/3)a^2+(3/c)b^2\), and \(2|\gamma|\|p\|_2\|u\|_2\le\|p\|_2^2+\gamma^2\|u\|_2^2\), give
\[
X'+c\|u_t\|_2^2\le C(t)X+(3/c)\|F\|_2^2,\quad
C(t)=1+\gamma^2P_L^2/\kappa+(3/c)[(L/\kappa)\|B(t)\|_2^2+\|S(t)\|_\infty^2].
\]
We used \(\|u\|_\infty^2\le L\|u_x\|_2^2\), \(\|u\|_2\le P_L\|u_x\|_2\), and dropped \(-2\mu\|p\|_2^2\). Put \(B_* = |B_0|\sqrt{LT}+D_Bq_0\), \(S_*=|S_0|+D_Sq_0\), \(M_*=M_0+D_Mq_0\),
\[
\Xi=T(1+\gamma^2P_L^2/\kappa)+(3/c)[(L/\kappa)B_*^2+TS_*^2],\quad E_*=(3/c)e^\Xi,\quad U_*^2=(3/c^2)(1+\Xi e^\Xi).
\]
By triangle inequality \(\|B\|_{L^2(Q_T)}\le B_*\); hence \(\int C\le\Xi\). Gronwall with zero initial data gives \(\sup X\le E_*\|F\|_2^2\). Integrating the differential inequality and using \(\int C X\le\Xi E_*\|F\|_2^2\) gives \(\|u_t\|_2\le U_*\|F\|_2\). Rearranging the PDE yields
\[
\|u_{xx}\|_2\le V_*\|F\|_2,\quad V_* =\kappa^{-1}[M_*U_*+\sqrt{L/\kappa}B_*\sqrt{E_*}+S_*\sqrt{TE_*}+1].
\]
For a.e. time, fundamental theorem of calculus and Cauchy–Schwarz show \(|u_x(0)|^2\le L^{-1}\|u_x\|_2^2+2\|u_x\|_2\|u_{xx}\|_2\); the older bound with \(2/L\) is conservative. Thus
\[
2A_0\kappa\|u_x(0,\cdot)\|_{L^2(J)}\le C_{\rm tr}\|F\|_2,\quad
C_{\rm tr}=2A_0\kappa\sqrt{2TE_*/(\kappa L)+2\sqrt{TE_*/\kappa}\,V_*}.
\]
The actual odd strong forced theorem justifies the tests and the \(H^2\) trace. Combining with §3 and the Gram bound proves
\[\|\mathcal Th\|_{L^2(J)}\ge(\sigma_N-C_{\rm tr}qH_N)\|h\|_2\ge\tfrac12\sigma_N\|h\|_2\]
for \(0<q<\min\{q_0,\sigma_N/(2C_{\rm tr}H_N)\}\). The latter is mathematically positive under the stated signs, but not empirically verified.

## 5. Line-by-line disposition

| Item | Recalculation | Disposition |
|---|---|---|
| \(M,S\) | Direct coefficient identities and base supremum bounds | Correct |
| \(B\) | \(Q\) is an \(L^2\) contraction; only bounded terms gain \(\sqrt{LT}\) | Correct |
| Reference eigenvalues | Negative, distinct, branches straddle \(-\mu\) | Correct |
| Gram on \(J\) | Finite entire exponential sum plus Vandermonde, not numerical rank | Correct |
| Flux and sine factors | \(\phi'_n(0)=\sqrt{2/L}q_n\) | Correct |
| Error ODE/forcing | Subtract both entire histories; initial error zero | Correct |
| \(H_N\) | \(B\) treated in \(L^2\), reference response in \(L^\infty\) | Correct |
| Gronwall \(\Xi,E_*,U_*\) | Three Young terms; integrated \(\|B\|^2\) | Correct |
| \(V_*,C_{tr}\) | PDE then endpoint trace over all \((0,T)\) | Correct, conservative |
| Uniformity | Only fixed \(N\); no uniform \(N\) constant or fixed experimental amplitude | Essential restriction |
| Units | Existing mixed norms interpreted in fixed units or nondimensionalized | Essential qualification |
| Foundational proof | Prior base existence, positivity and strong odd solution are invoked | Not independently certified in this document |

The reference is an exact auxiliary comparison, not a change of the actual nonzero experiment. This audit establishes neither the nonlinear result nor novelty; see separate files.
