# rigid spring

**Module:** solid

**Category:** nlconstraint

**Type string:** `"rigid spring"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `body_a` | body_a | -842150451 | $\in \mathbb{Z}$ |  |
| `body_b` | body_b | -842150451 | $\in \mathbb{Z}$ |  |
| `k` | k | 1 | $\in \mathbb{R}$ |  |
| `insertion_a` | insertion_a | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |
| `insertion_b` | insertion_b | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |
| `free_length` | free_length | 0 | $\in \mathbb{R}$ |  |


## Description

The `rigid spring` applies a linear spring that connects two rigid bodies $a$ and $b$ at arbitrary points (not necessarily nodes).

If the `free_length` parameter is zero, then the initial length of the spring, as defined by the two insertion points, is taken as the free length. 

_Example:_
```xml
<rigid_connector type="rigid spring">
  <body_a>1</body_a>
  <body_b>2</body_b>
  <insertion_a>0,0,1</insertion_a>
  <insertion_b>0,0,3</insertion_b>
  <k>1</k>
</rigid_connector>
```
