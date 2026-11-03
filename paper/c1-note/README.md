# Overleaf-Ready Clarification Note Package (`paper/c1-note/`)

**Title**: *Thermodynamic Consistency of Two-Phase Integral Nonlocal Thermoelasticity: Reciprocity, Boundary Closure, and Kernel Normalization*

**Document Type**: Focused 10–14 page foundational clarification note (`\documentclass[11pt,a4paper]{article}`, standard LaTeX packages only, no journal-specific template).

**Compiler Availability Note**: No TeX distribution (`latexmk`, `pdflatex`, `xelatex`, `lualatex`, `tectonic`, or `bibtex`) is installed in the execution sandbox (`NO_TEX_COMPILER`). Accordingly, we do **not** claim to have compiled `main.tex` to PDF inside the sandbox. Static syntax, brace/environment balance, theorem optional-argument brackets, math-mode `\AA`/`\r` checks, custom macro definitions (`\Rbb`, `\Nbb`, `\Cbb`, `\Lcal`, `\Kcal`, `\Ical`, `\Dcal`, `\dd`), `\label`/`\ref`/`\eqref` resolution, abstract word-count limit ($\le 250$ words), and primary-source BibTeX citation verification have been checked programmatically via `check_latex_and_refs.py` (0 errors across all 10 `.tex` files, 107 unique `\label` keys, 147 `\ref`/`\eqref` cross-references, and 24 full-text verified BibTeX keys).

---

## File Manifest

- `main.tex`: Master Overleaf LaTeX file (`\documentclass[11pt,a4paper]{article}`). To compile on Overleaf or any local TeX Live / MiKTeX installation, run `latexmk -pdf main.tex` (or `pdflatex main && bibtex main && pdflatex main && pdflatex main`).
- `sections/`:
  - `sec1_introduction.tex`: Section 1 — Introduction, detailed prior-art credits (Edelen–Laws, Eringen 1974, Polizzotto, Borino–Failla–Parrinello, Challamel–Wang, Fernández-Sáez et al., Romano et al., Mikhasev–Nobili, Nobili–Pramanik, Giorgi–Morro), and factual description of the $N=29$ surveyed spatial-nonlocal thermoelasticity papers (including explicit derivation of the Class II momentum equation $E u_{xx} - \beta\theta_x = (1-\ell^2\partial_x^2)\rho\ddot{u}$ where nonlocality remains on the inertia term, versus the bulk heat equation where the identical $\gamma=0$ operator on $\rho\eta$ and $q$ cancels).
  - `sec2_model.tex`: Section 2 — Two-phase integral operator $\mathcal{L}_{\gamma,\ell}$ on $L^2(\Omega)$, global Clausius–Duhem inequality, operator reciprocity $\mathcal{L}_\eta = \mathcal{L}_{\text{th}}^*$, and the two minimal consistent realizations Variant V1 and Variant V2 (with explicit note that V1/V2 labels follow Round 2 and are swapped relative to Round 1).
  - `sec3_theorem1.tex`: Section 3 — Theorem 1 (non-existence of Helmholtz or Gibbs free energy for stress-nonlocal + local-heating pairing) and the explicit one-page hand-checkable Maxwell-symmetry and closed-cycle calculation.
  - `sec4_mode_count.tex`: Section 4 — Theorem 2 (spatial mode count $N=4$ for Variant V1 vs. $N=3$ for Variant V2 and $N=2$ for $\gamma=0$ Class I/II, singular perturbation $q_4(\omega;\gamma) = -(\gamma\ell^2)^{-1} + O(1)$ as $\gamma \to 0^+$, and asymptotic damping).
  - `sec5_boundary_closure.tex`: Section 5 — Theorem 3 (exact differential equivalence and Constitutive Boundary Conditions under unnormalized $K_\ell^{\text{unnorm}}$, BFP-normalized $W_\ell^{\text{BFP}}$, and Neumann $K_\ell^{\text{Neu}}$ kernels) and Corollary 1 proving that the static $1/\sqrt{\gamma}$ surface thermal-strain layer is a kernel-truncation artifact.
  - `sec6_calibration.tex`: Section 6 — Calibrated magnitude estimate for fcc Aluminum at $300\text{ K}$ using the atomistic 2NN MEAM characteristic length $\bar{\ell}_1 = 0.120272\text{ nm}$ (Lazar, Agiasofitou & Böhlke 2022), showing that relative attenuation differences between V1, V2, and Class I/II are $O(10^{-4})$ or smaller across the Fourier-valid regime.
  - `sec7_limitations.tex`: Section 7 — Explicit limitations and summary of practical guidelines.
  - `appendix_proofs.tex`: Appendix A — Complete mathematical proofs of Proposition 1, Theorem 1, Theorem 2, Theorem 3, and Corollary 1.
- `references.bib`: BibTeX database containing 24 primary-source full-text verified entries.
- `unverified.md`: Separate documentation of 15 unread/paywalled primary sources excluded from `references.bib` and not cited in the text.
- `HAND_CHECK_THEOREM1.md` and `hand_check_theorem1.tex`: Standalone one-page hand-check sheet for Theorem 1 (Helmholtz Maxwell defect, Gibbs stress-gradient entropy check, and closed-cycle negative dissipation).
- `REFEREE_PACKAGE.md`: Referee package listing each external mathematical and continuum-mechanics theorem used in the note with its exact hypotheses and verification.
- `check_latex_and_refs.py`: Automated verification script for LaTeX structure, cross-references, macros, and primary-source citation rules.
- `c1-note.zip`: Self-contained Overleaf-ready archive of `paper/c1-note/`.
