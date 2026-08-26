# viscoelastic

**Module:** solid

**Category:** material

**Type string:** `"viscoelastic"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `density` | density | 1 | $\ge 0$ | M/L^3 |
| `t1` | t1 | 1 | $\in \mathbb{R}$ | t |
| `t2` | t2 | 1 | $\in \mathbb{R}$ | t |
| `t3` | t3 | 1 | $\in \mathbb{R}$ | t |
| `t4` | t4 | 1 | $\in \mathbb{R}$ | t |
| `t5` | t5 | 1 | $\in \mathbb{R}$ | t |
| `t6` | t6 | 1 | $\in \mathbb{R}$ | t |
| `g0` | g0 | 1 | $\in \mathbb{R}$ |  |
| `g1` | g1 | 0 | $\in \mathbb{R}$ |  |
| `g2` | g2 | 0 | $\in \mathbb{R}$ |  |
| `g3` | g3 | 0 | $\in \mathbb{R}$ |  |
| `g4` | g4 | 0 | $\in \mathbb{R}$ |  |
| `g5` | g5 | 0 | $\in \mathbb{R}$ |  |
| `g6` | g6 | 0 | $\in \mathbb{R}$ |  |
| `elastic` | elastic |  | N/A |  |


## Description

The material type for viscoelastic materials is `viscoelastic`.

For a viscoelastic material, the second Piola Kirchhoff stress can be written as follows [^1]:

\[
\mathbf{S}\left(t\right)=\int\limits_{-\infty}^{t}G\left(t-s\right)\frac{d\mathbf{S}^{e}}{ds}\,ds\,,
\]

where $\mathbf{S}^{e}$ is the elastic stress and $G$ is the relaxation function. It is assumed that the relaxation function is given by the following discrete relaxation spectrum:

\[
G\left(t\right)=\gamma_{0}+\sum\limits_{i=1}^{N}\gamma_{i}\exp\left(-t/\tau_{i}\right)\,,
\]

Note that the user does not have to enter all the $\tau_{i}$ and $\gamma_{i}$ coefficients. Instead, only the values that are used need to be entered. So, if $N$ is 2, only $\tau_{1}$, $\tau_{2}$, $\gamma_{1}$ and $\gamma_{2}$ have to be entered.

The `elastic` parameter defines the elastic material and must be an unconstrained elastic material. 

_Example:_

```xml
<material id="1" name="Material 1" type="viscoelastic">
  <g1>0.95</g1>
  <t1>0.01</t1>
  <elastic type="neo-Hookean">
    <E>1</E>
    <v>0.0</v>
  </elastic>
</material>
```

[^1]: Puso, M. A. and Weiss, J. A., "Finite element implementation of anisotropic quasi-linear viscoelasticity using a discrete spectrum approximation", J Biomech Eng 120, 1 (1998), pp. 62-70.
