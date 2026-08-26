The fiber density distribution type `von-Mises-3d` models a transversely isotropic 3D distribution [^1]. It corresponds to

\[
R\left(\mathbf{n}\right)=\frac{1}{\pi}\sqrt{\frac{b}{2\pi}}\frac{\exp\left(2bn_{1}^{2}\right)}{\mbox{erfi}\left(\sqrt{2b}\right)}\,,
\]

where $\left(n_{1},n_{2},n_{3}\right)$ are the components of $\mathbf{n}$ in the local Cartesian basis $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ of each element of the global basis by default; and b is the concentration parameter ($b>0$).

![FigPiPeriodicVonMisesDistribution.png](figs/FigPiPeriodicVonMisesDistribution.png)
/// figure-caption
Illustration of the `von-Mises-3d` distribution function.
///


_Example:_
```xml
<distribution type="von-Mises-3d">
  <b>0.5</b>
</distribution>
```

[^1]: Gasser, T Christian, Ogden, Ray W, and Holzapfel, Gerhard A, "Hyperelastic modelling of arterial layers with distributed collagen fibre orientations", J R Soc Interface 3, 6 (2006), pp. 15-35.