In a biphasic mixture of intrinsically incompressible solid and fluid constituents, the $\mathbf{u}-p$ formulation adopted in FEBio implies that the normal component of the relative fluid flux is a natural boundary condition. If this boundary condition is not explicitly prescribed, the code automatically assumes that it is equal to zero. Therefore, biphasic boundaries are impermeable by default. (To implement a free-draining boundary, the fluid pressure nodal degrees of freedom should be set to zero.)

The flux of fluid relative to the solid matrix is given by the vector $\mathbf{w}$. Since viscosity is not explicitly modeled in a biphasic material, the tangential component of $\mathbf{w}$ on a boundary surface may not be prescribed. Only the normal component of the relative fluid flux, $w_{n}=\mathbf{w}\cdot\mathbf{n}$, represents a natural boundary condition. To prescribe a value for $w_{n}$ on a surface, use:

```xml
<surface_load type="fluidflux" surface="surf1">
  <flux lc="1">1.0</flux>
  <linear>0</linear>
  <mixture>0</mixture>
</surface_load>
```

The `flux` parameter defines the flux that will be applied to the surface. The optional parameter `lc` defines a loadcurve for the normal flux evolution. If omitted a constant fluid flux is applied.

When `linear` is set to zero (default) it means that the flux matches the prescribed value even if the surface on which it is applied changes in area as it deforms. Therefore, the net volumetric flow rate across the surface changes with changes in area. This type of boundary condition is useful if the fluid flux is known in the current configuration.

When `linear` is set to non-zero it means that the prescribed flux produces a volumetric flow rate based on the undeformed surface area in the reference configuration. Therefore, the flux in the current configuration does not match the prescribed value. This type of boundary condition is useful if the net volumetric flow rate across the surface is known. For example: Let $Q$ be the known volumetric flow rate, let $A_{\mathrm{0}}$ be the surface area in the reference configuration (a constant). Using `linear` means that the user prescribes $Q/A_{\mathrm{0}}$ as the flux boundary condition. (However, regardless of the type, the fluid flux saved in the output file has a normal component equal to $Q/A$, where $A$ is the area in current configuration.)

Prescribing $w_{n}$ on a free surface works only if the nodal displacements of the corresponding faces are also prescribed. If the nodal displacements are not known a priori, the proper boundary condition calls for prescribing the normal component of the mixture velocity, $v_{n}=\left(\mathbf{v}^{s}+\mathbf{w}\right)\cdot\mathbf{n}$. To prescribe the value of $v_{n}$ on a surface, use

```xml
<surface_load type="fluidflux" surface="surf1">
  <flux lc="1">1.0</flux>
  <linear>0</linear>
  <mixture>1</mixture>
</surface_load>
```

For example, this boundary condition may be used when modeling a permeation problem through a biphasic material, when the upstream fluid velocity is prescribed, $v_{n}=v_{0}$. If the upstream face is free, the companion boundary condition would be to let $t_{n}^{e}=0$ on that face as well.
