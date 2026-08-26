This material describes an unconstrained hyperelastic Ogden material [^1].

The hyperelastic strain energy function for this material is given in terms of the eigenvalues of the right or left stretch tensor:

\[
W\left(\lambda_{1},\lambda_{2},\lambda_{3}\right)=\frac{1}{2}c_{p}\left(J-1\right)^{2}+\sum\limits_{i=1}^{N}\frac{c_{i}}{m_{i}^{2}}\left(\lambda_{1}^{m_{i}}+\lambda_{2}^{m_{i}}+\lambda_{3}^{m_{i}}-3-m_{i}\ln J\right).
\]

Here, $\lambda_{i}^{2}$ are the eigenvalues of the right or left Cauchy deformation tensor, $c_{p}$, $c_{i}$ and $m_{i}$ are material coefficients and $N$ ranges from 1 to 6. Any material parameters that are not specified by the user are assumed to be zero.

_Example:_
```xml
<material id="1" type="Ogden unconstrained">
  <m1>2.4</m1>
  <c1>1</c1>
  <cp>2</cp>
</material>
```

[^1]: Simo, J.C. and Taylor, R.L., "Quasi-incompressible finite elasticity in principal stretches: Continuum basis and numerical algorithms", Computer Methods in Applied Mechanics and Engineering 85 (1991), pp. 273-310.