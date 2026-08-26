# rigid angular damper

**Module:** solid

**Category:** nlconstraint

**Type string:** `"rigid angular damper"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `body_a` | body_a | -842150451 | $\in \mathbb{Z}$ |  |
| `body_b` | body_b | -842150451 | $\in \mathbb{Z}$ |  |
| `c` | c | 0 | $\in \mathbb{R}$ |  |


## Description

The rigid angular damper applies an angular damper that connects two rigid bodies $a$ and $b$.

_Example:_
```xml
<rigid_connector type="rigid angular damper">
  <body_a>1</body_a>
  <body_b>2</body_b>
  <c>1e-3</c>
</rigid_connector>
```

