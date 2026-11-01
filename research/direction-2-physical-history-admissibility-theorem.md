# Direction 2: prehistory admissibility, and the different rate-spectrum model

**CONDITIONALLY PROVED for the isolated constitutive ODE; OPEN for a complete coupled physical past.** The user's \(h_v(x,r)=\gamma\int_{-\infty}^0e^{rs}v(x,s)ds\) has a continuous rate coordinate \(r\). The frozen Direction 2 model has instead a single internal variable \(z\), relaxation rate \(\lambda\), and \(z_t+\lambda z=\lambda u_x\); its odd linearized variable has rate \(\mu=\lambda a/(a+k)\) after eliminating equilibrium. These are not interchangeable history maps, and the common history driving the physical \(z\)-ODE is strain, not an independently prescribed spectrum.

## Exact scalar-rate constitutive range

For \(X=L^2_o(0,L)\) and histories \(v\in L^2((-\infty,0);X)\), define \(H_\lambda v=\lambda\int_{-\infty}^0e^{\lambda s}v(s)ds\). It is bounded by Cauchy–Schwarz and is **onto** \(X\): choose \(v(s)=2e^{\lambda s}h\), which gives \(H_\lambda v=h\). This history is smooth in time, exponentially decaying and finite-energy. Smooth compactly supported-in-the-past time profiles can also realize any \(h\): choose any \(\chi\in C_c^\infty((-\infty,0))\) with nonzero weighted integral and scale it to \(\lambda\int e^{\lambda s}\chi(s)ds=1\). Spatial smoothness of the past requires corresponding spatial smoothness of \(h\); one cannot infer \(H^2\) regularity from arbitrary \(L^2\) input.

A stronger compatibility check at the frozen initial time is possible without solving the past PDE. Write \(r_0=k/(a+k)\in(0,1)\). For odd \(h\), let
\[v(s,x)=\big[(6-2r_0)e^{\lambda s}+(3r_0-6)e^{2\lambda s}\big]h(x),\quad s\le0.\]
Then \(v(0)=r_0h\) and \(\lambda\int_{-\infty}^0e^{\lambda s}v(s)ds=h\). Define \(z(s)=\lambda\int_{-\infty}^{s}e^{-\lambda(s-\tau)}v(\tau)d\tau\) and \(u(s,x)=\int_0^xv(s,\xi)d\xi\). Mean-zero odd \(h\) gives \(u(s,0)=u(s,L)=0\). At \(s=0\), \(z=h\), \(u_x=r_0h\); with initial temperature \(\theta_*\), the frozen constitutive stress is identically zero, so the initial equilibrium and zero displacement endpoints are satisfied. This is an exact **ODE and initial-slice compatibility** construction. It is not a past solution of the coupled equilibrium/heat system; we have not prescribed or solved past temperature, stress, loading, entropy or positivity constraints.

The same two requirements can be met by a smooth time profile supported in a finite interval ending at zero: take \(\chi_1\in C_c^\infty((-\infty,0])\) with \(\chi_1(0)=1\), and a bump \(\chi_2\in C_c^\infty((-\infty,0))\) with nonzero weighted integral. Set \(v(s)=h[r_0\chi_1(s)+c\chi_2(s)]\), selecting \(c\) to make the weighted integral equal one. Compactness here means support in \([-R,0]\), not vanishing near the present. This realizes any odd \(h\) at the ODE level with the same slice compatibility.

## Distinct distributed-rate histories

For the *alternative* interval-of-rates model, the exact finite-energy common-history range is the restriction of vector \(H^2(\mathbb C_+;X)\), and its closure in \(L^2((a,b);X)\) is the whole space; it is proper and nonclosed. See `candidate-1-physical-history-reachability-theorem.md`. Smooth compact histories and exponentially weighted histories give dense subranges, not all states; the old particular invisible example is excluded from that specified common-history range only. This result is not a range theorem for the actual one-rate Direction 2 state.

**Unresolved:** thermodynamic admissibility and actual strain–temperature histories must satisfy the frozen equations and prescribed past boundary/loading conditions. The scalar-rate construction is neither a proof that every state has such a past nor a physical nonuniqueness example. A physically admissible exact kernel vector remains unconstructed.
