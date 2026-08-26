To fix the fluid dilatation $e^{f}$ in a fluid or fluid-FSI or fluid-solutes analysis, use the zero `fluid dilatation boundary` condition.

```
<bc node_set="set01" type="zero fluid dilatation"/>
```

Zero fluid dilatation is the same as setting the effective fluid pressure $\tilde{p}$ to zero in fluid analyses. If you want to set the actual fluid pressure p to some value (such as zero) in a fluid analysis, use the fluid pressure boundary condition [fluid-Pressure](fluid_bc_fluid_pressure.md).