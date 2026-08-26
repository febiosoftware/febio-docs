FEBio’s `biphasic` module simulates porous, fluid-saturated materials by coupling solid deformation with interstitial fluid flow. The formulation treats the solid matrix and pore fluid as coexisting continua, enforcing mass conservation and momentum balance for both phases.

Key capabilities include:

* Large-deformation biphasic theory suitable for soft biological tissues.
* Darcy-type fluid flow through a deforming porous solid, with isotropic or anisotropic permeability.
* Compressible or incompressible solid and fluid phases.
* Coupling to nonlinear elastic, viscoelastic, and hyperelastic solid material models.
* Boundary conditions for fluid pressure, fluid flux, and mixed (leakage) conditions.
* Time-dependent analyses capturing consolidation, stress relaxation, creep, and load-rate effects.

These features make FEBio’s biphasic framework well suited for simulating cartilage, intervertebral disc, hydrated soft tissues, and other poroelastic biological materials.