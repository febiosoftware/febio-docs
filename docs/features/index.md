# Preface

The **FEBio Feature Manual** is a reference for every feature currently available in FEBio: the
materials, boundary and initial conditions, loads, constraints, solvers, domains, and mesh tools you can
name in an FEBio input file. Each page gives a feature's type string, the module it belongs to, its full
parameter table, and — where one has been written — a description of what it does and how to use it.

It complements the [Theory](../theory/index.md) and [Studio](../studio/index.md) manuals: Theory covers
the mathematics behind the models, Studio covers the GUI, and this manual covers the features themselves
as you would configure them.

Use the **Features** tab above to browse by module, by feature category, or by output variable.

!!! important
    This manual is a work in progress. The feature list and parameter tables are complete and generated
    directly from FEBio itself, but not every feature has a written description yet.

## About this manual

- **Source** — `source/feature-manual/febio_features.json`, FEBio's own feature database, exported from
  FEBio Studio (**FEBio → FEBio Info → Export**). This is what supplies every feature's type string,
  module, category, and parameter table, so those are always in step with the FEBio release.
- **Descriptions** — `source/feature-manual/meta/`, one hand-authored Markdown fragment per page,
  spliced into that page's *Description* section. Features with no fragment show
  *(No description provided)*.
- **Generator** — `tools/features2md.py`, ported from the standalone
  [febio-feature-manual](https://github.com/febiosoftware/febio-feature-manual) repository so this
  manual is built from source alongside the other two on every site build.
- **Output variables** — the *Output* section lists the plot and log variables available for use in an
  input file's output section, with descriptions drawn from `meta/plotvars.csv` and `meta/logvars.csv`.
- **Febcode** — the *Febcode* section documents FEBio's embedded scripting language, a lighter-weight
  alternative to writing a plugin.

If you find any issues with this manual, please report them to <info@febio.org>.
