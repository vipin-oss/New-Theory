# Active-base existence and regularity for the critical theorem

**Scope and conclusion.** For the original sinusoidal loading and zero initial internal memory, the explicit small-data regime below gives a nonempty family of nonzero amplitudes, a unique positive weak-initial strong-temperature base, the coefficients required by the critical theorem, and its odd forced estimates. This is a mathematical parameter regime, **not** a verified range for the unspecified experiment. We use and recheck the explicit reference-linear and contraction estimates in `direction-2-formulation-A-existence-investigation.md`, §§3–7, and its independent audit, §§3–8. The present argument adds the missing connection from that solution to all coefficients, the odd forced problem, the observation, and local nonlinear differentiability. It does not assert a corner-classical solution or general large-data continuation.

Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is the designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder. This is Arena's adversarial recalculation, not independent human certification. No model, boundary condition, material sign or loading shape is changed.

## 1. Original equations and exact reduction

On \(I=(0,L)\), \(T=10/\lambda\), prescribe \(u(0,t)=0\), \(u(L,t)=g_*\sin^2(\pi t/T)\), \(\theta(0,t)=\theta(L,t)=\theta_*\), \(\theta(x,0)=\theta_*\), and \(z(x,0)=z_0(x)\). The frozen equations are
\[
\sigma_x=0,\quad \sigma=(a+k)u_x-b(\theta-\theta_*)-kz,\quad
z_t=\lambda(u_x-z),\quad
c\theta_t=\kappa\theta_{xx}-b\theta (u_x)_t+k\lambda(u_x-z)^2. \tag{1}
\]
Assume \(a,k,\lambda,c,\kappa,\theta_*,L>0\), \(b\ne0\), \(g_*\ne0\). Put \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(d=b^2/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(m=g/L\), \(y=\theta-\theta_*\), \(v=\bar z\), \(p=Qz=z-\bar z\), \(Q=I-\text{mean}\). Integrating equilibrium gives
\[
\sigma=Dm-b\bar y-kv,\quad u_x=m+rp+\beta Qy,\quad
w:=u_x-z=m-v-\alpha p+\beta Qy, \tag{2}
\]
\[
v_t=\lambda(m-v),\quad p_t=-\mu p+\gamma Qy,\quad
(cI+d(\theta_*+y)Q)y_t=\kappa y_{xx}-b(\theta_*+y)E+k\lambda w^2,\quad E=m'+rp_t. \tag{3}
\]
The nonlocal \(Qy_t\) cannot be discarded. Initial \(v_0=\bar z_0\), \(p_0=Qz_0\), \(y_0=0\); \(u_0(x)=r\int_0^xQz_0\). Conversely these formulas reconstruct (1), \(u(L)=Lm=g\), and \(z=v+p\). \(p\) is the actual mean-free internal state, not an independently prescribed forcing.

For \(\theta_* /2\le\theta\le3\theta_*/2\), the mass map \(\mathsf M_\theta h=ch+d\theta Qh\) has the exact inverse
\[
\mathsf M_\theta^{-1}F={F\over c+d\theta}+{d\theta\over c+d\theta}\,
{\langle F/(c+d\theta)\rangle\over\langle c/(c+d\theta)\rangle},\quad
\left\langle {c\over c+d\theta}\right\rangle\ge {c\over c+3d\theta_*/2}>0. \tag{4}
\]
It is self-adjoint and positive in \(L^2(dx/\theta)\), since \((\mathsf M_\theta h,h)_{1/\theta}=c\int h^2/\theta+d\int|Qh|^2\). This is not an independent maximum principle.

## 2. Explicit sufficient finite-horizon regime

All formulas are numerical inequalities in one **fixed consistent unit system**; alternatively nondimensionalize (1) first and apply them to the dimensionless constants and corresponding interval. In particular \(H^2\) norms mix derivative units, so the numerical threshold is not an invariant engineering measurement. Let
\[
\mathcal E=\{y\in H^1_tL^2_x\cap L^2_t(H^2\cap H^1_0):y(0)=0\},\quad
\|y\|_\mathcal E=\|y_t\|_2+\|y_{xx}\|_2+\sup_t\|y(t)\|_{H^1},
\quad K=\sqrt L,\ H=L/\pi,\ S_L=\sqrt{L^{-1}+L}. \tag{5}
\]
Then \(\|y\|_\infty\le K\|y\|_\mathcal E\) and \(\|z_0\|_\infty\le S_L\|z_0\|_{H^2}\). Set \(C_*=c+d\theta_*\), \(b_0=b\theta_*r\mu\), \(c_0=b\theta_*r\gamma\), and
\[
\begin{gathered}
K_0=\max\{3|b_0|^2/c+|\gamma|H,\ (3|c_0|^2H^2/c+|\gamma|H)/\kappa\},\\
J=e^{K_0T/2}\max\{1,\sqrt{3/c}\},\quad U=\sqrt{(1+3/c+K_0TJ^2)/c},\\
C_L=U+\frac{C_*U+1+(|b_0|\sqrt T+|c_0|H\sqrt{T/\kappa})J}{\kappa}
+\sqrt{(1+H^2)/\kappa}\,J. \tag{6}
\end{gathered}
\]
Define
\[
\begin{aligned}
A_s&=\pi/T+2r\mu S_L,&A_R&=2r|\gamma|(1+\mu T)K,\\
W_s&=2+(1+2\alpha)S_L,&W_R&=2|\beta|(1+\alpha\lambda T)K,\\
C_N&=dK+|b|K\sqrt{LT}\max(A_s,A_R)+k\lambda\sqrt{LT}\max(W_s,W_R)^2,\\
C_N'&=2dK+|b|K\sqrt{LT}(A_s+2A_R)+2k\lambda\sqrt{LT}\,W_R(W_s+W_R),\\
C_B&=C_L\left(|b|\theta_*\pi\sqrt{LT}/T+2\sqrt L S_L\right),\\
s_*&=\min\left\{\frac{C_B}{2C_LC_N(1+2C_B)^2},\
\frac1{4C_LC_N'(1+2C_B)},\frac{\theta_*}{8KC_B}\right\}. \tag{7}
\end{aligned}
\]
All displayed denominators are strictly positive for the frozen signs and \(b\ne0\), so \(s_*>0\). The theorem applies when
\[
0<q:=|g_*|/L<s_*/2,\qquad z_0=0. \tag{8}
\]
More generally the same estimates apply to \(\|z_0\|_{H^2}+q<s_*\), with no oddness required for the nonlinear state. Inequality (8) is a **nonempty symbolic interval for every fixed set of finite positive material constants**: choose e.g. \(0<q<s_*/2\). This is not an assertion that an already prescribed but numerically unspecified amplitude lies there.

**Existence proof and provenance.** The exact reference system is
\[
(cI+d\theta_*Q)y_t-\kappa y_{xx}=f+b_0p-c_0Qy,\quad p_t=-\mu p+\gamma Qy. \tag{9}
\]
The earlier reports prove its Galerkin estimate \(\|y\|_\mathcal E\le C_L(\|f\|_2+\|p_0\|_2)\) with (6), by testing against \(y_t\) and \(p\); the nonlocal mass is kept in the Galerkin matrix. The PDE residual is
\[
N[y]=-dyQy_t-byE[y]+k\lambda w[y]^2, \tag{10}
\]
with \(p[y]=e^{-\mu t}p_0+\gamma\int_0^te^{-\mu(t-s)}Qy(s)ds\) and \(v=e^{-\lambda t}v_0+\lambda\int_0^te^{-\lambda(t-s)}m(s)ds\). The earlier audit derives, for \(s=q+\|z_0\|_{H^2}\), \(\|y\|,\|\tilde y\|\le R\),
\[
\|N[y]\|_2\le C_N(s+R)^2,\quad
\|N[y]-N[\tilde y]\|_2\le C_N'(s+R)\|y-\tilde y\|_\mathcal E. \tag{11}
\]
Here the product \(yQy_t\) uses \(\|y\|_\infty\le K\|y\|_\mathcal E\), not an unproved \(y_t\) supremum; the \(E,w\) bounds use the full Volterra history and \(H^2\hookrightarrow L^\infty\). Mapping an input to the heat solution of (9) with \(f=-b\theta_*m'+N[y]\) gives, with \(R=2C_Bs\),
\[
\|\Phi(y)\|_\mathcal E\le C_Bs+C_LC_N(1+2C_B)^2s^2\le R,\quad
\operatorname{Lip}(\Phi)\le C_LC_N'(1+2C_B)s\le1/4. \tag{12}
\]
Furthermore \(KR\le\theta_*/4\), giving \(3\theta_*/4\le\theta\le5\theta_*/4\), stronger than (4)'s safe bounds. The closed ball in \(\mathcal E\) is complete; its fixed point is a weak-initial strong-temperature solution of the original equations. The earlier independent audit §8 proves uniqueness in the full stated positive weak-initial class via the weighted difference energy, not merely inside this ball. This uniqueness is used as a previously proved lemma; it is not implied by Banach's theorem itself. The supplied constants are conservative and not optimized.

## 3. Coefficients from the actual base

For \(z_0=0\), the base and all coefficients are even by reflection and uniqueness. Since \(y_b\in\mathcal E\subset C_tH^1_0\) and
\[
p_b=\gamma\int_0^te^{-\mu(t-s)}Qy_b(s)ds,\qquad p_{b,t}=-\mu p_b+\gamma Qy_b,
\]
we have \(p_b\in H^1_tH^2_x\), because \(Q\) is bounded on \(H^2\), \(y_b\in L^2_tH^2\), and \(p_b(0)=0\in H^2\). Therefore \(w_b=m-v_b-\alpha p_b+\beta Qy_b\in H^1_tL^2\cap L^2_tH^2\); \(E_b=m'+rp_{b,t}\in L^2_{t,x}\). Define
\[
M=c+d(\theta_*+y_b),\quad B=-dQy_{b,t}-bE_b-br\gamma(\theta_*+y_b)+2k\gamma w_b,\quad
S=\lambda\alpha[br(\theta_*+y_b)-2kw_b]. \tag{13}
\]
Then \(M\in L^\infty\), \(M\ge c+3d\theta_*/4>0\), \(M_x=dy_{b,x}\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\), and
\[
S\in H^1_tL^2_x\cap L^2_tH^2_x\hookrightarrow C_tH^1_x\hookrightarrow L^\infty_{t,x}. \tag{14}
\]
No \(S_{xx}(t,0)\), \(M_t(t,0)\), or classical corner value is inferred.

## 4. Independent strong odd forced estimate

Let measurable even \(M,B,S\) satisfy (13)–(14), \(0<m_0\le M\le m_1\). In the odd space solve
\[
MY_t-\kappa Y_{xx}=BY+SP+F,\qquad P_t+\mu P=\gamma Y+G,\quad Y|_{\partial I}=0,\quad Y(0)=Y_0\in H^1_0,\ P(0)=P_0\in L^2. \tag{15}
\]
For Galerkin approximants in odd Dirichlet sines, the mass matrix \((M\phi_i,\phi_j)\) is symmetric and \(\ge m_0I\). Test the first equation by \(Y_t\) and the second by \(P\). In one dimension \(\|Y\|_\infty\le\sqrt L\|Y_x\|_2\). Young gives, with \(X=\kappa\|Y_x\|_2^2+\|P\|_2^2\),
\[
X'+m_0\|Y_t\|_2^2\le C[1+\|B(t)\|_2^2+\|S(t)\|_\infty^2]X+C(\|F(t)\|_2^2+\|G(t)\|_2^2). \tag{16}
\]
The coefficient is integrable. Gronwall bounds \(\sup X\) and \(\|Y_t\|_2\). The projected equation bounds \(\|Y_{xx}\|_2\) because \(-Y_{xx}\) lies in the same sine Galerkin space: its right side is bounded by \(m_1\|Y_t\|+\|B\|_2\|Y\|_\infty+\|S\|_\infty\|P\|+\|F\|\). The ODE bounds \(P_t\). Compactness gives almost-everywhere convergence of a subsequence of \(Y_N\), with a uniform space-time bound; dominated convergence against \(|B|^2\) passes \(BY_N\to BY\) in \(L^2\). Other terms pass weakly. The same energy estimate proves uniqueness. Thus
\[
\|Y\|_{H^1_tL^2\cap L^2_tH^2}+\|P\|_{H^1_tL^2}
\le C(\|Y_0\|_{H^1_0}+\|P_0\|_2+\|F\|_2+\|G\|_2). \tag{17}
\]
No \(M_t\) is used; initial \(P_0\) is not forced to vanish at spatial endpoints. The separate weak \(V'\) estimate, requiring \(M_x\), is proved in the companion audit. Equation (17) makes \(Y_x(0,\cdot)\in L^2(0,T)\) by the \(H^2\) trace, hence the actual delayed odd observation is a bounded \(L^2_o\to L^2(J)\) operator.

## 5. Startup compatibility

For the actual base \(z_0=0\), \(m(0)=m'(0)=0\), \(v_0=p_0=y_0=0\), and initial equilibrium is \(u_0=0\). The only compatibility required for \(\mathcal E\) is \(y_0\in H^1_0\), satisfied. If a corner-classical solution has continuous \(y_t,y_{xx}\), the bath yields \(y_t(0,0)=y_t(L,0)=0\); the initial PDE then gives \(y_{xx}(0,0)=y_{xx}(L,0)=0\). The first corner conditions therefore hold, but this does **not** prove the classical solution exists.

Higher regularity can fail: \(m''(0)=2\pi^2g_*/(LT^2)\ne0\). If one additionally demands enough regularity to differentiate (3) at \(t=0\), commute \(\partial_t\partial_{xx}\), and identify \(y_t(\cdot,0)=0\) as an \(H^2\) function, and require also \(y_{tt}\) continuous up to the initial corners, then \(y_{xxt}(\cdot,0)=0\) and the differentiated PDE gives \((cI+d\theta_*Q)y_{tt}(\cdot,0)=-b\theta_*m''(0)\). By the exact inverse of this constant-reference mass, \(y_{tt}(x,0)=-b\theta_*m''(0)/c\) in the interior. Continuity extends this nonzero value to the endpoints, but the fixed baths force \(y_{tt}=0\) there. These extra requirements are incompatible. They are **not** part of the weak-initial class or the critical proof. Modifying startup would change the prescribed experiment and is neither needed nor silently done here.

## 6. Local nonlinear map and quadratic remainder

Under the strict regime (8), there is \(r_0>0\) such that every \(h\in H^2(I)\) with \(\|h\|_{H^2}<r_0\) has \(q+\|h\|_{H^2}<s_*\). The same contraction yields a positive solution; the earlier full-class uniqueness applies. Thus this is an actual open \(H^2\) neighborhood in the weak-initial domain, intersected with any fixed prior ball of positive radius.

The fixed-point map \(\Phi(y,h)\) is a polynomial of degree at most two in \((y,h)\) followed by the bounded linear reference solver (9): \(p[y,h]\) and \(v[h]\) depend affinely on \((y,h)\); the products in (10) are bounded by \(\mathcal E\hookrightarrow L^\infty\), \(H^2\hookrightarrow L^\infty\) and \(y_t\in L^2\). Hence \(\Phi\) is \(C^\infty\) between the Banach spaces. At the base, \(\|D_y\Phi\|\le1/4\), so \(I-D_y\Phi\) is invertible by a Neumann series. The Banach implicit-function theorem yields a \(C^2\) solution map with bounded second derivative on a smaller neighborhood; Taylor's integral formula gives
\[
\|y(h)-y_b-Y[h]\|_\mathcal E\le C\|h\|_{H^2}^2. \tag{18}
\]
For odd \(h\), \(Qh=h\), and reflection makes \(Y,P\) odd; the first variation is exactly (15) with \(Y_0=0,P_0=h\), \(F=G=0\), and the actual \(M,B,S\) in (13). The boundary derivative is continuous \(\mathcal E\to L^2(J)\), so the nonlinear **flux-difference** map has \(\|\mathcal N(h)\|_{L^2(J)}\le C\|h\|_{H^2}^2\). This establishes the quadratic hypothesis for this weak-initial small-data regime, not for arbitrary amplitudes or the corner-classical domain. Nonlinear even corrections may be present. It does not establish the stronger \(L^2/L^4\) tame bound or a nonlinear \(4/7\) obstruction.

The complete force and two labeled fluxes are also \(C^2\) in \(h\), using \(\sigma=Dm-b\bar y-k\bar z\) and \(\mathcal E\to L^2\) endpoint gradients. For odd h, the linearized force is zero because both \(\bar Y\) and \(\bar h\) vanish. Reflection gives \(Y_x(L,t)=Y_x(0,t)\); with the usual outward-flux convention, the two linearized heat powers are equal in magnitude and opposite in sign. Thus the full vector derivative is a fixed bounded multiple of the flux-difference derivative. The \(C^2\) remainder covers all three output channels, including even nonlinear corrections. The companion audit therefore derives the nonlinear \(11/14\) obstruction for the full output vector in this regime; it does not derive the \(4/7\) endpoint.
