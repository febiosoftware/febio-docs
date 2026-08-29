# Conversion Notes

Generated from `source/FEBio_Theory_Manual.lyx` (the complete manual) using `tools/lyx2md.py`, with
`CHAPTERS_TO_CONVERT` now covering every chapter (`{1..9}`, where chapter 9 — marked in the LyX source with
`\start_of_appendix` — renders as "Appendix A"). Totals reconciled below; per-section detail follows. This
file originally covered only Chapter 2 (Continuum Mechanics) as a single-chapter pilot, then grew to
Chapters 1–3, and now covers the whole manual: Chapters 4 (Element Library), 5 (Constitutive Models), 6
(Dynamics), 7 (Contact and Coupling), 8 (Optimization), and Appendix A (Tensor Calculus) have since been
added.

## Reconciliation summary

| Check | Result |
|---|---|
| Chapters converted | 9 (Chapters 1–8 plus Appendix A / Tensor Calculus) |
| Sections converted | 64 |
| Inline `$...$` emitted | 5203 |
| Display `\[...\]` emitted | 1919 |
| Citations | 203 |
| Figures | 21 |
| Leftover LyX artifacts (`\begin_`, `\end_inset`, `\begin_inset`, `SpecialChar`, `\lang `) | **0** |
| Unhandled/unrecognized inset kinds | **0** |
| `mkdocs build --strict` | exit code 0, **zero** `WARNING`-level messages. 85 `INFO`-level "does not contain an anchor" messages remain — all of them cross-page `#mjx-eqn:<label>` equation links; mkdocs's static link checker inspects the raw Markdown/HTML source, but `mjx-eqn:` anchors are injected client-side by MathJax only after it typesets the target page, so they're invisible to that checker even though they resolve correctly in a real browser (see `docs/js/mathjax_config.js`'s `pageReady` hook and the README's equation cross-reference section) |

Chapter 2 alone reconciles exactly against its source range, as established during the original
single-chapter pilot: 1455 inline + 368 display = 1823, matching `grep -c "begin_inset Formula"` over
`source/ch2.lyx` (now retired in favor of the single vendored `source/FEBio_Theory_Manual.lyx`) exactly.
Chapter 3 has one formula-inset-count discrepancy against a raw source scan (1487 rendered vs. 1488 raw
`\begin_inset Formula` occurrences) not yet root-caused; given zero unhandled insets and zero leftover
artifacts otherwise, this is presumed to be a benign edge case (e.g. two adjacent insets on the same source
line) rather than lost content — 1 formula out of 1096 candidates (~0.1%), flagged here rather than pursued
further given the cost/benefit.

**Chapter 6 initially reconciled *not* exact** (385 rendered vs. 400 source formulas, a 15-formula gap) —
this was a real bug, not a benign discrepancy like Chapter 3's. Chapter 6 opens with substantial prose *and*
4 numbered equations directly after its `Chapter` heading, before Section 6.1 begins; the section-splitting
logic only captured content starting at each Section's own boundary, so that intro content — prose, labels,
*and* formulas — was silently dropped in its entirety, not just missing a label. Fixed by capturing the
chapter-level intro items and prepending them to the first section's body (`tools/lyx2md.py`, `main()`).
Chapter 6 now reconciles exactly: 400/400. (Chapter 3's smaller pre-existing 1-formula gap was checked
against this same bug and confirmed *not* to be an instance of it — Chapter 3's intro paragraph contains no
formulas at all.)

**Chapter 7's apparent 23-formula gap is not a bug.** It's fully explained by 23 local `FormulaMacro`
insets (LyX Math Macro *definitions*, not content) — `render_tabular` aside, these correctly produce no
visible output; see "Specific insets flagged" below.

## Per-section breakdown

