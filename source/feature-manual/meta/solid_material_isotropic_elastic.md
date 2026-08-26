The material type for isotropic elasticity is `isotropic elastic`. 

This material is an implementation of a hyperelastic constitutive material that reduces to the classical linear elastic material for small strains, but is objective for large deformations and rotations. The hyperelastic strain-energy function is given by: 

\[
W=\frac{1}{2}\lambda\left(\tr\mathbf{E}\right)^{2}+\mu\mathbf{E}:\mathbf{E}.
\]

Here, $\mathbf{E}$ is the Euler-Lagrange strain tensor and $\lambda$ and $\mu$ are the Lamé parameters, which are related to the more familiar Young's modulus $E$ and Poisson's ratio $\nu$  as follows:

\[
\lambda=\frac{\nu E}{\left(1+\nu\right)\left(1-2\nu\right)},\mu=\frac{E}{2\left(1+\nu\right)}\,.
\]

It is often convenient to express the material properties using the bulk modulus $K$ and shear modulus $G$. To convert to Young's modulus and Poisson's ratio, use the following formulas: 

\[
E=\frac{9KG}{3K+G},\quad\nu=\frac{3K-2G}{6K+2G}\,.
\]

Note that although this material is objective, it is not advised to use this model for large strains since the behavior may be unphysical. For example, it can be shown that for a uniaxial tension the stress grows unbounded and the volume tends to zero for finite strains. Also for large strains, the Young's modulus and Poisson's ratio input values have little relationship to the actual material parameters. Therefore it is advisable to use this material only for small strains and/or large rotations. To represent isotropic elastic materials under large strain and rotation, it is best to use some of the other available nonlinear material models, such as the Holmes-Mow material in Section [Holmes-Mow](solid_material_holmes-mow.md), the neo-Hookean material in Section [neo-Hookean](solid_material_neo-hookean.md), or the unconstrained Ogden material in Section [Ogden-Unconstrained](solid_material_ogden_unconstrained.md).

Example:

<material id="1" type="isotropic elastic">

  <E>1000.0</E>

  <v>0.45</v>

</material>