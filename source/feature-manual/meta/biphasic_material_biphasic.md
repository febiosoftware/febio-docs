The material type for a biphasic material is `biphasic`.

The `solid` property encloses a description of the solid matrix constitutive relation and associated material properties. The solid must be an unconstrained materil. The `permeability` property defines the permeability constitutive relation and associated material properties. The parameter `phi0` must be greater than 0 (no solid) and less than 1 (no porosity). The volume fraction of fluid (also known as the porosity) in the reference configuration is given by $1-\varphi_{r}^{s}$. The fluid density $\rho_{T}^{w}$ specified in `fluid_density` and the solid density $\rho_{T}^{s}$ specified in `density` within the `solid` property are needed only when body forces are prescribed.

_Example:_
```xml
<material id="1" name="Biphasic tissue" type="biphasic">
  <solid name="Elasticity" type="neo-Hookean">
    <E>1.0</E>
    <v>0.3</v>
  </solid>
  <phi0>0.2</phi0>
  <permeability name="Permeability" type="perm-const-iso">
    ... (description of permeability material)
  </permeability>
</material>
```
The stabilization parameter $\tau$ can be used to reduced oscillations in the fluid pressure field produced under certain loading conditions, when the finite element mesh is relatively coarse in the vicinity of a free-draining boundary (a boundary on which the fluid pressure is set to zero). When this occurs it is best to refine the mesh (create thinner elements in the direction normal to the boundary) to overcome these oscillations. When mesh refinement is not feasible or practical, one may use a non-zero stabilization parameter $\tau$. FEBio uses an implementation based on the formulation of Aguilar et al. [^1]. In our adaptation of this formulation the parameter $\tau$ has units of time. Its value is best estimated by identifying the thickness h of elements on the free-draining boundary, the characteristic modulus $E$ of the solid matrix and hydraulic permeability $k$ in these elements. Then $\tau$ may be set approximately to $h^{2}/\left(E\cdot k\right)$.

[^1]: Aguilar, G, Gaspar, F, Lisbona, F, and Rodrigo, C24558811158, "Numerical stabilization of Biot's consolidation model by a perturbation on the flow equation", International journal for numerical methods in engineering 75, 11 (2008), pp. 1282--1300.