The material type for osmotic pressure from virial expansion is `osmotic virial expansion`.

The Cauchy stress for this material is

\[
\boldsymbol{\sigma}=-\pi\mathbf{I},
\]

where $\pi$ is the osmotic pressure, given by

\[
\pi=c_{1}c+c_{2}c^{2}+c_{3}c^{3},\quad c=\frac{\varphi_{r}^{w}c_{r}}{J-1+\varphi_{r}^{w}}\,,
\]

$c$ is the solute concentration in the current configuration, and $J=\det\mathbf{F}$ is the relative volume.

This osmotic swelling pressure in the interstitial fluid of a porous material represents an entropic mechanism whose magnitude is independent of the external bath osmolarity. Typically, this material should be used in a solid mixture where the swelling pressure is resisted by a solid matrix in tension.

_Example:_
```xml
<Material>
  <material id="1" type="solid mixture">
    <solid type="osmotic virial expansion">
      <phiw0>0.8</phiw0>
      <cr lc="1">100</cr>
      <c1>2.436e-6</c1>
      <c2>0</c2>
      <c3>0</c3>
    </solid>
    <solid type="spherical fiber distribution"/>
  </material>
</Material>
<LoadData>
  <loadcurve id="1" type="smooth">
    <loadpoint>0,0</loadpoint>
    <loadpoint>1,1</loadpoint>
  </loadcurve>
</LoadData>
```
