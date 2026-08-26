The material type for constant isotropic diffusivity materials is `diff-const-iso`.

When the permeability is isotropic,

\[
\mathbf{d}=d\,\mathbf{I}
\]

For this material model, $d$ is constant. This assumption is only true when strains are small. Note that the user must specify $d\leqslant d_{0}$, since a solute cannot diffuse through the biphasic-solute mixture faster than in free solution.

_Example:_
```xml
<diffusivity name="Permeability" type="diff-const-iso">
  <free_diff>1e-9</ free_diff >
  <diff>0.5e-9</diff>
</diffusivity>
```
