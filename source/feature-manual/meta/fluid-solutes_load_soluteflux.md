In biphasic-solute and multiphasic analyses the molar flux of a solute $\iota$, given by the vector $\mathbf{j}^{\iota}=\varphi^{w}c^{\iota}\left(\mathbf{v}^{\iota}-\mathbf{v}^{s}\right)$, is evaluated relative to the solid matrix; it includes a diffusive component as well as a convective component contributed by the fluid flux $\mathbf{w}$ relative to the solid, see eq.[eq:bs-fluxes-w-j]. Since solute viscosity is not explicitly modeled, the tangential component of $\mathbf{j}^{\iota}$ on a boundary surface may not be prescribed. Only the normal component of the relative solute flux, $j_{n}^{\iota}=\mathbf{j}^{\iota}\cdot\mathbf{n}$, represents a natural boundary condition. Since a multiphasic mixture may contain electrically charged solutes, the solute flux that must be prescribed as a boundary condition is the effective solute flux $\tilde{j}_{n}^{\iota}=j_{n}^{\iota}+\sum_{\gamma}z^{\gamma}j_{n}^{\gamma}$, as explained in Section [subsec:Prescribed-Effective-Solute-Flux]. To prescribe a value for $\tilde{j}_{n}^{\iota}$ on a surface, use:

```
<surface_load type="soluteflux" surface="surface1">
  <flux lc="1">1.0</flux>
  <linear>0</linear>
  <solute_id>solute_name</solute_id>
  <shell_bottom>0</shell_bottom>
</surface_load>
```

The parameter `solute_id` specifies to which solute this flux condition applies, referencing the corresponding list of solute names in the `Globals` section.

The `flux` element defines the flux magnitude. The optional attribute `lc` defines a load controller for the normal flux evolution. If omitted a constant flux is applied.

When `linear` is set to 0 (default) it means that the flux matches the prescribed value even if the surface on which it is applied changes in area as it deforms. Therefore, the net molar flow rate across the surface changes with changes in area. This type of boundary condition is useful if the solute molar flux is known in the current configuration.

When `linear` is set to non-zero it means that the prescribed flux produces a molar flow rate based on the undeformed surface area in the reference configuration. Therefore, the flux in the current configuration does not match the prescribed value. This type of boundary condition is useful if the net molar flow rate across the surface is known. For example: Let $Q$ be the known molar flow rate (in units of moles per time [n/t]), let $A_{\mathrm{0}}$ be the surface area in the reference configuration (a constant). Using linear means that the user prescribes $Q/A_{\mathrm{0}}$ as the flux boundary condition (in units of moles per area per time $[n/L^{\mathrm{2}}\cdot t])$. However, regardless of the type, the solute molar flux saved in the output file has a normal component equal to $Q/A$, where $A$ is the area in the current configuration.

The `shell_bottom` tag should be set to 1 (true) when prescribing the flux on the bottom surface of a multiphasic shell.