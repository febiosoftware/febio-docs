# rigid_follower_moment

**Module:** solid

**Category:** load

**Type string:** `"rigid_follower_moment"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `rb` | rb | -1 | $\in \mathbb{Z}$ |  |
| `moment` | moment | {0.000000,0.000000,0.000000} | $\in \mathbb{R}^3$ |  |


## Description

The `rigid_follower_moment` load applies a moment in the local rigid body coordinate system. The direction of the moment in global coordinates therefore depends on orientation of the rigid body.

The `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the `Material` section.

The following example applies a moment about the x-axis. 

```
<rigid_load type="rigid_follower_moment">
  <rb>rigid</rb>
  <moment>100,0,0</force>
</rigid_load>
```
