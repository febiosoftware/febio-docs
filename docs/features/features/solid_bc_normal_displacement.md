# normal displacement

**Module:** solid

**Category:** bc

**Type string:** `"normal displacement"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `scale` | scale | 0 | $\in \mathbb{R}$ |  |
| `surface_hint` | surface_hint | 0 | $\in \mathbb{Z}$ |  |
| `relative` | relative | false | $\{0, 1\}$ |  |


## Description

The `normal displacement` boundary condition prescribes the displacement of a node along the normal vector to the surface on which the node lies. 

\[
\boldsymbol{u}=s\boldsymbol{N}
\]

Here, $\boldsymbol{u}$ is the displacement vector, $\boldsymbol{N}$ is the normal to the surface in the reference configuration, and $s$ is a scale factor. 

Note that this boundary condition requires a `surface` attribute, instead of the `node_set` attribute.
