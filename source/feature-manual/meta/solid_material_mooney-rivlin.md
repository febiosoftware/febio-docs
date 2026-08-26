This material model is a hyperelastic Mooney-Rivlin type with uncoupled deviatoric and volumetric behavior. The strain-energy function is given by:

\[
 \Psi=C_{1}\left(\tilde{I}_{1}-3\right)+C_{2}\left(\tilde{I}_{2}-3\right)+\frac{1}{2}K\left(\ln J\right)^{2}\,.
 \]
 
 $C_{1}$ and $C_{2}$ are the Mooney-Rivlin material coefficients. The variables $\tilde{I}_{1}$ and $\tilde{I}_{2}$ are the first and second invariants of the deviatoric right Cauchy-Green deformation tensor $\mathbf{\tilde{C}}$. The coefficient $K$ is a bulk modulus-like penalty parameter and $J$ is the determinant of the deformation gradient tensor. When $C_{2}=0$, this model reduces to an uncoupled version of the neo-Hookean constitutive model.

This material model uses a three-field element formulation, interpolating displacements as linear field variables and pressure and volume ratio as piecewise constant on each element [^1].

This material model is useful for modeling certain types of isotropic materials that exhibit some limited compressibility, i.e. $100 < (K/C_{\mathrm{1}}) < 10000$.

_Example:_
```xml
<material id="2" type="Mooney-Rivlin">
  <c1>10.0</c1>
  <c2>20.0</c2>
  <k>1000</k>
</material>
```

[^1]: Simo, J.C. and Taylor, R.L., "Quasi-incompressible finite elasticity in principal stretches: Continuum basis and numerical algorithms", Computer Methods in Applied Mechanics and Engineering 85 (1991), pp. 273-310.