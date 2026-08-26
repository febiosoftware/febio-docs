#!/usr/bin/env python3
"""Convert FEBio's feature database (febio_features.json) to Markdown pages.

This is a port of the standalone febio-feature-manual repo's build.py
(github.com/febiosoftware/febio-feature-manual), adapted to this repo's
multi-manual pipeline. The content-generation logic -- class-id normalization,
module/class filtering, filename scheme, page template, plot/log variable
tables -- is carried over unchanged so pages stay byte-comparable with
upstream. Two things differ:

  1. It does not write mkdocs.yml. build.py owns the site nav for all three
     manuals, so instead this script writes a generic nested nav tree to
     --stats-out, in the same spirit as tools/lyx2md.py's stats sidecar.
  2. Output directories are created with os.makedirs(exist_ok=True). Upstream
     gitignores its generated docs/modules/*.md, so that directory is absent
     in a fresh clone and upstream's build.py crashes on it.

The prose for each page lives in --meta-dir as one Markdown fragment per page
(named exactly like the page it belongs to); it is spliced verbatim into that
page's "## Description" section. Features with no fragment render
"(No description provided)" and are recorded in the stats sidecar's
needs_review list.

Layout note: feature pages are written flat into <docs-root>/features/ with
their figs/ directory alongside them, mirroring upstream exactly. The meta
fragments contain relative sibling links ([x](other_page.md)) and figure
references (figs/Foo.png) that only resolve under that layout.

Usage:
    python3 tools/features2md.py --features-json PATH --meta-dir DIR \
            --docs-root DIR --nav-root PREFIX --stats-out PATH
"""

import argparse
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Modules whose features are not published in the manual.
SKIP_MODULES = {"thermo-fluid", "polar fluid"}

# Classes that get no pages of their own.
SKIP_CLASSES = {"surface", "datarecord"}

# Category labels that read badly when just .capitalize()'d.
CLASS_DISPLAY_OVERRIDES = {
    "bc": "Boundary conditions",
    "ic": "Initial conditions",
}


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--features-json", required=True,
                        help="Path to febio_features.json (exported from FEBio Studio).")
    parser.add_argument("--meta-dir", required=True,
                        help="Directory of hand-authored per-page description fragments.")
    parser.add_argument("--docs-root", required=True,
                        help="Directory to write the manual's pages into (e.g. docs/features).")
    parser.add_argument("--nav-root", required=True,
                        help="Path prefix for nav entries, relative to docs/ (e.g. 'features').")
    parser.add_argument("--stats-out", required=True,
                        help="Where to write the nav tree / totals JSON sidecar.")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()


def normalize_class_id(raw):
    """FEMaterialProp_ID -> materialprop (upstream's exact normalization)."""
    class_id = raw
    if class_id.endswith("_ID"):
        class_id = class_id[:-3]
    if class_id.startswith("FE"):
        class_id = class_id[2:]
    return class_id.lower()


