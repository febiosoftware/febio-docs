# matching_osm_coef

**Module:** multiphasic

**Category:** bc

**Type string:** `"matching_osm_coef"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `ambient_pressure` | ambient_pressure | 0 | $\in \mathbb{R}$ |  |
| `ambient_osmolarity` | ambient_osmolarity | 0 | $\in \mathbb{R}$ |  |
| `shell_bottom` | shell_bottom | false | $\{0, 1\}$ |  |


## Description

The `matching_osm_coef` boundary condition is a surface boundary condition that imposes the same osmotic coefficient in the bath as in the multiphasic material bounded by that surface. 

_Example:_
```xml
<bc type="matching_osm_coeff">
  <ambient_pressure>1</ambient_pressure>
  <ambient_osmolarity>1e-3</ambient_osmolarity>
  <shell_bottom>0</shell_bottom>
</bc>
```
