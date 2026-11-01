# Critical asymptotics: artificial manufactured checks

All parameters, coefficients, exact fields and forcing here are **manufactured mathematical software tests**, not an active base or physical experiment. Both PDE and ODE have additional explicitly calculated forcing terms. They do not prove an asymptotic for the actual experiment; the analytical proof is in the new research report. No physical parameters are supplied.

Python 3.11+, NumPy 2, SciPy and Matplotlib:

```sh
python -m venv .venv
.venv/bin/pip install numpy scipy matplotlib
.venv/bin/python -m unittest discover -s code/direction-2-moment-analysis -v
.venv/bin/python -m unittest discover -s code/direction-2-critical-asymptotics -v
.venv/bin/python code/direction-2-critical-asymptotics/manufactured_high_frequency.py
.venv/bin/python code/direction-2-critical-asymptotics/solver_verification.py
.venv/bin/python code/direction-2-critical-asymptotics/mode_refinement.py
```

`manufactured_high_frequency.py` evaluates exact forced fields and both scaled output quantities for smooth and H²-but-not-H^2.1 coefficients. It verifies second- and fourth-order one-sided derivative formulas and observation-time quadrature, and writes `manufactured-asymptotics.png`. In the rough example the second derivative is unbounded at a single interior point; its arbitrary assigned point value does not affect the continuous a.e. forcing, but does affect a discrete quadrature, so FD mesh convergence is explicitly checked. `solver_verification.py` compares the independent finite-difference PDE–ODE solver with the exact manufactured solution, including mesh and time self-refinement. `mode_refinement.py` independently approximates the manufactured spatial boundary derivative by a truncated odd sine expansion; this is a representation check, not a full spectral time solver. The smooth example has finite Fourier support, while the rough example converges only algebraically. The graph shows exact manufactured mathematics, not measured data or a finite-difference result.

Use the existing active-base and supplied-coefficient solvers only when actual physical parameters or verified coefficient arrays become available. No actual-system numerical high-frequency conclusion is asserted.
