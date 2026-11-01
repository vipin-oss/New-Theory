# Protocol comparison: exact status

Write time profiles with support in the preparation interval, all initial-compatible and with positive bath temperatures if chosen sufficiently small. The following are candidates, not demonstrated physical protocols.

| Protocol | Controls | Known linear conclusion / obstruction | Nonlinear and energy status |
|---|---|---|---|
| Asymmetric terminal-gap | \(m=\tau_s=0,\tau_a\in C_c^\infty\) | Odd thermal nulling forces zero control/memory | Positive nonzero feasible loop unproved |
| Asymmetric no-gap flat | \(\tau_a(s)=e^{-1/s^2}\chi(s)\) for \(s<0\), \(\chi\) smooth, initially cut off | New flat theorem excludes odd exact nulling unless input zero | Smooth nontrivial control itself is admissible as boundary data, not a feasible terminal loop |
| Asymmetric nonflat | \(\tau_a=s\chi(s)\) near 0 | Corner jet may balance odd memory; no full moment solution | Positivity/existence and exact endpoint remain open |
| Symmetric bath only | \(m=\tau_a=0\), \(\tau_s\) smooth | No odd memory by symmetry; even nonzero memory plus thermal null unknown | No physical endpoint construction |
| Mechanical only | \(m\ne0,\tau_s=\tau_a=0\) | Mean memory is a scalar weighted moment; full even temperature modes must also vanish | Mechanical work and dissipation require full solution |
| Sequential mechanical then thermal | \(m\) supported earlier than \(\tau_s,\tau_a\) | State at stage change is nonzero; later controls cannot be replaced by arbitrary independent memory | No terminal proof |
| Overlapping all controls | all three nonzero | At first order odd decouples; even mechanisms could affect even/mean memory | Mode mixing and terminal constraints open |
| Terminal recovery stage | arbitrary early controls followed by uncontrolled cooling | Fixed-gap theorem rules out purely odd linear exact thermal restoration from the relaxed start | No finite-time nonlinear exact-cooling theorem |

Each candidate has finite control norms in the chosen smooth class. Actual energy and entropy accounting are in `08`; finite control norm alone does not prove finite PDE energy, interior positivity or physical feasibility. No optimized protocol is claimed.
