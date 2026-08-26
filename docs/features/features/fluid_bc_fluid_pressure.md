# fluid pressure

**Module:** fluid

**Category:** bc

**Type string:** `"fluid pressure"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `pressure` | fluid pressure | 0 | $\in \mathbb{R}$ | P |


## Description

To set the actual fluid pressure p in a fluid analysis use the `fluid pressure` boundary condition.

```
<bc type="fluid pressure" surface="FluidPressure1">
  <pressure lc="1">100</pressure>
</bc>
```

The optional `lc` attribute associates a load controller that multiplies the value of `pressure`. The surface must be defined in the `Mesh` section.

