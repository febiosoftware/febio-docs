The material type for a perfect osmometer equilibrium swelling pressure is `perfect osmometer`. The swelling pressure is described by the equations for a perfect osmometer, assuming that the material is porous, containing an interstitial solution whose solutes cannot be exchanged with the external bathing environment; similarly, solutes in the external bathing solution cannot be exchanged with the interstitial fluid of the porous material. Therefore, osmotic pressurization occurs when there is an imbalance between the interstitial and bathing solution osmolarities. Since osmotic swelling must be resisted by a solid matrix, this material is not stable on its own. It must be combined with an elastic material that resists the swelling, using a `solid mixture` container as described in Section [Solid-Mixture](solid_material_solid_mixture.md).

The Cauchy stress for this material is the stress from the perfect osmometer equilibrium response:

\[
\boldsymbol{\sigma}=-\pi\mathbf{I},
\]

where $\pi$ is the osmotic pressure, given by

\[
\pi=RT\left(\bar{c}-\bar{c}^{\ast}\right)\,.
\]

$\bar{c}$ is the interstitial fluid in the current configuration, related to the reference configuration via

\[
\bar{c}=\frac{\varphi_{0}^{w}}{J-1+\varphi_{0}^{w}}\bar{c}_{0}\,,
\]

where $J=\det\mathbf{F}$ is the relative volume. The values of the universal gas constant $R$ and absolute temperature $T$ must be specified as global constants.

Though this material is porous, this is not a full-fledged biphasic material. The behavior described by this material is strictly valid only after the transient response of interstitial fluid and solute fluxes has subsided.

_Example (using units of mm, N, s, nmol, K):_

Hyperosmotic loading of a cell with a membrane-impermeant solute, starting from isotonic conditions.
```
<Globals>
  <Constants>
    <R>8.314e-6</R>
    <T>310</T>
  </Constants>
</Globals>

<material id="1" type="solid mixture">
  <solid type="perfect osmometer">
    <phiw0>0.8</ phiw0>
    <iosm>300</cF0>
    <bosm lc="1">1</bosm>
  </solid>
  <solid type="neo-Hookean">
    <E>1.0</E>
    <v>0</v>
  </solid>
</material>

<LoadData>
  <loadcurve id="1">
    <loadpoint>0,300</loadpoint>
    <loadpoint>1,1500</loadpoint>
  </loadcurve>
</LoadData>
```