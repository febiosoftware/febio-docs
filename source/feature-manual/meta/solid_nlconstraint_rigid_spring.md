The `rigid spring` applies a linear spring that connects two rigid bodies $a$ and $b$ at arbitrary points (not necessarily nodes).

If the `free_length` parameter is zero, then the initial length of the spring, as defined by the two insertion points, is taken as the free length. 

_Example:_
```xml
<rigid_connector type="rigid spring">
  <body_a>1</body_a>
  <body_b>2</body_b>
  <insertion_a>0,0,1</insertion_a>
  <insertion_b>0,0,3</insertion_b>
  <k>1</k>
</rigid_connector>
```