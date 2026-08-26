The material type for transversely isotropic Veronda-Westmann materials is `trans iso Veronda-Westmann` [^1].

This uncoupled hyperelastic material differs from the Transversely Isotropic Mooney-Rivlin model in that it uses the Veronda-Westmann model for the isotropic matrix. The interpretation of the material parameters, except $C_{1}$ and $C_{2}$ is identical to this material model.

_Example:_

This example defines a transversely isotropic material model with a Veronda-Westmann basis. The fiber direction is implicitly implied as local.

```xml
<material id="3" type="trans iso Veronda-Westmann">
  <c1>13.85</c1>
  <c2>0.0</c2>
  <c3>2.07</c3>
  <c4>61.44</c4>
  <c5>640.7</c5>
  <lam_max>1.03</lam_max>
</material>
```

[^1]: Weiss, J.A., Gardiner, J.C., and C., Bonifasi-Lista, "Ligament material behavior is nonlinear, viscoelastic and rate-independent under shear loading", Journal of Biomechanics 35, 7 (2002), pp. 943-950.