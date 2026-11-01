# Modal reconstruction and signs

**Status: VERIFIED UNDER EXPLICIT ASSUMPTIONS.** The operator theorem itself does not require a PDE. The physical interpretation below assumes the frozen odd linear model, zero initial odd temperature and memory at \(s=-T\), compatible opposite boundary temperatures \(Y(0,s)=a(s)\), \(Y(L,s)=-a(s)\), and the coefficients and solution class stated below. It is not a verification of the nonlinear full system.

## 1. Spectral data and external theorem hypotheses

Use \(\phi_n(x)=\sqrt{2/L}\sin(q_nx)\), \(q_n=2\pi n/L\). For the frozen odd system
\[M Y_s=\kappa Y_{xx}+B_0Y+SP,\qquad P_s=-\mu P+\gamma Y,\quad M,\kappa,L,d=\gamma S/M>0,\]
set \(A_n=(\kappa q_n^2-B_0)/M\) and
\[D_n=\begin{pmatrix}-A_n&S/M\\\gamma&-\mu\end{pmatrix},\qquad
C_n=\frac{2\kappa\sqrt{2/L}\,q_n}{M}.\]
The eigenvalues solve \((\lambda+A_n)(\lambda+\mu)-d=0\). Since d>0, the two distinct real roots can be written \(\lambda_+=-\mu+\delta_n\), \(\lambda_-=-\mu-b_n\), with \(\delta_n,b_n>0\), \(b_n\delta_n=d\), and \(b_n-d/b_n=A_n-\mu\). The positive branch is
\[b_n=\tfrac12\left[A_n-\mu+\sqrt{(A_n-\mu)^2+4d}\right].\tag{1}\]
It increases strictly with \(A_n\). With \(\alpha=\kappa(2\pi/L)^2/M>0\) and \(\beta=-B_0/M-\mu\), (1) yields \(b_n=\alpha n^2+\beta+O(n^{-2})\), hence \(\sqrt{b_{n+1}}-\sqrt{b_n}=\sqrt\alpha+O(n^{-2})\). A finite set of strictly positive initial gaps and the positive limit give a strictly positive global square-root gap. The identity \(\mu B_0+\gamma S=0\), \(\mu>0\), additionally ensures both physical roots are negative; it is not needed for the abstract biorthogonal step.

## 2. Boundary normalization, input orientation and field class

Integration by parts gives
\[\int_0^L Y_{xx}\phi_n dx=-q_n^2Y_n+Y(0,s)\phi_n'(0)-Y(L,s)\phi_n'(L)
=-q_n^2Y_n+2a(s)\sqrt{2/L}\,q_n.\]
Thus the input in the ODE is exactly \((C_n a(s),0)^T\), not half that factor and with the displayed sign for the stated boundary convention. Set \(f(t)=a(-t)\), \(0\le t\le T\); then \(a(-T)=f(T)\), \(a(0)=f(0)\), and the zero-start Duhamel integral is
\[\binom{Y_n(0)}{P_n(0)}=C_n\int_0^T e^{tD_n}\binom10 f(t)dt.\tag{2}\]
For the constructed smooth f, \(f(T)=0\) ensures compatibility with zero temperature at the starting time. A smooth boundary lift \(Y=Z+a(s)(1-2x/L)\) converts the odd PDE to a homogeneous-Dirichlet heat equation coupled to a bounded ODE on \(L^2(0,L)^2\), with smooth L² forcing and zero initial data. Standard semigroup theory then yields a continuous L²-valued pair and permits the individual integrations by parts/variation-of-constants formula. \(f(0)=0\) makes the terminal boundary values zero. This is stronger than relying on arbitrary L² boundary input; a full weak formulation remains an assumption to be checked against the frozen original model.

## 3. Duhamel and exact pairing

The spectral projector formula gives
\[e^{tD_n}\binom10=\frac1{b_n+\delta_n}
\binom{\delta_ne^{(-\mu+\delta_n)t}+b_ne^{(-\mu-b_n)t}}
{\gamma[e^{(-\mu+\delta_n)t}-e^{(-\mu-b_n)t}]}.
\tag{3}\]
Let \(v=Qk\), \(f=e^{\mu t}tv\), and \(F(z)=\int_0^T e^{zt}f(t)dt\). Then
\[F(-\mu+\delta_n)=\int_0^T t e^{\delta_nt}v(t)dt,\quad
F(-\mu-b_n)=\int_0^T t e^{-b_nt}v(t)dt.\]
Equation (2) gives
\[Y_n(0)=\frac{C_n b_n}{b_n+\delta_n}\int_0^T t v(t)\left[e^{-b_nt}+\frac{d}{b_n^2}e^{\delta_nt}\right]dt.\tag{4}\]
The scaling factor \(C_nb_n/(b_n+\delta_n)\) is positive and is **not** part of the definition of the correction residual. Thus \(Y_n(0)=0\) iff \((\mathsf Dv)_n=0\).

For \(k=(I+\mathsf T)v\), expanding \(H_d\) and using \(\int_0^\infty t e^{-bt}H_d(t,s)dt=b^{-2}e^{ds/b}\) gives
\[\begin{aligned}
(\mathsf Bk)_n&=\int_0^T te^{-b_nt}(v+\mathsf Tv)(t)dt+\int_T^\infty te^{-b_nt}\mathsf Tv(t)dt\\
&=\int_0^T t e^{-b_nt}v(t)dt+\frac d{b_n^2}\int_0^T s e^{ds/b_n}v(s)ds=(\mathsf Dv)_n.
\end{aligned}\tag{5}\]
This directly checks the **plus tail**, slow factor \(d/b_n^2\), and identity for every n. Smoothness gives convergence and endpoint traces. Since \(Y(0)\) is L² and its entire odd sine-basis coefficient sequence is zero, the terminal odd temperature is zero as an L² field.

## 4. Memory and qualitative features

Under (4), \(F(-\mu-b_n)=-(d/b_n^2)F(-\mu+\delta_n)\). Substitution into the second row of (3) yields
\[P_n(0)=\frac{C_n\gamma}{b_n}F(-\mu+\delta_n)=\frac{C_n\gamma}{b_n}\int_0^T te^{dt/b_n}v(t)dt.\tag{6}\]
No additional \(\delta_n\), \(\mu\), or endpoint term remains. If \(v\ne0\), the entire function \(G(z)=\int_0^T te^{zt}v(t)dt\) is nonzero: otherwise polynomial moments vanish and v=0 in H. Its zeros cannot accumulate at 0, so all but finitely many \(P_n\) are nonzero (assuming the physical \(\gamma\ne0\), implied by d>0 with finite S). The sequence is the coefficient sequence of the above L² memory field; no stronger trace regularity is inferred.

If a constructed k is nonzero, v is nonzero since Q is injective. The weights in (4) are strictly positive, so real v and f must change sign. k vanishes near 0 and T, and \(v=k-\mathsf Tv\), so v and f are analytic near both endpoints. If f vanished on any (0,ε), then \(\mathsf Tv=0\) on that interval and, by analyticity, everywhere. The positive kernel expansion implies all weighted moments of v vanish, hence v=0: contradiction. If f were real analytic on an open connected neighborhood of [0,T], then k would also be real analytic there (the apparent t=0 quotient extends smoothly and analytically), yet it vanishes near 0 and is nonzero: contradiction. Thus the control is nonanalytic on the full interval and has no terminal switch-off gap.
