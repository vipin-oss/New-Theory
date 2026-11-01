# Rigorous boundary positivity and adjoint cone investigation

**Date:** 1 November 2026. **Overall verdict: REFORMULATE.** Under the unchanged base hypotheses, the cooperative comparison is sound after a correction to the latest report's coefficient-integrability justification. We prove that a nonzero cone input produces a nonzero, nonnegative interior temperature at almost every time while the coupling is uniformly positive, and we prove a corresponding **non-strict adjoint dual-cone property** on any observed part of that interval. We do not prove pointwise positivity throughout the interior, strictly positive boundary flux, delayed overlap for the actual parameter values, or full odd injectivity. No exact invisible input is constructed.

This is an independent single-agent Arena recalculation, not a certification by an independent human. Dr. Vipin Gupta is Principal Researcher and final decision-maker; ChatGPT is designated Independent Scientific Supervisor and Auditor; Arena is Research Scholar / Builder / Literature Investigator. This is an observation-and-state investigation, not a proposed continuum model or manuscript. No material, load, initial-data topology, delay, boundary condition, or solution class is altered. No demonstrated novelty is claimed.

## 1. Frozen problem, sources audited, and signs

The immediate predecessor and its boundary-flux, base-existence, active-base-regularity and transposition dependencies were inspected. Let \(I=(0,L)\), \(I_-=(0,\ell)\), \(\ell=L/2\), \(T=10/\lambda\), \(\delta=T/100\), \(J=(\delta,T)\), \(q=|g_*|/L>0\), and \(m(t)=(g_*/L)\sin^2(\pi t/T)\). Take the existing sufficient assumptions, in particular \(q<s_*\), not verified from actual numerical data. Put
\[
D=a+k,\quad r=k/D,\quad \alpha=a/D,\quad \beta=b/D,\quad \gamma=\lambda\beta,\quad \mu=\lambda\alpha,\quad d=b^2/D.
\]
The prescribed signs include \(a,k,c,\kappa,\lambda,\theta_*>0\), \(b\ne0\). Denote the symmetric active base temperature perturbation by \(y_b\), \(\theta_b=\theta_*+y_b\), and \(Qf=f-\bar f\). With zero base initial memory, exact ODE integration gives
\[
v_b=\lambda\int_0^t e^{-\lambda(t-s)}m(s)ds,\quad
p_b=\gamma\int_0^t e^{-\mu(t-s)}Qy_b(s)ds,\quad
w_b=m-v_b-\alpha p_b+\beta Qy_b. \tag{1}
\]
For odd input \(h\in X_o=H^2(I)\cap L^2_o(I)\), and for its bounded \(H_o=L^2_o(I)\) extension, the exact system and observation are
\[
M Y_t-\kappa Y_{xx}=BY+SP,\quad P_t+\mu P=\gamma Y,\quad
Y(\cdot,0)=0,\ P(\cdot,0)=h,\ Y|_{x=0,L}=0,\quad
\mathcal T h=2A_0\kappa Y_x(0,\cdot)|_J,
\]
\[
M=c+d\theta_b,\quad S=\lambda\alpha(br\theta_b-2kw_b),\quad
B=-dQ(y_b)_t-bE_b-br\gamma\theta_b+2k\gamma w_b. \tag{2}
\]
Here \(Y(\cdot,0)=0\) is an initial condition, not a consequence of the spatial endpoint conditions; no boundary condition is imposed on \(P\). No multiplication of \(SP\) into a scalar potential or erasure of memory is allowed. Reflection evenness of the base coefficients gives a Dirichlet temperature at \(x=\ell\) for odd solutions.

Since \(\operatorname{sgn}\gamma=\operatorname{sgn}b\), for either \(b>0\) or \(b<0\),
\[
S\gamma\ge\lambda\alpha|\gamma|\{ |b|r\theta_*-|b|r\|y_b(t)\|_\infty-2k\|w_b(t)\|_\infty\}. \tag{3}
\]
At the initial time this is strictly positive by the zero base state. In particular \(C_+=\operatorname{sgn}\gamma S\) and \(S\gamma\) have the same sign. The proof below refers to the sufficient hypothesis
\[
C_+(t,x)\ge c_0>0\quad\text{a.e. on }(0,t_1)\times I_- \tag{H+}
\]
for some \(t_1\le T\). Continuity and the explicit predecessor bound prove such a \(t_1>0\); its overlap with \(J\) is not established without further verified bounds. Restricting to a shorter interval makes its lower bound uniform.

