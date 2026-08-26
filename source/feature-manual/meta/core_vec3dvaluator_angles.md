This valuator generates a unit vector orientated via the specification of spherical angles (azimuth and declination) relative to the local material axes (or global coordinate system, if no local material axes are defined).

Note that both `theta` (the azimuth angle) and `phi` (the declination angle) are defined in degrees.

![FigSCS.png](figs/FigSCS.png)
/// figure-caption
Illustration for the `angles` valuator.
///

The fiber is oriented along 

\[
\mathbf{e}_{r}=\cos\theta\sin\phi\,\mathbf{e}_{1}+\sin\theta\sin\phi\,\mathbf{e}_{2}+\cos\phi\,\mathbf{e}_{3},0\leqslant\theta<2\pi,\;0\leqslant\phi\leqslant\pi,
\]

where $\left\{ \mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\right\}$ are orthonormal vectors representing the local element coordinate system, or global coordinate system.

```
<fiber type="angles">
  <theta>20</center>
  <phi>90</phi>
</fiber>
```

