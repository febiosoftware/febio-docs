# force

**Module:** solid

**Category:** load

**Type string:** `"force"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `scale` | scale | 1 | $\in \mathbb{R}$ |  |
| `force` | force | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | F |
| `shell_bottom` | shell_bottom | false | $\{0, 1\}$ |  |


## Description

A surface force applies an equivalent uniform traction load to a surface. The direction of the force remains unchanged as the mesh deforms.

```
<surface_load type="force" surface="surface1">
  <scale lc="1">1.0</scale>
  <force>0,0,1</force>
</surface_load>
```

The force vector is determined by two quantities. The direction and magnitude is defined by the force element. In addition, the magnitude can be scaled using the scale element. An optional load curve can be defined for the scale element using the lc attribute. This allows the surface force to become time dependent. If the lc attribute is omitted a constant force is applied.
