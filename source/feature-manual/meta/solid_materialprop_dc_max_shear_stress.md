The material type for maximum shear stress damage or yield criterion is `DC max shear stress`. For this criterion,

\[
\Xi\left(\mathbf{F}\right)=\max\left(\frac{\left|\sigma_{1}-\sigma_{2}\right|}{2},\frac{\left|\sigma_{2}-\sigma_{3}\right|}{2},\frac{\left|\sigma_{3}-\sigma_{1}\right|}{2}\right)
\]

where $\sigma_{1}$, $\sigma_{2}$, $\sigma_{3}$ are the principal values of $\boldsymbol{\sigma}_{0}\left(\mathbf{F}\right)$.

_Example:_
```xml
<criterion type="DC max shear stress"/>
```