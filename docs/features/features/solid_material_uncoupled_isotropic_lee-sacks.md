# uncoupled isotropic Lee-Sacks

**Module:** solid

**Category:** material

**Type string:** `"uncoupled isotropic Lee-Sacks"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\ge 0$ | M/L^3 |
| `k` | bulk modulus | 0 | $\ge 0$ | P |
| `pressure_model` | pressure_model | 0 | $[0, 3]$ |  |
| `c0` | c0 | 0 | $\in \mathbb{R}$ | P |
| `c1` | c1 | 0 | $\in \mathbb{R}$ | P |
| `c2` | c2 | 0 | $\in \mathbb{R}$ |  |
| `tangent_scale` | tangent_scale | 1 | $\in \mathbb{R}$ |  |


## Description

This material implements a Fung-type material, as presented in Kamensy, CMAME 2018. The material formulation is selected by setting the type attribute to `uncoupled isotropic Lee-Sacks`. 

The strain-energy density function for this material combines a neo-Hookean matrix with a Fung-type exponential term, and is defined as follows. 

\[
\Psi=\frac{c_{0}}{2}\left(I_{1}-3\right)+\frac{c_{1}}{2}\left(e^{c_{2}\left(I_{1}-3\right)^{2}}-1\right)
\]

As reported in Kamensky, the exponential term may cause convergence difficulties under certain loading conditions. It was reported that increasing the value of $c_{0}$ during the stiffness evaluation may improve convergence. The default value for tangent_scale is 1, and thus tangent scaling is not applied. A tangent scale factor of 20 was used in Kamensky.

_Example:_
```xml
<material id="1" name="material1" type="uncoupled isotropic Lee-Sacks">
  <k>1000</k>
  <c0>10</c0>
  <c1>0.209</c1>
  <c2>9.046</c2>
</material>
```
