The material type for cell growth is `cell growth` [^1].

The Cauchy stress for this material is

\[
\boldsymbol{\sigma}=-\pi\mathbf{I},
\]

where $\pi$ is the osmotic pressure, given by

\[
\pi=RT\left(\frac{c_{r}}{J-\varphi_{r}^{s}}-c_{e}\right),
\]

where $J=\det\mathbf{F}$ is the relative volume. The values of the universal gas constant $R$ and absolute temperature $T$ must be specified as global constants.

Cell growth may be modeled by simply increasing the mass of the intracellular solid matrix and membrane-impermeant solute. This is achieved by allowing the parameters $\varphi_{r}^{s}$ and $c_{r}$ to increase over time as a result of growth, by associating them with user-defined load curves. Since cell growth is often accompanied by cell division, and since daughter cells typically achieve the same solid and solute content as their parent, it may be convenient to assume that $\varphi_{r}^{s}$ and $c_{r}$ increase proportionally, though this is not an obligatory relationship. To ensure that the initial configuration is a stress-free reference configuration, let $c_{r}=\left(1-\varphi_{r}^{s}\right)c_{e}$ in the initial state prior to growth.

_Example (using units of mm, N, s, nmol, K):_
```
<Globals>
  <Constants>
    <T>298</T>
    <R>8.314e-06</R>
    <Fc>0</Fc>
  </Constants>
</Globals>

<Material>
  <material id="1" name="Cell" type="cell growth">
    <phir lc="1">1</phir>
    <cr lc="2">1</cr>
    <ce>300</ce>
  </material>
</Material>

<LoadData>
  <loadcurve id="1" type="smooth">
    <loadpoint>0,0.3</loadpoint>
    <loadpoint>1,0.6</loadpoint>
  </loadcurve>
  <loadcurve id="2" type="smooth">
    <loadpoint>0,210</loadpoint>
    <loadpoint>1,420</loadpoint>
  </loadcurve>
</LoadData>
```

[^1]: Ateshian, G.A, B., Morrison, Holmes, J.W., and Hung, C. T., "Mechanics of cell growth", Mechanics Research Communications 42 (2012), pp. 118-125.