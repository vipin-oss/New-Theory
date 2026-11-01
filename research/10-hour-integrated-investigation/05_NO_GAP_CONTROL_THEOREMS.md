# No-gap terminal controls: flat-class obstruction

## Theorem (linearized odd subsystem; positive coupling)

Fix \(T>0\), the positive physical parameters of Cycle 10, and \(a\in C^\infty([-T,0])\), \(a(-T)=0\), with \(a^{(j)}(0)=0\) for every \(j\ge0\). No terminal switch-off gap is assumed: the control may be nonzero in every interval \((-\epsilon,0)\). If the terminal linearized temperature is zero in \(L^2(0,L)\), then \(a=0\) almost everywhere and the terminal odd memory is zero. Moreover, even without thermal nulling, if the terminal odd memory has finite sine support, then \(a=0\).

**Evidence level A** for the stated smooth class, using the homogeneous-boundary lifting and its standard linear energy solution; a direct formula for every coefficient is given below. This is a linearized theorem, not a nonlinear physical no-go result. The proof strengthens the prior fixed-gap argument to all flat \(C^\infty\) terminal histories, including standard compactly supported-in-time bump controls that touch the terminal time in their support. Gevrey histories that are flat are included; no restriction is asserted for nonflat Gevrey or analytic histories. No claim of chronological novelty is made.

## Proof

Put \(f(t)=a(-t)\) for \(0<t<T\) and \(F(z)=\int_0^T e^{zt}f(t)dt\). Since \(f\in L^1\), \(F\) is entire. For every integer \(N\ge1\), terminal flatness implies
\[ |F(-x)|\le C_N x^{-N},\qquad x\to+\infty.\tag{1}\]
Indeed, on \((0,\epsilon)\) Taylor's theorem gives \(|f(t)|\le C_Nt^{N-1}\); integrate this bound against \(e^{-xt}\). On \((\epsilon,T)\), Cauchy–Schwarz gives an exponentially small bound. No differentiability at \(T\) is required.

For the Cycle 10 odd modal system set \(\delta_n=\lambda_{n,+}+\mu\), \(b_n=-\lambda_{n,-}-\mu\). The characteristic equation yields \(\delta_n b_n=d_0>0\), \(b_n\asymp q_n^2\), \(\delta_n\asymp q_n^{-2}\), and \(-\lambda_{n,-}\asymp q_n^2\). The exact terminal modal equations are
\[Y_n(0)=\frac{C_n}{\Delta_n}\bigl(\delta_nF(\lambda_{n,+})+b_nF(\lambda_{n,-})\bigr),\quad P_n(0)=\frac{C_n\gamma}{\Delta_n}\bigl(F(\lambda_{n,+})-F(\lambda_{n,-})\bigr).\tag{2}\]
They follow from finite-dimensional variation of constants and boundary integration by parts. Smooth terminal-flat controls have zero Dirichlet value at \(s=0\); the smooth input belongs to \(H^1_0(-T,0)\), and the homogeneous-boundary lift gives the strong linear solution and justifies every coefficient equation. Equality of the terminal field to zero entails each coefficient is zero, hence
\[F(-\mu+\delta_n)=-\frac{b_n}{\delta_n}F(\lambda_{n,-}).\tag{3}\]
The prefactor is \(O(q_n^4)\). Combining this with (1) at \(x=-\lambda_{n,-}\) implies for **each** \(j\), \(F(-\mu+\delta_n)=o(\delta_n^j)\). If \(F\) had a first nonzero Taylor coefficient at \(-\mu\), its value at those positive \(\delta_n\to0\) would be asymptotic to a nonzero multiple of a fixed power, a contradiction. Thus all Taylor coefficients vanish, and the identity theorem gives \(F\equiv0\). Fourier uniqueness of the zero extension of \(f\in L^1(0,T)\) implies \(f=0\) almost everywhere. Substitution into (2) gives \(P=0\).

For the second assertion, finite sine support gives \(F(-\mu+\delta_n)=F(\lambda_{n,-})\) for all sufficiently large \(n\); (1) and the same Taylor argument again give \(F\equiv0\). ∎

## Nonflat controls and endpoint jets

For sufficiently smooth \(f\), Watson's elementary Laplace expansion gives \(F(-x)\sim\sum_{j\ge0}f^{(j)}(0)x^{-j-1}\), with finite-order remainder justified by Taylor's theorem and a time split. For endpoint-compatible \(f(0)=0\), (3) allows the finite limit \(F(-\mu)=-f'(0)/d_0\). This is not a contradiction. In the original time orientation, \(a_s(0)=d_0F(-\mu)\), consistent with the corner equation \(M a_s(0)=S P(0,0)\), \(P(0,0)=\gamma F(-\mu)\), when classical corner traces exist. Higher jets generate further necessary compatibility relations; we have **not** proved that they are sufficient or inconsistent. No nonzero solution has been constructed or excluded for general nonflat \(C^\infty\), \(H^1_0\), \(H^2\), or arbitrary \(L^2\) controls. \(L^2\) endpoint evaluation is generally not defined; its terminal state requires an admissible transposition topology.

## Alternative approaches and limits

1. Entire transform with an accumulation point plus flat endpoint decay gives the proof above. Accumulation alone is insufficient: the values are related to fast moments, not known to vanish.
2. A boundary unique-continuation argument would need to control the nondiffusive ODE trace and the final-time corner. Neither a boundary flux identity nor a scalar heat theorem supplies it. No such proof is claimed.
3. A biorthogonal/Riesz moment argument faces spectral condensation at \(-\mu\); standard separated-exponential hypotheses fail. Nonexistence of a standard biorthogonal family is not itself a no-go theorem.
4. The no-gap flat class is nonquasianalytic: \(e^{-1/t^2}\) for \(t>0\), extended by zero at \(t=0\), shows flatness alone does not make a control vanish. The result depends essentially on the entire moment constraints and both branches.

## A second no-gap theorem: sign-definite inputs

Let \(a\in L^1(-T,0)\) be real and either \(a\ge0\) a.e. or \(a\le0\) a.e. If its associated linear odd terminal temperature has all sine coefficients zero, then \(a=0\) a.e. No flatness, gap, endpoint trace or infinite-order argument is needed. This is a separate **Level A modal theorem**, valid whenever the terminal constraint is interpreted through the coefficient formula (2); the first coefficient is well-defined even if an arbitrary \(L^1\) control has no \(L^2\) terminal state. In particular it applies to every sign-definite \(H^1\), \(H^1_0\), \(H^2\), smooth, piecewise smooth, or bounded-variation control for which the endpoint problem is admissible. It does not extend to arbitrary sign-changing controls or to the nonlinear system.

Indeed the first temperature coefficient is
\[Y_1(0)=\frac{C_1}{\Delta_1}\int_0^T\bigl(\delta_1 e^{\lambda_{1,+}t}+b_1e^{\lambda_{1,-}t}\bigr)a(-t)\,dt.\]
Here \(C_1,\Delta_1,\delta_1,b_1\) are strictly positive and the exponential kernel is strictly positive on the whole compact interval. Thus any nonzero one-sign input makes \(Y_1(0)\ne0\); nulling even that single mode forces the input to vanish. Mechanical displacement and the symmetric bath cannot change this odd first variation. This is a necessary sign-changing condition, not a proof that some sign-changing input is feasible. The argument remains valid for any finite signed control measure of one sign if the modal formulation is meaningful; interpreting such measures as physical bath temperatures is a separate issue.
