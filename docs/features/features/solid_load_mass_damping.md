# mass damping

**Module:** solid

**Category:** load

**Type string:** `"mass damping"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `C` | C | 0 | $\in \mathbb{R}$ |  |


## Description

The `mass damping` body load applies a body force that is proportional to the linear momentum density $\mathbf{p}=\rho\mathbf{v}$, where $\rho$  is the material density and $\mathbf{v}$ the velocity. An additional scale factor can be used to control the strength of the force, $\mathbf{f}=C\mathbf{p}$.