## 2. Dimensional audit and exact sinusoid

Set \(\xi=x/L\), \(\sigma=t/T\), \(u(\xi,\sigma)=y_b(L\xi,T\sigma)/\theta_*\), \(\rho=\lambda T=10\), \(\eta=2k/(|b|r\theta_*)\), \(\zeta=|\beta|\theta_*\). In the physical units recorded by the existence report, \(m,w_b,q,\eta,\zeta,\alpha,\rho\) are dimensionless. If
\[
R_t\ge\|(y_b)_t\|_{L^2((0,T)\times I)},\qquad R_x\ge\operatorname*{ess\,sup}_t\|(y_b)_x(t)\|_{L^2(I)},
\]
then the dimensionless \(\mathfrak R=\max\{\sqrt{T/L}\,R_t/\theta_*,\sqrt L\,R_x/\theta_*\}\) bounds both \(\|u_\sigma\|_{L^2((0,1)^2)}\) and \(\sup_\sigma\|u_\xi\|_2\). Indeed the substitutions give the squares \(T R_t^2/(L\theta_*^2)\) and \(L R_x^2/\theta_*^2\). The existence report's \(R_b=2C_Bq\) controls these components in its **fixed chosen units**; assign the respective component units before rescaling, rather than treating the combined numerical norm as unit-invariant. Unit conversion applied consistently to physical quantities and component bounds leaves \(\mathfrak R,\eta,\zeta,q,\rho\) unchanged. Without the fixed normalization/conversion, a numerical value for \(\mathfrak R\) is not available.

By \(u(0)=0\) in time and the spatial zero boundary condition,
\[
\|u(\sigma)\|_2\le\mathfrak R\sqrt\sigma,\qquad
\|u(\sigma)\|_\infty^2\le2\|u(\sigma)\|_2\|u_\xi(\sigma)\|_2,
\qquad \|u(\sigma)\|_\infty\le\mathcal Y(\sigma)=\sqrt2\mathfrak R\sigma^{1/4}. \tag{4}
\]
Use \(\|Qy\|_\infty\le2\|y\|_\infty\) and monotonicity of \(\mathcal Y\). Writing \(m_0=g_*/L\), integration by parts yields
\[
\frac{m(T\sigma)-v_b(T\sigma)}{m_0}
=G_\rho(\sigma):=\pi\int_0^\sigma e^{-\rho(\sigma-v)}\sin(2\pi v)dv
=\frac{\pi[\rho\sin(2\pi\sigma)-2\pi\cos(2\pi\sigma)+2\pi e^{-\rho\sigma}]}{\rho^2+4\pi^2}. \tag{5}
\]
The formula is valid for either sign of \(g_*\). Its absolute-value comparison is
\[
|G_\rho(\sigma)|\le F_\rho(\sigma):=\pi\int_0^\sigma e^{-\rho(\sigma-v)}|\sin(2\pi v)|dv\le\pi^2\sigma^2.
\]
Also \(\alpha|\gamma|/\mu=|\beta|\), so (1) gives the sharper exact-kernel bound
\[
\|w_b(T\sigma)\|_\infty\le q|G_\rho(\sigma)|+2\zeta(2-e^{-\alpha\rho\sigma})\mathcal Y(\sigma). \tag{6}
\]
Replacing \(|G|\) by \(F\) yields the predecessor's (B); replacing \(F\) with \(\pi^2\sigma^2(1+\rho\sigma/3)\) and \(1-e^{-\alpha\rho\sigma}\) by \(\alpha\rho\sigma\) yields its (A), a conservative estimate. The original (A) can also be obtained directly from separate \(|m|\) and \(|v_b|\) bounds. Factors \(T,\lambda,\theta_*\) enter only as displayed; \(L\) enters through \(q\) and \(\mathfrak R\).

