In a fluid or fluid-FSI analysis, the Cauchy stress is given by $\boldsymbol{\sigma}=-p\mathbf{I}+\boldsymbol{\tau}$, where $p$ is the elastic pressure and $\boldsymbol{\tau}$ is the viscous stress. The fluid pressure surface load prescribes $p$ on a boundary surface.

```
<surface_load type="fluid pressure" surface="surface1">
  <pressure>0.05</pressure>
</surface_load>
```

This boundary condition internally solves for the fluid dilatation $e^{f}$ for the user-prescribed pressure p, using the user-selected equation of state. Then $e^{f}$ is prescribed as an essential boundary condition on the selected surface.