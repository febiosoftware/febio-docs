The material type for isotropic Hencky hyperelasticity [^1] is `isotropic Hencky`.

This material is an implementation of a hyperelastic constitutive material that reduces to the classical linear elastic material for small strains, but is objective for large deformations and rotations. The hyperelastic strain-energy function is given by:

\[
W=\frac{1}{2}\lambda\left(\tr\mathbf{H}\right)^{2}+\mu\mathbf{H}:\mathbf{H}
\]

Here, $\mathbf{H}$ is the right Hencky strain tensor and $\lambda$ and $\mu$ are the Lamé parameters, which are related to the more familiar Young's modulus E and Poisson's ratio $\nu$ as follows:

\[
\lambda=\frac{\nu E}{\left(1+\nu\right)\left(1-2\nu\right)},\mu=\frac{E}{2\left(1+\nu\right)}\,.
\]

The Cauchy stress for this material takes the form

\[
\boldsymbol{\sigma}=\frac{\lambda}{J}\left(\mathbf{I}:\mathbf{h}\right)\mathbf{I}+\frac{2\mu}{J}\mathbf{h}
\]

where $\mathbf{h}$ is the left Hencky strain tensor. In the limit of infinitesimal strains and rotations, $J\to1$ and $\mathbf{h}\to\boldsymbol{\varepsilon}$ where $\boldsymbol{\varepsilon}$ is the infinitesimal strain tensor.

It is often convenient to express the material properties using the bulk modulus K and shear modulus G. To convert to Young's modulus and Poisson's ratio, use the following formulas: 

\[
E=\frac{9KG}{3K+G},\quad\nu=\frac{3K-2G}{6K+2G}\,.
\]

_Example:_
```xml
<material id="1" type="isotropic Hencky">
  <E>1000.0</E>
  <v>0.45</v>
</material>
```

[^1]: Xiao, H and Chen, LS, "Hencky's elasticity model and linear stress-strain relations in isotropic finite hyperelasticity", Acta Mechanica 157, 1 (2002), pp. 51--60.