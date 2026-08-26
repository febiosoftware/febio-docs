# prescribed fluid velocity

**Module:** fluid

**Category:** bc

**Type string:** `"prescribed fluid velocity"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `dof` | dof | -1 | $\in \mathbb{Z}$ |  |
| `value` | value | 0 | $\in \mathbb{R}$ | L/t |
| `relative` | relative | false | $\{0, 1\}$ |  |


## Description

The `prescribed fluid velocity` boundary condition can be used to to prescribe the fluid velocity on the boundary of a fluid domain.

