# Candidate 1: exact common-history range and its closure

This is an alternative-model result, not Direction 2. Let \(X=L^2(0,L)\), \(0<a<b\), \(\gamma\ne0\), and define \((Hv)(r)=\gamma\int_0^\infty e^{-rt}v(t)dt\) for \(v\in L^2(\mathbb R_+;X)\), restricted to \(r\in(a,b)\). The negative-time history is \(v(t)=v_{past}(-t)\). Bochner integrals are well-defined.

## Exact characterization

The vector-valued Paley–Wiener theorem gives an isometric Laplace transform (up to the conventional \(2\pi\) normalization) of \(L^2(\mathbb R_+;X)\) onto the vector Hardy space \(H^2(\mathbb C_+;X)\). Thus **exactly**
\[
\operatorname{ran}H=\{\gamma F|_{(a,b)}:F\in H^2(\mathbb C_+;X)\}\subset L^2((a,b);X).
\]
The restriction determines \(F\) uniquely by the identity theorem applied to all scalar dual pairings; hence it also determines the common \(L^2\) history uniquely. This is an exact range, not merely an analyticity necessary condition. For the representation \(h=\gamma F|_{(a,b)}\), the natural range norm is \(\|F\|_{H^2}\), up to normalization; it is not the ambient \(L^2_rX\) norm.

The range is dense: if \(g\in L^2((a,b);X)\) is orthogonal to it, then \(H^*g(t)=\gamma\int_a^b e^{-rt}g(r)dr=0\) a.e. \(t>0\). Its analytic Laplace transform vanishes identically; all \(\int r^n g(r)dr\) vanish, and polynomial density plus scalar dual pairings gives \(g=0\). It is proper: a nonzero rate function supported in a strict subinterval cannot be the restriction of a holomorphic function. Hence it is nonclosed.

For scalar \(X=\mathbb R\), \(H\) is Hilbert–Schmidt because \(\int_a^b\int_0^\infty e^{-2rt}dt\,dr<\infty\). In the actual infinite-dimensional spatial \(X\), however, \(H=H_{scalar}\otimes I_X\) is **not compact**: choose one nonzero history \(v_0\) and an orthonormal spatial sequence \(e_n\); images of \(v_0e_n\) remain orthogonal with constant positive norm. Nevertheless the inverse is unbounded even on a single fixed spatial direction, by compactness and injectivity of the scalar transform. Dense approximate reachability does not yield exact reachability or a bounded history reconstruction.

## Separate history classes

- Smooth compactly supported \(X\)-valued histories are dense in \(L^2_tX\); their images remain dense in \(L^2_rX\). Their exact range consists of restrictions of their actual Laplace transforms, which extend to entire \(X\)-valued functions of exponential type; entire continuation alone is not asserted sufficient without the appropriate inverse-transform support and regularity.
- Histories satisfying \(e^{\eta t}v\in L^2\), \(\eta>0\), extend holomorphically to \(\operatorname{Re}z>-\eta\). Conversely the shifted Hardy condition, not mere continuation, characterizes this weighted class. Its image is dense because it contains smooth compactly supported histories.
- Finite energy by itself gives the Hardy characterization above; compact support and smoothness are stronger, not equivalent. All these classes exclude the §6 example, because a spatial functional isolates its nonzero compactly supported rate density.
- Thermodynamic sign/storage and mechanical compatibility are separate restrictions. A common past satisfying a coupled mechanical PDE, boundary/loading conditions and a specified energy inequality is not the whole \(L^2_tX\) control class; its exact reachable graph and even density have not been established. The dissipative storage in the proof audit is not a proof of such compatibility.

## Stronger exclusion within the separated construction

Suppose \(\rho\) and \(K_\rho\) both extend analytically through \([a,b]\). Writing
\[K_\rho(r)=2\rho(r)\log\frac{b-r}{r-a}+\int_a^b\frac{\rho(s)-\rho(r)}{s-r}ds,\]
the last term extends analytically near either endpoint (the divided difference has a removable diagonal singularity). A holomorphic \(\rho\) not identically zero has a finite-order zero at an endpoint, so \(\rho(r)\log(r-a)\) cannot be holomorphic through it. Thus \(\rho=0\). In the separated ansatz of the proof audit, nonzero compactly supported \(\psi\) and \(\psi''\) are linearly independent. If its state \(h\) were in \(\operatorname{ran}H\), independent bounded spatial functionals isolate first \(\rho\), then \(K_\rho\), forcing both to be holomorphic in the right half-plane and hence \(\rho=0\). This rules out **all nontrivial examples of that separated form** satisfying the stated regularity, not just compactly supported \(\rho\). It does not prove injectivity for general reachable states or construct a reachable invisible state.

Restart: study general nonseparable histories and the actual coupled past graph; do not substitute dense range for exact reachability. The exact range and elementary transform facts may be classical; no novelty clearance or independent human audit is asserted.
