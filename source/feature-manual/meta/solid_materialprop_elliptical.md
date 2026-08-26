The fiber density distribution type `elliptical` models an orthotropic 2D distribution. This distribution corresponds to

\[
R\left(\mathbf{n}\right)=C^{-1}\left[\left(\frac{n_{1}}{a}\right)^{2}+\left(\frac{n_{2}}{b}\right)^{2}\right]^{-1/2}
\]

where $\left(n_{1},n_{2},n_{3}\right)$ are the components of $\mathbf{n}$ in the local Cartesian basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ of each element or the global basis by default, implying that the elliptical distribution lies in the $\left\{ \mathbf{e}_{1},\mathbf{e}_{2}\right\}$ plane; and $\left(a,b\right)$ are the semi-principal axes of the ellipse. Here, $C=4bK\left(e\right)$ where $K$ is the complete elliptic integral of the first kind and

\[
e=\sqrt{1-\frac{b^{2}}{a^{2}}}
\]

is the ellipse eccentricity.

![FigEllipticalDistribution.png](figs/FigEllipticalDistribution.png)
/// figure-caption
Illustration of the `elliptical` fiber distribution function.
///

_Example:_
```xml
<distribution type="elliptical">
  <spa1>8</spa1>
  <spa2>1</spa2>
</distribution>
```
