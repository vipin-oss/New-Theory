# Full linearized control geometry

Let \(Y,P,V\) be first variations of \(y,p,v\), with \(P\) mean-zero, \(\mathcal M=cI+d\theta_*Q\), \(B=-br\gamma\theta_*\), \(S=br\mu\theta_*\). At the relaxed zero-control base, the exact linearization is
\[\mathcal M Y_s=\kappa Y_{xx}+B QY+SP-b\theta_*m',\quad P_s=-\mu P+\gamma QY,\quad V_s=\lambda(m-V).\tag{1}\]
The endpoint temperatures are \(Y(0)=\tau_s+\tau_a\), \(Y(L)=\tau_s-\tau_a\). The linearized \(w^2\) term vanishes. Parity is invariant: the odd subsystem is the Cycle 10 system, driven only by \(\tau_a\); the even subsystem is (1) restricted to even fields and driven by \(m,\tau_s\). On even fields \(Q\) removes the spatial mean and is not diagonal in the even Dirichlet sine basis. Mechanical forcing is spatially constant. \(V(0)=\lambda\int_{-T}^0 e^{\lambda s}m(s)ds\); odd \(P\) cannot be altered at first order by the two even controls. This establishes that the flat no-gap odd obstruction persists under arbitrary admissible even first-order controls, but says nothing about whether nonzero **even or mean** memory can coexist with thermal nulling.

## Full formal adjoint and joint map

For endpoint tests \((\eta,h,\xi)\in L^2\times L^2_0\times\mathbb R\), the backward equations are
\[-\mathcal M\phi_s=\kappa\phi_{xx}+BQ\phi+\gamma\psi,\quad -\psi_s=SQ\phi-\mu\psi,\quad -\nu_s=-\lambda\nu,\]
\[\phi|_{\partial I}=0,\quad \mathcal M\phi(0)=\eta,\quad \psi(0)=h,\quad \nu(0)=\xi,\quad \bar\psi=0.\]
For smooth lifted inputs and tests the joint pairing is
\[\langle Y(0),\eta\rangle+\langle P(0),h\rangle+\xi V(0)=\int_{-T}^0\{\kappa[\tau_0\phi_x(0)-\tau_L\phi_x(L)]-b\theta_*m'\!\int_I\phi\,dx+\lambda m\nu\}\,ds.\tag{2}\]
The \(m'\) term is retained; converting it to a control on \(m\) requires a time integration by parts and endpoint/trace hypotheses. The formula is rigorous for the stated smooth class by integration by parts; its extension to a particular rough input topology needs the corresponding admissibility bound, not assumed here. Parity then specializes (2) to the rigorously bounded odd fixed-gap adjoint in Cycle 10. Full even joint-map range, compactness and null-control properties remain open; no claim that extra controls cancel the odd mode is made.
