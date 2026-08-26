The `rigid contractile` force applies an actuator force between arbitrary points (not necessarily nodes) on two rigid bodies $a$ and $b$.

The `f0` parameter represents the actuator force (positive for contraction). Optionally, it may be associated with a load curve.

_Example:_
```xml
<rigid_connector type="rigid contractile force">
  <body_a>1</body_a>
  <body_b>2</body_b>
  <insertion_a>0,0,1</insertion_a>
  <insertion_b>0,0,3</insertion_b>
  <f0 lc="1">1</f0>
</rigid_connector>
```