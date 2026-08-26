The `sliding-biphasic` implementation for sliding interfaces can deal with biphasic contact surfaces (including biphasic-on-biphasic, biphasic-on-elastic, biphasic-on-rigid) [^1] [^2]. It allows for the possibility to track fluid flow across the contact interface. In other words, fluid can flow from one side of the contact interface to the other when both contact surfaces are biphasic. 

Most of the parameters are identical to the [sliding-elastic](solid_surfaceinteraction_sliding-elastic.md) contact interface.

In order to model fluid flow across the interface, the user must define an additional parameter `pressure_penalty`:

```
<pressure_penalty>1.0</pressure_penalty>
```

In the same way that the penalty parameter controls the contact tractions, this parameter controls the penalty value that is used to calculate the Lagrange multipliers for the pressure constraint. 

If the `laugon` flag is set, the augmented Lagrangian method is used to enforce the pressure constraint. And if the `auto_penalty` flag is defined (which is the recommended approach), an initial guess for the pressure penalty is calculated automatically using the following formula: 

\[
\varepsilon_{p}=\frac{kA}{V},
\]

where $A$ is the element's area, $V$ is the element's volume and $k$ is a measure of the permeability which is defined as one third of the trace of the material's initial permeability tensor.

When either contact surface is biphasic, the surface outside the contact area(s) is automatically set to free-draining conditions (equivalent to setting the fluid pressure to zero).

As detailed in [^2] and the [FEBio Theory Manual](https://febio.org/knowledgebase/), the sliding-biphasic contact algorithm can include frictional contact. The effective friction coefficient $\mu_{\text{eff}}$ in this frictional contact algorithm depends on the temporally evolving local fluid load support (the ratio of fluid pressure $p$ to the normal component of the mixture contact traction $t_{n}$), according to

\[
\mu_{\text{eff}}=\mu_{\text{eq}}\left(1+\left(1-\varphi\right)\frac{p}{t_{n}}\right)\,.
\]

Recall that $t_{n}$ is negative whereas p is positive in compression. Here, $\mu_{\text{eq}}$ (fric_coeff) is the friction coefficient in the limit when the fluid load support has reduced to zero, and $\varphi$ (contact_frac) is the fraction of the apparent contact area over which the solid matrix of the primary surface contacts that of the secondary surface. Thus, $1-\varphi$ is the fraction of the apparent contact area where fluid contacts fluid or solid. For perfectly smooth contact surfaces one may assume that $\varphi=\varphi_{1}^{s}\varphi_{2}^{s}$, where $\varphi_{1}^{s}$ and $\varphi_{2}^{s}$ are the solid area (or volume) fractions of the primary and secondary contact surfaces, respectively. For example, when both contact surfaces are non-porous ($\varphi_{1}^{s}=\varphi_{2}^{s}=1$), the effective friction coefficient reduces to $\mu_{\text{eff}}=\mu_{\text{eq}}$. 

When performing biphasic-on-rigid contact a two-pass analysis should not be used; the rigid surface should be the secondary surface.

[^1]: Ateshian, GA, Maas, SA, and Weiss, J.A., "Finite element algorithm for frictionless contact of porous permeable media under finite deformation and sliding", J. Biomech. Engn. 132, 6 (2010), pp. 1006-1019.

[^2]: Zimmerman, Brandon K, Maas, Steve A, Weiss, Jeffrey A, and Ateshian, Gerard A, "A Finite Element Algorithm for Large Deformation Biphasic Frictional Contact Between Porous-Permeable Hydrated Soft Tissues", J Biomech Eng 144, 2 (2022).