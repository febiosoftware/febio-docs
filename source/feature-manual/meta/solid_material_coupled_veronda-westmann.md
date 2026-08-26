The material type for the coupled Veronda-Westmann material is `coupled Veronda-Westmann`.

The coupled Veronda-Westmann material is an unconstrained formulation of the Veronda-Westmann material and is defined by the following strain-energy function.

\[
W=c_{1}\left(e^{c_{2}\left(I_{1}-3\right)}-1\right)-\frac{c_{1}c_{2}}{2}\left(I_{2}-3\right)+\frac{\lambda}{2}\left(\ln J\right)^{2}
\]

Here, $I_{1}$ and $I_{2}$ are the first and second invariants of the right Cauchy-Green deformation tensor $\mathbf{C}$ and $J$ is the determinant of the deformation gradient tensor.

This material model uses a standard displacement-based element formulation, so care must be taken when modeling materials with nearly-incompressible material behavior to avoid element locking. For (nearly-) incompressible materials, use the Veronda-Westmann material described in Section [Veronda-Westmann](solid_material_veronda-westmann.md).

_Example:_
```xml
<material id="1" type="coupled Veronda-Westmann">
  <c1>10.0</c1>
  <c2>1.0</c2>
  <k>100.0</k>
</material>
```