The `rigid_follower_force` load applies a force in the local rigid body coordinate system. The direction of the force in global coordinates therefore depends on orientation of the rigid body.

The `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the Material section.

The `insertion` parameter is the position in the reference coordinate system of the point where the force is applied. 

The `relative` flag indicates whether the applied value should be absolute or relative to the value at the end of the previous analysis step.

The following example applies a moment about the x-axis. 

```
<rigid_load type="rigid_follower_force">
  <rb>rigid</rb>
  <insertion>1,2,3</dofs>
  <force>100,0,0</force>
</rigid_load>
```