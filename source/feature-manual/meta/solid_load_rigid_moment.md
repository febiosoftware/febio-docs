The `rigid_moment` load applies a moment about a particular coordinate axis.

The 'rb' parameter is the "name" attribute assigned to the corresponding rigid body material as defined in the Material section.

The values allowed for the `dof` parameter are: `Ru`, `Rv`, `Rw`. 

The `relative` flag indicates whether the applied value should be absolute or relative to the value at the end of the previous analysis step.

The following example applies a moment about the x-axis. 
```
<rigid_load type="rigid_moment">
  <rb>rigid</rb>
  <dof>Ru</dofs>
  <value lc="1">3.14</value>
</rigid_load>
```