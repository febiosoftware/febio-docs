The material type for prescribed active contraction along a single direction (or fiber) in a solid mixture of unconstrained materials is `prescribed uniaxial active contraction`. This material must be combined with a stable compressible material that acts as a passive matrix, using a [solid mixture](solid_material_solid_mixture.md) container.

In the reference configuration, the fiber is oriented along the unit vector $\mathbf{e}_{1}$, where $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ are orthonormal basis vectors representing the local element coordinate system when specified, or else the global Cartesian coordinate system. The active stress $\boldsymbol{\sigma}^{a}$ for this material is given by

\[
\boldsymbol{\sigma}^{a}=J^{-1}T_{0}\mathbf{n}\otimes\mathbf{n}\,,
\]

where $\mathbf{n}=\mathbf{F}\cdot\mathbf{e}_{1}$ is the stretched fiber orientation in the current (deformed) configuration.

_Example:_

Uniaxial contraction along $\mathbf{e}_{1}$, in a mixture containing a neo-Hookean solid.
```xml
<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="neo-Hookean">
    <E>1.0</E>
    <v>0.3</v>
  </solid>
  <solid type="prescribed uniaxial active contraction">
    <T0 lc="2">1</T0>
    <mat_axis type="angles">
      <theta>0</theta>
      <phi>90</phi>
    </mat_axis>
  </solid>
</material>
```