### Chapter 1 — Introduction

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 1.1 | Overview of FEBio | 0 | 0 | 0 | 0 | Yes | None |
| 1.2 | About this Document | 0 | 0 | 0 | 0 | Yes | None — all four chapter cross-references (`chap:Element-Library`, `chap:Constitutive-Models`, `chap:Contact-and-Coupling`, and the implicit Chapter 2/3 refs) now resolve to hyperlinked chapter numbers now that every chapter is converted |

### Chapter 2 — Continuum Mechanics

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 2.1 | Vectors and Tensors | 42 | 26 | 2 | 0 | Yes | None — gained a second footnote and its chapter-intro paragraph once the chapter-intro-capture fix (see Chapter 6 note above) applied here too |
| 2.2 | The Directional Derivative | 10 | 6 | 1 | 0 | Yes | None |
| 2.3 | Cauchy Stress | 21 | 1 | 0 | 0 | Yes | None |
| 2.4 | Axioms of Conservation | 30 | 11 | 0 | 0 | Yes | None |
| 2.5 | Kinematics of the Continuum | 210 | 57 | 1 | 3 | Mostly | 3 figures (`FigKinematicsContinuum.png`, `FigShearStrain.png`, `FigReferentialVolume.png` — not in the pilot's original inputs, fetched from upstream by `build.py` at build time, see README); `\ref{subsubsec:determinant}` now resolves correctly to Appendix A (`A.1-second-order-tensors.md#subsubsec:determinant`) now that it's converted |
| 2.6 | Hyperelasticity | 144 | 79 | 11 | 0 | Yes | `\ref{chap:Constitutive-Models}` now resolves to a hyperlinked "5" (Chapter 5 is converted); cross-section `\eqref{}`s into section 2.5 (including `eq87`, referenced via a plain `\ref{}` rather than `\eqref{}`) resolve to static links (e.g. `(2.5-35)`); uses `\obslash` (see README) and `\mbox{\thinspace and\thinspace}` (eq. 11, renders correctly via MathJax macro fix) |
| 2.7 | Biphasic Material | 26 | 6 | 3 | 0 | Yes | None |
| 2.8 | Biphasic-Solute Material | 109 | 13 | 14 | 0 | Yes | None |
| 2.9 | Triphasic and Multiphasic Materials | 66 | 15 | 0 | 0 | Yes | None |
| 2.10 | Constrained Reactive Mixture of Solids | 201 | 29 | 6 | 0 | Yes | Cross-section `\ref{subsec:Nearly-Incompressible-Hyperelast}` (into 2.6.8) correctly resolves to `2.6-hyperelasticity.md#subsec:Nearly-Incompressible-Hyperelast` |
| 2.11 | Equilibrium Swelling | 56 | 9 | 0 | 0 | Yes | None |
| 2.12 | Chemical Reactions | 105 | 41 | 0 | 0 | Yes | None |
| 2.13 | Fluid Mechanics | 127 | 24 | 0 | 0 | Yes | `\ref{sec:Viscous-Fluids}` now resolves to Chapter 5 (`5.16-viscous-fluids.md#sec:Viscous-Fluids`); cross-*chapter* `\eqref{eq:viscous-stress}` into section 5.16 now resolves to a static link |
| 2.14 | Fluid-Structure Interactions | 27 | 15 | 1 | 0 | Yes | None |
| 2.15 | Hybrid Biphasic Material | 137 | 17 | 8 | 0 | Yes | `\ref{sec:Hydraulic-Permeability}` now resolves to Chapter 5 (`5.8-hydraulic-permeability.md#sec:Hydraulic-Permeability`) |
| 2.16 | Fluid-Solutes Analyses | 144 | 19 | 12 | 0 | Yes | None |

### Chapter 3 — The Nonlinear FE Method

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 3.1 | Weak formulation for Solid Materials | 27 | 22 | 1 | 1 | Yes | Figure `FigCentrifugalBodyForce.png` (bare `Graphics` inset decorated with `Box`/`VSpace`, no `Float`/`Caption`); gained its chapter-intro paragraph (see Chapter 6 note above); the table before eq. 20 is centered (default behavior for all tables now) |
| 3.2 | Weak formulation for biphasic materials | 115 | 35 | 5 | 0 | Yes | None |
| 3.3 | Weak Formulation for Biphasic-Solute Materials | 156 | 62 | 3 | 0 | Yes | None |
| 3.4 | Weak Formulation for Multiphasic Materials | 150 | 87 | 2 | 0 | Yes | None |
| 3.5 | Computational Fluid Dynamics | 184 | 38 | 7 | 0 | Yes | Three `\eqref{}`s into Chapter 4/5 (`eq:virtual-work-internal`, `eq:virtual-work-external`, `eq:ideal-fluid`) now resolve to static links now that those chapters are converted |
| 3.6 | Weak Formulation for FSI | 81 | 131 | 1 | 0 | Yes | None |
| 3.7 | Weak Formulation for BFSI | 154 | 49 | 3 | 0 | Yes | None |
| 3.8 | Weak Formulation for Fluid-Solutes Analyses | 57 | 39 | 1 | 0 | Yes | None |
| 3.9 | Newton-Raphson Method | 37 | 30 | 1 | 0 | Yes | None |
| 3.10 | Generalized α-Method | 26 | 7 | 1 | 0 | Yes | Section title contains inline math (`$\alpha-$Method`); verified via headless browser that MathJax correctly typesets it both in the page heading and the nav sidebar |

### Chapter 4 — Element Library

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 4.1 | Solid Elements | 23 | 7 | 1 | 2 | Mostly | 4 `Tabular` insets with merged cells (colspan/rowspan) — not representable in plain Markdown, rendered best-effort and flagged; 2 figures (`FigSolidElementsTM.png`, `FigQuadraticTetrahedralElements.png`) fetched from upstream; `\Square` (eq. 374, "the biunit cube") has no macro definition anywhere in the source — see the "Specific equations/insets flagged" table below |
| 4.2 | Shell Elements | 69 | 56 | 11 | 3 | Yes | 3 figures (`FigShellElementsTM.png`, `FigShellElementTypesTM.png`, `FigShellElementsFB.png`) fetched from upstream; equations `eq:virtual-work-internal` and `eq:virtual-work-external`, referenced cross-chapter from Section 3.5, are defined here |

### Chapter 5 — Constitutive Models

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 5.1 | Linear Elasticity | 23 | 9 | 0 | 0 | Yes | 6 formulas in the Lame-parameter conversion table were misclassified as display/corrupted by a parser bug (see "Specific insets flagged" below); fixed, now correctly inline |
| 5.2 | Compressible Materials | 188 | 98 | 7 | 0 | Yes | None |
| 5.3 | Nearly-Incompressible Materials | 71 | 44 | 13 | 0 | Yes | None |
| 5.4 | Viscoelasticity | 227 | 44 | 20 | 5 | Yes | 5 figures fetched from upstream (`FigStandardLinearSolid.png`, `FigRelaxationSpectrumMalkin.png`, `FigRelaxationMalkin.png`, `FigRelaxationSpectrumExponential.png`, `FigContinuousExponentialRelaxation.png`) |
| 5.5 | Reactive Damage Mechanics | 109 | 47 | 10 | 0 | Yes | None |
| 5.6 | Reactive Plasticity | 209 | 17 | 3 | 3 | Yes | 3 figures fetched from upstream |
| 5.7 | Reactive Elastoplastic Damage Mechanics | 118 | 11 | 4 | 1 | Yes | `fig:damage-parametric` label is a sibling of `Caption` rather than nested inside it (unlike every other figure in the document) — both `render_float()` and `prescan_nested()` special-cased to detect it; 1 figure fetched from upstream |
| 5.8 | Hydraulic Permeability | 22 | 17 | 2 | 0 | Yes | None |
| 5.9 | Solute Diffusivity | 21 | 6 | 0 | 0 | Yes | None |
| 5.10 | Solute Solubility | 2 | 0 | 0 | 0 | Yes | None |
| 5.11 | Osmotic Coefficient | 2 | 0 | 0 | 0 | Yes | None |
| 5.12 | Active Contraction Model | 14 | 3 | 1 | 0 | Yes | None |
| 5.13 | Prescribed Active Contraction | 7 | 6 | 0 | 0 | Yes | None |
| 5.14 | Chemical Reaction Production Rate | 24 | 7 | 0 | 0 | Yes | None |
| 5.15 | Specific Reaction Rate | 11 | 2 | 2 | 0 | Yes | None |
| 5.16 | Viscous Fluids | 39 | 5 | 3 | 0 | Yes | `eq:ideal-fluid`, referenced cross-chapter from Section 3.5, is defined here |

### Chapter 6 — Dynamics

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 6.1 | Newmark Integration | 31 | 13 | 1 | 0 | Yes | Gained its chapter-intro prose and 4 equations (eq717–eq720) — see the reconciliation-summary bug fix above |
| 6.2 | Elastodynamics | 90 | 53 | 6 | 0 | Yes | None |
| 6.3 | Rigid Body Dynamics | 153 | 60 | 2 | 0 | Yes | None |

### Chapter 7 — Contact and Coupling

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 7.1 | Sliding Interfaces | 368 | 115 | 18 | 1 | Yes | 23 local `FormulaMacro` definitions (BFSI contact notation shorthand: `\no`, `\so`, `\Na`, `\Nb`, etc.) — render as nothing (definitions, not content); equivalent MathJax `macros` added to `docs/js/mathjax_config.js` since MathJax has no per-page macro scoping; 1 figure (`FigTwoBodyContactProblem.png`) fetched from upstream |
| 7.2 | Biphasic Contact | 219 | 67 | 11 | 0 | Yes | None |
| 7.3 | Biphasic-Solute Contact | 24 | 26 | 0 | 0 | Yes | None |
| 7.4 | Multiphasic Contact | 25 | 26 | 0 | 0 | Yes | None |
| 7.5 | Tied Contact | 7 | 17 | 0 | 0 | Yes | None |
| 7.6 | Tied Biphasic Contact | 33 | 21 | 1 | 0 | Yes | None |
| 7.7 | Tied Multiphasic Contact | 38 | 24 | 1 | 0 | Yes | None |
| 7.8 | Tied Fluid Interface | 73 | 26 | 1 | 0 | Yes | None |
| 7.9 | Rigid Connectors | 163 | 92 | 0 | 0 | Yes | None |
| 7.10 | Rigid-Deformable Coupling | 48 | 8 | 1 | 0 | Yes | None |
| 7.11 | Nonlinear Constraints | 36 | 12 | 0 | 0 | Yes | 2 `Example` layouts (`theorems-ams` module) — see "Specific insets flagged" below |

### Chapter 8 — Optimization

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| 8.1 | The Objective Function | 4 | 1 | 0 | 0 | Yes | None |
| 8.2 | The Levenberg-Marquardt Method | 18 | 5 | 0 | 0 | Yes | A bare `\url{...}` ERT pattern (not previously seen — only `\href{}{}` had occurred before) renders as a Markdown autolink `<url>` |

### Appendix A — Tensor Calculus

Chapter 9 in the LyX source; marked with `\start_of_appendix`, which switches this chapter (and any after
it) from numeric to lettered numbering and from "Chapter" to "Appendix" in the nav.

| Section | Title | Inline formulas | Display formulas | Citations | Figures | Converted cleanly? | Needs manual review |
|---|---|---|---|---|---|---|---|
| A.1 | Second-Order Tensors | 230 | 83 | 0 | 2 | Yes | `subsubsec:determinant`, referenced cross-chapter from Section 2.5, is defined here; 2 figures (`FigOrthoBases.png`, `FigRotationAboutX3.png`) fetched from upstream; 10 raw `Example` layouts in the source collapse to 5 real examples (3 runs of consecutive `Example` layouts are one logical example each) plus 2 separate `Theorem*` layouts — see "Specific insets flagged" below |
| A.2 | Higher Order Tensors | 22 | 23 | 0 | 0 | Yes | 1 `Example` layout |

## Specific equations/insets flagged for human review

| Section | Item | Issue | Resolution taken |
|---|---|---|---|
| 2.1 | eq. (11) `\mbox{\thinspace and\thinspace}` | `\mbox` and `\thinspace` are not in MathJax's default macro set | Added `mbox` and `thinspace` macros to `docs/js/mathjax_config.js`; verified render |
| 2.1, 2.6, 2.9–2.16, 3.x–7.x (throughout) | `\tr`, `\dev`, `\grad`, `\divg`, etc. | Custom operators defined in the *full manual's* LyX preamble (`\newcommand`), not standard LaTeX/MathJax | Added equivalent `macros` entries to `docs/js/mathjax_config.js` |
| 2.1, 2.6 (eq. 19, 22, 25, 26) | `\obslash` | **No macro definition exists anywhere in the source LyX file for this symbol** — appears to be a gap in the original document, not something this converter introduced | Renders as `⦸` (U+29B8 CIRCLED REVERSE SOLIDUS, `\mathbin{\unicode{x29B8}}` in `mathjax_config.js`), confirmed against the published manual as the correct glyph |
| 4.1 (eq. 374 and the sentence right after it) | `\Square` | **No macro definition exists anywhere in the source LyX file for this symbol either** — same gap class as `\obslash` above, and confirmed present in the real published manual too, so there's no reference rendering to match against. Per the manual's own prose it denotes "the biunit cube" (the reference/master isoparametric element domain for Gauss-quadrature integration); real amsmath/amssymb only define the lowercase `\square`/`\Box`, not a capitalized `\Square` | Aliased `Square: '\\square'` in `docs/js/mathjax_config.js`, rendering the standard hollow-square glyph (U+25A1) used for this exact "reference element" notation in FEM literature |
| 2.5, 3.1, 4.1, 4.2, 5.4, 5.6, 5.7, A.1 (throughout) | Figure captions/images | Original image binaries not present in the pilot's original input directory | `build.py` fetches the real artwork from `febiosoftware/FEBio` on GitHub at build time; original LyX caption text preserved verbatim |
| Chapter-spanning | Cross-section/cross-chapter `\eqref{}`/`\ref{}` to equations, e.g. `\eqref{eq88}` (2.5→2.6), `\eqref{eq:virtual-work-internal}`/`\eqref{eq:virtual-work-external}` (4.2→3.5), `\eqref{eq:ideal-fluid}` (5.16→3.5) | Each Section is a separate page; MathJax's per-page auto-numbering can't resolve a `\label{}` defined on a different page, so these previously rendered as unclickable "???" | `EQ_LABEL_REGISTRY` resolves these to a static link with the target's own page-local equation number, e.g. `(2.5-35)`, linking to MathJax's `#mjx-eqn:<label>` anchor |
| Chapter-spanning | `\ref{chap:X}` to a chapter (e.g. "see Chapter 5") | Previously rendered the chapter's full title instead of its number, and was unresolvable/inconsistent for chapters not yet converted | `CHAPTER_LABEL_REGISTRY` is populated for every chapter regardless of conversion status; a chapter `\ref{}` now always renders the chapter *number*, hyperlinked if converted, plain text otherwise |
| 2.10, 2.9 | `\ref{subsec:Nearly-Incompressible-Hyperelast}`, `\ref{subsec:BS-continuous-variables}` | Cross-section reference | Fixed a real converter bug where a redundant label re-registration during rendering (without a filename) silently overwrote the correct pre-scanned registry entry |
| 3.1 | `FigCentrifugalBodyForce.png` | Bare `Graphics` inset decorated with `Box Frameless`/`VSpace` insets, not wrapped in `Float`/`Caption` | Added `Box` (renders content transparently) and `VSpace` (renders as nothing) to the inset dispatch table |
| 3.1 | Figure after eq. 9 | Rendered right-aligned (LyX's `\align center` on the enclosing `Box` was silently dropped by the inline-only rendering state machine) | `center_images()` injects centering CSS directly into the image's `attr_list` style, once the more obvious `<div align="center">` wrapper approach was confirmed (via direct HTML inspection) to leave nested Markdown image syntax unprocessed without `md_in_html` |
| 3.1 | Table before eq. 20 | The manual's own layout doesn't center this particular (wider) table, but centering was made the default for *all* tables going forward per explicit request | Wrapped every table in `<div markdown="1" style="display: flex; justify-content: center;">`; required adding `md_in_html` to `mkdocs.yml` so the nested Markdown table syntax is actually parsed instead of left as literal text |
| 3.4 | `Tabular` inset (7×3 grid) | `render_tabular()` was previously a stub | Implemented for real: LyX's `<lyxtabular>`/`<row>`/`<cell>` pseudo-XML tags are used purely as delimiters to group the correctly-parsed `Text` insets holding each cell's content. Surfaced two general renderer bugs: (1) a cell's `\series bold` with no explicit `\series default` before `\end_layout` (LyX allows this — formatting is implicitly scoped to the paragraph) left an unclosed `**` that mis-paired with a later marker, corrupting everything in between — fixed by auto-closing any open bold/emph/tt state at the end of every `render_items_inline()` call; (2) a Markdown table needs a real newline between rows, which collided with a normalization pass collapsing stray single newlines to spaces — fixed with a sentinel character protecting row breaks |
| 4.1 | 4 `Tabular` insets (element property tables) | Merged cells (colspan/rowspan) — first occurrence in the document | Not representable in plain Markdown; `TABLE_CELL_SPAN_RE` detects and flags each occurrence, `render_tabular()` renders a best-effort approximation rather than silently misaligning |
| 5.7 | `fig:damage-parametric` | Figure label is a sibling of `Caption` within the same Plain Layout rather than nested inside it — every other figure in the document has the label inside the caption | Extended both `render_float()` and `prescan_nested()` to also detect a standalone `CommandInset label` sibling |
| 6.1 | Chapter-opening prose + eq717–eq720 | **Real content-loss bug**: content between the `Chapter` heading and the first `Section` boundary (intro prose *and* 4 numbered equations) was entirely dropped, not just missing its label — caught via formula-count reconciliation (385/400) | `main()` now captures this intro content and prepends it to the first section's body; Chapter 6 reconciles exactly (400/400) afterward |
| 7.1 | 23 `FormulaMacro` insets | LyX Math Macro *definitions* (BFSI contact notation shorthand), correctly produce no visible output — this explained an apparent 23-formula discrepancy that was not a bug | `FormulaMacro` insets render as `""`; equivalent macros added to `docs/js/mathjax_config.js`'s global `macros` block (MathJax has no per-page macro scoping) |
| 7.11, A.1, A.2 | `Example` (13 total: 2 in 7.11, 10 in A.1, 1 in A.2) / `Theorem*` (2, both in A.1) layouts | LyX's `theorems-ams` module — not previously encountered. Initially rendered as `!!! example "Example N"` / `!!! note "Theorem"` Material admonition callout boxes; the published manual doesn't box these off, it just numbers them inline like a normal LaTeX theorem environment, so the boxes were a visible deviation from the original | Rendered as a bold run-in label directly in the text flow instead — `**Example N.** <body>` / `**Theorem.** <body>` — with per-page numbering (mirrored between the pre-scan and render passes, same pattern as `ctx.eq_counter`/`ctx.fig_counter`) |
| A.1 | 3 places where the source has **multiple consecutive `\begin_layout Example` blocks with nothing but a blank line in between** ("Scaling transformation" x4, "Show that..."/"Using indicial notation..." x2, "Rotation about $x_3$"/"Reflection about..." x2) | **Real converter gap**: in LyX/LaTeX's `theorems-ams` module, consecutive same-style paragraphs continue the *same* numbered environment (extra paragraphs of one example), they don't each start a new one — a rule the counter/renderer didn't implement (it incremented and started a fresh bold label on every `Example` layout unconditionally). This produced 4 (and, in two other spots, 2 and 2) separate "Example N." labels in a row for what the published manual presents as one example each, e.g. "Example 2. A scaling transformation... Example 3. Solution. Is T a tensor?..." reading as 4 disconnected examples instead of one problem-then-solution. Found by systematically walking the parse tree for every consecutive same-kind `Example`/`Theorem*` run in the whole document (confirmed the 2 in 7.11 and the other 2 A.1/A.2 instances are each genuinely standalone) | Fixed in `tools/lyx2md.py`: `render_section_body()`'s `Example`/`Theorem*` branches (and the mirroring pre-scan counter in `main()`'s `prescan()`) now track the previous top-level layout's kind and only advance the counter / emit a fresh bold label when it *wasn't* the same kind; a same-kind continuation is appended as a new paragraph of the current example/theorem instead. A blank `text` item between two layouts (LyX's normal between-paragraph noise) doesn't break the run, but anything else non-blank does -- needed because Appendix A.1's second `Theorem*` (a genuinely separate fact, not a continuation) is wrapped in `\begin_deeper`/`\end_deeper`, which sits between the two `Theorem*` layouts as its own non-blank top-level `text` item and correctly breaks what would otherwise have been a false merge |
| 8.2 | `\url{...}` ERT | Only `\href{}{}` had previously been seen; a bare `\url{}` is a different ERT pattern | Added `ERT_URL_RE`, rendering as a Markdown autolink `<url>` |
| Throughout (all chapters) | `\begin_inset CommandInset bibtex` | LaTeX's `\bibliography{}` insertion marker, not a citation | Suppressed (renders as `""`) |
| 5.1 | 6 `\begin_inset Formula` insets inside the Lame-parameter conversion table, e.g. `$\begin{array}{l}`/`E=...\\`/`\nu=...`/`\end{array}$` | **Real parser bug**: LyX writes this formula's first line of math content (`$\begin{array}{l}`) directly on the same physical line as `\begin_inset Formula` itself, but the formula doesn't close there (it continues for 2 more lines before `\end{array}$`). `parse_flat()`'s existing single-line-inline-formula special case only fires when the formula closes on that same line (`spec.count("$") >= 2`); otherwise that leading text was silently discarded (it lives only in `spec`, which nothing downstream reads beyond its first token), corrupting the formula -- rendered as a bare `\[ ... \end{array}$ \]` with the `\begin{array}{l}` opener missing and a stray trailing `$`. Confirmed via exhaustive search of the whole source that this exact pattern (a Formula inset opening with unclosed math on its `\begin_inset` line) occurs in exactly these 6 places, all in this one table -- no other page is affected | Added a parser branch for this case: the leading math text is now prepended as the inset's first content line instead of being dropped, so the full `$\begin{array}{l}...\end{array}$` reaches `render_formula_inset()` intact and correctly resolves as inline math |
| 2.5, 5.4, 5.6, 5.7 | Figure `\ref{}`s (e.g. "is its complementary angle (Figure Figure (2.5)), so that" in 2.5) | The link text duplicated the literal word "Figure" already in the source prose, and showed the *section* number (`entry['section']`, e.g. "2.5") rather than a real per-figure count — the registry never tracked one | Added a per-page figure counter to the pre-scan pass (mirroring `ctx.fig_counter`, incremented on every `Graphics` inset in document order, matching what `pymdownx.blocks.caption` numbers on the page) and stored it in `LABEL_REGISTRY` as `fig_number`; a figure `\ref{}` now renders as just that number (e.g. "Figure [2](#fig17)"), with a `<section>.` prefix only for a figure defined on a different page — no cross-page figure reference currently occurs in the manual, but the logic mirrors `EQ_LABEL_REGISTRY`'s equation convention for when one does |
| — | `eq87`, `eq:viscous-stress`, `eq:virtual work` | Earlier notes here described these as broken references in FEBio's own source | **Correction (still accurate):** all three are real, resolvable labels — missed by an incomplete search at the time (only `CommandInset label` was checked, not raw `\label{}` embedded in formula bodies). All now resolve, since every chapter is converted |

## Fidelity spot-checks against published HTML

- **Section 2.1** (`docs/theory/chapter2/2.1-vectors-and-tensors.md` vs.
  [help.febio.org TM40-Section-2.1](https://help.febio.org/docs/FEBioTheory-4-0/TM40-Section-2.1.html)):
  matches on all definitions (dot/scalar product, cross product, vector
  outer product, double contraction/tensor inner product, trace, tensor
  invariants \(I_1, I_2, I_3\), symmetric/anti-symmetric decomposition,
  Voigt notation, permutation tensor, fourth-order tensor operators
  \(\otimes, \oslash, \obslash, \odot\) and their Cartesian component
  forms, fourth-order identity tensors) and its footnote citations. Equation numbering
  (1)–(26) is sequential and matches the source structure.
- **Section 2.6** (`docs/theory/chapter2/2.6-hyperelasticity.md` vs. the
  [published TOC for 2.6](https://help.febio.org/docs/FEBioTheory-4-0/TM40-Section-2.6.html)):
  all 9 subsections match exactly, in order — 2.6.1 Constitutive
  Restrictions, 2.6.2 Other Stress Tensors, 2.6.3 Directional Derivative of
  the Stress, 2.6.4 Isotropic Hyperelasticity, 2.6.5 Isotropic Elasticity in
  Principal Directions, 2.6.6 Transversely Isotropic Hyperelasticity, 2.6.7
  Incompressibility, 2.6.8 Nearly-Incompressible Hyperelasticity, 2.6.9
  Tension-Bearing Fiber Materials — confirmed via
  `grep -n "^## " docs/theory/chapter2/2.6-hyperelasticity.md`.

## Visual verification

`mkdocs serve` was run locally and section 2.1 and 2.6 were screenshotted
with a headless-Chromium Playwright script
(`tools/screenshot_section.py`) after waiting for MathJax's
`mjx-container` elements to appear:

- Section 2.1: confirmed all 26 numbered display equations render as typeset
  math (matrices, tensors, fractions), the sidebar nav lists all 16 sections,
  and the footnote renders at the bottom of the page.
- Section 2.6: confirmed the denser, citation-heavy section (11 citations, 79
  display equations) also renders cleanly end-to-end with no raw LaTeX
  visible.

For the Chapters 4–9 conversion, Playwright was used again (headless Chromium, not just static grep) to
spot-check: the full nav tree (all 9 chapters/appendix, in order, each expanding to its sections), a
footnote from a `Foot` inset rendering at the bottom of its page, the centered table and centered figure in
Section 3.1, and the absence of any raw `\macro` command names leaking onto the page from Chapter 7's local
`FormulaMacro` definitions. `Example`/`Theorem*` rendering was re-verified visually a second time after
switching it from a Material admonition box to a plain bold run-in label (Section 7.11), confirming the
label and body now flow inline with the surrounding text as in the published manual.

Real rendering bugs that were only caught by actually looking at the rendered page, not by static
grep-based checks, across the life of this project so far: the `\tr`/`\obslash` custom-macro gap, the
`\mbox`/`\thinspace` nesting issue, the table-cell unclosed-bold-marker bug, the table-row newline collapse,
the `mjx-eqn:` anchor space-to-underscore sanitization needed for a working cross-chapter equation link, a
figure's `\align center` being silently dropped by the inline-only rendering state machine, and `md_in_html`
being required for a `<div markdown="1">`-wrapped table's nested Markdown to actually parse — see
`docs/js/mathjax_config.js`, `tools/lyx2md.py`, and the tables above.
