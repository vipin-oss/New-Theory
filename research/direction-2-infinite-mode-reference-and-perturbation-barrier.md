# Infinite-mode reference injectivity and a perturbative obstruction

**Decision for the actual nonautonomous system: OPEN.** This is Arena's calculation, not independent human certification or a novelty claim. The constant system below is an analytical comparison, not the frozen nonzero-load experiment; no physical parameters or boundary observations are changed in the actual problem.

## 1. Conditional theorem for the exact comparison system

Let \(H_o=L^2_o(0,L)\), \(\phi_n=\sqrt{2/L}\sin(q_nx)\), \(q_n=2\pi n/L\). Consider the constant comparison system used in `direction-2-finite-prior-independent-proof-audit.md`, §2:
\[M_0Y_t-\kappa Y_{xx}=B_0Y+S_0P,\quad P_t+\mu P=\gamma Y,\quad (Y,P)(0)=(0,h),\quad Y|_{\partial I}=0.\]
Assume \(M_0,\kappa,\mu>0\), \(B_0<0\), \(S_0\gamma>0\), and \(\mu\kappa q_n^2/M_0>0\) with the physical comparison relation \(a_n\mu-d_0=\mu\kappa q_n^2/M_0\), where \(a_n=(\kappa q_n^2-B_0)/M_0\), \(d_0=\gamma S_0/M_0\). In particular these are the signs and constants of the inherited frozen-system comparison; \(A_0\ne0\). Write \(\mathcal T_0h=2A_0\kappa Y_x(0,t)\) on any nonempty interval \(J\Subset(0,\infty)\).

**CONDITIONALLY PROVED:** \(\ker(\mathcal T_0:H_o\to L^2(J))=\{0\}\).

**Proof.** For \(h=\sum h_n\phi_n\), the mode roots are
\[\lambda_{n,\pm}=-(a_n+\mu)/2\pm\sqrt{(a_n-\mu)^2/4+d_0},\quad \Delta_n=\lambda_{n,+}-\lambda_{n,-}.\]
The characteristic equation gives \(\lambda_{n,-}<-\mu<\lambda_{n,+}<0\); both roots decrease strictly with \(a_n\), so roots are pairwise distinct, even across branches. As \(n\to\infty\), \(\Delta_n\asymp q_n^2\), \(\lambda_{n,+}\to-\mu\), and \(\lambda_{n,-}\to-\infty\). Thus
\[F(t)=2A_0\kappa\sqrt{2/L}\frac{S_0}{M_0}\sum_{n\ge1}h_n\frac{q_n}{\Delta_n}(e^{\lambda_{n,+}t}-e^{\lambda_{n,-}t}).\tag{1}\]
Since \(\sum |h_n|/q_n<\infty\), this series converges absolutely and locally uniformly on \(\operatorname{Re}t>0\), including its finitely many low modes. The Weierstrass theorem gives a holomorphic function there. The inherited forward trace estimate and finite-sine approximation identify its restriction with the actual comparison flux. If it vanishes a.e. on \(J\), continuity and the identity theorem give \(F(t)=0\) for all \(t>0\).

For \(\operatorname{Re}z>0\), the Laplace transform of (1), justified by absolute convergence, is
\[\widehat F(z)=C\sum_{n\ge1}\frac{h_nq_n}{(z-\lambda_{n,+})(z-\lambda_{n,-})},\quad C=2A_0\kappa\sqrt{2/L}\,S_0/M_0\ne0.\tag{2}\]
The series is locally uniformly convergent on \(\mathbb C\setminus(\{-\mu\}\cup\{\lambda_{n,\pm}\})\): on any compact set avoiding these points, for all sufficiently large \(n\) the first factor is bounded below and the second is \(\asymp q_n^2\), so the tail is dominated by \(\sum|h_n|/q_n\). The excluded set has only the finite accumulation point \(-\mu\); its complement is connected. Since \(\widehat F=0\) on the right half-plane, the identity theorem gives zero throughout that complement. At each isolated simple pole \(\lambda_{n,+}\), the locally uniformly convergent sum of the other terms is holomorphic and the residue is \(C h_nq_n/\Delta_n\). This must vanish, so every \(h_n=0\). □

This includes arbitrary infinite \(\ell^2\) combinations, not a finite Gram argument. It applies only to the comparison operator, with actual nonzero load and nonautonomous coefficients absent from the comparison. The analytic continuation is proved here for the constant comparison, **not** assumed for the active base. Compactness still forbids an \(L^2\) lower bound.

## 2. Why small operator-norm perturbation cannot transfer injectivity

**PROVED abstract obstruction.** Let \(T:H_o\to L^2(J)\) be compact and injective. For every \(\epsilon>0\) there is a rank-one \(E\) with \(\|E\|<\epsilon\) such that \(T+E\) has a nonzero kernel while remaining injective on *every* finite sine span. Further, the column perturbations can decay exponentially in the sine index.

**Proof.** For \(N\ge1\), set \(v_N=c\sum_{j\ge0}2^{-j}\phi_{N+j}\), with \(c=(\sum4^{-j})^{-1/2}\). Then \(\|v_N\|=1\), \(v_N\rightharpoonup0\), and \(\|Tv_N\|\to0\) by compactness. Define \(E_Nx=-\langle x,v_N\rangle Tv_N\). Then \(\|E_N\|=\|Tv_N\|\to0\), and \((T+E_N)v_N=0\). Since \(T\) is injective, \((T+E_N)x=0\) iff \(x=\langle x,v_N\rangle v_N\). Every nonzero multiple of \(v_N\) has infinitely many nonzero sine coefficients, so no nonzero finite sine combination is in this kernel. The columns \(E_N\phi_n=-\langle\phi_n,v_N\rangle Tv_N\) vanish for \(n<N\) and have exponentially decaying norm thereafter. Thus any existing leading \(1/q_n\) profile and \(o(q_n^{-3/2})\) remainder asymptotics are unchanged; if an \(H^1\) weighted residual square sum already held, this perturbation would preserve it as well. □

Applying the abstract result to the injective comparison operator from §1 demonstrates the precise insufficiency of an operator-norm small-load estimate, finite-prior injectivity, high-frequency column asymptotics, and even the separate \(H^1\) square sum, taken alone. **It does not construct an active-base coefficient perturbation, an admissible physical history, or an actual kernel vector.** The actual structured PDE perturbation may have extra properties; a proof must exploit them.

## 3. Concrete restart target

Either develop a structured nonautonomous replacement for the isolated-residue argument that preserves the actual pre-delay graph and is valid at \(B\in L^2\), or produce an actual coefficient-dependent infinite synthesis solution. The reference proof exposes precisely where the route breaks: the actual coefficients couple modes, need not be time analytic, and the Laplace-transformed response need not have the simple comparison resolvent or isolated poles. The operator counterexample shows that bounding the difference in operator norm—even while preserving all finite-prior injectivity—is not enough. The endpoint square sum remains a logically separate question.
