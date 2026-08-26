The material type for an unconstrained continuous fiber distribution material is `continuous fiber distribution`.

The `fibers` parameter defines the fiber constitutive relation and associated material properties. The `distribution` parameter defines the fiber density distribution function. The `scheme` parameter specifies the numerical integration scheme.

_Example:_
```xml
<material id="1" name="Material" type="solid mixture">
  <solid type="neo-Hookean">
    <density>1</density>
    <E>1</E>
    <v>0.3</v>
  </solid>
  <solid type="continuous fiber distribution">
    <fibers type="fiber-exponential-power-law">
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
