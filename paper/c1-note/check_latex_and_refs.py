#!/usr/bin/env python3
"""
Static LaTeX & Bibliography Verification Script for paper/c1-note/
Since no TeX compiler (pdflatex/xelatex/lualatex/tectonic) is installed in the sandbox,
this script rigorously verifies:
  1. All \\input{...} files exist.
  2. All \\begin{...} / \\end{...} environments and curly braces {...} are balanced.
  3. All \\label{...} keys are unique, and all \\ref{...} / \\eqref{...} keys resolve.
  4. All \\cite{...} keys exist in references.bib.
  5. Zero unverified sources from unverified.md are cited via \\cite{...}.
  6. Estimates total page count for 11pt article class (1-inch margins).
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent


def check_brace_balance(text: str, filename: str) -> list[str]:
    errors = []
    # Strip comments
    lines = [re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines()]
    clean = "\n".join(lines)

    depth = 0
    for line_no, line in enumerate(lines, 1):
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "\\" and i + 1 < len(line):
                i += 2
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth < 0:
                    errors.append(f"{filename}:{line_no}: Unmatched closing brace '}}'")
                    depth = 0
            i += 1
    if depth != 0:
        errors.append(f"{filename}: End of file has unclosed braces (depth={depth})")

    # Check \begin{env} / \end{env} stack
    env_stack = []
    env_pattern = re.compile(r"\\(begin|end)\{([^}]+)\}")
    for line_no, line in enumerate(lines, 1):
        for m in env_pattern.finditer(line):
            kind, env = m.group(1), m.group(2)
            if kind == "begin":
                env_stack.append((env, line_no))
            else:
                if not env_stack:
                    errors.append(f"{filename}:{line_no}: Unmatched \\end{{{env}}}")
                else:
                    top_env, start_line = env_stack.pop()
                    if top_env != env:
                        errors.append(
                            f"{filename}:{line_no}: Mismatched \\end{{{env}}} for \\begin{{{top_env}}} at line {start_line}"
                        )
    for env, start_line in env_stack:
        errors.append(f"{filename}:{start_line}: Unclosed \\begin{{{env}}}")

    return errors


def main() -> int:
    tex_files = [ROOT / "main.tex"] + sorted((ROOT / "sections").glob("*.tex")) + [
        ROOT / "hand_check_theorem1.tex"
    ]

    errors = []
    for tf in tex_files:
        if not tf.exists():
            errors.append(f"Missing TeX file: {tf}")
            continue
        errors.extend(check_brace_balance(tf.read_text(encoding="utf-8"), tf.name))

    # Assemble full document text from main.tex + \input files
    main_text = (ROOT / "main.tex").read_text(encoding="utf-8")
    input_pattern = re.compile(r"\\input\{([^}]+)\}")

    full_doc_parts = []
    for line in main_text.splitlines():
        clean_line = re.sub(r"(?<!\\)%.*$", "", line)
        m = input_pattern.search(clean_line)
        if m:
            inc_rel = m.group(1)
            if not inc_rel.endswith(".tex"):
                inc_rel += ".tex"
            inc_path = ROOT / inc_rel
            if not inc_path.exists():
                errors.append(f"Missing \\input file: {inc_rel}")
            else:
                full_doc_parts.append(inc_path.read_text(encoding="utf-8"))
        else:
            full_doc_parts.append(line)

    full_doc = "\n".join(full_doc_parts)
    full_doc_no_comments = "\n".join(
        re.sub(r"(?<!\\)%.*$", "", line) for line in full_doc.splitlines()
    )

    # Check labels and refs in full_doc
    labels = re.findall(r"\\label\{([^}]+)\}", full_doc_no_comments)
    seen_labels = set()
    for lbl in labels:
        if lbl in seen_labels:
            errors.append(f"Duplicate \\label{{{lbl}}} in main document")
        seen_labels.add(lbl)

    refs = re.findall(r"\\(?:eq)?ref\{([^}]+)\}", full_doc_no_comments)
    for r in refs:
        for key in r.split(","):
            key = key.strip()
            if key not in seen_labels:
                errors.append(f"Unresolved \\ref or \\eqref key: {key}")

    # Check citations against references.bib
    bib_text = (ROOT / "references.bib").read_text(encoding="utf-8")
    bib_keys = set(re.findall(r"@\w+\{\s*([^,\s]+)\s*,", bib_text))

    cites_raw = re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", full_doc_no_comments)
    cited_keys = set()
    for c in cites_raw:
        for k in c.split(","):
            k = k.strip()
            if k:
                cited_keys.add(k)
                if k not in bib_keys:
                    errors.append(f"Cited key '{k}' not found in references.bib")

    # Check that no unverified author-year key from unverified.md is cited
    unverified_forbidden = {
        "EdelenLaws1971",
        "EringenEdelen1972",
        "Eringen1972Nonlocal",
        "Eringen1983",
        "Eringen1987",
        "Eringen1992",
        "Polizzotto2001",
        "Borino2003",
        "BorinoFaillaParrinello2003",
        "Polizzotto2014",
        "ChallamelWang2008",
        "Koutsoumaris2017",
        "twophase2024",
        "Ebrahimi2016",
        "Yu2016",
    }
    bad_cited = cited_keys.intersection(unverified_forbidden)
    if bad_cited:
        errors.append(f"Forbidden unverified keys cited: {sorted(bad_cited)}")

    # Count prose words (excluding displayed math/tables), equations, tables, and estimate page length
    doc_no_display = re.sub(
        r"\\begin\{(equation|align|table)\}.*?\\end\{\1\}",
        " ",
        full_doc_no_comments,
        flags=re.S,
    )
    doc_no_inline_math = re.sub(r"\$[^$]+\$", " MATH ", doc_no_display)
    plain_words = re.sub(
        r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", doc_no_inline_math
    )
    word_count = len(plain_words.split())
    numbered_eqs = len(
        re.findall(r"\\begin\{(equation|align)\}", full_doc_no_comments)
    )
    tables = len(re.findall(r"\\begin\{table\}", full_doc_no_comments))

    # Standard 11pt a4paper article with 1in margins fits ~600 prose words/page;
    # each displayed equation block takes ~0.04 pages, each table ~0.4 pages, plus ~1.2 pages for bibliography
    est_pages = (
        (word_count / 600.0)
        + (0.04 * numbered_eqs)
        + (0.40 * tables)
        + (0.048 * len(cited_keys))
    )

    print("=== LaTeX & Bibliography Verification Summary ===")
    print(f"TeX files checked       : {len(tex_files)}")
    print(f"Unique \\label{{...}} keys : {len(seen_labels)}")
    print(f"Total \\ref/\\eqref calls : {len(refs)}")
    print(f"BibTeX entries in .bib  : {len(bib_keys)}")
    print(f"Unique cited BibTeX keys: {len(cited_keys)}")
    print(f"Unverified keys cited   : {len(bad_cited)}")
    print(f"Approximate word count  : {word_count}")
    print(f"Displayed eq blocks     : {numbered_eqs}")
    print(f"Tables                  : {tables}")
    print(f"Estimated page count    : {est_pages:.1f} pages (target: 10-14 pages)")

    if errors:
        print("\nERRORS FOUND:")
        for e in errors:
            print("  -", e)
        return 1

    print("\nALL CHECKS PASSED (0 errors).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
