# shell velocity

**Module:** solid

**Category:** ic

**Type string:** `"shell velocity"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `value` | value | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |


## Description

The `shell velocity` initial condition can be used to set the initial velocity for the for the back-nodes of shells in a dynamic solid-mechanics analysis. 

_Example:_
```xml
<ic type="shell velocity" node_set="set1">
  <value>1.0,0.0,0.0</value>
</ic>
```
