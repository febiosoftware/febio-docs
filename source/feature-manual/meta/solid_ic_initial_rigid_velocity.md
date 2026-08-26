In dynamic analysis, the initial velocity of a rigid body can be set via the `initial_rigid_velocity` initial condition.

The `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the `Material` section.

The following example defines an initial velocity for a rigid body. 

```
<rigid_ic type="initial_rigid_velocity">
  <rb>rigid</rb>
  <value>1,0,0</value>
</rigid_ic>
```