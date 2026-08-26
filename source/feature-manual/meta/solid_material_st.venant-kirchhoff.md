The St.Venant-Kirchhoff material is a hyperelastic material that is analogous to a linear elastic material, but uses the Green-Lagrange strain instead of the infinitesimal strain tensor. The second Piola-Kirchhoff stress is defined as,

\[
    \mathbf{S} = \lambda \, \text{tr} \left( \mathbf{E}\right) \mathbf{I} + 2\mu\mathbf{E}
\]

Here, $\lambda$ and $\mu$ and related to the Young's modulus $E$ and Poisson's ratio $\nu$ as follows,

\[
    \lambda = \frac{E\,\nu}{\left(1+\nu\right)\left(1-2\nu\right)},\quad \mu=\frac{E}{2\left(1+\nu\right)}
\]

Note that this material can produce non-physical behavior under large deformations and it is better to use a [neo-Hookean](solid_material_neo-hookean.md) material.