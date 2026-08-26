The material type for prescribed isotropic active contraction, in a solid mixture of unconstrained materials, is `prescribed isotropic active contraction`. This material must be combined with a stable compressible material that acts as a passive matrix, using a [solid mixture](solid_material_solid_mixture.md) container.

The active stress $\boldsymbol{\sigma}^{a}$ for this material is given by

\[
\boldsymbol{\sigma}^{a}=J^{-1}T_{0}\mathbf{B}\,.
\]

_Example:_

Isotropic contraction in a mixture containing a neo-Hookean solid.

```xml
<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="neo-Hookean">
    <E>1.0</E>
    <v>0</v>
  </solid>
  <solid type="prescribed isotropic active contraction">
    <T0 lc="2">1</T0>
  </solid>
</material>
```

