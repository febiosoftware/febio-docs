The material type for a natural Neo-Hookean material is `natural neo-Hookean`.

This model describes an unconstrained Neo-Hookean material using the natural strain tensor [^1]. It has a non-linear stress-strain behavior, but reduces to the classical linear elasticity model for small strains and small rotations. It is derived from the following hyperelastic strain-energy function:

\[
W=\frac{\kappa}{2}K_{1}^{2}+\mu K_{2}^{2},
\]

where $\kappa$ is the bulk modulus and $\mu$ is the shear modulus, 

\[
\kappa=\frac{E}{3\left(1-2\nu\right)}\,,\quad\mu=\frac{E}{2\left(1+\nu\right)}
\]

Here, $K_{1}$ and $K_{2}$ are the first and second invariants of the left natural (Hencky) strain tensor $\boldsymbol{\eta}=\ln\mathbf{V}$ where $\mathbf{V}$ is the left stretch tensor in the polar decomposition $\mathbf{F}=\mathbf{V}\cdot\mathbf{R}$.

This material model uses a standard displacement-based element formulation, so care must be taken when modeling materials with nearly-incompressible material behavior to avoid element locking. For this case, use the Mooney-Rivlin material described in Section [Mooney-Rivlin](solid_material_mooney-rivlin.md).

_Example:_
```xml
<material id="1" type="natural neo-Hookean">
  <E>200e3</E>
  <v>0.3</v>
</material>
```
[^1]: Criscione, John C, Humphrey, Jay D, Douglas, Andrew S, and Hunter, William C, "An invariant basis for natural strain which yields orthogonal stress response terms in isotropic hyperelasticity", J. Mech. Phys. Solids 48, 12 (2000), pp. 2445--2465.