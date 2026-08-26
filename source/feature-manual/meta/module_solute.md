FEBio’s `biphasic-solute` module extends the biphasic formulation to model transport of dissolved solutes within fluid-saturated porous materials. It couples solid deformation, fluid flow, and solute transport in a fully nonlinear, large-deformation framework.

Core capabilities include:

* Advection–diffusion of solutes in a deforming porous solid, with transport driven by fluid flow and concentration gradients.
* Multiple solute species with distinct diffusivities and valences.
* Concentration-dependent and strain-dependent diffusivity and permeability.
* Donnan equilibrium and fixed charge density effects for charged tissues.
* Osmotic pressure contributions to the mixture stress.
* Chemical reaction kinetics between solutes and/or solid-bound species.
* Boundary conditions for concentration, flux, and reactive exchange.
* Transient analyses capturing swelling, deswelling, and time-dependent solute redistribution.

These features make the biphasic-solute module suitable for modeling cartilage swelling, nutrient transport in tissues, drug delivery in hydrated materials, and other chemo-mechanical coupling problems in biomechanics.