# cg

**Module:** core

**Category:** linearsolver

**Type string:** `"cg"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `print_level` | print_level | 0 | $\in \mathbb{Z}$ |  |
| `tol` | tol | 1e-05 | $\in \mathbb{R}$ |  |
| `max_iter` | max_iter | 0 | $\in \mathbb{Z}$ |  |
| `fail_max_iters` | fail_max_iters | true | $\{0, 1\}$ |  |
| `pc_left` | pc_left |  | N/A |  |


## Description

This iterative linear solver, from the MKL library, implements the Conjugate Gradient algorithm, which is an efficient Krylov-based iterative solution strategy for symmetric systems. It requires several configuration parameters, listed above, and only works with symmetric matrices. In the table below, N refers to the number of equations.

