The coupled Mooney-Rivlin material describes an unconstrained formulation of the Mooney-Rivlin material. The material type for this material is `coupled Mooney-Rivlin`.

The strain-energy function is given by the following expression.

\[
W=c_{1}\left(I_{1}-3\right)+c_{2}\left(I_{2}-3\right)-2\left(c_{1}+2c_{2}\right)\ln J+\frac{k}{2}\left(\ln J\right)^{2}
\]

Here, $I_{1}$ and $I_{2}$ are the first and second invariants of the right Cauchy-Green deformation tensor $\mathbf{C}$ and $J$ is the determinant of the deformation gradient tensor.

This material model uses a standard displacement-based element formulation, so care must be taken when modeling materials with nearly-incompressible material behavior to avoid element locking. For (nearly-) incompressible materials, use the Mooney-Rivlin material described in Section [Mooney-Rivlin](solid_material_mooney-rivlin.md).

_Example:_
```xml
<material id="1" type="coupled Mooney-Rivlin">
  <c1>10.0</c1>
  <c2>1.0</c2>
  <k>100.0</k>
</material>
```