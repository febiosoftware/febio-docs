FEBio’s `fluid-solute` module models transport of dissolved species in a viscous fluid without a porous solid matrix. It couples fluid mechanics with convection–diffusion of solutes in a fully nonlinear, transient framework.

Core capabilities include:

* Navier–Stokes-based fluid flow (incompressible or compressible).
* Advection–diffusion transport of one or multiple solute species.
* Species-specific diffusivities and optional concentration dependence.
* Convection-dominated transport with stabilized finite element formulations.
* Chemical reaction kinetics between solutes (mass action–type reactions).
* Boundary conditions for velocity, pressure, concentration, and solute flux.
* Transient simulations capturing mixing, dispersion, and reactive transport.

This module is suited for modeling solute transport in free-flowing biological fluids, such as nutrient transport in blood or drug dispersion in fluid-filled domains.