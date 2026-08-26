In a fluid-solutes analysis this surface load checks for the presence of solvent (fluid) backflow, i.e., when $v_{n}^{f}=\mathbf{v}^{f}\cdot\mathbf{n}$ is negative. When this condition is encountered, the effective concentration of the selected solute (solute_id) is set to its converged value from the previous time step. Otherwise, the natural boundary condition $\tilde{j}_{n}=0$ (zero diffusive solute flux relative to the solvent) prevails.

```
<surface_load type="solute backflow stabilization" surface="surface1">
	<solute_id>neutral</solute_id>
</surface_load>
```