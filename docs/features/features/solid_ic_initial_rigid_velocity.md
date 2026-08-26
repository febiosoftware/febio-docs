# initial_rigid_velocity

**Module:** solid

**Category:** ic

**Type string:** `"initial_rigid_velocity"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `rb` | Rigid material | -1 | $\in \mathbb{Z}$ |  |
| `value` | value | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ | L/t |


## Description

In dynamic analysis, the initial velocity of a rigid body can be set via the `initial_rigid_velocity` initial condition.

The `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the `Material` section.

The following example defines an initial velocity for a rigid body. 

```
<rigid_ic type="initial_rigid_velocity">
  <rb>rigid</rb>
  <value>1,0,0</value>
</rigid_ic>
```
