#!/usr/bin/env python3
"""
build.py -- Build script for the FEBio Manuals site (Theory Manual + Studio
Manual).

Mirrors the style of febio-feature-manual/build.py:
  1. Runs the LyX -> Markdown converter (tools/lyx2md.py) once per manual in
     MANUALS below, to (re)generate that manual's docs/<nav_root>/chapterN/*.md
     from its own vendored .lyx source, for whichever chapters that manual's
     "chapters" entry includes. Each run is a separate subprocess, so
     tools/lyx2md.py's module-level globals/label-registries never
     cross-contaminate between manuals.
  2. Writes mkdocs.yml with the same Material theme / markdown_extensions
     conventions as febio-feature-manual (indigo palette, the FEBio logo
     -- docs/febio.png, vendored from febio-feature-manual's own docs/
     directory -- in place of Material's default logo, arithmatex
     generic + MathJax via docs/js/mathjax_config.js + jsdelivr
     tex-mml-chtml, admonition, footnotes, toc permalink,
     pymdownx.blocks.caption, superfences, details), plus attr_list
     (needed so that the converter's explicit heading anchors --
     `## Title {: #label }`, produced from LyX \\label insets -- work for
     cross-chapter/cross-section \\ref links) and md_in_html (needed so a
     `<div markdown="1">` wrapper -- render_tabular()'s only way to center
     a table, since a Markdown table has no native alignment syntax and
     attr_list doesn't attach to one -- has its nested Markdown table
     syntax actually parsed, instead of passed through as literal text).

Navigation uses navigation.tabs: each entry in MANUALS becomes exactly one
top-level nav key (rendered as a tab), containing a Preface page plus one
nav group per converted chapter, each expanding to that chapter's sections
-- the same mechanism febio-feature-manual uses to render its own 5 tabs
from 5 top-level nav keys.

Usage:
    python3 build.py [-v|--verbose]
"""
import glob
import json
import re
import subprocess
import sys
import os
import urllib.parse as _urlparse
import urllib.request as _url

ROOT = os.path.dirname(os.path.abspath(__file__))

args = sys.argv[1:]
verbose = "-v" in args or "--verbose" in args

# ---------------------------------------------------------------------
# Manual configuration: one entry per manual converted into this site.
# ---------------------------------------------------------------------
MANUALS = [
    {
        "key": "theory",
        "nav_label": "Theory",
        "kind": "lyx",
        "lyx": os.path.join(ROOT, "source", "FEBio_Theory_Manual.lyx"),
        "bib": os.path.join(ROOT, "source", "FEBio3.bib"),
        "docs_root": os.path.join(ROOT, "docs", "theory"),
        "nav_root": "theory",
        "stats_file": os.path.join(ROOT, "tools", "_stats.json"),
        "chapters": "all",
        "fig_base": "https://raw.githubusercontent.com/febiosoftware/FEBio/master/Documentation/Figures/",
    },
    {
        "key": "studio",
        "nav_label": "Studio",
        "kind": "lyx",
        "lyx": os.path.join(ROOT, "source", "FEBioStudio_User_Manual.lyx"),
        "bib": os.path.join(ROOT, "source", "FEBioStudio.bib"),
        "docs_root": os.path.join(ROOT, "docs", "studio"),
        "nav_root": "studio",
        "stats_file": os.path.join(ROOT, "tools", "_stats_studio.json"),
        # Widened from a "1,2"-only pilot to the full manual once
        # tools/lyx2md.py's support for this manual's LyX constructs (e.g.
        # Wrap-figure insets, native href insets, Description/LyX-Code
        # layouts) was validated against real content -- see
        # CONVERSION_NOTES_STUDIO.md.
        "chapters": "all",
        "fig_base": "https://raw.githubusercontent.com/febiosoftware/FEBioStudio/master/Documentation/Figures/",
    },
    {
        # Unlike the other two, this manual has no LyX source: it is generated
        # from FEBio's exported feature database plus hand-authored per-feature
        # prose fragments, by tools/features2md.py (a port of the standalone
        # febio-feature-manual repo's build.py). Its figures are vendored, not
        # fetched, so it is skipped by step 4.
        "key": "features",
        "nav_label": "Features",
        "kind": "features",
        "features_json": os.path.join(ROOT, "source", "feature-manual", "febio_features.json"),
        "meta_dir": os.path.join(ROOT, "source", "feature-manual", "meta"),
        "docs_root": os.path.join(ROOT, "docs", "features"),
        "nav_root": "features",
        "stats_file": os.path.join(ROOT, "tools", "_stats_features.json"),
    },
]

