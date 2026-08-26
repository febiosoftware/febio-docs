The material type for constant orthotropic diffusivity materials is `diff-const-ortho`.

When the permeability is orhotropic,

\[
\mathbf{d}=\sum\limits_{a=1}^{3}d^{a}\mathbf{V}_{a}\otimes\mathbf{V}_{a}
\]

where $\mathbf{V}_{a}$ are orthonormal vectors normal to the planes of symmetry. For this material model, $d^{a}$'s are constant. Therefore this model should be used only when strains are small. Note that the user must specify $d^{a}\leqslant d_{0}$, since a solute cannot diffuse through the biphasic-solute mixture faster than in free solution.

_Example:_
```xml
<diffusivity name="Permeability" type="diff-const-ortho">
  <free_diff>0.005</free_diff >
  <diff>0.002,0.001,0.003</diff>
</diffusivity>
```