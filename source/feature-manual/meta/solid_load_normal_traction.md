This load can be applied to biphasic, biphasic-solute, triphasic and multiphasic analyses. In a mixture of intrinsically incompressible solid and fluid constituents, the formulation adopted in FEBio implies that the total traction is a natural boundary condition ([FEBio Theory Manual](https://help.febio.org/docs/FEBioTheory-4-5/TM45-Section-3.2.html)). If this boundary condition is not explicitly prescribed, the code automatically assumes that it is equal to zero. Therefore, boundaries of mixtures are traction-free by default.

The mixture traction $\mathbf{t}$ is the traction vector corresponding to the mixture (or total) stress $\boldsymbol{\sigma}$; thus $\mathbf{t}=\boldsymbol{\sigma}\cdot\mathbf{n}$, where $\mathbf{n}$ is the outward unit normal to the boundary surface. Since $\boldsymbol{\sigma}=-p\mathbf{I}+\boldsymbol{\sigma}^{e}$, where $p$ is the fluid pressure and $\boldsymbol{\sigma}^{e}$ is the effective stress resulting from strains in the solid matrix, it is also possible to represent the total traction as $\mathbf{t}=-p\mathbf{n}+\mathbf{t}^{e}$, where $\mathbf{t}^{e}=\boldsymbol{\sigma}^{e}\cdot\mathbf{n}$ is the effective traction. Currently, FEBio allows the user to specify only the normal component of the traction, either $t_{n}=\mathbf{t}\cdot\mathbf{n}$ (the normal component of the mixture traction) or $t_{n}^{e}=\mathbf{t}^{e}\cdot\mathbf{n}$ (the normal component of the effective traction):

A mixture normal traction is defined by the surface_load element using normal_traction for the type attribute.

```
<surface_load type="normal_traction" surface="surface1">
  <traction [lc="1"]>1.0</traction>
  <effective>1</effective>
  <linear>0</linear>
</surface_load>
```

The `traction` parameter defines the magnitude of the traction force. The optional attribute `lc` defines a load controller that controls the time dependency of the traction force magnitude. If omitted a constant traction is applied.

The `effective` parameter defines whether the traction is applied as an effective traction or a total mixture traction.

The `linear` parameter defines whether the traction remains normal to the deformed surface or the reference surface. If set to true the traction remains normal to the reference surface. When false it defines a follower force that remains normal to the deformed surface.

The `surface` attribute defines the surface to which the traction is applied. It consists of child elements defining the individual surface facets.

Unlike the mixture and effective traction, the fluid pressure $p$ is a nodal variable (see [zero displacement](solid_bc_zero_displacement.md)). There may be common situations where the user must apply a combination of related fluid pressure and traction boundary conditions. For example, if a biphasic surface is subjected to a non-zero fluid pressure $p_{0}$, the corresponding boundary conditions are $p=p_{0}$ and $t_{n}=-p_{0}$ (or $t_{n}^{e}=0$). In FEBio, both boundary conditions must be applied. For example:

```
<Boundary>
  <prescribed bc="p" node_set="set1">
    <scale lc="1">1.0</scale>
  </prescribed>
  <surface_load type="normal_traction" surface="surf1">
    <traction lc="1">-1.0</traction>
    <effective>0</effective>
    <linear>0</linear>
  </surface_load>
</Boundary>
<LoadData>
  <loadcontroller id="1" type="loadcurve">
    <points>
      <loadpoint>0,0</loadpoint>
      <loadpoint>1,2.0</loadpoint>
    </points>
  </loadcurve>
</LoadData>
```