def write_nav(f, items, indent):
    """Emit a nested mkdocs nav tree.

    Each item is [title, target]; a string target is a leaf page, a list
    target is a nested section. Titles are JSON-quoted so names carrying
    YAML-significant characters can't corrupt the file.
    """
    for title, target in items:
        if isinstance(target, str):
            f.write(f"{indent}- {json.dumps(title)}: {target}\n")
        else:
            f.write(f"{indent}- {json.dumps(title)}:\n")
            write_nav(f, target, indent + "  ")


print("Building FEBio Manuals site...")

# ---------------------------------------------------------------------
# Step 1: run the appropriate source -> Markdown converter, once per manual
# ---------------------------------------------------------------------
manual_stats = {}
for manual in MANUALS:
    if manual["kind"] == "features":
        script = os.path.join(ROOT, "tools", "features2md.py")
        cmd = [
            sys.executable, script,
            "--features-json", manual["features_json"],
            "--meta-dir", manual["meta_dir"],
            "--docs-root", manual["docs_root"],
            "--nav-root", manual["nav_root"],
            "--stats-out", manual["stats_file"],
        ]
        if verbose:
            cmd.append("--verbose")
    else:
        script = os.path.join(ROOT, "tools", "lyx2md.py")
        cmd = [
            sys.executable, script,
            "--lyx", manual["lyx"],
            "--bib", manual["bib"],
            "--docs-root", manual["docs_root"],
            "--nav-root", manual["nav_root"],
            "--stats-out", manual["stats_file"],
            "--chapters", manual["chapters"],
        ]

    if verbose:
        print(f"Running tools/{os.path.basename(script)} for '{manual['key']}' ...")

    result = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=not verbose,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: {os.path.basename(script)} failed for '{manual['key']}'")
        if not verbose:
            print(result.stdout)
            print(result.stderr)
        sys.exit(1)
    elif not verbose:
        print(result.stdout.strip())

    # -------------------------------------------------------------
    # Step 2: load this manual's conversion stats (per-chapter nav entries)
    # -------------------------------------------------------------
    with open(manual["stats_file"], "r", encoding="utf-8") as f:
        manual_stats[manual["key"]] = json.load(f)

# ---------------------------------------------------------------------
# Step 3: write mkdocs.yml
# ---------------------------------------------------------------------
if verbose:
    print("Writing mkdocs.yml...")

