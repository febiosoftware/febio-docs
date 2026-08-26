The material type for Holmes-Mow permeability is `perm-Holmes-Mow`.

This isotropic material is similar to the constant isotropic permeability material described above, except that it uses a strain-dependent permeability tensor [^1]:

\[
\mathbf{k}=k\left(J\right)\mathbf{I},
\]

where,

\[
k\left(J\right)=k_{0}\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha}e^{\frac{1}{2}M\left(J^{2}-1\right)}\,,
\]

and $J$ is the Jacobian of the deformation, i.e. $J=\det\mathbf{F}$ where $\mathbf{F}$ is the deformation gradient. Here, $\varphi_{r}^{s}$ is the referential solid volume fraction in the current configuration and $\varphi_{0}=\varphi_{r}^{s}\left(0\right)$ is its value in the reference configuration.

_Example:_

This example defines a permeability material of the Holmes-Mow type.

```xml
<permeability type="perm-Holmes-Mow">
  <perm>0.001</perm>
  <M>1.5</M>
  <alpha>2</alpha>
</permeability>
```

[^1]: Holmes, M. H. and Mow, V. C., "The nonlinear characteristics of soft gels and hydrated connective tissues in ultrafiltration", J Biomech 23, 11 (1990), pp. 1145-56.