# Candidate 1: singular integral and invisible-state proof audit

Cycle 4 checkpoint. This is Arena's independent recalculation of the earlier construction, not an independent human certification. This is an alternative model, not the frozen Direction 2 experiment. The notations and PDE are those in `autonomous-five-candidate-discovery-audit.md` §6.

## Principal value identity

For real or complex \(\rho\in L^2(a,b)\), write \(L(r)=\log((b-r)/(r-a))\), and suppose \(\rho L\in L^2(a,b)\). This is a sufficient **and necessary condition for the displayed decomposition to define an \(L^2\) coefficient**: the finite-interval Hilbert transform \(H\rho=\mathrm{pv}\int_a^b\rho(s)/(s-r)ds\) is bounded on \(L^2\) by extending \(\rho\) by zero to the line. Thus \(K_\rho=\rho L+H\rho\in L^2\) iff \(\rho L\in L^2\). This is not claimed to be the weakest assumption for a distributional identity or some other solution class.

For each \(\varepsilon>0\), diagonal exclusion and Fubini are legitimate on the finite square: the excluded kernel is bounded and \(\rho\in L^1\). Interchanging the two rate variables gives
\[
\iint_{|r-s|>\varepsilon}\rho(s){e^{-st}-e^{-rt}\over r-s}\,drds
=\int_a^b e^{-rt}K_{\rho,\varepsilon}(r)dr,
\quad K_{\rho,\varepsilon}(r)=\int_{|s-r|>\varepsilon}{\rho(r)+\rho(s)\over s-r}ds.
\]
The original difference quotient has absolute value at most \(t\) for \(t\ge0\); since \(\rho\in L^1\), the removed strip tends to zero by dominated convergence. The second term in \(K_{\rho,\varepsilon}\) converges in \(L^2\) to \(H\rho\). The first is \(\rho(r)L_\varepsilon(r)\), where \(L_\varepsilon=\log(\max(b-r,\varepsilon)/\max(r-a,\varepsilon))\) for sufficiently small \(\varepsilon\). It tends pointwise to \(L\), and \(|L_\varepsilon|\le |\log(b-r)|+|\log(r-a)|\) up to a fixed constant; equivalently, endpoint-by-endpoint it is bounded by \(|L|+C\). Weighted dominated convergence gives convergence in \(L^2\). Therefore
\[
\int_a^b\!\int_0^t e^{-r(t-s)}f(s)ds\,dr=\int_a^b e^{-rt}K_\rho(r)dr,\quad f(t)=\int_a^be^{-rt}\rho(r)dr.
\]
The two logarithms matter: the alternate form is \(K=2\rho L+\int(\rho(s)-\rho(r))/(s-r)ds\) when the latter integral is classically meaningful. The sign is as in the earlier report.

## Initial condition, flux, nontriviality and uniqueness

Choose nonzero \(\rho\in C_c^\infty(a,b)\) with zero integral and nonzero \(\psi\in C_c^\infty(0,L)\). Set \(u=\psi f\) and
\[
h=-r\rho\psi-\kappa\rho\psi''-\gamma K_\rho\psi,\qquad
p=e^{-rt}h+\gamma\psi\int_0^t e^{-r(t-s)}f(s)ds.
\]
The identity proves \(\int p\,dr=u_t-\kappa u_{xx}\) for every \(t\ge0\), with \(p(0)=h\), \(u(0)=0\). Both temperature boundary values and both endpoint derivatives vanish for all times, including before the observation delay. This provides an entire pre-delay solution rather than independently prescribed delayed data. \(f\not\equiv0\), since all polynomial moments zero would imply \(\rho=0\) by polynomial density. Hence \(u\ne0\), and \(h\ne0\): for two solutions with the same initial data, test the heat difference by \(u\), the ODE difference by \(p\), and apply Young's inequality and Gronwall. The bounded rate interval and nonzero finite \(\gamma\) suffice for uniqueness in the natural \(L^2_x\oplus L^2_{x,r}\) energy class.

The construction works for either sign of \(\gamma\). For \(\gamma<0\), the quadratic energy \(\|u\|_2^2-(1/\gamma)\|p\|_2^2\) has derivative \(-2\kappa\|u_x\|_2^2+(2/\gamma)\int r|p|^2\le0\), so this alternative system has a positive dissipative storage. This does **not** make the constructed initial state a mechanically compatible common prehistory; see the companion range report. Exact physical nonuniqueness and novelty remain unproved.
