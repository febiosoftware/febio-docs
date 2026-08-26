The material type for transversely isotropic Mooney-Rivlin materials is `trans iso Mooney-Rivlin`.

This constitutive model can be used to represent a material that has a single preferred fiber direction and was developed for application to biological soft tissues [#Puso98, #Quapp98, #Weiss96]. It can be used to model tissues such as tendons, ligaments and muscle. The elastic response of the tissue is assumed to arise from the resistance of the fiber family and an isotropic matrix. It is assumed that the uncoupled strain energy function can be written as follows:

\[
\Psi=F_{1}\left(\tilde{I}_{1},\tilde{I}_{2}\right)+F_{2}\left(\tilde{\lambda}\right)+\frac{K}{2}\left[\ln\left(J\right)\right]^{2}.
\]

Here $\tilde{I}_{1}$ and $\tilde{I}_{2}$ are the first and second invariants of the deviatoric version of the right Cauchy Green deformation tensor $\mathbf{\tilde{C}}$ and $\tilde{\lambda}$ is the deviatoric part of the stretch along the fiber direction $(\tilde{\lambda}^{2}=\mathbf{a}_{0}\cdot\mathbf{\tilde{C}}\cdot\mathbf{a}_{0}$, where $\mathbf{a}_{0}$ is the initial fiber direction), and $J=\det\left(\mathbf{F}\right)$ is the Jacobian of the deformation (volume ratio). The function $F_{1}$ represents the material response of the isotropic ground substance matrix and is the same as the Mooney-Rivlin form specified above, while $F_{2}$ represents the contribution from the fiber family. The strain energy of the fiber family is as follows:

\[
F_{2}\left(\tilde{\lambda}\right)=\begin{cases}
0 & \tilde{\lambda}\leqslant1\\
C_{3}\left(e^{-C_{4}}\left(\Ei\left(C_{4}\tilde{\lambda}\right)-\Ei\left(C_{4}\right)\right)-\ln\tilde{\lambda}\right) & 1<\tilde{\lambda}<\lambda_{m}\\
C_{5}\left(\tilde{\lambda}-1\right)+C_{6}\ln\tilde{\lambda} & \tilde{\lambda}\geqslant\lambda_{m}
\end{cases}\,
\]

where $\Ei\left(\cdot\right)$ is the exponential integral function. The resulting fiber stress is evaluated from

\[
\tilde{\lambda}\frac{\partial F_{2}}{\partial\tilde{\lambda}}=\begin{cases}
0 & \tilde{\lambda}\leqslant1\\
C_{3}\left(e^{C_{4}\left(\tilde{\lambda}-1\right)}-1\right) & 1<\tilde{\lambda}<\lambda_{m}\\
C_{5}\tilde{\lambda}+C_{6} & \tilde{\lambda}\geqslant\lambda_{m}
\end{cases}\,.
\]

Here, $C_{1}$ and $C_{2}$ are the Mooney-Rivlin material coefficients, lam_max ($\lambda_{m}$) is the stretch at which the fibers are straightened, $C_{3}$ scales the exponential stresses, $C_{4}$ is the rate of uncrimping of the fibers, and $C_{5}$ is the modulus of the straightened fibers. $C_{6}$ is determined from the requirement that the stress is continuous at $\lambda_{m}$.

This material model uses a three-field element formulation, interpolating displacements as linear field variables and pressure and volume ratio as piecewise constant on each element [#Simo91].

_Example:_

This example defines a transversely isotropic material with a Mooney-Rivlin basis. It defines a homogeneous fiber direction and uses the active fiber contraction feature.
```xml
<material id="3" type="trans iso Mooney-Rivlin">
  <c1>13.85</c1>
  <c2>0.0</c2>
  <c3>2.07</c3>
  <c4>61.44</c4>
  <c5>640.7</c5>
  <k>100.0</k>
  <lam_max>1.03</lam_max>
  <fiber type="vector">1,0,0</fiber>
</material>
```