def read_meta(meta_dir, filename, verbose, missing):
    """Return the hand-authored description fragment for a page, or ''."""
    try:
        with open(os.path.join(meta_dir, filename), mode="r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        if verbose:
            print(f"  WARNING: no description fragment for {filename}")
        missing.append(filename)
        return ""


def write_module_pages(data, meta_dir, docs_root, nav_root, verbose, missing):
    """Write docs/<root>/modules/module_<name>.md; return nav entries."""
    out_dir = os.path.join(docs_root, "modules")
    os.makedirs(out_dir, exist_ok=True)

    nav = []
    for module in data["modules"]:
        module_name = module["name"]
        clean_mod = module_name.replace(" ", "_").lower()
        filename = f"module_{clean_mod}.md"

        info = read_meta(meta_dir, filename, verbose, missing)
        if not info:
            info = module.get("info", "") or "(No description provided)"

        if verbose:
            print(f"  module: {module_name}")

        with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
            f.write(f"# {module_name} module\n\n")
            f.write("## Description\n\n")
            f.write(f"{info}\n")

        nav.append([module_name, f"{nav_root}/modules/{filename}"])

    return nav


def write_feature_pages(data, meta_dir, docs_root, nav_root, verbose, missing):
    """Write the feature pages; return (nav_tree, plot_variables, log_variables, count)."""
    out_dir = os.path.join(docs_root, "features")
    os.makedirs(out_dir, exist_ok=True)

    class_files = {}
    plot_variables = {}
    log_variables = {}
    count = 0

    for row in data["features"]:
        name = row["type_string"]
        class_id = normalize_class_id(row["super_class_id"])

        module_name = row["module"] or "core"
        if module_name.lower() in SKIP_MODULES:
            continue

        # plot/log classes become the Output tables rather than pages.
        if class_id.startswith("plot"):
            plot_variables[name] = (module_name, "")
            continue
        if class_id.startswith("log"):
            log_variables[name] = (module_name, "")
            continue

        if class_id in SKIP_CLASSES:
            continue

        clean_name = name.replace(" ", "_").lower()
        clean_class = class_id.replace(" ", "_").lower()
        clean_mod = module_name.replace(" ", "_").lower()
        filename = f"{clean_mod}_{clean_class}_{clean_name}.md"

        if verbose:
            print(f"  feature: {name} ({filename})")

        info = read_meta(meta_dir, filename, verbose, missing)

        with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
            f.write(f"# {name}\n\n")
            f.write(f"**Module:** {module_name}\n\n")
            f.write(f"**Category:** {class_id}\n\n")
            f.write(f'**Type string:** `"{name}"`\n\n')

            f.write("## Parameters\n\n")
            params = row["parameters"]
            if len(params) == 0:
                f.write("This feature has no parameters.\n")
            else:
                f.write("| Name | Description | Default | Range | Units |\n")
                f.write("|------|-------------|---------|-------|-------|\n")
                for p in params:
                    f.write(f"| `{p['name']}` | {p['description']} | {p['default']} "
                            f"| {p['range']} | {p['units']} |\n")

            f.write("\n\n## Description\n\n")
            f.write("(No description provided)\n\n" if info == "" else f"{info}\n")

        class_files.setdefault(class_id, []).append(
            [name, f"{nav_root}/features/{filename}"])
        count += 1

    nav = []
    for class_id in sorted(class_files):
        label = CLASS_DISPLAY_OVERRIDES.get(class_id, class_id.capitalize())
        nav.append([label, class_files[class_id]])

    return nav, plot_variables, log_variables, count


def join_csv_descriptions(csv_path, variables):
    """Fill in descriptions for plot/log variables from the meta CSV."""
    with open(csv_path, mode="r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) < 2:
                continue
            var_name = row[0].strip()
            if var_name in variables:
                variables[var_name] = (variables[var_name][0], row[1].strip())


def write_variable_table(path, heading, blurb, variables, missing_desc):
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(f"# {heading}\n\n")
        f.write(f"{blurb}\n\n")
        f.write("|variable | description|module|\n")
        f.write("|-------- | -----------|------|\n")
        for var, (module, desc) in variables.items():
            if desc == "":
                missing_desc.append(var)
            f.write(f"|`{var}` | {desc}|{module}|\n")


def main():
    args = parse_args()
    verbose = args.verbose

    print("Building FEBio Feature Manual...")
    if verbose:
        print(f"Reading {args.features_json}...")

    with open(args.features_json, mode="r", encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(args.docs_root, exist_ok=True)

    missing = []
    module_nav = write_module_pages(
        data, args.meta_dir, args.docs_root, args.nav_root, verbose, missing)
    feature_nav, plot_variables, log_variables, feature_count = write_feature_pages(
        data, args.meta_dir, args.docs_root, args.nav_root, verbose, missing)

    join_csv_descriptions(os.path.join(args.meta_dir, "plotvars.csv"), plot_variables)
    join_csv_descriptions(os.path.join(args.meta_dir, "logvars.csv"), log_variables)

    missing_vars = []
    write_variable_table(
        os.path.join(args.docs_root, "plotvars.md"), "Plot Variables",
        "The following plot variables are available in FEBio:",
        plot_variables, missing_vars)
    write_variable_table(
        os.path.join(args.docs_root, "logvars.md"), "Log Variables",
        "The following log variables are available in FEBio:",
        log_variables, missing_vars)

    nav = [
        ["Modules", module_nav],
        ["Features", feature_nav],
        ["Output", [
            ["Plot variables", f"{args.nav_root}/plotvars.md"],
            ["Log variables", f"{args.nav_root}/logvars.md"],
        ]],
        ["Febcode", f"{args.nav_root}/febcode.md"],
    ]

    stats = {
        "nav": nav,
        "totals": {
            "modules": len(module_nav),
            "categories": len(feature_nav),
            "features": feature_count,
            "plot_vars": len(plot_variables),
            "log_vars": len(log_variables),
            "missing_descriptions": len(missing),
            "vars_missing_descriptions": len(missing_vars),
        },
        "needs_review": {
            "pages_without_description": sorted(missing),
            "variables_without_description": sorted(missing_vars),
        },
    }

    with open(args.stats_out, mode="w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    t = stats["totals"]
    print(f"  wrote {t['features']} feature pages in {t['categories']} categories, "
          f"{t['modules']} module pages, "
          f"{t['plot_vars']} plot vars, {t['log_vars']} log vars.")
    print(f"  {t['missing_descriptions']} pages have no description fragment "
          f"(see {os.path.basename(args.stats_out)}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
