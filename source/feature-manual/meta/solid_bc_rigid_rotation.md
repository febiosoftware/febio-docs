The `rigid_rotation` constraint prescribes the value of a rigid rotational degree of freedom.

The `rb` parameter is the name attribute assigned to the corresponding rigid body material as defined in the Material section.

The values allowed for the `dof` parameter are: `Ru`, `Rv`, or `Rw`. 

If the `relative` flag is set, the value is taken relative to the dof value at the start of the step.

The following example prescribes a rotation around the x-axis. 

```
<rigid_bc type="rigid_rotation">
  <rb>rigid</rb>
  <dof>Ru</dof>
  <value lc="1">3.14</value>
</rigid_bc>
```