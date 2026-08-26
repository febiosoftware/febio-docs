# Broyden

**Module:** core

**Category:** newtonstrategy

**Type string:** `"Broyden"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `max_ups` | max_ups | 10 | $\in \mathbb{Z}$ |  |
| `max_buffer_size` | max_buffer_size | 0 | $\ge 0$ |  |
| `cycle_buffer` | cycle_buffer | true | $\{0, 1\}$ |  |
| `cmax` | cmax | 100000 | $\ge 0$ |  |


## Description

The Broyden method is similar to BFGS, but works with both symmetric and non-symmetric matrices. Therefore, it is the recommended method for problems that generate a non-symmetric stiffness matrix, such as (some) contact formulations, biphasic, multi-phasic, fluid, fluid FSI.

The Broyden method calculates the global stiffness matrix at the beginning of each time step. For each iteration, a matrix update is then done. The maximum number of such updates is set with `max_ups`. When FEBio reaches this number, or if the solution diverges and diverge_reform is set to 1, it reforms the global stiffness matrix (that is, it recalculates it) and factorizes it, essentially taking a "full Newton" iteration. Then FEBio continues with Broyden iterations. The `max_refs` parameter is used to set the maximum of such reformations FEBio can do, before it fails the timestep. In that case, FEBio will either terminate or, if the auto-time stepper is enabled, retry with a smaller time step size.