with open(os.path.join(ROOT, "mkdocs.yml"), mode="w", encoding="utf-8") as f:
    f.write('site_name: "FEBio Manuals"\n')
    f.write("site_description: Theoretical background and user documentation for FEBio and FEBio Studio.\n")
    f.write("site_author: FEBio Team\n")
    f.write("theme:\n")
    f.write("  name: material\n")
    f.write("  logo: febio.png\n")
    f.write("  palette:\n")
    f.write("    primary: indigo\n")
    f.write("    accent: indigo\n")
    f.write("  font:\n")
    f.write("    text: 'Roboto'\n")
    f.write("    code: 'Roboto Mono'\n")
    f.write("  features:\n")
    f.write("    - navigation.tabs\n")
    f.write("    - navigation.top\n")
    f.write("    - navigation.footer\n")
    f.write("    - search.highlight\n")
    f.write("    - search.suggest\n")
    f.write("    - toc.integrate\n")
    f.write("    - content.external.links\n")
    f.write("markdown_extensions:\n")
    f.write("  - admonition\n")
    f.write("  - attr_list\n")
    f.write("  - md_in_html\n")
    f.write("  - codehilite\n")
    f.write("  - footnotes\n")
    f.write("  - toc:\n")
    f.write("      permalink: true\n")
    f.write("  - pymdownx.arithmatex:\n")
    f.write("      generic: true\n")
    f.write("  - pymdownx.superfences\n")
    f.write("  - pymdownx.blocks.caption\n")
    f.write("  - pymdownx.details\n")
    f.write("extra_javascript:\n")
    f.write("  - js/mathjax_config.js\n")
    f.write("  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\n")
    f.write("nav:\n")
    for manual in MANUALS:
        stats = manual_stats[manual["key"]]
        f.write(f"  - {manual['nav_label']}:\n")
        f.write(f"    - Preface: {manual['nav_root']}/index.md\n")

        if manual["kind"] == "features":
            # Arbitrarily nested nav tree (sections within sections) rather
            # than the LyX manuals' fixed chapter/section shape.
            write_nav(f, stats["nav"], "    ")
        else:
            for chap in stats["chapters"]:
                kind = "Appendix" if chap.get("is_appendix") else "Chapter"
                f.write(f"    - {kind} {chap['chap_display']} - {chap['title']}:\n")
                for title, path in chap["nav"]:
                    f.write(f"      - {title}: {path}\n")

for manual in MANUALS:
    if manual["kind"] == "features":
        t = manual_stats[manual["key"]]["totals"]
        print(f"  {manual['key']}: wrote nav for {t['categories']} categories, "
              f"{t['features']} feature pages, {t['modules']} module pages.")
        continue
    chapters = manual_stats[manual["key"]]["chapters"]
    total_sections = sum(len(c["nav"]) for c in chapters)
    print(f"  {manual['key']}: wrote nav for {len(chapters)} chapters, {total_sections} section pages.")

# ---------------------------------------------------------------------
# Step 4: fetch any figure artwork that isn't already vendored in the
# repo, once per manual from that manual's own upstream Figures/ dir.
# Scans every converted chapter's generated Markdown for figure
# references (not hardcoded to a specific chapter's known figures), so
# this keeps working as more chapters get converted.
# ---------------------------------------------------------------------
_FIG_RE = re.compile(r"!\[[^\]]*\]\(figs/([^)]+?)\)")

for manual in MANUALS:
    # The Features manual's figures are vendored in source control, not
    # fetched from an upstream repo, and its pages don't live in chapter*/.
    if manual["kind"] != "lyx":
        continue
    for _md_path in glob.glob(os.path.join(manual["docs_root"], "chapter*", "*.md")):
        _chapter_dir = os.path.dirname(_md_path)
        _figs_dir = os.path.join(_chapter_dir, "figs")
        with open(_md_path, "r", encoding="utf-8") as _f:
            _text = _f.read()
        for _fig in _FIG_RE.findall(_text):
            os.makedirs(_figs_dir, exist_ok=True)
            _dest = os.path.join(_figs_dir, _fig)
            if os.path.exists(_dest) and os.path.getsize(_dest) > 2048:
                continue
            try:
                # Some Studio Manual figure filenames contain literal spaces
                # (e.g. "Model Viewer.png") -- urlretrieve rejects a raw
                # space in a URL outright ("URL can't contain control
                # characters"), so the figure name portion needs percent-
                # encoding even though the local path (_dest) doesn't.
                _url.urlretrieve(manual["fig_base"] + _urlparse.quote(_fig), _dest)
                print(f"  fetched figure ({manual['key']}): {_fig}")
            except Exception as _e:
                print(f"  WARNING: could not fetch {_fig} ({manual['key']}): {_e}")

print("Build complete.")
print()
print("Next steps:")
print("  pip install mkdocs mkdocs-material")
print("  mkdocs serve      # preview at http://127.0.0.1:8000")
print("  mkdocs build --strict")
