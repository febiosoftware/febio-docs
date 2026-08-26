This surface load can be prescribed on a multiphasic boundary where a natural solute flux is desired. On this boundary, the solute is convected with the solvent according to $j_{n}=cw_{n}$. The implication of this surface load is that there is no diffusive hindrance to solute transport on the external side of the boundary. Here, $c$ is the average solute concentration and $\mathbf{w}$ is the average solvent volumetric flux in the finite element connected to the boundary face on which this surface load is prescribed. The normal solvent flux $w_{n}$ is evaluated as $\mathbf{w}\cdot\mathbf{n}$ using the normal $\mathbf{n}$ on the boundary. To prescribe a solute natural flux on a surface, use:

```
<surface_load type="solute natural flux" surface="surface1">
  <solute_id>solute_name</solute_id>
  <shell_bottom>0</shell_bottom>
  <update>0</update>
</surface_load>
```

The parameter `solute_id` specifies to which solute this flux condition applies, referencing the corresponding list of solute names in the `Globals` section. The parameter `update` is a boolean flag (0=false, 1=true, default is false) which, when set to true, initializes the effective solute concentration of surface nodes to the average value of concentrations within the underlying elements, at each iteration. You may set this flag to true when the iterative numerical solution fails to converge. This surface load is only needed for biphasic-solute and multiphasic analyses, since $\tilde{j}_{n}^{\iota}=0$ is the natural boundary condition for fluid-solutes analyses.