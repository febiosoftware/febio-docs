The material type for a Veronda-Westmann material with an ellipsoidal continuous fiber distribution is `EFD Veronda-Westmann`.

The stress $\tilde{\boldsymbol{\sigma}}$ for this material is given by,

\[
\tilde{\boldsymbol{\sigma}}=\tilde{\boldsymbol{\sigma}}_{VW}+\tilde{\boldsymbol{\sigma}}_{f}\,.
\]

Here, $\tilde{\boldsymbol{\sigma}}_{VW}$ is the stress from the Veronda-Westmann basis (see [Veronda-Westmann](solid_material_veronda-westmann.md)), and $\tilde{\boldsymbol{\sigma}}_{f}$ is the stress contribution from the ellipsoidal fiber distribution (see [EFD-Uncoupled](solid_material_efd_uncoupled.md)).

_Example:_
```xml
<material id="1" type="EFD Veronda-Westmann">
  <c1>1</c1>
  <c2>0.5</c2>
  <k>1000</k>
  <beta>4.5,4.5,4.5</beta>
  <ksi>1,1,1</ksi>
  <mat_axis type="local">0,0,0</mat_axis>
</material>
```
