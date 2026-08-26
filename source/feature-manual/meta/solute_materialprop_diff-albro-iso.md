The material type for a porosity and concentration-dependent diffusivity which is isotropic is `diff-Albro-iso`.

This material uses a porosity and concentration-dependent diffusivity tensor that remains isotropic with deformation:

\[
\mathbf{d}=d_{0}\exp\left(-\alpha_{D}\frac{1-\varphi^{w}}{\varphi^{w}}-\frac{c}{c_{D}}\right)\mathbf{I},
\]

where $c_{D}^{-1}=1/c_{D}$ and the porosity $\varphi^{w}$ varies with deformation according to the kinematic constraint

\[
\varphi^{w}=1-\frac{\varphi_{r}^{s}}{J}\,.
\]

$J$ is the Jacobian of the deformation, i.e. $J=\det\mathbf{F}$ where $\mathbf{F}$ is the deformation gradient and $\varphi_{r}^{s}$ is the referential solid volume fraction. Here, $c$ represents the actual concentration of the solute whose diffusivity is given by $\mathbf{d}$. This constitutive relation is based on the experimental findings reported by Albro et al. [^1].

_Example:_
```xml
<solute sol="1">
  <diffusivity type="diff-Albro-iso">
    <free_diff>123e-6</free_diff>
    <alphad>18</alphad>
    <cdinv>0.0625</cdinv>
  </diffusivity>
  <solubility type="solub-const">
    <solub>1</solub>
  </solubility>
</solute>
```

[^1]: Albro, Michael B, Rajan, Vikram, Li, Roland, Hung, Clark T, and Ateshian, Gerard A, "Characterization of the Concentration-Dependence of Solute Diffusivity and Partitioning in a Model Dextran-Agarose Transport Sy…", Cell Mol Bioeng 2, 3 (2009), pp. 295-305.