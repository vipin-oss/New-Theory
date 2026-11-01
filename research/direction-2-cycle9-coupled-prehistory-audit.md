# Cycle 9: audit of the earlier constitutive prehistory

Let \(h\) be an odd nonzero spatial profile and \(r=k/(a+k)\). The prior report's strain, renamed \(\varepsilon=u_x\) to avoid confusion with mean memory, is
\[\varepsilon(s,x)=f(s)h(x),\quad f(s)=(6-2r)e^{\lambda s}+(3r-6)e^{2\lambda s}.\]
The exact isolated ODE solution from \(-\infty\) is \(z(s,x)=\zeta(s)h(x)\),
\[\zeta(s)=\tfrac12(6-2r)e^{\lambda s}+\tfrac13(3r-6)e^{2\lambda s}.\]
Thus \(f(0)=r\), \(\zeta(0)=1\), and \(\zeta'=\lambda(f-\zeta)\). The exponential decay provides finite time-weighted \(L^2\) strain energy; spatial regularity is inherited from \(h\). Since \(\bar h=0\), \(u(s,x)=f(s)\int_0^x h\) has zero endpoint displacement at all times. At \(s=0\), with \(\theta=\theta_*\), \((a+k)f(0)-k\zeta(0)=0\), so stress vanishes and equilibrium holds on that **slice**. The smooth finite-interval bump construction likewise solves the isolated ODE and terminal conditions, not automatically the coupled equations.

For an arbitrary temperature field the exact residuals of the constructed history are
\[R_{\rm mech}=\partial_x\sigma=[Df-k\zeta]h_x-b\theta_x,\]
\[R_{\rm heat}=c\theta_s-\kappa\theta_{xx}+b\theta f' h-k\lambda(f-\zeta)^2h^2,\quad R_z=z_s-\lambda(\varepsilon-z)=0.\tag{1}\]
Neither vanishes merely from the scalar ODE. The unprescribed \(\theta\) is constrained simultaneously by \(R_{\rm mech}=0\), the thermal PDE and fixed baths. If one sets \(\theta=\theta_*\) for the whole past, \(R_{\rm mech}=C(s)h_x\), \(C=Df-k\zeta\), which is nonzero in general. In fact \(C(0)=0\) but
\[C'(0)=\lambda D(5r-r^2-6)=-\lambda D(2-r)(3-r)\ne0\quad(0<r<1),\]
so it fails at all sufficiently small negative times for nonconstant \(h\).

There is a stronger failure for the **explicit exponential construction** and a smooth nonzero sine-prior \(h\), with both baths fixed. Mechanical equilibrium forces \(b(\theta-\theta_*)=C(s)h(x)+c_0(s)\); the two endpoints have \(h(0)=h(L)=0\), hence \(c_0=0\). Substitution into (1) yields an odd part \((cC'/b)h-(\kappa C/b)h''+b\theta_*f'h\) and an even part
\[[C f'-k\lambda(f-\zeta)^2]h^2.\]
As \(s\uparrow0\), the even coefficient tends to \(-k\lambda(1-r)^2<0\), so it is nonzero on a preceding interval. Because \(h^2\not\equiv0\), the even part cannot vanish. Thus no sufficiently regular temperature can complete this specific prehistory into a full coupled fixed-bath solution. This does not rule out another history, another preparation, or weak solutions outside the stated regularity. No arbitrary body force, heat source or spatially varying stress is used to repair it.
