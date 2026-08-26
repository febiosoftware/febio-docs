This is a material used for modeling human lung tissue as described by Birzle[^1].

This model is derived from the following hyperelastic strain-energy function: 

\[
W=c\left(I_{1}-3\right)+\frac{c}{\beta}\left(I_{3}^{-\beta}-1\right)+c_{1}\left(I_{3}^{-\frac{1}{3}}I_{1}-3\right)^{d_{1}}+c_{3}\left(I_{3}^{\frac{1}{3}}-1\right)^{d_{3}},
\]

where $I_{1}$ and $I_{2}$ are the first and second invariants of the right Cauchy-Green deformation tensor $\mathbf{C}$,

\[
c=\frac{E}{4\left(1+\nu\right)},
\]

and

\[
\beta=\frac{\nu}{1-2\nu}.
\]

_Example:_
```xml
<material id="1" type="lung">
  <density>1</density>
  <E>1913.7</E>
  <v>0.3413</v>
  <c1>278.2</c1>
  <c3>5.766</c3>
  <d1>3</d1>
  <d3>6</d3>
</material>
```

[^1]: Birzle, Anna M., Martin, Christian, Uhlig, Stefan, and Wall, Wolfgang A., "A coupled approach for identification of nonlinear and compressible material models for soft tissue based on different experime…", Journal of the Mechanical Behavior of Biomedical Materials 94 (2019), pp. 126--143.