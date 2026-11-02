# Candidate nonlocal thermoelasticity package — status

**Not submission-ready.** The model is a thermodynamically structured periodic one-dimensional candidate, not a verified new theory. The literal requirements of full primary-source comparison, general Green–Lindsay and exact-delay DPL recovery, and published numerical benchmark reproduction remain unmet. See LITERATURE.md, MANUSCRIPT.md, RESULTS.md and STATUS.md. No independent review, experimental validation, PDF compilation or journal acceptance is claimed.

## Run
Requires Python 3.10+ and NumPy, SciPy, SymPy. For example, in an environment with package access:

    python -m venv .venv
    . .venv/bin/activate
    python -m pip install -r requirements.txt
    python -m unittest discover -v -s . -p 'test_*.py'
    python benchmark.py

Run these commands from this directory. The tested versions are listed in RESULTS.md. Code uses complex Fourier coefficients; zero coefficient or reduced-state cases do not all have a positive-definite five-variable metric. The code is research illustration, not production numerical software.
