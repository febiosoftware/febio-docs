This material describes a coupled, transversely isotropic material that will conform to a particular Poisson's ratio when stretched along the fiber direction [^1].

The strain energy function for this constitutive model is a three part expression:

\[
W=W_{\text{fiber}}+W_{\text{matrix}}+W_{\text{vol}},
\]

where:

\[
\begin{aligned}W_{\text{fiber}} & =\frac{1}{2}\frac{c_{1}}{c_{2}}\left(e^{c_{2}\left({\lambda-1}\right)^{2}-1}\right),\\
W_{\text{matrix}} & =\frac{\mu}{2}\left(I_{1}-3\right)-\mu\ln\left(\sqrt{I_{3}}\right),\\
W_{\text{vol}} & =\frac{\kappa}{2}\left(\ln\left(\frac{I_{5}-I_{1}I_{4}+I_{2}}{I_{4}^{2(m-v_{0})}e^{-4m\left(\lambda-1\right)}}\right)\right)^{2}.
\end{aligned}
\]

In the equations above, $\lambda$ is the stretch ratio of the material along the fiber direction. The desired Poisson's ratio must first be selected based on available data for uniaxial tension along the fiber direction. The function with which to fit the Poisson's ratio data is:

\[
v=-\frac{\lambda^{m-v_{0}}e^{-m\left(\lambda-1\right)}-1}{\lambda-1}\,.
\]

The volumetric penalty coefficient $\kappa$ must be selected to be large enough to enforce the Poisson's function above. If this material is to be used in a biphasic representation, $\kappa$ must be selected based on experimental stress-relaxation data, since $\kappa$ has an effect on the biphasic behavior of the material. Once $\kappa$, $v_{0}$, and $m$ are chosen, $c_{\mathrm{1}}$, $c_{\mathrm{2}}$ and $\mu$ should be selected by fitting the stress-strain behavior of the material to experimental data. The Cauchy stress of the material is given by:

\[
\boldsymbol{\sigma}=\frac{2}{J}\left(\left(W_{1}+I_{1}W_{2}\right)\mathbf{B}-W_{2}\mathbf{B}^{2}+W_{3}\left(I_{3}\mathbf{1}\right)+W_{4}I_{4}\left(\mathbf{a}\otimes\mathbf{a}\right)+W_{5}I_{4}\left(\mathbf{a}\otimes\mathbf{a}\cdot\mathbf{B}+\mathbf{B}\cdot\mathbf{a}\otimes\mathbf{a}\right)\right)
\]

where $J$ is the jacobian of the deformation gradient $\mathbf{F}$, $\mathbf{B}=\mathbf{F}\cdot\mathbf{F}^{T}$ is the left Cauchy-Green deformation tensor, $\mathbf{1}$ is the $3\times3$ identity tensor, $\mathbf{a}$ is the fiber orientation vector in the deformed configuration.

_Example:_
```xml
<material id="1" name="Material1" type="PRLig">
  <c1>90</c1>
  <c2>160</c2>
  <mu>0.025</mu>
  <v0>5.85</v0>
  <m>-100</m>
  <k>1.55</k>
</material>
```

[^1]: Swedberg, A.M., Reese, S.P., Maas, S.A., Ellis, B. J., and Weiss, J.A., "Continuum description of the Poisson's ratio of ligament and tendon under finite deformation.", Journal of Biomechanics 47, 12 (2014), pp. 3201-3209.