# relaxation-Malkin-distortion

**Module:** solid

**Category:** materialprop

**Type string:** `"relaxation-Malkin-distortion"`

## Parameters

| Name | Description | Default | Range | Units |
|------|-------------|---------|-------|-------|
| `t1c0` | constant for tau1 | 0 | $\gt 0$ | t |
| `t1c1` | coefficient for tau1 | 0 | $\in \mathbb{R}$ | t |
| `t1s0` | strain for tau1 | 1 | $\gt 0$ |  |
| `t2c0` | constant for tau2 | 0 | $\gt 0$ | t |
| `t2c1` | coefficient for tau2 | 0 | $\in \mathbb{R}$ | t |
| `t2s0` | strain for tau2 | 1 | $\gt 0$ |  |
| `beta` | power exponent beta | 1 | $\gt 0$ |  |


## Description

See Section [relaxation-malkin](solid_materialprop_relaxation-malkin.md) for the description of this relaxation function. When the material parameters vary with the distortional strain $K_{2}$ according to

\[
\begin{aligned}\tau_{1}\left(K_{2}\right) & =\tau_{10}+\tau_{11}\exp\left(-\frac{K_{2}}{s_{1}}\right)\\
\tau_{2}\left(K_{2}\right) & =\tau_{20}+\tau_{21}\exp\left(-\frac{K_{2}}{s_{2}}\right)
\end{aligned}
\]

 The material type is `relaxation-Malkin-distortion`.

 The definition of $K_{2}$ is given in [relaxation-exp-dist-user](solid_materialprop_relaxation-exp-dist-user.md) and examples of how to specify these functions can be found there as well.


