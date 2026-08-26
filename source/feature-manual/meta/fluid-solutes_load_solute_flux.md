In fluid-solutes analyses the molar flux of solute \iota , given by the vector $\mathbf{j}^{\iota}=c^{\iota}\left(\mathbf{v}^{\iota}-\mathbf{v}^{f}\right)$, is evaluated relative to the solvent (fluid); it only includes a diffusive contribution relative to the solvent. Since solute viscosity is not explicitly modeled, the tangential component of $\mathbf{j}^{\iota}$ on a boundary surface may not be prescribed. Only the normal component of the relative solute flux, $j_{n}^{\iota}=\mathbf{j}^{\iota}\cdot\mathbf{n}$, represents a natural boundary condition. Since a fluid-solutes mixture may contain electrically charged solutes, the solute flux that must be prescribed as a boundary condition is the effective solute flux $\tilde{j}_{n}^{\iota}=j_{n}^{\iota}+\sum_{\gamma}z^{\gamma}j_{n}^{\gamma}$. To prescribe a value for $\tilde{j}_{n}^{\iota}$ on a surface, use:

```
<surface_load type="solute flux" surface="surface1">
  <flux lc="1">1.0</flux>
  <solute_id>solute_name</solute_id>
</surface_load>
```

The parameter `solute_id` specifies to which solute this flux condition applies, referencing the corresponding list of solute names in the `Globals` section.

The `flux` element defines the flux magnitude. The optional attribute `lc` defines a load controller for the normal flux evolution. If omitted a constant flux is applied.