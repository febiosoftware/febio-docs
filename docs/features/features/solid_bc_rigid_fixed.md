# rigid_fixed

**Module:** solid

**Category:** bc

**Type string:** `"rigid_fixed"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `rb` | Rigid material | -1 | $\in \mathbb{Z}$ |  |
| `Rx_dof` | X-displacement | false | $\{0, 1\}$ |  |
| `Ry_dof` | Y-displacement | false | $\{0, 1\}$ |  |
| `Rz_dof` | Z-displacement | false | $\{0, 1\}$ |  |
| `Ru_dof` | X-rotation | false | $\{0, 1\}$ |  |
| `Rv_dof` | Y-rotation | false | $\{0, 1\}$ |  |
| `Rw_dof` | Z-rotation | false | $\{0, 1\}$ |  |


## Description

The `rigid_fixed` rigid constraint fixes one or multiple rigid degrees of freedom.

The name of the rigid material is defined in the `Material` section. The referenced material must be a "rigid body" material. 

The following example fixes the displacement degrees of freedom. 

```
<rigid_bc type="rigid_fixed">
  <rb>RigidMaterial1</rb>
  <Rx_dof>1</Rx_dof>
  <Ry_dof>1</Ry_dof>
  <Rz_dof>1</Rz_dof>
</rigid_bc>
```

