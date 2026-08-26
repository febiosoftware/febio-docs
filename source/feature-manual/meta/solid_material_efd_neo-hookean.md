The material type for a Neo-Hookean material with an ellipsoidal continuous fiber distribution is `EFD neo-Hookean`.

The Cauchy stress for this material is given by,

\[
\boldsymbol{\sigma}=\boldsymbol{\sigma}_{NH}+\boldsymbol{\sigma}_{f}.
\]

Here, $\boldsymbol{\sigma}_{NH}$ is the stress from the Neo-Hookean basis (see [neo-Hookean](solid_material_neo-hookean.md)), and $\boldsymbol{\sigma}_{f}$ is the stress contribution from the fibers (see  [Ellipsoidal-Fiber-Distribution](solid_material_ellipsoidal_fiber_distribution.md)).

_Example:_
```xml
<material id="1" type="EFD neo-Hookean">
  <E>1</E>
  <v>0.3</v>
  <beta>4.5,4.5,4.5</beta>
  <ksi>1,1,1</ksi>
  <mat_axis type="local">0,0,0</mat_axis>
</material>
```
