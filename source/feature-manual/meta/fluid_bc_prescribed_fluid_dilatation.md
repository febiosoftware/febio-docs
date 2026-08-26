The `prescribed fluid dilatation` boundary condition can be used to prescribe the fluid dilatation $e^{f}$ on the boundary of a fluid, fluid-FSI or fluid-solutes material.

If the `relative` flag is set to 1, then the value is relative with respect to the current position of the node at the time the boundary condition becomes active. This only has an effect in multi-step analyses. 

```
<bc type="prescribed fluid dilatation" node_set="set1">
  <value lc="1">-1e-8</value>
  <relative>0</relative>
<bc>
```

Although the `prescribed fluid dilatation` boundary condition with a value of zero can also be used to fix the effective fluid pressure, the user should use the [zero fluid dilatation](fluid_bc_zero_fluid_dilatation.md) boundary condition whenever possible, since this option causes the equation corresponding to that degree of freedom to be removed from the linear system of equations. This results in fewer equations that need to be solved for and thus reduces the run time of the FE analysis.