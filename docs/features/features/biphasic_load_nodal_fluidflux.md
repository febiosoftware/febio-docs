# nodal fluidflux

**Module:** biphasic

**Category:** load

**Type string:** `"nodal fluidflux"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `relative` | relative | false | $\{0, 1\}$ |  |
| `value` | value | 0 | $\in \mathbb{R}$ |  |


## Description

The `nodal fluidflux` load implements an equivalent nodal force load. This load will be applied directly to the load vector of the system.

```
<nodal_load type="nodal fluidflux" node_set="set1">
  <value lc="1">1</value>
</nodal_load>
```