Define
\[
H(s)=\sup_{0\le v\le s}\{\mathcal Y(v)+\eta[q|G_\rho(v)|+2\zeta(2-e^{-\alpha\rho v})\mathcal Y(v)]\}. \tag{7}
\]
If \(H(s)\le1/2\), (3) gives \(S\gamma\ge\tfrac12\lambda\alpha|\gamma||b|r\theta_*\) through \(Ts\). This is sharper than the same supremum with \(F\), not necessarily sharper than every other independent estimate. The supremum cannot generally be removed on the basis of monotonicity: \(F'_\rho(1/2)=-\rho F_\rho(1/2)<0\), while the remaining positive terms need not dominate that derivative. The same issue applies to \(|G|\). No counterexample to the actual experiment is asserted. If \(H(0.01)<1/2\), continuity yields an explicitly certifiable \(s_1>0.01\) and \(t_1=Ts_1>\delta\); equality at 0.01 alone need not give overlap.

The full-horizon bound also checks out: under all independent sufficient existence assumptions, especially \(\theta_b\ge\theta_*/2\), and \(\|w_b\|_\infty\le C_wq\) with \(C_w=W_s+2C_BW_R\),
\[
S\gamma\ge\lambda\alpha|\gamma|(|b|r\theta_*/2-2kC_wq)>0
\quad\text{if }q<|b|r\theta_*/(4kC_w). \tag{8}
\]
The earlier denominator 8 gives the stronger quarter-nominal lower bound. Equality at denominator 4 gives only \(\ge0\). The bound does not verify itself for the experiment.

### Reproducible certification procedure

Use physical inputs \(a,k,b,c,\kappa,\lambda,\theta_*,L,g_*\), the prescribed \(T=10/\lambda\), and the exact chosen-unit Sobolev/linear-solver constants \(S_L,K_x,C_L,C_B,C_N,C_N'\) or independently certified component bounds \(R_t,R_x\). The cross-sectional factor \(A_0\) is needed to scale flux but not for coupling sign. All material inputs must be in consistent units; there are no invented values. First verify the three explicit existence inequalities (6.1) in `direction-2-formulation-A-existence-investigation.md` for the zero-memory base, including the positivity condition; derive \(R_t,R_x\) in those units. Then:

```text
rho = lambda*T; assert T == 10/lambda and q > 0
Rdim = max(sqrt(T/L)*Rt/theta_star, sqrt(L)*Rx/theta_star)
eta = 2*k/(abs(b)*r*theta_star); zeta = abs(beta)*theta_star
Y(v) = sqrt(2)*Rdim*v^(1/4)
G(v) = pi*(rho*sin(2*pi*v)-2*pi*cos(2*pi*v)
            +2*pi*exp(-rho*v))/(rho^2+4*pi^2)
Bnd(v) = Y(v)+eta*(q*abs(G(v))+2*zeta*(2-exp(-alpha*rho*v))*Y(v))
Use interval arithmetic or certified adaptive subdivision to bound sup Bnd on [0,s].
Find a certified s1 > 0.01 with sup(Bnd,[0,s1]) <= 1/2;
if none is certified, return INCONCLUSIVE, not a sign failure.
If found, overlap length is at least T*(s1-0.01).
```
For rigorous numerics, enclose the supremum on each subinterval, including the nonsmooth zero at \(v=0\) and zeros of \(G\); use outward-rounded interval evaluations, and refine until the desired upper bound is certified. A mere grid maximum is not a certificate. Since \(H\) is nondecreasing and continuous, certified bisection on \(s\) works, but it may fail to certify at equality. The existence constants are data-only in the fixed normalization, so they give a positive initial interval and, **if** the strict delayed test succeeds, a positive computable overlap lower bound. No positive delayed overlap follows numerically without supplied values.

## 3. Comparison and a correction to the preceding audit

The base provides globally \(M\ge m_0>0\), \(M,S\in L^\infty\), \(M_x\in L^\infty_tL^2_x\), \(B\in L^2_{t,x}\). On every positive-time strip \((a,T)\), \(a>0\), the base audit additionally provides \(B\in L^\infty_tL^2_x\cap L^2_tL^\infty_x\cap L^6_{t,x}\), and \(M,\kappa/M\) are spatially Lipschitz and time-Hölder in the reported senses. None of this implies \(B\in L^\infty_{t,x}\), or the stronger strip estimates all the way to \(t=0\).

**Correction:** the latest report justified global Gronwall with \(\|B(t)\|_2^4\) by saying \(B\in L^\infty_tL^2_x\) in the active class. The audited source establishes that stronger estimate on positive-time strips, not globally. The comparison result survives with the sharper exponent \(4/3\), as already correctly used in the earlier boundary-flux report. No change is made to either previous file.

For \(Z=\operatorname{sgn}\gamma P\), \(C_+=\operatorname{sgn}\gamma S\), and \(\operatorname{sgn}\gamma h\ge0\) on \(I_-\), we have under \(C_+\ge0\)
\[
M Y_t-\kappa Y_{xx}=BY+C_+Z,\quad Z_t+\mu Z=|\gamma|Y,\quad Y|_{0,\ell}=0. \tag{9}
\]
For the established strong-temperature/energy solution \(Y\in H^1_tL^2_x\cap L^2_tH^2_x\cap C_tH^1_0\), \(Z\in H^1_tL^2_x\), test the divided heat equation with \(-Y_-\), equivalently the original equation with \(-Y_-/M\), and the ODE with \(-Z_-\). The time-dependent test is in \(L^2_tH^1_0\); \(M^{-1}\in L^\infty\) and its spatial derivative is controlled by \(M_x\). The strong time derivative and Lipschitz truncation justify the chain rule without differentiating \(M\) in time. In one dimension,
\[
\|v\|_\infty^2\le2\|v\|_2\|v_x\|_2,\quad
\int |B|v^2\le\varepsilon\|v_x\|_2^2+C_\varepsilon\|B\|_2^{4/3}\|v\|_2^2,
\]
\[
\|M_x\|_2\|v\|_\infty\|v_x\|_2
\le\varepsilon\|v_x\|_2^2+C_\varepsilon\|M_x\|_2^4\|v\|_2^2.
\]
For \(v=Y_-\), the cooperative terms are bounded by \(C\|Y_-\|_2\|Z_-\|_2\), since \(-C_+ZY_-/M\le C Z_-Y_-\) and \(-|\gamma|YZ_-\le |\gamma|Y_-Z_-\). Thus
\[
\frac{d}{dt}(\|Y_-\|_2^2+\|Z_-\|_2^2)\le
C(1+\|M_x\|_2^4+\|B\|_2^{4/3})(\|Y_-\|_2^2+\|Z_-\|_2^2).
\]
The coefficient is integrable globally because \(4/3<2\), even without global \(L^\infty_tL^2_x\). Zero initial negative parts and Gronwall yield \(Y,Z\ge0\). For a.e. \(t\), \(Y(t)\in H^2(I_-)\) has a \(C^1\) spatial representative, so \(Y_x(t,0)\ge0\). The map \(Y\mapsto Y_x(0,\cdot)\) is a continuous trace \(L^2_tH^2_x\to L^2_t\). The inward derivative at the left endpoint is \(+Y_x(0,t)\), while the outward derivative is \(-Y_x(0,t)\). No strictness or pointwise time continuity of the derivative follows from this argument.

## 4. What can be proved beyond nonnegativity

**Proposition (nonzero temperature a.e.).** Assume (H+) and a nonzero \(h\in H_o\) with \(Z(0)=\operatorname{sgn}\gamma h\ge0\) on \(I_-\). Then for almost every \(t\in(0,t_1)\), \(Y(t)\ge0\) and \(Y(t)\not\equiv0\) in \(L^2(I_-)\). Consequently its continuous spatial representative is positive on some nonempty interior open set, possibly depending on \(t\). This also covers the actual \(H^2\) inputs.

**Proof.** Comparison and the exact ODE give \(Z(t)\ge e^{-\mu t}Z(0)\) a.e. in space-time. Therefore \(C_+Z\) is nonzero in \(L^2(I_-)\) at a.e. time, because \(c_0>0\) and \(Z(0)\ne0\). Suppose the set \(E=\{t:Y(t)=0\text{ in }L^2\}\) has positive measure. Since \(Y\in H^1_tL^2_x\), its derivative vanishes for a.e. \(t\in E\): apply the scalar level-set derivative property to a countable dense set of inner products. For a.e. such time \(Y(t)\in H^2\), hence \(Y_{xx}(t)=0\), and \(BY(t)=0\). Equation (9) then gives \(C_+Z(t)=0\), a contradiction. Finally \(H^1(I_-)\hookrightarrow C(\bar I_-)\). □

This establishes genuine interior response but **not** \(Y(x,t)>0\) at every interior point, positivity on a fixed spacetime cylinder, or any strict derivative at the endpoint. The proof uses no smooth Green kernel and works for nonzero \(L^2\) cone inputs, not just continuous initial data.

## 5. Integrating factor, weak improvement and direct barrier attempt

On any \([a,t_1']\subset(0,t_1)\), \(V=B/M\in L^2_tL^\infty_x\subset L^1_tL^\infty_x\). The same is **not established from the global \(L^2_{t,x}\) bound near zero**. Let \(K(t)=\|V(t)\|_{L^\infty_x}\) on such a strip and \(\widehat Y=e^{\int_a^tK(s)ds}Y\). With \(A=\kappa/M\), the equation is, a.e.,
\[
\widehat Y_t-A\widehat Y_{xx}=(V+K)\widehat Y+e^{\int_a^tK}C_+Z/M\ge0. \tag{10}
\]
The exponential is bounded and absolutely continuous. Its time derivative times \(Y\) is in \(L^1_tL^2_x\), not automatically \(L^2_tL^2_x\); here \(K\in L^2\) on a finite positive-time strip and \(Y\in L^\infty_tL^2_x\), so it is in fact \(L^2_tL^2_x\). Thus the transformed function retains the strong-temperature class on that strip. \(A\) is uniformly elliptic, spatially Lipschitz and time-Hölder there, and the source \((V+K)\widehat Y+e^{\int K}C_+Z/M\) is nonnegative in \(L^2\), not necessarily bounded or continuous. This removes the adverse potential for a supersolution comparison; it is not a positivity-improvement theorem.

A local barrier can be seeded where the source has a positive lower bound: for an actual nonzero \(H^2\) cone input, continuity gives an interior interval where \(Z(0)\ge h_0>0\); (H+) and (9) give a positive lower bound for the transformed source on a compact time strip there. A smooth compactly supported bump \(\phi\ge0\) inside that interval and sufficiently small \(\varepsilon>0\) give a local subsolution \(\varepsilon(1-e^{-\omega(t-a)})\phi\), by bounding its derivatives and using the positive source. This supplies a fixed interior region of strict positivity after \(a\), subject to the standard weak comparison on that subcylinder; the global negative-part proof applies to the difference. For a merely \(L^2\) input such a uniformly positive interval is not guaranteed.

The attempted continuation from this seed to **every** point and to the boundary would require a chain of weak barriers or a positive Dirichlet evolution kernel for the actual time-dependent \(A\). A naive stationary bump cannot be extended across an unseeded region while retaining a valid parabolic subsolution; positivity of a constant-coefficient heat kernel is not a representation of (10). We have not supplied a complete propagation/weak-Hopf construction. Neither the interior a.e. nonzero proposition nor the seed proves positive boundary slope. A sufficient separately proved statement would be: every nonnegative strong supersolution of \(u_t-Au_{xx}\ge0\) on a strip with the displayed ellipticity, regularity and nontrivial prior interior source satisfies \(u_x(0,t)>0\) for a.e. later time, with the derivative identified with its \(L^2\) trace. Its hypotheses and proof are not yet established here.

## 6. Strict flux and logical consequences

The strict boundary question remains **NOT ESTABLISHED** at the actual regularity. A classical Hopf lemma requires more than \(Y\ge0\): one needs prior local strict interior positivity, the right coefficient/solution class, and comparison of its boundary liminf quotient with the actual trace. Where \(Y(t)\in H^2\), a proven positive inward liminf quotient at that time would agree with \(Y_x(0,t)\); the point is to obtain the lemma for a.e. such time, not to assume pointwise time regularity. A local barrier would also need positive lower data on its entire inner parabolic boundary, not merely nonzero temperature somewhere.

If (H+) holds through \(t_1>\delta\) **and** a valid strict boundary theorem supplies \(Y_x(0,t)>0\) on a positive-measure subset of \((\delta,t_1)\) for each nonzero cone input, then \(\ker\mathcal T\) avoids that cone and its negative. Neither the strict-flux theorem nor the actual overlap is established. Positivity before \(\delta\) alone cannot supply delayed strictness.

Nonnegative output of cone inputs does not imply nonzero output. Strictly positive output for each nonzero cone input implies no nonzero kernel member in either cone, by linearity. It does **not** imply injectivity on their linear span: the simple positive linear map \((x_1,x_2)\mapsto x_1+x_2\) has strictly positive outputs on nonzero positive vectors but kills \((1,-1)\). This is a logical illustration, not a physical counterexample. In \(H_o\), the cone on the half-interval is generating: every signed input is a difference of two cone inputs. Thus its linear span is all \(H_o\), but that does not prevent cancellation. For \(X_o\), positive-part splitting need not preserve \(H^2\); avoid assuming it does.

No total-positivity, sign-regularity or variation-diminishing result was verified for the actual two-component nonautonomous evolution and endpoint observation. Positivity of the scalar heat semigroup does not establish such a property for a heat–ODE memory coupling, and even variation diminution by itself would not automatically yield injectivity. No modal decoupling or coefficientwise cancellation inference is valid here.

## 7. Rigorous adjoint cone and exact kernel

For \(f\in L^2(J)\), the forward zero-initial source problem defines a bounded functional on \(L^2((0,T)\times I)^2\). Its Riesz pair \((z_f,w_f)\) satisfies distributionally
\[
-\partial_t(Mz_f)-\kappa(z_f)_{xx}-Bz_f-\gamma w_f=0,\quad
-(w_f)_t+\mu w_f-Sz_f=0,\quad w_f(T)=0. \tag{11}
\]
The boundary data \(z_f(0,t)=2A_0\mathbf1_Jf\), \(z_f(L,t)=0\), and the temperature terminal condition are meant **only in forward-residual transposition**; no classical trace or pointwise terminal value for \(z_f\) is claimed. In contrast \(w_f\in H^1_tL^2_x\) and
\[
w_f(0)=\int_0^T e^{-\mu t}S(t)z_f(t)dt,\quad
\langle\mathcal T h,f\rangle=\langle h,\Pi_o w_f(0)\rangle_{L^2(I)}. \tag{12}
\]
This follows by subtracting \(e^{-\mu t}h\) from the forward memory and testing its source \(Se^{-\mu t}h\); the mass remains inside \(-\partial_t(Mz)\).

**Proved non-strict dual-cone result.** Assume \(C_+\ge0\) on \((0,t_1)\times I_-\), \(t_1>\delta\), and \(A_0\kappa>0\). If \(f\ge0\) and is supported in \(J\cap(0,t_1)\), then
\[
\operatorname{sgn}\gamma\,[\Pi_o w_f(0)](x)\ge0\quad\text{for a.e. }x\in I_-. \tag{13}
\]
Indeed the primal comparison gives \(\langle\mathcal T h,f\rangle\ge0\) for every \(h\in H_o\) with \(\operatorname{sgn}\gamma h|_{I_-}\ge0\). Every nonnegative \(L^2(I_-)\) test extends oddly after multiplying by \(\operatorname{sgn}\gamma\); oddness yields twice the half-interval pairing. Self-duality of the nonnegative \(L^2\) cone proves (13). This is established from the equations via the already proved forward comparison and transposition, without assuming a sign for \(z_f\) or \(w_f\) individually. Odd projection need not preserve positivity of a general full-domain function; (13) is a special dual consequence, not a generic projection property. The half-interval dual cone is the natural weighted-sign pairing.

Strict pairing \(\langle h,\Pi_o w_f(0)\rangle>0\) for every nonzero cone input is not proved for any particular nonnegative \(f\). Nor does (13) apply to controls extending beyond \(t_1\) unless sign is established there. This is cone preservation at the initial adjoint observation state, not a proved pointwise positivity theorem for the entire backward coupled solution. It cannot alone imply full-space injectivity.

As a bounded operator \(\mathcal T:H_o\to L^2(J)\), \(\mathcal T^*\) has domain all of \(L^2(J)\), with \(\mathcal T^*f=\Pi_o w_f(0)\). Its range orthogonal complement is exactly
\[
(\operatorname{ran}\mathcal T^*)^\perp=\{h\in H_o:\ Y_x(0,\cdot)=0\text{ in }L^2(J)\}=\ker\mathcal T. \tag{14}
\]
For such \(h\), (2) is still the same homogeneous coupled evolution with nonzero unknown initial memory and \(Y(\cdot,0)=0\); oddness makes the other endpoint derivative zero too. It does **not** imply \(Y\equiv0\), \(P(\delta)=0\), or a homogeneous scalar equation. The exact unresolved statement is: does zero left endpoint derivative on \(J\), for the actual reachable pair generated by (2), force \(h=0\)? A coupled boundary continuation/adjoint separation theorem, a valid coupled moment completeness proof, or another independent method could answer it. The variable even multipliers couple modes; no spectral or time-analytic decomposition has been established. An inhomogeneous scalar Carleman estimate leaves \(SP\) and a delayed memory snapshot. Hence density \(\overline{\operatorname{ran}\mathcal T^*}^{H_o}=H_o\) is open. Density in \(L^2\) implies separation of the actual \(H^2\) input set, but \(H^2\)-topology density is a different statement, and separation of \(H^2\) alone does not prove \(L^2\) density.

The pre-delay Fredholm and finite-Gram reductions remain as in the predecessor. \(D_\delta=e^{-\mu\delta}I+K_\delta\), with \(K_\delta:H_o\to H^2\cap H^1_0\), is Fredholm and preserves the stated Sobolev equivalence; its injectivity and joint backward uniqueness are open absent the unverified Neumann criterion. The finite Gram matrix tests the vertical fiber only with a basis of that fiber, and its actual rank is unknown. A forward upper energy bound cannot be reversed into a lower bound. Compactness does not establish noninjectivity.

## 8. Primary-source verification and limits

The search was targeted, not exhaustive. Primary theorem statements and the indicated proof passages, not just abstracts, were inspected; no new literature-wide priority or absence claim is made.

1. **Avner Friedman**, “Remarks on the maximum principle for parabolic equations and its applications,” *Pacific Journal of Mathematics* **8** (1958), [primary PDF](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-8/issue-2/Remarks-on-the-maximum-principle-for-parabolic-equations-and-its/pjm/1103040096.pdf), §2, Theorem 2 and proof. The paper assumes continuous coefficients on the closure, continuous solution there with continuous interior time and second spatial derivatives, nonpositive zero-order coefficient, an interior tangent sphere and strict interior comparison. It proves strict inward non-tangential liminf for a maximum using an exponential sphere barrier and classical weak maximum principle. Our \(B\) is not known continuous or bounded and \(Y\) is not known classical; strict interior comparison is also missing. It is not directly applicable. A weak adaptation would need a complete comparison and trace argument.
2. **Erik Ekström and Johan Tysk**, “A boundary point lemma for Black–Scholes type operators,” [primary text](https://www2.math.uu.se/~johantys/Hopf), Theorem 2.2, Hypothesis 2.1 and proof. Its special homogeneous Black–Scholes operator has coefficient matrix with specified continuity, local spatial Lipschitz properties and structural boundary degeneracy; it assumes a strict comparison near the boundary and a lower bound \(a_{11}\ge Cx_1^\beta\), \(0\le\beta<2\). The proof constructs an explicit barrier and uses a classical maximum principle. Our uniform ellipticity meets only part of the geometry: the rough potential, weak source-driven solution and prior strict comparison are not matched. The theorem's own boundary-face structure is different.
3. **Paul M. N. Feehan**, “Maximum principles for boundary-degenerate linear parabolic differential operators,” [arXiv:1306.5197v2](https://arxiv.org/html/1306.5197), Proposition 5.4 and proof steps, including the displayed barrier \(h=x_d\). This result uses a special degenerate boundary and a positive inward drift at the relevant boundary; it is not a general theorem for our nondegenerate endpoint with an unbounded potential. Its proof relies on the stated local coefficient properties and strict comparison, not just energy regularity. The PDF fetch failed; HTML statement/proof portions were inspected. No claim is made that a different result in the article cannot be adapted.
4. **D. P. Jha and R. K. George**, “Observability and Null Controllability for Parabolic Systems with Delay and Memory,” [arXiv:2506.22221v2](https://arxiv.org/html/2506.22221), Lemmas 3.5 and 3.7 and Proposition 3.8. The inspected ODE estimate assumes zero initial auxiliary memory, a moving interior region and its weight hypotheses; the Volterra proof uses a monotone weight and a short-time remainder. Proposition 3.8 has constant Laplacian principal part and interior observation. It is not a theorem about the actual unknown delayed memory with only endpoint flux. The displayed proof of Lemma 3.5 invokes an earlier moving-control estimate, so its full dependency chain was not independently verified.
5. **B. Schwarz**, “Totally positive differential systems,” *Pacific Journal of Mathematics* **32** (1970), [primary PDF](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-32/issue-1/Totally-positive-differential-systems/pjm/1102977536.pdf). Theorems 2–4 and their proofs were inspected: for continuous finite-dimensional matrix ODE coefficients, Theorem 2 characterizes total positivity by tridiagonality and nonnegative adjacent off-diagonals; Theorem 3 adds that neither adjacent coupling vanishes identically on any interval for strict total positivity; Theorem 4 proves the sign-variation inequality from strict total positivity. The proof uses compound matrices and their irreducibility. These finite-dimensional hypotheses and conclusions do not establish total positivity of the infinite-dimensional coupled parabolic–ODE endpoint map.

The available sources do not close all requested categories: no directly applicable primary theorem for positivity-improvement with this rough nonautonomous potential, weak boundary normal derivative, coupled PDE–ODE, and endpoint observation has been verified here. This is an explicit evidence gap, not a claim that no such theorem exists.

## 9. Theorem map and decision

| Question | Verdict | Precise status |
|---|---|---|
| Nonnegative comparison for cone inputs | **PROVED** | On any interval where \(C_+\ge0\), under the existing base/solution assumptions. |
| Strict interior positivity | **PROVED UNDER EXPLICIT ADDITIONAL HYPOTHESES** | For \(H^2\) cone inputs and uniform positive coupling, a source-seeded interior subcylinder is strictly positive; positivity at every interior point is **NOT ESTABLISHED**. For \(H_o\), nonzero nonnegative temperature holds a.e. in time. |
| Strict endpoint flux | **NOT ESTABLISHED** | Weak propagation, boundary barrier and trace link not completed. |
| Delayed window overlap | **PROVED UNDER EXPLICIT ADDITIONAL HYPOTHESES** | Certified strict (7) at 0.01 supplies overlap; actual parameters not verified. |
| Sign-cone kernel exclusion | **NOT ESTABLISHED** | Needs both overlap and strict boundary response. |
| Cancellation exclusion | **NOT ESTABLISHED** | Cone positivity does not give linear-space injectivity. |
| Adjoint cone preservation | **PROVED UNDER EXPLICIT ADDITIONAL HYPOTHESES** | (13) for nonnegative controls supported in the observed part of a cooperative interval; non-strict only. |
| Adjoint range density | **NOT ESTABLISHED** | Equivalent to the unresolved coupled zero-flux implication (14). |
| Full odd-channel injectivity | **NOT ESTABLISHED** | Neither density nor an independent injectivity proof. |
| Nonzero exact invisible input | **NOT ESTABLISHED** | No physical counterexample constructed. |
| New theorem beyond established positivity/observability | **NOT ESTABLISHED** | Elementary consequences above are derived here; literature priority and novelty not demonstrated. |
| New foundational continuum theory | **REFORMULATE** | This is an inverse observation/state question, not a new foundational constitutive theory. |

**Final verdict: REFORMULATE.** The most precise next target is an actual-class weak propagation and boundary-point result linking a nontrivial coupled source to the \(L^2\)-time derivative trace, plus a certified base-specific sign interval. A rigorous coupled separation argument could instead prove all-input injectivity without first proving boundary-to-interior continuation. Dr. Gupta remains the final decision-maker.
