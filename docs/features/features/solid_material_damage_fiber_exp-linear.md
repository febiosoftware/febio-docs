# damage fiber exp-linear

**Module:** solid

**Category:** material

**Type string:** `"damage fiber exp-linear"`

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
| `c3` | c3 | 0 | $\ge 0$ |  |
| `c4` | c4 | 0 | $\ge 0$ |  |
| `c5` | c5 | 0 | $\ge 0$ |  |
| `lambda` | lambda | 0 | $\gt 0$ |  |
| `fiber` | fiber |  | N/A |  |


## Description

This continuous damage formulation uses a slightly modified damage formulation. The total damage is here defined as,

\[
D=D_{1}+D_{2}
\]

Here, $D_{1}$ defines the same damage term as defined above. The $D_{2}$ is defined as follows,

\[
D_{2}=D_{3}\left[a\left(\mathrm{exp}\left(b\beta\right)-1\right)+c\left(\mathrm{exp}\left(d\beta\right)-1\right)\right]
\]

The material parameters a and c control the magnitude of the continuous damage of the two phenomena: 1) slow, constant increased in damage, 2) sharp jump in damage near failure. The other material parameters, b and d, control the rate of continuous damage accumulation for the two phenomena mentioned above, and is a function of the collagen discontinuous damage. Furthermore, 

\[
D_{3}\left(\gamma\right)=\frac{D_{3\infty}}{1+exp\left(-\left(\gamma-\gamma_{0}\right)/r_{\gamma}\right)}
\]

Here, $D_{3\infty}$ is the maximum achievable discontinuous damage possible for the model, $\gamma_{0}$ determines the shape of the curve, and $r_{\gamma}$ controls the rate of discontinuous damage accumulation.

The effective strain-energy function is given by,

\[
\Psi^{0}=\sqrt{I_{4}}
\]

and

\[
m\left(P\right)=\left\{ \begin{array}{cc}
c_{3}\left(\exp\left(-c_{4}\right)\left(Ei\left(c_{4}\left(P+1\right)\right)-Ei\left(c_{4}\right)\right)-\log\left(P+1\right)\right), & P\leqq\lambda^{*}+1\\
c_{5}P+c_{6}\log\left(P+1\right)+d & P>\lambda^{*}+1
\end{array}\right.
\]

Here, $d$ is determined by requiring continuity at $\lambda^{*}$.




