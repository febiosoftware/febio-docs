# linear truss

**Module:** solid

**Category:** material

**Type string:** `"linear truss"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\gt 0$ |  |
| `E` | E | 0 | $\gt 0$ | P |
| `v` | v | 0.5 | $[-1, 0.5]$ |  |


## Description

The `linear-truss` material defines the material properties for a `linear-truss` domain. It is currently the only material that can be assigned to a linear-truss domain. 

Note that in the current implementation the Poisson's ratio `v` parameter is not used since the linear truss is assumed to be incompressible (i.e. $\nu=0.5$). 

