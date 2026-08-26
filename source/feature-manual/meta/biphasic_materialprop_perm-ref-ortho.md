The material type for a poroelastic material with strain-dependent permeability which is orthotropic in the reference configuration is `perm-ref-ortho`.

This material uses a strain-dependent permeability tensor that accommodates strain-induced anisotropy:

\[
\mathbf{k}=k_{0}\mathbf{I}+\sum\limits_{a=1}^{3}k_{1}^{a}\mathbf{m}_{a}+k_{2}^{a}\left(\mathbf{m}_{a}\cdot\mathbf{b}+\mathbf{b}\cdot\mathbf{m}_{a}\right)\,,
\]

\[
\begin{aligned}k_{0} & =k_{0r}\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha_{^{0}}}e^{M_{^{0}}\left(J^{2}-1\right)/2}\\
k_{1}^{a} & =\frac{k_{1r}^{a}}{J^{2}}\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha_{^{a}}}e^{M_{^{a}}\left(J^{2}-1\right)/2}\\
k_{2}^{a} & =\frac{k_{2r}^{a}}{2J^{4}}\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha_{^{a}}}e^{M_{a}\left(J^{2}-1\right)/2}
\end{aligned}
,\quad a=1,2,3\,.
\]

$J$ is the Jacobian of the deformation, i.e. $J=\det\mathbf{F}$ where $\mathbf{F}$ is the deformation gradient. $\mathbf{m}_{a}$ are second order tensors representing the spatial structural tensors describing the orthogonal planes of symmetry, given by

\[
\mathbf{m}_{a}=\mathbf{F}\cdot\left(\mathbf{V}_{a}\otimes\mathbf{V}_{a}\right)\cdot\mathbf{F}^{T},\quad a=1-3,
\]

where $\mathbf{V}_{a}$ are orthonormal vectors normal to the planes of symmetry. Here, $\varphi_{r}^{s}$ is the referential solid volume fraction in the current configuration and $\varphi_{0}=\varphi_{r}^{s}\left(0\right)$ is its value in the reference configuration. Note that the permeability in the reference state ($\mathbf{F}=\mathbf{I}$) is given by $\mathbf{k}=k_{0r}\mathbf{I}+\sum\limits_{a=1}^{3}\left(k_{1r}^{a}+k_{2r}^{a}\right)\mathbf{V}_{a}\otimes\mathbf{V}_{a}$.

_Example:_

```xml
<permeability name="Permeability" type="perm-ref-ortho">
  <perm0>0.001</perm0>
  <perm1>0.01, 0.02, 0.03</perm1>
  <perm2>0.001, 0.002, 0.003</perm2>
  <M0>0.5</M0>
  <M>1.5, 2.0, 2.5</M>
  <alpha0>1.5</alpha0>
  <alpha>2, 2.5, 3</alpha>
</permeability>
```

