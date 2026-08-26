In dynamic analysis, the initial angular velocity of a rigid body can be set via the `initial_rigid_angular_velocity` rigid constraint.

This `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the Material section.

The following example defines an initial angular velocity for a rigid body. 

```
<rigid_ic type="initial_rigid_angular_velocity">
  <rb>rigid</rb>
  <value>1,0,0</value>
</rigid_ic>
```