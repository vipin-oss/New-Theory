# Overleaf source project

This is a typesetting conversion of `paper/EXACT_SMOOTH_KERNEL_MANUSCRIPT.md` at commit `82827b3a36afbcc485da296ca86ae787fa51f48e`. The seven files in `sections/` are included by `main.tex`; `references.bib` supplies all five references. Authorship is intentionally unspecified, pending the principal researcher's decision.

## Overleaf

Upload `exact-smooth-kernel-latex.zip` as a new project, set `main.tex` as the main document and select **pdfLaTeX**. Overleaf normally runs BibTeX and repeated LaTeX passes automatically. If references remain unresolved, recompile from scratch. Check the resulting log and PDF before use.

## Local build

A current TeX Live installation with the packages in `main.tex` and BibTeX is required. From this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively use `latexmk -pdf main.tex`. These are instructions, not a claim that a build was completed here. The accompanying quality report documents the build limitation. This is a candidate manuscript awaiting independent review; mathematical novelty and nonlinear physical preparation are not established.
