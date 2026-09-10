# Preface

The **FEBio User Manual** is the practical guide to running FEBio: how to invoke it from the command
line, how the free-format XML input file is structured, and how to set up multi-step analyses, restarts,
parameter optimization, plugins, and configuration. It also documents FEBio's output — the binary plot
database and the log/data records — in its appendices.

It sits between the other manuals: [Theory](../theory/index.md) explains the mathematics behind the
models, [Features](../features/index.md) is the per-feature parameter reference, and this manual covers
how you actually drive the solver.

Use the **User** tab above to browse by chapter and section.

## About this conversion

- **Source** — `source/FEBio_User_Manual.lyx`, vendored from
  [febiosoftware/FEBio](https://github.com/febiosoftware/FEBio)'s `Documentation/` directory. Note this
  is a stripped-down cut of the upstream manual rather than the complete document.
- **Converter** — `tools/lyx2md.py`, the same deterministic, stdlib-only LyX parser used for the Theory
  and Studio manuals. All 14 chapters are converted (Chapters 1–9 plus Appendices A–E).
- **Bibliography** — `source/FEBio3.bib`. The vendored cut carries 12 citations but lost the upstream
  document's own `bibfiles` pointer; `FEBio3.bib` is the database upstream names, and every cited key
  resolves in it. Citations render as per-page footnotes.
- **Equations** — rendered with MathJax. The manual's six `\newcommand` operator macros (`\tr`, `\dev`,
  `\Dev`, `\grad`, `\divg`, `\Ei`) are declared globally in `docs/js/mathjax_config.js`.
- **Figures** — not part of the LyX source; fetched at build time from the FEBio repository's
  `Documentation/Figures/` directory by `build.py`.

See [`CONVERSION_NOTES_USER.md`](https://github.com/febiosoftware/febio-docs/blob/main/CONVERSION_NOTES_USER.md)
for the per-chapter breakdown and everything flagged for manual review.
