# pardiso

**Module:** core

**Category:** linearsolver

**Type string:** `"pardiso"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `print_condition_number` | print_condition_number | false | $\{0, 1\}$ |  |
| `precondition` | precondition | false | $\{0, 1\}$ |  |
| `msglvl` | msglvl | 0 | $\in \mathbb{Z}$ |  |


## Description

The Pardiso solver is an efficient sparse direct linear solver and is the default linear solver in FEBio. FEBio uses the implementation from the MKL library. It does not require any configuration parameters. It can take symmetric, unsymmetric, and structurally symmetric sparse matrix formats.
