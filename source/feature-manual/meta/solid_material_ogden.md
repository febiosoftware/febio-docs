This material describes an incompressible hyperelastic Ogden material [^1].

The uncoupled hyperelastic strain energy function for this material is given in terms of the eigenvalues of the deformation tensor:

\[
\Psi=\sum\limits_{i=1}^{N}\frac{c_{i}}{m_{i}^{2}}\left(\tilde{\lambda}_{1}^{m_{i}}+\tilde{\lambda}_{2}^{m_{i}}+\tilde{\lambda}_{3}^{m_{i}}-3\right)+U\left(J\right).
\]

Here, $\tilde{\lambda}_{i}^{2}$ are the eigenvalues of $\mathbf{\tilde{C}}$, $c_{i}$ and $m_{i}$ are material coefficients and $N$ ranges from 1 to 6. Note that you only have to include the material parameters for the terms you intend to use.

_Example:_
```xml
<material id="1" type="Ogden">
  <m1>2.4</m1>
  <c1>1</c1>
  <k>100</k>
</material>
```

[^1]: Simo, J.C. and Taylor, R.L., "Quasi-incompressible finite elasticity in principal stretches: Continuum basis and numerical algorithms", Computer Methods in Applied Mechanics and Engineering 85 (1991), pp. 273-310.