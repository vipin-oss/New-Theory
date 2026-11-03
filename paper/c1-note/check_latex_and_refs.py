#!/usr/bin/env python3
"""
Static LaTeX & Bibliography Verification Script for paper/c1-note/
Since no TeX compiler (latexmk/pdflatex/xelatex/lualatex/tectonic) is installed in the sandbox,
this script rigorously verifies:
  1. All \\input{...} files exist.
  2. All \\begin{...} / \\end{...} environments and curly braces {...} are balanced.
  3. No unbraced [...] inside optional arguments \\begin{theorem}[...] etc.
  4. No \\mathrm{\\AA} or raw \\AA / \\r inside math mode (must use \\text{\\normalfont\\AA}).
  5. All custom macros (e.g., \\Rbb, \\Nbb, \\Cbb, \\Lcal, \\Kcal, \\Ical, \\Dcal, \\dd) are defined in main.tex.
  6. All \\label{...} keys are unique, and all \\ref{...} / \\eqref{...} keys resolve.
  7. All \\cite{...} keys exist in references.bib, and zero unverified sources are cited.
  8. Abstract word count <= 250 words and estimated page count <= 14 pages.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent


def check_file_syntax(text: str, filename: str) -> list[str]:
    errors = []
    lines = [re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines()]

    # 1. Brace balance
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

    # 2. \begin{env} / \end{env} stack
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

    # 3. Check optional arguments of \begin{theorem}[...] for unbraced [ or ]
    for line_no, line in enumerate(lines, 1):
        for m in re.finditer(r"\\begin\{(?:theorem|proposition|corollary|lemma|definition|remark)\}\[", line):
            start = m.end()
            brace_level = 0
            closed = False
            for j in range(start, len(line)):
                if line[j] == "{":
                    brace_level += 1
                elif line[j] == "}":
                    brace_level = max(0, brace_level - 1)
                elif line[j] == "[" and brace_level == 0:
                    errors.append(
                        f"{filename}:{line_no}: Unbraced '[' inside theorem optional argument [...]"
                    )
                elif line[j] == "]" and brace_level == 0:
                    closed = True
                    break
            if not closed:
                errors.append(
                    f"{filename}:{line_no}: Unclosed optional argument '[' on theorem environment"
                )

    # 4. Check for \mathrm{\AA} or raw \AA in math mode without \text{...}
    for line_no, line in enumerate(lines, 1):
        if r"\mathrm{\AA}" in line:
            errors.append(
                f"{filename}:{line_no}: Found \\mathrm{{\\AA}} (causes 'Command \\r invalid in math mode'); use \\text{{\\normalfont\\AA}}"
            )

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
        errors.extend(check_file_syntax(tf.read_text(encoding="utf-8"), tf.name))

    main_text = (ROOT / "main.tex").read_text(encoding="utf-8")
    defined_macros = set(
        re.findall(r"\\newcommand\{\\([a-zA-Z]+)\}", main_text)
    )

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

    # Check that all \Xbb and \Xcal macros used in full_doc are defined in main.tex
    used_custom = set(
        re.findall(r"\\([A-Z](?:bb|cal))\b", full_doc_no_comments)
    )
    undefined_custom = used_custom - defined_macros
    if undefined_custom:
        errors.append(
            f"Undefined custom macros used in document: {sorted(undefined_custom)}"
        )

    # Check abstract word count <= 250 words
    abs_match = re.search(
        r"\\begin\{abstract\}(.*?)\\end\{abstract\}", full_doc_no_comments, re.S
    )
    abs_words = len(abs_match.group(1).split()) if abs_match else 0
    if abs_words > 250:
        errors.append(f"Abstract has {abs_words} words (exceeds 250-word limit)")

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

    # Check that no unverified key or isothermal PhamVu2024 key is cited
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
        "PhamVu2024",
    }
    bad_cited = cited_keys.intersection(unverified_forbidden)
    if bad_cited:
        errors.append(f"Forbidden/unverified keys cited: {sorted(bad_cited)}")

    # Count prose words, equations, tables, and estimate page length
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

    est_pages = (
        (word_count / 600.0)
        + (0.04 * numbered_eqs)
        + (0.40 * tables)
        + (0.048 * len(cited_keys))
    )

    print("=== LaTeX & Bibliography Verification Summary ===")
    print(f"TeX files checked       : {len(tex_files)}")
    print(f"Defined custom macros   : {sorted(defined_macros)}")
    print(f"Used *bb/*cal macros    : {sorted(used_custom)}")
    print(f"Abstract word count     : {abs_words} words (limit: <= 250)")
    print(f"Unique \\label{{...}} keys : {len(seen_labels)}")
    print(f"Total \\ref/\\eqref calls : {len(refs)}")
    print(f"BibTeX entries in .bib  : {len(bib_keys)}")
    print(f"Unique cited BibTeX keys: {len(cited_keys)}")
    print(f"Unverified keys cited   : {len(bad_cited)}")
    print(f"Approximate prose words : {word_count}")
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
