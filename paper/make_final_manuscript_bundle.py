#!/usr/bin/env python3
"""Rebuild a deterministic, self-contained final-manuscript source ZIP."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

paper = Path(__file__).resolve().parent
root = paper / "final-manuscript"
files = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix not in {".pdf", ".aux", ".log", ".bbl", ".blg"})
with ZipFile(paper / "final-manuscript-overleaf.zip", "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for path in files:
        info = ZipInfo(path.relative_to(root).as_posix(), (1980, 1, 1, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes(), compresslevel=9)
