# damage fiber exponential

**Module:** solid

**Category:** material

**Type string:** `"damage fiber exponential"`

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
| `k1` | k1 | 0 | $\ge 0$ |  |
| `k2` | k2 | 0 | $\gt 0$ |  |
| `kappa` | kappa | 0 | $[0, 0.333333]$ |  |
| `fiber` | fiber |  | N/A |  |


## Description

The material type for Damage Fiber Exponential is `damage fiber exponential`.

The effective strain-energy function is given by,

\[
\Psi^{0}=\kappa I_{1}+(1-3\kappa)I_{4}
\]

and

\[
m(P)=\frac{k_{1}}{2k_{2}}\left\{ \exp\left(k_{2}\left\langle P\right\rangle ^{2}\right)-1\right\},
\]

where $a$ denotes the direction of the fibers.
So that,

\[
\Psi=\frac{k_{1}}{2k_{2}}\left\{ \exp\left(k_{2}\left\langle \left(1-D_{a}\right)\left(\kappa I_{1}-\left(1-3\kappa\right)I_{4}\right)-1\right\rangle ^{2}\right)-1\right\} .
\]

The Cauchy stress then takes on the following form,

\[
\sigma=\frac{2}{J}(1-D)\frac{dm}{dP}\left[\kappa b+(1-3\kappa)I_{4}m\right].
\]

_Example:_
```xml
<solid type="damage fiber exponential"> 
  <k1>1288.97</k1> 
  <k2>400</k2> 
  <kappa>0.2</kappa> 
  <t0>0.9</t0> 
  <Dmax>0.99</Dmax> 
  <beta_s>0.001</beta_s> 
  <gamma_max>6.67</gamma_max> 
  <fiber type="angles"> 
    <theta>-54.94</theta> 
    <phi>90</phi> 
  </fiber> 
</solid>
```
