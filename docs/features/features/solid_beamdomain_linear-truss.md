# linear-truss

**Module:** solid

**Category:** beamdomain

**Type string:** `"linear-truss"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `cross_sectional_area` | cross_sectional_area | 0 | $\in \mathbb{R}$ |  |


## Description

The `linear-truss` domain is used for modeling linear trusses. It requires the `linear truss` material. 

This domain uses the Kirchhoff stress and the logarithmic strain to construct the internal forces. 

\[
    \tau = E \, \log \left( \lambda \right)
\]

where $\lambda = L_t / L_0$ is the stretch in the truss. 
