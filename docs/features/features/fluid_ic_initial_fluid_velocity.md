# initial fluid velocity

**Module:** fluid

**Category:** ic

**Type string:** `"initial fluid velocity"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `value` | value | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | L/t |


## Description

The `initial fluid velocity` initial condition can be used to set the initial velocity for a fluid mechanics analysis.

_Example:_
```xml
<ic type="initial fluid velocity" node_set="set1">
  <value>1.0,0.0,0.0</value>
</ic>
```
