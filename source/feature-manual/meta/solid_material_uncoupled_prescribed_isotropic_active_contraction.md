The material type for prescribed isotropic active contraction, in an uncoupled solid mixture, is `uncoupled prescribed isotropic active contraction`. This material must be combined with a stable uncoupled material that acts as a passive matrix, using a `uncoupled solid mixture` container as described in [uncoupled solid mixture](solid_material_uncoupled_solid_mixture.md).

The active stress $\boldsymbol{\sigma}^{a}$ for this material is given by

\[
\boldsymbol{\sigma}^{a}=J^{-1}T_{0}\mathbf{B}\,.
\]

Note: If the solid material in the mixture is (nearly) incompressible, this isotropic contraction will cause no change in the deformation.

_Example:_

Isotropic contraction in a mixture containing a Mooney-Rivlin solid.

```xml
<material id="1" type="uncoupled solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="Mooney-Rivlin">
    <c1>1.0</c1>
    <c2>0</c2>
    <k>5.0</k>
  </solid>
  <solid type="prescribed isotropic active contraction uncoupled">
    <T0 lc="2">1</T0>
  </solid>
</material>
```
