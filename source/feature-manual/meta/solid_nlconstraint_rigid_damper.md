The `rigid damper` applies a linear damper that connects two rigid bodies $a$ and $b$ at arbitrary points (not necessarily nodes).

_Example:_
```xml
<rigid_connector type="rigid damper">
  <body_a>1</body_a>
  <body_b>2</body_b>
  <insertion_a>0,0,1</insertion_a>
  <insertion_b>0,0,3</insertion_b>
  <c>1e-7</c>
</rigid_connector>
```