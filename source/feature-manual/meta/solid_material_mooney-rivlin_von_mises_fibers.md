The material type for a thin material where fiber orientation follows a von Mises distribution is `Mooney-Rivlin von Mises Fibers`. 

This constitutive model is designed for thin soft tissues. Fibers are multi-directional: they are distributed within the plane tangent to the tissue surface and they follow a unimodal distribution. It is a constitutive model that is suitable for ocular tissues (e.g. sclera and cornea) but can be used for other thin soft tissues. The proposed strain energy function is as follows:

\[
\Psi=F_{1}\left(\tilde{I}_{1},\tilde{I}_{2}\right)+\int\limits_{\theta_{P}-\pi/2}^{\theta_{P}+\pi/2}P\left(\theta\right)F_{2}\left(\tilde{\lambda}\left[\theta\right]\right)d\theta+\frac{K}{2}\left[\ln\left(J\right)\right]^{2},
\]

where $P$ is the 2D unimodal distribution function of the fibers which satisfies the normalization condition:

\[
\int\limits_{\theta_{P}-\pi/2}^{\theta_{P}+\pi/2}P\left(\theta\right)d\theta=1.
\]

$\theta_{P}$ is the preferred fiber orientation relative to a local coordinate system (parameter tp). The functions $F_{1}$ and $F_{2}$ are described in the [trans iso Mooney-Rivlin](solid_material_trans_iso_mooney-rivlin.md) model. The user can choose between 2 distribution functions using the parameter `vmc`.

### Semi-circular von Mises distribution (vmc = 1)
The semi-circular von Mises distribution is one of the simplest unimodal distribution in circular statistics. It can be expressed as [^1],

\[
P\left(\theta\right)=\frac{1}{\pi I_{0}\left(k_{f}\right)}\exp\left[k_{f}\cos\left(2\left(\theta-\theta_{p}\right)\right)\right],
\]

where $I_{0}$ is the modified Bessel function of the first kind (order 0), and $k_{f}$ is the fiber concentration factor. $k_{f}$ controls the amount of fibers that are concentrated along the orientation $\theta_{P}$ as illustrated in the figure below.

![FigMooneyRivlinVonMises](figs/FigMooneyRivlinVonMises.png)
/// figure-caption
Polar representation of the semi-circular von-Mises distribution describing in-plane collagen fiber alignment. In this case, the preferred fiber orientation $\theta_{P}$ is equal to zero degrees. When the fiber concentration factor k is equal to zero, the collagen fibers have an isotropic distribution in a plane tangent to the scleral wall. As $k$ increases, the collagen fibers align along the preferred fiber orientation $\theta_{P}$. Note that the distributions were plotted on a circle of unit one to ease visualization.
///

### Constrained von Mises Mixture Distribution (vmc = 2)

The semi-circular von Mises distribution is ideal for its simplicity but in some instance it fails to accurately describe the isotropic subpopulation of fibers present in thin soft tissues. An improved mathematical description is proposed here as a weighted mixture of the semi-circular uniform distribution and the semi-circular von Mises distribution. It can be expressed as [^2]:

\[
P\left(\theta\right)=\frac{1-\beta}{\pi}+\frac{\beta}{\pi I_{0}\left(k_{f}\right)}\exp\left[k_{f}\cos\left(2\left(\theta-\theta_{p}\right)\right)\right],
\]

where $\beta$ needs to be constrained for uniqueness and stability. $\beta$ is expressed as:

\[
\beta=\left(\frac{I_{1}\left(k_{f}\right)}{I_{0}\left(k_{f}\right)}\right)^{n},
\]

where $I_{1}$ is the modified Bessel function of the first kind (order 1), and n is an exponent to be determined experimentally (parameter var_n). n=2 has been found to be suitable for the sclera based on fiber distribution measurements using small angle light scattering.

### Note about Numerical Integration
All numerical integrations are performed using a 10-point Gaussian quadrature rule. The number of Gaussian integration points can be increased for numerical stability. This is controlled through the parameter gipt. We recommend to use at least gipt = 20 ($2\times 10$ integration points). Note that the more integration points are used, the slower the model will run. By increasing the number of integration points, one should observe convergence in the numerical accuracy. The parameter gipt is required to be a multiple of 10.

### Definition of the Fiber Plane
The user must specify two directions to define a local coordinate system of the plane in which the fibers lay. This can be done by defining two directions with the parameter `mat_axis`. The first direction (vector $\mathbf{a}$ of mat_axis) must be the reference direction used to define the angle tp ($\theta_{P}$). The second direction (vector $\mathbf{d}$ of mat_axis) can be any other direction in the plane of the fibers. Thus, a fiber at angle $\theta_{P}$ will be along the vector $\mathbf{v}=\cos\theta_{P}\mathbf{e}_{1}+\sin\theta_{P}\mathbf{e}_{2}$ where $\mathbf{e}_{1}=\mathbf{a}/\left\Vert \mathbf{a}\right\Vert$, $\mathbf{e}_{2}=\left(\mathbf{e}_{3}\times\mathbf{a}\right)/\left\Vert \mathbf{e}_{3}\times\mathbf{a}\right\Vert$, $\mathbf{e}_{3}=\left(\mathbf{a}\times\mathbf{d}\right)/\left\Vert \mathbf{a}\times\mathbf{d}\right\Vert$.

### Note on parameters kf and tp

The parameters `kf` and `tp` can be specified either in the `Material` section or in the `ElementData` section. With this second option the user can define different fiber characteristics for each element separately, which can be useful if fiber orientations or concentrations vary spatially. The parameter `mat_axis` can also be defined either in the `Material` section or in the `ElementData` section.

### Example
This example defines a thin soft tissue material where fibers are distributed according to a constrained von Mises mixture distribution.

```
<material id="1" name="Material 1" type="Mooney-Rivlin von Mises Fibers">
  <c1>10.0</c1>
  <c2>0.0</c2>
  <c3>50.0</c3>
  <c4>5.0</c4>
  <c5>1</c5>
  <lam_max>10</lam_max>
  <k>1000000.0</k>
  <kf>1</kf>
  <vmc>2</vmc>
  <var_n>2.0</var_n>
  <tp>0.0</tp>
  <gipt>40</gipt>
  <mat_axis type="local">4,1,3</mat_axis>
</material>
```

[^1]: Girard, M.J.A., Downs, J.C., and Burgoyne, C. F., "Peripapillary and posterior scleral mechanics - Part I: Development of an anisotropic hyperelastic constitutive model", J Biomech Eng 131, 5 (2009), pp. 051011.

[^2]: Gouget, C.L.M., Girard, M.J.A., and Ethier, C.R., "A constrained von Mises distribution to describe fiber organization in thin soft tissues", Biomechanics And Modeling in Mechanobiolgy 11, 3-4 (2012), pp. 475-482.