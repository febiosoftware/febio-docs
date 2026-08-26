The material type for constant isotropic permeability is \perm-const-iso.

This isotropic material model uses the biphasic theory for describing the time-dependent material behavior of materials that consist of both a solid and fluid phase [^1].

When the permeability is isotropic,

\[
\mathbf{k}=k\,\mathbf{I}
\]

For this material model, $k$ is constant. Generally, this assumption is only reasonable when strains are small.

_Example:_

```xml
<permeability name="Permeability" type="perm-const-iso">
  <perm>0.001</perm>
</permeability>
```

[^1]: Mow, V.C., Kuei, S.C., Lai, W.M., and Armstrong, C.G., "Biphasic creep and stress relaxation of articular cartilage in compression: Theory and experiments", J. Biomech. Eng. 102 (1980), pp. 73-84.