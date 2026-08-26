# Ogden

**Module:** solid

**Category:** material

**Type string:** `"Ogden"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\ge 0$ | M/L^3 |
| `k` | bulk modulus | 0 | $\ge 0$ | P |
| `pressure_model` | pressure_model | 0 | $[0, 3]$ |  |
| `c1` | c1 | 0 | $\in \mathbb{R}$ | P |
| `c2` | c2 | 0 | $\in \mathbb{R}$ | P |
| `c3` | c3 | 0 | $\in \mathbb{R}$ | P |
| `c4` | c4 | 0 | $\in \mathbb{R}$ | P |
| `c5` | c5 | 0 | $\in \mathbb{R}$ | P |
| `c6` | c6 | 0 | $\in \mathbb{R}$ | P |
| `m1` | m1 | 1 | $\neq 0$ |  |
| `m2` | m2 | 1 | $\neq 0$ |  |
| `m3` | m3 | 1 | $\neq 0$ |  |
| `m4` | m4 | 1 | $\neq 0$ |  |
| `m5` | m5 | 1 | $\neq 0$ |  |
| `m6` | m6 | 1 | $\neq 0$ |  |


## Description

This material describes an incompressible hyperelastic Ogden material [^1].

The uncoupled hyperelastic strain energy function for this material is given in terms of the eigenvalues of the deformation tensor:

\[
\Psi=\sum\limits_{i=1}^{N}\frac{c_{i}}{m_{i}^{2}}\left(\tilde{\lambda}_{1}^{m_{i}}+\tilde{\lambda}_{2}^{m_{i}}+\tilde{\lambda}_{3}^{m_{i}}-3\right)+U\left(J\right).
\]

Here, $\tilde{\lambda}_{i}^{2}$ are the eigenvalues of $\mathbf{\tilde{C}}$, $c_{i}$ and $m_{i}$ are material coefficients and $N$ ranges from 1 to 6. Note that you only have to include the material parameters for the terms you intend to use.

_Example:_
```xml
<material id="1" type="Ogden">
  <m1>2.4</m1>
  <c1>1</c1>
  <k>100</k>
</material>
```

[^1]: Simo, J.C. and Taylor, R.L., "Quasi-incompressible finite elasticity in principal stretches: Continuum basis and numerical algorithms", Computer Methods in Applied Mechanics and Engineering 85 (1991), pp. 273-310.
