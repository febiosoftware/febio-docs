# rigid contractile force

**Module:** solid

**Category:** nlconstraint

**Type string:** `"rigid contractile force"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `body_a` | body_a | -842150451 | $\in \mathbb{Z}$ |  |
| `body_b` | body_b | -842150451 | $\in \mathbb{Z}$ |  |
| `f0` | f0 | 0 | $\in \mathbb{R}$ |  |
| `insertion_a` | insertion_a | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |
| `insertion_b` | insertion_b | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |


## Description

The `rigid contractile` force applies an actuator force between arbitrary points (not necessarily nodes) on two rigid bodies $a$ and $b$.

The `f0` parameter represents the actuator force (positive for contraction). Optionally, it may be associated with a load curve.

_Example:_
```xml
<rigid_connector type="rigid contractile force">
  <body_a>1</body_a>
  <body_b>2</body_b>
  <insertion_a>0,0,1</insertion_a>
  <insertion_b>0,0,3</insertion_b>
  <f0 lc="1">1</f0>
</rigid_connector>
```
