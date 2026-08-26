The material type for a user-defined CDF is `CDF user`.

For this material the CDF $F\left(\Xi\right)$ is specified by the user. It can be a constant, linear ramp, mathematical expression, a series of points, or a step function. It is the user's responsibility to ensure that the function rises monotonically from 0 to 1 and does not exceed unity.

_Example:_
```xml
<damage type="CDF user">
  <cdf type="point">
    <interpolate>control points</interpolate>
    <extend>constant</extend>
    <points>
      <pt>0,0</pt>
      <pt>0.49,0</pt>
	  <pt>0.5,0</pt>
      <pt>0.99,0</pt>
      <pt>1.01,1</pt>
      <pt>1.49,1</pt>
      <pt>1.5,1</pt>
      <pt>2.5,1</pt>
    </points>
  </cdf>
</damage>