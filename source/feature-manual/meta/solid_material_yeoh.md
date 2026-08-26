This material implements a Yeoh material, as presented online (https://en.wikipedia.org/wiki/Yeoh_hyperelastic_model). The material formulation is selected by setting the type attribute to `Yeoh`.

The strain-energy density function for this material combines a neo-Hookean matrix with a Fung-type exponential term, and is defined as follows. 

\[
\Psi=\sum_{i=1}^{6}c_{i}\left(\tilde{I}_{1}-3\right)^{i}
\]

_Example:_
```xml
<material id="1" name="material1" type="Yeoh">
  <k>100</k>
  <c1>0.75</c0>
  <c1>-0.04</c1>
  <c2>0.08</c2>
</material>
```
