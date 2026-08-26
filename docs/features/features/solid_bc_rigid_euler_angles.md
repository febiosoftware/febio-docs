# rigid_euler_angles

**Module:** solid

**Category:** bc

**Type string:** `"rigid_euler_angles"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `rb` | Rigid material | -1 | $\in \mathbb{Z}$ |  |
| `convention` | convention | 0 | $[0, 0]$ |  |
| `Ex` | Ex | 0 | $\in \mathbb{R}$ | d |
| `Ey` | Ey | 0 | $\in \mathbb{R}$ | d |
| `Ez` | Ez | 0 | $\in \mathbb{R}$ | d |


## Description

The `rigid_euler_angles` constraint allows the user to prescribe the rotation of a rigid body using three Euler angles. 

The `rb` parameter is the name attribute assigned to the corresponding rigid body material as defined in the Material section.

The following example prescribes a rotation around the z-axis using a load controller. 

```
<rigid_bc type="rigid_euler_angles">
  <rb>rigid</rb>
  <Ex>0</Ex>
  <Ey>0</Ey>
  <Ez lc="1">180.0</Ez>
</rigid_bc>
```
