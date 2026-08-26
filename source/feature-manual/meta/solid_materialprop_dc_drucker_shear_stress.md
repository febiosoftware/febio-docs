The material type for the Drucker shear stress criterion is `DC Drucker shear stress`. It is based on the yield criterion for plasticity introduced in [^1]. For this criterion,

\[
\Xi\left(\mathbf{F}\right)=k=\left(J_{2}^{3}-cJ_{3}^{2}\right)^{1/6}
\]

where $J_{2}=\frac{1}{2}\text{dev}\boldsymbol{\sigma}_{0}:\text{dev}\boldsymbol{\sigma}_{0}$, $J_{3}=\det\left(\text{dev}\boldsymbol{\sigma}_{0}\right)$, $k$ is the yield limit in simple shear and $c$ is a user-specified non-dimensional material constant which must lie in the range $-\frac{27}{8}\le c\le\frac{9}{4}$. To better understand the meaning of $k$, consider uniaxial loading of a bar which yields at the normal stress value of $\sigma_{y}$. In this case,

\[
k=\frac{\sigma_{y}}{\sqrt{3}}\left(1-\frac{4}{27}c\right)^{1/6}\quad\frac{\sigma_{y}}{\sqrt{3}}\left(\frac{2}{3}\right)^{1/6}\le k\le\frac{\sigma_{y}}{\sqrt{3}}\left(\frac{3}{2}\right)^{1/6}
\]

In the special case when $c=0$ the Drucker criterion reduces to the von Mises criterion, with $k=\sigma_{y}/\sqrt{3}$.

_Example:_
```xml
<criterion type="DC Drucker shear stress">
  <c>2.25</c>
</criterion>
```

[^1]: Drucker, Daniel Charles, "Relation of experiments to mathematical theories of plasticity", Journal of Applied Mechanics (1949).
