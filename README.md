# FEBio-Documentation

A MkDocs site collecting FEBio's manuals into one searchable site (Material for MkDocs theme, indigo
palette, `pymdownx.arithmatex` + MathJax for equations, footnote-based citations). The site has three
tabs, each a separately generated manual:

- **Theory** — the FEBio Theory Manual. Started as a single-chapter pilot (Chapter 2, Continuum
  Mechanics); now covers the complete manual — Chapters 1 through 8 plus Appendix A (Tensor Calculus).
- **Studio** — the FEBio Studio Manual. Started as a 2-chapter pilot (Introduction, Getting Started);
  now covers the complete manual — Chapters 1 through 20 plus Appendices A (Mesh Import Formats) and B
  (Standard Data Fields). See [`CONVERSION_NOTES_STUDIO.md`](CONVERSION_NOTES_STUDIO.md) for the full
  per-chapter breakdown and the real converter gaps this manual's content surfaced.
- **Features** — the FEBio Feature Manual, absorbed from the standalone
  [`febio-feature-manual`](https://github.com/febiosoftware/febio-feature-manual) repository. 660 feature
  pages across 32 categories, 7 module pages, and the plot/log output-variable tables.

The two LyX manuals share one generic, stdlib-only converter (`tools/lyx2md.py`). The Feature Manual has
no LyX source — it is generated from FEBio's exported feature database by `tools/features2md.py`. Both
converters are run once per manual by `build.py` with that manual's own source/output paths — see "How
the converter works" below.

## Table of Contents
- [Repository layout](#repository-layout)
- [Prerequisites](#prerequisites)
- [Building the manual](#building-the-manual)
- [Deployment](#deployment)
- [How the converter works](#how-the-converter-works)
- [Conversion statistics](#conversion-statistics)
- [Known limitations / needs manual review](#known-limitations--needs-manual-review)
- [Validation performed](#validation-performed)

## Repository layout

```
source/                        vendored source for every manual
  FEBio_Theory_Manual.lyx      Theory Manual (the complete manual; from febiosoftware/FEBio's Documentation/ dir)
  FEBio3.bib
  FEBioStudio_User_Manual.lyx  Studio Manual (from febiosoftware/FEBioStudio's Documentation/ dir)
  FEBioStudio.bib
  feature-manual/
    febio_features.json        FEBio's feature database, exported from FEBio Studio
    meta/                      hand-authored per-feature descriptions + plotvars/logvars CSVs
tools/lyx2md.py                 the LyX converter (stdlib-only, generic -- see "How the converter works")
tools/features2md.py            the Feature Manual generator (port of febio-feature-manual's build.py)
build.py                        runs the right converter per manual (see its MANUALS list), generates mkdocs.yml
docs/                            generated Markdown SOURCE for mkdocs -- this is mkdocs's input, not the
                                 deployed site; see "Deployment" below
  index.md                      site root landing page (not manual-specific; links to all three tabs)
  theory/index.md                Theory Manual Preface (hand-authored)
  theory/chapter<N>/*.md         Theory Manual generated pages
  studio/index.md                Studio Manual Preface (hand-authored)
  studio/chapter<N>/*.md         Studio Manual generated pages
  features/index.md              Feature Manual Preface (hand-authored)
  features/febcode.md, febcode.png -- the febcode DSL manual (hand-authored upstream)
  features/features/*.md         generated feature pages (flat, with figs/ alongside -- see below)
  features/modules/*.md          generated module pages
  features/plotvars.md, logvars.md -- generated output-variable tables
  js/mathjax_config.js, febio.png -- the header logo, vendored from febio-feature-manual's docs/
tools/_stats.json                Theory Manual conversion stats (see build.py's MANUALS list)
tools/_stats_studio.json         Studio Manual conversion stats
tools/_stats_features.json       Feature Manual nav tree + totals + features lacking descriptions
.github/workflows/deploy.yml    GitHub Actions workflow that builds and deploys to the gh-pages branch
```

Each manual's `.lyx`/`.bib` pair is vendored (checked-in) under `source/`, so this repository builds
standalone from a bare `git clone` — the converter does not depend on any sibling directory outside this
repo. (`tools/lyx2md.py` will also pick up the Theory Manual from a sibling `../febio-docs/` directory
instead, if present and no `--lyx`/`--bib` flags are given, which is how it was used during local
development against the original workspace layout — see the module docstring.)

Which chapters actually get converted into pages is controlled per-manual by the `"chapters"` entry in
`build.py`'s `MANUALS` list (passed through to `tools/lyx2md.py --chapters`), either a comma-separated list
or `"all"`. Both manuals now use `"all"`: the Theory Manual's `{1..9}` (chapter 9 is the source's
`\start_of_appendix`-marked chapter, rendered as "Appendix A") and the Studio Manual's `{1..22}` (chapters
21 and 22 are `\start_of_appendix`-marked, rendered as "Appendix A" and "Appendix B"). Chapters not in a
manual's set are still scanned for their titles and label positions (so numbering and cross-references
stay correct regardless of conversion order), they just don't produce output files yet — this is how both
manuals grew from a small pilot to the full manual without ever needing to rewrite the cross-reference
machinery. A chapter with no `\begin_layout Section` boundaries at all (Studio Manual's Appendix B is
entirely Standard paragraphs and tables directly under the chapter heading) still produces a real output
page — treated as a single synthetic section numbered `<chapter>.1` — since `mkdocs build --strict` rejects
an empty nav list outright rather than degrading gracefully.

## Prerequisites

```
pip install mkdocs mkdocs-material
```

## Building the manual

```
python3 build.py       # runs each manual's converter, writes mkdocs.yml
mkdocs serve           # preview at http://127.0.0.1:8000
mkdocs build --strict  # build the static site into site/
```

`build.py` invokes a converter as a subprocess once per manual in its `MANUALS` list, reads back each
manual's own stats sidecar file, and uses that to generate a single `mkdocs.yml` with the correct
navigation automatically — the nav never needs to be hand-maintained. Which converter runs is selected by
the entry's `"kind"`:

- `"lyx"` (Theory, Studio) → `tools/lyx2md.py`. Its sidecar records per-chapter/per-section formula,
  citation, and figure counts plus nav ordering; the nav becomes a Preface entry followed by one group
  per converted chapter, expanding to that chapter's sections.
- `"features"` (Features) → `tools/features2md.py`. Its sidecar records a freely nested nav tree, which
  `build.py`'s `write_nav()` emits recursively; the nav becomes a Preface entry followed by Modules,
  Features (subdivided by category), Output, and Febcode.

`"kind"` also gates the figure-fetching step: only `"lyx"` manuals fetch missing figures from upstream,
since the Feature Manual's figures are vendored in `docs/features/features/figs/`.

Navigation uses `navigation.tabs`, so each manual is exactly one top-level nav key rendered as a tab
("Theory", "Studio", "Features").

## Deployment

The live site (<https://wesley-jakob-gilbert.github.io/FEBio-Documentation/>)
is served by GitHub Pages **from the `gh-pages` branch**, not from the
`docs/` folder on `main`. `docs/` on `main` is mkdocs's *source* input
(Markdown); the `gh-pages` branch holds the fully rendered, compiled HTML
output that `mkdocs build` produces into a local, gitignored `site/`
directory. These are two different branches with two different kinds of
content — pushing to `main` alone does not, by itself, change what's live.

Two ways the `gh-pages` branch gets updated:

- **Automatically:** `.github/workflows/deploy.yml` runs on every push to
  `main`. It re-generates `docs/`/`mkdocs.yml` from both manuals' vendored `.lyx` sources (so the
  deploy can never drift from what's actually committed), validates with
  `mkdocs build --strict`, then runs `mkdocs gh-deploy --force`, which
  builds the site and pushes the result to `gh-pages`. GitHub's own internal
  "pages build and deployment" step then republishes that branch to the live
  CDN — this second step happens outside our workflow and isn't always
  instant.
- **Manually**, e.g. to deploy local changes right away:
  ```
  mkdocs gh-deploy --force
  ```
  (requires push access to this repository).

## How the converter works

There are two converters, both stdlib-only. `tools/features2md.py` is described at the end of this
section; the bulk of it covers `tools/lyx2md.py`, which does far more work.

`tools/lyx2md.py` is a **stdlib-only, deterministic** Python 3 parser for
LyX's plain-text `.lyx` format. It does not shell out to LyX, Pandoc, or any
other external tool. It's generic across manuals — CLI flags (`--lyx`, `--bib`, `--docs-root`,
`--nav-root`, `--stats-out`, `--chapters`) select which manual's source it reads and where it writes,
each defaulting to the Theory Manual's paths so a bare `python3 tools/lyx2md.py` is unchanged; `build.py`
invokes it once per manual (see its `MANUALS` list) as a separate subprocess, so module-level globals and
label registries never cross-contaminate between manuals. The numbered steps below describe the rendering
logic itself, which is identical regardless of which manual is being converted.

1. **Tokenize into a tree.** `parse_flat()` reads the file line-by-line and
   builds an order-preserving tree of `('text', line)`, `('inset', spec,
   subitems)`, and `('layout', spec, subitems)` tuples, tracking
   `\begin_layout`/`\end_layout` and `\begin_inset`/`\end_inset` nesting.
   Inline formula insets (`\begin_inset Formula $x$` fully on one line) are
   special-cased at parse time so they don't get treated as the multi-line
   display-equation form.

2. **Chapter/section boundary detection.** `main()` locates every `Chapter` layout in the source (not just
   the ones being converted) to compute each one's absolute chapter number by position, then splits each
   converted chapter into its `Section` boundaries and numbers them `<chapter>.<n>`. Content that appears
   between the `Chapter` heading and the first `Section` boundary (chapter-level intro prose, and in one
   case — Chapter 6 — several numbered equations) is prepended to the first section's body rather than
   dropped; this was a real bug caught by reconciling formula counts chapter-by-chapter against the source
   (see `CONVERSION_NOTES.md`). A chapter whose source is marked with LyX's native `\start_of_appendix`
   layout (and every chapter after it) is numbered with a letter instead of a digit and labeled "Appendix"
   instead of "Chapter" in the nav — this is how Chapter 9 becomes "Appendix A" without hardcoding a chapter
   number.

3. **Two-pass label resolution.** Before rendering, a pre-scan pass walks
   every converted section and registers all `\begin_inset CommandInset label` targets
   (chapters, subsections, subsubsections, figures) into a global `LABEL_REGISTRY`, plus a parallel
   `EQ_LABEL_REGISTRY` for equation `\label{}`s (see the cross-section equation references bullet below), so
   `\ref{}`/`\eqref{}` cross-references — including ones that point to a *different*
   section's or *chapter's* file — can be resolved to the correct relative link, regardless of processing
   order. Every chapter lives in its own sibling directory under `docs/theory/` (`chapter1/`, `chapter2/`,
   ...), so `build_relative_link()` computes same-page / same-chapter / cross-chapter links accordingly. A
   third registry, `CHAPTER_LABEL_REGISTRY`, is populated for *every* chapter in the source regardless of
   whether it's actually converted, so a `\ref{}` to a chapter (e.g. "see Chapter 5") always renders the
   correct chapter *number* — hyperlinked if that chapter has been converted, plain text if not — instead of
   the chapter's full title.

4. **Character formatting** (`\series bold` → `**`, `\emph on` → `_`,
   `\shape italic` → `_`, `\family typewriter` → `` ` ``) is applied via a
   small state machine in `render_items_inline()`. LyX scopes this formatting to a single paragraph/layout
   and doesn't require an explicit closing toggle before `\end_layout` (confirmed: table cells routinely
   end with formatting left open), so any marker still open at the end of a call is auto-closed rather than
   leaking into whatever the caller appends next. A separate `fix_emphasis_whitespace()` post-pass hoists
   any whitespace LyX left *inside* emphasis/bold/code delimiters back *outside* them — Markdown (unlike
   LyX) requires no whitespace adjacent to the marker or it won't recognize the emphasis run at all. That
   pass masks underscores inside inline math (`$t_{0}$`-style LaTeX subscripts) before pairing markers,
   since otherwise they're indistinguishable from a real `_..._` delimiter and can shift the pairing across
   an entire paragraph.

5. **Math.** Inline `\begin_inset Formula $...$` becomes inline `$...$`;
   display insets (`\begin{equation}`, `align`, `aligned`, `eqnarray`,
   `array`) become `\[ ... \]` blocks with the LyX `\label{}` preserved
   inside, so MathJax's `tags: 'ams'` + `\eqref{}` numbering works exactly
   like in the Feature Manual. A same-page `\eqref{}`/`\ref{}` to an equation passes through as literal
   LaTeX for MathJax to resolve; a reference to an equation defined on a *different* page is resolved at
   build time instead (MathJax's per-page auto-numbering can't do this itself) — see the "Known
   limitations" bullet below. `ref` to a subsection becomes a Markdown link showing the subsection's title;
   `ref` to a figure becomes a Markdown link showing just the figure's number — its 1-indexed position among
   `Graphics` insets on its own page (matching what `pymdownx.blocks.caption` displays next to it), with a
   `<section>.` prefix only when the figure is defined on a *different* page than the reference, mirroring
   the equation-reference convention above. No "Figure" text is added, since the source prose always writes
   that word itself immediately before the `\ref{}` (e.g. "(Figure `\ref{fig17}`)" or "Figure~`\ref{...}`a-c.").

6. **Citations** (`\begin_inset CommandInset citation`) become
   `[^section-n]` footnote references, deduplicated per page (the same
   BibTeX key cited twice on one page reuses one footnote number), with
   definitions resolved from that manual's `.bib` file via a small hand-written
   BibTeX field parser (`parse_bib()`), and appended at the bottom of each
   page as `Author. "Title." *Journal* (Year).`. `\begin_inset CommandInset bibtex`
   (LaTeX's `\bibliography{}` insertion marker, not an actual citation) is suppressed. Real footnotes
   (`\begin_inset Foot`, distinct from citations) are collected separately and appended as
   `[^section-fn1]`, `[^section-fn2]`, etc. Author/title/journal fields sometimes spell an accented letter
   as a raw LaTeX accent command rather than a literal Unicode character (e.g. `{\"u}` or `\"u` for
   u-umlaut, found in author names like "Gültekin"); `decode_latex_accents()` translates the common ones
   (umlaut, acute, grave, circumflex, tilde) to their real Unicode character, and residual `{...}`
   capitalization-protection braces around specific words/acronyms in a title (e.g. `{A {Nonparametric}
   Approach}`) are stripped, since no case-transformation is applied to citation text here that they'd need
   to protect against.

7. **Figures** (`\begin_inset Float figure` + `\begin_inset Graphics`)
   become `![name](figs/name.png)` followed by a
   `pymdownx.blocks.caption`-style `/// figure-caption` block, with the
   figure's own `\label` hoisted to an `<a id="...">` anchor placed before
   the image (rather than left inline in the caption prose, which is where
   LyX actually stores it). A LyX `scale NN` attribute is carried through as inline CSS
   (`{: style="width:NN%" }` via `attr_list`) so the figure isn't embedded at full native pixel size. A bare
   `Graphics` inset not wrapped in a `Float` (decorated instead with LyX `Box`/`VSpace` insets, which are
   otherwise purely presentational and rendered as their content passed through transparently) is also
   handled, as is `\begin_inset Wrap figure` (LaTeX's `wrapfig` text-wrapped figure, found in the Studio
   Manual) — Markdown has no text-wrap-around-image equivalent, so it renders identically to an ordinary
   `Float figure`, and the figure-numbering prescan counts it the same way so `\ref{}` numbering stays
   consistent with what actually appears on the page.

8. **Tables** (`\begin_inset Tabular`) become plain Markdown tables (first row as header), always wrapped in
   a centering `<div markdown="1" style="display: flex; justify-content: center;">` — a plain Markdown table
   has no native alignment syntax, and `attr_list` doesn't attach to a table at all (confirmed empirically:
   an appended `{: ... }` gets absorbed as a bogus extra table row instead), so `md_in_html` is required in
   `mkdocs.yml` to get the nested table syntax inside that wrapper `div` actually parsed rather than passed
   through as literal text. LyX's tabular format is an embedded pseudo-XML dialect (`<lyxtabular>`, `<row>`,
   `<cell>`) that `parse_flat()` doesn't parse structurally; `render_tabular()` uses those tags purely as
   delimiters to group the `Text` insets (which *are* ordinary, correctly-parsed insets) holding each cell's
   real content, protecting row-separator newlines with a sentinel character so they survive a later
   prose-whitespace-normalization pass that would otherwise collapse them onto one line. Merged cells
   (colspan/rowspan) aren't representable in plain Markdown and are flagged for manual review rather than
   silently producing a misaligned table (occurs in the element-property tables of Section 4.1). A table
   wrapped in `\begin_inset Float table` (found throughout the Studio Manual; the Theory Manual only ever
   uses bare `Tabular` insets) is rendered the same way, via the same `render_tabular()` call, with its
   caption using `pymdownx.blocks.caption`'s separate `table-caption` type (own numbering sequence, doesn't
   perturb figure `\ref{}` numbering).

9. **ERT** ("evil red text", raw LaTeX LyX has no native inset for) is reconstructed from its per-line
   `\backslash`-token encoding and handles the two patterns that occur in this document: `\href{url}{text}`
   (rendering a real Markdown link, unwrapping a nested `\emph{}` in the link text to Markdown emphasis) and
   a bare `\url{url}` (rendering as a Markdown autolink `<url>`). Anything else is flagged for manual review
   instead of guessed at. LyX's *native* hyperlink inset (`\begin_inset CommandInset href`, distinct from
   the ERT reconstruction above and used throughout the Studio Manual) follows the same convention: an
   optional display `name` becomes a Markdown link, an unnamed one becomes a bare autolink.

10. **Unhandled inset kinds** render as `<!-- UNHANDLED INSET ... -->` HTML
    comments and are logged to `needs_review` — this makes the required
    zero-leftover-artifact grep double as a completeness check: any real
    parser gap shows up as a `grep`-able marker instead of silently
    dropping content.

11. **Headings** get explicit anchor IDs via `attr_list` syntax
    (`## Title {: #label }`), which is why `attr_list` was added to
    `mkdocs.yml`'s `markdown_extensions` beyond the Feature Manual's
    baseline set — it's required for the cross-section `\ref{}` links in
    step 3 to have a target to land on.

12. **Theorem-style layouts.** LyX's `theorems-ams` module layouts `Example` (numbered, per-page counter)
    and `Theorem*` (unnumbered) render as a bold run-in label directly in the text flow — `**Example
    N.** <body>` / `**Theorem.** <body>` — matching the published manual's plain LaTeX theorem-style
    numbering, not a Material admonition callout box (which the original document doesn't use; an earlier
    version of this converter rendered these as `!!! example "Example N"` boxes, since corrected). Per
    LyX/LaTeX semantics, *consecutive* same-kind layouts (nothing but a blank line between them) are
    additional paragraphs of the **same** environment instance, not a new one each — `render_section_body()`
    tracks the previous top-level layout's kind and only advances the counter / starts a fresh bold label
    when it wasn't the same kind (a non-blank item in between, e.g. LyX's `\begin_deeper`, still breaks the
    run, since that does mark a genuinely separate instance — confirmed against Appendix A.1, which has
    both cases). `Paragraph` layouts (an unnumbered run-in sub-heading, one level below Subsubsection)
    render as a bold `####` heading. `FormulaMacro` insets (LyX Math Macro definitions, e.g. Chapter 7's 23
    local shorthand macros) render as nothing — they're definitions, not visible content; the equivalent
    MathJax `macros` entries live in `docs/js/mathjax_config.js` instead, since MathJax has no per-page
    macro scoping.

13. **`Description` layouts** (LaTeX's `description` list environment, used throughout the Studio Manual;
    never occurs in the Theory Manual) render as a paragraph whose label (everything up to the first plain
    space) is auto-bolded, matching LyX's own rendering — unless the body already starts with `**`, since
    some source items explicitly wrap their label in `\series bold` instead of relying on auto-bolding, and
    auto-bolding again would double it up.

14. **`LyX-Code` layouts** (literal code/data listings — XML session-file snippets, CSV data rows, also
    Studio-Manual-only) render via `render_code_line()`, which skips the prose-oriented character-formatting
    state machine and whitespace normalization used everywhere else (both would corrupt significant
    indentation/whitespace in a literal listing). Consecutive `LyX-Code` layouts are grouped into a single
    fenced ` ``` ` block rather than one block per line, mirroring the Example/Theorem* continuation rule
    above.

Output: one Markdown file per converted Section, in `docs/theory/chapter<N>/` for the Theory Manual (e.g.
`2.1-vectors-and-tensors.md`) or `docs/studio/chapter<N>/` for the Studio Manual.

### The Feature Manual generator

`tools/features2md.py` is a port of the standalone
[`febio-feature-manual`](https://github.com/febiosoftware/febio-feature-manual) repository's `build.py`.
There is no parsing involved: it reads `febio_features.json` — FEBio's own feature database, exported
from FEBio Studio via **FEBio → FEBio Info → Export** — and emits one page per feature containing the
type string, module, category, and a parameter table, then splices in the matching hand-authored
description fragment from `source/feature-manual/meta/`. The plot and log variable tables are built the
same way, joining the database against `meta/plotvars.csv` and `meta/logvars.csv`.

The content-generation logic is carried over unchanged so pages stay comparable with upstream. Two things
differ:

- It does not write its own `mkdocs.yml` (upstream's did) — `build.py` owns the site nav for all three
  manuals, so instead it writes a nested nav tree to `--stats-out`.
- Output directories are created with `exist_ok=True`. Upstream gitignores its generated
  `docs/modules/*.md`, which leaves that directory absent in a fresh clone and makes upstream's
  `build.py` crash on it.

**Layout constraint worth knowing before rearranging anything:** the feature pages are written *flat*
into `docs/features/features/` with `figs/` alongside them, exactly as upstream laid them out. The `meta/`
fragments contain 44 relative sibling links (`[x](other_page.md)`) and 25 figure references
(`figs/Foo.png`) that only resolve under that layout — which is why the nav's "Features" section sits
inside the "Features" tab and the path doubles up. Flattening it would silently break those links
(`mkdocs build --strict` would catch them, but the fix would mean rewriting authored prose).

## Conversion statistics

### Theory Manual

Totals for the complete, fully-converted manual; see `CONVERSION_NOTES.md` for the full per-section
breakdown.

| Metric | Count |
|---|---|
| Chapters converted | 9 (Chapters 1–8 plus Appendix A / Tensor Calculus) |
| Sections converted | 64 |
| Inline `$...$` formulas emitted | 5203 |
| Display `\[...\]` formulas emitted | 1919 |
| Citations | 203 |
| Figures | 21 (artwork fetched at build time — see below) |
| Unhandled/unknown inset kinds | 0 |
| Leftover LyX bookkeeping artifacts in output | 0 |

See [`CONVERSION_NOTES.md`](CONVERSION_NOTES.md) for the full per-section
breakdown and every item flagged for manual review.

### Studio Manual

Totals for the complete, fully-converted manual; see `CONVERSION_NOTES_STUDIO.md` for the full per-chapter
breakdown.

| Metric | Count |
|---|---|
| Chapters converted | 22 (Chapters 1–20 plus Appendices A and B) |
| Sections converted | 117 |
| Inline `$...$` formulas emitted | 126 |
| Display `\[...\]` formulas emitted | 18 |
| Citations | 2 |
| Figures | 194 (artwork fetched at build time — see below) |
| Unhandled/unknown inset kinds | 0 |
| Leftover LyX bookkeeping artifacts in output | 0 |

See [`CONVERSION_NOTES_STUDIO.md`](CONVERSION_NOTES_STUDIO.md) for the full per-chapter breakdown and
every real converter gap this manual's content surfaced (not present in the Theory Manual's source).

### Feature Manual

Generated by `tools/features2md.py` from `source/feature-manual/`; totals are also written to
`tools/_stats_features.json` on every build.

| Metric | Count |
|---|---|
| Feature pages | 660 |
| Feature categories (nav sections) | 32 |
| Module pages | 7 |
| Plot variables tabulated | 262 |
| Log variables tabulated | 419 |
| Feature pages with no description yet | 264 |
| Output variables with no description yet | 38 |
| Vendored figures | 25 |

Features are filtered exactly as upstream did: the `thermo-fluid` and `polar fluid` modules are skipped
entirely, the `surface` and `datarecord` classes get no pages, and `plot*`/`log*` classes are diverted
into the Output tables instead of becoming pages. The pages lacking descriptions are listed individually
under `needs_review.pages_without_description` in the stats sidecar — adding one is just a matter of
dropping a Markdown fragment into `source/feature-manual/meta/` named exactly like the page.

## Known limitations / needs manual review

- **Every chapter of the Studio Manual is now converted.** It started as a 2-chapter pilot so the
  converter's support for this manual's LyX constructs (e.g. `Wrap`-figure insets, native
  `CommandInset href` links, `Description`/`LyX-Code` layouts, a `Float table` content-loss bug) could be
  validated against real content before committing to a full 20-chapter/117-section conversion — see
  `CONVERSION_NOTES_STUDIO.md` for the complete list of real converter gaps this manual's content
  surfaced, several of which also turned out to be latent bugs in the Theory Manual's own output (e.g.
  malformed bold/italic nesting when LyX doesn't close formatting markers in reverse-of-open order,
  `\size <name>` commands leaking as literal text, undecoded LaTeX accent escapes in citation author
  names).
- **Figure artwork is fetched automatically at build time, per manual.** Figures aren't part of either
  manual's original LyX/BibTeX inputs, so `build.py` scans every converted chapter's generated Markdown for
  figure references and fetches any missing ones from that manual's own upstream `Documentation/Figures/`
  directory — [`febiosoftware/FEBio`](https://github.com/febiosoftware/FEBio) for the Theory Manual,
  [`febiosoftware/FEBioStudio`](https://github.com/febiosoftware/FEBioStudio) for the Studio Manual — into
  that chapter's `figs/` directory (skipping the fetch if a real copy is already present). The original
  LyX-authored captions are preserved intact either way.
- **Cross-section (and cross-chapter) `\eqref{}`/`\ref{}` references to equations are resolved to static
  links, not left as `\eqref{}`.** Each Section is a separately-loaded page, and
  MathJax's `tags: 'ams'` auto-numbering is per-page -- it has no way to
  resolve a reference to a `\label{}` defined on a *different* page, which
  renders as a bare "???" with nothing to click. `EQ_LABEL_REGISTRY` in
  `tools/lyx2md.py` tracks every labeled equation's 1-indexed position
  among its own page's AMS-numbered equations (verified to exactly match
  what MathJax itself displays, and cross-checked via a real browser that the link both navigates to the
  right page and lands on the right equation); such a reference is
  then replaced with a real link like `(2.5-35)` to the target page's
  MathJax-generated `#mjx-eqn:<label>` anchor, mirroring how the published
  manual itself handles the identical problem at its finer per-subsection
  pagination (there it reads `(2.5.4-2)`). MathJax sanitizes spaces in the label to underscores when
  building that anchor id (confirmed against the one label in this document that contains a space,
  `eq:virtual work` → `mjx-eqn:eq:virtual_work`) — `mathjax_eqn_id()` replicates that. Because the anchor is
  injected by MathJax *after* the browser's initial page-load fragment-scroll
  already ran (and thus failed to find it), `docs/js/mathjax_config.js`
  also re-attempts the scroll once typesetting finishes, via MathJax's
  `startup.pageReady` hook. Same-page references are untouched since
  MathJax already resolves those correctly on its own.
- **Merged cells (colspan/rowspan) aren't representable in plain Markdown tables.** The element-property
  tables in Section 4.1 use them; `render_tabular()` flags each occurrence for manual review and renders a
  best-effort approximation rather than silently producing a misaligned table.
- **Every chapter is now converted, so cross-references no longer point outside the site.** (Earlier notes
  in this file mis-described three references — `eq87`, `eq:viscous-stress`, `eq:virtual work` — as broken
  references in FEBio's own source; they were always real, resolvable labels, just in chapters not yet
  converted at the time. All three, and every other cross-reference in the manual, now resolve.) `mkdocs
  build --strict` still emits `INFO`-level "does not contain an anchor" messages for cross-page equation
  links — this is a static-checker false positive, not a broken link: `#mjx-eqn:<label>` anchors are
  injected client-side by MathJax only after it typesets the target page, so mkdocs's link checker (which
  only inspects the built HTML/Markdown source) can't see them, even though they resolve correctly in a
  real browser. Zero `WARNING`-level messages.
- **`\obslash` has no LaTeX macro definition anywhere in the LyX source.**
  The document's preamble defines `\tr`, `\dev`, `\grad`, `\divg`, etc. as
  `\newcommand`s (and `docs/js/mathjax_config.js` reproduces them as MathJax
  `macros` so they render instead of leaving raw command names on the page),
  but `\obslash` — used 8 times in Chapter 2 for a tensor "conjugate"
  transpose-product operator — is never defined, even in the full manual.
  It was initially approximated as an overlined `\oslash`; visual comparison
  against the published manual showed the actual glyph is a
  backslash-in-a-circle rather than an overlined forward-slash-in-a-circle,
  so it now renders as U+29B8 CIRCLED REVERSE SOLIDUS (`⦸`), the mirror
  image of `\oslash`'s U+2298 CIRCLED DIVISION SLASH. This depends on the
  MathJax web font covering that codepoint — reconfirm visually if the
  MathJax CDN version ever changes.
- **`\mbox{...}` is aliased to keep its argument in math mode** rather than
  switching to true text mode, because the LyX source nests math macros
  (`\dot{}`, `\thinspace`) inside `\mbox{}` in a few places, and MathJax's
  `\text{}` does not expand macros in its argument. It's aliased to
  `\mathrm{#1}` rather than a no-op group, so plain-word arguments (`and`,
  `grad`, `div`, `M`) render in upright text font while nested macros like
  `\dot{}` and `\thinspace` still expand correctly.
- **`mkdocs build --strict` succeeds (exit code 0).** The only diagnostics
  emitted are the `INFO`-level anchor messages described above —
  there are zero `WARNING`-level messages.

## Validation performed

1. `python3 build.py && mkdocs build --strict` — exit code 0.
2. `grep -rn '\begin_\|\end_inset\|\begin_inset\|SpecialChar\|\lang ' docs/theory/` —
   **zero matches** across all converted pages.
3. Zero unhandled/unknown inset kinds logged across all converted chapters.
4. Formula counts reported by the converter's own render-pass counters (not a post-hoc regex scan) were
   checked chapter-by-chapter against the source. Chapter 2 alone reconciles exactly (1455 inline + 368
   display = 1823, matching `grep -c "begin_inset Formula"` over its source range exactly, as in the
   original single-chapter pilot); Chapter 6 also reconciles exactly (400/400) after the chapter-intro
   content-loss fix described above. Chapter 3 has one long-standing, tiny (1 of 1096, ~0.1%) unreconciled
   formula not further pursued — see `CONVERSION_NOTES.md`. Chapter 7's apparent 23-formula "gap" is fully
   explained by its 23 `FormulaMacro` definitions, which correctly produce no visible output.
5. A real browser (headless Chromium via Playwright) was used throughout development to verify things a
   static grep can't catch: MathJax equation/table/figure rendering, a chapter title containing inline math
   (`$\alpha-$Method`) rendering correctly in both the page heading and the nav sidebar, and that a
   cross-chapter equation reference link both navigates to the right page *and* scrolls to the right
   equation. (`navigation.tabs` was originally removed in favor of a single unified sidebar while this was
   a single-manual site; it was reintroduced when the Studio Manual pilot was added, this time with each
   manual as one top-level nav key/tab rather than one tab per chapter — see item 8 below.)
6. Sections 2.1 and 2.6 were read in full and spot-checked against the
   published manual at
   [help.febio.org TM40-Section-2.1](https://help.febio.org/docs/FEBioTheory-4-0/TM40-Section-2.1.html)
   and the [Chapter 2 table of contents](https://help.febio.org/docs/FEBioTheory-4-5/TM45-Chapter-2.html) — see `CONVERSION_NOTES.md` for the detailed comparison. Every equation, definition, and the section 2.6 subsection ordering (2.6.1 through 2.6.9) match the published manual exactly.
7. The site was served locally with `mkdocs serve` and screenshotted with a
   headless Chromium (Playwright) during the original single-chapter pilot — see `screenshot_section_2.1.png` and
   `screenshot_section_2.6.png` in the repo root. Equations render as
   properly typeset math (fractions, matrices, tensor operators, numbered
   equations with working anchors) with no raw LaTeX source visible on the
   page.
8. **Studio Manual pilot (Chapters 1–2) and `navigation.tabs` addition:** `python3 build.py &&
   mkdocs build --strict` — exit code 0, zero `WARNING`-level messages, run against both manuals together.
   The leftover-artifact grep from item 2 was re-run over all of `docs/` (both `docs/theory/` and
   `docs/studio/`) — zero matches. The built HTML (`site/index.html`) was checked for `md-tabs__link`
   elements confirming exactly two tabs render ("Theory", "Studio"). Two real converter gaps were found and
   fixed against this manual's actual content (not present in the Theory Manual's source, so never
   previously exercised): a `Wrap`-figure inset (LaTeX's `wrapfig`) had no renderer and was falling through
   to `UNHANDLED INSET`, now aliased to the existing `Float figure` renderer; and a whitespace-normalization
   regex intended to strip a spurious space before sentence-ending punctuation was also stripping the
   genuine space before a literal file-extension token (`"the .xplt file extension"` was rendering as
   `"the.xplt..."`), fixed with a negative lookahead so it only strips a space before punctuation *not*
   immediately followed by a word character.
9. **Studio Manual widened from the 2-chapter pilot to the complete manual (all 20 chapters plus
   Appendices A and B, 117 sections):** `python3 build.py && mkdocs build --strict` — exit code 0, zero
   `WARNING`-level messages. The leftover-artifact grep — zero matches across all 117 Studio Manual
   sections plus all 64 Theory Manual sections. Every section's `needs_review` entries were scanned and
   confirmed to be only the two routine, expected categories (figure-fetch placeholders, and — before every
   chapter was converted — forward references into not-yet-converted chapters); zero unexpected entries
   remained after the converter fixes below. A broad spot-check read roughly 15 sections spanning materials,
   contact, post-processing, mesh data, Python scripting, and both appendices for rendering quality beyond
   what the automated checks catch. Ten further real converter gaps were found and fixed this pass — see
   `CONVERSION_NOTES_STUDIO.md` for the complete list — the most significant being a content-loss bug where
   a table wrapped in a `\begin_inset Float table` (as opposed to the already-handled `Float figure`) was
   silently dropped entirely (caption and anchor still rendered, but the table itself vanished with no
   `needs_review` flag), and a formatting-nesting bug — also present in some pre-existing Theory Manual
   output — where LyX source that closes character-formatting markers out of LIFO order (e.g. closing
   `\series bold` while `\emph on`, opened after it, is still active) produced invalid Markdown nesting;
   fixed by replacing four independent boolean flags with an explicit open-marker stack.
