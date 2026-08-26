The material type for a swelling pressure combined with an ellipsoidal continuous fiber distribution is `EFD Donnan equilibrium`. The swelling pressure is described by the equations for ideal Donnan equilibrium, assuming that the material is porous, with a charged solid matrix, and the external bathing environment consists of a salt solution of monovalent counter-ions.

The Cauchy stress for this material is given by,

\[
\boldsymbol{\sigma}=\boldsymbol{\sigma}_{DE}+\boldsymbol{\sigma}_{f}\,.
\]

$\boldsymbol{\sigma}_{f}$ is the stress contribution from the fibers. $\boldsymbol{\sigma}_{DE}$ is the stress from the Donnan equilibrium response, as described in [Donnan-Equilibrium-Swelling](solid_material_donnan_equilibrium.md).

_Example (using units of mm, N, s, nmol, K):_
```
<Globals>
  <Constants>
    <R>8.314e-6</R>
    <T>310</T>
  </Constants>
</Globals>

<material id="1" type="EFD Donnan equilibrium">
  <phiw0>0.8</phiw0>
  <cF0 lc="1">1</cF0>
  <bosm>300</bosm>
  <beta>3,3,3</beta>
  <ksi>0.01,0.01,0.01</ksi>
  <mat_axis type="local">0,0,0</mat_axis>
</material>

<LoadData>
  <loadcurve id="1">
    <loadpoint>0,0</loadpoint>
    <loadpoint>1,150</loadpoint>
  </loadcurve>
</LoadData>
```