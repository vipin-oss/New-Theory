# Counterattempts and remaining verification obligations

These labels describe this agent's review only; they do not imply an independent reviewer participated.

| Challenge | Status | Result |
|---|---|---|
| Fast annihilator might be a measure but not a smooth function | VERIFIED UNDER EXPLICIT ASSUMPTIONS | Compactly supported measure convolved with a compact bump remains an annihilator and is nonzero; disjoint intervals give infinitely many. See `FREDHOLM_RANGE_AND_ENDPOINT_CHECK.md`. |
| Convolution might destroy moments or introduce a zero denominator | VERIFIED | Laplace convolution factorization is exact; the smoothing bump for the biorthogonals is nonnegative and nonzero, so its Laplace values are strictly positive. |
| Reverse/shift might cost an uncontrolled factor \(e^{\ell b_n}\) | VERIFIED UNDER EXPLICIT ASSUMPTIONS | The source's \(e^{-\ell b_n}\) L² estimate cancels it exactly; the remaining shift/smoothing exponent is \(a+\epsilon<T-\eta\). |
| C∞ convergence might fail despite L² convergence | VERIFIED UNDER EXPLICIT ASSUMPTIONS | A common compact support and explicit C^j series majorant work for each j. |
| R may not land in the strong weighted sequence space | VERIFIED UNDER EXPLICIT ASSUMPTIONS | Each coordinate is bounded by \(C e^{-Tb_n}\); weighted squared norms are bounded by a summable \(e^{-2\eta b_n}\) series. |
| Fredholm only yields closure of range | VERIFIED | Riesz–Schauder gives closed range, and hence exact \(\operatorname{ran}A=(\ker A^*)^\perp\). |
| A might not be invertible | VERIFIED | It need not be; the proof chooses seeds in its finite-codimension actual range and uses the inverse only on \((\ker A)^\perp\). |
| Endpoint evaluation is not bounded in H | VERIFIED | General H evaluation is indeed unbounded; the corrected endpoint map on interior-supported X is the bounded smoothing functional \(-TQx(T)\). |
| Infinite-kernel result may contradict dense range or analytic-control uniqueness | VERIFIED | Dense range concerns \(\ker B^*\), not \(\ker B\); constructed f is nonanalytic on the entire interval even though analytic near endpoints. |
| Modal scaling or the sign of the coupled tail may differ | VERIFIED UNDER EXPLICIT ASSUMPTIONS | Independently derived from the specified modal ODE and boundary convention; factor \(C_nb_n/(b_n+\delta_n)\), plus tail and \(d/b_n^2\) are accounted for. |
| \(b_n\asymp n^2\) alone might not give the root gap | VERIFIED | Correct: it does not. The frozen theorem includes a separate square-root gap; the physical root formula supplies it. |
| Smooth boundary data automatically validate every physical claim | NOT VERIFIED | Only the stated frozen linear odd PDE with smooth compatible boundary lift was analyzed. Nonlinear preparation and original full-system reachability are separate. |
| A separate mathematician or AI has certified the proof | NOT VERIFIED | No independent reviewer has examined it. |
| The cited external theorem's published proof has been independently certified | NOT VERIFIED | The exact theorem statement and assumptions were inspected and applied, not reproved or externally certified. |
| Original Ivanov–Pandolfi priority comparison | NOT VERIFIED | The original proof was not accessible; no priority or novelty claim. |

No counterexample to the stated operator theorem was found in these attempts. The conclusion is a same-agent mathematical verification *conditional on the stated external results*, not proof by computation or independent certification. Before relying on the PDE interpretation, an external expert should check the exact frozen PDE coefficients, regularity/solution theory and the sign convention in the original model, as well as the biorthogonal source and infinite-dimensional construction.
