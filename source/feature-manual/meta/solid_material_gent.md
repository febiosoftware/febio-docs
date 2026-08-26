The uncoupled Gent material is defined using the `Gent` type string.

The strain energy of this material is defined via an uncoupled formulation, 

\[
\Psi_{r}=\tilde{\Psi}_{r}\left(\tilde{\mathbf{C}}\right)+U\left(J\right)
\]

Here, the deviatoric strain energy is given by,

\[
\tilde{\Psi}=-\frac{\mu J_{m}}{2}\ln\left(1-\frac{\tilde{I}_{1}-3}{J_{m}}\right)
\]

_Example:_
```xml
<material id="2" type="Gent">
  <G>3.14</G>
  <Jm>1.5</Jm>
  <k>1e5</k>
</material>
```
 