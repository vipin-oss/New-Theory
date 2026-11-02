# Candidate mathematical manuscript: Overleaf project

The project develops the frozen manuscript at commit `82827b3a36afbcc485da296ca86ae787fa51f48e`; it does not replace or modify that manuscript. Authorship and affiliation require confirmation. The paper and its proof remain subject to separate independent review; literature and priority have not been established.

Upload the complete project (or the accompanying `final-manuscript-overleaf.zip`) to Overleaf and select `main.tex` and pdfLaTeX. Locally, with a current TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively run `latexmk -pdf main.tex`. Compilation was not available in the development environment: neither this project nor its bibliography or references have been compiled or visually checked. There is no PDF and no known page count. After building, inspect the log for errors, missing citations/references, box warnings and PDF font embedding, and check equations, tables and page breaks visually. Then obtain independent mathematical, physical-model and bibliographic review. Detailed reports are in `../development/` in the repository; `FINAL_AUDIT_REPORT.md` summarizes the gates.
