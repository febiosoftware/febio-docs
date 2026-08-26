The scheme type for the trapezoidal integration rule is `fibers-2d-trapezoidal` for unconstrained and uncoupled continuous fiber distributions. This integration rule should only be used with 2D fiber density distributions. This scheme discretizes the unit circle into a set of $N$ circular arcs of identical lengths. The unit normal $\mathbf{n}$ passes through the centroid of each arc element. The integration is performed as a summation over N. For each direction $\mathbf{n}$ the stress is evaluated only if the fiber bundle is in tension along that direction.

The parameter `nth` may be any number greater than 0. Odd values for `nth` produce more accurate results than even values.

_Example:_
```xml
<scheme type="fibers-2d-trapezoidal">
  <nth>31</nth>
</scheme>
```
