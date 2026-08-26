# fluid-FSI

**Module:** fluid-FSI

**Category:** solver

**Type string:** `"fluid-FSI"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `symmetric_stiffness` | matrix format | 0 | $[0, 3]$ |  |
| `equation_scheme` | equation_scheme | 0 | $[0, 1]$ |  |
| `equation_order` | equation_order | 0 | $[0, 2]$ |  |
| `optimize_bw` | optimize_bw | false | $\{0, 1\}$ |  |
| `lstol` | lstol | 0.9 | $\ge 0$ |  |
| `lsmin` | lsmin | 0.01 | $\ge 0$ |  |
| `lsiter` | lsiter | 5 | $\ge 0$ |  |
| `ls_check_jacobians` | ls_check_jacobians | false | $\{0, 1\}$ |  |
| `max_refs` | max_refs | 15 | $\ge 0$ |  |
| `check_zero_diagonal` | check_zero_diagonal | false | $\{0, 1\}$ |  |
| `zero_diagonal_tol` | zero_diagonal_tol | 0 | $\in \mathbb{R}$ |  |
| `force_partition` | force_partition | 0 | $\in \mathbb{Z}$ |  |
| `reform_each_time_step` | reform_each_time_step | true | $\{0, 1\}$ |  |
| `reform_augment` | reform_augment | false | $\{0, 1\}$ |  |
| `diverge_reform` | diverge_reform | true | $\{0, 1\}$ |  |
| `min_residual` | min_residual | 1e-20 | $\ge 0$ |  |
| `max_residual` | max_residual | 0 | $\ge 0$ |  |
| `dtol` | dtol | 0.001 | $\in \mathbb{R}$ |  |
| `vtol` | vtol | 0.001 | $\in \mathbb{R}$ |  |
| `ftol` | ftol | 0.001 | $\in \mathbb{R}$ |  |
| `etol` | etol | 0.01 | $\ge 0$ |  |
| `rtol` | rtol | 0.001 | $\ge 0$ |  |
| `rhoi` | rhoi | 0 | $\in \mathbb{R}$ |  |
| `predictor` | predictor | 0 | $\in \mathbb{Z}$ |  |
| `min_volume_ratio` | min_volume_ratio | 0 | $\in \mathbb{R}$ |  |
| `order` | order | 2 | $\in \mathbb{Z}$ |  |
| `qn_method` | Quasi-Newton method |  | N/A |  |
| `linear_solver` | linear_solver |  | N/A |  |


## Description

(No description provided)

