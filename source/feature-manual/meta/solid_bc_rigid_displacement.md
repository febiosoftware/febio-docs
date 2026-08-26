The `rigid_displacement` constraint prescribes the value of a rigid displacement degree of freedom.

The `rb` parameter is the name attribute assigned to the corresponding rigid body material as defined in the Material section.

The values allowed for the `dof` parameter are: `x`, `y`, or `z`. 

If the `relative` flag is set, the value is taken relative to the dof value at the start of the step.

The following example prescribes the x-displacement degree of freedom. 

```
<rigid_bc type="rigid_displacement">
  <rb>rigid</rb>
  <dof>x</dof>
  <value lc="1">3.14</value>
</rigid_bc>
```