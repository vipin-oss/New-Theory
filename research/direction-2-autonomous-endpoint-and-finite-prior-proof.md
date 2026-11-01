# Endpoint cancellation and an active-base finite-prior theorem

Status: first proof plus self-audit by Arena; not independent human certification. This is an explicit **conditional, restricted linearized** result, not a new foundational continuum theory or a claim of historical novelty. All physical material couplings remain nonzero; no data or equation of the active experiment is changed.

## 1. The alleged endpoint mismatch

Fix the actual even coefficients \(M,B,S\). Let \(\mathcal U_n f\) be the endpoint flux on \(J=(\delta,T)\) of the auxiliary system (1) in `direction-2-critical-theorem-independent-audit.md`: source \(e^{-\mu t}f\phi_n\), **actual** feedback \(Sp\), zero initial \(Y,p\). Define
\[
\rho_n(f)=\mathcal U_n f-\frac{2A_0c_L e^{-\mu t}f(t,0)}{q_n}.
\]
Linearity of the fixed-coefficient auxiliary system gives the exact identity
\[
\rho_n(S)-\rho_n(f)=\mathcal U_n(S-f)-\frac{2A_0c_Le^{-\mu t}(S-f)(t,0)}{q_n}=\rho_n(S-f).
\]
So the mismatch is indeed present if one compares raw fluxes while subtracting only the true leading coefficient; it is **not** present in the difference of the separately corrected remainders. Apply the earlier weak/strong estimate to \(S-f\): the explicit trial \(A_{S-f}=e^{-\mu t}(S-f)\phi_n/(\kappa q_n^2)\) has exactly that boundary flux, and its error has \(L^2H^1=O(q_n^{-2}\|S-f\|_{\mathcal A})\), \(L^2H^2=O(q_n^{-1}\|S-f\|_{\mathcal A})\). The multiplicative derivative trace bound gives
\[
\|\rho_n(S)-\rho_n(f)\|_{L^2(J)}\le Cq_n^{-3/2}\|S-f\|_{\mathcal A}.
\]
This separately verifies the *endpoint cancellation*, not every prerequisite of the inherited energy estimate. It supports (11) of the Volkov audit; it does not prove its dyadic summability hypothesis.

Exact smooth endpoint matching is unavailable for the whole abstract class: take \(f(t,x)=|t-t_0|^\alpha\) with interior \(t_0\) and \(1/2<\alpha<1\). It is spatially even and in \(H^1_tL^2_x\cap L^2_tH^2_x\), but its endpoint time function is not \(C^1\). A \(C^\infty(\overline Q)\) approximant equal to that endpoint at every time would have a smooth endpoint trace, contradiction. This is not an example of a physically attainable active coefficient. Matching is unnecessary for the separately corrected estimate.

## 2. A theorem for the actual active base

Use the exact hypotheses and notation of `direction-2-active-base-existence-and-regularity.md`, including \(a,k,\lambda,c,\kappa,\theta_*,L>0\), \(b\ne0\), \(g_*\ne0\), \(\mu=\lambda a/(a+k)>0\), \(\gamma=\lambda b/(a+k)\), \(r=k/(a+k)\), \(d=b^2/(a+k)\), \(0<\delta<T\), the frozen loading and homogeneous thermal boundary condition, and the weak-initial solution class. Let \(s_*,C_B,K,A_s,A_R,W_s,W_R\) be exactly the positive constants of its (7), and \(q=|g_*|/L\). Put
\[
C_y=2KC_B,\quad C_w=W_s+2C_BW_R,\quad D_M=dC_y,
\quad D_S=\mu(|br|C_y+2kC_w),
\]
\[
D_B=2dC_B+\sqrt{LT}\{ |b|(A_s+2C_BA_R)+|br\gamma|C_y+2k|\gamma|C_w\}.
\]
Let \(M_0=c+d\theta_*\), \(B_0=-br\gamma\theta_*<0\), \(S_0=\mu br\theta_*\ne0\), \(q_0=s_*/2\). The actual active-base estimates imply for every \(0<q<q_0\)
\[
\|M-M_0\|_\infty\le D_Mq,\quad
\|B-B_0\|_{L^2(Q)}\le D_Bq,\quad
\|S-S_0\|_\infty\le D_Sq,\quad M\ge c. \tag{1}
\]
Here the \(L^2\) norm is on all of \((0,T)\times(0,L)\); no \(L^\infty\) bound on \(B\) is assumed. The first two terms in \(D_B\) come respectively from \(dQy_{b,t}\) and \(bE_b\); the rest from \(y_b,w_b\).

