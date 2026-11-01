# Candidate 2: variational shape derivative

**Status: CONDITIONALLY PROVED** for the smooth alternative two-dimensional scalar interface model, not the frozen Direction 2 system. Arena's self-audit is not independent human certification. The formula is a local derivative, not a proof of a trivial shape-derivative kernel or physical uniqueness.

## Geometry, model and assumptions

Let \(\Omega\) be smooth and bounded, \(D\Subset\Omega\) have a closed \(C^4\) boundary \(\Gamma\), and \(\mu_\pm>0\), \(\alpha\ge0\), \(\beta>0\) be fixed constants in the energy in discovery audit §8. Let \(V\in C_c^3(\Omega;\mathbb R^2)\), \(T_\varepsilon=\mathrm{Id}+\varepsilon V\), and transport the inclusion and interface by \(T_\varepsilon\); the exterior boundary and boundary data are fixed. The surface coefficients remain the same constants on the moving interface. Let \(u_f^\varepsilon\) solve the weak transmission problem for boundary value \(f\in H^{1/2}(\partial\Omega)\), and define the symmetric DtN pairing by its energy. On \(\Gamma\), write arc-length derivative \(\partial_s\), tangent \(\tau\), and \(j=\tau\cdot(DV)\tau\).

## Derivative with all terms represented

The pullback of the moving graph space is the fixed \(V_0\) of the interface-density audit. Change of variables gives, in operator norm on that space, a \(C^1\) family of coercive bilinear forms: the bulk coefficients involve \(DT_\varepsilon^{-1}\) and \(\det DT_\varepsilon\); the interface expression uses \(J_\varepsilon=|DT_\varepsilon\tau|\), \(J_\varepsilon^{-1}\), and \(\partial_sJ_\varepsilon\), all \(C^1\) in \(\varepsilon\) with bounded coefficients. Uniform coercivity holds for small \(\varepsilon\). A fixed lifting supported in an outer collar, followed by inversion of the coercive operator, gives \(C^1\) dependence of the pulled-back state in the graph norm. Differentiating the pairing and using stationarity against zero-boundary variations cancels both state derivative terms. Thus, for undeformed solutions \(u=u_f\), \(v=u_g\),
\[
\begin{aligned}
\langle\Lambda'_V f,g\rangle={}&\sum_{\pm}\mu_\pm\int_{\Omega_\pm}\big((\operatorname{div}V)I-DV-DV^T\big)\nabla u\cdot\nabla v\,dx\\
&+\int_\Gamma\big[-\alpha j\,u_s v_s-3\beta j\,u_{ss}v_{ss}-\beta j_s(u_s v_{ss}+u_{ss}v_s)\big]ds. \tag{1}
\end{aligned}
\]
Here \(\Omega_-=D\), \(\Omega_+=\Omega\setminus\bar D\); surface derivatives are of the common trace. This formula is bounded on the graph space; no strong conormal or curvature traces are needed for (1).

**Check of surface factors.** Under pullback, \(ds_\varepsilon=J_\varepsilon ds\), \(\partial_{s_\varepsilon}=J_\varepsilon^{-1}\partial_s\), and \(\partial_{s_\varepsilon}^2g=J_\varepsilon^{-2}g_{ss}-J_\varepsilon^{-3}(J_\varepsilon)_s g_s\). At zero, \(J'_0=j\). Differentiating the first- and second-order surface forms gives respectively \(-j g_sh_s\) and \(-3j g_{ss}h_{ss}-j_s(g_sh_{ss}+g_{ss}h_s)\). This independently fixes the coefficients and signs.

## Interface representation and sign convention

Assume additionally that both phase solutions are \(H^2\) near \(\Gamma\), so their normal derivatives have the necessary traces. Let \(n\) point from \(D\) into \(\Omega_+\), \(\tau_s=-\mathcal K n\), and choose a deformation normal at \(\Gamma\), \(V=\xi n\). Then \(j=\mathcal K\xi\), and integration by parts in the two harmonic phases turns the bulk part of (1) into
\[
\int_\Gamma\xi\{\mu_+(u_n^+v_n^+-u_sv_s)-\mu_-(u_n^-v_n^--u_sv_s)\}\,ds.\tag{2}
\]
The full interface formula is (2) plus the surface integral in (1) with \(j=\mathcal K\xi\). The jump condition itself is weakly encoded by the original form; no unproved classical fourth-order trace is invoked. Formula (2) follows from the divergence of \((V\cdot\nabla u)\nabla v+(V\cdot\nabla v)\nabla u-V(\nabla u\cdot\nabla v)\), with the exterior phase's inner outward normal \(-n\). Constants give zero surface terms. For a circle with uniform radial expansion, \(j\) is constant and the first- and second-gradient forms scale as radius to powers \(-1\) and \(-3\), confirming the factors.

## Kernel and partial patches

The kernel is the set of normal velocities \(\xi\) annihilating (1) for all admissible control/observation pairs; its triviality is **OPEN**. The earlier density of individual interface traces does not imply density of the needed products or normal-derivative terms. Under the connected exterior-collar and reciprocity assumptions of `candidate-2-partial-data-shape-identifiability.md`, the derivative response has homogeneous Dirichlet data and is harmonic in the unchanged collar. The same two-step UCP argument therefore reduces zero disjoint-patch derivative to zero full-boundary derivative. This does not prove the latter kernel is zero. No current literature claim of novelty is made.
