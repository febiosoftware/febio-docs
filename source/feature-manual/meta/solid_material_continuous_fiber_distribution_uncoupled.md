The material type for an uncoupled continuous fiber distribution material is `continuous fiber distribution uncoupled`.

The `fiber` property defines the fiber constitutive relation and associated material properties. The `distribution` property defines the fiber density distribution function. The `scheme` property specifies the numerical integration scheme.

_Example:_
```xml
<material id="1" name="Material" type="uncoupled solid mixture">
  <solid type="Mooney-Rivlin">
    <density>1</density>
    <c1>1</c1>
    <c2>0.3</c2>
  </solid>
  <solid type="continuous fiber distribution uncoupled">
    <fibers type="fiber-exponential-power-law-uncoupled">
      <alpha>0</alpha>
      <beta>2</beta>
      <ksi>1</ksi>
    </fibers>
    <distribution type="spherical">
    </distribution>
    <scheme type="fibers-3d-gkt">
      <nph>7</nph>
      <nth>11</nth>
    </scheme>
  </solid>
</material>
```

