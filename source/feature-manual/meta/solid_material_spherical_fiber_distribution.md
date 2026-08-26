The material type for a spherical (isotropic) continuous fiber distribution is `spherical fiber distribution`. Since fibers can only sustain tension, this material is not stable on its own. It must be combined with a stable compressible material that acts as a ground matrix, using a `solid mixture` container as described in Section [solid mixture](solid_material_solid_mixture.md).

The Cauchy stress for this fibrous material is given by [^1][^2][^3]:

\[
\boldsymbol{\sigma}=\int_{0}^{2\pi}\int_{0}^{\pi}H\left(I_{n}-1\right)\sigma_{n}\left(\mathbf{n}\right)\sin\varphi\,d\varphi\,d\theta\,.
\]

Here, $I_{n}=\lambda_{n}^{2}=\mathbf{N}\cdot\mathbf{C}\cdot\mathbf{N}$ is the square of the fiber stretch $\lambda_{n}$, $\mathbf{N}$ is the unit vector along the fiber direction, in the reference configuration, which in spherical angles is directed along $\left(\theta,\varphi\right)$, $\mathbf{n}=\mathbf{F}\cdot\mathbf{N}/\lambda_{n}$, and $H\left(.\right)$ is the unit step function that enforces the tension-only contribution.

The fiber stress is determined from a fiber strain energy function,

\[
\sigma_{n}=\frac{2I_{n}}{J}\frac{\partial\Psi}{\partial I_{n}}\mathbf{n}\otimes\mathbf{n}\,,
\]

where in this material, the fiber strain energy density is given by

\[
\Psi=\frac{\xi}{\alpha}\left(\exp\left[\alpha\left(I_{n}-1\right)^{\beta}\right]-1\right)\,,
\]

where $\xi>0$, $\alpha\geqslant0$, and $\beta\geqslant2$.

Note: In the limit when $\alpha\to0$, this expressions produces a power law,

\[
\lim\limits_{\alpha\to0}\Psi=\xi\left(I_{n}-1\right)^{\beta}
\]

Note: When $\beta>2$, the fiber modulus is zero at the strain origin ($I_{n}=1$). Therefore, use $\beta>2$ when a smooth transition in the stress is desired from compression to tension. 

_Example:_
```xml
<material id="1" type="solid mixture">
  <solid type="neo-Hookean">
    <E>1000.0</E>
    <v>0.45</v>
  </solid>
  <solid type="spherical fiber distribution">
    <ksi>10</ksi>
    <alpha>0</alpha>
    <beta>2.5</beta>
  </solid>
</material>
```

[^1]: Lanir, Y., "Constitutive equations for fibrous connective tissues", J Biomech 16, 1 (1983), pp. 1-12.

[^2]: Ateshian, G. A., "Anisotropy of fibrous tissues in relation to the distribution of tensed and buckled fibers", J Biomech Eng 129, 2 (2007), pp. 240-9.

[^3]: Ateshian, G. A., Rajan, V., Chahine, N. O., Canal, C. E., and Hung, C. T., "Modeling the matrix of articular cartilage using a continuous fiber angular distribution predicts many observed phenomena", J Biomech Eng 131, 6 (2009), pp. 061003.
