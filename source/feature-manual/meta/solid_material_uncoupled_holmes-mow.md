The material type for the uncoupled Holmes-Mow material is `uncoupled Holmes-Mow`.

This material model uncouples deviatoric and volumetric behaviors,

\[
\Psi_{r}=\tilde{\Psi}_{r}\left(\tilde{\mathbf{C}}\right)+U\left(J\right)
\]

The deviatoric strain-energy function is given by

\[
\tilde{\Psi}_{r}=\frac{1}{2}\frac{\mu}{\beta}\left(e^{\tilde{Q}}-1\right)
\]

where $\mu$ is the shear modulus and

\[
\tilde{Q}=\beta\left(\tilde{I}_{1}-3\right)
\]

where $\beta$ is the exponential stiffening coefficient.

_Example:_
```xml
<material id="1" name="Material1" type="uncoupled Holmes-Mow">
  <density>1</density>
  <mu>0.5</mu>
  <beta>2</beta>
  <k>5000</k>
</material>
```