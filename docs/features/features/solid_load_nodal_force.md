# nodal_force

**Module:** solid

**Category:** load

**Type string:** `"nodal_force"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `relative` | relative | false | $\{0, 1\}$ |  |
| `value` | value | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | F |
| `shell_bottom` | shell_bottom | false | $\{0, 1\}$ |  |


## Description

This nodal load defines a force that is applied to each node in the node set. The value parameter sets the force vector. An optional load curve can be defined to scale the vector. 

```
<nodal_load type="nodal_force" node_set="set1">
  <value lc="1">1,0,0</scale>
</nodal_load>
```
