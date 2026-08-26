The material type for a strain-dependent diffusivity tensor which is isotropic in the reference configuration is `diff-ref-iso`.

This material uses a strain-dependent diffusivity tensor that accommodates strain-induced anisotropy:

\[
\mathbf{d}=\left(d_{0r}\mathbf{I}+\frac{d_{1r}}{J^{2}}\mathbf{b}+\frac{d_{2r}}{J^{4}}\mathbf{b}^{2}\right)\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{r}^{s}}\right)e^{M\left(J^{2}-1\right)/2},
\]

where $J$ is the jacobian of the deformation, i.e. $J=\det\mathbf{F}$ where $\mathbf{F}$ is the deformation gradient, and $\mathbf{b}=\mathbf{F}\cdot\mathbf{F}^{T}$ is the left Cauchy-Green tensor. Note that the diffusivity in the reference state $(\mathbf{F}=\mathbf{I})$ is isotropic and given by $\mathbf{d}=\left(d_{0r}+d_{1r}+d_{2r}\right)\mathbf{I}$.

_Example:_
```xml
<diffusivity name="Diffusivity" type="diff-ref-iso">
  <phi0>0.2</phi0>
  <free_diff>0.005</free_diff>
  <diff0>0.001</diff0>
  <diff1>0.005</diff1>
  <diff2>0.002</diff2>
  <M>1.5</M>
  <alpha>2</alpha>
</diffusivity>
```
