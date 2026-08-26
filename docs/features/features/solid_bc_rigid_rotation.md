# rigid_rotation

**Module:** solid

**Category:** bc

**Type string:** `"rigid_rotation"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `rb` | Rigid material | -1 | $\in \mathbb{Z}$ |  |
| `dof` | dof | -1 | $\in \mathbb{Z}$ |  |
| `value` | value | 0 | $\in \mathbb{R}$ | r |
| `relative` | relative | false | $\{0, 1\}$ |  |


## Description

The `rigid_rotation` constraint prescribes the value of a rigid rotational degree of freedom.

The `rb` parameter is the name attribute assigned to the corresponding rigid body material as defined in the Material section.

The values allowed for the `dof` parameter are: `Ru`, `Rv`, or `Rw`. 

If the `relative` flag is set, the value is taken relative to the dof value at the start of the step.

The following example prescribes a rotation around the x-axis. 

```
<rigid_bc type="rigid_rotation">
  <rb>rigid</rb>
  <dof>Ru</dof>
  <value lc="1">3.14</value>
</rigid_bc>
```
