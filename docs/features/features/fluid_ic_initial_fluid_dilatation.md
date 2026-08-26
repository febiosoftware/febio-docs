# initial fluid dilatation

**Module:** fluid

**Category:** ic

**Type string:** `"initial fluid dilatation"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `value` | value | 0 | $\in \mathbb{R}$ |  |


## Description

The `initial fluid dilatation` initial condition can be used to set the initial value of the fluid dilatation in a fluid analysis.

_Example:_
```xml
<ic type="initial fluid dilatation" node_set="set1">
  <value>1e-8</value>
</ic>
```
