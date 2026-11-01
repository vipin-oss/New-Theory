# Cycle 10: adjoint, signed moment synthesis and control constraint

Let \(Y,P\) solve the linear odd system in `direction-2-cycle10-linearized-control-system.md`, with terminal pair \((Y(0),P(0))\). For terminal test functions \((\eta,h)\in H_o\times H_o\), solve backward
\[-M\phi_s-\kappa\phi_{xx}=B\phi+\gamma\psi,\qquad -\psi_s=S\phi-\mu\psi,\qquad \phi|_{\partial I}=0,\quad M\phi(0)=\eta,\quad\psi(0)=h.\tag{1}\]
For the unreduced full space, the mass at equilibrium is \(cI+d\theta_*Q\), self-adjoint; (1) is its odd restriction \(MI\). Green's identity gives
\[\langle Y(0),\eta\rangle+\langle P(0),h\rangle=2\kappa\int_{-T_p}^0 a(s)\phi_x(0,s)ds.\tag{2}\]
The sign follows from \(-\kappa\int_{\partial I}Y\partial_\nu\phi\): at the left/right \(Y=(a,-a)\), \(\partial_\nu\phi=(-\phi_x(0),\phi_x(L))\), and odd \(\phi\) has \(\phi_x(L)=\phi_x(0)\). First establish (2) for finite sine adjoint data and smooth lifted controls, then pass by boundedness on a fixed positive terminal gap; boundary evaluation of arbitrary \(L^2\) data is not used.

Let \(\mathcal A a=Y(0)\), \(\mathcal K a=P(0)\), acting on \(U=L^2(-T_p,-\varepsilon)\). Their joint adjoint is (2)'s boundary trace. For \(\eta=0\), finite-mode calculation gives, with \(t=-s\in[\varepsilon,T_p]\),
\[\mathcal K^*h(-t)=\sum_{n\ge1}h_n\frac{2\kappa c_Lq_n\gamma}{M\Delta_n}\left(e^{\lambda_{n,+}t}-e^{\lambda_{n,-}t}\right).\tag{3}\]
The coefficients \(q_n/\Delta_n=O(1/q_n)\), so the series converges absolutely uniformly for \(t\ge\varepsilon\) by Cauchy–Schwarz. It is \(\gamma/(A_0 S)\) times the already audited constant-reference flux synthesis in `direction-2-cycle6-reference-infinite-mode-injectivity.md`. The latter is injective on signed \(\ell^2\) coefficients on any nonempty positive time interval: analyticity and isolated fast poles prove this, not finite rank. Consequently \(\ker\mathcal K^*=0\) and \(\overline{\operatorname{ran}\mathcal K}=H_o\). This proves injectivity of the infinite **synthesis** (3), not completeness of \(\{k_n\}\) as functions spanning all of \(L^2\) time. No bounded inverse or exact reachability follows.

The exact null-temperature condition is \(\mathcal A a=0\). For general bounded \(\mathcal A,\mathcal K\), the constrained memory-range annihilator is
\[(\mathcal K\ker\mathcal A)^\perp=\{h:\mathcal K^*h\in(\ker\mathcal A)^\perp=\overline{\operatorname{ran}\mathcal A^*}\}.\tag{4}\]
Closure is essential: no bounded separator is posited. For the fixed gap, the direct moment calculation in the terminal-constraint report proves the stronger special fact \(\ker\mathcal A=\{0\}\). This is a statement about controls supported away from the terminal time, not all endpoint-restored controls.
