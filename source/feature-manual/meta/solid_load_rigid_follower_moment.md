The `rigid_follower_moment` load applies a moment in the local rigid body coordinate system. The direction of the moment in global coordinates therefore depends on orientation of the rigid body.

The `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the `Material` section.

The following example applies a moment about the x-axis. 

```
<rigid_load type="rigid_follower_moment">
  <rb>rigid</rb>
  <moment>100,0,0</force>
</rigid_load>
```