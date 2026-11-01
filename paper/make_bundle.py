"""Create the focused review bundle, preserving paths and deterministic metadata."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import hashlib

ROOT = Path(__file__).resolve().parent.parent
FILES = (
    'paper/EXACT_SMOOTH_KERNEL_MANUSCRIPT.md',
    'paper/INDEPENDENT_REFEREE_PACKAGE.md',
    'paper/REFERENCE_VERIFICATION.md',
    'research/exact-kernel-injectivity/FLAT_KERNEL_CONSTRUCTION_OR_NO_GO.md',
    'research/kernel-certification-dossier/BIORTHOGONAL_NORMALIZATION_CHECK.md',
    'research/kernel-certification-dossier/FREDHOLM_RANGE_AND_ENDPOINT_CHECK.md',
    'research/kernel-certification-dossier/EXACT_MODAL_RECONSTRUCTION_CHECK.md',
    'code/exact-kernel-injectivity/README.md',
    'code/exact-kernel-injectivity/test_structure.py',
)

def put(z, name, data):
    entry = ZipInfo(name, (2020, 1, 1, 0, 0, 0))
    entry.compress_type = ZIP_DEFLATED
    entry.external_attr = 0o100644 << 16
    z.writestr(entry, data)

def main():
    out = ROOT / 'paper' / 'exact-smooth-kernel-review-bundle.zip'
    rows = []
    with ZipFile(out, 'w') as z:
        for name in FILES:
            data = (ROOT / name).read_bytes()
            put(z, name, data)
            rows.append(f'{hashlib.sha256(data).hexdigest()}  {name}')
        intro = ('Frozen source theorem commit e1dfe145943b7c572c384442442517db6abf41f6.\n'
                 'No independent certification or priority claim.\n'
                 'Python test dependency: mpmath 1.3.0; run python code/exact-kernel-injectivity/test_structure.py.\n'
                 'The tests are diagnostics only and do not prove the theorem.\n\nSHA256\n' + '\n'.join(rows) + '\n')
        put(z, 'BUNDLE_README.txt', intro.encode())
    print(out)

if __name__ == '__main__':
    main()
