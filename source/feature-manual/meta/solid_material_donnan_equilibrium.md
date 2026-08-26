The material type for a Donnan equilibrium swelling pressure is `Donnan equilibrium`. The swelling pressure is described by the equations for ideal Donnan equilibrium, assuming that the material is porous, with a charged solid matrix, and the external bathing environment consists of a salt solution of monovalent counter-ions [^1] [^2]. Since osmotic swelling must be resisted by a solid matrix, this material is not stable on its own. It must be combined with an elastic material that resists the swelling, using a `solid mixture` container as described in [solid-mixture](solid_material_solid_mixture.md).

The Cauchy stress for this material is the stress from the Donnan equilibrium response [^3]: 

\[
\boldsymbol{\sigma}=-\pi\mathbf{I},
\]

where $\pi$ is the osmotic pressure, given by

\[
\pi=R\,T\,\Phi\left(\sqrt{\left(c^{F}\right)^{2}+\left(\bar{c}^{\ast}\right)^{2}}-\bar{c}^{\ast}\right),
\]

and $c^{F}$ is the fixed-charge density in the current configuration, related to the reference configuration via 

\[
c^{F}=\frac{\varphi_{0}^{w}}{J-1+\varphi_{0}^{w}}c_{0}^{F},
\]

where $J=\det\mathbf{F}$ is the relative volume. The values of the universal gas constant $R$ and absolute temperature $T$ must be specified as global constants. For ideal Donnan law, use $\Phi=1$.

Note that $c_{0}^{F}$ may be negative or positive; the gel porosity is unitless and must be in the range $0<\varphi_{0}^{w}<1$. A self-consistent set of units must be used for this model. For example:

|                | (m, N, s, mol, K)         | (mm, N, s, nmol, K)                     |
|----------------|---------------------------|-----------------------------------------|
|R               | 8.314 J/mol\cdot K        | $8.314×10^{\mathrm{-6}} mJ/nmol\cdot K$ |
|T               | K                         | K                                       |
|$c_{0}^{F}$     | $Eq/m^{\mathrm{3}}= mEq/L$| $nEq/mm^{\mathrm{3}}= mEq/L$            | 
|$\bar{c}^{\ast}$| $mol/m^{\mathrm{3}}= mM$  | $nmol/mm^{\mathrm{3}}= mM$              |
|$\xi_{i}$       | Pa                        | MPa                                     |
|$\pi$           | Pa                        | MPa                                     |

Though this material is porous, this is not a full-fledged biphasic material as described in Section [sec:Biphasic-Materials] for example. The behavior described by this material is strictly valid only after the transient response of interstitial fluid and ion fluxes has subsided (thus Donnan equilibrium).

Donnan osmotic swelling reduces to zero when either $c_{0}^{F}=0$ or $\bar{c}^{\ast}\to\infty$. Therefore, entering any other values for $c_{0}^{F}$ and $\bar{c}^{\ast}$ at the initial time point of an analysis produces an instantaneous, non-zero swelling pressure. Depending on the magnitude of this pressure relative to the solid matrix stiffness, the nonlinear analysis may not converge due to this sudden swelling. Therefore, it is recommended to prescribe a load curve for either `cF0` or `bosm`, to ease into the initial swelling prior to the application of other loading conditions.

_Example (using units of mm, N, s, nmol, K):_
```
<Globals>
  <Constants>
    <R>8.314e-6</R>
    <T>310</T>
  </Constants>
</Globals>

<material id="1" type="solid mixture">
  <mat_axis type="local">0,0,0</mat_axis>
  <solid type="Donnan equilibrium">
    <phiw0>0.8</phiw0>
    <cF0 lc="1">1</cF0>
    <bosm>300</bosm>
  </solid>
  <solid type="ellipsoidal fiber distribution">
    <ksi>0.01,0.01,0.01</ksi>
    <beta>3,3,3</beta>
  </solid>
</material>

<LoadData>
  <loadcurve id="1">
    <loadpoint>0,0</loadpoint>
    <loadpoint>1,150</loadpoint>
  </loadcurve>
</LoadData>
```

[^1]: Overbeek, J T, "The Donnan equilibrium", Prog Biophys Biophys Chem 6 (1956), pp. 57-84.

[^2]: Lai, W M, Hou, J S, and Mow, V C, "A triphasic theory for the swelling and deformation behaviors of articular cartilage", J Biomech Eng 113, 3 (1991), pp. 245-58.

[^3]: Ateshian, G. A., Rajan, V., Chahine, N. O., Canal, C. E., and Hung, C. T., "Modeling the matrix of articular cartilage using a continuous fiber angular distribution predicts many observed phenomena", J Biomech Eng 131, 6 (2009), pp. 061003.