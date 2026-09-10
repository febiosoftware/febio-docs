window.MathJax = {
  tex: {
    tags: 'ams',
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    // The FEBio Theory Manual LyX source defines a handful of custom
    // LaTeX operators in its document preamble (\newcommand{\tr}{...}
    // etc., see FEBio_Theory_Manual.lyx lines ~104-158). The Feature
    // Manual has no such preamble macros, so this `macros` block is an
    // intentional addition beyond the Feature Manual's baseline config,
    // needed so MathJax can render these operators instead of leaving
    // raw command names on the page. \obslash has no macro definition
    // anywhere in the LyX source (a genuine gap in the original document,
    // not introduced by this converter). Visual comparison against the
    // published manual confirmed it should render as U+29B8 CIRCLED
    // REVERSE SOLIDUS (a backslash-in-a-circle, the mirror image of
    // \oslash's U+2298 CIRCLED DIVISION SLASH) -- consistent with its use
    // alongside \oslash as its "conjugate" (X-transposed) counterpart in
    // eqs. 17-24; see CONVERSION_NOTES.md.
    macros: {
      tr: '\\operatorname{tr}',
      dev: '\\operatorname{dev}',
      Dev: '\\operatorname{Dev}',
      grad: '\\operatorname{grad}',
      Grad: '\\operatorname{Grad}',
      divg: '\\operatorname{div}',
      Divg: '\\operatorname{Div}',
      Ei: '\\operatorname{Ei}',
      cay: '\\operatorname{cay}',
      rot: '\\operatorname{rot}',
      obslash: '\\mathbin{\\unicode{x29B8}}',
      // \Square has no macro definition anywhere in the LyX source either
      // (same gap class as \obslash above) -- used in section 4.1 eq. 374
      // and the sentence right after it to denote "the biunit cube" (the
      // reference/master isoparametric element domain for Gauss-quadrature
      // integration). Not a real amsmath/amssymb command (which only
      // define the lowercase \square/\Box), so aliased to \square, the
      // standard hollow-square glyph for this exact usage in FEM notation.
      Square: '\\square',
      // \mbox is plain-TeX/LaTeX only; MathJax's default macro set does
      // not define it. The LyX source uses \mbox{...} in a handful of
      // places (section 2.1 eq. 11 "\mbox{\thinspace and\thinspace}";
      // also \mbox{\dot{...}}, \mbox{grad}, \mbox{div}, \mbox{M} in later
      // sections), mixing literal text with nested math macros like
      // \dot{} and \thinspace. Real LaTeX \mbox switches to horizontal
      // (text) mode but macros are still expanded textually beforehand;
      // MathJax's \text{} does not expand nested macros at all, so
      // aliasing \mbox to \text{} would leave literal "\thinspace"/"\dot{}"
      // command names on the page. \mathrm{} keeps the argument in math
      // mode -- so nested macros like \dot{} and \thinspace still expand
      // -- while switching the font to upright/roman, giving correct
      // rendering for both the macro-nesting cases and the plain-word
      // cases ("and", "grad", "div", "M") in one alias.
      mbox: ['\\mathrm{#1}', 1],
      thinspace: '\\,',
      // Chapter 7 (Contact and Coupling) defines 23 of its own local
      // shorthand macros via LyX Math Macro insets (\newcommand{\no}{...}
      // etc., BFSI contact notation), rendered nowhere else in the
      // document. MathJax's macros config has no per-chapter/per-page
      // scoping, so -- same as the \tr/\dev/etc. set above -- these are
      // added globally; a short generic-looking name like \no or \so is
      // only ever invoked with a leading backslash (a LaTeX macro
      // command), so it can't collide with the plain English words "no"/
      // "so" appearing as ordinary prose text elsewhere. It *could*
      // collide with an unrelated future chapter's own local macro
      // reusing one of these same short names for something different --
      // worth rechecking if that ever happens.
      mueff: '\\mu_{\\text{eff}}',
      mueq: '\\mu_{\\text{eq}}',
      mumin: '\\mu_{\\text{min}}',
      no: '\\mathbf{\\mathbf{n}}^{(1)}',
      so: '\\mathbf{s}^{(1)}',
      jeta: 'J_{\\eta}^{(1)}',
      wn: 'w_{n}^{(1)}',
      jn: 'j_{n}^{(1)}',
      Na: 'N_{a}^{(1)}',
      Nb: 'N_{b}^{(2)}',
      Nc: 'N_{c}^{(1)}',
      Nd: 'N_{d}^{(2)}',
      mc: '\\bar{\\mathbf{m}}_{c}^{(1)}',
      mb: '\\bar{\\mathbf{m}}_{b}^{(2)}',
      Mb: '\\bar{\\mathbf{M}}_{b}^{(2)}',
      Mc: '\\bar{\\mathbf{M}}_{c}^{(1)}',
      Ac: '\\mathbf{A}_{c}^{(1)}',
      No: '\\mathbf{N}^{(1)}',
      Nbo: '\\mathbf{\\bar{\\mathbf{N}}}^{(1)}',
      Nt: '\\tilde{\\mathbf{\\mathbf{N}}}^{(1)}',
      So: '\\mathbf{\\mathbf{S}}^{(1)}',
      Sb: '\\mathbf{\\bar{\\mathbf{S}}}^{(1)}',
      Nh: '\\hat{\\mathbf{N}}^{(1)}'
    }
  },
  startup: {
    // Equation anchors (id="mjx-eqn:<label>") are only added to the DOM
    // once MathJax finishes typesetting a labeled \begin{equation}, which
    // happens *after* the browser's own initial "scroll to #fragment on
    // page load" attempt has already run and failed (the anchor didn't
    // exist yet). This matters here because cross-section equation
    // references (e.g. section 2.6 linking to an equation defined in
    // section 2.5) are resolved at build time to real links landing on
    // exactly this kind of anchor -- see EQ_LABEL_REGISTRY in
    // tools/lyx2md.py. Without this, following such a link lands on the
    // right page but not scrolled to the right equation. Re-attempting
    // the scroll after typesetting completes is MathJax's documented
    // pattern for this.
    pageReady: () => {
      return MathJax.startup.defaultPageReady().then(() => {
        if (location.hash) {
          const el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
          if (el) el.scrollIntoView();
        }
      });
    }
  }
};
