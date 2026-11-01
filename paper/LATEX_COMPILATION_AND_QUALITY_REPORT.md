# LaTeX compilation and quality report

## Status: source delivered; compilation and visual review outstanding

- **Source:** `paper/EXACT_SMOOTH_KERNEL_MANUSCRIPT.md` at `82827b3a36afbcc485da296ca86ae787fa51f48e`. The original manuscript was not edited.
- **Engine/result:** no local PDFLaTeX, latexmk, BibTeX or Tectonic executable was available. A Tectonic release download failed at GitHub's release-assets host; Debian package index retrieval failed due to network restrictions. The npm `texlive` package was examined as an alternative but is an older browser/JavaScript engine with an incomplete bundled package set and was not established as a suitable multi-file BibTeX build environment. **No manuscript compilation was run, no PDF was produced, and Overleaf compilation has not been verified.**
- **Page count:** unavailable. **Numbered displayed equations:** 24 in both manuscript and LaTeX source. **Bibliography:** five source entries and five cited keys; rendered bibliography and ordering not verified.
- **Compiler warnings/errors:** unavailable because there was no build. In particular, undefined-reference/citation warnings, overfull/underfull boxes, page breaks, PDF font embedding, alignment and hyperlink behavior have not been assessed. Source formatting is not a substitute for visual inspection. Check these after the first complete PDFLaTeX/BibTeX build on Overleaf.

## Source quality checks

The A4 11-point article uses Latin Modern, one-inch margins, AMS environments, mathtools, mathrsfs, bm, microtype, hyperref, cleveref, enumitem and booktabs. The theorem, lemma, proposition, corollary, definition and remark environments are defined. Long paired equations have been split using `aligned`; line fitting remains unverified. All original displayed equation bodies were compared mechanically with their LaTeX versions after removing whitespace, layout spacing and inserted alignment breaks: all 24 match. All 97 inline math expressions in the Markdown occur in the source, with three additional inline expressions used to convert Markdown's Unicode mathematical text. A static scan found 31 distinct labels, no duplicate labels and no missing cross-reference targets; the five citation keys match the bibliography. These checks cannot validate TeX compilation or mathematical correctness.

The main theorem, strict positivity and increase, asymptotic order and **separate** square-root gap, dependent tail, endpoint representative, Fredholm argument, complete proof and conditional linear-model interpretation are retained. Candidate status, same-agent review, inaccessible Ivanov–Pandolfi proof, unverified novelty, and the absence of a nonlinear preparation or full-system inverse result remain explicit. Reference metadata follows the five entries and prior source checks in `paper/REFERENCE_VERIFICATION.md`; unavailable author/year information in the NYU notes is not invented. The citation of Ivanov–Pandolfi remains a limited indirect discussion, not a sixth verified bibliography entry.

No mathematical inconsistency was identified by the conversion checks, which do not constitute an independent proof audit. The source's authorship is unspecified; the LaTeX title block therefore leaves the author blank for the principal researcher to determine. Bibliographic citations and equation references were converted to keys/labels; additional layout changes do not intentionally alter the mathematics. Independent expert review and a literature/priority assessment are still needed.

## Archive verification and reproducibility

`paper/exact-smooth-kernel-latex.zip` contains ten files at its root: `main.tex`, `references.bib`, `README.md` and seven section files. It needs no repository-relative inputs. `python paper/make_latex_bundle.py` rebuilds it using sorted paths and fixed ZIP metadata. Two successive builds were byte-identical; a separate temporary extraction passed CRC checks and byte comparison against all ten source files. SHA-256: `fcd938a6cb7c9f08ded4f55df62c4ccc76963a087799c272d5cacee718ce307f`. Independent extraction was verified; an independent compilation was not possible here.

Next: upload the ZIP, compile with pdfLaTeX and BibTeX as described in its README, inspect the log and PDF, correct any layout or compilation issues without changing the mathematics, and obtain independent mathematical and physical-model review.
