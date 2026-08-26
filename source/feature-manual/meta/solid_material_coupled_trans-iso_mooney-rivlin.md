This material describes a transversely isotropic Mooney-Rivlin material using a fully-coupled formulation. It is defined through the `coupled trans-iso Mooney-Rivlin` material type.

The strain-energy function for this constitutive model is defined by

\[
W=c_{1}\left(I_{1}-3\right)+c_{2}\left(I_{2}-3\right)-2\left(c_{1}+2c_{2}\right)\ln J+F\left(\lambda\right)+U\left(J\right)
\]

The first three terms define the coupled Mooney-Rivlin matrix response. The third term is the fiber response which is a function of the fiber stretch $\lambda$ and is defined as in [^1]. For U, the following form is chosen in FEBio.

\[
U\left(J\right)=\frac{1}{2}k\left(\ln J\right)^{2}
\]

where $J=\det\mathbf{F}$ is the Jacobian of the deformation.

_Example:_
```xml
<material id="1" type="coupled trans-iso Mooney-Rivlin">
  <c1>1</c1>
  <c2>0.1</c2>
  <c3>1</c3>
  <c4>1</c4>
  <c5>1.34</c5>
  <lam_max>1.3</lam_max>
  <k>100</k>
</material>
```

[^1]: Weiss, J.A., Maker, B.N., and Govindjee, S., "Finite element implementation of incompressible, transversely isotropic hyperelasticity", Computer Methods in Applications of Mechanics and Engineering 135 (1996), pp. 107-128.