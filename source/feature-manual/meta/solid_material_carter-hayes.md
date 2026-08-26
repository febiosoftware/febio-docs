This model describes an unconstrained neo-Hookean material whose Young's modulus is a power-law function of the referential apparent density $\rho_{r}^{\sigma}$ of a solid-bound molecule. It is derived from the following hyperelastic strain-energy function: 

\[
\Psi_{r}=\frac{E_{Y}}{2\left(1+\nu\right)}\left[\frac{1}{2}\left(tr\mathbf{C}-3\right)-\ln J+\frac{\nu}{1-2\nu}\left(\ln J\right)^{2}\right].
\]

Here, $\mathbf{C}$ is the right Cauchy-Green deformation tensor and $J$ is the determinant of the deformation gradient tensor.

Young's modulus depends on $\rho_{r}^{\sigma}$ according to a power law [^1] [^2], $E_{Y}=E_{0}\left(\frac{\rho_{r}^{\sigma}}{\rho_{0}}\right)^{\gamma}\,$.This type of material references a solid-bound molecule that belongs to a multiphasic mixture. Therefore this material may only be used as the solid (or a component of the solid) in a multiphasic mixture. The solid-bound molecule must be defined in the `Globals` section and must be included in the multiphasic mixture using a `solid_bound` tag. The parameter `sbm` must refer to the global index of that solid-bound molecule. The value of $\rho_{r}^{\sigma}$ is specified within the `solid_bound` tag. If a chemical reaction is defined within that multiphasic mixture that alters the value of $\rho_{r}^{\sigma}$, lower and upper bounds may be specified for this referential density within the `solid_bound` tag to prevent $E_{Y}$ from reducing to zero or achieving excessively elevated values.

_Example:_
```xml
<material id="1" name="solid matrix" type="multiphasic">
  <phi0>0</phi0>
  <solid_bound sbm="1">
    <rho0>1</rho0>
    <rhomin>0.1</rhomin>
    <rhomax>5</rhomax>
  </solid_bound>
  <fixed_charge_density>0</fixed_charge_density>
  <solid type="Carter-Hayes">
    <sbm>1</sbm>
    <E0>10000</E0>
    <rho0>1</rho0>
    <gamma>2.0</gamma>
    <v>0</v>
  </solid>
  <permeability type="perm-const-iso">
    <perm>1</perm>
  </permeability>
  <osmotic_coefficient type="osm-coef-const">
    <osmcoef>1</osmcoef>
  </osmotic_coefficient>
  <reaction name="solid remodeling" type="mass-action-forward">
    <Vbar>0</Vbar>
    <vP sbm="1">1</vP>
    <forward_rate type="Huiskes reaction rate">
      <B>1</B>
      <psi0>0.01</psi0>
    </forward_rate>
  </reaction>
</material>
```

[^1]: Carter, D R and Hayes, W C, "Bone compressive strength: the influence of density and strain rate", Science 194, 4270 (1976), pp. 1174-6.

[^2]: Carter, D R and Hayes, W C, "The compressive behavior of bone as a two-phase porous structure", J Bone Joint Surg Am 59, 7 (1977), pp. 954-62.