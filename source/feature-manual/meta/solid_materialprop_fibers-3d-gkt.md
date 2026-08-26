The scheme type for the Gauss-Kronrod trapezoidal rule is `fibers-3d-gkt` for unconstrained and uncoupled continuous fiber distributions. This integration rule should only be used with 3D fiber density distributions. This scheme automatically limits the range of integration to fibers that are in tension [^1]. A Gauss-Kronrod quadrature rule is employed for integration across latitudes of the unit sphere. A trapezoidal rule is used for integration across longitudes.

The parameter `nph` must be one of the values 7, 11, 15, 19, 23 and 27. The parameter `nth` may be any number greater than 0. Odd values for `nth` produce more accurate results than even values. A recommended combination is nph=7 and nth=31. The total number of integration points is N=nph ×nth. Increasing values of N require increasing computational time.

_Example:_
```xml
<scheme type="fibers-3d-gkt">
  <nph>7</nph>
  <nth>31</nth>
</scheme>
```

[^1]: Hou, C and Ateshian, G.A., "A Gauss-Kronrod-Trapezoidal integration scheme for modeling biological tissues with continuous fiber distributions.", Computer Methods in Biomechanics and Biomedical Engineering 19, 8 (2016), pp. 883-893.