For any fixed \(N\ge1\), let \(V_N=\operatorname{span}\{\phi_1,\ldots,\phi_N\}\), where \(\phi_n=c_L\sin(q_nx)\), \(q_n=2\pi n/L\). Define
\[
a_n=(\kappa q_n^2-B_0)/M_0,\quad d_0=\gamma S_0/M_0>0,\quad
\lambda_{n,\pm}=-\frac{a_n+\mu}{2}\pm\sqrt{\frac{(a_n-\mu)^2}{4}+d_0},
\]
\[\Delta_n=\lambda_{n,+}-\lambda_{n,-}>0,\quad c_n=|S_0|/(M_0\Delta_n),\quad
u_n(t)=\frac{S_0}{M_0\Delta_n}(e^{\lambda_{n,+}t}-e^{\lambda_{n,-}t}),\quad
k_n^0(t)=2A_0\kappa c_Lq_nu_n(t).
\]
The superscript zero denotes a **reference response used inside the proof**, not the experimental base. Let \(G_N=(\int_\delta^T k_m^0 k_n^0dt)_{m,n\le N}\), and \(\sigma_N=\sqrt{\lambda_{\min}(G_N)}\). Define
\[
f_n=D_M\sqrt T\,c_n(|\lambda_{n,+}|+|\lambda_{n,-}|)
 +2D_Bc_Lc_n+D_S\sqrt T(1+2|\gamma|Tc_n),\quad H_N=(\sum_{n=1}^Nf_n^2)^{1/2}.
\]
The following constants bound the actual forced evolution. Set \(P_L=L/\pi\), \(B_* = |B_0|\sqrt{LT}+D_Bq_0\), \(S_*=|S_0|+D_Sq_0\), \(M_*=M_0+D_Mq_0\),
\[
\Xi=T(1+\gamma^2P_L^2/\kappa)+\frac3c\left(\frac L\kappa B_*^2+TS_*^2\right),\quad
E_*={3\over c}e^\Xi,\quad U_*^2={3\over c^2}(1+\Xi e^\Xi),
\]
\[
V_*={1\over\kappa}\left(M_*U_*+\sqrt{L/\kappa}\,B_*\sqrt{E_*}+S_*\sqrt{TE_*}+1\right),
\quad C_{\rm tr}=2A_0\kappa\left({2TE_*\over\kappa L}+2\sqrt{TE_*/\kappa}\,V_*\right)^{1/2}.
\]
All constants are finite and positive. **Theorem.** \(\sigma_N>0\), and if the true nonzero frozen load obeys
\[
0<q<\min\{q_0,\sigma_N/(2C_{\rm tr}H_N)\}, \tag{2}
\]
then the actual delayed flux-difference derivative \(\mathcal T\), retaining full history \([0,T]\), satisfies
\[
\|\mathcal T h\|_{L^2(\delta,T)}\ge \frac{\sigma_N}{2}\|h\|_{L^2(0,L)}\quad(h\in V_N). \tag{3}
\]
Consequently its exact kernel intersects \(V_N\) only in zero. The threshold is symbolic, not verified for the unspecified real loading; it depends on \(N\), and no bound uniform in \(N\) is claimed. All input modes are in the admissible odd \(H^2\) space. The theorem concerns the derivative, not global nonlinear identifiability.

## 3. Proof

**Reference Gram.** The comparison equations have coefficients \(M_0,B_0,S_0\) but retain *both* coupling terms and the full memory ODE. With initial \((Y,P)=(0,\phi_n)\), their modal system is \(u_n'=-a_nu_n+(S_0/M_0)v_n\), \(v_n'=-\mu v_n+\gamma u_n\), \(u_n(0)=0,v_n(0)=1\). Hence the displayed \(u_n\) and reference output are exact. This auxiliary constant-coefficient system is a proof device only; (3) is for the actual nonautonomous physical solution at a strictly nonzero load.

