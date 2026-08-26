The prescribed concentration boundary condition can be used to prescribe the value of the effective solute concentration $\tilde{c}$ in a multiphasic or fluid-solutes analysis.

If the `relative` flag is set to 1, then the value is relative with respect to the current effective solute concentration at the time the boundary condition becomes active. This only has an effect in multi-step analyses. 

```
<bc type="prescribed concentration" node_set="set1">
  <dof>c1</dof>
  <value lc="1">1.0</value>
  <relative>0</relative>
<bc>
```

Although the `prescribed concentration element` with a value of zero can also be used to fix that degree of freedom, the user should use the [zero concentration boundary](solute_bc_zero_concentration.md) condition whenever possible, since this option causes the equation corresponding to the constrained degree of freedom to be removed from the linear system of equations. This results in fewer equations that need to be solved for and thus reduces the run time of the FE analysis.