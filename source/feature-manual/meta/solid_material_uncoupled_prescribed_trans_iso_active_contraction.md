The material type for prescribed isotropic active contraction in a plane transverse to a given direction (or fiber), in an uncoupled solid mixture, is `uncoupled prescribed trans iso active contraction`. This material must be combined with a stable uncoupled material that acts as a passive matrix, using a `uncoupled solid mixture` container as described in [uncoupled solid mixture](solid_material_uncoupled_solid_mixture.md).

In the reference configuration, the fiber is oriented along the unit vector $\mathbf{e}_{1}, where \left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ are orthonormal basis vectors representing the local element coordinate system when specified, or else the global Cartesian coordinate system. The active stress $\boldsymbol{\sigma}^{a}$ for this material is given by

\[
\boldsymbol{\sigma}^{a}=J^{-1}T_{0}\left(\mathbf{B}-\mathbf{n}\otimes\mathbf{n}\right)\,,
\]

where $\mathbf{n}=\mathbf{F}\cdot\mathbf{e}_{1}$ is the stretched fiber orientation in the current (deformed) configuration and $\mathbf{B}=\mathbf{F}\cdot\mathbf{F}^{T}$ is the left Cauchy-Green tensor.

_Example:_

Isotropic contraction in plane transverse to $\mathbf{e}_{1}$, in a mixture containing a Mooney-Rivlin solid.

```xml
<material id="1" type="uncoupled solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="Mooney-Rivlin">
    <c1>1.0</c1>
    <c2>0</c2>
    <k>1000</k>
  </solid>
  <solid type="uncoupled prescribed trans iso active contraction">
    <T0 lc="2">1</T0>
    <mat_axis type="angles">
      <theta>0</theta>
      <phi>90</phi>
    </mat_axis>
  </solid>
</material>
```