Because \(a_n\mu-d_0=\mu\kappa q_n^2/M_0>0\) and \(a_n+\mu>0\), both roots are negative. The characteristic polynomial at \(-\mu\) is \(-d_0<0\), so \(\lambda_{n,-}<-\mu<\lambda_{n,+}<0\). As \(a_n\) strictly increases in \(n\), both roots strictly decrease: their derivatives with respect to \(a\) are \(-1/2\pm(a-\mu)/(4\sqrt{(a-\mu)^2/4+d_0})<0\). Thus all \(2N\) exponents are distinct. A finite linear combination of the \(k_n^0\) that vanishes on \(J\) is an entire exponential polynomial vanishing identically; the Vandermonde determinant of derivatives at any point forces all its coefficients to vanish. Each coefficient multiplying its two exponentials is nonzero. Hence the \(k_n^0\) are linearly independent, \(G_N\) is positive definite and \(\sigma_N>0\). Its entries are finite explicit sums of \((e^{(\lambda+\lambda')T}-e^{(\lambda+\lambda')\delta})/(\lambda+\lambda')\).

**Exact difference.** For \(h=\sum h_n\phi_n\), let \((Y,P)\) be the actual linearized state and \((Y^0,P^0)\) the comparison. Their difference \((u,p)=(Y-Y^0,P-P^0)\) has zero initial data, zero thermal boundary values, and solves
\[
Mu_t-\kappa u_{xx}=Bu+Sp+F,\quad p_t+\mu p=\gamma u,\quad
F=-(M-M_0)Y_t^0+(B-B_0)Y^0+(S-S_0)P^0. \tag{4}
\]
No post-delay restart occurs. In the reference solution \(Y^0=\sum h_nu_n\phi_n\), \(P^0=\sum h_nv_n\phi_n\), and \(v_n=e^{-\mu t}+\gamma\int_0^t e^{-\mu(t-s)}u_n(s)ds\). Since both roots are negative, \(|u_n|\le2c_n\), \(|u_n'|\le c_n(|\lambda_{n,+}|+|\lambda_{n,-}|)\), \(|v_n|\le1+2|\gamma|Tc_n\). Combining these bounds with (1) and Cauchy–Schwarz yields \(\|F\|_{L^2(Q)}\le qH_N\|h\|_2\).

**Forced-energy bound.** With \(\mathscr E=\kappa\|u_x\|_2^2+\|p\|_2^2\), test the first equation by \(2u_t\) and the ODE by \(2p\). The one-dimensional inequality \(\|u\|_\infty^2\le L\|u_x\|_2^2\), Poincaré, and Young yield
\[
\mathscr E'+c\|u_t\|_2^2\le C(t)\mathscr E+(3/c)\|F(t)\|_2^2,
\quad C(t)=1+\gamma^2P_L^2/\kappa+\frac3c\left((L/\kappa)\|B(t)\|_2^2+\|S(t)\|_\infty^2\right).
\]
Thus \(\int_0^T C\le\Xi\), \(\sup_t\mathscr E\le E_*\|F\|_2^2\) and \(\|u_t\|_2\le U_*\|F\|_2\). The PDE then gives \(\|u_{xx}\|_2\le V_*\|F\|_2\). The trace inequality \(|u_x(t,0)|^2\le 2L^{-1}\|u_x(t)\|_2^2+2\|u_x(t)\|_2\|u_{xx}(t)\|_2\) yields \(2A_0\kappa\|u_x(\cdot,0)\|_{L^2(J)}\le C_{\rm tr}\|F\|_2\). Strong solutions and this testing are justified by the inherited actual-base forced theorem; the estimates extend by its approximation procedure. Therefore
\[
\|\mathcal T h-\sum h_nk_n^0\|_{L^2(J)}\le C_{\rm tr}qH_N\|h\|_2.
\]
The reference Gram lower bound and (2) give (3). □

## 4. Adversarial self-audit and limitations

1. **No equilibrium replacement:** the comparison is used exactly inside a difference equation; (4) includes all actual coefficient differences. The theorem concerns the original prescribed nonzero load under the stronger symbolic condition (2), not the reference system as an experiment.
2. **No modal decoupling for the true system:** only the auxiliary constant-coefficient comparison is diagonalized; the exact error equation controls all actual cross-mode coupling.
3. **No delay reset:** all forcing and energy norms extend to time zero; \(J\) only restricts the final observation.
4. **No positivity/Hopf or analytic active coefficients:** neither enters. Analyticity is invoked solely for a finite exponential polynomial of the comparison problem.
5. **No global identification:** Gram positivity is for each *fixed* \(N\) and \(q_N\)-dependent threshold; \(\sigma_N\) can collapse as \(N\to\infty\). A compact infinite-dimensional observation cannot have a uniform \(L^2\) lower bound. Numerical Gram rank would not replace the analytic argument.
6. **Actual condition:** all source constants have definitions in the cited small-load proof; no material value is assumed. The regime is nonempty because the finite Gram has positive smallest eigenvalue and all other constants are finite, not because the actual unspecified experiment has been verified to satisfy it.
7. **Independent audit pending:** this proof reuses prior base and strong-solvability theorems. Arena's check is adversarial self-review, not an independent scientist's certification; the exact proof and literature overlap still merit independent scrutiny.
8. **Novelty:** finite-dimensional perturbation stability is standard. The theorem is an explicit model-specific consequence and is not by itself evidence of a new continuum theory or verified research breakthrough.
