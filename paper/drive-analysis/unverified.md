# Verification Status & Remaining Epistemic Boundaries (`unverified.md`)

## 1. Phase 1 Corpus & Review Coverage — 100% Complete (`0` Unread PDFs)

- **`Papers` folder (`papers_manifest.csv` & `paper_table.csv`):** **152 / 152 PDFs (`100% done`)**, `0 pending`, `0 text-extraction-failed`.
  - **138 PDFs** read via full-document PyMuPDF/Drive text extraction (covering title, abstract, introduction, constitutive/governing equations, geometry, solution method, main theorems/results, validation, stated limitations, and future work).
  - **8 scanned / image-only historical PDFs** read visually by rasterizing pages with PyMuPDF (`pymupdf` at 130–150 DPI) and inspecting the rendered images directly:
    1. `Unknown_e.pdf` — Barnett, Lothe, Gavazza & Musgrave (1985, *Proc. R. Soc. Lond. A* 402:153–166)
    2. `Stoneley_1924.pdf` — R. Stoneley (1924, *Proc. R. Soc. Lond. A* 106:416–428)
    3. `Lamb_1917.pdf` — Horace Lamb (1917, *Proc. R. Soc. Lond. A* 93:114–128) *(resolved prior `text-extraction-failed`)*
    4. `Green_1991.pdf` — A. E. Green & P. M. Naghdi (1991, *Proc. R. Soc. Lond. A* 432:171–194) *(resolved prior `text-extraction-failed`)*
    5. `Eringen_1966.pdf` — A. C. Eringen (1966, *J. Math. Mech.* 15:909–923)
    6. `SurfaceStressinSolids.pdf` — M. E. Gurtin & A. I. Murdoch (1978, *Int. J. Solids Struct.* 14:431–440)
    7. `ContinuumTheoryofElasticMaterialSurfacesARMA571975AddendumARMA591975.pdf` — M. E. Gurtin & A. I. Murdoch (1975, *Arch. Ration. Mech. Anal.* 57:291–323 & Addenda 59:389–390)
    8. `maxwell1867.pdf` — J. Clerk Maxwell (1867, *Phil. Trans. R. Soc. Lond.* 157:49–88)
  - **6 full-length monographs (261–484 pp.)** read systematically via PyMuPDF across frontmatter, complete table of contents, core constitutive/wave/boundary chapters, and closing chapters/index (including the 29.7 MB `nonlocal-continuum-field-theories-2004.pdf` and 30.2 MB `Unknown_10.1007@978-1-4612-2210-1.pdf` that exceeded the 25 MB Drive inline text-extraction limit).
- **Master review (`review paper.pdf`, `1SWgLp_NZehw4OeOi6LtkAT-ffF_4qQdA`):** All **157 pages** read section-by-section via PyMuPDF and mapped in [`review_map.md`](review_map.md).
- **Workspace hygiene:** All temporary downloaded PDFs and rasterized PNGs were deleted immediately after extraction (`0` binary PDFs in the repository or git history).

---

## 2. Explicit Epistemic Boundaries & Items Not Claimed as Certified

To maintain strict scientific honesty, the following boundaries remain:

1. **External 2020–2026 literature access depth:** Targeted web searches up to November 2026 were executed across Springer, ScienceDirect, Taylor & Francis, Wiley, Nature, Royal Society, and arXiv (`candidates.md` & `gap_map.md`). While publisher abstracts, metadata, reference lists, and open-access/preview equations were inspected for the closest 2023–2026 papers (including Anh & Vinh, *Arch. Appl. Mech.* 96:59, March 2026; Hue, Vinh & Anh, *ZAMP*, Jan 2026; Russillo et al., *Continuum Mech. Thermodyn.*, Aug 2024; Almuneef et al., *Arch. Appl. Mech.* 96:84, April 2026), subscription-paywalled full texts outside the Drive folder could not be downloaded into the sandbox. Therefore, external novelty is established to the standard of a thorough targeted literature screen, not an exhaustive legal priority guarantee.
2. **Master review publication metadata:** `review paper.pdf` carries author Vipin Gupta (Gurugram University) and date November 3, 2026, without a journal name or DOI. It is cited as an unpublished/working review manuscript in the user's Drive.
3. **Single-agent verification vs. independent human peer review:** Although `pilot/pilot.py` and `pilot/test_pilot.py` use **two mathematically independent numerical discretizations** (analytical 6-wave differential + Robin-CBC eigenmode solver vs. direct Legendre spectral-Galerkin Fredholm integral solver, agreeing to `4.75e-15`) plus SymPy symbolic verification, both implementations were written and executed in this session. Same-agent cross-method verification is strong internal verification, not a substitute for independent human expert refereeing.
4. **Experimental validation:** Candidate C1 resolves mathematical, thermodynamic, and boundary-value inconsistencies in nonlocal generalized thermoelasticity and quantifies their macroscopic/nanoscale signatures, but does not introduce new laboratory data.
5. **Minor missing DOI on one 2010 journal article:** Position 132 (`Propagation_of_SH_Waves_in_an_Irregular_Non_Homoge.pdf`, Chattopadhyay et al., *Applied Mathematical Sciences* 4(44):2157–2170, 2010) was published in a venue issue without a CrossRef DOI printed on the article; all bibliographic fields were verified directly from page 2 of the PDF.
