FEBio’s `multiphasic` module generalizes the biphasic-solute formulation to model mixtures composed of a deformable solid matrix, a fluid phase, and multiple interacting solute species with full electrochemical coupling. It is designed for charged, hydrated biological tissues and other complex porous media.

Core capabilities include:

* Large-deformation mixture theory with simultaneous solution of solid mechanics, fluid flow, and solute transport.
* Multiple solutes with independent diffusivities, valences, and convection–diffusion transport.
* Electroneutrality constraints and electric potential governed by ion distributions.
* Donnan equilibrium and fixed charge density to represent charged solid matrices (e.g., proteoglycans).
* Osmotic pressure and chemical potential contributions to stress and fluid flux.
* Concentration-, strain-, and field-dependent permeability and diffusivity.
* Reactive chemistry, including binding reactions and mass action kinetics.
* Comprehensive boundary conditions for displacement, pressure, concentration, electric potential, and fluxes.

The multiphasic module enables simulation of swelling tissues, ion transport in cartilage and intervertebral disc, electrochemical coupling, and other strongly coupled chemo-electro-mechanical phenomena in biomechanics.