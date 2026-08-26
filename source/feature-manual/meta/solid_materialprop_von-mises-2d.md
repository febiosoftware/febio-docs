The fiber density distribution type `von-Mises-2d` models an orthotropic 2D distribution. This distribution corresponds to

\[
R\left(\mathbf{n}\right)=\frac{\exp\left[b\left(2n_{1}^{2}-1\right)\right]}{2\pi I_{0}\left(b\right)}
\]

where $\left(n_{1},n_{2},n_{3}\right)$ are the components of $\mathbf{n}$ in the local Cartesian basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$  of each element or the global basis by default, with the distribution lying in the $\left\{ \mathbf{e}_{1},\mathbf{e}_{2}\right\}$ plane; and $b$ is the concentration parameter $(b>0)$. $I_{0}$ is the modified Bessel function of the first kind of order 0.

![2D Von-Mises Distribution](figs/FigVonMisesDistribution.png)
/// figure-caption
Illustration of the `von-Mises-2d` distribution function.
///

_Example:_
```xml
<distribution type="von-Mises-2d">
  <b>3</b>
</distribution>
```