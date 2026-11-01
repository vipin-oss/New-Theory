# Moment-analysis diagnostic

The executed numerical experiments are abstract Hilbert-space examples plus an explicitly artificial constant-coefficient Galerkin software test, not the prescribed physical system. The active-base and Galerkin commands require user-supplied physical parameters or actual base coefficient arrays; they have not been validated on the real experiment. These programs are numerical diagnostics, not rigorous enclosures, completeness proofs, or nonlinear-admissibility tests.

## Installation and abstract tests

Python 3.11+, NumPy and SciPy are required. For example:

```sh
python -m venv .venv
.venv/bin/pip install numpy scipy
.venv/bin/python -m unittest discover -s code/direction-2-moment-analysis -v
.venv/bin/python code/direction-2-moment-analysis/moments.py abstract --sizes 4 8 16 32 64 --output-dim 4096
```

The two abstract operators are defined on sequence spaces with leading profile `e0/n`. They have, respectively, an injective synthesis and an explicit one-dimensional infinite kernel. The latter uses an infinite normalized vector with tail `v_n = const/n²`; finite output truncation is used for numerical tests. These examples are **not** thermoviscoelastic coefficient fields. Distances are calculated using SVD-based least-squares projection rather than a normal-equation inverse. Their reciprocals are the minimal control norms only when the target is outside the span of the other columns. Close-to-zero distances are numerically ill-conditioned and cannot certify exact rank.

## Parameterized active base

Provide a JSON file with numeric keys `a`, `k`, `b`, `c`, `kappa`, `lambda`, `L`, `A0`, `theta_star`, and `g_star`. All positive material inputs must be positive, and `b`, `g_star` must be nonzero. No defaults or sample physical values are provided. Run

```sh
.venv/bin/python code/direction-2-moment-analysis/moments.py base --params /path/to/actual-parameters.json --cells 100 --steps 1000 --output /path/to/base.npz
.venv/bin/python code/direction-2-moment-analysis/moments.py galerkin --input /path/to/base.npz --modes 12 --target 1
```

The first command approximates the nonzero-loaded base (finite-difference temperature, pointwise memory, trapezoidal mean, BDF time stepping). It includes `delta=T/100` in the output time grid and stores the actual-model coefficient formulas `M,B,S`; this is an approximation, not a verified solver or a certificate that the admissible class exists. `cells` and `steps` above are illustrative *discretization controls*, not material data. The parameters and active-base solution must be provided/verified by the user, and independent spatial, temporal, and solver-tolerance refinements are required.

## Supplying precomputed coefficients

Instead of running `base`, an NPZ file can contain arrays `t` (starting at 0 and including `delta` exactly), `x` (including 0 and L), and `M`, `B`, `S` of shape `(len(t),len(x))`; also scalar `gamma`, `mu`, `kappa`, `A0`, `L`, `delta`. Arrays must come from the actual nonzero-loaded base. The code checks shapes, finiteness, grid monotonicity, positive M and that the delay is interior, but **cannot** establish model provenance, parity, compatibility, or coefficient errors.

The Galerkin method uses the odd sine basis, a spatial quadrature mass matrix, BDF with interpolated coefficients, and a derivative trace of the Galerkin expansion. It weights observations by trapezoid quadrature on the delayed grid. It reports singular values, an augmented-family projection distance, and the reciprocal norm. The user must check grid resolution, symmetry, solver tolerances, independent numerical formulations, coefficient errors, and quadrature convergence. No current physical run, numerical table, plot, or assertion of finite/infinite rank is provided. If the augmented columns are linearly dependent, small computed distance/rank is merely a floating-point diagnostic.
