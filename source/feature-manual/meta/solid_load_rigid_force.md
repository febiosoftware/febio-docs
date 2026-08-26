The `rigid_force` load applies a load directly to the rigid degree of freedom.

The `rb` parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the `Material` section.

The values allowed for the dof parameter are: `Rx`, `Ry`, `Rz`. 

The `load_type` allows the following values:

1. 0 = a load (force/moment) is applied directly to the degree of freedom. 
2. 1 = a follower load applied is applied to the rigid body. The load is applied in the rigid body's coordinate system, so it rotates with the rigid body. This only works for Rx, Ry, Rz. 
3. 2 = target load. The load's value is ramped up from its initial value at the start of the step, and ramped up linearly to the value specified in the value parameter. 

The following example applies a force in the x-direction. 

```
<rigid_load type="rigid_force">
  <rb>1</rb>
  <dof>Rx</dofs>
  <value lc="1">3.14</value>
</rigid_load>
```