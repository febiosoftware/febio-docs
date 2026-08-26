In a multiphasic mixture the nodal degree of freedom for fluid pressure represents the effective fluid pressure $\tilde{p}$, which is related to the actual fluid pressure $p$. One may assign the value of $p$ directly on a boundary, by using the `actual fluid pressure` boundary condition.

```
<bc surface="FluidPressure1" type="actual fluid pressure">
  <pressure>0</pressure>
  <shell_bottom>0</shell_bottom>
</bc>
```

This boundary condition evaluates $p$ from nodal values of $\tilde{p}$ on the surface, and using the average values of $\Phi$  and $c^{\alpha}$ at the integration points of the underlying element. This surface load is particularly useful when the effective solute concentrations $\tilde{c}^{\alpha}$ are not prescribed as boundary conditions on that surface, but evolve with the analysis solution. 

The `shell_bottom` boolean flag (0=false, 1=true) should be set to true when prescribing this pressure on the bottom of a multiphasic shell domain.Prescribe the actual fluid pressure in a multiphasic mixture.