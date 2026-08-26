The fiber density distribution type `ellipsoidal` models a generally orthotropic 3D distribution. It corresponds to

\[
R\left(\mathbf{n}\right)=C^{-1}\left[\left(\frac{n_{1}}{a}\right)^{2}+\left(\frac{n_{2}}{b}\right)^{2}+\left(\frac{n_{3}}{c}\right)^{2}\right]^{-1/2}\,,
\]

where $\left(n_{1},n_{2},n_{3}\right)$ are the components of $\mathbf{n}$ in the local Cartesian basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ of each element, when specified or the global basis by default; and $C$ is calculated to satisfy the integration constraint on $R\left(\mathbf{n}\right)$. The parameters $\left(a,b,c\right)$ represents the semi-principal axes of the ellipsoid and must be positive.

The value of $C$ is automatically adjusted to account for the values of the semi-principal axes $\left(a,b,c\right)$. Therefore, only the relative ratios of these parameters matter.

![FigEllipsoidalDistribution.png](figs/FigEllipsoidalDistribution.png)
/// figure-caption
Illustration of the `ellipsoidal` fiber distribution function.
///


_Example:_
```xml
<distribution type="ellipsoidal">
  <spa>3,2,1</spa>
</distribution>
```
