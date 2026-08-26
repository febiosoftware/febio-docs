The prescribed fluid pressure boundary condition can be used to prescribe the effective fluid pressure $\tilde{p}$ on the boundary of a biphasic or multiphasic material.

If the `relative` flag is set to 1, then the value is relative with respect to the current position of the node at the time the boundary condition becomes active. This only has an effect in multi-step analyses. 

```
<bc type="prescribed fluid pressure" node_set="set1">
  <value lc="1">1.0</value>
  <relative>0</relative>
<bc>
```

Although the `prescribed fluid pressure` boundary condition with a value of zero can also be used to fix the effective fluid pressure, the user should use the [zero fluid pressure](biphasic_bc_zero_fluid_pressure.md) boundary condition whenever possible, since this option causes the equation corresponding to that degree of freedom to be removed from the linear system of equations. This results in fewer equations that need to be solved for and thus reduces the run time of the FE analysis.