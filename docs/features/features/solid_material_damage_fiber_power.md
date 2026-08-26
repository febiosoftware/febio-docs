# damage fiber power

**Module:** solid

**Category:** material

**Type string:** `"damage fiber power"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\ge 0$ | M/L^3 |
| `t0` | t0 | 1e+09 | $\ge 0$ |  |
| `Dmax` | Dmax | 1 | $[0, 1]$ |  |
| `beta_s` | beta_s | 0 | $\gt 0$ |  |
| `gamma_max` | gamma_max | 0 | $\ge 0$ |  |
| `D2_a` | D2_a | 0 | $\in \mathbb{R}$ |  |
| `D2_b` | D2_b | 0 | $\in \mathbb{R}$ |  |
| `D2_c` | D2_c | 0 | $\in \mathbb{R}$ |  |
| `D2_d` | D2_d | 0 | $\in \mathbb{R}$ |  |
| `D3_inf` | D3_inf | 0 | $\in \mathbb{R}$ |  |
| `D3_g0` | D3_g0 | 0 | $\in \mathbb{R}$ |  |
| `D3_rg` | D3_rg | 1 | $\in \mathbb{R}$ |  |
| `a1` | a1 | 0 | $\ge 0$ |  |
| `a2` | a2 | 0 | $\gt 1$ |  |
| `kappa` | kappa | 0 | $[0, 0.666667]$ |  |
| `fiber` | fiber |  | N/A |  |


## Description

The material type for Damage Fiber Power is `damage fiber power`.

By setting, 

\[
\Psi^{0}=\kappa\mathit{I_{1}}+\left(1-\frac{3}{2}\kappa\right)\mathit{K_{3}}
\]

and $\mathit{m(P)=\alpha_{1}(P)^{\alpha_{2}},}$ the strain-energy form above can be made suitable for modeling damage,

\[
\varPsi(C,D)=\alpha_{1}\left(\left(1-D\right)\left[\kappa I_{1}+\left(1-\frac{3}{2}\kappa\right)K_{3}\right]-c\right)^{\alpha_{2}}
\]

The Cauchy stress takes on the following form,

\[
\sigma=\frac{2}{J}(1-D)\frac{dm}{dP}\left[\kappa b+\left(1-\frac{3}{2}\kappa\right)\left[bI_{4}+I_{1}I_{4}m-I_{4}a\bigodot ba\right]\right]
\]

_Example:_
```xml
<solid type="damage fiber power">
  <a1>1400</a1>
  <a2>2.2</a2>
  <kappa>1e-08</kappa>
  <t0>0.98</t0>
  <Dmax>0.96</Dmax>
  <beta_s>0.06</beta_s>
  <gamma_max>17.98</gamma_max>
  <fiber type="angles">
    <theta>-39.87</theta>
    <phi>90</phi>
  </fiber>
</solid>
```
