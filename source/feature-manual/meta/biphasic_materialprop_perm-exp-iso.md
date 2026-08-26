The material type for exponential isotropic permeability is `perm-exp-iso`.

This isotropic material model has the general form

\[
\mathbf{k}=k\left(J\right)\,\mathbf{I}
\]

where $J=\det\mathbf{F}$ is the determinant of the deformation gradient. For this material model,

\[
k\left(J\right)=k_{0}\exp\left(M\frac{J-1}{J-\varphi_{0}}\right)\,,
\]

where $\varphi_{0}$ is the referential solid volume fraction of the porous solid matrix. Pore closure occurs as $J$ approaches $\varphi_{0}$ from above, in which case the permeability reduces to zero,

\[
\lim_{J\to\varphi_{0}}k\left(J\right)=0\,.
\]

Representative variations of $k\left(J\right)/k_{0}$ are shown in the figure below.

![FigPermExpIso.png](figs/FigPermExpIso.png)
/// figure-caption
Exponential isotropic permeability, showing dependence of $k\left(J\right)/k_{0}$ on material parameter $M$, when $\varphi_{0}=0.2$ and $\varphi_{0}<J\le1.2$.
///

_Example:_
```
<permeability name="Permeability" type="perm-exp-iso">
  <perm>0.001</perm>
  <M>1.5</M>
</permeability>
```