# Independent recalculation: pre-delay memory isomorphism

**Verdict: CONDITIONALLY PROVED** under the inherited active-base construction, coefficient bounds and strong forced-solution theorem. No independent human certification is implied. The actual graph or boundary uniqueness is not established by this result.

## Reference calculation on all odd modes

Let \(D=a+k\), \(r=k/D\), \(\alpha=a/D\), \(\beta=b/D\), \(\gamma=\lambda\beta\), \(\mu=\lambda\alpha\), \(d=b^2/D\), \(M_0=c+d\theta_*\), \(B_0=-br\gamma\theta_*\), \(S_0=\mu br\theta_*\). With \(q_n=2\pi n/L\), \(a_n=(\kappa q_n^2-B_0)/M_0\), \(d_0=\gamma S_0/M_0>0\), the mode matrix on \((u_n,v_n)\) is \(\begin{psmallmatrix}-a_n&S_0/M_0\\\gamma&-\mu\end{psmallmatrix}\), giving \(z^2+(a_n+\mu)z+a_n\mu-d_0\). Direct substitution gives \(\mu B_0+\gamma S_0=0\), hence \(a_n\mu-d_0=\mu\kappa q_n^2/M_0>0\). Its discriminant is \((a_n-\mu)^2+4d_0>0\), the polynomial at \(-\mu\) is \(-d_0<0\), and sum/product of roots give \(\lambda_{n,-}<-\mu<\lambda_{n,+}<0\).

For \((u_n,v_n)(0)=(0,1)\), \(u_n=(S_0/M_0)(e^{\lambda_{n,+}t}-e^{\lambda_{n,-}t})/(\lambda_{n,+}-\lambda_{n,-})\). Thus \(\gamma u_n\ge0\), and \(v_n=e^{-\mu t}+\gamma\int_0^te^{-\mu(t-s)}u_n(s)ds\ge e^{-\mu t}\). The bounded reference energy estimate gives \(\sup_n|v_n(\delta)|<\infty\); hence on the complete odd ONB \(D^0_\delta\) is a bounded multiplier, onto, with \(\|(D^0_\delta)^{-1}\|\le e^{\mu\delta}\). This is not a finite-section conclusion.

## Complete nondimensionalization and uniform constants

Use \(\xi=x/L\), \(\tau=t/T\), \(\Theta=\theta/\theta_*\), \(U=u/L\), \(Z=z\), \(\Sigma=\sigma/D\), \(T=10/\lambda\). Then
\[\Sigma_\xi=0,\quad \Sigma=U_\xi-\widehat b(\Theta-1)-rZ,\quad Z_\tau=\widehat\lambda(U_\xi-Z),\]
\[\Theta_\tau=\widehat\kappa\Theta_{\xi\xi}-\widehat b_T\Theta(U_\xi)_\tau+\widehat k_T(U_\xi-Z)^2,\]
with \(\widehat b=b\theta_*/D\), \(\widehat\lambda=\lambda T=10\), \(\widehat\kappa=\kappa T/(cL^2)\), \(\widehat b_T=b/c\), \(\widehat k_T=k\lambda T/(c\theta_*)\). The domain/time are both \((0,1)\), delay is \(\widehat\delta=1/100\), and \(q=|g_*|/L\) is dimensionless. To recompute the inherited base constants in their original common-coupling form, multiply the dimensionless heat equation by \(c\theta_*/D\): use \(a'=a/D\), \(k'=k/D\), \(b'=b\theta_*/D\), \(c'=c\theta_*/D\), \(\kappa'=\kappa\theta_*T/(DL^2)\), \(\lambda'=\lambda T\), \(\theta_*'=L'=T'=1\). This preserves the same coefficient \(b'\) in stress and heat; setting the normalized heat coefficient to one inside the old formulas without also transforming the coupling would be wrong. For the linearized odd system write \(y=Y/\theta_*\), \(p=P\); its dimensionless coefficients are \(\widehat M=M/c\), \(\widehat B=TB/c\), \(\widehat S=TS/(c\theta_*)\), \(\widehat\gamma=T\gamma\theta_*\), \(\widehat\mu=T\mu\). In what follows hats are suppressed and all norms, \(s_*\), and \(D_M,D_B,D_S\) are recomputed in these dimensionless variables; dimensional numerical constants from previous mixed norms are not simply reused.

