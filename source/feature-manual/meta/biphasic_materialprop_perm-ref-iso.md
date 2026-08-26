The material type for a biphasic material with strain-dependent permeability which is isotropic in the reference configuration is `perm-ref-iso`.

This material uses a strain-dependent permeability tensor that accommodates strain-induced anisotropy:

\[
\mathbf{k}=\left(k_{0r}\mathbf{I}+\frac{k_{1r}}{J^{2}}\mathbf{b}+\frac{k_{2r}}{J^{4}}\mathbf{b}^{2}\right)\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha}e^{M\left(J^{2}-1\right)/2},
\]

where $J$ is the Jacobian of the deformation, i.e. $J=\det\mathbf{F}$ where $\mathbf{F}$ is the deformation gradient, and $\mathbf{b}=\mathbf{F}\cdot\mathbf{F}^{T}$ is the left Cauchy-Green tensor. Here, $\varphi_{r}^{s}$ is the referential solid volume fraction in the current configuration and $\varphi_{0}=\varphi_{r}^{s}\left(0\right)$ is its value in the reference configuration. Note that the permeability in the reference state ($\mathbf{F}=\mathbf{I}$) is isotropic and given by $\mathbf{k}=\left(k_{0r}+k_{1r}+k_{2r}\right)\mathbf{I}$.

_Example:_
```xml
<permeability name="Permeability" type="perm-ref-iso">
  <perm0>0.001</perm0>
  <perm1>0.005</perm1>
  <perm2>0.002</perm2>
  <M>1.5</M>
  <alpha>2</alpha>
</permeability>
```