# velocity

**Module:** solid

**Category:** ic

**Type string:** `"velocity"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `value` | value | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | L/t |


## Description

The `velocity` initial condition can be used to set the initial velocity for a dynamic solid-mechanics analysis. 

_Example:_
```xml
<ic type="velocity" node_set="set1">
  <value>1.0,0.0,0.0</value>
</ic>
```
