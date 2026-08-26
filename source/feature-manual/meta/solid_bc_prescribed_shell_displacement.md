The `prescribed shell displacement` boundary condition can be used to prescribe the value of the nodal back-displacement degrees of freedom of a shell.

If the `relative` flag is set to 1, then the value is relative with respect to the current position of the node at the time the boundary condition becomes active. This only has an effect in multi-step analyses. 

```
<bc type="prescribed shell displacement" node_set="set1">
  <dof>sx</dof>
  <value lc="1">1.0</value>
  <relative>0</relative>
<bc>
```

Although the `prescribe shell displacement` element with a value of zero can also be used to fix a certain nodal degree of freedom, the user should use the [zero shell displacement](solid_bc_zero_shell_displacement.md) boundary condition whenever possible, since this option causes the equation corresponding to the constrained degree of freedom to be removed from the linear system of equations. This results in fewer equations that need to be solved for and thus reduces the run time of the FE analysis.