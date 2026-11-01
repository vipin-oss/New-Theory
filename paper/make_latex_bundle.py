#!/usr/bin/env python3
"""Build the independent Overleaf source archive with stable ordering and metadata."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

paper = Path(__file__).resolve().parent
root = paper / "latex"
names = ["README.md", "main.tex", "references.bib"] + [
    "sections/abstract.tex", "sections/introduction.tex",
    "sections/mathematical_formulation.tex", "sections/main_theorem.tex",
    "sections/proof.tex", "sections/linear_model_interpretation.tex",
    "sections/consequences_and_limitations.tex",
]
with ZipFile(paper / "exact-smooth-kernel-latex.zip", "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for name in sorted(names):
        info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        archive.writestr(info, (root / name).read_bytes(), compresslevel=9)
