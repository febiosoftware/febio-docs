The material type for a user-defined bond recruitment function is `recruitment user`.

For this material the recruitment function $F\left(\Xi\right)$ is specified by the user. It can be a constant, linear ramp, mathematical expression, a series of points, or a step function. It is the user's responsibility to ensure that the function starts at 1 and rises monotonically.

_Example:_
```xml
<recruitment type="recruitment user">
  <function type="point">
    <interpolate>linear</interpolate>
    <extend>constant</extend>
    <points>
      <pt>0,1</pt>
      <pt>0.063,1</pt>
      <pt>0.13,1.8</pt>
    </points>
  </function>
</recruitment>
```
