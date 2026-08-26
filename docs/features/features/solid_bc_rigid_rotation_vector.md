# rigid_rotation_vector

**Module:** solid

**Category:** bc

**Type string:** `"rigid_rotation_vector"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `rb` | Rigid material | -1 | $\in \mathbb{Z}$ |  |
| `vx` | vx | 0 | $\in \mathbb{R}$ | r |
| `vy` | vy | 0 | $\in \mathbb{R}$ | r |
| `vz` | vz | 0 | $\in \mathbb{R}$ | r |


## Description

The `rigid_rotation_vector` constraint allows the user to prescribe the rotation of a rigid body using a rotation vector. In essence, this combines the effect of using three separate rigid rotation constraints, one for each component of the rotation vector, and thus might be a more convenient choice if the rotation of the rigid body is fully prescribed. 

The `rb` parameter is the name attribute assigned to the corresponding rigid body material as defined in the Material section.

The following example prescribes a rotation around the z-axis using a load controller. 

```
<rigid_bc type="rigid_rotation_vector">
  <rb>rigid</rb>
  <vx>0</vx>
  <vy>0</vy>
  <vz lc="1">3.14</vz>
</rigid_bc>
```
