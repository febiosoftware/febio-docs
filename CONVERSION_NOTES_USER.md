# Conversion Notes — FEBio User Manual

Companion to `CONVERSION_NOTES.md` (Theory) and `CONVERSION_NOTES_STUDIO.md` (Studio). Covers the
conversion of `source/FEBio_User_Manual.lyx` → `docs/user/` by `tools/lyx2md.py`.

## Scope

The vendored source is **a stripped-down cut of the upstream User Manual**, committed by Steve Maas on
2026-09-10 ("Added stripped-down user manual"). It is 876 KB against the upstream copy's 2.8 MB in
[febiosoftware/FEBio](https://github.com/febiosoftware/FEBio)'s `Documentation/` directory. Everything
below describes the cut as vendored, not the full manual.

All 14 chapters convert: Chapters 1–9 plus five lettered appendices (the source marks Chapter 10 with
LyX's native `\start_of_appendix`).

| Chapter | Title | Sections |
|---|---|---|
| Chapter 1 | Introduction | 4 |
| Chapter 2 | Running FEBio | 10 |
| Chapter 3 | Free Format Input | 19 |
| Chapter 4 | Multi-Step Analysis | 2 |
| Chapter 5 | Restart Input file | 6 |
| Chapter 6 | Parameter Optimization | 3 |
| Chapter 7 | Configuration File | 2 |
| Chapter 8 | FEBio Plugins | 2 |
| Chapter 9 | Troubleshooting | 13 |
| Appendix A | Heterogeneous model parameters | 2 |
| Appendix B | Referencing Parameters | 1 |
| Appendix C | Math Expression | 2 |
| Appendix D | FEBio Binary Database Specification | 5 |
| Appendix E | FEBio Output | 2 |

| Metric | Count |
|---|---|
| Chapters converted | 14 (1–9 plus Appendices A–E) |
| Sections converted | 73 |
| Inline `$...$` formulas | 254 |
| Display `\[...\]` formulas | 18 |
| Citations | 13 |
| Figures | 6 (fetched at build time) |
| Unhandled/unknown inset kinds | 0 |
| Leftover LyX bookkeeping artifacts in output | 0 |

## Bibliography

The vendored cut has **12 citation insets (13 distinct keys) but no bibliography pointer** — the
upstream document carries `bibfiles "FEBio3"` and 143 citations; the stripping removed the
`\bibliography`/bibtex inset along with most of the citing text, but left these behind.

`build.py` therefore points this manual's `--bib` at `source/FEBio3.bib`, the database upstream names
and which the Theory Manual already uses. **All 13 keys resolve in it:** `Bathe86`, `Betsch95`,
`Bischoff18`, `Bischoff97`, `Gee09`, `Hou18`, `Klinkel99`, `MacNeal78`, `Maker95`, `Shim23`, `Simo90`,
`Simo93`, `Vu-Quoc03`. They render as per-page Markdown footnotes, as in the other manuals.

**Open question for the FEBio maintainers:** whether the stripped cut is *supposed* to retain these
citations, or whether they are leftovers that should have gone with the removed chapters.

## Dangling cross-references (the one real content gap)

The cut contains **35 `\ref{}` cross-references to 24 distinct labels that no longer exist anywhere in
the document** — all of them to sections that *are* present in the full upstream manual (verified: 24/24
defined upstream, 0/24 defined in the cut). They point mostly at the removed Materials chapter and at
boundary-condition/fluid sections, e.g. `chap:Materials`, `sec:Elastic-Solids`,
`sec:Biphasic-Materials`, `subsec:Fluid-Backflow-Stabilization`, `subsec:Prescribed-Displacement`.

These are a consequence of the stripping, not a converter defect. `render_ref()` degrades them to
readable italic plain text rather than emitting a dead link — so
"A complete list of available materials and their parameters is provided in Chapter *Materials*."
rather than a link labelled `chap:Materials` pointing at a nonexistent anchor. Every one is recorded in
`tools/_stats_user.json` under the owning section's `needs_review`.

**Open question for the FEBio maintainers:** whether the referencing prose should be reworded, or those
target sections restored.

## Converter gaps this manual surfaced

Converting it exposed seven constructs absent from both the Theory and Studio manuals. All are fixed;
`unhandled` is 0 and the leftover-artifact grep is clean.

| # | Construct | Count | Previous behavior | Fix |
|---|---|---|---|---|
| 1 | `Verbatim` layout | 88 | Fell through to the prose renderer, flattening `febio_spec` XML listings into paragraphs and destroying indentation | Treated like `LyX-Code`: fenced code, with consecutive layouts joined into one block |
| 2 | `Newline` inset | 33 | `<!-- UNHANDLED INSET Newline -->` mid-sentence | Renders as `<br>` (a forced line break) |
| 3 | ERT `\\` | 15 | `<!-- ERT: \\ -->` | Same `<br>`; the source uses both spellings for the same effect |
| 4 | `\nospellcheck on`/`default` | 10 | Leaked into the page as literal text | Dropped as editor-only bookkeeping, in both the prose and verbatim renderers |
| 5 | `Flex URL` inset | 5 | `<!-- UNHANDLED INSET Flex -->` | Renders as a Markdown autolink |
| 6 | `Paragraph*` / `Labeling` layouts | 5 / 4 | Unhandled; `Labeling` also leaked `\labelwidthstring 00.00.0000` | Aliased to the existing `Paragraph` and `Description` renderers |
| 7 | Space in a figure filename | 1 | `![FEBio flow](figs/FEBio flow.png)` — the space ends the link target, so the image never rendered | Space percent-encoded in the link; `build.py`'s fetcher now un-quotes before using the name as a path |

Two further fixes were needed for correct output:

- **`\begin_deeper` fragmenting code listings.** The manual indents the body of an XML sample inside
  `\begin_deeper`/`\end_deeper`, which force-closed the open fence and split one listing into two
  adjacent code blocks (section 3.7's `ut4-solid` `SolidDomain` sample). Deeper markers are now
  transparent to an open fence while still breaking an Example/Theorem\* continuation run, which is
  what they were originally checked against.
- **Fence ownership.** A `LyX-Code` run immediately followed by a `Verbatim` run would have merged into
  a single fence, so the open fence now records which layout kind opened it.

**Item 7 also fixed a pre-existing Studio Manual bug**: three of its figures (`file viewer.png`,
`Model Viewer.png`, `Material Viewer.png`) have spaces in their names and had never rendered as images.

## Known limitations / flagged for review

- **One table with merged cells** (4 `multicolumn` attributes across 2 tables in Chapter 1). Markdown
  has no colspan, so `render_tabular()` flags rather than guesses — this is the first manual in the
  repo to actually reach that code path. See the owning section's `needs_review`.
- **Graphics sizing attributes are partly ignored.** `render_graphics()` honors `scale NN` but drops
  `width` (`4.88in`, `2cm`) and `special height=...`. Only the two front-matter images use those, and
  the front matter isn't converted, so nothing rendered is affected today.
- **Front matter is not converted** (title page, `\begin_layout Title`/`Date`, the table of contents
  inset). This matches the Theory and Studio manuals. Consequently `FigFEBioTitle.png` and
  `NIHlogo.png` are referenced by the source but never fetched — only the 6 in-body figures are.
- **Math macros.** The source defines six operator macros via `FormulaMacro` insets (`\tr`, `\dev`,
  `\Dev`, `\grad`, `\divg`, `\Ei`); `\grad` and `\divg` are used in body math. All six were already
  present in `docs/js/mathjax_config.js` from the Theory Manual, so no additions were needed.

## Validation

- `python3 build.py` — 73 sections across 14 chapters, `unhandled: 0`.
- `mkdocs build --strict` — exits 0 with zero `WARNING`-level output.
- Leftover-artifact grep across `docs/` — zero matches for `begin_inset`, `end_inset`, `begin_layout`,
  `SpecialChar`, `nospellcheck`, `labelwidthstring`, `UNHANDLED`.
- Theory and Studio output re-checked after every converter change: byte-identical apart from the three
  intentionally-fixed Studio figure links described above.
