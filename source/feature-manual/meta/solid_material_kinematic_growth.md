Kinematic growth, based on the framework first proposed in [^1], uses the multiplicative decomposition of the deformation gradient into

\[
\mathbf{F}=\mathbf{F}^{e}\cdot\mathbf{F}^{g}\,,
\]

where $\mathbf{F}^{e}$ represents the elastic deformation and $\mathbf{F}^{g}$ represents the growth. The related Jacobians are

\[
$J^{e}=\det\mathbf{F}^{e}\quad J^{g}=\det\mathbf{F}^{g}\,.
\]

A constitutive model for the growth tensor was provided by [^2],

\[
\mathbf{F}^{g}=\vartheta^{\text{iso}}\mathbf{I}+\left(\vartheta^{\text{ani}}-1\right)\mathbf{n}_{r}\otimes\mathbf{n}_{r}
\]

where $\mathbf{n}_{r}$ is the referential unit vector for a fiber direction (or normal to an area), $\vartheta^{\text{iso}}$ represents isotropic growth, and $\vartheta^{\text{ani}}$ represents anisotropic growth.

For volume growth, let $\vartheta^{\text{iso}}=\vartheta^{g}$ and $\vartheta^{\text{ani}}=1$, where $\vartheta^{g}$ is called the growth multiplier in FEBio, which is typically prescribed using a loadcurve. For area growth in the plane transverse to the normal direction $\mathbf{n}$, let $\vartheta^{\text{iso}}=\sqrt{\vartheta^{g}}$ and $\vartheta^{\text{ani}}=2-\sqrt{\vartheta^{g}}$. Finally, for fiber growth, let $\vartheta^{\text{iso}}=1$ and $\vartheta^{\text{ani}}=\vartheta^{g}$. For general growth the user specifies the desired values of $\vartheta^{\text{iso}}$ and $\vartheta^{\text{ani}}$.

Internally, the calculations within FEBio require the evaluation of the inverse of $\mathbf{F}^{g}$, which is generally given by

\[
\left(\mathbf{F}^{g}\right)^{-1}=\frac{1}{\vartheta^{\text{iso}}+\vartheta^{\text{ani}}-1}\left(\left(1+\frac{\vartheta^{\text{ani}}-1}{\vartheta^{\text{iso}}}\right)\mathbf{I}-\frac{\vartheta^{\text{ani}}-1}{\vartheta^{\text{iso}}}\mathbf{n}_{r}\otimes\mathbf{n}_{r}\right)
\]

The mass density of a growing material is evaluated from $\rho=\rho_{r}/J$ where $\rho_{r}$ is the (invariant) referential mass density of the growing solid (when there is neither growth nor deformation) and $J=\det\mathbf{F}=\det\mathbf{F}^{e}\det\mathbf{F}^{g}\equiv J^{e}J^{g}$. It follows that the mass density change produced only by the growth is $\rho J^{e}\equiv\rho_{rg}=\rho_{r}/J^{g}$, thus $J^{g}=\det\mathbf{F}^{g}$ may be used to evaluate the evolving solid mass density $\rho_{rg}$ due only to growth. From the general expression for $\mathbf{F}^{g}$ above it follows that

\[
J^{g}=\det\mathbf{F}^{g}=\left(\vartheta^{\text{iso}}\right)^{2}\left(\vartheta^{\text{iso}}+\vartheta^{\text{ani}}-1\right)
\]

[^1]: Rodriguez, E K, Hoger, A, and McCulloch, A D, "Stress-dependent finite growth in soft elastic tissues", J Biomech 27, 4 (1994), pp. 455-67.

[^2]: Menzel, Andreas and Kuhl, Ellen, "Frontiers in growth and remodeling", Mech Res Commun 42 (2012), pp. 1-14.