The inherited base bounds provide \(\|M-M_0\|_\infty\le D_Mq\), \(\|B-B_0\|_2\le D_Bq\), \(\|S-S_0\|_\infty\le D_Sq\), uniformly for \(0<q<q_0=s_*/2\), and \(M\ge1\). Set \(B_*=|B_0|+D_Bq_0\), \(S_*=|S_0|+D_Sq_0\),
\[\Xi_0=1+\frac{\gamma^2}{\kappa\pi^2}+3\left(\frac{B_0^2}{\kappa}+S_0^2\right),\quad \Xi=1+\frac{\gamma^2}{\kappa\pi^2}+3\left(\frac{B_*^2}{\kappa}+S_*^2\right).\]
Testing the reference heat equation by \(2Y_t^0\) and the ODE by \(2P^0\), using \(\|Y^0\|_\infty\le\|Y_x^0\|_2\) and Poincaré, yields \(X'= (\kappa\|Y_x^0\|^2+\|P^0\|^2)'\) with \(X'+\|Y_t^0\|^2\le\Xi_0X\), \(X(0)=\|h\|_2^2\). Thus
\[\|Y_t^0\|_2\le C_t\|h\|_2,\quad \|Y^0\|_\infty\le C_\infty\|h\|_2,\quad \|P^0\|_2\le C_p\|h\|_2,\]
\[C_t=\sqrt{1+\Xi_0e^{\Xi_0}},\quad C_\infty=e^{\Xi_0/2}/\sqrt\kappa,\quad C_p=e^{\Xi_0/2}.\]
These constants control the full \(\ell^2\) input, uniformly in all modes and in \(q\).

Subtracting full histories yields exactly \(F=-(M-M_0)Y_t^0+(B-B_0)Y^0+(S-S_0)P^0\). In particular \(B-B_0\in L^2\) multiplies the bounded reference \(Y^0\); no \(B\in L^\infty\) assumption occurs. Hence
\[\|F\|_2\le q C_F\|h\|_2,\quad C_F=D_MC_t+D_BC_\infty+D_SC_p.\]
For the actual forced difference with zero initial state, the same energy calculation and three Young inequalities give \(\sup_tX(t)\le3e^{\Xi}\|F\|_2^2\). Poincaré then gives \(\|Y-Y^0\|_{L^2(Q)}\le C_{\rm forc}\|F\|_2\), \(C_{\rm forc}=\sqrt{3e^\Xi}/(\pi\sqrt\kappa)\). Since \(P-P^0=\gamma\int_0^te^{-\mu(t-s)}(Y-Y^0)(s)ds\),
\[\|D_\delta-D^0_\delta\|\le C_Dq,\quad C_D=|\gamma|\sqrt\delta C_{\rm forc}C_F.\]
Thus \(0<q<\min\{s_*/2,e^{-\mu\delta}/(2C_D)\}\) yields a Neumann inverse, with \(\|D_\delta^{-1}\|\le2e^{\mu\delta}\). The constants depend on the fixed dimensionless materials, geometry/time scaling, and chosen base bound \(q_0\), not on \(h\), mode count or the variable \(q<q_0\). If \(C_D=0\), interpret the second threshold as \(+\infty\). No experimental numerical validation follows.

**Audit boundary:** this calculation relies on the cited actual-base bound and forced-solution limit/trace machinery; they have not been re-proved here or independently certified. Uniform energy estimates do not imply a positive observation lower bound, graph uniqueness, or square-sum regularity.
