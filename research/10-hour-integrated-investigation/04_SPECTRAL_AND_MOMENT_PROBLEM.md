# Spectral branches and terminal moments

The linear odd derivation, boundary factor and terminal pair are in Cycle 10 and the flat-control theorem. Put \(x_n=A_n-\mu\to\infty\). Solving \(\delta_n(x_n+\delta_n)=d_0\) by substitution gives
\[\delta_n=d_0x_n^{-1}-d_0^2x_n^{-3}+2d_0^3x_n^{-5}+O(x_n^{-7}),\quad \lambda_{n,+}=-\mu+\delta_n,\quad \lambda_{n,-}=-A_n-\delta_n,\]
\[\Delta_n=x_n+2\delta_n,\quad \Delta_n^{-1}=x_n^{-1}-2d_0x_n^{-3}+O(x_n^{-5}),\quad \delta_n/\Delta_n=d_0x_n^{-2}-3d_0^2x_n^{-4}+O(x_n^{-6}).\]
The other temperature coefficient is \(1-\delta_n/\Delta_n\); memory response is \(C_n\gamma/\Delta_n=O(q_n^{-1})\) and slow temperature response is \(C_n\delta_n/\Delta_n=O(q_n^{-3})\). The fast temperature coefficient is \(O(q_n)\), but on any fixed time gap its terminal action is exponentially suppressed. These expansions hold uniformly for large n at fixed physical parameters; constants are not asserted uniform over degenerate parameter limits.

The exact modal formulas and the fast/slow moment constraints are (2)–(3) in `05_NO_GAP_CONTROL_THEOREMS.md`. In particular the ratio in the temperature equation is \(b_n/\delta_n\sim x_n^2/d_0\), not merely \(O(1)\). The simultaneous assignment \((Y(0),P(0))=(0,h)\) demands both moment equations for every n; no interchange of infinite sums is needed to derive their necessity. Numerical diagonalization is not used as a proof of their solvability.
