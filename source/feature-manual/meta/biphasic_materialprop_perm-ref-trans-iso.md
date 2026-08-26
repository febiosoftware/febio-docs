The material type for a biphasic material with strain-dependent permeability which is transversely isotropic in the reference configuration is `perm-ref-trans-iso`.

This material uses a strain-dependent permeability tensor that accommodates strain-induced anisotropy:

\[
\begin{aligned}\mathbf{k} & =k_{0r}\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha_{0}}e^{M_{^{0}}\left(J^{2}-1\right)/2}\mathbf{I}\\
 & +\left(\frac{k_{1r}^{T}}{J^{2}}\left(\mathbf{b}-\mathbf{m}\right)+\frac{k_{2r}^{T}}{2J^{4}}\left[2\mathbf{b}^{2}-\left(\mathbf{m}\cdot\mathbf{b}+\mathbf{b}\cdot\mathbf{m}\right)\right]\right)\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha_{T}}e^{M_{T}\left(J^{2}-1\right)/2}\\
 & +\left(\frac{1}{J^{2}}k_{1r}^{A}\mathbf{m}+\frac{1}{2J^{4}}k_{2r}^{A}\left(\mathbf{m}\cdot\mathbf{b}+\mathbf{b}\cdot\mathbf{m}\right)\right)\left(\frac{J-\varphi_{r}^{s}}{1-\varphi_{0}}\right)^{\alpha_{A}}e^{M_{A}\left(J^{2}-1\right)/2}
\end{aligned}
\]

where $J$ is the Jacobian of the deformation, i.e. $J=\det\mathbf{F}$ where $\mathbf{F}$ is the deformation gradient, and $\mathbf{b}=\mathbf{F}\cdot\mathbf{F}^{T}$ is the left Cauchy-Green tensor. $\mathbf{m}$ is a second order tensor representing the spatial structural tensor describing the axial direction, given by

\[
\mathbf{m}=\mathbf{F}\cdot\left(\mathbf{V}\otimes\mathbf{V}\right)\cdot\mathbf{F}^{T}\,,
\]

where $\mathbf{V}$ is a unit vector along the axial direction. Here, $\varphi_{r}^{s}$ is the referential solid volume fraction in the current configuration and $\varphi_{0}=\varphi_{r}^{s}\left(0\right)$ is its value in the reference configuration. Note that the permeability in the reference state ($\mathbf{F}=\mathbf{I}$) is given by,

\[
\mathbf{k_{|F=I}}=\left(k_{0r}+k_{1r}^{T}+k_{2r}^{T}\right)\mathbf{I}+\left(k_{1r}^{A}-k_{1r}^{T}+k_{2r}^{A}-k_{2r}^{T}\right)\left(\mathbf{V}\otimes\mathbf{V}\right)
\]

_Example:_
```xml
<permeability name="Permeability" type="perm-ref-trans-iso">
  <perm0>0.002</perm0>
  <perm1A>0.01</perm1A>
  <perm2A>0.01</perm2A>
  <perm1T>0.001</perm1T>
  <perm2T>0.05</perm2T>
  <M0>1.0</M0>
  <MA>0.5</MA>
  <MT>1.5</MT>
  <alpha0>1.0</alpha0>
  <alphaA>0.5</alphaA>
  <alphaT>2.0</alphaT>
</permeability>
```
