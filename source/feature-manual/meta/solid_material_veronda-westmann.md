The material type for incompressible Veronda-Westmann materials is `Veronda-Westmann` [^1].

This model is similar to the Mooney-Rivlin model in that it also uses an uncoupled deviatoric dilatational strain energy:

\[
\Psi=C_{1}\left[e^{\left(C_{2}\left(\tilde{I}_{1}-3\right)\right)}-1\right]-\frac{C_{1}C_{2}}{2}\left(\tilde{I}_{2}-3\right)+U\left(J\right)\,.
\]

The dilatational term is identical to the one used in the Mooney-Rivlin model. This model can be used to describe certain types of biological materials that display exponential stiffening with increasing strain. It has been used to describe the response of skin tissue [^1].

_Example:_
```xml
<material id="2" type="Veronda-Westmann">
  <c1>1000.0</c1>
  <c2>2000.0</c2>
  <k>1000</k>
</material>
```

[^1]: Veronda, D.R. and Westmann, R.A., "Mechanical Characterization of Skin - Finite Deformations", J. Biomechanics Vol. 3 (1970), pp. 111-124.
