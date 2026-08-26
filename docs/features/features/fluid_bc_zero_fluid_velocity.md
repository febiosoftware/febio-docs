# zero fluid velocity

**Module:** fluid

**Category:** bc

**Type string:** `"zero fluid velocity"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `wx_dof` | x-velocity | false | $\{0, 1\}$ |  |
| `wy_dof` | y-velocity | false | $\{0, 1\}$ |  |
| `wz_dof` | z-velocity | false | $\{0, 1\}$ |  |


## Description

The `zero fluid velocity` boundary condition sets all specified fluid velocity degrees of freedom on a boundary of the fluid domain to zero.

_Example:_

```xml
<bc type="zero fluid velocity" node_set="outer_surface">
    <wx_dof>1</wx_dof>
    <wy_dof>1</wy_dof>
    <wz_dof>1</wz_dof>
</bc>
```


